---
title: Java中浮点数的进制转换原理
main_color: "#42E7EC"
top_img: https://bu.dusays.com/2025/05/13/68222883ade00.png
tag: 
- Java
- 源码
- 底层
- 基础
cover: https://bu.dusays.com/2025/05/13/68222883ade00.png
keywords: Java、浮点数、源码、底层
categories: Java
top_group_index: 3
swiper_index: 3
ai: true
---

### 有趣的现象：

在Java有一个非常有意思的现象，当我们定义一个浮点数，然后直接打印出来的时候，会发现打印出来的结果就是我们定义的值，但是如果这个浮点数参数了运算，我们打印运算后结果的时候，有时候输出的结果是存储再计算机中**真实的值**，但是有时后又不是，可以参考下面的例子，这是为什么呢？

~~~java
double a = 0.1;
double b = 0.2;
double c = 2.5;

System.out.println(a); // 0.1
System.out.println(a + b); // 0.30000000000000004
System.out.println(a + c); // 2.6
~~~

### 转换原理：

之所以会出现上面的这种情况，其实是java在把计算机中存储的二进制数据转换成十进制的时候，会把转换后结果的误差限定在**一个ULP(Unit in the Last Place)**的范围内，这样做的效果就是 **可以使用最少的位数精确的表达出来浮点数的数值。**下面是详细的介绍：

##### 1. Java打印浮点数的流程：

众所周知，Java中想要使用print函数进行输出的话，需要把对应的数据类型先转换成String类型才可以，即使是八种基本数据类型也不例外，以下是浮点数在java中被转换成字符串的流程：

* 调用Double.toString()方法把浮点数转换成字符串类型
  * 继续调用FloatingDecimal.toJavaFormatString(d)方法进行类型的转换
  * 在上面这个方法中会先调用getBinaryToASCIIConverter(d)方法先把二进制的转换成十进制的结果(在这个过程中会对转换后的十进制数据的精度进行限制)
    * 在getBinaryToASCIIConverter(d)方法中会进行参数的构造，然后调用 **dtoa()**方法把**二进制**浮点数转换成**十进制**
  * 然后再调用toJavaFormatString()方法把十进制结果转换成字符串
* 打印转换后的字符串结果

##### 2. 核心方法的源码：

通过上面的流程其实不难发现，java之所以在打印的时候输出的浮点数精度不一样，全是**dtoa()**方法的功劳，下面是getBinaryToASCIIConverter(d) 和 dtoa( int binExp, long fractBits, int nSignificantBits, boolean isCompatibleFormat)的源码解读。

