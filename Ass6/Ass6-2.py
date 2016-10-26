import sys
import math

def main():
    #first read the nums one by one
    filename = sys.argv[1]
    f = open(filename, 'rU')

    max_heap = []
    min_heap = []

    median_main = []
    temp = []
    for nums in f:
        a = int(nums.rstrip('\n'))
        if len(min_heap) < 1 and len(max_heap) < 1:
            temp.append(a)
            if len(temp)==2:
                if temp[1]>temp[0]:
                    max_heap.append(temp[0])
                    min_heap.append(temp[1])
                    median_main.append(temp[0])
                    median_main.append(temp[0])
                    continue
                else:
                    max_heap.append(temp[1])
                    min_heap.append(temp[0])
                    median_main.append(temp[1])
                    median_main.append(temp[1])
                    continue
            else:
                continue

        if a > max_heap[0] and a < min_heap[0]:
            insert_max_heap(max_heap, a)
        elif a >= min_heap[0]:
            insert_min_heap(min_heap, a)
        elif a <= max_heap[0]:
            insert_max_heap(max_heap, a)

        if abs(len(max_heap) - len(min_heap)) > 1:
            modify(min_heap,max_heap)

        if len(max_heap) >= len(min_heap):
            median_main.append(max_heap[0])
        elif len(max_heap) < len(min_heap):
            median_main.append(min_heap[0])

    #print median_main
    #print min_heap
    #print max_heap
    median_sum = sum(median_main)
    median_mod = median_sum % len(median_main)
    print median_sum
    print median_mod
    print len(median_main)


def insert_max_heap(heap, num):
    heap.append(num)
    i = heap.index(num) + 1
    while i != 1:
        parent = int(math.floor(i/2))
        if heap[parent-1] <= heap[i-1]:
            heap[i-1], heap[parent-1] = heap[parent-1], heap[i-1]
        i = parent


def insert_min_heap(heap, num):
    heap.append(num)
    i = heap.index(num) + 1
    while i != 1:
        parent = int(math.floor(i / 2))
        if heap[parent - 1] >= heap[i - 1]:
            heap[i - 1], heap[parent-1] = heap[parent - 1], heap[i - 1]
        i = parent

def modify(min_heap,max_heap):
    if len(min_heap) > len(max_heap):
        insert_max_heap(max_heap,min_heap[0])
        heapify(min_heap,1)
    elif len(max_heap) > len(min_heap):
        insert_min_heap(min_heap,max_heap[0])
        heapify(max_heap,0)


def heapify(heap_dont_lie,bool_eya):
    heap_dont_lie[0] = heap_dont_lie[len(heap_dont_lie) - 1]
    del heap_dont_lie[len(heap_dont_lie) - 1]
    i = 0
    if bool_eya:
        while i<len(heap_dont_lie):
            c1_present = hasChild(heap_dont_lie,(2*i+1))
            c2_present = hasChild(heap_dont_lie,(2*i+2))

            if not c1_present and not c2_present:
                i += 1
                continue

            elif c1_present and c2_present:
                child_1 = heap_dont_lie[2*i+1]
                child_2 = heap_dont_lie[2*i+2]
                if child_1 < child_2 and child_1 < heap_dont_lie[i]:
                    heap_dont_lie[2*i+1] = heap_dont_lie[i]
                    heap_dont_lie[i] = child_1
                elif child_2 < child_1 and child_2 < heap_dont_lie[i]:
                    heap_dont_lie[2*i+2] = heap_dont_lie[i]
                    heap_dont_lie[i] = child_2
            elif c1_present:
                child_1 = heap_dont_lie[2 * i + 1]
                if child_1 < heap_dont_lie[i]:
                    heap_dont_lie[2 * i + 1] = heap_dont_lie[i]
                    heap_dont_lie[i] = child_1
            elif c2_present:
                child_2 = heap_dont_lie[2 * i + 2]
                if child_2 < heap_dont_lie[i]:
                    heap_dont_lie[2*i+2] = heap_dont_lie[i]
                    heap_dont_lie[i] = child_2
            i += 1
    else:
        while i<len(heap_dont_lie):
            c1_present = hasChild(heap_dont_lie,(2*i+1))
            c2_present = hasChild(heap_dont_lie,(2*i+2))

            if not c1_present and not c2_present:
                i += 1
                continue

            elif c1_present and c2_present:
                child_1 = heap_dont_lie[2*i+1]
                child_2 = heap_dont_lie[2*i+2]
                if child_1 > child_2 and child_1 > heap_dont_lie[i]:
                    heap_dont_lie[2*i+1] = heap_dont_lie[i]
                    heap_dont_lie[i] = child_1
                elif child_2 > child_1 and child_2 > heap_dont_lie[i]:
                    heap_dont_lie[2*i+2] = heap_dont_lie[i]
                    heap_dont_lie[i] = child_2
            elif c1_present:
                child_1 = heap_dont_lie[2 * i + 1]
                if child_1 > heap_dont_lie[i]:
                    heap_dont_lie[2 * i + 1] = heap_dont_lie[i]
                    heap_dont_lie[i] = child_1
            elif c2_present:
                child_2 = heap_dont_lie[2 * i + 2]
                if child_2 > heap_dont_lie[i]:
                    heap_dont_lie[2*i+2] = heap_dont_lie[i]
                    heap_dont_lie[i] = child_2
            i += 1

def hasChild(heap,a):
    if a<len(heap):
        return 1
    else: return 0

if __name__ == '__main__':
    main()