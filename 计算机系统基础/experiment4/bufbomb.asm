
bufbomb:     file format elf64-x86-64


Disassembly of section .init:

0000000000401000 <_init>:
  401000:	f3 0f 1e fa          	endbr64 
  401004:	48 83 ec 08          	sub    $0x8,%rsp
  401008:	48 8b 05 e9 2f 00 00 	mov    0x2fe9(%rip),%rax        # 403ff8 <__gmon_start__@Base>
  40100f:	48 85 c0             	test   %rax,%rax
  401012:	74 02                	je     401016 <_init+0x16>
  401014:	ff d0                	call   *%rax
  401016:	48 83 c4 08          	add    $0x8,%rsp
  40101a:	c3                   	ret    

Disassembly of section .plt:

0000000000401020 <free@plt-0x10>:
  401020:	ff 35 e2 2f 00 00    	push   0x2fe2(%rip)        # 404008 <_GLOBAL_OFFSET_TABLE_+0x8>
  401026:	ff 25 e4 2f 00 00    	jmp    *0x2fe4(%rip)        # 404010 <_GLOBAL_OFFSET_TABLE_+0x10>
  40102c:	0f 1f 40 00          	nopl   0x0(%rax)

0000000000401030 <free@plt>:
  401030:	ff 25 e2 2f 00 00    	jmp    *0x2fe2(%rip)        # 404018 <free@GLIBC_2.2.5>
  401036:	68 00 00 00 00       	push   $0x0
  40103b:	e9 e0 ff ff ff       	jmp    401020 <_init+0x20>

0000000000401040 <strcpy@plt>:
  401040:	ff 25 da 2f 00 00    	jmp    *0x2fda(%rip)        # 404020 <strcpy@GLIBC_2.2.5>
  401046:	68 01 00 00 00       	push   $0x1
  40104b:	e9 d0 ff ff ff       	jmp    401020 <_init+0x20>

0000000000401050 <__isoc99_fscanf@plt>:
  401050:	ff 25 d2 2f 00 00    	jmp    *0x2fd2(%rip)        # 404028 <__isoc99_fscanf@GLIBC_2.7>
  401056:	68 02 00 00 00       	push   $0x2
  40105b:	e9 c0 ff ff ff       	jmp    401020 <_init+0x20>

0000000000401060 <puts@plt>:
  401060:	ff 25 ca 2f 00 00    	jmp    *0x2fca(%rip)        # 404030 <puts@GLIBC_2.2.5>
  401066:	68 03 00 00 00       	push   $0x3
  40106b:	e9 b0 ff ff ff       	jmp    401020 <_init+0x20>

0000000000401070 <fclose@plt>:
  401070:	ff 25 c2 2f 00 00    	jmp    *0x2fc2(%rip)        # 404038 <fclose@GLIBC_2.2.5>
  401076:	68 04 00 00 00       	push   $0x4
  40107b:	e9 a0 ff ff ff       	jmp    401020 <_init+0x20>

0000000000401080 <strlen@plt>:
  401080:	ff 25 ba 2f 00 00    	jmp    *0x2fba(%rip)        # 404040 <strlen@GLIBC_2.2.5>
  401086:	68 05 00 00 00       	push   $0x5
  40108b:	e9 90 ff ff ff       	jmp    401020 <_init+0x20>

0000000000401090 <printf@plt>:
  401090:	ff 25 b2 2f 00 00    	jmp    *0x2fb2(%rip)        # 404048 <printf@GLIBC_2.2.5>
  401096:	68 06 00 00 00       	push   $0x6
  40109b:	e9 80 ff ff ff       	jmp    401020 <_init+0x20>

00000000004010a0 <strcmp@plt>:
  4010a0:	ff 25 aa 2f 00 00    	jmp    *0x2faa(%rip)        # 404050 <strcmp@GLIBC_2.2.5>
  4010a6:	68 07 00 00 00       	push   $0x7
  4010ab:	e9 70 ff ff ff       	jmp    401020 <_init+0x20>

00000000004010b0 <fprintf@plt>:
  4010b0:	ff 25 a2 2f 00 00    	jmp    *0x2fa2(%rip)        # 404058 <fprintf@GLIBC_2.2.5>
  4010b6:	68 08 00 00 00       	push   $0x8
  4010bb:	e9 60 ff ff ff       	jmp    401020 <_init+0x20>

00000000004010c0 <memcpy@plt>:
  4010c0:	ff 25 9a 2f 00 00    	jmp    *0x2f9a(%rip)        # 404060 <memcpy@GLIBC_2.14>
  4010c6:	68 09 00 00 00       	push   $0x9
  4010cb:	e9 50 ff ff ff       	jmp    401020 <_init+0x20>

00000000004010d0 <malloc@plt>:
  4010d0:	ff 25 92 2f 00 00    	jmp    *0x2f92(%rip)        # 404068 <malloc@GLIBC_2.2.5>
  4010d6:	68 0a 00 00 00       	push   $0xa
  4010db:	e9 40 ff ff ff       	jmp    401020 <_init+0x20>

00000000004010e0 <__isoc99_sscanf@plt>:
  4010e0:	ff 25 8a 2f 00 00    	jmp    *0x2f8a(%rip)        # 404070 <__isoc99_sscanf@GLIBC_2.7>
  4010e6:	68 0b 00 00 00       	push   $0xb
  4010eb:	e9 30 ff ff ff       	jmp    401020 <_init+0x20>

00000000004010f0 <realloc@plt>:
  4010f0:	ff 25 82 2f 00 00    	jmp    *0x2f82(%rip)        # 404078 <realloc@GLIBC_2.2.5>
  4010f6:	68 0c 00 00 00       	push   $0xc
  4010fb:	e9 20 ff ff ff       	jmp    401020 <_init+0x20>

0000000000401100 <fopen@plt>:
  401100:	ff 25 7a 2f 00 00    	jmp    *0x2f7a(%rip)        # 404080 <fopen@GLIBC_2.2.5>
  401106:	68 0d 00 00 00       	push   $0xd
  40110b:	e9 10 ff ff ff       	jmp    401020 <_init+0x20>

0000000000401110 <atoi@plt>:
  401110:	ff 25 72 2f 00 00    	jmp    *0x2f72(%rip)        # 404088 <atoi@GLIBC_2.2.5>
  401116:	68 0e 00 00 00       	push   $0xe
  40111b:	e9 00 ff ff ff       	jmp    401020 <_init+0x20>

0000000000401120 <exit@plt>:
  401120:	ff 25 6a 2f 00 00    	jmp    *0x2f6a(%rip)        # 404090 <exit@GLIBC_2.2.5>
  401126:	68 0f 00 00 00       	push   $0xf
  40112b:	e9 f0 fe ff ff       	jmp    401020 <_init+0x20>

0000000000401130 <__ctype_b_loc@plt>:
  401130:	ff 25 62 2f 00 00    	jmp    *0x2f62(%rip)        # 404098 <__ctype_b_loc@GLIBC_2.3>
  401136:	68 10 00 00 00       	push   $0x10
  40113b:	e9 e0 fe ff ff       	jmp    401020 <_init+0x20>

Disassembly of section .text:

0000000000401140 <_start>:
  401140:	f3 0f 1e fa          	endbr64 
  401144:	31 ed                	xor    %ebp,%ebp
  401146:	49 89 d1             	mov    %rdx,%r9
  401149:	5e                   	pop    %rsi
  40114a:	48 89 e2             	mov    %rsp,%rdx
  40114d:	48 83 e4 f0          	and    $0xfffffffffffffff0,%rsp
  401151:	50                   	push   %rax
  401152:	54                   	push   %rsp
  401153:	45 31 c0             	xor    %r8d,%r8d
  401156:	31 c9                	xor    %ecx,%ecx
  401158:	48 c7 c7 f2 15 40 00 	mov    $0x4015f2,%rdi
  40115f:	ff 15 8b 2e 00 00    	call   *0x2e8b(%rip)        # 403ff0 <__libc_start_main@GLIBC_2.34>
  401165:	f4                   	hlt    
  401166:	66 2e 0f 1f 84 00 00 	cs nopw 0x0(%rax,%rax,1)
  40116d:	00 00 00 

