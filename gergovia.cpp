#include<algorithm>
#include<cstdio>

using namespace std;

int main()
{
	long long int t;
	
	while(1)
	{
		scanf("%lld",&t);
		if(t == 0)
			break;
		long long int x,b=0,w=0;
		for(int i=0;i<t;i++)
		{
			scanf("%lld",&x);
			x += b;	
			w += (x<0 ? -x:x);
			b = x;
		}
		printf("%lli\n",w);
	}
	return 0;
}