* getBinaryToASCIIConverter(d)：

  ~~~java
      /**
       * 这个方法其实就做了一件事，就是为dtoa方法构造参数：
       * 		1. 首先把二进制浮点数据转换成长整型数据。之所以要进行转换是因为在计算机底层表示二进制的时候是使用阶码(二进制指数)，符号位以及尾数三个部分进行表示的，如果直接使用二进制浮点数进行后面的转换操作会比较麻烦，并且长整型和二进制浮点数都是64位的，这样可以方便地使用按位操作来提取这些部分，而不是直接进行浮点运算，所以这里转换成了长整型进行后面的操作。
       * 		2. 计算出转换需要规格化后的的阶码，符号位，尾数，以及该数据类型的有效位：nSignificantBits
       *@param d：原始的double数据
       *@param isCompatibleFormat: 是否兼容特定格式(例如:IEEE 754)
       **/
      static BinaryToASCIIConverter getBinaryToASCIIConverter(double d, boolean isCompatibleFormat) {
          // 把原始的64位二进制数据转换成64位长整型数据
          long dBits = Double.doubleToRawLongBits(d);
          // 通过与符号位掩码 DoubleConsts.SIGN_BIT_MASK 进行按位与操作来判断 d 是否为负数。
          boolean isNegative = (dBits&DoubleConsts.SIGN_BIT_MASK) != 0;
          // 提取出尾数部分（有效位），通过与尾数位掩码 DoubleConsts.SIGNIF_BIT_MASK 进行按位与操作得到
          long fractBits = dBits & DoubleConsts.SIGNIF_BIT_MASK;
          // 提取出指数部分。首先用指数位掩码 DoubleConsts.EXP_BIT_MASK 提取出指数，然后右移 EXP_SHIFT 位，得到实际的指数值
          int  binExp = (int)( (dBits&DoubleConsts.EXP_BIT_MASK) >> EXP_SHIFT );
          // 检查是否为特殊值（NaN 或无穷大）。如果指数是最大值（表示无穷大或 NaN），且尾数为零，则返回正/负无穷大；否则，返回 NaN。
          if ( binExp == (int)(DoubleConsts.EXP_BIT_MASK>>EXP_SHIFT) ) {
              if ( fractBits == 0L ){
                  return isNegative ? B2AC_NEGATIVE_INFINITY : B2AC_POSITIVE_INFINITY;
              } else {
                  return B2AC_NOT_A_NUMBER;
              }
          }
  
          int  nSignificantBits;
          // 1. 处理非规格化数字：如果指数为0（表示这是一个非规格化的数字），则需要将尾数左移，以便将其转为规格化形式，并调整指数。
          if ( binExp == 0 ){
              // 如果指数为0并且位数也为0的情况，意味着这个浮点数就是0
              if ( fractBits == 0L ){
                  return isNegative ? B2AC_NEGATIVE_ZERO : B2AC_POSITIVE_ZERO;
              }
              int leadingZeros = Long.numberOfLeadingZeros(fractBits);
              int shift = leadingZeros-(63-EXP_SHIFT);
              fractBits <<= shift;
              binExp = 1 - shift;
              nSignificantBits =  64-leadingZeros; // recall binExp is  - shift count.
          } else {
              // 2. 处理规格化数字：如果指数非零，则将尾数与假设的最高有效位 FRACT_HOB 进行按位或操作，计算实际的有效位数 nSignificantBits。(这里其实是一个固定的标准，比如double类型的nSignificantBits固定位53位，float的为22位。
              fractBits |= FRACT_HOB;
              nSignificantBits = EXP_SHIFT+1;
          }
  
          // 3. 调整指数偏移：从指数中减去偏移量 DoubleConsts.EXP_BIAS，得到实际的指数值。
          binExp -= DoubleConsts.EXP_BIAS;
          BinaryToASCIIBuffer buf = getBinaryToASCIIBuffer();
          buf.setSign(isNegative);
          // 调用dtoa方法完成进制转换以及精度限制
          buf.dtoa(binExp, fractBits, nSignificantBits, isCompatibleFormat);
          return buf;
      }
  ~~~