0000000000401170 <_dl_relocate_static_pie>:
  401170:	f3 0f 1e fa          	endbr64 
  401174:	c3                   	ret    
  401175:	66 2e 0f 1f 84 00 00 	cs nopw 0x0(%rax,%rax,1)
  40117c:	00 00 00 
  40117f:	90                   	nop

0000000000401180 <deregister_tm_clones>:
  401180:	b8 c0 40 40 00       	mov    $0x4040c0,%eax
  401185:	48 3d c0 40 40 00    	cmp    $0x4040c0,%rax
  40118b:	74 13                	je     4011a0 <deregister_tm_clones+0x20>
  40118d:	b8 00 00 00 00       	mov    $0x0,%eax
  401192:	48 85 c0             	test   %rax,%rax
  401195:	74 09                	je     4011a0 <deregister_tm_clones+0x20>
  401197:	bf c0 40 40 00       	mov    $0x4040c0,%edi
  40119c:	ff e0                	jmp    *%rax
  40119e:	66 90                	xchg   %ax,%ax
  4011a0:	c3                   	ret    
  4011a1:	66 66 2e 0f 1f 84 00 	data16 cs nopw 0x0(%rax,%rax,1)
  4011a8:	00 00 00 00 
  4011ac:	0f 1f 40 00          	nopl   0x0(%rax)

00000000004011b0 <register_tm_clones>:
  4011b0:	be c0 40 40 00       	mov    $0x4040c0,%esi
  4011b5:	48 81 ee c0 40 40 00 	sub    $0x4040c0,%rsi
  4011bc:	48 89 f0             	mov    %rsi,%rax
  4011bf:	48 c1 ee 3f          	shr    $0x3f,%rsi
  4011c3:	48 c1 f8 03          	sar    $0x3,%rax
  4011c7:	48 01 c6             	add    %rax,%rsi
  4011ca:	48 d1 fe             	sar    %rsi
  4011cd:	74 11                	je     4011e0 <register_tm_clones+0x30>
  4011cf:	b8 00 00 00 00       	mov    $0x0,%eax
  4011d4:	48 85 c0             	test   %rax,%rax
  4011d7:	74 07                	je     4011e0 <register_tm_clones+0x30>
  4011d9:	bf c0 40 40 00       	mov    $0x4040c0,%edi
  4011de:	ff e0                	jmp    *%rax
  4011e0:	c3                   	ret    
  4011e1:	66 66 2e 0f 1f 84 00 	data16 cs nopw 0x0(%rax,%rax,1)
  4011e8:	00 00 00 00 
  4011ec:	0f 1f 40 00          	nopl   0x0(%rax)

00000000004011f0 <__do_global_dtors_aux>:
  4011f0:	f3 0f 1e fa          	endbr64 
  4011f4:	80 3d cd 2e 00 00 00 	cmpb   $0x0,0x2ecd(%rip)        # 4040c8 <completed.0>
  4011fb:	75 13                	jne    401210 <__do_global_dtors_aux+0x20>
  4011fd:	55                   	push   %rbp
  4011fe:	48 89 e5             	mov    %rsp,%rbp
  401201:	e8 7a ff ff ff       	call   401180 <deregister_tm_clones>
  401206:	c6 05 bb 2e 00 00 01 	movb   $0x1,0x2ebb(%rip)        # 4040c8 <completed.0>
  40120d:	5d                   	pop    %rbp
  40120e:	c3                   	ret    
  40120f:	90                   	nop
  401210:	c3                   	ret    
  401211:	66 66 2e 0f 1f 84 00 	data16 cs nopw 0x0(%rax,%rax,1)
  401218:	00 00 00 00 
  40121c:	0f 1f 40 00          	nopl   0x0(%rax)

0000000000401220 <frame_dummy>:
  401220:	f3 0f 1e fa          	endbr64 
  401224:	eb 8a                	jmp    4011b0 <register_tm_clones>

0000000000401226 <initialize_bomb>:
  401226:	55                   	push   %rbp
  401227:	48 89 e5             	mov    %rsp,%rbp
  40122a:	48 83 ec 30          	sub    $0x30,%rsp
  40122e:	48 89 7d d8          	mov    %rdi,-0x28(%rbp)
  401232:	c7 45 fc 0a 00 00 00 	movl   $0xa,-0x4(%rbp)
  401239:	c7 45 f8 14 00 00 00 	movl   $0x14,-0x8(%rbp)
  401240:	c7 45 f4 1e 00 00 00 	movl   $0x1e,-0xc(%rbp)
  401247:	c7 45 f0 28 00 00 00 	movl   $0x28,-0x10(%rbp)
  40124e:	c7 45 ec 32 00 00 00 	movl   $0x32,-0x14(%rbp)
  401255:	c7 45 e8 3c 00 00 00 	movl   $0x3c,-0x18(%rbp)
  40125c:	48 8b 45 d8          	mov    -0x28(%rbp),%rax
  401260:	48 89 c7             	mov    %rax,%rdi
  401263:	e8 18 fe ff ff       	call   401080 <strlen@plt>
  401268:	89 45 e4             	mov    %eax,-0x1c(%rbp)
  40126b:	83 7d e4 0a          	cmpl   $0xa,-0x1c(%rbp)
  40126f:	74 19                	je     40128a <initialize_bomb+0x64>
  401271:	48 8d 05 90 0d 00 00 	lea    0xd90(%rip),%rax        # 402008 <_IO_stdin_used+0x8>
  401278:	48 89 c7             	mov    %rax,%rdi
  40127b:	e8 e0 fd ff ff       	call   401060 <puts@plt>
  401280:	bf 00 00 00 00       	mov    $0x0,%edi
  401285:	e8 96 fe ff ff       	call   401120 <exit@plt>
  40128a:	48 8b 45 d8          	mov    -0x28(%rbp),%rax
  40128e:	48 89 c6             	mov    %rax,%rsi
  401291:	48 8d 05 aa 0d 00 00 	lea    0xdaa(%rip),%rax        # 402042 <_IO_stdin_used+0x42>
  401298:	48 89 c7             	mov    %rax,%rdi
  40129b:	b8 00 00 00 00       	mov    $0x0,%eax
  4012a0:	e8 eb fd ff ff       	call   401090 <printf@plt>
  4012a5:	8b 45 e4             	mov    -0x1c(%rbp),%eax
  4012a8:	48 98                	cltq   
  4012aa:	48 8d 50 ff          	lea    -0x1(%rax),%rdx
  4012ae:	48 8b 45 d8          	mov    -0x28(%rbp),%rax
  4012b2:	48 01 d0             	add    %rdx,%rax
  4012b5:	0f b6 00             	movzbl (%rax),%eax
  4012b8:	3c 34                	cmp    $0x34,%al
  4012ba:	75 31                	jne    4012ed <initialize_bomb+0xc7>
  4012bc:	8b 45 fc             	mov    -0x4(%rbp),%eax
  4012bf:	8d 0c 00             	lea    (%rax,%rax,1),%ecx
  4012c2:	8b 55 f8             	mov    -0x8(%rbp),%edx
  4012c5:	89 d0                	mov    %edx,%eax
  4012c7:	01 c0                	add    %eax,%eax
  4012c9:	01 d0                	add    %edx,%eax
  4012cb:	8d 14 01             	lea    (%rcx,%rax,1),%edx
  4012ce:	8b 45 f0             	mov    -0x10(%rbp),%eax
  4012d1:	c1 e0 02             	shl    $0x2,%eax
  4012d4:	01 c2                	add    %eax,%edx
  4012d6:	8b 45 fc             	mov    -0x4(%rbp),%eax
  4012d9:	8d 0c 02             	lea    (%rdx,%rax,1),%ecx
  4012dc:	8b 55 e8             	mov    -0x18(%rbp),%edx
  4012df:	89 d0                	mov    %edx,%eax
  4012e1:	c1 e0 02             	shl    $0x2,%eax
  4012e4:	01 d0                	add    %edx,%eax
  4012e6:	01 c8                	add    %ecx,%eax
  4012e8:	89 45 e8             	mov    %eax,-0x18(%rbp)
  4012eb:	eb 37                	jmp    401324 <initialize_bomb+0xfe>
  4012ed:	48 8d 05 5c 0d 00 00 	lea    0xd5c(%rip),%rax        # 402050 <_IO_stdin_used+0x50>
  4012f4:	48 89 c7             	mov    %rax,%rdi
  4012f7:	e8 64 fd ff ff       	call   401060 <puts@plt>
  4012fc:	48 8d 05 85 0d 00 00 	lea    0xd85(%rip),%rax        # 402088 <_IO_stdin_used+0x88>
  401303:	48 89 c7             	mov    %rax,%rdi
  401306:	e8 55 fd ff ff       	call   401060 <puts@plt>
  40130b:	48 8d 05 ae 0d 00 00 	lea    0xdae(%rip),%rax        # 4020c0 <_IO_stdin_used+0xc0>
  401312:	48 89 c7             	mov    %rax,%rdi
  401315:	e8 46 fd ff ff       	call   401060 <puts@plt>
  40131a:	bf 00 00 00 00       	mov    $0x0,%edi
  40131f:	e8 fc fd ff ff       	call   401120 <exit@plt>
  401324:	c9                   	leave  
  401325:	c3                   	ret    

