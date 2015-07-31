#include<algorithm>
#include<cstdio>

using namespace std;

int main()
{
	int t,x,size;
	bool valid;
	scanf("%d",&t);
	while(t--)
	{
		scanf("%d",&size);
		valid = true;
		int a[size/2] = {0};
		for(int i=0;i<size;i++)
		{
			scanf("%d",&x);
			if(x >= size || x < 1)
				valid = false;
			else if(x == size-1)
			{
				if (a[0]<2)	a[0]++;
				else		valid = false;
			}
			else if(x >= (size+1)/2)
			{
				int tmp = size-x-1;
				if(a[tmp]<2)	a[tmp]++;
				else		valid = false;
			}
			else
			{
				if(a[x]<2)	a[x]++;
				else		valid = false;
			}

		}
		if (valid)	printf("YES\n");
		else		printf("NO\n");
	}
	return 0;
}
