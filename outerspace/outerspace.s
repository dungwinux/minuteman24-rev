convert:
        add     r0, r0, #1
        and     r1, r0, #255
        mov     r0, #0
        cmp     r1, #64
        ldrls   r0, .LCPI0_0
.LPC0_0:
        addls   r0, pc, r0
        ldrbls  r0, [r0, r1]
        bx      lr
.LCPI0_0:
        .long   .Lswitch.table.convert-(.LPC0_0+8)

encode:
        push    {r4, r5, r6, r7, r8, lr}
        mov     r8, r0
        mvn     r0, #2
.LBB1_1:
        add     r2, r1, r0
        ldrb    r2, [r2, #3]
        add     r0, r0, #1
        cmp     r2, #0
        bne     .LBB1_1
        mov     r5, #0
        cmn     r0, #2
        beq     .LBB1_13
        mov     r2, #0
        cmp     r0, #0
        beq     .LBB1_5
.LBB1_4:
        mov     r3, r1
        ldrb    r7, [r3, r2]!
        lsr     r7, r7, #2
        mov     r4, r8
        strb    r7, [r4, r5]!
        ldrb    r7, [r3]
        ldrb    r6, [r3, #1]
        and     r7, r7, #3
        lsl     r7, r7, #4
        orr     r7, r7, r6, lsr #4
        strb    r7, [r4, #1]
        ldrb    r7, [r3, #1]
        ldrb    r6, [r3, #2]
        and     r7, r7, #15
        lsl     r7, r7, #2
        orr     r7, r7, r6, lsr #6
        strb    r7, [r4, #2]
        ldrb    r3, [r3, #2]
        and     r3, r3, #63
        strb    r3, [r4, #3]
        add     r2, r2, #3
        add     r5, r5, #4
        cmp     r2, r0
        blo     .LBB1_4
.LBB1_5:
        sub     r0, r0, r2
        cmn     r0, #2
        beq     .LBB1_9
        ldrb    r2, [r1, r2]!
        lsr     r2, r2, #2
        mov     r3, r8
        strb    r2, [r3, r5]!
        ldrb    r2, [r1]
        ldrb    r7, [r1, #1]
        and     r2, r2, #3
        lsl     r2, r2, #4
        orr     r2, r2, r7, lsr #4
        strb    r2, [r3, #1]
        mov     r2, #255
        cmp     r0, #0
        mov     r0, #255
        bne     .LBB1_8
        ldrb    r0, [r1, #1]
        ldrb    r1, [r1, #2]
        and     r0, r0, #15
        lsl     r0, r0, #2
        orr     r0, r0, r1, lsr #6
.LBB1_8:
        add     r1, r8, r5
        strb    r2, [r1, #3]
        strb    r0, [r1, #2]
        add     r5, r5, #4
.LBB1_9:
        cmp     r5, #0
        beq     .LBB1_12
        mov     r6, r8
        mov     r7, r5
.LBB1_11:
        ldrb    r0, [r6]
        bl      convert
        strb    r0, [r6], #1
        subs    r7, r7, #1
        bne     .LBB1_11
.LBB1_12:
        mov     r0, #0
        strb    r0, [r8, r5]
.LBB1_13:
        and     r0, r5, #255
        pop     {r4, r5, r6, r7, r8, lr}
        bx      lr

.Lswitch.table.convert:
        .ascii  ";+abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789/"