0000000000401326 <smoke>:
  401326:	55                   	push   %rbp
  401327:	48 89 e5             	mov    %rsp,%rbp
  40132a:	48 8d 05 b5 0d 00 00 	lea    0xdb5(%rip),%rax        # 4020e6 <_IO_stdin_used+0xe6>
  401331:	48 89 c7             	mov    %rax,%rdi
  401334:	e8 27 fd ff ff       	call   401060 <puts@plt>
  401339:	bf 00 00 00 00       	mov    $0x0,%edi
  40133e:	e8 dd fd ff ff       	call   401120 <exit@plt>

0000000000401343 <fizz>:
  401343:	55                   	push   %rbp
  401344:	48 89 e5             	mov    %rsp,%rbp
  401347:	48 83 ec 10          	sub    $0x10,%rsp
  40134b:	89 7d fc             	mov    %edi,-0x4(%rbp)
  40134e:	8b 05 94 2d 00 00    	mov    0x2d94(%rip),%eax        # 4040e8 <cookie>
  401354:	39 45 fc             	cmp    %eax,-0x4(%rbp)
  401357:	75 1b                	jne    401374 <fizz+0x31>
  401359:	8b 45 fc             	mov    -0x4(%rbp),%eax
  40135c:	89 c6                	mov    %eax,%esi
  40135e:	48 8d 05 9c 0d 00 00 	lea    0xd9c(%rip),%rax        # 402101 <_IO_stdin_used+0x101>
  401365:	48 89 c7             	mov    %rax,%rdi
  401368:	b8 00 00 00 00       	mov    $0x0,%eax
  40136d:	e8 1e fd ff ff       	call   401090 <printf@plt>
  401372:	eb 19                	jmp    40138d <fizz+0x4a>
  401374:	8b 45 fc             	mov    -0x4(%rbp),%eax
  401377:	89 c6                	mov    %eax,%esi
  401379:	48 8d 05 a0 0d 00 00 	lea    0xda0(%rip),%rax        # 402120 <_IO_stdin_used+0x120>
  401380:	48 89 c7             	mov    %rax,%rdi
  401383:	b8 00 00 00 00       	mov    $0x0,%eax
  401388:	e8 03 fd ff ff       	call   401090 <printf@plt>
  40138d:	bf 00 00 00 00       	mov    $0x0,%edi
  401392:	e8 89 fd ff ff       	call   401120 <exit@plt>

0000000000401397 <bang>:
  401397:	55                   	push   %rbp
  401398:	48 89 e5             	mov    %rsp,%rbp
  40139b:	48 83 ec 10          	sub    $0x10,%rsp
  40139f:	89 7d fc             	mov    %edi,-0x4(%rbp)
  4013a2:	8b 15 44 2d 00 00    	mov    0x2d44(%rip),%edx        # 4040ec <global_value>
  4013a8:	8b 05 3a 2d 00 00    	mov    0x2d3a(%rip),%eax        # 4040e8 <cookie>
  4013ae:	39 c2                	cmp    %eax,%edx
  4013b0:	75 1e                	jne    4013d0 <bang+0x39>
  4013b2:	8b 05 34 2d 00 00    	mov    0x2d34(%rip),%eax        # 4040ec <global_value>
  4013b8:	89 c6                	mov    %eax,%esi
  4013ba:	48 8d 05 7f 0d 00 00 	lea    0xd7f(%rip),%rax        # 402140 <_IO_stdin_used+0x140>
  4013c1:	48 89 c7             	mov    %rax,%rdi
  4013c4:	b8 00 00 00 00       	mov    $0x0,%eax
  4013c9:	e8 c2 fc ff ff       	call   401090 <printf@plt>
  4013ce:	eb 1c                	jmp    4013ec <bang+0x55>
  4013d0:	8b 05 16 2d 00 00    	mov    0x2d16(%rip),%eax        # 4040ec <global_value>
  4013d6:	89 c6                	mov    %eax,%esi
  4013d8:	48 8d 05 86 0d 00 00 	lea    0xd86(%rip),%rax        # 402165 <_IO_stdin_used+0x165>
  4013df:	48 89 c7             	mov    %rax,%rdi
  4013e2:	b8 00 00 00 00       	mov    $0x0,%eax
  4013e7:	e8 a4 fc ff ff       	call   401090 <printf@plt>
  4013ec:	bf 00 00 00 00       	mov    $0x0,%edi
  4013f1:	e8 2a fd ff ff       	call   401120 <exit@plt>

