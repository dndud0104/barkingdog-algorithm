#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int arr[6][2];

int countRoom(int k) {
	int count = 0;
	for (int i = 0; i < 6; i++) {
		for (int j = 0; j < 2; j++) {
			if (arr[i][j] > 0) {
				count++;
				arr[i][j] = arr[i][j] - k;
				j--;
			}
		}
	}
	return count;
}

int main() {
	int N, K;
	int grade, gender;
	
	scanf("%d %d", &N, &K);
	for (int i = 0; i < N; i++) {
		scanf("%d %d", &gender, &grade);
		arr[grade - 1][gender]++;
	}

	printf("%d\n", countRoom(K));
	/*for (int i = 0; i < 6; i++) {
		for (int j = 0; j<2; j++) {
			printf("%d ", arr[i][j]);
		}
		printf("\n");
	}*/
}