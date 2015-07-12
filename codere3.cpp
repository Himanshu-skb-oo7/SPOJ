#include<stdio.h>
#include<iostream>

using namespace std;

int sequence[1000],increasing_sequence[1000],decreasing_sequence[1000];

int main()
{
  int test,n,i,j,max;
  scanf("%d", &test);
  while(test--)
  {
    
    scanf("%d", &n);
    scanf("%d", &sequence[0]);
    
    increasing_sequence[0]=1;    
    for(i=1; i<n; i++)
    {
      scanf("%d", &sequence[i]);
      max=0;
      for(j=0; j<i; j++)
        if(sequence[j]<sequence[i] && increasing_sequence[j]>max)
          max=increasing_sequence[j];
      increasing_sequence[i]=max+1;
    }
    
    decreasing_sequence[n-1]=1;
    for(i=n-2; i>=0; i--)
    {
      max=0;
      for(j=n-1; j>i; j--)
        if(sequence[j]<sequence[i] && decreasing_sequence[j]>max)
            max=decreasing_sequence[j];
      decreasing_sequence[i]=max+1;
    }
    
    max=0;
    for(i=0; i<n; i++)
      if((increasing_sequence[i]+decreasing_sequence[i])>max)
        max=increasing_sequence[i]+decreasing_sequence[i];

    printf("%d\n", max-1);
  }
  return 0;
}
