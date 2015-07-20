tiles = [1,0,3,0]
for i in xrange(4,31):
        tiles.append(4*tiles[i-2]-tiles[i-4])

while True:
        num = int(raw_input())
        if num == -1:
                break
        print tiles[num]
