#include <stdio.h>
#include <string.h>
#include <errno.h>

int main(int argc, char *argv[])
{
	FILE *fp;
	char msgbuf[1024] = { '\0' };

	/* Open input file: */
	if ((fp = fopen("nonexistent", "r")) == NULL) {
		int retval = errno;
		snprintf(msgbuf, sizeof(msgbuf),
			"%s: file %s, function %s, line %d; error %d, %s.\n",
			argv[0], __FILE__, __func__, __LINE__, retval,
			strerror(retval));
		fputs(msgbuf, stderr);
		return retval;
	} else {
		/* ... Use file ... */
		fclose(fp);
		fp = NULL;
	}
	return 0;
}
