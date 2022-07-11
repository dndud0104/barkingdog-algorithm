#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <string.h>

const int MX = 600005;
int pre[600005], nxt[600005];
char dat[600005];
int cursor = 0;
int unused = 1;

void traverse();

void insert(int addr, int num) {
	dat[unused] = num;
	pre[unused] = addr;
	if (unused == nxt[addr]) {
		nxt[unused] = -1;
	}
	else {
		nxt[unused] = nxt[addr];
	}
	nxt[addr] = unused;
	pre[nxt[unused]] = unused;
	unused++;
}

void erase(int addr) {
	if (nxt[addr] != -1) {
		pre[nxt[addr]] = pre[addr];
	}
	nxt[pre[addr]] = nxt[addr];
}

void traverse() {
	int cur = nxt[0];
	while (cur != -1) {
		printf("%c", dat[cur]);
		cur = nxt[cur];
	}
}

int main(void) {
	char word[100000];
	int count;
	int max;
	char code;
	for (int i = 0; i < MX; i++) {
		pre[i] = -1;
		nxt[i] = -1;
	}
	scanf("%s", &word);
	cursor = strlen(word);
	max = strlen(word);
	for (int i = 0; i < strlen(word); i++) {
		dat[unused] = word[i];
		nxt[i] = i + 1;
		pre[unused] = i;
		unused++;
	}
	scanf("%d", &count);

	for (int i = 0; i < count; i++) {
		getchar();
		scanf("%c", &code);
		switch (code) {
		case 'L':
			if (cursor != 0)
				cursor = pre[cursor];
			break;
		case 'D':
			if (cursor != max)
				cursor = nxt[cursor];
			break;
		case 'B':
			if (cursor != 0) {
				erase(cursor);
				cursor = pre[cursor];
			}
			break;
		case 'P':
			getchar();
			scanf("%c", &code);
			insert(cursor, code);
			cursor = nxt[cursor];
			break;
		}
		code = "";
	}

	traverse();
}