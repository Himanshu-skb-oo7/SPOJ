for _ in range(input()):

        count,total = 0,0
        n,m = map(int,raw_input().split())

        for i in range(n,m+1):
                for j in range(1,13):
                        day21 = 21 + ((153*(j+12*((14-j)/12)-3)+2)/5) + (365*(i+4800-((14-j)/12))) + ((i+4800-((14-j)/12))/4) - ((i+4800-((14-j)/12))/100) + ((i+4800-((14-j)/12))/400) - 32045
                        if day21%7 == 4:
                                count += 1
        for i in range(n,m+1):
                total += 365
                if ((i%4 == 0 and i%100 != 0) or i%400==0):
                        total += 1
        safe_days = total - count
        
        days = [0,0,0,0,0]
        for i in range(4,-1,-1):
                if i==3:
                        days[i] = safe_days%18
                        safe_days = safe_days/18
                else:
                        days[i] = safe_days%20
                        safe_days = safe_days/20
                        
        print '.'.join(map(str,days))
