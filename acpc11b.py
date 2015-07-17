for _ in range(input()):
        m1 = map(int, raw_input().split())
        m1.pop(0)
        m2 = map(int, raw_input().split())
        m2.pop(0)
        
        m1,m2 = sorted(m1),sorted(m2)
        l1,l2 = len(m1),len(m2)
        
        i,j,diff = 0,0,1000000
        while i < l1 and j < l2:
                diff  = min(diff, abs(m1[i] - m2[j]))
                if m1[i] < m2[j]:
                        i += 1
                else:
                        j += 1
        print diff
