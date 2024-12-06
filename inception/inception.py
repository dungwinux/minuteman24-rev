from keystone import *
from itertools import *
from random import seed, randrange

seed(0xc3c3c3c3)

ks = Ks(KS_ARCH_X86, KS_MODE_64)
def asm(s):
    enc, _ = ks.asm(s)
    return bytes(enc)

# program signature
# inception(success_function, failed_function, input)

# separate assembly instructions by ; or \n
decryptor_family = lambda key, size: """
    lea     r8, [rip + after_decrypt]
    add     cl, {}
decrypt:
    xor     byte ptr [r8 + rcx - 1], {}
    dec     rcx
    jnz     decrypt
after_decrypt:
""".format(size, key)

checker_family = lambda expected: """
    movzx   r8, byte ptr [r9 + rdx]
    inc     rdx
    sub     r8b, {}
    je      after_check
    jmp     rsi
after_check:
""".format(expected)


stub, _ = ks.asm(checker_family(2) + decryptor_family(1, 1))
stub_size = len(stub)

flag = "UMASS{s31f_d3cr4pti0n_iz_da_b3st}"

prolog = """
    mov     r9, rdx
    xor     edx, edx
    xor     ecx, ecx
"""

final = """
    jmp     rdi
"""

final_code, _ = ks.asm(final)
final_code = bytes(final_code)

prog = final_code

xor = lambda x, y: x ^ y
xorkey = lambda s, key: starmap(xor, zip(s, repeat(key)))

# print(bytes(xorkey("Hello, world".encode(), 0x1)).decode())

for ch in reversed(flag):
    c = ord(ch)
    d = randrange(0x100)
    # print(d)

    encrypted_prog = bytes(xorkey(prog[:stub_size], d))
    checker = asm(checker_family(c))
    decryptor = asm(decryptor_family(d, stub_size))
    prog = checker + decryptor + encrypted_prog + prog[stub_size:]

prog = asm(prolog) + prog


# print(bytes(prog).hex())
c_array = ", ".join(hex(x) for x in prog)
# print(c_array) 

blob = 'char const inception[] __attribute__((section(".inception, \\"wax\\""))) = {{ {} }};'.format(c_array)

c_code = blob + """
typedef int (*MessageFunc)();

typedef int (*InceptionFunc)(MessageFunc success, MessageFunc failed, char *user_input);

#include <stdio.h>

int success()
{
    puts("Success!");
    return 0;
}

int failed()
{
    puts("Incorrect!");
    return -1;
}

int main()
{
    char s[100] = {0};
    puts("Please input the flag:");
    if (scanf("%99s", s) == 0) {
        puts("Empty!");
        return -1;
    }
    return ((InceptionFunc)inception)(success, failed, s);
}
"""


with open("blob.c", "w") as fd:
    fd.write(c_code)