* **dtoa( int binExp, long fractBits, int nSignificantBits, boolean isCompatibleFormat)：**

  ~~~java
  	/**
       * 这个方法的作用就是进行二进制与十进制的转换，并对结果进行精度的限制：
       * 		1. 进行合法性校验，并计算得到一些转换时必要的参数，像：尾数的有效位，浮点数小数的位数等
       * 		2. 判断当前的浮点数是否是简单的数，也就是判断精度大小以及是否是整数，如果是的话直接把二进制转换成十进制就可以了
       * 		3. 如果是复杂的浮点数，需要计算得到B5，B2，S5，S2，M5，M2这六个参数，然后通过这六个参数对原来的二进制浮点数进行缩放和精度限制，以得到想要的结果。
       * 		4. 对转换完成的结果进行四舍五入，确保最终的十进制表示尽可能精确地反映原始浮点数值
       * @param binExp 浮点数的二进制指数
       * @param fractBits 浮点数的尾数部分
       * @param nSignificantBits 该浮点类型的有效位
       * @param isCompatibleFormat 是否兼容特定的格式
       */
      private void dtoa( int binExp, long fractBits, int nSignificantBits, boolean isCompatibleFormat)
      {
          // 保证尾数大于0，小于等于0是没有意义的
          assert fractBits > 0 ;
          // 确保尾数的最高位为1，因为在上面的方法中，尾数已经被规范化了，这里如果为0的化明显是有错误的
          assert (fractBits & FRACT_HOB)!=0  ;
          // 计算fractBits末尾有多少个连续的零。
          final int tailZeros = Long.numberOfTrailingZeros(fractBits);
          //  表示该浮点数真实有效的位数。这里 EXP_SHIFT + 1 是一个常量，表示浮点数有效位数的最大值(例如Double类型为53，去除掉尾数末尾连续的0之后的值就是nFractBits)
          final int nFractBits = EXP_SHIFT+1-tailZeros;
  
          // 初始化两个标志位：decimalDigitsRoundedUp 表示是否需要进行四舍五入；exactDecimalConversion 表示是否精确转换（无精度损失）
          decimalDigitsRoundedUp = false;
          exactDecimalConversion = false;
          // 计算小数部分的位数 nTinyBits，即有效位数减去指数部分之后的剩余位数，确保其非负。
          int nTinyBits = Math.max( 0, nFractBits - binExp - 1 );
  
          // 处理“简单”的数，通过指数的大小判断当前的浮点数是否是极端的数据：指数在MIN_SMALL_BIN_EXP 到 MAX_SMALL_BIN_EXP 之间，表示数值的规模适中，这样的数不需要特别处理极大或极小的情况。它们的二进制浮点表示相对简单，转换成十进制字符串时可以用更高效、简单的方法处理，因此被认为是“容易处理”的数。如果指数 binExp 太小（小于MIN_SMALL_BIN_EXP），表示数值接近于零，可能会有大量前导零，在十进制转换中需要考虑非常小的数字。如果指数binExp 太大（大于 MAX_SMALL_BIN_EXP），表示数值非常大，需要处理大量尾随零和可能的溢出问题。
          if ( binExp <= MAX_SMALL_BIN_EXP && binExp >= MIN_SMALL_BIN_EXP ){
  
              // 判断有效位的位数是否使用long类型可以存储以及是否会发生溢出(使用long类型比使用BigInteger类型计算的更快，所以在这判断了一下是否可以使用long进行加速计算)
              if ( (nTinyBits < FDBigInteger.LONG_5_POW.length) && ((nFractBits + N_5_BITS[nTinyBits]) < 64 ) ){
                  // 未规格化的尾数位数为0表示当前的数没有小数部分，直接使用整数部分的转换方法
                  if ( nTinyBits == 0 ) {
                      int insignificant;
                      if ( binExp > nSignificantBits ){
                          insignificant = insignificantDigitsForPow2(binExp-nSignificantBits-1);
                      } else {
                          insignificant = 0;
                      }
                      // 比较指数和有效位数的大小来使尾数左移或右移对应的尾数，这个操作非常的关键，经过移位后fractBits表示的就是浮点数的尾数了，而是二进制的整数
                      if ( binExp >= EXP_SHIFT ){
                          fractBits <<= (binExp-EXP_SHIFT);
                      } else {
                          fractBits >>>= (EXP_SHIFT-binExp) ;
                      }
                      // 调用 developLongDigits 方法将结果转换为十进制字符串表示
                      developLongDigits( 0, fractBits, insignificant );
                      return;
                  }
              }
          }
  
          // 通过调用estimateDecExp()来获取当前浮点数的十进制指数
          int decExp = estimateDecExp(fractBits,binExp);
          int B2, B5;
          int S2, S5;
          int M2, M5;
  
          /**
           * 一个十进制可以表示为：x = m * 10^decEXp；进一步可以拆分为：x = m * 2^decExp * 5^decExp,这样就在十进制浮点数和二进制浮点数之间建立了联系(二进制：x = m * 2^binExp）
           * B5：它调整与 5 相关的因子，用来平衡十进制指数的影响，取0和-decExp中的最大值，当decExp < 0时，表示十进制指数是负的，意味着需要将数值缩小到一个更小的范围。因此，我们需要乘以5^B5来抵消负指数的影响
           * B2：B2是一个非负整数，它调整与 2 相关的因子，用来平衡二进制指数的影响，表示在转换过程中，需要乘以 2^B2 以平衡二进制指数的2的部分。
           * S5：它调整与 5 相关的因子，也是用来平衡十进制指数的影响的，取0和decExp中的最大值，当decExp > 0时，表示十进制指数时正的，意味着转换后会将数值放大到一个更大的范围。因此，需要除以5^S5来抵消正指数的影响
           * S2：B2是一个非负整数，它调整与 2 相关的因子，用来平衡二进制指数的影响，表示在转换过程中，需要除以 2^B2 以平衡二进制指数的2的部分。
           * 从上面的定义中不难看出，B 系列负责放大数值，以便将二进制数转换为一个可操作的整数范围。S 系列负责缩小数值，以确保最终结果与十进制表示相符。例如：在将一个二进制浮点数表示成形如 M * 10^E 的十进制形式时：我们需要放大数值 M，使其成为一个适合处理的整数范围，这个放大的操作由 B5 和 B2 来完成。同时，必须确保十进制指数 E 被正确调整。这意味着，我们在放大 M 的时候，还需要相应地缩小与指数相关的部分，这个缩小操作由 S5 和 S2 来完成。
           * 最终的公式：M' = (M * 2^B2 * 5^B5) / (2^S2 * 5^S5)
           */
          B5 = Math.max( 0, -decExp );
          B2 = B5 + nTinyBits + binExp;
          S5 = Math.max( 0, decExp );
          S2 = S5 + nTinyBits;
  
          /**
           * M: (1 / 2^nSignificantBits) * 2^nTinyBits * 10^max(0, -decExp), 此时M表示的是 “当前浮点数”的最小浮动单位ULP的一半，这样我们就可以根据M的值来确定转换后的十进制结果的精度了
           * M5：M 的十进制部分(5 的因子)。它表示需要乘以多少个 5 来缩放最小单位 M。M5 被设置为 B5，这意味着在十进制因子方面，M 与 B 有相同的 5 因子。因为我们需要确保在十进制的缩放上，它们是同步的。
           * M2：M 的二进制部分(2 的因子)。它表示需要乘以多少个 2 来缩放最小单位 M。M2 被设定为 B2 - nSignificantBits，这是因为 M 代表了 ULP 的一半。减去 nSignificantBits 后，M 的二进制缩放与 B 对齐，同时反映出 M 的实际二进制精度需求。
           * M系列参数的作用：在十进制转换过程中，我们需要确定要生成多少位数（即确定如何四舍五入）。M 的值用来界定舍入的边界。当我们对十进制数进行迭代计算时，如果余数小于等于 M，那么可以认为当前的十进制结果已经足够准确，不需要再继续计算。例如，当我们得到一个结果 B/S，如果余数（B % S）比 M 更小，则表示这个结果是精确的（在浮点精度范围内），不需要再进一步增加精度。
           * ULP(Unit in the Last Place)：指的是浮点数表示中的最小可分辨单位，每一个浮点数都有一个固定的精度，这种情况下ULP就是该浮点数尾数的最小的变化，如浮点数为0.1，那么下一个可以表示的浮点数就是0.2，此时ULP是这两个浮点数的差异(0.1，0.2)。所以ULP通常用于量化浮点数运算中的误差范围，并确保计算精度。
           */
          M5 = B5;
          M2 = B2 - nSignificantBits;
  
          // 去掉尾数末尾的0
          fractBits >>>= tailZeros;
          // 作用是调整二进制指数 B2，使得尾数fractBits的最高有效位（最左侧的非零位）与预期的位置对齐。调整 B2 的目的是为了确保在二进制到十进制转换的过程中，计算能够尽可能准确地表示浮点数，减少舍入误差。这种调整使得转换算法能够有效地操作不同表示形式的数值，从而实现高效且精确的计算。
          B2 -= nFractBits-1;
          // 找到B2，S2，M2中的公共因子，把公共因子去掉，这里是方便计算用的
          int common2factor = Math.min( B2, S2 );
          B2 -= common2factor;
          S2 -= common2factor;
          M2 -= common2factor;
          // 当尾数只有一位的时候需要让M2的值更小一些，以便能更精确的表示最小化范围的浮点数
          if ( nFractBits == 1 ) {
              M2 -= 1;
          }
          // 如果M2 = 0表示当前的浮点数精度的上下界已经不能再缩小了，M2 < 0其实是无效的，但实际上又需要进行缩小，所以让B2，S2也缩小相应的值来进行平衡
          if ( M2 < 0 ){
              B2 -= M2;
              S2 -= M2;
              M2 =  0;
          }
  
          // 转换后十进制的位数
          int ndigit = 0;
          // 精度的上下界
          boolean low, high;
          // 用于判断小数点前最后一位的精确度差异
          long lowDigitDifference;
          // 当前十进制位的具体值
          int  q;
  
          // Bbits 是在二进制转换过程中，表示十进制数的二进制位数总数的近似值。这个值包含了尾数的有效位数、乘以 2 的调整以及乘以 5 的调整。通过计算 Bbits，我们可以估算尾数 B 在乘以 5^B5 和 2^B2 后所需的总二进制位数。
          int Bbits = nFractBits + B2 + (( B5 < N_5_BITS.length )? N_5_BITS[B5] : ( B5*3 ));
          // 乘以10后的有效位数, 程序可以决定使用不同的优化路径来转换浮点数，例如使用整数或长整数运算。
          int tenSbits = S2+ 1 + (( (S5+1) < N_5_BITS.length )? N_5_BITS[(S5+1)] : ( (S5+1)*3 ));
          // 根据Bbits以及tenSbits的值来确定使用什么长度的数据类型来转换浮点数，这个方法中，32位/64位/FDBigInteger这三个不同的数据类型的处理逻辑是一样的
          if ( Bbits < 64 && tenSbits < 64){
              if ( Bbits < 32 && tenSbits < 32){
                  // 计算当前的尾数 fractBits 乘以 5 的 B5 次方，再乘以 2 的 B2 次方。这表示尾数部分的十进制值的起始点
                  int b = ((int)fractBits * FDBigInteger.SMALL_5_POW[B5] ) << B2;
                  // 基数部分，乘以 5 的 S5 次方和 2 的 S2 次方
                  int s = FDBigInteger.SMALL_5_POW[S5] << S2;
                  // 上下界的差值（用来确定精度范围），乘以 5 的 M5 次方和 2 的 M2 次方。
                  int m = FDBigInteger.SMALL_5_POW[M5] << M2;
                  // s 乘以 10，用来确定下一位的十进制值。
                  int tens = s * 10;
  
                  ndigit = 0;
                  // 计算尾数除以基数的商，结果就是当前位的十进制的值
                  q = b / s;
                  // 将尾数的余数乘以 10，准备计算下一位
                  b = 10 * ( b % s );
                  // 将上下界乘以 10，以确保计算精度, 并更新上下界的值
                  m *= 10;
                  low  = (b <  m );
                  high = (b+m > tens );
                  assert q < 10 : q;
                  // 如果第一次计算的商 q 为 0，且不超出范围（!high），则表示估计的指数 decExp 过高，需要减小。
                  if ( (q == 0) && ! high ){
                      decExp--;
                  } else {
                      // 将计算的数字字符添加到结果数组中。
                      digits[ndigit++] = (char)('0' + q);
                  }
  
                  // 判断当前的格式是否与预期的输出格式兼容/指数是否太大或者太小
                  if ( !isCompatibleFormat ||decExp < -3 || decExp >= 8 ){
                      high = low = false;
                  }
                  // 通过迭代来转换并保存十进制的每一位
                  while( ! low && ! high ){
                      q = b / s;
                      b = 10 * ( b % s );
                      m *= 10;
                      assert q < 10 : q;
                      if ( m > 0L ){
                          low  = (b <  m );
                          high = (b+m > tens );
                      } else {
                          low = true;
                          high = true;
                      }
                      digits[ndigit++] = (char)('0' + q);
                  }
                  // 用于判断小数点前最后一位的精确度差异
                  lowDigitDifference = (b<<1) - tens;
                  // 表示是否已经精确转换为十进制表示（b == 0 表示尾数已经全部转换完成）
                  exactDecimalConversion  = (b == 0);
              } else {
                  long b = (fractBits * FDBigInteger.LONG_5_POW[B5] ) << B2;
                  long s = FDBigInteger.LONG_5_POW[S5] << S2;
                  long m = FDBigInteger.LONG_5_POW[M5] << M2;
                  long tens = s * 10L;
  
                  ndigit = 0;
                  q = (int) ( b / s );
                  b = 10L * ( b % s );
                  m *= 10L;
                  low  = (b <  m );
                  high = (b+m > tens );
                  assert q < 10 : q;
                  if ( (q == 0) && ! high ){
                      decExp--;
                  } else {
                      digits[ndigit++] = (char)('0' + q);
                  }
  
                  if ( !isCompatibleFormat || decExp < -3 || decExp >= 8 ){
                      high = low = false;
                  }
                  while( ! low && ! high ){
                      q = (int) ( b / s );
                      b = 10 * ( b % s );
                      m *= 10;
                      assert q < 10 : q;
                      if ( m > 0L ){
                          low  = (b <  m );
                          high = (b+m > tens );
                      } else {
                          low = true;
                          high = true;
                      }
                      digits[ndigit++] = (char)('0' + q);
                  }
                  lowDigitDifference = (b<<1) - tens;
                  exactDecimalConversion  = (b == 0);
              }
          } else {
  
              FDBigInteger Sval = FDBigInteger.valueOfPow52(S5, S2);
              int shiftBias = Sval.getNormalizationBias();
              Sval = Sval.leftShift(shiftBias); // normalize so that division works better
  
              FDBigInteger Bval = FDBigInteger.valueOfMulPow52(fractBits, B5, B2 + shiftBias);
              FDBigInteger Mval = FDBigInteger.valueOfPow52(M5 + 1, M2 + shiftBias + 1);
  
              FDBigInteger tenSval = FDBigInteger.valueOfPow52(S5 + 1, S2 + shiftBias + 1); //Sval.mult( 10 );
  
              ndigit = 0;
              q = Bval.quoRemIteration( Sval );
              low  = (Bval.cmp( Mval ) < 0);
              high = tenSval.addAndCmp(Bval,Mval)<=0;
  
              assert q < 10 : q;
              if ( (q == 0) && ! high ){
                  decExp--;
              } else {
                  digits[ndigit++] = (char)('0' + q);
              }
  
              if (!isCompatibleFormat || decExp < -3 || decExp >= 8 ){
                  high = low = false;
              }
              while( ! low && ! high ){
                  q = Bval.quoRemIteration( Sval );
                  assert q < 10 : q;
                  Mval = Mval.multBy10();
                  low  = (Bval.cmp( Mval ) < 0);
                  high = tenSval.addAndCmp(Bval,Mval)<=0;
                  digits[ndigit++] = (char)('0' + q);
              }
              if ( high && low ){
                  Bval = Bval.leftShift(1);
                  lowDigitDifference = Bval.cmp(tenSval);
              } else {
                  lowDigitDifference = 0L;
              }
              exactDecimalConversion  = (Bval.cmp( FDBigInteger.ZERO ) == 0);
          }
          // 十进制指数+1，在格式化过程中，指数部分的偏移量需要调整。
          this.decExponent = decExp+1;
          // 十进制数字数组 digits 中第一个有效数字的索引。
          this.firstDigitIndex = 0;
          // nDigits 是有效的数字总数，即转换后得到的十进制数字的位数。
          this.nDigits = ndigit;
          /**
           * 在浮点数转换过程中，直接使用计算得到的结果可能会导致精度问题。特别是在我们尝试将尾数的二进制部分精确地转换为十进制时，可能会出现以下两种情况：
           *  低估（b < m）：当前的结果 b 在舍入时可能偏低，意味着我们需要增加最后的数字，以接近真实值。
           *  高估（b + m > tens）：当前的结果 b 加上舍入值 m 超过了基准值 tens，这表明当前结果 b 可能高于真实值，我们需要增加最后的数字来修正偏差。
           * 所以：舍入操作是为了在浮点数转换为十进制数时，处理精度和表示问题。通过在 b < m 或 b + m > tens 时进行舍入，可以确保最终的十进制表示尽可能精确地反映原始浮点数值。
           */
          if ( high ){
              if ( low ){
                  if ( lowDigitDifference == 0L ){
                      if ( (digits[firstDigitIndex+nDigits-1]&1) != 0 ) {
                          roundup();
                      }
                  } else if ( lowDigitDifference > 0 ){
                      roundup();
                  }
              } else {
                  roundup();
              }
          }
      }
  ~~~

