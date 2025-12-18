
bomb:     file format elf64-x86-64


Disassembly of section .init:

0000000000001000 <_init>:
    1000:	f3 0f 1e fa          	endbr64 
    1004:	48 83 ec 08          	sub    $0x8,%rsp
    1008:	48 8b 05 d9 2f 00 00 	mov    0x2fd9(%rip),%rax        # 3fe8 <__gmon_start__@Base>
    100f:	48 85 c0             	test   %rax,%rax
    1012:	74 02                	je     1016 <_init+0x16>
    1014:	ff d0                	call   *%rax
    1016:	48 83 c4 08          	add    $0x8,%rsp
    101a:	c3                   	ret    

Disassembly of section .plt:

0000000000001020 <.plt>:
    1020:	ff 35 4a 2f 00 00    	push   0x2f4a(%rip)        # 3f70 <_GLOBAL_OFFSET_TABLE_+0x8>
    1026:	f2 ff 25 4b 2f 00 00 	bnd jmp *0x2f4b(%rip)        # 3f78 <_GLOBAL_OFFSET_TABLE_+0x10>
    102d:	0f 1f 00             	nopl   (%rax)
    1030:	f3 0f 1e fa          	endbr64 
    1034:	68 00 00 00 00       	push   $0x0
    1039:	f2 e9 e1 ff ff ff    	bnd jmp 1020 <_init+0x20>
    103f:	90                   	nop
    1040:	f3 0f 1e fa          	endbr64 
    1044:	68 01 00 00 00       	push   $0x1
    1049:	f2 e9 d1 ff ff ff    	bnd jmp 1020 <_init+0x20>
    104f:	90                   	nop
    1050:	f3 0f 1e fa          	endbr64 
    1054:	68 02 00 00 00       	push   $0x2
    1059:	f2 e9 c1 ff ff ff    	bnd jmp 1020 <_init+0x20>
    105f:	90                   	nop
    1060:	f3 0f 1e fa          	endbr64 
    1064:	68 03 00 00 00       	push   $0x3
    1069:	f2 e9 b1 ff ff ff    	bnd jmp 1020 <_init+0x20>
    106f:	90                   	nop
    1070:	f3 0f 1e fa          	endbr64 
    1074:	68 04 00 00 00       	push   $0x4
    1079:	f2 e9 a1 ff ff ff    	bnd jmp 1020 <_init+0x20>
    107f:	90                   	nop
    1080:	f3 0f 1e fa          	endbr64 
    1084:	68 05 00 00 00       	push   $0x5
    1089:	f2 e9 91 ff ff ff    	bnd jmp 1020 <_init+0x20>
    108f:	90                   	nop
    1090:	f3 0f 1e fa          	endbr64 
    1094:	68 06 00 00 00       	push   $0x6
    1099:	f2 e9 81 ff ff ff    	bnd jmp 1020 <_init+0x20>
    109f:	90                   	nop
    10a0:	f3 0f 1e fa          	endbr64 
    10a4:	68 07 00 00 00       	push   $0x7
    10a9:	f2 e9 71 ff ff ff    	bnd jmp 1020 <_init+0x20>
    10af:	90                   	nop
    10b0:	f3 0f 1e fa          	endbr64 
    10b4:	68 08 00 00 00       	push   $0x8
    10b9:	f2 e9 61 ff ff ff    	bnd jmp 1020 <_init+0x20>
    10bf:	90                   	nop
    10c0:	f3 0f 1e fa          	endbr64 
    10c4:	68 09 00 00 00       	push   $0x9
    10c9:	f2 e9 51 ff ff ff    	bnd jmp 1020 <_init+0x20>
    10cf:	90                   	nop
    10d0:	f3 0f 1e fa          	endbr64 
    10d4:	68 0a 00 00 00       	push   $0xa
    10d9:	f2 e9 41 ff ff ff    	bnd jmp 1020 <_init+0x20>
    10df:	90                   	nop

Disassembly of section .plt.got:

00000000000010e0 <__cxa_finalize@plt>:
    10e0:	f3 0f 1e fa          	endbr64 
    10e4:	f2 ff 25 0d 2f 00 00 	bnd jmp *0x2f0d(%rip)        # 3ff8 <__cxa_finalize@GLIBC_2.2.5>
    10eb:	0f 1f 44 00 00       	nopl   0x0(%rax,%rax,1)

Disassembly of section .plt.sec:

00000000000010f0 <getenv@plt>:
    10f0:	f3 0f 1e fa          	endbr64 
    10f4:	f2 ff 25 85 2e 00 00 	bnd jmp *0x2e85(%rip)        # 3f80 <getenv@GLIBC_2.2.5>
    10fb:	0f 1f 44 00 00       	nopl   0x0(%rax,%rax,1)

0000000000001100 <strcpy@plt>:
    1100:	f3 0f 1e fa          	endbr64 
    1104:	f2 ff 25 7d 2e 00 00 	bnd jmp *0x2e7d(%rip)        # 3f88 <strcpy@GLIBC_2.2.5>
    110b:	0f 1f 44 00 00       	nopl   0x0(%rax,%rax,1)

0000000000001110 <puts@plt>:
    1110:	f3 0f 1e fa          	endbr64 
    1114:	f2 ff 25 75 2e 00 00 	bnd jmp *0x2e75(%rip)        # 3f90 <puts@GLIBC_2.2.5>
    111b:	0f 1f 44 00 00       	nopl   0x0(%rax,%rax,1)

0000000000001120 <strlen@plt>:
    1120:	f3 0f 1e fa          	endbr64 
    1124:	f2 ff 25 6d 2e 00 00 	bnd jmp *0x2e6d(%rip)        # 3f98 <strlen@GLIBC_2.2.5>
    112b:	0f 1f 44 00 00       	nopl   0x0(%rax,%rax,1)

0000000000001130 <__stack_chk_fail@plt>:
    1130:	f3 0f 1e fa          	endbr64 
    1134:	f2 ff 25 65 2e 00 00 	bnd jmp *0x2e65(%rip)        # 3fa0 <__stack_chk_fail@GLIBC_2.4>
    113b:	0f 1f 44 00 00       	nopl   0x0(%rax,%rax,1)

0000000000001140 <printf@plt>:
    1140:	f3 0f 1e fa          	endbr64 
    1144:	f2 ff 25 5d 2e 00 00 	bnd jmp *0x2e5d(%rip)        # 3fa8 <printf@GLIBC_2.2.5>
    114b:	0f 1f 44 00 00       	nopl   0x0(%rax,%rax,1)

0000000000001150 <fgets@plt>:
    1150:	f3 0f 1e fa          	endbr64 
    1154:	f2 ff 25 55 2e 00 00 	bnd jmp *0x2e55(%rip)        # 3fb0 <fgets@GLIBC_2.2.5>
    115b:	0f 1f 44 00 00       	nopl   0x0(%rax,%rax,1)

0000000000001160 <__isoc99_sscanf@plt>:
    1160:	f3 0f 1e fa          	endbr64 
    1164:	f2 ff 25 4d 2e 00 00 	bnd jmp *0x2e4d(%rip)        # 3fb8 <__isoc99_sscanf@GLIBC_2.7>
    116b:	0f 1f 44 00 00       	nopl   0x0(%rax,%rax,1)

0000000000001170 <fopen@plt>:
    1170:	f3 0f 1e fa          	endbr64 
    1174:	f2 ff 25 45 2e 00 00 	bnd jmp *0x2e45(%rip)        # 3fc0 <fopen@GLIBC_2.2.5>
    117b:	0f 1f 44 00 00       	nopl   0x0(%rax,%rax,1)

0000000000001180 <exit@plt>:
    1180:	f3 0f 1e fa          	endbr64 
    1184:	f2 ff 25 3d 2e 00 00 	bnd jmp *0x2e3d(%rip)        # 3fc8 <exit@GLIBC_2.2.5>
    118b:	0f 1f 44 00 00       	nopl   0x0(%rax,%rax,1)

0000000000001190 <__ctype_b_loc@plt>:
    1190:	f3 0f 1e fa          	endbr64 
    1194:	f2 ff 25 35 2e 00 00 	bnd jmp *0x2e35(%rip)        # 3fd0 <__ctype_b_loc@GLIBC_2.3>
    119b:	0f 1f 44 00 00       	nopl   0x0(%rax,%rax,1)

Disassembly of section .text:

00000000000011a0 <_start>:
    11a0:	f3 0f 1e fa          	endbr64 
    11a4:	31 ed                	xor    %ebp,%ebp
    11a6:	49 89 d1             	mov    %rdx,%r9
    11a9:	5e                   	pop    %rsi
    11aa:	48 89 e2             	mov    %rsp,%rdx
    11ad:	48 83 e4 f0          	and    $0xfffffffffffffff0,%rsp
    11b1:	50                   	push   %rax
    11b2:	54                   	push   %rsp
    11b3:	45 31 c0             	xor    %r8d,%r8d
    11b6:	31 c9                	xor    %ecx,%ecx
    11b8:	48 8d 3d e4 01 00 00 	lea    0x1e4(%rip),%rdi        # 13a3 <main>
    11bf:	ff 15 13 2e 00 00    	call   *0x2e13(%rip)        # 3fd8 <__libc_start_main@GLIBC_2.34>
    11c5:	f4                   	hlt    
    11c6:	66 2e 0f 1f 84 00 00 	cs nopw 0x0(%rax,%rax,1)
    11cd:	00 00 00 

00000000000011d0 <deregister_tm_clones>:
    11d0:	48 8d 3d 91 32 00 00 	lea    0x3291(%rip),%rdi        # 4468 <__TMC_END__>
    11d7:	48 8d 05 8a 32 00 00 	lea    0x328a(%rip),%rax        # 4468 <__TMC_END__>
    11de:	48 39 f8             	cmp    %rdi,%rax
    11e1:	74 15                	je     11f8 <deregister_tm_clones+0x28>
    11e3:	48 8b 05 f6 2d 00 00 	mov    0x2df6(%rip),%rax        # 3fe0 <_ITM_deregisterTMCloneTable@Base>
    11ea:	48 85 c0             	test   %rax,%rax
    11ed:	74 09                	je     11f8 <deregister_tm_clones+0x28>
    11ef:	ff e0                	jmp    *%rax
    11f1:	0f 1f 80 00 00 00 00 	nopl   0x0(%rax)
    11f8:	c3                   	ret    
    11f9:	0f 1f 80 00 00 00 00 	nopl   0x0(%rax)

