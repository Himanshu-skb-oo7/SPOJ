#include<algorithm>
#include<cstdio>

using namespace std;

int main()
{
	unsigned long long int size;
	scanf("%llu",&size);
	do
	{	
	  unsigned long long int arr1[size],arr2[size],cost = 0;
			
		for(int i = 0;i<size;i++)
			scanf("%llu",&arr1[i]);
		
		for(int i = 0;i<size;i++)
			scanf("%llu",&arr2[i]);
		
		sort(arr1,arr1 + size);
		sort(arr2,arr2 + size);
		
		for(int i = 0;i<size;i++)
			cost += (arr1[i]*arr2[size-i-1]);
		
		printf("%llu\n",cost);
		scanf("%llu",&size);
		
	}while(size != 0);
	
	return 0;
}
