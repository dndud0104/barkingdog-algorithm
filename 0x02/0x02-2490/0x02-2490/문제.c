#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main() {
	int a;
	int sum;
	for (int i = 0; i < 3; i++) {
		sum = 0;
		for (int j = 0; j < 4; j++) {
			scanf("%d", &a);
			sum += a;
		}
		switch (sum)
		{
		case 0:
			printf("D");
			break;
		case 1:
			printf("C");
			break;
		case 2:
			printf("B");
			break;
		case 3:
			printf("A");
			break;
		case 4:
			printf("E");
			break;
		}
		printf("\n");
	}
}