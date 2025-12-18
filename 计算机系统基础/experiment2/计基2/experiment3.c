#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <windows.h>

#define STUDENTS_NUM 5
#define COURSES 8

#pragma pack(1)
typedef struct temp {
	char  name[8];
	char  sid[11];    //  如U202315123
	short  scores[8]; //  8门课的分数
	short  average;   //  平均分
}student;

void display(student students[], int n, const char* title) {
	printf("\n%s:\n", title);
	printf("%-8s %-9s", "姓名", "学号");
	for (int i = 0; i < COURSES; i++) {
		printf("  %5s%d", "课程", i + 1);
	}
	printf("  平均分\n");
	printf("---------------------------------------------------------------------------------------------\n");
	for (int i = 0; i < n; i++) {
		printf("%-8s %-11s", students[i].name, students[i].sid);
		for (int j = 0; j < COURSES; j++) {
			printf("  %-6d", students[i].scores[j]);
		}
		printf("  %d\n", students[i].average);
	}
}

void initStudents(student* students, int num)
{
	srand(time(0));

	// 随机生成其他学生的姓名、学号和成绩
	char names[][8] = { "JiaNZ", "LiSi", "WangWu", "ZhaoLiu", "QianQi" }; // 示例姓名
	char sids[][11] = { "U202315594", "U202315111", "U202315112", "U202315113", "U202315114" }; // 示例学号
	for (int i = 0; i < STUDENTS_NUM; i++) {
		strcpy_s(students[i].name, 8, names[i]);
		strcpy_s(students[i].sid, 11, sids[i]);
		for (int j = 0; j < 8; j++) {
			students[i].scores[j] = rand() % 101; // 生成0-100的随机数
		}
	}
}

void computeAverageScore(student* s, int num)
{
	for (int i = 0; i < num; i++)
	{
		int sum = 0;
		for (int j = 0; j < 8; j++)
		{
			sum += s[i].scores[j];
		}
		s[i].average = sum / 8;
	}
}

void sort(student* s, int num)
{
	for (int i = 0; i < num; i++)
	{
		for (int j = i + 1; j < num; j++)
		{
			if (s[i].average < s[j].average)
			{
				student temp = s[i];
				s[i] = s[j];
				s[j] = temp;
			}
		}
	}
}

void QuickSort(student* s, int left, int right)
{
	if (left >= right)
	{
		return;
	}
	int i = left;
	int j = right;
	student temp = s[left];
	while (i < j)
	{
		while (i < j && s[j].average <= temp.average)
		{
			j--;
		}
		s[i] = s[j];
		while (i < j && s[i].average >= temp.average)
		{
			i++;
		}
		s[j] = s[i];
	}
	s[i] = temp;
	QuickSort(s, left, i - 1);
	QuickSort(s, i + 1, right);
}

int main() {
	student s[STUDENTS_NUM];
	LARGE_INTEGER start, finish, freq;
	double duration;

	initStudents(s, STUDENTS_NUM); // 初始化学生信息

	// 获取高性能计数器的频率
	QueryPerformanceFrequency(&freq);

	// 计算平均分的时间测量
	QueryPerformanceCounter(&start);
	computeAverageScore(s, STUDENTS_NUM);
	QueryPerformanceCounter(&finish);
	duration = (double)(finish.QuadPart - start.QuadPart) * 1000.0 / freq.QuadPart;
	printf("计算平均成绩用时： %f 毫秒\n", duration);

	QueryPerformanceCounter(&start);
	computeAverageScore2(s, STUDENTS_NUM);
	QueryPerformanceCounter(&finish);
	duration = (double)(finish.QuadPart - start.QuadPart) * 1000.0 / freq.QuadPart;
	printf("计算平均成绩用时（优化前）： %f 毫秒\n", duration);

	QueryPerformanceCounter(&start);
	computeAverageScore3(s, STUDENTS_NUM);
	QueryPerformanceCounter(&finish);
	duration = (double)(finish.QuadPart - start.QuadPart) * 1000.0 / freq.QuadPart;
	printf("计算平均成绩用时（优化后）： %f 毫秒\n", duration);

	display(s, STUDENTS_NUM, "排序前的学生信息");

	////排序的时间测量
	//QueryPerformanceCounter(&start);
	//sort(s, STUDENTS_NUM);
	//QueryPerformanceCounter(&finish);
	//duration = (double)(finish.QuadPart - start.QuadPart) * 1000.0 / freq.QuadPart;
	//printf("排序用时（优化前）： %f 毫秒\n", duration);

	QueryPerformanceCounter(&start);
	QuickSort(s, 0, STUDENTS_NUM - 1);
	QueryPerformanceCounter(&finish);
	duration = (double)(finish.QuadPart - start.QuadPart) * 1000.0 / freq.QuadPart;
	printf("排序用时（优化后）： %f 毫秒\n", duration);

	display(s, STUDENTS_NUM, "排序后的学生信息");

	return 0;
}