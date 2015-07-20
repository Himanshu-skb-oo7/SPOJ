tiles = [1,1,5,11]
for i in xrange(4,22):
        tiles.append(tiles[i-1]+5*tiles[i-2]+tiles[i-3]-tiles[i-4])

for i in xrange(1,input()+1):
        print i,tiles[input()]
