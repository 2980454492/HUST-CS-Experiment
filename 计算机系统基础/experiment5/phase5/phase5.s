
phase5.o:     file format elf64-x86-64


Disassembly of section .text:

0000000000000000 <do_phase>:
   0:	f3 0f 1e fa          	endbr64 
   4:	55                   	push   %rbp
   5:	48 89 e5             	mov    %rsp,%rbp
   8:	48 83 ec 10          	sub    $0x10,%rsp
   c:	89 7d fc             	mov    %edi,-0x4(%rbp)
   f:	48 8d 35 00 00 00 00 	lea    0x0(%rip),%rsi        # 16 <do_phase+0x16>
  16:	48 8d 3d 00 00 00 00 	lea    0x0(%rip),%rdi        # 1d <do_phase+0x1d>
  1d:	b8 00 00 00 00       	mov    $0x0,%eax
  22:	e8 00 00 00 00       	call   27 <do_phase+0x27>
  27:	48 8d 35 00 00 00 00 	lea    0x0(%rip),%rsi        # 2e <do_phase+0x2e>
  2e:	48 8d 3d 00 00 00 00 	lea    0x0(%rip),%rdi        # 35 <do_phase+0x35>
  35:	b8 00 00 00 00       	mov    $0x0,%eax
  3a:	e8 00 00 00 00       	call   3f <do_phase+0x3f>
  3f:	90                   	nop
  40:	90                   	nop
  41:	90                   	nop
  42:	90                   	nop
  43:	90                   	nop
  44:	90                   	nop
  45:	90                   	nop
  46:	90                   	nop
  47:	90                   	nop
  48:	90                   	nop
  49:	90                   	nop
  4a:	90                   	nop
  4b:	90                   	nop
  4c:	90                   	nop
  4d:	90                   	nop
  4e:	90                   	nop
  4f:	90                   	nop
  50:	90                   	nop
  51:	90                   	nop
  52:	90                   	nop
  53:	90                   	nop
  54:	90                   	nop
  55:	c9                   	leave  
  56:	c3                   	ret    
