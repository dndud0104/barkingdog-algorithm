#include <stdio.h>

int main() {
	int result;
	int arr1[3] = { 1,52,48 };
	int arr2[2] = { 50,42 };
	int arr3[4] = { 4,13,63,87 };

	result = func2(arr1, 3);
	printf("%d\n", result);
	
	result = func2(arr2, 2);
	printf("%d\n", result);
	
	result = func2(arr3, 4);
	printf("%d\n", result);
	return 0;
}

int func2(int arr[], int N) {
	int counter[101] = { 0 };
	for (int i = 0; i < N; i++) {
		if (counter[100 - arr[i]] == 1) {
			return 1;
		}
		counter[arr[i]] = 1;
	}

	return 0;
}