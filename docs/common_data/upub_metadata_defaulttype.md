# upub - 标准数据类型

标准数据类型定义，包含各数据库类型的映射。

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2023-09-04 14:35:47 | V3.0.1.1 | 沈勋 | 版本统一调整 |


## 类型列表（共 34 个）

### Char (字符)


| 数据库 | 类型 |
|--------|------|
| c | `char` |
| oracle | `char` |
| db2 | `char` |
| sqlserver | `char` |
| java | `char` |
| mysql | `char` |
| informix | `char` |
| sybase | `char` |

### String (字符串)

- DB2有长度限制，32K级。C语言类型实际无效

| 数据库 | 类型 |
|--------|------|
| c | `char [$L]` |
| oracle | `varchar2($L)` |
| db2 | `varchar($L)` |
| sqlserver | `varchar($L)` |
| java | `String` |
| mysql | `varchar($L)` |
| informix | `varchar($L)` |
| sybase | `varchar($L)` |

### Int8 (8位整数)


| 数据库 | 类型 |
|--------|------|
| c | `int8_t` |
| oracle | `number(3,0)` |
| db2 | `smallint` |
| sqlserver | `tinyint ` |
| java | `short` |
| mysql | `smallint` |
| informix | `smallint` |
| sybase | `tinyint` |

### Int16 (16位整数)


| 数据库 | 类型 |
|--------|------|
| c | `int16_t` |
| oracle | `number(6,0)` |
| db2 | `smallint` |
| sqlserver | `smallint` |
| java | `short` |
| mysql | `mediumint` |
| informix | `smallint` |
| sybase | `smallint` |

### Int32 (32位整数)


| 数据库 | 类型 |
|--------|------|
| c | `int32_t` |
| oracle | `number(10,0)` |
| db2 | `int` |
| sqlserver | `int` |
| java | `int` |
| mysql | `int` |
| informix | `int` |
| sybase | `int` |

### Double (浮点数)

-  

| 数据库 | 类型 |
|--------|------|
| c | `double` |
| oracle | `number($L,$P)` |
| db2 | `decimal($L,$P)` |
| sqlserver | `decimal($L,$P)` |
| java | `BigDecimal` |
| mysql | `decimal($L,$P)` |
| informix | `decimal($L,$P)` |
| sybase | `decimal($L,$P)` |

### Clob (字符型大对象)

- DB2要求指定长度，一般为2G

| 数据库 | 类型 |
|--------|------|
| oracle | `clob` |
| db2 | `clob(1024M)` |
| sqlserver | `text` |
| java | `String` |
| c | `void *` |
| mysql | `longtext` |
| informix | `text` |
| sybase | `text` |

### DateTime (日期时间)


| 数据库 | 类型 |
|--------|------|
| oracle | `date` |
| db2 | `timestamp` |
| sqlserver | `datetime` |
| java | `Date` |
| mysql | `timestamp` |
| informix | `datetime` |
| sybase | `datetime` |
| c | `long` |

### Cursor (结果集游标)


| 数据库 | 类型 |
|--------|------|
| oracle | `cursor` |
| c | `void *` |

### Void (未知类型)

- 针对具体语言

| 数据库 | 类型 |
|--------|------|
| c | `void *` |
| sqlserver | ` ` |

### CUnpacker (解包器类)

- 针对具体语言

| 数据库 | 类型 |
|--------|------|
| c | `IF2UnPacker *` |
| java | `IDataSet` |

### Int64 (64位整数)


| 数据库 | 类型 |
|--------|------|
| c | `int64_t` |
| oracle | `number(20,0)` |
| mysql | `int64` |

### UINT8 ()


| 数据库 | 类型 |
|--------|------|
| c | `uint8_t` |

### UINT16 ()


| 数据库 | 类型 |
|--------|------|
| c | `uint16_t` |

### UINT32 ()


| 数据库 | 类型 |
|--------|------|
| c | `uint32_t` |

### UINT64 ()


| 数据库 | 类型 |
|--------|------|
| c | `uint64_t` |

