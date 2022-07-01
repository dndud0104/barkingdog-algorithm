#include <stdio.h>

int main() {
	int result;
	//result = func3(9);
	result = func3(693953651);
	//result = func3(756580036);
	printf("%d", result);
	return 0;
}

int func3(int N) {
	//for (int i = 1; i < N/2; i++) {
	for (int i = 1; i*i <= N; i++) {
		if (N == i * i) {
			return 1;
		}
	}
	return 0;
}