00000000004013f6 <test>:
  4013f6:	55                   	push   %rbp
  4013f7:	48 89 e5             	mov    %rsp,%rbp
  4013fa:	48 83 ec 30          	sub    $0x30,%rsp
  4013fe:	48 89 7d d8          	mov    %rdi,-0x28(%rbp)
  401402:	c7 45 f8 00 00 00 00 	movl   $0x0,-0x8(%rbp)
  401409:	48 8b 45 d8          	mov    -0x28(%rbp),%rax
  40140d:	8b 40 7c             	mov    0x7c(%rax),%eax
  401410:	85 c0                	test   %eax,%eax
  401412:	74 24                	je     401438 <test+0x42>
  401414:	48 8b 45 d8          	mov    -0x28(%rbp),%rax
  401418:	8b 40 7c             	mov    0x7c(%rax),%eax
  40141b:	83 f8 01             	cmp    $0x1,%eax
  40141e:	74 18                	je     401438 <test+0x42>
  401420:	48 8b 45 d8          	mov    -0x28(%rbp),%rax
  401424:	8b 40 7c             	mov    0x7c(%rax),%eax
  401427:	83 f8 02             	cmp    $0x2,%eax
  40142a:	74 0c                	je     401438 <test+0x42>
  40142c:	48 8b 45 d8          	mov    -0x28(%rbp),%rax
  401430:	8b 40 7c             	mov    0x7c(%rax),%eax
  401433:	83 f8 03             	cmp    $0x3,%eax
  401436:	75 75                	jne    4014ad <test+0xb7>
  401438:	48 8b 45 d8          	mov    -0x28(%rbp),%rax
  40143c:	48 8d 15 40 0d 00 00 	lea    0xd40(%rip),%rdx        # 402183 <_IO_stdin_used+0x183>
  401443:	48 89 d6             	mov    %rdx,%rsi
  401446:	48 89 c7             	mov    %rax,%rdi
  401449:	e8 b2 fc ff ff       	call   401100 <fopen@plt>
  40144e:	48 89 45 f0          	mov    %rax,-0x10(%rbp)
  401452:	48 83 7d f0 00       	cmpq   $0x0,-0x10(%rbp)
  401457:	75 1d                	jne    401476 <test+0x80>
  401459:	48 8b 45 d8          	mov    -0x28(%rbp),%rax
  40145d:	48 89 c6             	mov    %rax,%rsi
  401460:	48 8d 05 1e 0d 00 00 	lea    0xd1e(%rip),%rax        # 402185 <_IO_stdin_used+0x185>
  401467:	48 89 c7             	mov    %rax,%rdi
  40146a:	b8 00 00 00 00       	mov    $0x0,%eax
  40146f:	e8 1c fc ff ff       	call   401090 <printf@plt>
  401474:	eb 76                	jmp    4014ec <test+0xf6>
  401476:	48 8d 55 e4          	lea    -0x1c(%rbp),%rdx
  40147a:	48 8b 45 f0          	mov    -0x10(%rbp),%rax
  40147e:	48 89 d6             	mov    %rdx,%rsi
  401481:	48 89 c7             	mov    %rax,%rdi
  401484:	e8 44 03 00 00       	call   4017cd <convert_to_byte_string>
  401489:	48 89 45 e8          	mov    %rax,-0x18(%rbp)
  40148d:	48 8b 45 f0          	mov    -0x10(%rbp),%rax
  401491:	48 89 c7             	mov    %rax,%rdi
  401494:	e8 d7 fb ff ff       	call   401070 <fclose@plt>
  401499:	8b 55 e4             	mov    -0x1c(%rbp),%edx
  40149c:	48 8b 45 e8          	mov    -0x18(%rbp),%rax
  4014a0:	89 d6                	mov    %edx,%esi
  4014a2:	48 89 c7             	mov    %rax,%rdi
  4014a5:	e8 d9 05 00 00       	call   401a83 <getbuf>
  4014aa:	89 45 fc             	mov    %eax,-0x4(%rbp)
  4014ad:	8b 05 35 2c 00 00    	mov    0x2c35(%rip),%eax        # 4040e8 <cookie>
  4014b3:	39 45 fc             	cmp    %eax,-0x4(%rbp)
  4014b6:	75 1b                	jne    4014d3 <test+0xdd>
  4014b8:	8b 45 fc             	mov    -0x4(%rbp),%eax
  4014bb:	89 c6                	mov    %eax,%esi
  4014bd:	48 8d 05 dd 0c 00 00 	lea    0xcdd(%rip),%rax        # 4021a1 <_IO_stdin_used+0x1a1>
  4014c4:	48 89 c7             	mov    %rax,%rdi
  4014c7:	b8 00 00 00 00       	mov    $0x0,%eax
  4014cc:	e8 bf fb ff ff       	call   401090 <printf@plt>
  4014d1:	eb 19                	jmp    4014ec <test+0xf6>
  4014d3:	8b 45 fc             	mov    -0x4(%rbp),%eax
  4014d6:	89 c6                	mov    %eax,%esi
  4014d8:	48 8d 05 df 0c 00 00 	lea    0xcdf(%rip),%rax        # 4021be <_IO_stdin_used+0x1be>
  4014df:	48 89 c7             	mov    %rax,%rdi
  4014e2:	b8 00 00 00 00       	mov    $0x0,%eax
  4014e7:	e8 a4 fb ff ff       	call   401090 <printf@plt>
  4014ec:	c9                   	leave  
  4014ed:	c3                   	ret    

00000000004014ee <save_char>:
  4014ee:	55                   	push   %rbp
  4014ef:	48 89 e5             	mov    %rsp,%rbp
  4014f2:	89 f8                	mov    %edi,%eax
  4014f4:	88 45 fc             	mov    %al,-0x4(%rbp)
  4014f7:	8b 05 f3 2b 00 00    	mov    0x2bf3(%rip),%eax        # 4040f0 <gets_cnt>
  4014fd:	3d ff 03 00 00       	cmp    $0x3ff,%eax
  401502:	0f 8f 95 00 00 00    	jg     40159d <save_char+0xaf>
  401508:	0f b6 45 fc          	movzbl -0x4(%rbp),%eax
  40150c:	c0 f8 04             	sar    $0x4,%al
  40150f:	0f be c0             	movsbl %al,%eax
  401512:	83 e0 0f             	and    $0xf,%eax
  401515:	89 c6                	mov    %eax,%esi
  401517:	8b 15 d3 2b 00 00    	mov    0x2bd3(%rip),%edx        # 4040f0 <gets_cnt>
  40151d:	89 d0                	mov    %edx,%eax
  40151f:	01 c0                	add    %eax,%eax
  401521:	8d 0c 10             	lea    (%rax,%rdx,1),%ecx
  401524:	48 63 c6             	movslq %esi,%rax
  401527:	48 8d 15 82 2b 00 00 	lea    0x2b82(%rip),%rdx        # 4040b0 <trans_char>
  40152e:	0f b6 14 10          	movzbl (%rax,%rdx,1),%edx
  401532:	48 63 c1             	movslq %ecx,%rax
  401535:	48 8d 0d c4 2b 00 00 	lea    0x2bc4(%rip),%rcx        # 404100 <gets_buf>
  40153c:	88 14 08             	mov    %dl,(%rax,%rcx,1)
  40153f:	0f be 45 fc          	movsbl -0x4(%rbp),%eax
  401543:	83 e0 0f             	and    $0xf,%eax
  401546:	89 c6                	mov    %eax,%esi
  401548:	8b 15 a2 2b 00 00    	mov    0x2ba2(%rip),%edx        # 4040f0 <gets_cnt>
  40154e:	89 d0                	mov    %edx,%eax
  401550:	01 c0                	add    %eax,%eax
  401552:	01 d0                	add    %edx,%eax
  401554:	8d 48 01             	lea    0x1(%rax),%ecx
  401557:	48 63 c6             	movslq %esi,%rax
  40155a:	48 8d 15 4f 2b 00 00 	lea    0x2b4f(%rip),%rdx        # 4040b0 <trans_char>
  401561:	0f b6 14 10          	movzbl (%rax,%rdx,1),%edx
  401565:	48 63 c1             	movslq %ecx,%rax
  401568:	48 8d 0d 91 2b 00 00 	lea    0x2b91(%rip),%rcx        # 404100 <gets_buf>
  40156f:	88 14 08             	mov    %dl,(%rax,%rcx,1)
  401572:	8b 15 78 2b 00 00    	mov    0x2b78(%rip),%edx        # 4040f0 <gets_cnt>
  401578:	89 d0                	mov    %edx,%eax
  40157a:	01 c0                	add    %eax,%eax
  40157c:	01 d0                	add    %edx,%eax
  40157e:	83 c0 02             	add    $0x2,%eax
  401581:	48 98                	cltq   
  401583:	48 8d 15 76 2b 00 00 	lea    0x2b76(%rip),%rdx        # 404100 <gets_buf>
  40158a:	c6 04 10 20          	movb   $0x20,(%rax,%rdx,1)
  40158e:	8b 05 5c 2b 00 00    	mov    0x2b5c(%rip),%eax        # 4040f0 <gets_cnt>
  401594:	83 c0 01             	add    $0x1,%eax
  401597:	89 05 53 2b 00 00    	mov    %eax,0x2b53(%rip)        # 4040f0 <gets_cnt>
  40159d:	90                   	nop
  40159e:	5d                   	pop    %rbp
  40159f:	c3                   	ret    

