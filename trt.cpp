#include <cstdio>
#include <algorithm>

using namespace std;

int main(){
  int N,treats[2000];
  long long dp[2][2000];
  
  scanf("%d",&N);
  for(int i = 0;i<N;++i)
    scanf("%d",&treats[i]);
  
  for(int i = 0;i<N;++i)
    dp[1][i] = N*treats[i];
  
  for(int i = 2;i<=N;++i)
    for(int j = 0;j+i-1<N;++j)
      dp[i%2][j] = max((N+1-i)*treats[j]+dp[1-(i%2)][j+1],(N+1-i)*treats[j+i-1]+dp[1-(i%2)][j]);
  
  printf("%lld\n",dp[N%2][0]);
  
  return 0;
}
