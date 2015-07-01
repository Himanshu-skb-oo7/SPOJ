#include<stdio.h>
int main()
{	int i,n,x,y;
	scanf("%d",&n);
	for(i=0;i<n;i++)
	{	scanf("%d %d",&x,&y);
		printf("%d\n",rev(rev(x)+rev(y)));
			
	}
	return 0;
}
int rev(int p)
{	int q=0,digit;
	do{	digit=p%10;
		q=(q*10)+digit;
		p/=10;
		}while(p>0);
	return q;
}