### CPacker (打包器)


| 数据库 | 类型 |
|--------|------|
| c | `IF2Packer *` |

### Char (字符)


| 数据库 | 类型 |
|--------|------|
| c | `char` |
| oracle | `char` |
| db2 | `char` |
| sqlserver | `char` |
| java | `char` |
| mysql | `char` |
| informix | `char` |
| sybase | `char` |

### String (字符串)

- DB2有长度限制，32K级。C语言类型实际无效

| 数据库 | 类型 |
|--------|------|
| c | `char [$L]` |
| oracle | `varchar2($L)` |
| db2 | `varchar($L)` |
| sqlserver | `varchar($L)` |
| java | `String` |
| mysql | `varchar($L)` |
| informix | `varchar($L)` |
| sybase | `varchar($L)` |

### Int8 (8位整数)


| 数据库 | 类型 |
|--------|------|
| c | `int8_t` |
| oracle | `number(3,0)` |
| db2 | `smallint` |
| sqlserver | `tinyint ` |
| java | `short` |
| mysql | `smallint` |
| informix | `smallint` |
| sybase | `tinyint` |

### Int16 (16位整数)


| 数据库 | 类型 |
|--------|------|
| c | `int16_t` |
| oracle | `number(6,0)` |
| db2 | `smallint` |
| sqlserver | `smallint` |
| java | `short` |
| mysql | `mediumint` |
| informix | `smallint` |
| sybase | `smallint` |

### Int32 (32位整数)


| 数据库 | 类型 |
|--------|------|
| c | `int32_t` |
| oracle | `number(10,0)` |
| db2 | `int` |
| sqlserver | `int` |
| java | `int` |
| mysql | `int` |
| informix | `int` |
| sybase | `int` |

### Double (浮点数)

-  

| 数据库 | 类型 |
|--------|------|
| c | `double` |
| oracle | `number($L,$P)` |
| db2 | `decimal($L,$P)` |
| sqlserver | `decimal($L,$P)` |
| java | `BigDecimal` |
| mysql | `decimal($L,$P)` |
| informix | `decimal($L,$P)` |
| sybase | `decimal($L,$P)` |

### Clob (字符型大对象)

- DB2要求指定长度，一般为2G

| 数据库 | 类型 |
|--------|------|
| oracle | `clob` |
| db2 | `clob(1024M)` |
| sqlserver | `text` |
| java | `String` |
| c | `void *` |
| mysql | `longtext` |
| informix | `text` |
| sybase | `text` |

### DateTime (日期时间)


| 数据库 | 类型 |
|--------|------|
| oracle | `date` |
| db2 | `timestamp` |
| sqlserver | `datetime` |
| java | `Date` |
| mysql | `timestamp` |
| informix | `datetime` |
| sybase | `datetime` |
| c | `long` |

### Cursor (结果集游标)


| 数据库 | 类型 |
|--------|------|
| oracle | `cursor` |
| c | `void *` |

### Void (未知类型)

- 针对具体语言

| 数据库 | 类型 |
|--------|------|
| c | `void *` |
| sqlserver | ` ` |

### CUnpacker (解包器类)

- 针对具体语言

| 数据库 | 类型 |
|--------|------|
| c | `IF2UnPacker *` |
| java | `IDataSet` |

### Int64 (64位整数)


| 数据库 | 类型 |
|--------|------|
| c | `int64_t` |
| oracle | `number(20,0)` |
| mysql | `int64` |

### UINT8 ()


| 数据库 | 类型 |
|--------|------|
| c | `uint8_t` |

### UINT16 ()


| 数据库 | 类型 |
|--------|------|
| c | `uint16_t` |

### UINT32 ()


| 数据库 | 类型 |
|--------|------|
| c | `uint32_t` |

### UINT64 ()


| 数据库 | 类型 |
|--------|------|
| c | `uint64_t` |

### CPacker (打包器)


| 数据库 | 类型 |
|--------|------|
| c | `IF2Packer *` |
