import sys
n=-1
for line in sys.stdin:
    if n==-1:
        data = []
        n = int(line)
    elif n==0:
        print(day, end=' ')
        max_item = max(items, key=items.get)
        print(max_item, end=' ')
        print(items[max_item])
        n = -1
    else:
        data.append(line.split())
        n -= 1
        if n == 0:
            day = data[0][0]
            items={}
            for i in range(len(data)):
                if data[i][0]!=day:
                    print(day, end=' ')
                    max_item = max(items, key=items.get)
                    print(max_item, end=' ')
                    print(items[max_item])
                    day = data[i][0]
                    items = {}

                if data[i][1] in items:
                    print(data[i][3])
                    items[data[i][1]] += int(data[i][3])
                else:
                    items[data[i][1]] = int(data[i][3])
                    
