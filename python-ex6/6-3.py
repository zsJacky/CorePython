#!/usr/bin/env python 
import random

def bubblesort(target):
    print target
    length = len(target)

    while length > 1:
        length -= 1
        cur = 0
        while cur < length:
            if target[cur] > target[cur+1]:
                target[cur], target[cur+1] = target[cur+1], target[cur]
            cur += 1
    return target

if __name__ == "__main__":
    target = [random.randint(1, 1000) for i in xrange(20)]
    print bubblesort(target)