import sys
import numpy as np
import time

t0 = time.clock()

inversions = 0

def sort_and_count(A,n):
    if n == 1:
        return A
    mid = n//2
    left = A[0:mid]
    right = A[mid:n]
    B = sort_and_count(left,len(left))
    C = sort_and_count(right,len(right))
    D = merge_and_count(B,C)
    return D

def merge_and_count(B,C):
    global inversions
    i = 0
    j = 0
    k = 0
    n = len(B) + len(C)
    D = []
    for k in range(0,n):
        if i < len(B) and j < len(C):
            if B[i] < C[j]:
                D.append(B[i])
                i += 1
            elif B[i] > C[j]:
                D.append(C[j])
                j += 1
                inversions = inversions + len(B) - i
        else:
            if i < len(B):
                D.append(B[i])
                i += 1
            elif j < len(C):
                D.append(C[j])
                j += 1
    return D

def main():
    filename = sys.argv[1]
    f = open(filename, 'rU')
    array_list = []
    for nums in f:
        array_list.append(int(nums.rstrip('\n')))

    #array_list = array_list[0:5]
    #array_list = [4, 80, 70, 23, 9, 60, 68, 27, 66, 78, 12, 40, 52, 53, 44, 8, 49, 28, 18, 46, 21, 39, 51, 7, 87, 99, 69, 62, 84, 6, 79, 67, 14, 98, 83, 0, 96, 5, 82, 10, 26, 48, 3, 2, 15, 92, 11, 55, 63, 97, 43, 45, 81, 42, 95, 20, 25, 74, 24, 72, 91, 35, 86, 19, 75, 58, 71, 47, 76, 59, 64, 93, 17, 50, 56, 94, 90, 89, 32, 37, 34, 65, 1, 73, 41, 36, 57, 77, 30, 22, 13, 29, 38, 16, 88, 61, 31, 85, 33, 54]
    n = len(array_list)

    array_list = sort_and_count(array_list,n)
    #print array_list
    print inversions, n

    t1 = time.clock()
    print "Time is:" + str(t1-t0)

if __name__ == '__main__':
    main()