00000000004015a0 <save_term>:
  4015a0:	55                   	push   %rbp
  4015a1:	48 89 e5             	mov    %rsp,%rbp
  4015a4:	8b 15 46 2b 00 00    	mov    0x2b46(%rip),%edx        # 4040f0 <gets_cnt>
  4015aa:	89 d0                	mov    %edx,%eax
  4015ac:	01 c0                	add    %eax,%eax
  4015ae:	01 d0                	add    %edx,%eax
  4015b0:	48 98                	cltq   
  4015b2:	48 8d 15 47 2b 00 00 	lea    0x2b47(%rip),%rdx        # 404100 <gets_buf>
  4015b9:	c6 04 10 00          	movb   $0x0,(%rax,%rdx,1)
  4015bd:	90                   	nop
  4015be:	5d                   	pop    %rbp
  4015bf:	c3                   	ret    

00000000004015c0 <Gets>:
  4015c0:	55                   	push   %rbp
  4015c1:	48 89 e5             	mov    %rsp,%rbp
  4015c4:	48 83 ec 20          	sub    $0x20,%rsp
  4015c8:	48 89 7d f8          	mov    %rdi,-0x8(%rbp)
  4015cc:	48 89 75 f0          	mov    %rsi,-0x10(%rbp)
  4015d0:	89 55 ec             	mov    %edx,-0x14(%rbp)
  4015d3:	8b 45 ec             	mov    -0x14(%rbp),%eax
  4015d6:	48 63 d0             	movslq %eax,%rdx
  4015d9:	48 8b 4d f0          	mov    -0x10(%rbp),%rcx
  4015dd:	48 8b 45 f8          	mov    -0x8(%rbp),%rax
  4015e1:	48 89 ce             	mov    %rcx,%rsi
  4015e4:	48 89 c7             	mov    %rax,%rdi
  4015e7:	e8 d4 fa ff ff       	call   4010c0 <memcpy@plt>
  4015ec:	48 8b 45 f8          	mov    -0x8(%rbp),%rax
  4015f0:	c9                   	leave  
  4015f1:	c3                   	ret    

00000000004015f2 <main>:
  4015f2:	55                   	push   %rbp
  4015f3:	48 89 e5             	mov    %rsp,%rbp
  4015f6:	48 81 ec 90 00 00 00 	sub    $0x90,%rsp
  4015fd:	89 bd 7c ff ff ff    	mov    %edi,-0x84(%rbp)
  401603:	48 89 b5 70 ff ff ff 	mov    %rsi,-0x90(%rbp)
  40160a:	83 bd 7c ff ff ff 03 	cmpl   $0x3,-0x84(%rbp)
  401611:	7f 3a                	jg     40164d <main+0x5b>
  401613:	48 8b 85 70 ff ff ff 	mov    -0x90(%rbp),%rax
  40161a:	48 8b 00             	mov    (%rax),%rax
  40161d:	48 89 c6             	mov    %rax,%rsi
  401620:	48 8d 05 b9 0b 00 00 	lea    0xbb9(%rip),%rax        # 4021e0 <_IO_stdin_used+0x1e0>
  401627:	48 89 c7             	mov    %rax,%rdi
  40162a:	b8 00 00 00 00       	mov    $0x0,%eax
  40162f:	e8 5c fa ff ff       	call   401090 <printf@plt>
  401634:	48 8d 05 d5 0b 00 00 	lea    0xbd5(%rip),%rax        # 402210 <_IO_stdin_used+0x210>
  40163b:	48 89 c7             	mov    %rax,%rdi
  40163e:	e8 1d fa ff ff       	call   401060 <puts@plt>
  401643:	b8 00 00 00 00       	mov    $0x0,%eax
  401648:	e9 4e 01 00 00       	jmp    40179b <main+0x1a9>
  40164d:	48 8b 85 70 ff ff ff 	mov    -0x90(%rbp),%rax
  401654:	48 83 c0 08          	add    $0x8,%rax
  401658:	48 8b 00             	mov    (%rax),%rax
  40165b:	48 8d 55 80          	lea    -0x80(%rbp),%rdx
  40165f:	48 83 c2 64          	add    $0x64,%rdx
  401663:	48 89 c6             	mov    %rax,%rsi
  401666:	48 89 d7             	mov    %rdx,%rdi
  401669:	e8 d2 f9 ff ff       	call   401040 <strcpy@plt>
  40166e:	48 8b 85 70 ff ff ff 	mov    -0x90(%rbp),%rax
  401675:	48 83 c0 10          	add    $0x10,%rax
  401679:	48 8b 10             	mov    (%rax),%rdx
  40167c:	48 8d 45 80          	lea    -0x80(%rbp),%rax
  401680:	48 89 d6             	mov    %rdx,%rsi
  401683:	48 89 c7             	mov    %rax,%rdi
  401686:	e8 b5 f9 ff ff       	call   401040 <strcpy@plt>
  40168b:	48 8b 85 70 ff ff ff 	mov    -0x90(%rbp),%rax
  401692:	48 83 c0 18          	add    $0x18,%rax
  401696:	48 8b 00             	mov    (%rax),%rax
  401699:	48 89 c7             	mov    %rax,%rdi
  40169c:	e8 6f fa ff ff       	call   401110 <atoi@plt>
  4016a1:	89 45 fc             	mov    %eax,-0x4(%rbp)
  4016a4:	48 8d 45 80          	lea    -0x80(%rbp),%rax
  4016a8:	48 83 c0 64          	add    $0x64,%rax
  4016ac:	48 89 c6             	mov    %rax,%rsi
  4016af:	48 8d 05 8e 0b 00 00 	lea    0xb8e(%rip),%rax        # 402244 <_IO_stdin_used+0x244>
  4016b6:	48 89 c7             	mov    %rax,%rdi
  4016b9:	b8 00 00 00 00       	mov    $0x0,%eax
  4016be:	e8 cd f9 ff ff       	call   401090 <printf@plt>
  4016c3:	48 8d 45 80          	lea    -0x80(%rbp),%rax
  4016c7:	48 83 c0 64          	add    $0x64,%rax
  4016cb:	48 89 c7             	mov    %rax,%rdi
  4016ce:	e8 f1 03 00 00       	call   401ac4 <gencookie>
  4016d3:	89 05 0f 2a 00 00    	mov    %eax,0x2a0f(%rip)        # 4040e8 <cookie>
  4016d9:	8b 05 09 2a 00 00    	mov    0x2a09(%rip),%eax        # 4040e8 <cookie>
  4016df:	89 c6                	mov    %eax,%esi
  4016e1:	48 8d 05 6b 0b 00 00 	lea    0xb6b(%rip),%rax        # 402253 <_IO_stdin_used+0x253>
  4016e8:	48 89 c7             	mov    %rax,%rdi
  4016eb:	b8 00 00 00 00       	mov    $0x0,%eax
  4016f0:	e8 9b f9 ff ff       	call   401090 <printf@plt>
  4016f5:	48 8d 45 80          	lea    -0x80(%rbp),%rax
  4016f9:	48 89 c6             	mov    %rax,%rsi
  4016fc:	48 8d 05 60 0b 00 00 	lea    0xb60(%rip),%rax        # 402263 <_IO_stdin_used+0x263>
  401703:	48 89 c7             	mov    %rax,%rdi
  401706:	b8 00 00 00 00       	mov    $0x0,%eax
  40170b:	e8 80 f9 ff ff       	call   401090 <printf@plt>
  401710:	8b 45 fc             	mov    -0x4(%rbp),%eax
  401713:	89 c6                	mov    %eax,%esi
  401715:	48 8d 05 5e 0b 00 00 	lea    0xb5e(%rip),%rax        # 40227a <_IO_stdin_used+0x27a>
  40171c:	48 89 c7             	mov    %rax,%rdi
  40171f:	b8 00 00 00 00       	mov    $0x0,%eax
  401724:	e8 67 f9 ff ff       	call   401090 <printf@plt>
  401729:	48 8d 05 67 fc ff ff 	lea    -0x399(%rip),%rax        # 401397 <bang>
  401730:	48 89 c1             	mov    %rax,%rcx
  401733:	48 8d 05 09 fc ff ff 	lea    -0x3f7(%rip),%rax        # 401343 <fizz>
  40173a:	48 89 c2             	mov    %rax,%rdx
  40173d:	48 8d 05 e2 fb ff ff 	lea    -0x41e(%rip),%rax        # 401326 <smoke>
  401744:	48 89 c6             	mov    %rax,%rsi
  401747:	48 8d 05 3a 0b 00 00 	lea    0xb3a(%rip),%rax        # 402288 <_IO_stdin_used+0x288>
  40174e:	48 89 c7             	mov    %rax,%rdi
  401751:	b8 00 00 00 00       	mov    $0x0,%eax
  401756:	e8 35 f9 ff ff       	call   401090 <printf@plt>
  40175b:	48 8d 45 80          	lea    -0x80(%rbp),%rax
  40175f:	48 83 c0 64          	add    $0x64,%rax
  401763:	48 89 c7             	mov    %rax,%rdi
  401766:	e8 bb fa ff ff       	call   401226 <initialize_bomb>
  40176b:	48 8d 45 80          	lea    -0x80(%rbp),%rax
  40176f:	48 89 c7             	mov    %rax,%rdi
  401772:	e8 7f fc ff ff       	call   4013f6 <test>
  401777:	48 8d 45 80          	lea    -0x80(%rbp),%rax
  40177b:	48 83 c0 64          	add    $0x64,%rax
  40177f:	48 89 c6             	mov    %rax,%rsi
  401782:	48 8d 05 29 0b 00 00 	lea    0xb29(%rip),%rax        # 4022b2 <_IO_stdin_used+0x2b2>
  401789:	48 89 c7             	mov    %rax,%rdi
  40178c:	b8 00 00 00 00       	mov    $0x0,%eax
  401791:	e8 fa f8 ff ff       	call   401090 <printf@plt>
  401796:	b8 00 00 00 00       	mov    $0x0,%eax
  40179b:	c9                   	leave  
  40179c:	c3                   	ret    

