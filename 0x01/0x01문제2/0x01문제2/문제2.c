#include <stdio.h>

int main() {
	int result;
	//int arr[3] = { 1,52,48 };
	//result = func2(arr, 3);
	//int arr[2] = { 50,42 };
	//result = func2(arr, 2);
	int arr[4] = { 4,13,63,87 };
	result = func2(arr, 4);
	printf("%d", result);
	return 0;
}

int func2(int arr[], int N) {
	for (int i = 0; i < N - 1; i++) {
		for (int j = i + 1; j < N; j++) {
			if (arr[i] + arr[j] == 100) {
				return 1;
			}
		}
	}
	return 0;
}