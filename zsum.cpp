#include<stdio.h>

using namespace std;

#define MOD 10000007

long long modexpo(long long a,long long b,int n)
{
  long long d=1;
  while(b)
  { if(b%2)
      d=(d*a)%n;
    b>>=1;
    a=(a*a)%n;
  }
 return d;
}
 
int main()
{
  long long n,k;
  scanf("%lld%lld",&n,&k);
  while(n)
  {
    long long a,b,c,d,ans;
    b=modexpo(n,k,MOD);
    a=(2*modexpo(n-1,k,MOD))%MOD;
    d=modexpo(n,n,MOD);
    c=(2*modexpo(n-1,n-1,MOD))%MOD;
    ans=((a+b)%MOD+(c+d)%MOD)%MOD;
    printf("%lld\n",ans);
    scanf("%lld%lld",&n,&k);
  }
 return 0;
 }
