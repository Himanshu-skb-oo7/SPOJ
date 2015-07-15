def foo(n, numbers):
        w = max(numbers)
        if w >= n:
                return -1
        temp = 0
        for i in numbers:
                if i == w - 1:
                        temp += 1
                elif i != w:
                        return -1
        if temp == w:
                return w
        if temp == 0:
                return w + 1
        return -1

print foo(input(),map(int,raw_input().split()))