000000000040179d <convert_to_hex_value>:
  40179d:	55                   	push   %rbp
  40179e:	48 89 e5             	mov    %rsp,%rbp
  4017a1:	48 83 ec 20          	sub    $0x20,%rsp
  4017a5:	48 89 7d e8          	mov    %rdi,-0x18(%rbp)
  4017a9:	48 8d 55 fc          	lea    -0x4(%rbp),%rdx
  4017ad:	48 8b 45 e8          	mov    -0x18(%rbp),%rax
  4017b1:	48 8d 0d 08 0b 00 00 	lea    0xb08(%rip),%rcx        # 4022c0 <_IO_stdin_used+0x2c0>
  4017b8:	48 89 ce             	mov    %rcx,%rsi
  4017bb:	48 89 c7             	mov    %rax,%rdi
  4017be:	b8 00 00 00 00       	mov    $0x0,%eax
  4017c3:	e8 18 f9 ff ff       	call   4010e0 <__isoc99_sscanf@plt>
  4017c8:	8b 45 fc             	mov    -0x4(%rbp),%eax
  4017cb:	c9                   	leave  
  4017cc:	c3                   	ret    

00000000004017cd <convert_to_byte_string>:
  4017cd:	55                   	push   %rbp
  4017ce:	48 89 e5             	mov    %rsp,%rbp
  4017d1:	53                   	push   %rbx
  4017d2:	48 83 ec 58          	sub    $0x58,%rsp
  4017d6:	48 89 7d a8          	mov    %rdi,-0x58(%rbp)
  4017da:	48 89 75 a0          	mov    %rsi,-0x60(%rbp)
  4017de:	48 89 e0             	mov    %rsp,%rax
  4017e1:	48 89 c3             	mov    %rax,%rbx
  4017e4:	c7 45 ec 00 00 00 00 	movl   $0x0,-0x14(%rbp)
  4017eb:	c7 45 d4 00 10 00 00 	movl   $0x1000,-0x2c(%rbp)
  4017f2:	8b 45 d4             	mov    -0x2c(%rbp),%eax
  4017f5:	48 63 d0             	movslq %eax,%rdx
  4017f8:	48 83 ea 01          	sub    $0x1,%rdx
  4017fc:	48 89 55 c8          	mov    %rdx,-0x38(%rbp)
  401800:	48 63 d0             	movslq %eax,%rdx
  401803:	49 89 d2             	mov    %rdx,%r10
  401806:	41 bb 00 00 00 00    	mov    $0x0,%r11d
  40180c:	48 63 d0             	movslq %eax,%rdx
  40180f:	49 89 d0             	mov    %rdx,%r8
  401812:	41 b9 00 00 00 00    	mov    $0x0,%r9d
  401818:	48 98                	cltq   
  40181a:	ba 10 00 00 00       	mov    $0x10,%edx
  40181f:	48 83 ea 01          	sub    $0x1,%rdx
  401823:	48 01 d0             	add    %rdx,%rax
  401826:	be 10 00 00 00       	mov    $0x10,%esi
  40182b:	ba 00 00 00 00       	mov    $0x0,%edx
  401830:	48 f7 f6             	div    %rsi
  401833:	48 6b c0 10          	imul   $0x10,%rax,%rax
  401837:	48 89 c1             	mov    %rax,%rcx
  40183a:	48 81 e1 00 f0 ff ff 	and    $0xfffffffffffff000,%rcx
  401841:	48 89 e2             	mov    %rsp,%rdx
  401844:	48 29 ca             	sub    %rcx,%rdx
  401847:	48 39 d4             	cmp    %rdx,%rsp
  40184a:	74 12                	je     40185e <convert_to_byte_string+0x91>
  40184c:	48 81 ec 00 10 00 00 	sub    $0x1000,%rsp
  401853:	48 83 8c 24 f8 0f 00 	orq    $0x0,0xff8(%rsp)
  40185a:	00 00 
  40185c:	eb e9                	jmp    401847 <convert_to_byte_string+0x7a>
  40185e:	48 89 c2             	mov    %rax,%rdx
  401861:	81 e2 ff 0f 00 00    	and    $0xfff,%edx
  401867:	48 29 d4             	sub    %rdx,%rsp
  40186a:	48 89 c2             	mov    %rax,%rdx
  40186d:	81 e2 ff 0f 00 00    	and    $0xfff,%edx
  401873:	48 85 d2             	test   %rdx,%rdx
  401876:	74 10                	je     401888 <convert_to_byte_string+0xbb>
  401878:	25 ff 0f 00 00       	and    $0xfff,%eax
  40187d:	48 83 e8 08          	sub    $0x8,%rax
  401881:	48 01 e0             	add    %rsp,%rax
  401884:	48 83 08 00          	orq    $0x0,(%rax)
  401888:	48 89 e0             	mov    %rsp,%rax
  40188b:	48 83 c0 00          	add    $0x0,%rax
  40188f:	48 89 45 c0          	mov    %rax,-0x40(%rbp)
  401893:	c7 45 e8 00 04 00 00 	movl   $0x400,-0x18(%rbp)
  40189a:	c7 45 e4 00 00 00 00 	movl   $0x0,-0x1c(%rbp)
  4018a1:	bf 00 04 00 00       	mov    $0x400,%edi
  4018a6:	e8 25 f8 ff ff       	call   4010d0 <malloc@plt>
  4018ab:	48 89 45 d8          	mov    %rax,-0x28(%rbp)
  4018af:	48 83 7d d8 00       	cmpq   $0x0,-0x28(%rbp)
  4018b4:	0f 85 8c 01 00 00    	jne    401a46 <convert_to_byte_string+0x279>
  4018ba:	b8 00 00 00 00       	mov    $0x0,%eax
  4018bf:	e9 b6 01 00 00       	jmp    401a7a <convert_to_byte_string+0x2ad>
  4018c4:	48 8b 45 c0          	mov    -0x40(%rbp),%rax
  4018c8:	48 8d 15 f4 09 00 00 	lea    0x9f4(%rip),%rdx        # 4022c3 <_IO_stdin_used+0x2c3>
  4018cf:	48 89 d6             	mov    %rdx,%rsi
  4018d2:	48 89 c7             	mov    %rax,%rdi
  4018d5:	e8 c6 f7 ff ff       	call   4010a0 <strcmp@plt>
  4018da:	85 c0                	test   %eax,%eax
  4018dc:	75 09                	jne    4018e7 <convert_to_byte_string+0x11a>
  4018de:	83 45 ec 01          	addl   $0x1,-0x14(%rbp)
  4018e2:	e9 5f 01 00 00       	jmp    401a46 <convert_to_byte_string+0x279>
  4018e7:	48 8b 45 c0          	mov    -0x40(%rbp),%rax
  4018eb:	48 8d 15 d4 09 00 00 	lea    0x9d4(%rip),%rdx        # 4022c6 <_IO_stdin_used+0x2c6>
  4018f2:	48 89 d6             	mov    %rdx,%rsi
  4018f5:	48 89 c7             	mov    %rax,%rdi
  4018f8:	e8 a3 f7 ff ff       	call   4010a0 <strcmp@plt>
  4018fd:	85 c0                	test   %eax,%eax
  4018ff:	75 4a                	jne    40194b <convert_to_byte_string+0x17e>
  401901:	83 7d ec 00          	cmpl   $0x0,-0x14(%rbp)
  401905:	7f 3b                	jg     401942 <convert_to_byte_string+0x175>
  401907:	48 8b 05 b2 27 00 00 	mov    0x27b2(%rip),%rax        # 4040c0 <stderr@GLIBC_2.2.5>
  40190e:	48 8d 15 b1 09 00 00 	lea    0x9b1(%rip),%rdx        # 4022c6 <_IO_stdin_used+0x2c6>
  401915:	48 8d 0d ad 09 00 00 	lea    0x9ad(%rip),%rcx        # 4022c9 <_IO_stdin_used+0x2c9>
  40191c:	48 89 ce             	mov    %rcx,%rsi
  40191f:	48 89 c7             	mov    %rax,%rdi
  401922:	b8 00 00 00 00       	mov    $0x0,%eax
  401927:	e8 84 f7 ff ff       	call   4010b0 <fprintf@plt>
  40192c:	48 8b 45 d8          	mov    -0x28(%rbp),%rax
  401930:	48 89 c7             	mov    %rax,%rdi
  401933:	e8 f8 f6 ff ff       	call   401030 <free@plt>
  401938:	b8 00 00 00 00       	mov    $0x0,%eax
  40193d:	e9 38 01 00 00       	jmp    401a7a <convert_to_byte_string+0x2ad>
  401942:	83 6d ec 01          	subl   $0x1,-0x14(%rbp)
  401946:	e9 fb 00 00 00       	jmp    401a46 <convert_to_byte_string+0x279>
  40194b:	83 7d ec 00          	cmpl   $0x0,-0x14(%rbp)
  40194f:	0f 85 f1 00 00 00    	jne    401a46 <convert_to_byte_string+0x279>
  401955:	e8 d6 f7 ff ff       	call   401130 <__ctype_b_loc@plt>
  40195a:	48 8b 10             	mov    (%rax),%rdx
  40195d:	48 8b 45 c0          	mov    -0x40(%rbp),%rax
  401961:	0f b6 00             	movzbl (%rax),%eax
  401964:	48 0f be c0          	movsbq %al,%rax
  401968:	48 01 c0             	add    %rax,%rax
  40196b:	48 01 d0             	add    %rdx,%rax
  40196e:	0f b7 00             	movzwl (%rax),%eax
  401971:	0f b7 c0             	movzwl %ax,%eax
  401974:	25 00 10 00 00       	and    $0x1000,%eax
  401979:	85 c0                	test   %eax,%eax
  40197b:	74 35                	je     4019b2 <convert_to_byte_string+0x1e5>
  40197d:	e8 ae f7 ff ff       	call   401130 <__ctype_b_loc@plt>
  401982:	48 8b 10             	mov    (%rax),%rdx
  401985:	48 8b 45 c0          	mov    -0x40(%rbp),%rax
  401989:	0f b6 40 01          	movzbl 0x1(%rax),%eax
  40198d:	48 0f be c0          	movsbq %al,%rax
  401991:	48 01 c0             	add    %rax,%rax
  401994:	48 01 d0             	add    %rdx,%rax
  401997:	0f b7 00             	movzwl (%rax),%eax
  40199a:	0f b7 c0             	movzwl %ax,%eax
  40199d:	25 00 10 00 00       	and    $0x1000,%eax
  4019a2:	85 c0                	test   %eax,%eax
  4019a4:	74 0c                	je     4019b2 <convert_to_byte_string+0x1e5>
  4019a6:	48 8b 45 c0          	mov    -0x40(%rbp),%rax
  4019aa:	0f b6 40 02          	movzbl 0x2(%rax),%eax
  4019ae:	84 c0                	test   %al,%al
  4019b0:	74 38                	je     4019ea <convert_to_byte_string+0x21d>
  4019b2:	48 8b 05 07 27 00 00 	mov    0x2707(%rip),%rax        # 4040c0 <stderr@GLIBC_2.2.5>
  4019b9:	48 8b 55 c0          	mov    -0x40(%rbp),%rdx
  4019bd:	48 8d 0d 24 09 00 00 	lea    0x924(%rip),%rcx        # 4022e8 <_IO_stdin_used+0x2e8>
  4019c4:	48 89 ce             	mov    %rcx,%rsi
  4019c7:	48 89 c7             	mov    %rax,%rdi
  4019ca:	b8 00 00 00 00       	mov    $0x0,%eax
  4019cf:	e8 dc f6 ff ff       	call   4010b0 <fprintf@plt>
  4019d4:	48 8b 45 d8          	mov    -0x28(%rbp),%rax
  4019d8:	48 89 c7             	mov    %rax,%rdi
  4019db:	e8 50 f6 ff ff       	call   401030 <free@plt>
  4019e0:	b8 00 00 00 00       	mov    $0x0,%eax
  4019e5:	e9 90 00 00 00       	jmp    401a7a <convert_to_byte_string+0x2ad>
  4019ea:	48 8b 45 c0          	mov    -0x40(%rbp),%rax
  4019ee:	48 89 c7             	mov    %rax,%rdi
  4019f1:	e8 a7 fd ff ff       	call   40179d <convert_to_hex_value>
  4019f6:	88 45 bf             	mov    %al,-0x41(%rbp)
  4019f9:	8b 45 e4             	mov    -0x1c(%rbp),%eax
  4019fc:	3b 45 e8             	cmp    -0x18(%rbp),%eax
  4019ff:	75 2c                	jne    401a2d <convert_to_byte_string+0x260>
  401a01:	8b 45 e8             	mov    -0x18(%rbp),%eax
  401a04:	01 c0                	add    %eax,%eax
  401a06:	48 63 d0             	movslq %eax,%rdx
  401a09:	48 8b 45 d8          	mov    -0x28(%rbp),%rax
  401a0d:	48 89 d6             	mov    %rdx,%rsi
  401a10:	48 89 c7             	mov    %rax,%rdi
  401a13:	e8 d8 f6 ff ff       	call   4010f0 <realloc@plt>
  401a18:	48 89 45 d8          	mov    %rax,-0x28(%rbp)
  401a1c:	48 83 7d d8 00       	cmpq   $0x0,-0x28(%rbp)
  401a21:	75 07                	jne    401a2a <convert_to_byte_string+0x25d>
  401a23:	b8 00 00 00 00       	mov    $0x0,%eax
  401a28:	eb 50                	jmp    401a7a <convert_to_byte_string+0x2ad>
  401a2a:	d1 65 e8             	shll   -0x18(%rbp)
  401a2d:	8b 45 e4             	mov    -0x1c(%rbp),%eax
  401a30:	8d 50 01             	lea    0x1(%rax),%edx
  401a33:	89 55 e4             	mov    %edx,-0x1c(%rbp)
  401a36:	48 63 d0             	movslq %eax,%rdx
  401a39:	48 8b 45 d8          	mov    -0x28(%rbp),%rax
  401a3d:	48 01 c2             	add    %rax,%rdx
  401a40:	0f b6 45 bf          	movzbl -0x41(%rbp),%eax
  401a44:	88 02                	mov    %al,(%rdx)
  401a46:	48 8b 55 c0          	mov    -0x40(%rbp),%rdx
  401a4a:	48 8b 45 a8          	mov    -0x58(%rbp),%rax
  401a4e:	48 8d 0d f0 08 00 00 	lea    0x8f0(%rip),%rcx        # 402345 <_IO_stdin_used+0x345>
  401a55:	48 89 ce             	mov    %rcx,%rsi
  401a58:	48 89 c7             	mov    %rax,%rdi
  401a5b:	b8 00 00 00 00       	mov    $0x0,%eax
  401a60:	e8 eb f5 ff ff       	call   401050 <__isoc99_fscanf@plt>
  401a65:	85 c0                	test   %eax,%eax
  401a67:	0f 8f 57 fe ff ff    	jg     4018c4 <convert_to_byte_string+0xf7>
  401a6d:	48 8b 45 a0          	mov    -0x60(%rbp),%rax
  401a71:	8b 55 e4             	mov    -0x1c(%rbp),%edx
  401a74:	89 10                	mov    %edx,(%rax)
  401a76:	48 8b 45 d8          	mov    -0x28(%rbp),%rax
  401a7a:	48 89 dc             	mov    %rbx,%rsp
  401a7d:	48 8b 5d f8          	mov    -0x8(%rbp),%rbx
  401a81:	c9                   	leave  
  401a82:	c3                   	ret    

