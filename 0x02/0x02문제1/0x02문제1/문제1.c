//백준 10871
//X보다 작은 수
#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

void test1();
void test2();


int main() {
	test1();
	printf("\n");
	test2();

	return 0;
}

//배열O
void test1() {
	int N, X, a[10000];
	scanf("%d %d", &N, &X);

	for (int i = 0; i < N; i++)
		scanf("%d", &a[i]);
	for (int i = 0; i < N; i++)
		if (a[i] < X)
			printf("%d ", a[i]);
}
//배열X
void test2() {
	int N, X, a;
	scanf("%d %d", &N, &X);

	for (int i = 0; i < N; i++) {
		scanf("%d", &a);
		if (a < X)
			printf("%d ", a);
	}
}