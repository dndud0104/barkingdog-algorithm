#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <string.h>

int main() {
	int N;
	int cham;

	scanf("%d", &N);
	for (int i = 0; i < N; i++) {
		char arr1[1005];
		char arr2[1005];
		int count1[26];
		int count2[26];
		cham = 1;
		memset(arr1, NULL, 1005);
		memset(arr2, NULL, 1005);
		memset(count1, 0, 26);
		memset(count2, 0, 26);

		scanf("%s %s", &arr1, &arr2);
		for (int j = 0; arr1[j] != '\0'; j++) {
			count1[arr1[j] - 97]++;
		}
		for (int j = 0; arr2[j] != '\0'; j++) {
			count2[arr2[j] - 97]++;
		}
		for (int j = 0; j<26; j++) {
			if (count1[j] != count2[j]) {
				cham = 0;
				break;
			}
		}
		if (cham == 1) {
			printf("Possible\n");
		}
		else {
			printf("Impossible\n");
		}
	}
}