0000000000401a83 <getbuf>:
  401a83:	55                   	push   %rbp
  401a84:	48 89 e5             	mov    %rsp,%rbp
  401a87:	48 83 ec 40          	sub    $0x40,%rsp
  401a8b:	48 89 7d c8          	mov    %rdi,-0x38(%rbp)
  401a8f:	89 75 c4             	mov    %esi,-0x3c(%rbp)
  401a92:	48 b8 6c 61 6e 67 75 	movabs $0x65676175676e616c,%rax
  401a99:	61 67 65 
  401a9c:	48 89 45 f4          	mov    %rax,-0xc(%rbp)
  401aa0:	c7 45 fc 00 00 00 00 	movl   $0x0,-0x4(%rbp)
  401aa7:	8b 55 c4             	mov    -0x3c(%rbp),%edx
  401aaa:	48 8b 4d c8          	mov    -0x38(%rbp),%rcx
  401aae:	48 8d 45 d0          	lea    -0x30(%rbp),%rax
  401ab2:	48 89 ce             	mov    %rcx,%rsi
  401ab5:	48 89 c7             	mov    %rax,%rdi
  401ab8:	e8 03 fb ff ff       	call   4015c0 <Gets>
  401abd:	b8 01 00 00 00       	mov    $0x1,%eax
  401ac2:	c9                   	leave  
  401ac3:	c3                   	ret    

