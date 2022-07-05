#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

void swapCard(int card[], int s, int e);

int main() {
	int Card[20];
	int start, end;

	for (int i = 0; i < 20; i++) {
		Card[i] = i + 1;
	}
	for (int i = 0; i < 10; i++) {
		scanf("%d %d", &start, &end);
		swapCard(Card, start-1, end-1);
	}
	for (int i = 0; i < 20; i++) {
		printf("%d ", Card[i]);
	}
}

void swapCard(int card[], int s, int e) {
	int tmp;
	for (int i = s; i <= e; i++,e--) {
		tmp = card[i];
		card[i] = card[e];
		card[e] = tmp;
	}
	/*for (int i = 0; i < 20; i++) {
		printf("%d ", card[i]);
	}
	printf("\n");*/
}