0000000000001200 <register_tm_clones>:
    1200:	48 8d 3d 61 32 00 00 	lea    0x3261(%rip),%rdi        # 4468 <__TMC_END__>
    1207:	48 8d 35 5a 32 00 00 	lea    0x325a(%rip),%rsi        # 4468 <__TMC_END__>
    120e:	48 29 fe             	sub    %rdi,%rsi
    1211:	48 89 f0             	mov    %rsi,%rax
    1214:	48 c1 ee 3f          	shr    $0x3f,%rsi
    1218:	48 c1 f8 03          	sar    $0x3,%rax
    121c:	48 01 c6             	add    %rax,%rsi
    121f:	48 d1 fe             	sar    %rsi
    1222:	74 14                	je     1238 <register_tm_clones+0x38>
    1224:	48 8b 05 c5 2d 00 00 	mov    0x2dc5(%rip),%rax        # 3ff0 <_ITM_registerTMCloneTable@Base>
    122b:	48 85 c0             	test   %rax,%rax
    122e:	74 08                	je     1238 <register_tm_clones+0x38>
    1230:	ff e0                	jmp    *%rax
    1232:	66 0f 1f 44 00 00    	nopw   0x0(%rax,%rax,1)
    1238:	c3                   	ret    
    1239:	0f 1f 80 00 00 00 00 	nopl   0x0(%rax)

0000000000001240 <__do_global_dtors_aux>:
    1240:	f3 0f 1e fa          	endbr64 
    1244:	80 3d 3d 32 00 00 00 	cmpb   $0x0,0x323d(%rip)        # 4488 <completed.0>
    124b:	75 2b                	jne    1278 <__do_global_dtors_aux+0x38>
    124d:	55                   	push   %rbp
    124e:	48 83 3d a2 2d 00 00 	cmpq   $0x0,0x2da2(%rip)        # 3ff8 <__cxa_finalize@GLIBC_2.2.5>
    1255:	00 
    1256:	48 89 e5             	mov    %rsp,%rbp
    1259:	74 0c                	je     1267 <__do_global_dtors_aux+0x27>
    125b:	48 8b 3d a6 2d 00 00 	mov    0x2da6(%rip),%rdi        # 4008 <__dso_handle>
    1262:	e8 79 fe ff ff       	call   10e0 <__cxa_finalize@plt>
    1267:	e8 64 ff ff ff       	call   11d0 <deregister_tm_clones>
    126c:	c6 05 15 32 00 00 01 	movb   $0x1,0x3215(%rip)        # 4488 <completed.0>
    1273:	5d                   	pop    %rbp
    1274:	c3                   	ret    
    1275:	0f 1f 00             	nopl   (%rax)
    1278:	c3                   	ret    
    1279:	0f 1f 80 00 00 00 00 	nopl   0x0(%rax)

0000000000001280 <frame_dummy>:
    1280:	f3 0f 1e fa          	endbr64 
    1284:	e9 77 ff ff ff       	jmp    1200 <register_tm_clones>

0000000000001289 <initialize_bomb>:
    1289:	f3 0f 1e fa          	endbr64 
    128d:	55                   	push   %rbp
    128e:	48 89 e5             	mov    %rsp,%rbp
    1291:	48 83 ec 30          	sub    $0x30,%rsp
    1295:	48 89 7d d8          	mov    %rdi,-0x28(%rbp)
    1299:	c7 45 e4 01 00 00 00 	movl   $0x1,-0x1c(%rbp)
    12a0:	c7 45 e8 02 00 00 00 	movl   $0x2,-0x18(%rbp)
    12a7:	c7 45 ec 03 00 00 00 	movl   $0x3,-0x14(%rbp)
    12ae:	c7 45 f0 04 00 00 00 	movl   $0x4,-0x10(%rbp)
    12b5:	c7 45 f4 05 00 00 00 	movl   $0x5,-0xc(%rbp)
    12bc:	c7 45 f8 06 00 00 00 	movl   $0x6,-0x8(%rbp)
    12c3:	48 8b 45 d8          	mov    -0x28(%rbp),%rax
    12c7:	48 89 c7             	mov    %rax,%rdi
    12ca:	e8 51 fe ff ff       	call   1120 <strlen@plt>
    12cf:	89 45 fc             	mov    %eax,-0x4(%rbp)
    12d2:	83 7d fc 0a          	cmpl   $0xa,-0x4(%rbp)
    12d6:	74 19                	je     12f1 <initialize_bomb+0x68>
    12d8:	48 8d 05 29 0d 00 00 	lea    0xd29(%rip),%rax        # 2008 <_IO_stdin_used+0x8>
    12df:	48 89 c7             	mov    %rax,%rdi
    12e2:	e8 29 fe ff ff       	call   1110 <puts@plt>
    12e7:	bf 00 00 00 00       	mov    $0x0,%edi
    12ec:	e8 8f fe ff ff       	call   1180 <exit@plt>
    12f1:	48 8b 45 d8          	mov    -0x28(%rbp),%rax
    12f5:	48 89 c6             	mov    %rax,%rsi
    12f8:	48 8d 05 99 31 00 00 	lea    0x3199(%rip),%rax        # 4498 <studentid>
    12ff:	48 89 c7             	mov    %rax,%rdi
    1302:	e8 f9 fd ff ff       	call   1100 <strcpy@plt>
    1307:	48 8b 45 d8          	mov    -0x28(%rbp),%rax
    130b:	48 89 c6             	mov    %rax,%rsi
    130e:	48 8d 05 2d 0d 00 00 	lea    0xd2d(%rip),%rax        # 2042 <_IO_stdin_used+0x42>
    1315:	48 89 c7             	mov    %rax,%rdi
    1318:	b8 00 00 00 00       	mov    $0x0,%eax
    131d:	e8 1e fe ff ff       	call   1140 <printf@plt>
    1322:	8b 45 fc             	mov    -0x4(%rbp),%eax
    1325:	48 98                	cltq   
    1327:	48 8d 50 ff          	lea    -0x1(%rax),%rdx
    132b:	48 8b 45 d8          	mov    -0x28(%rbp),%rax
    132f:	48 01 d0             	add    %rdx,%rax
    1332:	0f b6 00             	movzbl (%rax),%eax
    1335:	3c 34                	cmp    $0x34,%al
    1337:	75 31                	jne    136a <initialize_bomb+0xe1>
    1339:	8b 45 e4             	mov    -0x1c(%rbp),%eax
    133c:	8d 0c 00             	lea    (%rax,%rax,1),%ecx
    133f:	8b 55 e8             	mov    -0x18(%rbp),%edx
    1342:	89 d0                	mov    %edx,%eax
    1344:	01 c0                	add    %eax,%eax
    1346:	01 d0                	add    %edx,%eax
    1348:	8d 14 01             	lea    (%rcx,%rax,1),%edx
    134b:	8b 45 f0             	mov    -0x10(%rbp),%eax
    134e:	c1 e0 02             	shl    $0x2,%eax
    1351:	01 c2                	add    %eax,%edx
    1353:	8b 45 e4             	mov    -0x1c(%rbp),%eax
    1356:	8d 0c 02             	lea    (%rdx,%rax,1),%ecx
    1359:	8b 55 f8             	mov    -0x8(%rbp),%edx
    135c:	89 d0                	mov    %edx,%eax
    135e:	c1 e0 02             	shl    $0x2,%eax
    1361:	01 d0                	add    %edx,%eax
    1363:	01 c8                	add    %ecx,%eax
    1365:	89 45 f8             	mov    %eax,-0x8(%rbp)
    1368:	eb 37                	jmp    13a1 <initialize_bomb+0x118>
    136a:	48 8d 05 df 0c 00 00 	lea    0xcdf(%rip),%rax        # 2050 <_IO_stdin_used+0x50>
    1371:	48 89 c7             	mov    %rax,%rdi
    1374:	e8 97 fd ff ff       	call   1110 <puts@plt>
    1379:	48 8d 05 08 0d 00 00 	lea    0xd08(%rip),%rax        # 2088 <_IO_stdin_used+0x88>
    1380:	48 89 c7             	mov    %rax,%rdi
    1383:	e8 88 fd ff ff       	call   1110 <puts@plt>
    1388:	48 8d 05 31 0d 00 00 	lea    0xd31(%rip),%rax        # 20c0 <_IO_stdin_used+0xc0>
    138f:	48 89 c7             	mov    %rax,%rdi
    1392:	e8 79 fd ff ff       	call   1110 <puts@plt>
    1397:	bf 00 00 00 00       	mov    $0x0,%edi
    139c:	e8 df fd ff ff       	call   1180 <exit@plt>
    13a1:	c9                   	leave  
    13a2:	c3                   	ret    

