from __future__ import annotations

import xml.etree.ElementTree as ET
from pathlib import Path
from dataclasses import dataclass, field
from typing import Optional, List, Dict


@dataclass
class TableField:
    id: str
    allow_null: bool
    uuid: Optional[str] = None
    data_type: Optional[str] = None
    chinese_name: Optional[str] = None
    dictionary_type: Optional[str] = None
    description: Optional[str] = None
    public_type: Optional[str] = None
    comments: Optional[str] = None


@dataclass
class TableIndex:
    name: str
    global_index: bool
    flags: Optional[str] = None
    index_type_ex: Optional[str] = None
    fields: List[str] = field(default_factory=list)


@dataclass
class TableStructure:
    path: str
    file_name: str
    table_name: str
    chinese_name: str
    object_id: Optional[str] = None
    space: Optional[str] = None
    run_mode: Optional[str] = None
    has_history: bool = False
    data_storage_medium: Optional[str] = None
    index_space: Optional[str] = None
    history_space: Optional[str] = None
    history_index_space: Optional[str] = None
    archive_space: Optional[str] = None
    archive_index_space: Optional[str] = None
    fields: List[TableField] = field(default_factory=list)
    indexes: List[TableIndex] = field(default_factory=list)


class TableStructureParser:
    def __init__(self) -> None:
        self.standard_fields: Dict[str, Dict] = {}
        self.tablespace_relations: Dict[str, Dict] = {}

    def load_standard_fields(self, stdfield_path: str | Path) -> None:
        file_path = Path(stdfield_path)
        if not file_path.exists():
            return

        tree = ET.parse(file_path)
        root = tree.getroot()

        for item in root.findall(".//items"):
            name = item.attrib.get("name")
            if name:
                self.standard_fields[name] = {
                    "chineseName": item.attrib.get("chineseName"),
                    "dataType": item.attrib.get("dataType"),
                    "dictionaryType": item.attrib.get("dictionaryType"),
                    "description": item.attrib.get("description"),
                    "publicType": _standard_field_public_type(item),
                }

    def load_tablespace_relations(self, mdbobject_path: str | Path) -> None:
        file_path = Path(mdbobject_path)
        if not file_path.exists():
            return

        tree = ET.parse(file_path)
        root = tree.getroot()

        for relation in root.findall("relations"):
            main_space = relation.attrib.get("mainSpace")
            index_space = relation.attrib.get("indexSpace")

            if main_space:
                ts_prop = relation.find(".//value[@xsi:type='stock:TableSpaceRelationProperty']", namespaces={"xsi": "http://www.w3.org/2001/XMLSchema-instance"})
                if ts_prop is not None:
                    self.tablespace_relations[main_space] = {
                        "index_space": index_space,
                        "history_space": ts_prop.attrib.get("hisSpace"),
                        "history_index_space": ts_prop.attrib.get("hisIndexSpace"),
                        "archive_space": ts_prop.attrib.get("fileSpace"),
                        "archive_index_space": ts_prop.attrib.get("fileIndexSpace"),
                    }

    def parse_path(self, path: str | Path) -> TableStructure:
        file_path = Path(path)
        tree = ET.parse(file_path)
        root = tree.getroot()

        file_name = file_path.name
        table_name = file_name.rsplit(".", 1)[0]

        structure = TableStructure(
            path=str(file_path),
            file_name=file_name,
            table_name=table_name,
            chinese_name=root.attrib.get("chineseName", ""),
            object_id=root.attrib.get("objectId"),
            space=root.attrib.get("space"),
            run_mode=root.attrib.get("runMode"),
            data_storage_medium=root.attrib.get("dataStorageMedium"),
        )

        if structure.space and structure.space in self.tablespace_relations:
            ts_rel = self.tablespace_relations[structure.space]
            structure.index_space = ts_rel.get("index_space")
            structure.history_space = ts_rel.get("history_space")
            structure.history_index_space = ts_rel.get("history_index_space")
            structure.archive_space = ts_rel.get("archive_space")
            structure.archive_index_space = ts_rel.get("archive_index_space")

        table_base_prop = root.find(".//value[@xsi:type='stock:TableBaseProperty']", namespaces={"xsi": "http://www.w3.org/2001/XMLSchema-instance"})
        if table_base_prop is not None:
            structure.has_history = table_base_prop.attrib.get("history", "false").lower() == "true"

        for prop in root.findall("properties"):
            field = TableField(
                id=prop.attrib.get("id", ""),
                allow_null=prop.attrib.get("allowNull", "false").lower() == "true",
                uuid=prop.attrib.get("uuid"),
                comments=prop.attrib.get("comments"),
            )

            if field.id in self.standard_fields:
                std_field = self.standard_fields[field.id]
                field.data_type = std_field.get("dataType")
                field.chinese_name = std_field.get("chineseName")
                field.dictionary_type = std_field.get("dictionaryType")
                field.description = std_field.get("description")
                field.public_type = std_field.get("publicType")

            structure.fields.append(field)

        for idx in root.findall("indexs"):
            index = TableIndex(
                name=idx.attrib.get("name", ""),
                global_index=idx.attrib.get("global", "false").lower() == "true",
                flags=idx.attrib.get("flags"),
                index_type_ex=idx.attrib.get("indexTypeEx"),
            )

            for item in idx.findall("items"):
                attrname = item.attrib.get("attrname")
                if attrname:
                    index.fields.append(attrname)

            structure.indexes.append(index)

        return structure


def _standard_field_public_type(item: ET.Element) -> str | None:
    for mapping in item.findall(".//map"):
        if mapping.attrib.get("key") == "public_type":
            return mapping.attrib.get("value")
    return None
