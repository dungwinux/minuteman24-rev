// clang -mllvm --x86-asm-syntax=intel -fno-verbose-asm --target=x86_64-pc-linux-unknown -S baby_asm.c -O0 -o baby_asm.s
unsigned long long baby(unsigned a) {
    // a = 1551273638
    a *= a;
    a += 1122488755;
    return a;
    // 2406449899953755044
}