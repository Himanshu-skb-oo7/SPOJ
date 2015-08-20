#include <iostream>
#include <algorithm>
using namespace std;

#include <string.h>
#include <math.h> 

#define MAX 400000
#define inf 0x7fffffff

long long int arr[100000] = {0};
long long int tree[MAX];
long long int lazy[MAX];
/*
void build_tree(long long int node, long long int a, long long int b) {
    if(a > b) return;
    
    if(a == b) {
        tree[node] = arr[a]; 
        return;
    }
    
    build_tree(node*2, a, (a+b)/2); 
    build_tree(node*2+1, 1+(a+b)/2, b);
    
    tree[node] = tree[node*2] + tree[node*2+1]; 
}
*/
void update_tree(long long int node, long long int a, long long int b, long long int i, long long int j, long long int value) {
  
    if(lazy[node] != 0) { 
        tree[node] += lazy[node]; 

        if(a != b) {
            tree[node] += lazy[node]*(b-a);
            lazy[node*2] += lazy[node];
            lazy[node*2+1] += lazy[node]; 
        }

        lazy[node] = 0; 
    }
  
    if(a > b || a > j || b < i)
        return;
    
    if(a >= i && b <= j) { 
            tree[node] += value;

        if(a != b) { 
            tree[node] += value*(b-a);
            lazy[node*2] += value;
            lazy[node*2+1] += value;
        }

        return;
    }

    update_tree(node*2, a, (a+b)/2, i, j, value); 
    update_tree(1+node*2, 1+(a+b)/2, b, i, j, value);

    tree[node] = tree[node*2] + tree[node*2+1];
}

long long int query_tree(long long int node, long long int a, long long int b, long long int i, long long int j) {
    
    if(a > b || a > j || b < i) return 0;

    if(lazy[node] != 0) { 
        tree[node] += lazy[node]; 

        if(a != b) {
            tree[node] += lazy[node]*(b-a);
            lazy[node*2] += lazy[node]; 
            lazy[node*2+1] += lazy[node]; 
        }

        lazy[node] = 0; 
    }

    if(a >= i && b <= j) 
        return tree[node];

    long long int q1 = query_tree(node*2, a, (a+b)/2, i, j); 
    long long int q2 = query_tree(1+node*2, 1+(a+b)/2, b, i, j); 

    long long int res = q1 + q2; 
    
    return res;
}

int main() {
    int test;
    cin >> test;

    while (test--)
    {
        long long int N,n;
        cin >> N >> n;
        for(long long int i = 0; i < N; i++) arr[i] = 0;

        //build_tree(1, 0, N-1);
        memset(tree, 0, sizeof tree);
        memset(lazy, 0, sizeof lazy);

        for (long long int i = 0; i < n; ++i)
        {
            long long int query;
            cin >> query;

            if(query)
            {
                long long int a,b;
                cin >> a >> b;
                cout << query_tree(1, 0, N-1, a-1, b-1) << endl;
            }
            else
            {
                long long int a,b,c;
                cin >> a >> b >> c;
                update_tree(1, 0, N-1, a-1, b-1, c);
            }
        }
    }
    long long int arr[100000] = {0}; 

}