0000000000401ac4 <gencookie>:
  401ac4:	55                   	push   %rbp
  401ac5:	48 89 e5             	mov    %rsp,%rbp
  401ac8:	48 83 ec 20          	sub    $0x20,%rsp
  401acc:	48 89 7d e8          	mov    %rdi,-0x18(%rbp)
  401ad0:	48 8b 45 e8          	mov    -0x18(%rbp),%rax
  401ad4:	48 89 c7             	mov    %rax,%rdi
  401ad7:	e8 a4 f5 ff ff       	call   401080 <strlen@plt>
  401adc:	48 83 f8 0a          	cmp    $0xa,%rax
  401ae0:	74 19                	je     401afb <gencookie+0x37>
  401ae2:	48 8d 05 5f 08 00 00 	lea    0x85f(%rip),%rax        # 402348 <_IO_stdin_used+0x348>
  401ae9:	48 89 c7             	mov    %rax,%rdi
  401aec:	e8 6f f5 ff ff       	call   401060 <puts@plt>
  401af1:	b8 00 00 00 00       	mov    $0x0,%eax
  401af6:	e9 8d 00 00 00       	jmp    401b88 <gencookie+0xc4>
  401afb:	48 8b 45 e8          	mov    -0x18(%rbp),%rax
  401aff:	0f b6 00             	movzbl (%rax),%eax
  401b02:	3c 55                	cmp    $0x55,%al
  401b04:	74 21                	je     401b27 <gencookie+0x63>
  401b06:	48 8b 45 e8          	mov    -0x18(%rbp),%rax
  401b0a:	0f b6 00             	movzbl (%rax),%eax
  401b0d:	3c 75                	cmp    $0x75,%al
  401b0f:	74 16                	je     401b27 <gencookie+0x63>
  401b11:	48 8d 05 4f 08 00 00 	lea    0x84f(%rip),%rax        # 402367 <_IO_stdin_used+0x367>
  401b18:	48 89 c7             	mov    %rax,%rdi
  401b1b:	e8 40 f5 ff ff       	call   401060 <puts@plt>
  401b20:	b8 00 00 00 00       	mov    $0x0,%eax
  401b25:	eb 61                	jmp    401b88 <gencookie+0xc4>
  401b27:	c7 45 fc 01 00 00 00 	movl   $0x1,-0x4(%rbp)
  401b2e:	eb 42                	jmp    401b72 <gencookie+0xae>
  401b30:	8b 45 fc             	mov    -0x4(%rbp),%eax
  401b33:	48 63 d0             	movslq %eax,%rdx
  401b36:	48 8b 45 e8          	mov    -0x18(%rbp),%rax
  401b3a:	48 01 d0             	add    %rdx,%rax
  401b3d:	0f b6 00             	movzbl (%rax),%eax
  401b40:	3c 2f                	cmp    $0x2f,%al
  401b42:	7e 14                	jle    401b58 <gencookie+0x94>
  401b44:	8b 45 fc             	mov    -0x4(%rbp),%eax
  401b47:	48 63 d0             	movslq %eax,%rdx
  401b4a:	48 8b 45 e8          	mov    -0x18(%rbp),%rax
  401b4e:	48 01 d0             	add    %rdx,%rax
  401b51:	0f b6 00             	movzbl (%rax),%eax
  401b54:	3c 39                	cmp    $0x39,%al
  401b56:	7e 16                	jle    401b6e <gencookie+0xaa>
  401b58:	48 8d 05 23 08 00 00 	lea    0x823(%rip),%rax        # 402382 <_IO_stdin_used+0x382>
  401b5f:	48 89 c7             	mov    %rax,%rdi
  401b62:	e8 f9 f4 ff ff       	call   401060 <puts@plt>
  401b67:	b8 00 00 00 00       	mov    $0x0,%eax
  401b6c:	eb 1a                	jmp    401b88 <gencookie+0xc4>
  401b6e:	83 45 fc 01          	addl   $0x1,-0x4(%rbp)
  401b72:	83 7d fc 09          	cmpl   $0x9,-0x4(%rbp)
  401b76:	7e b8                	jle    401b30 <gencookie+0x6c>
  401b78:	48 8b 45 e8          	mov    -0x18(%rbp),%rax
  401b7c:	48 83 c0 01          	add    $0x1,%rax
  401b80:	48 89 c7             	mov    %rax,%rdi
  401b83:	e8 88 f5 ff ff       	call   401110 <atoi@plt>
  401b88:	c9                   	leave  
  401b89:	c3                   	ret    

Disassembly of section .fini:

0000000000401b8c <_fini>:
  401b8c:	f3 0f 1e fa          	endbr64 
  401b90:	48 83 ec 08          	sub    $0x8,%rsp
  401b94:	48 83 c4 08          	add    $0x8,%rsp
  401b98:	c3                   	ret    
