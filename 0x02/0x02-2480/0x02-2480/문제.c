#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main() {
	int dice[3];
	int count[6] = { 0 };
	int tmp;
	int n = 2;
	scanf("%d %d %d", &dice[0], &dice[1], &dice[2]);
	for (int i = 0; i < 3; i++) {
		count[dice[i] - 1]++;
	}
	for (int i = 0; i < 6; i++) {
		if (count[i] == 3) {
			printf("%d", 10000 + (i + 1) * 1000);
			return 0;
		}
		else if (count[i] == 2) {
			printf("%d", 1000 + (i + 1) * 100);
			return 0;
		}
	}
	for (int i = 5; i >= 0; i--) {
		if (count[i] == 1) {
			printf("%d", (i + 1) * 100);
			return 0;
		}
	}
	return 0;
}