#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <string.h>

int main() {
	char word[100];
	int counter[26] = { 0 };
	scanf("%s", &word);

	for (int i = 0; i < strlen(word); i++) {
		counter[(int)word[i] - 97]++;
	}
	for (int i = 0; i < 26; i++) {
		printf("%d ", counter[i]);
	}
}