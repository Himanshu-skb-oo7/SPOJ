importPackage(java.io);
importPackage(java.lang);
br = new BufferedReader(new InputStreamReader(System['in']));

while(true) {
  n = br.readLine();
  if(n==42)
    break;
  System.out.println(n);
}
