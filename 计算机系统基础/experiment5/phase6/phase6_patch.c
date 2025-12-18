// phase6_patch.c
#include <stdio.h>

// 声明 phase 是外部定义在 phase6.o 中的函数指针
extern void (*phase)(int); 

// 自定义打印学号的函数
static void my_phase(int cookie) {
    printf("U202315594\n"); // 替换为你的学号
}

// 利用构造函数特性，在程序加载时劫持 phase 指针
__attribute__((constructor)) 
void hijack_phase() {
    phase = my_phase; // 将 phase 指向自定义函数
}