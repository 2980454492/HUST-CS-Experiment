; 指定处理器指令集和模型
.686P
.model flat, c

; 声明 printf 函数原型
printf proto c :ptr sbyte, :vararg

; 包含库文件
includelib  libcmt.lib
includelib  legacy_stdio_definitions.lib 

; 定义学生结构体
student  struct
    sname   db   8 dup(0)       ; 学生姓名，8 字节
    sid     db   11 dup(0)      ; 学生学号，11 字节
    scores  dw   8  dup(0)      ; 学生成绩，8 个字（16 位）
    average dw   0             ; 学生平均分
student   ends

; 数据段
.data
   lpfmt  db "%s %s %d %d",0dh,0ah,0  ; 格式字符串，用于输出学生信息
   lpfmt_string  db "%s  ",0          ; 格式字符串，用于输出字符串
   lpfmt_num  db "%d  ",0             ; 格式字符串，用于输出数字

; 代码段
.code

; 计算学生平均分的函数（版本 2）
computeAverageScore2 proc
    push ebp                     ; 保存基指针
    mov ebp, esp                 ; 设置新的基指针
    push eax                     ; 保存寄存器
    push esi
    push edi
    push ebx

    mov esi, [ebp+8]             ; 获取学生结构体数组的地址
    mov ecx, [ebp+12]            ; 获取学生数量
    test ecx, ecx                ; 检查学生数量是否为 0
    jz done                      ; 如果为 0，跳转到 done

student_loop:
    mov eax, 0                   ; 清零累加器
    lea edi, [esi+19]            ; 计算学生成绩的起始地址（sname 8 字节 + sid 11 字节 = 19 字节）

    mov ebx, 8                   ; 设置循环计数器为 8（8 个成绩）
score_loop:
    movsx edx, word ptr [edi]    ; 将 16 位成绩扩展为 32 位并加载到 edx
    add eax, edx                 ; 累加成绩
    add edi, 2                   ; 移动到下一个成绩
    dec ebx                      ; 减少循环计数器
    jnz score_loop               ; 如果计数器不为 0，继续循环

    cdq                          ; 将 eax 扩展到 edx:eax
    mov ebx, 8                   ; 设置除数为 8
    idiv ebx                     ; 用 edx:eax 除以 8，结果在 eax
    mov [esi+35], ax             ; 将平均分存储到学生结构体中（sname 8 + sid 11 + scores 16 = 35 字节）
    add esi, 37                  ; 移动到下一个学生（每个学生占用 37 字节）
    dec ecx                      ; 减少学生计数器
    jnz student_loop             ; 如果还有学生，继续循环

done:
    pop ebx                      ; 恢复寄存器
    pop edi
    pop esi
    pop eax
    pop ebp
    ret                          ; 返回
computeAverageScore2 endp

; 计算学生平均分的函数（版本 3）
computeAverageScore3 proc
    push ebp                     ; 保存基指针
    mov ebp, esp                 ; 设置新的基指针
    push eax                     ; 保存寄存器
    push ecx
    push edx
    push esi
    push edi
    push ebx

    mov esi, [ebp+8]             ; 获取学生结构体数组的地址
    mov ecx, [ebp+12]            ; 获取学生数量
    test ecx, ecx                ; 检查学生数量是否为 0
    jz done                      ; 如果为 0，跳转到 done

student_loop:
    lea  edi, [esi + 19]         ; 计算学生成绩的起始地址

    ; 手动加载并累加 8 个成绩
    movsx eax, word ptr [edi]    ; 加载第一个成绩
    movsx ebx, word ptr [edi+2]  ; 加载第二个成绩
    add eax, ebx                 ; 累加
    movsx edx, word ptr [edi+4]  ; 加载第三个成绩
    add eax, edx                 ; 累加
    movsx ebx, word ptr [edi+6]  ; 加载第四个成绩
    add eax, ebx                 ; 累加
    movsx edx, word ptr [edi+8]  ; 加载第五个成绩
    add eax, edx                 ; 累加
    movsx ebx, word ptr [edi+10] ; 加载第六个成绩
    add eax, ebx                 ; 累加
    movsx edx, word ptr [edi+12] ; 加载第七个成绩
    add eax, edx                 ; 累加
    movsx ebx, word ptr [edi+14] ; 加载第八个成绩
    add eax, ebx                 ; 累加

    shr eax, 3                   ; 将总分右移 3 位（相当于除以 8）
    mov [esi + 35], ax           ; 将平均分存储到学生结构体中
    add esi, 37                  ; 移动到下一个学生
    dec ecx                      ; 减少学生计数器
    jnz student_loop             ; 如果还有学生，继续循环

done:
    pop ebx                      ; 恢复寄存器
    pop edi
    pop esi
    pop edx
    pop ecx
    pop eax
    pop ebp
    ret                          ; 返回
computeAverageScore3 endp

end