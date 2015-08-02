#include<iostream>
#include<algorithm>

using namespace std;

int main()
{
        int h,w,m;
        
        cin>>h>>w;
        int dp[h][w];
        for(int i=0;i<h;i++)
                for(int j=0;j<w;j++)
                {
                        cin>>dp[i][j];
                        if (i != 0)
                        {
                                if(w > 2)
                                {
                                        if(j == 0)
                                                dp[i][0] += min(dp[i-1][1],dp[i-1][0]);
                                        else if(j == w-1)
                                                dp[i][j] += min(dp[i-1][j],dp[i-1][j-1]);
                                        else
                                                dp[i][j] += min(min(dp[i-1][j+1],dp[i-1][j]),dp[i-1][j-1]);
                                }
                                else if(w == 2)
                                {
                                        if(j == 0)
                                                dp[i][0] += min(dp[i-1][0],dp[i-1][1]);
                                        else if(j == 1)
                                                dp[i][1] += min(dp[i-1][0],dp[i-1][1]);
                                }
                                else if(w == 1)
                                {
                                        dp[i][0] += dp[i-1][0];
                                }
                        }
                }
        
        m = dp[h-1][0];
        for(int i=0;i<w;i++)
                if(dp[h-1][i]<m)
                        m = dp[h-1][i];
        cout<<m<<endl;
        
        return 0;
}
