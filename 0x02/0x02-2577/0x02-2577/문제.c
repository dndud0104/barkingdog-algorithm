#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main() {
	int num1, num2, num3;
	int Array[10] = { 0 };
	int result;
	int tmp;
	scanf("%d", &num1);
	scanf("%d", &num2);
	scanf("%d", &num3);
	result = num1 * num2*num3;
	while (result > 0) {
		tmp = result % 10;
		Array[tmp]++;
		result /= 10;
	}
	for (int i = 0; i < 10; i++) {
		printf("%d\n", Array[i]);
	}
	return 0;
}