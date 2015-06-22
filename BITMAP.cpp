#include <algorithm>
#include <iostream>
#include <string>
#include <queue>
#include <string>

using namespace std;

int bitmap[182][182];
int n,m;

void BFS(int p,int q)
{
	queue<int> frontier;
	bitmap[p][q] = 0;

	frontier.push(p);
	frontier.push(q);

	while (!frontier.empty()) {

		queue<int> next;
		int l = frontier.size();

		for (int i = 0; i < l; i += 2)
		{
			p = frontier.front();
			frontier.pop();
			q = frontier.front();
			frontier.pop();
			int dist = bitmap[p][q] + 1;

			if (p >= 1)
				if (dist < bitmap[p-1][q])
				{
					next.push(p-1);
					next.push(q);
					bitmap[p-1][q] = dist;
				}
			if (p <= n-2)
				if (dist < bitmap[p+1][q])
				{
					next.push(p+1);
					next.push(q);
					bitmap[p+1][q] = dist;
				}
			if (q >= 1)
				if (dist < bitmap[p][q-1])
				{
					next.push(p);
					next.push(q-1);
					bitmap[p][q-1] = dist;
				}
			if (q <= m-2)
				if (dist < bitmap[p][q+1])
				{
					next.push(p);
					next.push(q+1);
					bitmap[p][q+1] = dist;
				}
		}
		frontier = next;
	}
}

int main()
{
	int test;
	cin>>test;
	while (test--){
		
		queue<int> positions;
		int l = 0;
		string temp;
		cin>>n>>m;
		for (int i = 0; i < n; ++i)
		{
			cin>>temp;
			for (int j = 0; j < m; ++j)
			{
				if (temp[j]=='1')
				{
					bitmap[i][j] = 0;
					positions.push(i);
					positions.push(j);
					l++;
				}
				else
					bitmap[i][j] = 10000;
			}
		}

		for (int i = 0; i < l; ++i)
		{
			int p = positions.front();
			positions.pop();
			int q = positions.front();
			positions.pop();
			BFS(p,q);
		}

		for (int i = 0; i < n; ++i)
		{
			for (int j = 0; j < m; ++j)
				cout<<bitmap[i][j]<<" ";
			cout<<endl;
		}

	}	
	return 0;
}
