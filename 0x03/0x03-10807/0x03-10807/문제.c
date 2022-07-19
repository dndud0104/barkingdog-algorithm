#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int arr[100];

int countNum(int v, int s) {
	int count = 0;
	for (int i=0; i < s; i++) {
		if (arr[i] == v) count++;
	}
	return count;
}

int main() {
	int N, v, num;

	scanf("%d", &N);
	for (int i = 0; i < N; i++) {
		scanf("%d", &num);
		arr[i] = num;
	}
	scanf("%d", &v);
	printf("%d", countNum(v, N));
}