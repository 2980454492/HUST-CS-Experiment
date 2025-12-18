#include <stdio.h>
#include <stdlib.h>

// 判断两个函数的输出是否相同
void check(int (*func)(int), int (*standard)(int), int x) {
    if (func(x) == standard(x)) {
        printf("正确\n");
    }
    else {
        printf("错误\n");
    }
}

void check(int (*func)(int, int), int (*standard)(int, int), int x, int y) {
    if (func(x, y) == standard(x, y)) {
        printf("正确\n");
    }
    else {
        printf("错误\n");
    }
}

void check(int (*func)(int, int, int), int (*standard)(int, int, int), int x, int y, int z) {
    if (func(x, y, z) == standard(x, y, z)) {
        printf("正确\n");
    }
    else {
        printf("错误\n");
    }
}

// (1) 返回 x 的绝对值
int absVal(int x) {
    int sign = x >> 31; // 获取符号位
    return (x ^ sign) - sign; // 如果x为负数，则取反并加1
}

int absVal_standard(int x) {
    return (x < 0) ? -x : x;
}

// (2) 实现 -x
int negate(int x) {
    return ~x + 1; // 按位取反加1得到相反数
}

int negate_standard(int x) {
    return -x;
}

// (3) 实现 &
int bitAnd(int x, int y) {
    return ~(~x | ~y); // 使用德摩根定律
}

int bitAnd_standard(int x, int y) {
    return x & y;
}

// (4) 实现 |
int bitOr(int x, int y) {
    return ~(~x & ~y); // 使用德摩根定律
}

int bitOr_standard(int x, int y) {
    return x | y;
}

// (5) 实现 ^
int bitXor(int x, int y) {
    return (x | y) & ~(x & y); // 异或的逻辑实现
}

int bitXor_standard(int x, int y) {
    return x ^ y;
}

// (6) 判断x是否为最大的正整数（7FFFFFFF）
int isTmax(int x) {
    return !(x ^ 0x7FFFFFFF);
}

int isTmax_standard(int x) {
    return x == 0x7FFFFFFF;
}

// (7) 统计x的二进制表示中 1 的个数
int bitCount(int x) {
    x = (x & 0x55555555) + ((x >> 1) & 0x55555555); // 每两位分一组
    x = (x & 0x33333333) + ((x >> 2) & 0x33333333); // 每四位分一组
    x = (x & 0x0F0F0F0F) + ((x >> 4) & 0x0F0F0F0F); // 每八位分一组
    x = (x & 0x00FF00FF) + ((x >> 8) & 0x00FF00FF); // 每十六位分一组
    x = (x & 0x0000FFFF) + ((x >> 16) & 0x0000FFFF); // 每三十二位分一组
    return x;
}

int bitCount_standard(int x) {
    int count = 0;
    while (x) {
        count += x & 1;
        x >>= 1;
    }
    return count;
}

// (8) 产生从lowbit 到 highbit 全为1，其他位为0的数
int bitMask(int highbit, int lowbit) {
    int mask1 = (0x7FFFFFFF >> (30 - highbit)); 
    int mask2 = (0xFFFFFFFF << lowbit); 
    return (mask1 & mask2); // 按位与得到从lowbit到highbit的全1区域
}

int bitMask_standard(int highbit, int lowbit) {
    int mask = 0;
    for (int i = lowbit; i <= highbit; i++) {
        mask |= 1 << i;
    }
    return mask;
}

// (9) 判断x+y是否会产生溢出
int addOK(int x, int y) {
    int sum = x + y;
    int sign_x = (x >> 31) & 1;
    int sign_y = (y >> 31) & 1;
    int sign_sum = (sum >> 31) & 1;
    return (sign_x & sign_y & ~sign_sum) | (~sign_x & ~sign_y & sign_sum); // 溢出条件
}

int addOK_standard(int x, int y) {
    int sum = x + y;
    return (x > 0 && y > 0 && sum < 0) || (x < 0 && y < 0 && sum > 0);
}

// (10) 将x的第n个字节与第m个字节交换
int byteSwap(int x, int n, int m) {
    int mask_n = 0xFF << (n * 8);
    int mask_m = 0xFF << (m * 8);
    int byte_n = (x & mask_n) >> (n * 8);
    int byte_m = (x & mask_m) >> (m * 8);
    return (x & ~(mask_n | mask_m)) | (byte_n << (m * 8)) | (byte_m << (n * 8));
}

int byteSwap_standard(int x, int n, int m) {
    unsigned char* bytes = (unsigned char*)&x;
    unsigned char temp = bytes[n];
    bytes[n] = bytes[m];
    bytes[m] = temp;
    return x;
}

// (11) 实现逻辑非(!)
int bang(int x) {
    int mask = x | (~x + 1); // 如果x为0，则mask为-1；否则为其他值
    return !((mask >> 31) & 1); // 如果x为0，返回1；否则返回0
}

int bang_standard(int x) {
    return !x;
}

// (12) 判断二进制中1的个数的奇偶性
int bitParity(int x) {
    x ^= x >> 16;
    x ^= x >> 8;
    x ^= x >> 4;
    x ^= x >> 2;
    x ^= x >> 1;
    return x & 1;
}

int bitParity_standard(int x) {
    int count = 0;
    while (x) {
        count += x & 1;
        x >>= 1;
    }
    return count % 2;
}

int main() {
    // 测试每个函数
    printf("absVal测试：");
    check(absVal, absVal_standard, -5);
    printf("negate测试：");
    check(negate, negate_standard, 5);
    printf("bitAnd测试：");
    check(bitAnd, bitAnd_standard, 5, 3);
    printf("bitOr测试：");
    check(bitOr, bitOr_standard, 5, 3);
    printf("bitXor测试：");
    check(bitXor, bitXor_standard, 5, 3);
    printf("isTmax测试：");
    check(isTmax, isTmax_standard, 0x7FFFFFFF);
    printf("bitCount测试：");
    check(bitCount, bitCount_standard, 5);
    printf("bitMask测试：");
    check(bitMask, bitMask_standard, 5, 3);
    printf("addOK测试：");
    check(addOK, addOK_standard, 0x7FFFFFFF, 1);
    printf("byteSwap测试：");
    check(byteSwap, byteSwap_standard, 0x12345678, 1, 3);
    printf("bang测试：");
    check(bang, bang_standard, 0);
    printf("bitParity测试：");
    check(bitParity, bitParity_standard, 5);
    return 0;
}