//I gave up......... :<

import java.io.*;
import java.util.Arrays;
import java.util.TreeMap;

public class OrderStatisticSet {
    private static FastReader in;
    private static PrintWriter out;
    private static int [] arr, sortedArr;
    private static char [] commands;
    private static TreeMap<Integer, Integer> map;

    public static void main (String [] args) throws IOException {
        in = new FastReader ();
        out = new PrintWriter (System.out, true);
        
    	int q = in.nextInt();
        arr = new int [q + 1];
        sortedArr = new int[q + 1];
        commands = new char[q + 1];
        map = new TreeMap<Integer, Integer>();
        
        sortedArr[0] = Integer.MIN_VALUE;
        for (int i = 1; i <= q; i++) {
        	commands[i] = in.nextChar();
        	arr[i] = sortedArr[i] = in.nextInt();
        }
        Arrays.sort(sortedArr);
        
        map.put(sortedArr[1], 1);
        for (int i = 2; i <= q; i++)
        	if (sortedArr[i] != sortedArr[i-1])
        		map.put(sortedArr[i], i);
        
        IntervalTree root = new IntervalTree (1, q);
        
        for (int i = 1;  i <= q; i++) {
            int nodeIndex = map.get(arr[i]);
            
            if (commands[i] == 'I') {
            	root.update(nodeIndex, 1);
            } else if (commands[i] == 'D') {
            	root.update(nodeIndex, 0);
            } else if (commands[i] == 'K') {
            	if (root.sum < arr[i])
            		out.println("invalid");
            	else
            		out.println(sortedArr[root.binarySearch(1, q, arr[i])]);
            } else if (commands[i] == 'C') {
            	if (nodeIndex == 1)
            		out.println(0);
            	else
            		out.println(root.query(1, nodeIndex-1).sum);
            }
        }
    }
    
    static class IntervalTree {
        public IntervalTree Lchild = null,
                            Rchild = null;
        public int start, end, sum;
        
        public IntervalTree () {}
        
        public IntervalTree (int _start, int _end) {
            start = _start; end = _end;
            if (start != end) {
                int mid = (start + end) >> 1;
                Lchild = new IntervalTree (start, mid);
                Rchild = new IntervalTree (mid + 1, end);
                join (this, Lchild, Rchild);
            }
            else {
            	this.sum = 0;
            }
        }
        
        public IntervalTree query (int a, int b) {
            if (a == start && end == b) return this;
            int mid = (start + end) >> 1;
            if (a > mid) return Rchild.query (a, b);
            if (b <= mid) return Lchild.query (a, b);
            IntervalTree ans = new IntervalTree ();
            join (ans, Lchild.query (a, mid), Rchild.query (mid + 1, b));
            return ans;
        }
        
        public void update(int i, int value) {
            if(i == start && i == end) {
              this.sum = value; 
              return; 
            } 
            if(start > i || i > end) return;
            if(Lchild == null) return;
            int mid = (start + end) >> 1;
            if (i > mid) Rchild.update(i, value);
            else         Lchild.update(i, value);
            join (this, Lchild, Rchild);               
        } 
        
        public int binarySearch(int a, int b, int value) {
        	if (b-a+1 == value)
        		return b;
        	
        	int mid = (a+b)>>1;
        	int left = Lchild.sum;
        	if (left >= value)
        		return Lchild.binarySearch(a, mid, value);
        	return Rchild.binarySearch(mid+1, b, value-left);
        }
        
        public void join (IntervalTree parent, IntervalTree Lchild, IntervalTree Rchild) {
        	 parent.sum = Lchild.sum + Rchild.sum;
        }
    }
}

/** Faster input **/
class FastReader {
    final private int BUFFER_SIZE = 1 << 16;
    private DataInputStream din;
    private byte[] buffer;
    private int bufferPointer, bytesRead;
    public FastReader(){
        din=new DataInputStream(System.in);
        buffer=new byte[BUFFER_SIZE];
        bufferPointer=bytesRead=0;
    }

    public FastReader(String file_name) throws IOException{
        din=new DataInputStream(new FileInputStream(file_name));
        buffer=new byte[BUFFER_SIZE];
        bufferPointer=bytesRead=0;
    }

    public String readLine() throws IOException{
        byte[] buf=new byte[64]; // line length
        int cnt=0,c;
        while((c=read())!=-1){
            if(c=='\n')break;
            buf[cnt++]=(byte)c;
        }
        return new String(buf,0,cnt);
    }

    public int nextInt() throws IOException{
        int ret=0;byte c=read();
        while(c<=' ')c=read();
        boolean neg=(c=='-');
        if(neg)c=read();
        do{ret=ret*10+c-'0';}while((c=read())>='0'&&c<='9');
        if(neg)return -ret;
        return ret;
    } 

    public long nextLong() throws IOException{
        long ret=0;byte c=read();
        while(c<=' ')c=read();
        boolean neg=(c=='-');
        if(neg)c=read();
        do{ret=ret*10+c-'0';}while((c=read())>='0'&&c<='9');
        if(neg)return -ret;
        return ret;
    }

    public double nextDouble() throws IOException{
        double ret=0,div=1;byte c=read();
        while(c<=' ')c=read();
        boolean neg=(c=='-');
        if(neg)c = read();
        do {ret=ret*10+c-'0';}while((c=read())>='0'&&c<='9');
        if(c=='.')while((c=read())>='0'&&c<='9')
            ret+=(c-'0')/(div*=10);
        if(neg)return -ret;
        return ret;
    }
    
    public char nextChar() throws IOException{
        byte c=read();
        while(c<=' ')c=read();
        return (char)c;
    }
    
    private void fillBuffer() throws IOException{
        bytesRead=din.read(buffer,bufferPointer=0,BUFFER_SIZE);
        if(bytesRead==-1)buffer[0]=-1;
    }
    
    private byte read() throws IOException{
        if(bufferPointer==bytesRead)fillBuffer();
        return buffer[bufferPointer++];
    }
    
    public void close() throws IOException{
        if(din==null) return;
        din.close();
    }
}
