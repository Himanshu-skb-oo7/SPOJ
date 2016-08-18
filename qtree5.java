import java.util.*;
import java.io.*;
/*
* https://github.com/detel/Algorithms/blob/master/Graph-Theory/Centroid%20Decomposition.java
* https://github.com/detel/Miscellaneous/blob/master/IncreaseStackSize.java
*/
public class QTREE5 {
    public static InputReader in;
    public static PrintWriter out;

    public static final int MOD = (int) (1e9 + 7);
    public static ArrayList<Integer>[] graph;
    public static int[] P, subSize, label, dist[];
    public static int LOGMAXN;
    
    public static void main(String[] args) {
        new Thread(null, new Runnable() {
            public void run() {
                try{
                    solve();
                }
                catch(Exception e){
                    e.printStackTrace();
                }
            }
        }, "1", 1 << 26).start();
    }
    
    @SuppressWarnings("unchecked")
    public static void solve() {
        in = new InputReader(System.in);
        out = new PrintWriter(System.out);
        
        int n = in.nextInt();
        graph = new ArrayList[n];
        for(int i = 0; i < n; ++i)  graph[i] = new ArrayList<Integer>();
        for(int i = 1; i < n; ++i) {
            int u = in.nextInt() - 1,
                v = in.nextInt() - 1;
            graph[u].add(v);
            graph[v].add(u);
        }
        
        // construct centroid tree in P
        P = new int[n];
        subSize = new int[n];
        label = new int[n];
        Arrays.fill(P, -2);
        decompose(0, -1, n, 0);

        // preprocess needed distances
        LOGMAXN = (int)(Math.log(n)/Math.log(2) + 3);
        dist = new int[LOGMAXN][n];
        for(int i = 0; i < n; ++i)
            computeDist(i, label[i], i, -1, 0);
        
        // process queries
        int m = in.nextInt();
        near = new TreeMap[n];
        for (int i = 0; i < n; i++)
            near[i] = new TreeMap<Integer, Integer>();
        //Arrays.fill(near, n);
        boolean[] isWhite = new boolean[n];
        StringBuilder sb = new StringBuilder();
        while(m-- > 0) {
            if(in.nextInt() == 0) {
                int i = in.nextInt() - 1;
                isWhite[i] = !isWhite[i];
                update(i, isWhite[i]);
            } else {
                sb.append(query(in.nextInt() - 1)+"\n");
            }
        }
        
        out.print(sb);

        out.close();
    }
    
    /*
     * Update and Query
     */
    public static TreeMap<Integer, Integer>[] near;
    public static void update(int v, boolean toAdd) {
        int u = v,
            lb = label[v];
        while(u != -1) {
            int key = dist[lb][v];
            if(toAdd) {
                if(!near[u].containsKey(key))
                    near[u].put(key, 0);
                near[u].put(key, near[u].get(key) + 1);
            } else {
                near[u].put(key, near[u].get(key) - 1);
                if(near[u].get(key) == 0)
                    near[u].remove(key);
            }
            u = P[u];
            --lb;
        }
    }
    
    public static int query(int v) {
        int u = v,
            lb = label[v],
            ans = Integer.MAX_VALUE;
        while(u != -1) {
            if(near[u].firstEntry() != null)
                ans = Math.min(ans, near[u].firstKey() + dist[lb][v]);
            u = P[u];
            --lb;
        }
        return ans == Integer.MAX_VALUE? -1 : ans;
    }
    
    public static int findSize(int u, int p) {
        int sz = 1;
        for(int i = 0, size = graph[u].size(); i < size; ++i) {
            int v = graph[u].get(i);
            if(v != p && P[v] == -2)
                sz += findSize(v, u);
        }
        return subSize[u] = sz;
    }

    public static int decompose(int u, int p, int n, int lb) {
        if(p == -1)
            n = findSize(u, -1);
        int idx = -1;
        for(int i = 0, size = graph[u].size(); i < size; ++i) {
            int v = graph[u].get(i);
            if(v != p && P[v] == -2 && subSize[v] > n / 2) {
                idx = v;
                break;
            }
        }
        if(idx != -1)
            return decompose(idx, u, n, lb);

        //u is centroid, decompose forest
        P[u] = -1;
        for(int i = 0, size = graph[u].size(); i < size; ++i) {
            int v = graph[u].get(i);
            if(P[v] == -2)
                P[decompose(v, -1, n, lb + 1)] = u;
        }
        label[u] = lb;
        return u;
    }
    
    /*
     * Distance Preprocessing
     */
    public static void computeDist(int s, int lb, int u, int p, int d) {
        dist[lb][u] = d;
        for(int i = 0, size = graph[u].size(); i < size; ++i) {
            int v = graph[u].get(i);
            if(v != p && label[v] >= lb)
                computeDist(s, lb, v, u, d + 1);
        }
    }


    static class Node implements Comparable<Node> {
        int next;
        long dist;

        public Node(int u, int v) {
            this.next = u;
            this.dist = v;
        }

        public void print() {
            out.println(next + " " + dist + " ");
        }

        public int compareTo(Node n) {
            return Integer.compare(-this.next, -n.next);
        }
    }

    static class InputReader {

        private InputStream stream;
        private byte[] buf = new byte[8192];
        private int curChar, snumChars;
        private SpaceCharFilter filter;

        public InputReader(InputStream stream) {
            this.stream = stream;
        }

        public int snext() {
            if (snumChars == -1)
                throw new InputMismatchException();
            if (curChar >= snumChars) {
                curChar = 0;
                try {
                    snumChars = stream.read(buf);
                } catch (IOException e) {
                    throw new InputMismatchException();
                }
                if (snumChars <= 0)
                    return -1;
            }
            return buf[curChar++];
        }

        public int nextInt() {
            int c = snext();
            while (isSpaceChar(c))
                c = snext();
            int sgn = 1;
            if (c == '-') {
                sgn = -1;
                c = snext();
            }
            int res = 0;
            do {
                if (c < '0' || c > '9')
                    throw new InputMismatchException();
                res *= 10;
                res += c - '0';
                c = snext();
            } while (!isSpaceChar(c));
            return res * sgn;
        }

        public long nextLong() {
            int c = snext();
            while (isSpaceChar(c))
                c = snext();
            int sgn = 1;
            if (c == '-') {
                sgn = -1;
                c = snext();
            }
            long res = 0;
            do {
                if (c < '0' || c > '9')
                    throw new InputMismatchException();
                res *= 10;
                res += c - '0';
                c = snext();
            } while (!isSpaceChar(c));
            return res * sgn;
        }

        public int[] nextIntArray(int n) {
            int a[] = new int[n];
            for (int i = 0; i < n; i++)
                a[i] = nextInt();
            return a;
        }

        public String readString() {
            int c = snext();
            while (isSpaceChar(c))
                c = snext();
            StringBuilder res = new StringBuilder();
            do {
                res.appendCodePoint(c);
                c = snext();
            } while (!isSpaceChar(c));
            return res.toString();
        }

        public boolean isSpaceChar(int c) {
            if (filter != null)
                return filter.isSpaceChar(c);
            return c == ' ' || c == '\n' || c == '\r' || c == '\t' || c == -1;
        }

        public interface SpaceCharFilter {
            public boolean isSpaceChar(int ch);
        }
    }
}