00000000000013a3 <main>:
    13a3:	f3 0f 1e fa          	endbr64 
    13a7:	55                   	push   %rbp
    13a8:	48 89 e5             	mov    %rsp,%rbp
    13ab:	48 83 ec 20          	sub    $0x20,%rsp
    13af:	89 7d ec             	mov    %edi,-0x14(%rbp)
    13b2:	48 89 75 e0          	mov    %rsi,-0x20(%rbp)
    13b6:	83 7d ec 01          	cmpl   $0x1,-0x14(%rbp)
    13ba:	75 13                	jne    13cf <main+0x2c>
    13bc:	48 8b 05 bd 30 00 00 	mov    0x30bd(%rip),%rax        # 4480 <stdin@GLIBC_2.2.5>
    13c3:	48 89 05 c6 30 00 00 	mov    %rax,0x30c6(%rip)        # 4490 <infile>
    13ca:	e9 91 00 00 00       	jmp    1460 <main+0xbd>
    13cf:	83 7d ec 02          	cmpl   $0x2,-0x14(%rbp)
    13d3:	75 63                	jne    1438 <main+0x95>
    13d5:	48 8b 45 e0          	mov    -0x20(%rbp),%rax
    13d9:	48 83 c0 08          	add    $0x8,%rax
    13dd:	48 8b 00             	mov    (%rax),%rax
    13e0:	48 8d 15 ff 0c 00 00 	lea    0xcff(%rip),%rdx        # 20e6 <_IO_stdin_used+0xe6>
    13e7:	48 89 d6             	mov    %rdx,%rsi
    13ea:	48 89 c7             	mov    %rax,%rdi
    13ed:	e8 7e fd ff ff       	call   1170 <fopen@plt>
    13f2:	48 89 05 97 30 00 00 	mov    %rax,0x3097(%rip)        # 4490 <infile>
    13f9:	48 8b 05 90 30 00 00 	mov    0x3090(%rip),%rax        # 4490 <infile>
    1400:	48 85 c0             	test   %rax,%rax
    1403:	75 5b                	jne    1460 <main+0xbd>
    1405:	48 8b 45 e0          	mov    -0x20(%rbp),%rax
    1409:	48 83 c0 08          	add    $0x8,%rax
    140d:	48 8b 10             	mov    (%rax),%rdx
    1410:	48 8b 45 e0          	mov    -0x20(%rbp),%rax
    1414:	48 8b 00             	mov    (%rax),%rax
    1417:	48 89 c6             	mov    %rax,%rsi
    141a:	48 8d 05 c7 0c 00 00 	lea    0xcc7(%rip),%rax        # 20e8 <_IO_stdin_used+0xe8>
    1421:	48 89 c7             	mov    %rax,%rdi
    1424:	b8 00 00 00 00       	mov    $0x0,%eax
    1429:	e8 12 fd ff ff       	call   1140 <printf@plt>
    142e:	bf 08 00 00 00       	mov    $0x8,%edi
    1433:	e8 48 fd ff ff       	call   1180 <exit@plt>
    1438:	48 8b 45 e0          	mov    -0x20(%rbp),%rax
    143c:	48 8b 00             	mov    (%rax),%rax
    143f:	48 89 c6             	mov    %rax,%rsi
    1442:	48 8d 05 bc 0c 00 00 	lea    0xcbc(%rip),%rax        # 2105 <_IO_stdin_used+0x105>
    1449:	48 89 c7             	mov    %rax,%rdi
    144c:	b8 00 00 00 00       	mov    $0x0,%eax
    1451:	e8 ea fc ff ff       	call   1140 <printf@plt>
    1456:	bf 08 00 00 00       	mov    $0x8,%edi
    145b:	e8 20 fd ff ff       	call   1180 <exit@plt>
    1460:	48 8d 05 b8 0c 00 00 	lea    0xcb8(%rip),%rax        # 211f <_IO_stdin_used+0x11f>
    1467:	48 89 c7             	mov    %rax,%rdi
    146a:	e8 a1 fc ff ff       	call   1110 <puts@plt>
    146f:	e8 83 03 00 00       	call   17f7 <read_line>
    1474:	48 89 45 f0          	mov    %rax,-0x10(%rbp)
    1478:	48 8b 45 f0          	mov    -0x10(%rbp),%rax
    147c:	48 89 c7             	mov    %rax,%rdi
    147f:	e8 05 fe ff ff       	call   1289 <initialize_bomb>
    1484:	48 8d 05 ad 0c 00 00 	lea    0xcad(%rip),%rax        # 2138 <_IO_stdin_used+0x138>
    148b:	48 89 c7             	mov    %rax,%rdi
    148e:	e8 7d fc ff ff       	call   1110 <puts@plt>
    1493:	48 8d 05 be 0c 00 00 	lea    0xcbe(%rip),%rax        # 2158 <_IO_stdin_used+0x158>
    149a:	48 89 c7             	mov    %rax,%rdi
    149d:	e8 6e fc ff ff       	call   1110 <puts@plt>
    14a2:	e8 50 03 00 00       	call   17f7 <read_line>
    14a7:	48 89 45 f8          	mov    %rax,-0x8(%rbp)
    14ab:	48 8b 45 f8          	mov    -0x8(%rbp),%rax
    14af:	48 89 c7             	mov    %rax,%rdi
    14b2:	e8 f4 04 00 00       	call   19ab <phase_1>
    14b7:	48 8d 05 d1 0c 00 00 	lea    0xcd1(%rip),%rax        # 218f <_IO_stdin_used+0x18f>
    14be:	48 89 c7             	mov    %rax,%rdi
    14c1:	e8 4a fc ff ff       	call   1110 <puts@plt>
    14c6:	48 8d 05 d3 0c 00 00 	lea    0xcd3(%rip),%rax        # 21a0 <_IO_stdin_used+0x1a0>
    14cd:	48 89 c7             	mov    %rax,%rdi
    14d0:	e8 3b fc ff ff       	call   1110 <puts@plt>
    14d5:	e8 1d 03 00 00       	call   17f7 <read_line>
    14da:	48 89 45 f8          	mov    %rax,-0x8(%rbp)
    14de:	48 8b 45 f8          	mov    -0x8(%rbp),%rax
    14e2:	48 89 c7             	mov    %rax,%rdi
    14e5:	e8 25 05 00 00       	call   1a0f <phase_2>
    14ea:	48 8d 05 eb 0c 00 00 	lea    0xceb(%rip),%rax        # 21dc <_IO_stdin_used+0x1dc>
    14f1:	48 89 c7             	mov    %rax,%rdi
    14f4:	e8 17 fc ff ff       	call   1110 <puts@plt>
    14f9:	48 8d 05 ed 0c 00 00 	lea    0xced(%rip),%rax        # 21ed <_IO_stdin_used+0x1ed>
    1500:	48 89 c7             	mov    %rax,%rdi
    1503:	e8 08 fc ff ff       	call   1110 <puts@plt>
    1508:	e8 ea 02 00 00       	call   17f7 <read_line>
    150d:	48 89 45 f8          	mov    %rax,-0x8(%rbp)
    1511:	48 8b 45 f8          	mov    -0x8(%rbp),%rax
    1515:	48 89 c7             	mov    %rax,%rdi
    1518:	e8 b8 05 00 00       	call   1ad5 <phase_3>
    151d:	48 8d 05 e7 0c 00 00 	lea    0xce7(%rip),%rax        # 220b <_IO_stdin_used+0x20b>
    1524:	48 89 c7             	mov    %rax,%rdi
    1527:	e8 e4 fb ff ff       	call   1110 <puts@plt>
    152c:	48 8d 05 ed 0c 00 00 	lea    0xced(%rip),%rax        # 2220 <_IO_stdin_used+0x220>
    1533:	48 89 c7             	mov    %rax,%rdi
    1536:	e8 d5 fb ff ff       	call   1110 <puts@plt>
    153b:	e8 b7 02 00 00       	call   17f7 <read_line>
    1540:	48 89 45 f8          	mov    %rax,-0x8(%rbp)
    1544:	48 8b 45 f8          	mov    -0x8(%rbp),%rax
    1548:	48 89 c7             	mov    %rax,%rdi
    154b:	e8 21 07 00 00       	call   1c71 <phase_4>
    1550:	48 8d 05 f4 0c 00 00 	lea    0xcf4(%rip),%rax        # 224b <_IO_stdin_used+0x24b>
    1557:	48 89 c7             	mov    %rax,%rdi
    155a:	e8 b1 fb ff ff       	call   1110 <puts@plt>
    155f:	48 8d 05 f6 0c 00 00 	lea    0xcf6(%rip),%rax        # 225c <_IO_stdin_used+0x25c>
    1566:	48 89 c7             	mov    %rax,%rdi
    1569:	e8 a2 fb ff ff       	call   1110 <puts@plt>
    156e:	e8 84 02 00 00       	call   17f7 <read_line>
    1573:	48 89 45 f8          	mov    %rax,-0x8(%rbp)
    1577:	48 8b 45 f8          	mov    -0x8(%rbp),%rax
    157b:	48 89 c7             	mov    %rax,%rdi
    157e:	e8 94 07 00 00       	call   1d17 <phase_5>
    1583:	48 8d 05 ee 0c 00 00 	lea    0xcee(%rip),%rax        # 2278 <_IO_stdin_used+0x278>
    158a:	48 89 c7             	mov    %rax,%rdi
    158d:	e8 7e fb ff ff       	call   1110 <puts@plt>
    1592:	48 8d 05 f0 0c 00 00 	lea    0xcf0(%rip),%rax        # 2289 <_IO_stdin_used+0x289>
    1599:	48 89 c7             	mov    %rax,%rdi
    159c:	e8 6f fb ff ff       	call   1110 <puts@plt>
    15a1:	e8 51 02 00 00       	call   17f7 <read_line>
    15a6:	48 89 45 f8          	mov    %rax,-0x8(%rbp)
    15aa:	48 8b 45 f8          	mov    -0x8(%rbp),%rax
    15ae:	48 89 c7             	mov    %rax,%rdi
    15b1:	e8 10 08 00 00       	call   1dc6 <phase_6>
    15b6:	48 8d 05 ea 0c 00 00 	lea    0xcea(%rip),%rax        # 22a7 <_IO_stdin_used+0x2a7>
    15bd:	48 89 c7             	mov    %rax,%rdi
    15c0:	e8 4b fb ff ff       	call   1110 <puts@plt>
    15c5:	48 8d 05 ec 0c 00 00 	lea    0xcec(%rip),%rax        # 22b8 <_IO_stdin_used+0x2b8>
    15cc:	48 89 c7             	mov    %rax,%rdi
    15cf:	e8 3c fb ff ff       	call   1110 <puts@plt>
    15d4:	b8 00 00 00 00       	mov    $0x0,%eax
    15d9:	c9                   	leave  
    15da:	c3                   	ret    

00000000000015db <invalid_phase>:
    15db:	f3 0f 1e fa          	endbr64 
    15df:	55                   	push   %rbp
    15e0:	48 89 e5             	mov    %rsp,%rbp
    15e3:	48 83 ec 10          	sub    $0x10,%rsp
    15e7:	48 89 7d f8          	mov    %rdi,-0x8(%rbp)
    15eb:	48 8b 45 f8          	mov    -0x8(%rbp),%rax
    15ef:	48 89 c6             	mov    %rax,%rsi
    15f2:	48 8d 05 f0 0c 00 00 	lea    0xcf0(%rip),%rax        # 22e9 <_IO_stdin_used+0x2e9>
    15f9:	48 89 c7             	mov    %rax,%rdi
    15fc:	b8 00 00 00 00       	mov    $0x0,%eax
    1601:	e8 3a fb ff ff       	call   1140 <printf@plt>
    1606:	bf 08 00 00 00       	mov    $0x8,%edi
    160b:	e8 70 fb ff ff       	call   1180 <exit@plt>

