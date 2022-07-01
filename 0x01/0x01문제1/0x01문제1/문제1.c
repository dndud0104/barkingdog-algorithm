#include <stdio.h>

int main() {
	int N = 16;
	//int N = 34567;
	//int N = 27639;
	int result;
	result = func1(N);
	printf("%d", result);
	return 0;
}

int func1(int N) {
	int sum = 0;
	for (int i = 1; i <= N; i++) {
		if (i % 3 == 0 || i % 5 == 0) {
			sum += i;
		}
	}
	return sum;
}