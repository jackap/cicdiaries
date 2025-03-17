This simple program helps on finding and exploiting a buffer overflow https://bytesoverbombs.io/exploiting-a-64-bit-buffer-overflow-469e8b500f10

## How to compile
`gcc -o exploit main.c -fno-stack-protector -D_FORTIFY_SOURCE=0 -no-pie -fno-PIE`
In this way the program can be hacked

First thing to do after compiling is analyze the source with IDA or GDB like in this case.

1) disassemble vuln

I run GDB and set a breakpoint at the end of the program.	
2) break *\*(endpoint)*

Then we create a hook-stop (define hook-stop) that will display:
```sh
Use rip if 64 bit or eip if 32 bit
x/1i $rip that is the HEX value of the content of the instruction pointer 

x/8wx $rsp examin 8 words in the stack

end 

then r to run 
```
Next we want to check rsp and rbp before the read function
```bash
(gdb) x $rsp 
0x7fffffffe240:	0xffffffff

(gdb) x $rbp
0x7fffffffe3e0:	0xffffe400


The content of the stack at rbp is:
0x7fffffffe2e0:	0x00000000	0x00000000	0xf7de6ac6	0x00007fff

NEXT we repeat with a pattern such that we know the number of chars to use:

0x7fffffffe3e0:	0x396e4138	0x41306f41	0x6f41316f	0x336f4132


Program received signal SIGSEGV, Segmentation fault.
0x0000000000400606 in vuln ()

then 
0x00007fffffffe120 in ?? ()
```