0000000000001610 <read_six_numbers>:
    1610:	f3 0f 1e fa          	endbr64 
    1614:	55                   	push   %rbp
    1615:	48 89 e5             	mov    %rsp,%rbp
    1618:	48 83 ec 20          	sub    $0x20,%rsp
    161c:	48 89 7d e8          	mov    %rdi,-0x18(%rbp)
    1620:	48 89 75 e0          	mov    %rsi,-0x20(%rbp)
    1624:	48 8b 45 e0          	mov    -0x20(%rbp),%rax
    1628:	48 8d 78 14          	lea    0x14(%rax),%rdi
    162c:	48 8b 45 e0          	mov    -0x20(%rbp),%rax
    1630:	48 8d 70 10          	lea    0x10(%rax),%rsi
    1634:	48 8b 45 e0          	mov    -0x20(%rbp),%rax
    1638:	4c 8d 48 0c          	lea    0xc(%rax),%r9
    163c:	48 8b 45 e0          	mov    -0x20(%rbp),%rax
    1640:	4c 8d 40 08          	lea    0x8(%rax),%r8
    1644:	48 8b 45 e0          	mov    -0x20(%rbp),%rax
    1648:	48 8d 48 04          	lea    0x4(%rax),%rcx
    164c:	48 8b 55 e0          	mov    -0x20(%rbp),%rdx
    1650:	48 8b 45 e8          	mov    -0x18(%rbp),%rax
    1654:	57                   	push   %rdi
    1655:	56                   	push   %rsi
    1656:	48 8d 35 9d 0c 00 00 	lea    0xc9d(%rip),%rsi        # 22fa <_IO_stdin_used+0x2fa>
    165d:	48 89 c7             	mov    %rax,%rdi
    1660:	b8 00 00 00 00       	mov    $0x0,%eax
    1665:	e8 f6 fa ff ff       	call   1160 <__isoc99_sscanf@plt>
    166a:	48 83 c4 10          	add    $0x10,%rsp
    166e:	89 45 fc             	mov    %eax,-0x4(%rbp)
    1671:	83 7d fc 05          	cmpl   $0x5,-0x4(%rbp)
    1675:	7f 05                	jg     167c <read_six_numbers+0x6c>
    1677:	e8 0e 03 00 00       	call   198a <explode_bomb>
    167c:	90                   	nop
    167d:	c9                   	leave  
    167e:	c3                   	ret    

000000000000167f <string_length>:
    167f:	f3 0f 1e fa          	endbr64 
    1683:	55                   	push   %rbp
    1684:	48 89 e5             	mov    %rsp,%rbp
    1687:	48 89 7d e8          	mov    %rdi,-0x18(%rbp)
    168b:	48 8b 45 e8          	mov    -0x18(%rbp),%rax
    168f:	48 89 45 f8          	mov    %rax,-0x8(%rbp)
    1693:	c7 45 f4 00 00 00 00 	movl   $0x0,-0xc(%rbp)
    169a:	eb 09                	jmp    16a5 <string_length+0x26>
    169c:	48 83 45 f8 01       	addq   $0x1,-0x8(%rbp)
    16a1:	83 45 f4 01          	addl   $0x1,-0xc(%rbp)
    16a5:	48 8b 45 f8          	mov    -0x8(%rbp),%rax
    16a9:	0f b6 00             	movzbl (%rax),%eax
    16ac:	84 c0                	test   %al,%al
    16ae:	75 ec                	jne    169c <string_length+0x1d>
    16b0:	8b 45 f4             	mov    -0xc(%rbp),%eax
    16b3:	5d                   	pop    %rbp
    16b4:	c3                   	ret    

00000000000016b5 <strings_not_equal>:
    16b5:	f3 0f 1e fa          	endbr64 
    16b9:	55                   	push   %rbp
    16ba:	48 89 e5             	mov    %rsp,%rbp
    16bd:	53                   	push   %rbx
    16be:	48 83 ec 20          	sub    $0x20,%rsp
    16c2:	48 89 7d e0          	mov    %rdi,-0x20(%rbp)
    16c6:	48 89 75 d8          	mov    %rsi,-0x28(%rbp)
    16ca:	48 8b 45 e0          	mov    -0x20(%rbp),%rax
    16ce:	48 89 c7             	mov    %rax,%rdi
    16d1:	e8 a9 ff ff ff       	call   167f <string_length>
    16d6:	89 c3                	mov    %eax,%ebx
    16d8:	48 8b 45 d8          	mov    -0x28(%rbp),%rax
    16dc:	48 89 c7             	mov    %rax,%rdi
    16df:	e8 9b ff ff ff       	call   167f <string_length>
    16e4:	39 c3                	cmp    %eax,%ebx
    16e6:	74 07                	je     16ef <strings_not_equal+0x3a>
    16e8:	b8 01 00 00 00       	mov    $0x1,%eax
    16ed:	eb 45                	jmp    1734 <strings_not_equal+0x7f>
    16ef:	48 8b 45 e0          	mov    -0x20(%rbp),%rax
    16f3:	48 89 45 e8          	mov    %rax,-0x18(%rbp)
    16f7:	48 8b 45 d8          	mov    -0x28(%rbp),%rax
    16fb:	48 89 45 f0          	mov    %rax,-0x10(%rbp)
    16ff:	eb 23                	jmp    1724 <strings_not_equal+0x6f>
    1701:	48 8b 45 e8          	mov    -0x18(%rbp),%rax
    1705:	0f b6 10             	movzbl (%rax),%edx
    1708:	48 8b 45 f0          	mov    -0x10(%rbp),%rax
    170c:	0f b6 00             	movzbl (%rax),%eax
    170f:	38 c2                	cmp    %al,%dl
    1711:	74 07                	je     171a <strings_not_equal+0x65>
    1713:	b8 01 00 00 00       	mov    $0x1,%eax
    1718:	eb 1a                	jmp    1734 <strings_not_equal+0x7f>
    171a:	48 83 45 e8 01       	addq   $0x1,-0x18(%rbp)
    171f:	48 83 45 f0 01       	addq   $0x1,-0x10(%rbp)
    1724:	48 8b 45 e8          	mov    -0x18(%rbp),%rax
    1728:	0f b6 00             	movzbl (%rax),%eax
    172b:	84 c0                	test   %al,%al
    172d:	75 d2                	jne    1701 <strings_not_equal+0x4c>
    172f:	b8 00 00 00 00       	mov    $0x0,%eax
    1734:	48 8b 5d f8          	mov    -0x8(%rbp),%rbx
    1738:	c9                   	leave  
    1739:	c3                   	ret    

000000000000173a <blank_line>:
    173a:	f3 0f 1e fa          	endbr64 
    173e:	55                   	push   %rbp
    173f:	48 89 e5             	mov    %rsp,%rbp
    1742:	48 83 ec 10          	sub    $0x10,%rsp
    1746:	48 89 7d f8          	mov    %rdi,-0x8(%rbp)
    174a:	eb 37                	jmp    1783 <blank_line+0x49>
    174c:	e8 3f fa ff ff       	call   1190 <__ctype_b_loc@plt>
    1751:	48 8b 08             	mov    (%rax),%rcx
    1754:	48 8b 45 f8          	mov    -0x8(%rbp),%rax
    1758:	48 8d 50 01          	lea    0x1(%rax),%rdx
    175c:	48 89 55 f8          	mov    %rdx,-0x8(%rbp)
    1760:	0f b6 00             	movzbl (%rax),%eax
    1763:	48 0f be c0          	movsbq %al,%rax
    1767:	48 01 c0             	add    %rax,%rax
    176a:	48 01 c8             	add    %rcx,%rax
    176d:	0f b7 00             	movzwl (%rax),%eax
    1770:	0f b7 c0             	movzwl %ax,%eax
    1773:	25 00 20 00 00       	and    $0x2000,%eax
    1778:	85 c0                	test   %eax,%eax
    177a:	75 07                	jne    1783 <blank_line+0x49>
    177c:	b8 00 00 00 00       	mov    $0x0,%eax
    1781:	eb 10                	jmp    1793 <blank_line+0x59>
    1783:	48 8b 45 f8          	mov    -0x8(%rbp),%rax
    1787:	0f b6 00             	movzbl (%rax),%eax
    178a:	84 c0                	test   %al,%al
    178c:	75 be                	jne    174c <blank_line+0x12>
    178e:	b8 01 00 00 00       	mov    $0x1,%eax
    1793:	c9                   	leave  
    1794:	c3                   	ret    

0000000000001795 <skip>:
    1795:	f3 0f 1e fa          	endbr64 
    1799:	55                   	push   %rbp
    179a:	48 89 e5             	mov    %rsp,%rbp
    179d:	48 83 ec 10          	sub    $0x10,%rsp
    17a1:	48 8b 15 e8 2c 00 00 	mov    0x2ce8(%rip),%rdx        # 4490 <infile>
    17a8:	8b 05 52 33 00 00    	mov    0x3352(%rip),%eax        # 4b00 <num_input_strings>
    17ae:	48 63 c8             	movslq %eax,%rcx
    17b1:	48 89 c8             	mov    %rcx,%rax
    17b4:	48 c1 e0 02          	shl    $0x2,%rax
    17b8:	48 01 c8             	add    %rcx,%rax
    17bb:	48 c1 e0 04          	shl    $0x4,%rax
    17bf:	48 8d 0d fa 2c 00 00 	lea    0x2cfa(%rip),%rcx        # 44c0 <input_strings>
    17c6:	48 01 c8             	add    %rcx,%rax
    17c9:	be 50 00 00 00       	mov    $0x50,%esi
    17ce:	48 89 c7             	mov    %rax,%rdi
    17d1:	e8 7a f9 ff ff       	call   1150 <fgets@plt>
    17d6:	48 89 45 f8          	mov    %rax,-0x8(%rbp)
    17da:	48 83 7d f8 00       	cmpq   $0x0,-0x8(%rbp)
    17df:	74 10                	je     17f1 <skip+0x5c>
    17e1:	48 8b 45 f8          	mov    -0x8(%rbp),%rax
    17e5:	48 89 c7             	mov    %rax,%rdi
    17e8:	e8 4d ff ff ff       	call   173a <blank_line>
    17ed:	85 c0                	test   %eax,%eax
    17ef:	75 b0                	jne    17a1 <skip+0xc>
    17f1:	48 8b 45 f8          	mov    -0x8(%rbp),%rax
    17f5:	c9                   	leave  
    17f6:	c3                   	ret    

