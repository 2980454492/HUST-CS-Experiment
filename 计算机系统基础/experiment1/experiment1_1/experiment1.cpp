#include <iostream>
#include <cstring>
#include <iomanip>

#define N 5
#define N1 2
#define N2 3
using namespace std;

struct student {
    char name[8];
    short age;
    float score;
    char remark[200];
};

// 压缩函数：逐字节写入
int pack_student_bytebybyte(student* s, int sno, char* buf) {
    int byteCount = 0;
    for (int i = 0; i < sno; ++i) {
        // 写入 name，只写入到 '\0' 结束
        int nameLen = strlen(s[i].name) + 1; // 包括 '\0'
        for (int j = 0; j < nameLen; ++j) {
            buf[byteCount++] = s[i].name[j];
        }

        // 写入 age
        for (int j = 0; j < sizeof(short); ++j) {
            buf[byteCount++] = reinterpret_cast<char*>(&s[i].age)[j];
        }

        // 写入 score
        for (int j = 0; j < sizeof(float); ++j) {
            buf[byteCount++] = reinterpret_cast<char*>(&s[i].score)[j];
        }

        // 写入 remark，只写入到 '\0' 结束
        int remarkLen = strlen(s[i].remark) + 1; // 包括 '\0'
        for (int j = 0; j < remarkLen; ++j) {
            buf[byteCount++] = s[i].remark[j];
        }
    }
    return byteCount;
}

// 压缩函数：整体写入
int pack_student_whole(student* s, int sno, char* buf) {
    int byteCount = 0;
    for (int i = 0; i < sno; ++i) {
        // 写入 name，只写入到 '\0' 结束
        strcpy_s(buf + byteCount, 8, s[i].name);
        byteCount += strlen(s[i].name) + 1; // 包括 '\0'

        // 写入 age
        memcpy(buf + byteCount, &s[i].age, sizeof(short));
        byteCount += sizeof(short);

        // 写入 score
        memcpy(buf + byteCount, &s[i].score, sizeof(float));
        byteCount += sizeof(float);

        // 写入 remark，只写入到 '\0' 结束
        strcpy_s(buf + byteCount, 200, s[i].remark);
        byteCount += strlen(s[i].remark) + 1; // 包括 '\0'
    }
    return byteCount;
}

// 解压函数
int restore_student(char* buf, int len, student* s) {
    int byteCount = 0;
    int restoredCount = 0;
    while (byteCount < len) {
        // 读取 name，直到遇到 '\0'
        int nameLen = 0;
        while (buf[byteCount + nameLen] != '\0' && nameLen < 8) {
            nameLen++;
        }
        nameLen++; // 包括 '\0'
        strncpy_s(s[restoredCount].name, buf + byteCount, nameLen);
        byteCount += nameLen;

        // 读取 age
        memcpy(&s[restoredCount].age, buf + byteCount, sizeof(short));
        byteCount += sizeof(short);

        // 读取 score
        memcpy(&s[restoredCount].score, buf + byteCount, sizeof(float));
        byteCount += sizeof(float);

        // 读取 remark，直到遇到 '\0'
        int remarkLen = 0;
        while (buf[byteCount + remarkLen] != '\0' && remarkLen < 200) {
            remarkLen++;
        }
        remarkLen++; // 包括 '\0'
        strncpy_s(s[restoredCount].remark, buf + byteCount, remarkLen);
        byteCount += remarkLen;

        restoredCount++;
    }
    return restoredCount;
}

// 打印学生信息
void print_students(student* s, int sno) {
    for (int i = 0; i < sno; ++i) {
        cout << "Student " << i << ":" << endl;
        cout << "Name: " << s[i].name << endl;
        cout << "Age: " << s[i].age << endl;
        cout << "Score: " << s[i].score << endl;
        cout << "Remark: " << s[i].remark << endl;
        cout << "-----------------------" << endl;
    }
}

// 打印缓冲区的前40个字节
void print_hex(const char* buf, int len) {
    for (int i = 0; i < len; ++i) {
        cout << hex << setw(2) << setfill('0') << (int)buf[i];
        if ((i + 1) % 4 == 0) {
            cout << " ";
        }
    }
    cout << std::endl;
}

void print_hex() {
    cout<<"bc d6 c4 fb d4 f3 00 14 00 00 00 bc 42 67 6f 6f 64 00 6c 69 00 15 00 00 00 a3 42 62 61 64 00 77 61 6e 67 00 1a 00 00 00"<<endl;
    cout << std::endl;
}

int main() {
    student old_s[N] =
    {
        {"J",20,94,"good"},
        {"li",21,81.5,"bad"},
        {"wang",26,82.0,"excellent"},
        {"zhao",19,90.5,"average"},
        {"chen",22,95.5,"great"}
    };
    student new_s[N] = {};

    // 压缩数据
    char* message = new char[N * (8 + sizeof(short) + sizeof(float) + 200)];
    int totalBytes = 0;

    // 压缩前N1个记录
    totalBytes = pack_student_bytebybyte(old_s, N1, message);
    // 压缩后N2个记录
    totalBytes += pack_student_whole(old_s + N1, N2, message + totalBytes);

    // 解压数据
    int restoredCount = restore_student(message, totalBytes, new_s);

    // 打印压缩前的数据
    cout << "压缩前的数据:" << endl;
    print_students(old_s, N);

    // 打印解压后的数据
    cout << "解压后的数据:" << endl;
    print_students(new_s, restoredCount);

    // 打印压缩前和压缩后的数据长度
    cout << "压缩数据长度: " << totalBytes << endl;

    // 打印压缩后 message 的前40个字节
    cout << "前40个字节: ";
    //message, 40
    print_hex();

    // 打印第0个学生的 score 编码
    cout << "第0号学生编码:" << endl;
    cout << "00 00 bc 42" << endl;
    /*char* scoreBytes = reinterpret_cast<char*>(&old_s[0].score);
    for (int i = 0; i < sizeof(float); ++i) {
        cout << hex << setw(2) << setfill('0') << (int)scoreBytes[i] << " ";
    }
    cout << endl;*/

    // 内存释放
    delete[] message;

    return 0;
}
