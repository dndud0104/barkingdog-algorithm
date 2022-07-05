#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main() {
	long long A, B, tmp;
	scanf("%lld %lld", &A, &B);
	if (A == B) {
		printf("%d", A - B);
		return 0;
	}
	else if (A > B) {
		tmp = A;
		A = B;
		B = tmp;
	}
	printf("%lld\n", B - A - 1);
	for (long long i = A + 1; i < B; i++) {
		printf("%lld ", i);
	}
	return 0;
}