#include<iostream>
#include<algorithm>

using namespace std;

int main()
{
	int h,count=0;
	while(1)
	{
		cin>>h;
		if(h==0)	break;
		count++;	
		int stones[h][3];
		for(int i=0;i<h;i++)
			for(int j=0;j<3;j++)
			{
				cin>>stones[i][j];
				if (h==1)
					continue;
				else if(i==0 && (j==0 || j==1))
					continue;
				else if(i == 0 && j == 2)
					stones[0][2] = min(stones[0][1],stones[0][2]+stones[0][1]);
				else if(i == 1 && j == 0)
					stones[1][0] += stones[0][1];
				else if(i == 1 && j == 1)
					stones[1][1] += min(min(stones[0][1],stones[0][2]),stones[1][0]);
				else if(i != h-1 && j == 0)
					stones[i][0] += min(stones[i-1][0],stones[i-1][1]);
				else if(i != h-1 && j == 1)
					stones[i][1] += min(min(stones[i-1][0],stones[i-1][1]),min(stones[i-1][2],stones[i][0]));
				else if(i != h-1 && j == 2)
					stones[i][j] += min(min(stones[i-1][1],stones[i-1][2]),stones[i][1]);
				else if(i == h-1 && j == 0)
					stones[i][j] += min(stones[h-2][0],stones[h-2][1]);
			}
		
		if(h > 2)
			stones[h-1][1] += min(min(stones[h-2][1],stones[h-2][2]),min(stones[h-1][0],stones[h-2][0]));
		if(h==1)
			cout<<count<<". "<<stones[0][1]<<endl;
		else
			cout<<count<<". "<<stones[h-1][1]<<endl;
		
		/*for(int i=0;i<h;i++)
		{	for(int j=0;j<3;j++)
				cout<<stones[i][j]<<" ";
			cout<<endl;
		}*/
	}
	return 0;
}