00000000000017f7 <read_line>:
    17f7:	f3 0f 1e fa          	endbr64 
    17fb:	55                   	push   %rbp
    17fc:	48 89 e5             	mov    %rsp,%rbp
    17ff:	48 83 ec 10          	sub    $0x10,%rsp
    1803:	b8 00 00 00 00       	mov    $0x0,%eax
    1808:	e8 88 ff ff ff       	call   1795 <skip>
    180d:	48 89 45 f8          	mov    %rax,-0x8(%rbp)
    1811:	48 83 7d f8 00       	cmpq   $0x0,-0x8(%rbp)
    1816:	0f 85 86 00 00 00    	jne    18a2 <read_line+0xab>
    181c:	48 8b 15 6d 2c 00 00 	mov    0x2c6d(%rip),%rdx        # 4490 <infile>
    1823:	48 8b 05 56 2c 00 00 	mov    0x2c56(%rip),%rax        # 4480 <stdin@GLIBC_2.2.5>
    182a:	48 39 c2             	cmp    %rax,%rdx
    182d:	75 19                	jne    1848 <read_line+0x51>
    182f:	48 8d 05 d6 0a 00 00 	lea    0xad6(%rip),%rax        # 230c <_IO_stdin_used+0x30c>
    1836:	48 89 c7             	mov    %rax,%rdi
    1839:	e8 d2 f8 ff ff       	call   1110 <puts@plt>
    183e:	bf 08 00 00 00       	mov    $0x8,%edi
    1843:	e8 38 f9 ff ff       	call   1180 <exit@plt>
    1848:	48 8d 05 db 0a 00 00 	lea    0xadb(%rip),%rax        # 232a <_IO_stdin_used+0x32a>
    184f:	48 89 c7             	mov    %rax,%rdi
    1852:	e8 99 f8 ff ff       	call   10f0 <getenv@plt>
    1857:	48 85 c0             	test   %rax,%rax
    185a:	74 0a                	je     1866 <read_line+0x6f>
    185c:	bf 00 00 00 00       	mov    $0x0,%edi
    1861:	e8 1a f9 ff ff       	call   1180 <exit@plt>
    1866:	48 8b 05 13 2c 00 00 	mov    0x2c13(%rip),%rax        # 4480 <stdin@GLIBC_2.2.5>
    186d:	48 89 05 1c 2c 00 00 	mov    %rax,0x2c1c(%rip)        # 4490 <infile>
    1874:	b8 00 00 00 00       	mov    $0x0,%eax
    1879:	e8 17 ff ff ff       	call   1795 <skip>
    187e:	48 89 45 f8          	mov    %rax,-0x8(%rbp)
    1882:	48 83 7d f8 00       	cmpq   $0x0,-0x8(%rbp)
    1887:	75 19                	jne    18a2 <read_line+0xab>
    1889:	48 8d 05 7c 0a 00 00 	lea    0xa7c(%rip),%rax        # 230c <_IO_stdin_used+0x30c>
    1890:	48 89 c7             	mov    %rax,%rdi
    1893:	e8 78 f8 ff ff       	call   1110 <puts@plt>
    1898:	bf 00 00 00 00       	mov    $0x0,%edi
    189d:	e8 de f8 ff ff       	call   1180 <exit@plt>
    18a2:	8b 05 58 32 00 00    	mov    0x3258(%rip),%eax        # 4b00 <num_input_strings>
    18a8:	48 63 d0             	movslq %eax,%rdx
    18ab:	48 89 d0             	mov    %rdx,%rax
    18ae:	48 c1 e0 02          	shl    $0x2,%rax
    18b2:	48 01 d0             	add    %rdx,%rax
    18b5:	48 c1 e0 04          	shl    $0x4,%rax
    18b9:	48 8d 15 00 2c 00 00 	lea    0x2c00(%rip),%rdx        # 44c0 <input_strings>
    18c0:	48 01 d0             	add    %rdx,%rax
    18c3:	48 89 c7             	mov    %rax,%rdi
    18c6:	e8 55 f8 ff ff       	call   1120 <strlen@plt>
    18cb:	89 45 f4             	mov    %eax,-0xc(%rbp)
    18ce:	83 7d f4 4e          	cmpl   $0x4e,-0xc(%rbp)
    18d2:	7e 59                	jle    192d <read_line+0x136>
    18d4:	48 8d 05 5a 0a 00 00 	lea    0xa5a(%rip),%rax        # 2335 <_IO_stdin_used+0x335>
    18db:	48 89 c7             	mov    %rax,%rdi
    18de:	e8 2d f8 ff ff       	call   1110 <puts@plt>
    18e3:	8b 05 17 32 00 00    	mov    0x3217(%rip),%eax        # 4b00 <num_input_strings>
    18e9:	8d 50 01             	lea    0x1(%rax),%edx
    18ec:	89 15 0e 32 00 00    	mov    %edx,0x320e(%rip)        # 4b00 <num_input_strings>
    18f2:	48 63 d0             	movslq %eax,%rdx
    18f5:	48 89 d0             	mov    %rdx,%rax
    18f8:	48 c1 e0 02          	shl    $0x2,%rax
    18fc:	48 01 d0             	add    %rdx,%rax
    18ff:	48 c1 e0 04          	shl    $0x4,%rax
    1903:	48 8d 15 b6 2b 00 00 	lea    0x2bb6(%rip),%rdx        # 44c0 <input_strings>
    190a:	48 01 d0             	add    %rdx,%rax
    190d:	48 be 2a 2a 2a 74 72 	movabs $0x636e7572742a2a2a,%rsi
    1914:	75 6e 63 
    1917:	48 bf 61 74 65 64 2a 	movabs $0x2a2a2a64657461,%rdi
    191e:	2a 2a 00 
    1921:	48 89 30             	mov    %rsi,(%rax)
    1924:	48 89 78 08          	mov    %rdi,0x8(%rax)
    1928:	e8 5d 00 00 00       	call   198a <explode_bomb>
    192d:	8b 05 cd 31 00 00    	mov    0x31cd(%rip),%eax        # 4b00 <num_input_strings>
    1933:	8b 55 f4             	mov    -0xc(%rbp),%edx
    1936:	83 ea 01             	sub    $0x1,%edx
    1939:	48 63 ca             	movslq %edx,%rcx
    193c:	48 63 d0             	movslq %eax,%rdx
    193f:	48 89 d0             	mov    %rdx,%rax
    1942:	48 c1 e0 02          	shl    $0x2,%rax
    1946:	48 01 d0             	add    %rdx,%rax
    1949:	48 c1 e0 04          	shl    $0x4,%rax
    194d:	48 8d 14 08          	lea    (%rax,%rcx,1),%rdx
    1951:	48 8d 05 68 2b 00 00 	lea    0x2b68(%rip),%rax        # 44c0 <input_strings>
    1958:	48 01 d0             	add    %rdx,%rax
    195b:	c6 00 00             	movb   $0x0,(%rax)
    195e:	8b 05 9c 31 00 00    	mov    0x319c(%rip),%eax        # 4b00 <num_input_strings>
    1964:	8d 50 01             	lea    0x1(%rax),%edx
    1967:	89 15 93 31 00 00    	mov    %edx,0x3193(%rip)        # 4b00 <num_input_strings>
    196d:	48 63 d0             	movslq %eax,%rdx
    1970:	48 89 d0             	mov    %rdx,%rax
    1973:	48 c1 e0 02          	shl    $0x2,%rax
    1977:	48 01 d0             	add    %rdx,%rax
    197a:	48 c1 e0 04          	shl    $0x4,%rax
    197e:	48 8d 15 3b 2b 00 00 	lea    0x2b3b(%rip),%rdx        # 44c0 <input_strings>
    1985:	48 01 d0             	add    %rdx,%rax
    1988:	c9                   	leave  
    1989:	c3                   	ret    

000000000000198a <explode_bomb>:
    198a:	f3 0f 1e fa          	endbr64 
    198e:	55                   	push   %rbp
    198f:	48 89 e5             	mov    %rsp,%rbp
    1992:	48 8d 05 b7 09 00 00 	lea    0x9b7(%rip),%rax        # 2350 <_IO_stdin_used+0x350>
    1999:	48 89 c7             	mov    %rax,%rdi
    199c:	e8 6f f7 ff ff       	call   1110 <puts@plt>
    19a1:	bf 08 00 00 00       	mov    $0x8,%edi
    19a6:	e8 d5 f7 ff ff       	call   1180 <exit@plt>

00000000000019ab <phase_1>:
    19ab:	f3 0f 1e fa          	endbr64 
    19af:	55                   	push   %rbp
    19b0:	48 89 e5             	mov    %rsp,%rbp
    19b3:	48 83 ec 20          	sub    $0x20,%rsp
    19b7:	48 89 7d e8          	mov    %rdi,-0x18(%rbp)
    19bb:	0f b6 05 df 2a 00 00 	movzbl 0x2adf(%rip),%eax        # 44a1 <studentid+0x9>
    19c2:	83 e8 30             	sub    $0x30,%eax
    19c5:	88 45 fb             	mov    %al,-0x5(%rbp)
    19c8:	0f be 45 fb          	movsbl -0x5(%rbp),%eax
    19cc:	89 45 fc             	mov    %eax,-0x4(%rbp)
    19cf:	8b 55 fc             	mov    -0x4(%rbp),%edx
    19d2:	48 89 d0             	mov    %rdx,%rax
    19d5:	48 c1 e0 02          	shl    $0x2,%rax
    19d9:	48 01 d0             	add    %rdx,%rax
    19dc:	48 8d 14 85 00 00 00 	lea    0x0(,%rax,4),%rdx
    19e3:	00 
    19e4:	48 01 d0             	add    %rdx,%rax
    19e7:	48 01 c0             	add    %rax,%rax
    19ea:	48 8d 15 2f 26 00 00 	lea    0x262f(%rip),%rdx        # 4020 <special>
    19f1:	48 01 c2             	add    %rax,%rdx
    19f4:	48 8b 45 e8          	mov    -0x18(%rbp),%rax
    19f8:	48 89 d6             	mov    %rdx,%rsi
    19fb:	48 89 c7             	mov    %rax,%rdi
    19fe:	e8 b2 fc ff ff       	call   16b5 <strings_not_equal>
    1a03:	85 c0                	test   %eax,%eax
    1a05:	74 05                	je     1a0c <phase_1+0x61>
    1a07:	e8 7e ff ff ff       	call   198a <explode_bomb>
    1a0c:	90                   	nop
    1a0d:	c9                   	leave  
    1a0e:	c3                   	ret    

