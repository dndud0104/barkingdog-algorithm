#include <stdio.h>

void insert(int idx, int num, int arr[], int *len) {
	for (int i = *len; i > idx; i--)
		arr[i] = arr[i - 1];
	arr[idx] = num;
	*len += 1;
}

void erase(int idx, int arr[], int *len) {
	*len -= 1;
	for (int i = idx; i < *len; i++)
		arr[i] = arr[i + 1];
}

void printArr(int arr[], int *len) {
	for (int i = 0; i < *len; i++)
		printf("%d ", arr[i]);
	printf("\n\n");
}

void insert_test() {
	printf("***** insert_test *****\n");
	int arr[10] = { 10, 20, 30 };
	int len = 3;
	int *plen;
	plen = &len;
	insert(3, 40, arr, plen); // 10 20 30 40
	printArr(arr, plen);
	insert(1, 50, arr, plen); // 10 50 20 30 40
	printArr(arr, plen);
	insert(0, 15, arr, plen); // 15 10 50 20 30 40
	printArr(arr, plen);
}

void erase_test() {
	printf("***** erase_test *****\n");
	int arr[10] = { 10, 50, 40, 30, 70, 20 };
	int len = 6;
	int *plen;
	plen = &len;
	erase(4, arr, plen); // 10 50 40 30 20
	printArr(arr, plen);
	erase(1, arr, plen); // 10 40 30 20
	printArr(arr, plen);
	erase(3, arr, plen); // 10 40 30
	printArr(arr, plen);
}

int main(void) {
	insert_test();
	erase_test();
}