#include <stdio.h>

int main()
{
    long long int n;
    while (1)
    {
        scanf("%lld",&n);
        if(n==0)
            break;
        printf("%lld\n",((n+1)*(3*n+2))/2);
    }
    return 0;
}