##### 3. 具体的例子：

假如，打印`0.1` + `0.2`的值

* Java 在执行浮点数运算（如 `0.1 + 0.2`）时，会先将十进制的浮点数 `0.1` 和 `0.2` 转换为符合 IEEE 754 标准的二进制浮点数表示。由于 `0.1` 和 `0.2` 不能精确地用二进制表示，因此在这个转换过程中会产生一些精度舍入误差。转换后的二进制数被输入到 CPU 的 ALU进行加法操作。在这一过程中，也可能会因为运算的有限精度再次引入微小的舍入误差，得到一个近似的二进制结果。

* Java 拿到这个二进制浮点数结果后，会调用 `Double.toString()` 方法来生成结果的十进制字符串表示。`Double.toString()` 方法内部使用了 `dtoa()` 算法，该算法将二进制浮点数转换回十进制，同时根据当前的 `M` 值（决定输出的有效位数）进行精度舍入。

* dtoa执行逻辑：

  * 输入参数：

    * `binExp = -2`：二进制指数
    * `fractBits = 5404319552844596`：64位的长整型尾数。
    * `nSignificantBits = 53`：有效位的位数。
    * `isCompatibleFormat = true`：是否与 Java 的浮点格式兼容。

  * 计算相关参数：

    * `tailZeros = 2`：尾数部分的末尾有两个0
    * `nFractBits = 51`：尾数部分减去末尾0后的实际的有效位
    * `nTinyBits = 52`：二进制浮点数小数的位数

  * 判断当前的浮点数是否时`简单数`，简单数就是大小适中(没有极端值)并且没有小数部分的浮点数，这种浮点数直接移位对齐然后转换成对应的十进制就可以了，很明显这里不是简单数

  * 如果当前的浮点数是`复杂数`，那么就需要先求出对应的六个参数：

    * `B5 = 1`
    * `B2 = 51`
    * `S5 = 0`
    * `S2 = 52`
    * `M5 = 1`
    * `M2 = -2`
    * 尾数部分右移去除末尾的`0`，同时`B2`,`S2`,`M2`去除掉公共的指数
      * `fractBits = 1351079888211149`
      * `B2 = 0`
      * `S2 = 51`
      * `M2 = -3`：由于`M2 < 0`，所以需要把`M2`置为0，同时`B2`和`S2`加上对应的值，所以最终的结果为`B2 = 3`, `S2 = 54`,`M2 = 0`

  * 然后就是具体的计算了，因为当前的类型是double，所以使用的是64位的long来保存中间结果，各中间结果的具体数值如下(可以根据上面源码中的公式计算得出)：

    * `b = 54043195528445960`
    * `s = 18014398509481984`
    * `m = 5`
    * `tens = 180143985094819840`
    * `q = 3`
    * `更新后的b = 80`
    * `low = false`
    * `high = false`

    通过判断是否超出精度来决定是否保存的前的结果到digits结果数组中

  * 通过执行下面的代码进行不断的迭代最终得到：`digits: [3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4,,,]`

    ```java
    while( ! low && ! high ){
        q = (int) ( b / s );
        b = 10 * ( b % s );
        m *= 10;
        assert q < 10 : q; 
        if ( m > 0L ){
            low  = (b <  m );
            high = (b+m > tens );
        } else {
            low = true;
            high = true;
        }
        digits[ndigit++] = (char)('0' + q);
    }
    ```

  * 根据`low`和`high`的值判断一下是否需要进行舍入以提高精度，在这个例子中不需要进行舍入操作

  * 最后就是把转换后的保存了十进制的`digits`数据转换成String类型进行输出

