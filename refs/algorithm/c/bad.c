int Bad(unsigned int N)
{
	if (N == 0)
		return 0;
	else
		return Bad(N / 3 + 1) + N - 1;
}
