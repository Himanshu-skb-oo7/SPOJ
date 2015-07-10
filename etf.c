#include<stdio.h>
int phi(int n)
{ 
  int i,result = n;
  
  for(i=2;i*i <= n;i++)
  { if (!(n%i))
    { while (!(n%i))
        n /= i;
      result -= result/i;
    } 
  } 
  
  if (n > 1)
    result -= result/n;

  return result; 
}

int main()
{
    int test,num;
    scanf("%d",&test);
    while(test--)
    {
        scanf("%d",&num);
        printf("%d\n",phi(num));
    }
    return 0;
}
