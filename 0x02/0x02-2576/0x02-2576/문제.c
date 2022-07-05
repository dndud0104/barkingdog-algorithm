#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main() {
	int mean = 100;
	int a;
	int sum = 0;
	int count = 0;

	for (int i = 0; i < 7; i++) {
		scanf("%d", &a);
		if (a % 2 != 0) {
			sum += a;
			count++;
			if (mean > a) {
				mean = a;
			}
		}
	}
	if (count != 0) {
		printf("%d\n%d", sum, mean);
	}
	else {
		printf("-1");
	}
		
}