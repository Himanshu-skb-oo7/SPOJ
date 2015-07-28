while True:
        line = raw_input()
        if line == 'Q':
                break
        x,y,count = 0,0,0
        positions = [(x,y)]

        for ch in line:
                if ch == 'U':
                        y += 1
                        if (x,y) in positions:
                                count += 1
                        else:
                                positions.append((x,y))
                if ch == 'D':
                        y -= 1
                        if (x,y) in positions:
                                count += 1
                        else:
                                positions.append((x,y))
                if ch == 'R':
                        x += 1
                        if (x,y) in positions:
                                count += 1
                        else:
                                positions.append((x,y))
                if ch == 'L':
                        x -= 1
                        if (x,y) in positions:
                                count += 1
                        else:
                                positions.append((x,y))
        print count
