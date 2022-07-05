#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int calcMoneyY(int c, int c_t[]);
int calcMoneyM(int c, int c_t[]);

int main() {
	int count;
	int calltime[20];
	int Y, M;

	scanf("%d", &count);
	for (int i = 0; i < count; i++) {
		scanf("%d", &calltime[i]);
	}
	Y = calcMoneyY(count, calltime);
	M = calcMoneyM(count, calltime);

	if (Y < M) {
		printf("Y %d", Y);
	}
	else if (M < Y) {
		printf("M %d", M);
	}
	else {
		printf("Y M %d", Y);
	}
}

int calcMoneyY(int c, int c_t[])
{
	int result = 0;
	for (int i = 0; i < c; i++) {
		result += (c_t[i] / 30 + 1) * 10;
		printf("%d\n", result);
	}
	return result;
}
int calcMoneyM(int c, int c_t[])
{
	int result = 0;
	for (int i = 0; i < c; i++) {
		result += (c_t[i] / 60 + 1) * 15;
	}
	return result;
}