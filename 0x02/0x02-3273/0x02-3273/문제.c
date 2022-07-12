#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int arr[100001];
int exist[2000001];

//2중 for문, 시간초과
/*int countPair(int x, int s) {
	int count=0;
	for (int i = 0; i < s - 1; i++) {
		for (int j = i + 1; j < s; j++) {
			if (arr[i] + arr[j] == x) count++;
		}
	}
	return count;
}*/

//정렬후 앞뒤합, 시간초과
/*int countPair(int x, int s) {
	int count = 0;
	int tmp;
	int start = 0;
	int end = s-1;
	
	for (int i = 0; i < s; i++) {
		for (int j = 0; j < s - 1; j++) {
			if (arr[j] > arr[j+1]) {
				tmp = arr[j];
				arr[j] = arr[j+1];
				arr[j+1] = tmp;
			}
		}
	}

	for (int i = 0; start != end; i++) {
		if (arr[start] + arr[end] == x) {
			count++;
			end--;
		}
		else if (arr[start] + arr[end] > x) {
			end--;
		}
		else {
			start++;
		}
	}

	return count;
}*/

//도저히 모르겠어서 정답 봄
int countPair(int x, int s) {
	int count = 0;
	for (int i = 0; i < s; i++) {
		if (x - arr[i] > 0 && exist[x - arr[i]]) count++;
		exist[arr[i]]=1;
	}
	return count;
}

int main() {
	int size, num, x;

	scanf("%d", &size);
	for (int i = 0; i < size; i++) {
		scanf("%d", &num);
		arr[i] = num;
	}
	scanf("%d", &x);
	printf("%d", countPair(x, size));
}