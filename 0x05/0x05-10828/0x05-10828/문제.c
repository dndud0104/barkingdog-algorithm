#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <string.h>

int dat[10005];
int pos = 0;

void push(int x) {
	dat[pos] = x;
	pos++;
}
int top() {
	if (pos == 0) return -1;
	else return dat[pos - 1];
}
int empty() {
	if (pos == 0) return 1;
	else return 0;
}
int pop() {
	if (pos == 0) return -1;
	else {
		return dat[--pos];
	}
	
}
int main() {
	int count;
	char opcode[10];
	int x;

	scanf("%d", &count);
	for (int i = 0; i < count; i++) {
		scanf("%s", &opcode);
		if (strcmp(opcode, "push") == 0) {
			scanf("%d", &x);
			push(x);
		}
		else if (strcmp(opcode, "top") == 0) {
			printf("%d\n", top());
		}
		else if (strcmp(opcode, "size") == 0) {
			printf("%d\n", pos);
		}
		else if (strcmp(opcode, "empty") == 0){
			printf("%d\n", empty());
		}
		else {
			printf("%d\n", pop());
		}
	}
}