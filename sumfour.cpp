#include <cstdio>
#include <cmath>
#include <algorithm>
#include <cstring>

using namespace std;

int arr1[10000013],arr2[10000013],MAX;
                                 
int binary_search(int key)
{
    int mid,temp,count = 0,first = 0,last = MAX-1;

    while (first <= last)
    {
        mid = (first+last)/2;
        
        if (arr2[mid] == key)
        {   
            count += 1;

            temp = mid-1;
            if (temp >= 0)
                while (arr2[temp] == key)
                {
                    count += 1;
                    if (temp == 0)
                        break;
                    temp -= 1;
                }
            
            temp = mid+1;
            if (temp < MAX)
                while (arr2[temp] == key)
                {
                    count += 1;
                    if (temp == MAX-1)
                        break;
                    temp += 1;
                }
            
            return count;
        }
        else if(arr2[mid] < key)
            first = mid+1;
        else
            last = mid-1;
    }
    return 0;        
}

int main()
{  
    int test,count,i,j;

    scanf("%d",&test);
    MAX = test*test;
    
    int a[test],b[test],c[test],d[test];

    for (i = 0; i < test; ++i)
        scanf("%d%d%d%d",&a[i],&b[i],&c[i],&d[i]);

    count = 0;
    for (i = 0; i < test; ++i)
        for (j = 0; j < test; ++j)
        {
            arr1[count] = a[i]+b[j];
            arr2[count] = -1*(c[i]+d[j]);
            count += 1;
        }
    sort(arr1,arr1+count);
    sort(arr2,arr2+count);
    
    i = count = 0;
    int key,final_count = 0,recurrence = 0;

    while(i<MAX)
    {
        key = arr1[i];
        recurrence = 0;
        while(i<MAX && arr1[i] == key)
        {
            recurrence += 1;
            i += 1;
            if (i == MAX)
                break;
        }
        count = binary_search(key);

        final_count += count*recurrence;
    }
    
    printf("%d\n",final_count);
    return 0;
}
