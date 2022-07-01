#include <stdio.h>

int main() {
	int result;
	//result = func4(5);
	result = func4(97615282);
	//result = func4(1024);
	printf("%d", result);

	return 0;
}

int func4(int N) {
	int i;
	for (i = 1; i <= N; i *= 2) {
	}
	return i/2;
}