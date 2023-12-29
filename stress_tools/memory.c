#include <stdio.h>
#include <malloc.h>
#include <errno.h>

#define ONE_KB (1 * 1024)
#define ONE_MB (ONE_KB * 1024)
#define ONE_GB (ONE_MB * 1024)

int main()
{
		char *p1 = (char *) malloc (ONE_GB);
		char *p2 = (char *) malloc (ONE_GB);
		char *p3 = (char *) malloc (ONE_GB);
		char *p4 = (char *) malloc (ONE_GB);
		char *p5 = (char *) malloc (ONE_GB);
		if (!p1 || !p2 || !p3 || !p4 || !p5) {
				printf("Malloc failure (%d)\n", errno);
				return (0);
		}

		int idx = 0, offset_sz = 512;
		while (1) {
			if (idx >= ONE_GB) idx = 0;

			p1[idx] = 0x55;
			p2[idx] = 0x55;
			p3[idx] = 0x55;
			p4[idx] = 0x55;
			p5[idx] = 0x55;
			idx += offset_sz;
		}

		return (0);
}
