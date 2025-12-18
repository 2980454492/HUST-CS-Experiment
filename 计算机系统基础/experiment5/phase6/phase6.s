
phase6.o:     file format elf64-x86-64


Disassembly of section .text:

0000000000000000 <do_phase>:
   0:	f3 0f 1e fa          	endbr64 
   4:	55                   	push   %rbp
   5:	48 89 e5             	mov    %rsp,%rbp
   8:	48 83 ec 10          	sub    $0x10,%rsp
   c:	89 7d fc             	mov    %edi,-0x4(%rbp)
   f:	48 8b 05 00 00 00 00 	mov    0x0(%rip),%rax        # 16 <do_phase+0x16>
  16:	48 85 c0             	test   %rax,%rax
  19:	74 10                	je     2b <do_phase+0x2b>
  1b:	48 8b 15 00 00 00 00 	mov    0x0(%rip),%rdx        # 22 <do_phase+0x22>
  22:	b8 00 00 00 00       	mov    $0x0,%eax
  27:	ff d2                	call   *%rdx
  29:	eb 0c                	jmp    37 <do_phase+0x37>
  2b:	48 8d 3d 00 00 00 00 	lea    0x0(%rip),%rdi        # 32 <do_phase+0x32>
  32:	e8 00 00 00 00       	call   37 <do_phase+0x37>
  37:	90                   	nop
  38:	c9                   	leave  
  39:	c3                   	ret    
