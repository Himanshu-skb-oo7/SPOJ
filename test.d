import std.c.stdio;

int main()
{
  int t;
  while(1)
  {
    scanf("%d",&t);
    if(t==42)
      break;
    printf("%d\n",t);
  }
  return 0;
}