0000000000001a0f <phase_2>:
    1a0f:	f3 0f 1e fa          	endbr64 
    1a13:	55                   	push   %rbp
    1a14:	48 89 e5             	mov    %rsp,%rbp
    1a17:	48 83 ec 40          	sub    $0x40,%rsp
    1a1b:	48 89 7d c8          	mov    %rdi,-0x38(%rbp)
    1a1f:	64 48 8b 04 25 28 00 	mov    %fs:0x28,%rax
    1a26:	00 00 
    1a28:	48 89 45 f8          	mov    %rax,-0x8(%rbp)
    1a2c:	31 c0                	xor    %eax,%eax
    1a2e:	48 8d 55 e0          	lea    -0x20(%rbp),%rdx
    1a32:	48 8b 45 c8          	mov    -0x38(%rbp),%rax
    1a36:	48 89 d6             	mov    %rdx,%rsi
    1a39:	48 89 c7             	mov    %rax,%rdi
    1a3c:	e8 cf fb ff ff       	call   1610 <read_six_numbers>
    1a41:	8b 45 e0             	mov    -0x20(%rbp),%eax
    1a44:	85 c0                	test   %eax,%eax
    1a46:	79 05                	jns    1a4d <phase_2+0x3e>
    1a48:	e8 3d ff ff ff       	call   198a <explode_bomb>
    1a4d:	8b 45 e0             	mov    -0x20(%rbp),%eax
    1a50:	0f b6 15 4a 2a 00 00 	movzbl 0x2a4a(%rip),%edx        # 44a1 <studentid+0x9>
    1a57:	0f be d2             	movsbl %dl,%edx
    1a5a:	83 ea 30             	sub    $0x30,%edx
    1a5d:	39 d0                	cmp    %edx,%eax
    1a5f:	74 05                	je     1a66 <phase_2+0x57>
    1a61:	e8 24 ff ff ff       	call   198a <explode_bomb>
    1a66:	8b 45 e4             	mov    -0x1c(%rbp),%eax
    1a69:	0f b6 15 30 2a 00 00 	movzbl 0x2a30(%rip),%edx        # 44a0 <studentid+0x8>
    1a70:	0f be d2             	movsbl %dl,%edx
    1a73:	83 ea 30             	sub    $0x30,%edx
    1a76:	39 d0                	cmp    %edx,%eax
    1a78:	74 05                	je     1a7f <phase_2+0x70>
    1a7a:	e8 0b ff ff ff       	call   198a <explode_bomb>
    1a7f:	c7 45 dc 02 00 00 00 	movl   $0x2,-0x24(%rbp)
    1a86:	eb 30                	jmp    1ab8 <phase_2+0xa9>
    1a88:	8b 45 dc             	mov    -0x24(%rbp),%eax
    1a8b:	48 98                	cltq   
    1a8d:	8b 54 85 e0          	mov    -0x20(%rbp,%rax,4),%edx
    1a91:	8b 45 dc             	mov    -0x24(%rbp),%eax
    1a94:	83 e8 01             	sub    $0x1,%eax
    1a97:	48 98                	cltq   
    1a99:	8b 4c 85 e0          	mov    -0x20(%rbp,%rax,4),%ecx
    1a9d:	8b 45 dc             	mov    -0x24(%rbp),%eax
    1aa0:	83 e8 02             	sub    $0x2,%eax
    1aa3:	48 98                	cltq   
    1aa5:	8b 44 85 e0          	mov    -0x20(%rbp,%rax,4),%eax
    1aa9:	01 c8                	add    %ecx,%eax
    1aab:	39 c2                	cmp    %eax,%edx
    1aad:	74 05                	je     1ab4 <phase_2+0xa5>
    1aaf:	e8 d6 fe ff ff       	call   198a <explode_bomb>
    1ab4:	83 45 dc 01          	addl   $0x1,-0x24(%rbp)
    1ab8:	83 7d dc 05          	cmpl   $0x5,-0x24(%rbp)
    1abc:	7e ca                	jle    1a88 <phase_2+0x79>
    1abe:	90                   	nop
    1abf:	48 8b 45 f8          	mov    -0x8(%rbp),%rax
    1ac3:	64 48 33 04 25 28 00 	xor    %fs:0x28,%rax
    1aca:	00 00 
    1acc:	74 05                	je     1ad3 <phase_2+0xc4>
    1ace:	e8 5d f6 ff ff       	call   1130 <__stack_chk_fail@plt>
    1ad3:	c9                   	leave  
    1ad4:	c3                   	ret    

0000000000001ad5 <phase_3>:
    1ad5:	f3 0f 1e fa          	endbr64 
    1ad9:	55                   	push   %rbp
    1ada:	48 89 e5             	mov    %rsp,%rbp
    1add:	48 83 ec 30          	sub    $0x30,%rsp
    1ae1:	48 89 7d d8          	mov    %rdi,-0x28(%rbp)
    1ae5:	64 48 8b 04 25 28 00 	mov    %fs:0x28,%rax
    1aec:	00 00 
    1aee:	48 89 45 f8          	mov    %rax,-0x8(%rbp)
    1af2:	31 c0                	xor    %eax,%eax
    1af4:	c7 45 f0 00 00 00 00 	movl   $0x0,-0x10(%rbp)
    1afb:	c7 45 f4 00 00 00 00 	movl   $0x0,-0xc(%rbp)
    1b02:	48 8d 4d ec          	lea    -0x14(%rbp),%rcx
    1b06:	48 8d 55 e8          	lea    -0x18(%rbp),%rdx
    1b0a:	48 8b 45 d8          	mov    -0x28(%rbp),%rax
    1b0e:	48 8d 35 53 08 00 00 	lea    0x853(%rip),%rsi        # 2368 <_IO_stdin_used+0x368>
    1b15:	48 89 c7             	mov    %rax,%rdi
    1b18:	b8 00 00 00 00       	mov    $0x0,%eax
    1b1d:	e8 3e f6 ff ff       	call   1160 <__isoc99_sscanf@plt>
    1b22:	89 45 f4             	mov    %eax,-0xc(%rbp)
    1b25:	83 7d f4 01          	cmpl   $0x1,-0xc(%rbp)
    1b29:	7f 05                	jg     1b30 <phase_3+0x5b>
    1b2b:	e8 5a fe ff ff       	call   198a <explode_bomb>
    1b30:	0f b6 05 68 29 00 00 	movzbl 0x2968(%rip),%eax        # 449f <studentid+0x7>
    1b37:	0f be c0             	movsbl %al,%eax
    1b3a:	8d 50 d0             	lea    -0x30(%rax),%edx
    1b3d:	8b 45 e8             	mov    -0x18(%rbp),%eax
    1b40:	39 c2                	cmp    %eax,%edx
    1b42:	74 05                	je     1b49 <phase_3+0x74>
    1b44:	e8 41 fe ff ff       	call   198a <explode_bomb>
    1b49:	8b 45 e8             	mov    -0x18(%rbp),%eax
    1b4c:	83 f8 09             	cmp    $0x9,%eax
    1b4f:	77 7d                	ja     1bce <phase_3+0xf9>
    1b51:	89 c0                	mov    %eax,%eax
    1b53:	48 8d 14 85 00 00 00 	lea    0x0(,%rax,4),%rdx
    1b5a:	00 
    1b5b:	48 8d 05 0e 08 00 00 	lea    0x80e(%rip),%rax        # 2370 <_IO_stdin_used+0x370>
    1b62:	8b 04 02             	mov    (%rdx,%rax,1),%eax
    1b65:	48 98                	cltq   
    1b67:	48 8d 15 02 08 00 00 	lea    0x802(%rip),%rdx        # 2370 <_IO_stdin_used+0x370>
    1b6e:	48 01 d0             	add    %rdx,%rax
    1b71:	3e ff e0             	notrack jmp *%rax
    1b74:	c7 45 f0 2f 03 00 00 	movl   $0x32f,-0x10(%rbp)
    1b7b:	eb 56                	jmp    1bd3 <phase_3+0xfe>
    1b7d:	c7 45 f0 30 01 00 00 	movl   $0x130,-0x10(%rbp)
    1b84:	eb 4d                	jmp    1bd3 <phase_3+0xfe>
    1b86:	c7 45 f0 84 01 00 00 	movl   $0x184,-0x10(%rbp)
    1b8d:	eb 44                	jmp    1bd3 <phase_3+0xfe>
    1b8f:	c7 45 f0 8e 02 00 00 	movl   $0x28e,-0x10(%rbp)
    1b96:	eb 3b                	jmp    1bd3 <phase_3+0xfe>
    1b98:	c7 45 f0 1c 01 00 00 	movl   $0x11c,-0x10(%rbp)
    1b9f:	eb 32                	jmp    1bd3 <phase_3+0xfe>
    1ba1:	c7 45 f0 01 02 00 00 	movl   $0x201,-0x10(%rbp)
    1ba8:	eb 29                	jmp    1bd3 <phase_3+0xfe>
    1baa:	c7 45 f0 a9 01 00 00 	movl   $0x1a9,-0x10(%rbp)
    1bb1:	eb 20                	jmp    1bd3 <phase_3+0xfe>
    1bb3:	c7 45 f0 74 03 00 00 	movl   $0x374,-0x10(%rbp)
    1bba:	eb 17                	jmp    1bd3 <phase_3+0xfe>
    1bbc:	c7 45 f0 7b 00 00 00 	movl   $0x7b,-0x10(%rbp)
    1bc3:	eb 0e                	jmp    1bd3 <phase_3+0xfe>
    1bc5:	c7 45 f0 41 01 00 00 	movl   $0x141,-0x10(%rbp)
    1bcc:	eb 05                	jmp    1bd3 <phase_3+0xfe>
    1bce:	e8 b7 fd ff ff       	call   198a <explode_bomb>
    1bd3:	8b 45 ec             	mov    -0x14(%rbp),%eax
    1bd6:	39 45 f0             	cmp    %eax,-0x10(%rbp)
    1bd9:	74 05                	je     1be0 <phase_3+0x10b>
    1bdb:	e8 aa fd ff ff       	call   198a <explode_bomb>
    1be0:	90                   	nop
    1be1:	48 8b 45 f8          	mov    -0x8(%rbp),%rax
    1be5:	64 48 33 04 25 28 00 	xor    %fs:0x28,%rax
    1bec:	00 00 
    1bee:	74 05                	je     1bf5 <phase_3+0x120>
    1bf0:	e8 3b f5 ff ff       	call   1130 <__stack_chk_fail@plt>
    1bf5:	c9                   	leave  
    1bf6:	c3                   	ret    

