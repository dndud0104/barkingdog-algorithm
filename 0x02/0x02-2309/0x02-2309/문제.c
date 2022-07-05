#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main() {
	int nanjeng[9];
	int result[7];
	int x;
	int tmp;
	int sum;
	for (int i = 0; i < 9; i++) {
		scanf("%d", &nanjeng[i]);
	}

	for (int i = 0; i < 8; i++) {
		for (int j = i+1; j < 9; j++) {
			x = 0;
			sum = 0;
			for (int k = 0; k < 9; k++) {
				if (k != i && k != j) {
					result[x++] = nanjeng[k];
					sum += nanjeng[k];
				}
			}
			if (sum == 100)
				break;
		}
		if (sum == 100)
			break;
	}

	printf("%d\n", sum);

	for (int i = 0; i < 6; i++) {
		for (int j = 0; j < 6 - i; j++) {
			if (result[j] > result[j + 1]) {
				tmp = result[j];
				result[j] = result[j + 1];
				result[j + 1] = tmp;
			}
		}
	}
	for (int i = 0; i < 7; i++) {
		printf("%d\n", result[i]);
	}
	return 0;
}