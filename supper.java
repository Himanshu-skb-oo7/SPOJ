import java.util.ArrayList;
import java.util.Collections;
import java.util.Scanner;

public class SupernumbersInAPermutation {
	
	private static Scanner in;
	private static int permutation[];

	public static void main(String[] args) {
		
		in = new Scanner(System.in);
		
		for (int i = 0; i < 10; i++) {
			int LISLength = -1,
			    n = in.nextInt();
			int LIS[] = new int[n+1],
			    LDS[] = new int[n+1];
			ArrayList<Integer> superNumbers = new ArrayList<Integer>(); 
			
			permutation = new int[n+1];
			
			IntervalTree root = new IntervalTree(1, n);
			
			for (int j = 1; j <= n; j++) {
				permutation[j] = in.nextInt();
				LIS[j] = 1 + root.query(1, permutation[j]).data;
				root.update(permutation[j], LIS[j]);
				LISLength = Math.max(LISLength, LIS[j]);
				//System.out.println(LIS[j] + " " + root.data);
			}
			
			root = new IntervalTree(1, n);
			
			for (int j = n; j >= 1; j--) {
				LDS[j] = 1 + root.query(permutation[j], n).data;
				root.update(permutation[j], LDS[j]);
				//System.out.println(LIS[j] + " " + LDS[j]);
			}
			
			for (int j = 1; j <= n; j++)
			  if (LIS[j] + LDS[j] - 1 == LISLength)
			    superNumbers.add(permutation[j]);
			
			Collections.sort(superNumbers);
			
			System.out.println(superNumbers.size());
			for (int j = 0; j < superNumbers.size(); j++)
				System.out.print(superNumbers.get(j)+ " ");
		}
	}
	
	static class IntervalTree {
        public IntervalTree Lchild = null,
                            Rchild = null;
        public int data, start, end;
        
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
            	this.data = 0;
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
            if(start == i && i ==end) {
            	this.data = value;
            	return; 
            } 
            if(start > i || i > end) return;
            if(Lchild == null) return;
            int mid = (start + end) >> 1;
            if (i > mid) Rchild.update(i, value);
            else         Lchild.update(i, value);
            join (this, Lchild, Rchild);          
        } 
        
        public void join (IntervalTree parent, IntervalTree Lchild, IntervalTree Rchild) {
            parent.data = Math.max(Lchild.data, Rchild.data);
        }
    }
}
