import sys
import numpy as np

comparisons = 0

def quick_sort(A, start_ind, end_ind):
    len_A = end_ind - start_ind
    if len_A <= 1: return

    if len_A%2 == 0:
        mid = A[start_ind + len_A//2 - 1]
    else:
        mid = A[start_ind + len_A//2]
    piv = np.median([A[start_ind], mid, A[len_A - 1]]).astype(int)

    ind = A.index(piv)
    A[start_ind], A[ind] = A[ind], A[start_ind]

    pivot = A[start_ind]
    partition(A, start_ind, end_ind)
    quick_sort(A, start_ind, A.index(pivot))
    quick_sort(A, A.index(pivot)+1, end_ind)

def partition(A, l, r):
    global comparisons
    comparisons = comparisons + (len(A) - 1)
    pivot = A[l]
    i = l + 1
    for j in range(l+1,r):
        if A[j] < pivot:
            A[i], A[j] = A[j], A[i]
            i += 1
    A[l], A[i-1] = A[i-1], A[l]

def main():
    filename = sys.argv[1]
    f = open(filename, 'rU')
    array_list = []
    for nums in f:
        array_list.append(int(nums.rstrip('\n')))
    #print array_list
    quick_sort(array_list,0,len(array_list))
    print array_list
    #print comparisons
if __name__ == '__main__':
    main()