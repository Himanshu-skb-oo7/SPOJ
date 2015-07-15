#include<iostream>
#include<algorithm>

using namespace std;

int main()
{
	int test,h,w,M;
	cin>>test;

	while(test--)
	{
		cin>>h>>w;
		int stones[h][w];
		for(int i=0;i<h;i++)
			for(int j=0;j<w;j++)
			{
				cin>>stones[i][j];
				if (i != 0)
				{
					if(w > 2)
					{
						if(j == 0)
							stones[i][0] += max(stones[i-1][1],stones[i-1][0]);
						else if(j == w-1)
							stones[i][j] += max(stones[i-1][j],stones[i-1][j-1]);
						else
							stones[i][j] += max(max(stones[i-1][j+1],stones[i-1][j]),stones[i-1][j-1]);
					}
					else if(w == 2)
					{
						if(j == 0)
							stones[i][0] += max(stones[i-1][0],stones[i-1][1]);
						else if(j == 1)
							stones[i][1] += max(stones[i-1][0],stones[i-1][1]);
					}
					else if(w == 1)
					{
						stones[i][0] += stones[i-1][0];
					}
				}
			}
		M = stones[h-1][0];
		for(int i=0;i<w;i++)
			if(stones[h-1][i]>M)
				M = stones[h-1][i];
		cout<<M<<endl;
	}
	return 0;
}
