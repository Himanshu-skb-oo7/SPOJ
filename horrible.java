import java.io.*;
import java.util.Arrays;

public class Main
{
    private static FastReader in;
    private static PrintWriter out;
    private static int [] arr;

    public static void main (String[] args) throws IOException{
        in = new FastReader ();
        out = new PrintWriter (System.out, true);
        int test = in.nextInt();
        while (test-- > 0) {
	        int n = in.nextInt (), c = in.nextInt();
	        arr = new int [n + 1];
	        Arrays.fill(arr, 0);
	        IntervalTree root = new IntervalTree (1, n);
	        
	        while (c-- > 0) {
	            int command = in.nextInt(),
	        	          p = in.nextInt(),
	        	          q = in.nextInt();
	        	          
	            if (command == 1) {
	            	IntervalTree result = root.lazyQuery(p, q);
	            	out.println(result.sum);
	            } else if (command == 0){
	            	//arr[0] = 3;
	            	int v = in.nextInt();
	            	root.lazyRangeUpdate(p, q, v);
	            }
	        }
        }
    }
    
    static class IntervalTree {
        public IntervalTree Lchild = null,
                            Rchild = null;
        public int start, end;
        public long sum, lazy;
        
        public IntervalTree () {}
        
        public IntervalTree (int _start, int _end) {
            start = _start; end = _end;
            if (start != end) {
                int mid = (start + end) >> 1;
                Lchild = new IntervalTree (start, mid);
                Rchild = new IntervalTree (mid + 1, end);
                /*join (this, Lchild, Rchild);*/
            }
            /*else {
            	this.sum = arr [start];
            }*/
        }
        
        public long range () { 
            return end - start + 1;
        }
        
        public void push () { 
            if (Lchild != null) {
                Lchild.sum += Lchild.range () * lazy;
                Lchild.lazy += lazy;
                Rchild.sum += Rchild.range () * lazy;
                Rchild.lazy += lazy;
                sum = Lchild.sum + Rchild.sum;
            } 
            lazy = 0;
        } 
        
        public IntervalTree lazyQuery (int a, int b) {
            if (a == start && end == b) return this;
            
            push();             //being lazy
            
            int mid = (start + end) >> 1;
            if (a > mid) return Rchild.lazyQuery (a, b);
            if (b <= mid) return Lchild.lazyQuery (a, b);
            IntervalTree ans = new IntervalTree();
            join (ans, Lchild.lazyQuery (a, mid), Rchild.lazyQuery (mid + 1, b));
            return ans;
        }
        
        public void lazyRangeUpdate(int _start, int _end, int value) {
            if(_start > end || start > _end) return;
            if(start == _start && end == _end) {
                sum += range()*value;
                lazy += value;
                return;
            }
            
            push();               //being lazy
            
            int mid = (start + end) >> 1;
            if (_start > mid)             Rchild.lazyRangeUpdate(_start, _end, value);
            else if(mid >= _end)          Lchild.lazyRangeUpdate(_start, _end, value);
            else{                         Lchild.lazyRangeUpdate(_start, mid, value);
                                          Rchild.lazyRangeUpdate(mid+1, _end, value);
            }
            join (this, Lchild, Rchild);               
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
