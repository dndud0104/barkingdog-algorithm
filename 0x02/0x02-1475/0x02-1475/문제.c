#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int num_set[10];

void countSet(int x) {
	if (x == 6 || x == 9) {
		if (num_set[6] == num_set[9]) num_set[6]++;
		else num_set[9]++;
	}
	else {
		num_set[x]++;
	}
}

int maxSet() {
	int max = num_set[0];
	for (int i = 0; i < 10; i++) {
		if (max < num_set[i]) max = num_set[i];
	}
	return max;
}

int main() {
	char room_num[1000000];

	scanf("%s", &room_num);

	for (int i = 0; room_num[i] != '\0'; i++) {
		countSet(room_num[i] - '0');
	}
	printf("%d", maxSet());
}