0000000000001bf7 <func4>:
    1bf7:	f3 0f 1e fa          	endbr64 
    1bfb:	55                   	push   %rbp
    1bfc:	48 89 e5             	mov    %rsp,%rbp
    1bff:	48 83 ec 20          	sub    $0x20,%rsp
    1c03:	89 7d ec             	mov    %edi,-0x14(%rbp)
    1c06:	89 75 e8             	mov    %esi,-0x18(%rbp)
    1c09:	89 55 e4             	mov    %edx,-0x1c(%rbp)
    1c0c:	8b 45 e4             	mov    -0x1c(%rbp),%eax
    1c0f:	2b 45 e8             	sub    -0x18(%rbp),%eax
    1c12:	89 c2                	mov    %eax,%edx
    1c14:	c1 ea 1f             	shr    $0x1f,%edx
    1c17:	01 d0                	add    %edx,%eax
    1c19:	d1 f8                	sar    %eax
    1c1b:	89 c2                	mov    %eax,%edx
    1c1d:	8b 45 e8             	mov    -0x18(%rbp),%eax
    1c20:	01 d0                	add    %edx,%eax
    1c22:	89 45 fc             	mov    %eax,-0x4(%rbp)
    1c25:	8b 45 fc             	mov    -0x4(%rbp),%eax
    1c28:	3b 45 ec             	cmp    -0x14(%rbp),%eax
    1c2b:	7e 19                	jle    1c46 <func4+0x4f>
    1c2d:	8b 45 fc             	mov    -0x4(%rbp),%eax
    1c30:	8d 50 ff             	lea    -0x1(%rax),%edx
    1c33:	8b 4d e8             	mov    -0x18(%rbp),%ecx
    1c36:	8b 45 ec             	mov    -0x14(%rbp),%eax
    1c39:	89 ce                	mov    %ecx,%esi
    1c3b:	89 c7                	mov    %eax,%edi
    1c3d:	e8 b5 ff ff ff       	call   1bf7 <func4>
    1c42:	01 c0                	add    %eax,%eax
    1c44:	eb 29                	jmp    1c6f <func4+0x78>
    1c46:	8b 45 fc             	mov    -0x4(%rbp),%eax
    1c49:	3b 45 ec             	cmp    -0x14(%rbp),%eax
    1c4c:	7d 1c                	jge    1c6a <func4+0x73>
    1c4e:	8b 45 fc             	mov    -0x4(%rbp),%eax
    1c51:	8d 48 01             	lea    0x1(%rax),%ecx
    1c54:	8b 55 e4             	mov    -0x1c(%rbp),%edx
    1c57:	8b 45 ec             	mov    -0x14(%rbp),%eax
    1c5a:	89 ce                	mov    %ecx,%esi
    1c5c:	89 c7                	mov    %eax,%edi
    1c5e:	e8 94 ff ff ff       	call   1bf7 <func4>
    1c63:	01 c0                	add    %eax,%eax
    1c65:	83 c0 01             	add    $0x1,%eax
    1c68:	eb 05                	jmp    1c6f <func4+0x78>
    1c6a:	b8 00 00 00 00       	mov    $0x0,%eax
    1c6f:	c9                   	leave  
    1c70:	c3                   	ret    

0000000000001c71 <phase_4>:
    1c71:	f3 0f 1e fa          	endbr64 
    1c75:	55                   	push   %rbp
    1c76:	48 89 e5             	mov    %rsp,%rbp
    1c79:	48 83 ec 30          	sub    $0x30,%rsp
    1c7d:	48 89 7d d8          	mov    %rdi,-0x28(%rbp)
    1c81:	64 48 8b 04 25 28 00 	mov    %fs:0x28,%rax
    1c88:	00 00 
    1c8a:	48 89 45 f8          	mov    %rax,-0x8(%rbp)
    1c8e:	31 c0                	xor    %eax,%eax
    1c90:	48 8d 4d e8          	lea    -0x18(%rbp),%rcx
    1c94:	48 8d 55 e4          	lea    -0x1c(%rbp),%rdx
    1c98:	48 8b 45 d8          	mov    -0x28(%rbp),%rax
    1c9c:	48 8d 35 c5 06 00 00 	lea    0x6c5(%rip),%rsi        # 2368 <_IO_stdin_used+0x368>
    1ca3:	48 89 c7             	mov    %rax,%rdi
    1ca6:	b8 00 00 00 00       	mov    $0x0,%eax
    1cab:	e8 b0 f4 ff ff       	call   1160 <__isoc99_sscanf@plt>
    1cb0:	89 45 ec             	mov    %eax,-0x14(%rbp)
    1cb3:	83 7d ec 02          	cmpl   $0x2,-0x14(%rbp)
    1cb7:	75 0f                	jne    1cc8 <phase_4+0x57>
    1cb9:	8b 45 e4             	mov    -0x1c(%rbp),%eax
    1cbc:	85 c0                	test   %eax,%eax
    1cbe:	78 08                	js     1cc8 <phase_4+0x57>
    1cc0:	8b 45 e4             	mov    -0x1c(%rbp),%eax
    1cc3:	83 f8 0e             	cmp    $0xe,%eax
    1cc6:	7e 05                	jle    1ccd <phase_4+0x5c>
    1cc8:	e8 bd fc ff ff       	call   198a <explode_bomb>
    1ccd:	c7 45 f0 07 00 00 00 	movl   $0x7,-0x10(%rbp)
    1cd4:	8b 45 e4             	mov    -0x1c(%rbp),%eax
    1cd7:	ba 0e 00 00 00       	mov    $0xe,%edx
    1cdc:	be 00 00 00 00       	mov    $0x0,%esi
    1ce1:	89 c7                	mov    %eax,%edi
    1ce3:	e8 0f ff ff ff       	call   1bf7 <func4>
    1ce8:	89 45 f4             	mov    %eax,-0xc(%rbp)
    1ceb:	8b 45 f4             	mov    -0xc(%rbp),%eax
    1cee:	3b 45 f0             	cmp    -0x10(%rbp),%eax
    1cf1:	75 08                	jne    1cfb <phase_4+0x8a>
    1cf3:	8b 45 e8             	mov    -0x18(%rbp),%eax
    1cf6:	39 45 f0             	cmp    %eax,-0x10(%rbp)
    1cf9:	74 05                	je     1d00 <phase_4+0x8f>
    1cfb:	e8 8a fc ff ff       	call   198a <explode_bomb>
    1d00:	90                   	nop
    1d01:	48 8b 45 f8          	mov    -0x8(%rbp),%rax
    1d05:	64 48 33 04 25 28 00 	xor    %fs:0x28,%rax
    1d0c:	00 00 
    1d0e:	74 05                	je     1d15 <phase_4+0xa4>
    1d10:	e8 1b f4 ff ff       	call   1130 <__stack_chk_fail@plt>
    1d15:	c9                   	leave  
    1d16:	c3                   	ret    

0000000000001d17 <phase_5>:
    1d17:	f3 0f 1e fa          	endbr64 
    1d1b:	55                   	push   %rbp
    1d1c:	48 89 e5             	mov    %rsp,%rbp
    1d1f:	48 83 ec 30          	sub    $0x30,%rsp
    1d23:	48 89 7d d8          	mov    %rdi,-0x28(%rbp)
    1d27:	64 48 8b 04 25 28 00 	mov    %fs:0x28,%rax
    1d2e:	00 00 
    1d30:	48 89 45 f8          	mov    %rax,-0x8(%rbp)
    1d34:	31 c0                	xor    %eax,%eax
    1d36:	48 8b 45 d8          	mov    -0x28(%rbp),%rax
    1d3a:	48 89 c7             	mov    %rax,%rdi
    1d3d:	e8 3d f9 ff ff       	call   167f <string_length>
    1d42:	89 45 ec             	mov    %eax,-0x14(%rbp)
    1d45:	83 7d ec 06          	cmpl   $0x6,-0x14(%rbp)
    1d49:	74 05                	je     1d50 <phase_5+0x39>
    1d4b:	e8 3a fc ff ff       	call   198a <explode_bomb>
    1d50:	c7 45 e8 00 00 00 00 	movl   $0x0,-0x18(%rbp)
    1d57:	eb 30                	jmp    1d89 <phase_5+0x72>
    1d59:	8b 45 e8             	mov    -0x18(%rbp),%eax
    1d5c:	48 63 d0             	movslq %eax,%rdx
    1d5f:	48 8b 45 d8          	mov    -0x28(%rbp),%rax
    1d63:	48 01 d0             	add    %rdx,%rax
    1d66:	0f b6 00             	movzbl (%rax),%eax
    1d69:	0f be c0             	movsbl %al,%eax
    1d6c:	83 e0 0f             	and    $0xf,%eax
    1d6f:	48 98                	cltq   
    1d71:	48 8d 15 b8 25 00 00 	lea    0x25b8(%rip),%rdx        # 4330 <array.3096>
    1d78:	0f b6 14 10          	movzbl (%rax,%rdx,1),%edx
    1d7c:	8b 45 e8             	mov    -0x18(%rbp),%eax
    1d7f:	48 98                	cltq   
    1d81:	88 54 05 f1          	mov    %dl,-0xf(%rbp,%rax,1)
    1d85:	83 45 e8 01          	addl   $0x1,-0x18(%rbp)
    1d89:	83 7d e8 05          	cmpl   $0x5,-0x18(%rbp)
    1d8d:	7e ca                	jle    1d59 <phase_5+0x42>
    1d8f:	c6 45 f7 00          	movb   $0x0,-0x9(%rbp)
    1d93:	48 8d 45 f1          	lea    -0xf(%rbp),%rax
    1d97:	48 8d 35 fa 05 00 00 	lea    0x5fa(%rip),%rsi        # 2398 <_IO_stdin_used+0x398>
    1d9e:	48 89 c7             	mov    %rax,%rdi
    1da1:	e8 0f f9 ff ff       	call   16b5 <strings_not_equal>
    1da6:	85 c0                	test   %eax,%eax
    1da8:	74 05                	je     1daf <phase_5+0x98>
    1daa:	e8 db fb ff ff       	call   198a <explode_bomb>
    1daf:	90                   	nop
    1db0:	48 8b 45 f8          	mov    -0x8(%rbp),%rax
    1db4:	64 48 33 04 25 28 00 	xor    %fs:0x28,%rax
    1dbb:	00 00 
    1dbd:	74 05                	je     1dc4 <phase_5+0xad>
    1dbf:	e8 6c f3 ff ff       	call   1130 <__stack_chk_fail@plt>
    1dc4:	c9                   	leave  
    1dc5:	c3                   	ret    

