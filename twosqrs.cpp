#include <cstdio>
#include <cmath>

using namespace std;
                             
int main()
{
    int test,primes[78498] = {0};
    double SQRT;
    bool is_composite[1000000] = {0};
    unsigned long long num;

    for (int i = 2; i <= 1000; ++i)
        if (!is_composite[i])
            for (unsigned long long j = i*i; j < 1000000; j += i)
                is_composite[j] = 1;

    int j = 0;
    for (int i = 2; i < 1000000; ++i)
        if (!is_composite[i])
        {
            primes[j] = i;
            j += 1;
        }

    scanf("%d",&test);

    while (test--)
    {
        scanf("%lld",&num);
        SQRT = sqrt(num);

        if (SQRT == (int)SQRT)
        {
            printf("Yes\n");
            continue;
        }

        int count = 0,not_found = 1;

        for (int i = 0; i < j; ++i)
        {
            count = 0;
            while (num%primes[i] == 0)
            {
                if (primes[i]%4 == 3)
                    count++;
                num/= primes[i];
            }
            if (count%2 == 1)
            {
                printf("No\n");
                not_found = 0;
                break;
            }
        }

        if (not_found && num%4 != 3)
            printf("Yes\n");
        else if(not_found)
            printf("No\n");
    }
    return 0;
}