##### 4. 原理总结：

（1）**Java 中浮点数进制转换的过程和机制：**Java 使用 IEEE 754 双精度浮点数格式（`double`）来表示浮点数，这种格式将一个浮点数表示为符号位、指数部分和尾数部分的组合。由于十进制小数（如 `0.1` 或 `0.2`）无法精确地用二进制表示，所以浮点数的二进制表示通常是一个近似值。这种表示导致在浮点数的计算和转换过程中出现舍入误差。在 Java 中，将浮点数转换为十进制表示是通过 `dtoa` 方法（double to ASCII）来实现的。在这个方法中，`M` 的计算决定了输出结果的精度和舍入行为。

M在 `dtoa` 方法中的作用：`M` 的计算和使用决定了浮点数在转换为十进制字符串时的精度和舍入方向，直接影响到最终的输出结果。

* 如果 `M` 较大，表示浮点数的两个相邻值之间有较大的差距，`dtoa` 方法会选择较少的有效位数来表示数值，从而输出一个更简洁的十进制数。
* 果 `M` 较小，则表示浮点数的相邻值之间的差距很小，`dtoa` 方法会保留更多的有效位数来确保精度。

（2）**Java 中浮点数赋值、舍入及运算输出差异的机制**

* 直接赋值：
  * 当浮点数被直接赋值时，Java 将十进制数转换为最接近的 IEEE 754 二进制浮点数表示。转换后的结果是一个近似值。
  * 输出时，Java 使用 `dtoa` 方法，将这个二进制表示转回十进制字符串，其中 `M` 决定了输出的舍入方式和精度。因此，可能会输出一个用户期望的简短结果（如 `0.1`），而不是精确的二进制表示值。
