#include <cstdio>
#include <cmath>
#include <cstring>

using namespace std;

char str1[2013], str2[2013];
int DP[2013][2013], k;

int blast(char str1[],char str2[],int k)
{
    int len1, len2;

    len1 = strlen(str1);
    len2 = strlen(str2);
    
    for (int i = 0; i <= len1; ++i)
        DP[i][0] = k*i;

    for (int j = 0; j <= len2; ++j)
        DP[0][j] = k*j;
        
    for (int i = 1; i <= len1; ++i)
        for (int j = 1; j <= len2; ++j)
            DP[i][j] = min(DP[i-1][j-1]+(int)abs(str1[i - 1] - str2[j - 1]), min(DP[i-1][j], DP[i][j-1])+k);
    
    return DP[len1][len2];
}

int main()
{
    scanf("%s%s%d", str1, str2, &k);    
    printf("%d\n", blast(str1,str2,k));

    return 0;
}
