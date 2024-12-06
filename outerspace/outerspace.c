// clang-armv7a -O3
#ifndef uint8_t
#define uint8_t unsigned char
#endif

uint8_t convert(uint8_t q) __attribute__ ((minsize)) {
    switch (q) {
    case 1 ... 26:
        return q - 1 + 'a';
    case 27 ... 52:
        return q - 27 + 'A';
    case 53 ... 62:
        return q - 53 + '0';
    case 0:
        return '+';
    case 63:
        return '/';
    case 255:
        return ';';
    default:
        return 0;
      // padding ;
  }
}


#define PAD 255

uint8_t encode(uint8_t *a, uint8_t const *b) {
    unsigned ai = 0;
    unsigned bi = 0;
    unsigned b_length = 0;

    while (b[b_length] != 0) ++b_length;
    if (b_length == 0) return 0;

    for (; bi < b_length - 2; ai += 4, bi += 3) {
        a[ai + 0] = b[bi] >> 2;
        a[ai + 1] = ((b[bi] & 0b11) << 4) | (b[bi + 1] >> 4);
        a[ai + 2] = ((b[bi + 1] & 0b1111) << 2) | (b[bi + 2] >> 6);
        a[ai + 3] = b[bi + 2] & 0b111111;
    }
    if (b_length != bi) {
        a[ai + 0] = b[bi] >> 2;
        a[ai + 1] = ((b[bi] & 0b11) << 4) | (b[bi + 1] >> 4);
        a[ai + 3] = PAD;
        a[ai + 2] = (b_length - bi == 2) ? ((b[bi + 1] & 0b1111) << 2) | (b[bi + 2] >> 6) : PAD;
        ai += 4;
    }
    for (unsigned i = 0; i < ai; ++i) a[i] = convert(a[i]);
    a[ai] = 0;
    return ai;
}