* 舍入后的值：
  * 当调用round()函数对浮点数进行舍入的时候(BigDecimal的setScale方法为例，这个方法可以在进行精度的舍入的时候保留指定的精度并且可以指定舍入的方向)，首先会根据相关算法进行舍入，然后把十进制的结果换为最接近的二进制浮点数表示。
  * 输出时还是会调用`dtoa` 方法，将这个二进制表示转回十进制字符串，输出的舍入方式和精度依旧由M决定。
* 运算的值：
  * 浮点数在运算时（如 `0.1 + 0.2`），每一步计算都会引入微小的舍入误差，这是因为所有运算都基于浮点数的二进制近似表示。
  * 运算结果的输出也是通过 `dtoa` 方法自动格式化的。`M` 的值决定了输出的有效位数和舍入行为，因此可能会出现 `0.30000000000000004` 而不是 `0.3` 的结果。

**总之：**在 Java 中，浮点数赋值、舍入和运算的输出差异主要源于二进制浮点数转换为十进制数进行输出的时候，在 `dtoa` 方法中会根据`M`的值处理精度和舍入问题，`M`的值由想要输出的浮点数的内容决定，所以**浮点数本身的精度是决定输出精度的关键而不是操作的类型**(这里的精度指的是浮点数在java中的精度，比如0.1的精度就是小数点后一位)。