0000000000001dc6 <phase_6>:
    1dc6:	f3 0f 1e fa          	endbr64 
    1dca:	55                   	push   %rbp
    1dcb:	48 89 e5             	mov    %rsp,%rbp
    1dce:	48 81 ec 90 00 00 00 	sub    $0x90,%rsp
    1dd5:	48 89 bd 78 ff ff ff 	mov    %rdi,-0x88(%rbp)
    1ddc:	64 48 8b 04 25 28 00 	mov    %fs:0x28,%rax
    1de3:	00 00 
    1de5:	48 89 45 f8          	mov    %rax,-0x8(%rbp)
    1de9:	31 c0                	xor    %eax,%eax
    1deb:	48 8d 05 8e 25 00 00 	lea    0x258e(%rip),%rax        # 4380 <node1>
    1df2:	48 89 45 98          	mov    %rax,-0x68(%rbp)
    1df6:	48 8d 55 a0          	lea    -0x60(%rbp),%rdx
    1dfa:	48 8b 85 78 ff ff ff 	mov    -0x88(%rbp),%rax
    1e01:	48 89 d6             	mov    %rdx,%rsi
    1e04:	48 89 c7             	mov    %rax,%rdi
    1e07:	e8 04 f8 ff ff       	call   1610 <read_six_numbers>
    1e0c:	c7 45 88 00 00 00 00 	movl   $0x0,-0x78(%rbp)
    1e13:	eb 54                	jmp    1e69 <phase_6+0xa3>
    1e15:	8b 45 88             	mov    -0x78(%rbp),%eax
    1e18:	48 98                	cltq   
    1e1a:	8b 44 85 a0          	mov    -0x60(%rbp,%rax,4),%eax
    1e1e:	85 c0                	test   %eax,%eax
    1e20:	7e 0e                	jle    1e30 <phase_6+0x6a>
    1e22:	8b 45 88             	mov    -0x78(%rbp),%eax
    1e25:	48 98                	cltq   
    1e27:	8b 44 85 a0          	mov    -0x60(%rbp,%rax,4),%eax
    1e2b:	83 f8 06             	cmp    $0x6,%eax
    1e2e:	7e 05                	jle    1e35 <phase_6+0x6f>
    1e30:	e8 55 fb ff ff       	call   198a <explode_bomb>
    1e35:	8b 45 88             	mov    -0x78(%rbp),%eax
    1e38:	83 c0 01             	add    $0x1,%eax
    1e3b:	89 45 8c             	mov    %eax,-0x74(%rbp)
    1e3e:	eb 1f                	jmp    1e5f <phase_6+0x99>
    1e40:	8b 45 88             	mov    -0x78(%rbp),%eax
    1e43:	48 98                	cltq   
    1e45:	8b 54 85 a0          	mov    -0x60(%rbp,%rax,4),%edx
    1e49:	8b 45 8c             	mov    -0x74(%rbp),%eax
    1e4c:	48 98                	cltq   
    1e4e:	8b 44 85 a0          	mov    -0x60(%rbp,%rax,4),%eax
    1e52:	39 c2                	cmp    %eax,%edx
    1e54:	75 05                	jne    1e5b <phase_6+0x95>
    1e56:	e8 2f fb ff ff       	call   198a <explode_bomb>
    1e5b:	83 45 8c 01          	addl   $0x1,-0x74(%rbp)
    1e5f:	83 7d 8c 05          	cmpl   $0x5,-0x74(%rbp)
    1e63:	7e db                	jle    1e40 <phase_6+0x7a>
    1e65:	83 45 88 01          	addl   $0x1,-0x78(%rbp)
    1e69:	83 7d 88 05          	cmpl   $0x5,-0x78(%rbp)
    1e6d:	7e a6                	jle    1e15 <phase_6+0x4f>
    1e6f:	c7 45 88 00 00 00 00 	movl   $0x0,-0x78(%rbp)
    1e76:	eb 41                	jmp    1eb9 <phase_6+0xf3>
    1e78:	48 8b 45 98          	mov    -0x68(%rbp),%rax
    1e7c:	48 89 45 90          	mov    %rax,-0x70(%rbp)
    1e80:	c7 45 8c 01 00 00 00 	movl   $0x1,-0x74(%rbp)
    1e87:	eb 10                	jmp    1e99 <phase_6+0xd3>
    1e89:	48 8b 45 90          	mov    -0x70(%rbp),%rax
    1e8d:	48 8b 40 08          	mov    0x8(%rax),%rax
    1e91:	48 89 45 90          	mov    %rax,-0x70(%rbp)
    1e95:	83 45 8c 01          	addl   $0x1,-0x74(%rbp)
    1e99:	8b 45 88             	mov    -0x78(%rbp),%eax
    1e9c:	48 98                	cltq   
    1e9e:	8b 44 85 a0          	mov    -0x60(%rbp,%rax,4),%eax
    1ea2:	39 45 8c             	cmp    %eax,-0x74(%rbp)
    1ea5:	7c e2                	jl     1e89 <phase_6+0xc3>
    1ea7:	8b 45 88             	mov    -0x78(%rbp),%eax
    1eaa:	48 98                	cltq   
    1eac:	48 8b 55 90          	mov    -0x70(%rbp),%rdx
    1eb0:	48 89 54 c5 c0       	mov    %rdx,-0x40(%rbp,%rax,8)
    1eb5:	83 45 88 01          	addl   $0x1,-0x78(%rbp)
    1eb9:	83 7d 88 05          	cmpl   $0x5,-0x78(%rbp)
    1ebd:	7e b9                	jle    1e78 <phase_6+0xb2>
    1ebf:	48 8b 45 c0          	mov    -0x40(%rbp),%rax
    1ec3:	48 89 45 98          	mov    %rax,-0x68(%rbp)
    1ec7:	48 8b 45 98          	mov    -0x68(%rbp),%rax
    1ecb:	48 89 45 90          	mov    %rax,-0x70(%rbp)
    1ecf:	c7 45 88 01 00 00 00 	movl   $0x1,-0x78(%rbp)
    1ed6:	eb 22                	jmp    1efa <phase_6+0x134>
    1ed8:	8b 45 88             	mov    -0x78(%rbp),%eax
    1edb:	48 98                	cltq   
    1edd:	48 8b 54 c5 c0       	mov    -0x40(%rbp,%rax,8),%rdx
    1ee2:	48 8b 45 90          	mov    -0x70(%rbp),%rax
    1ee6:	48 89 50 08          	mov    %rdx,0x8(%rax)
    1eea:	48 8b 45 90          	mov    -0x70(%rbp),%rax
    1eee:	48 8b 40 08          	mov    0x8(%rax),%rax
    1ef2:	48 89 45 90          	mov    %rax,-0x70(%rbp)
    1ef6:	83 45 88 01          	addl   $0x1,-0x78(%rbp)
    1efa:	83 7d 88 05          	cmpl   $0x5,-0x78(%rbp)
    1efe:	7e d8                	jle    1ed8 <phase_6+0x112>
    1f00:	48 8b 45 90          	mov    -0x70(%rbp),%rax
    1f04:	48 c7 40 08 00 00 00 	movq   $0x0,0x8(%rax)
    1f0b:	00 
    1f0c:	48 8b 45 98          	mov    -0x68(%rbp),%rax
    1f10:	48 89 45 90          	mov    %rax,-0x70(%rbp)
    1f14:	c7 45 88 00 00 00 00 	movl   $0x0,-0x78(%rbp)
    1f1b:	eb 29                	jmp    1f46 <phase_6+0x180>
    1f1d:	48 8b 45 90          	mov    -0x70(%rbp),%rax
    1f21:	8b 10                	mov    (%rax),%edx
    1f23:	48 8b 45 90          	mov    -0x70(%rbp),%rax
    1f27:	48 8b 40 08          	mov    0x8(%rax),%rax
    1f2b:	8b 00                	mov    (%rax),%eax
    1f2d:	39 c2                	cmp    %eax,%edx
    1f2f:	7d 05                	jge    1f36 <phase_6+0x170>
    1f31:	e8 54 fa ff ff       	call   198a <explode_bomb>
    1f36:	48 8b 45 90          	mov    -0x70(%rbp),%rax
    1f3a:	48 8b 40 08          	mov    0x8(%rax),%rax
    1f3e:	48 89 45 90          	mov    %rax,-0x70(%rbp)
    1f42:	83 45 88 01          	addl   $0x1,-0x78(%rbp)
    1f46:	83 7d 88 04          	cmpl   $0x4,-0x78(%rbp)
    1f4a:	7e d1                	jle    1f1d <phase_6+0x157>
    1f4c:	90                   	nop
    1f4d:	48 8b 45 f8          	mov    -0x8(%rbp),%rax
    1f51:	64 48 33 04 25 28 00 	xor    %fs:0x28,%rax
    1f58:	00 00 
    1f5a:	74 05                	je     1f61 <phase_6+0x19b>
    1f5c:	e8 cf f1 ff ff       	call   1130 <__stack_chk_fail@plt>
    1f61:	c9                   	leave  
    1f62:	c3                   	ret    

0000000000001f63 <fun7>:
    1f63:	f3 0f 1e fa          	endbr64 
    1f67:	55                   	push   %rbp
    1f68:	48 89 e5             	mov    %rsp,%rbp
    1f6b:	48 83 ec 10          	sub    $0x10,%rsp
    1f6f:	48 89 7d f8          	mov    %rdi,-0x8(%rbp)
    1f73:	89 75 f4             	mov    %esi,-0xc(%rbp)
    1f76:	48 83 7d f8 00       	cmpq   $0x0,-0x8(%rbp)
    1f7b:	75 07                	jne    1f84 <fun7+0x21>
    1f7d:	b8 ff ff ff ff       	mov    $0xffffffff,%eax
    1f82:	eb 50                	jmp    1fd4 <fun7+0x71>
    1f84:	48 8b 45 f8          	mov    -0x8(%rbp),%rax
    1f88:	8b 00                	mov    (%rax),%eax
    1f8a:	39 45 f4             	cmp    %eax,-0xc(%rbp)
    1f8d:	7d 19                	jge    1fa8 <fun7+0x45>
    1f8f:	48 8b 45 f8          	mov    -0x8(%rbp),%rax
    1f93:	48 8b 40 08          	mov    0x8(%rax),%rax
    1f97:	8b 55 f4             	mov    -0xc(%rbp),%edx
    1f9a:	89 d6                	mov    %edx,%esi
    1f9c:	48 89 c7             	mov    %rax,%rdi
    1f9f:	e8 bf ff ff ff       	call   1f63 <fun7>
    1fa4:	01 c0                	add    %eax,%eax
    1fa6:	eb 2c                	jmp    1fd4 <fun7+0x71>
    1fa8:	48 8b 45 f8          	mov    -0x8(%rbp),%rax
    1fac:	8b 00                	mov    (%rax),%eax
    1fae:	39 45 f4             	cmp    %eax,-0xc(%rbp)
    1fb1:	75 07                	jne    1fba <fun7+0x57>
    1fb3:	b8 00 00 00 00       	mov    $0x0,%eax
    1fb8:	eb 1a                	jmp    1fd4 <fun7+0x71>
    1fba:	48 8b 45 f8          	mov    -0x8(%rbp),%rax
    1fbe:	48 8b 40 10          	mov    0x10(%rax),%rax
    1fc2:	8b 55 f4             	mov    -0xc(%rbp),%edx
    1fc5:	89 d6                	mov    %edx,%esi
    1fc7:	48 89 c7             	mov    %rax,%rdi
    1fca:	e8 94 ff ff ff       	call   1f63 <fun7>
    1fcf:	01 c0                	add    %eax,%eax
    1fd1:	83 c0 01             	add    $0x1,%eax
    1fd4:	c9                   	leave  
    1fd5:	c3                   	ret    

Disassembly of section .fini:

0000000000001fd8 <_fini>:
    1fd8:	f3 0f 1e fa          	endbr64 
    1fdc:	48 83 ec 08          	sub    $0x8,%rsp
    1fe0:	48 83 c4 08          	add    $0x8,%rsp
    1fe4:	c3                   	ret    
