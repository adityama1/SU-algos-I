import sys
import math
input_data = []

def main():

    filename = sys.argv[1]
    f = open(filename, 'rU')

    global input_data
    for nums in f:
        input_data.append(int(nums.rstrip('\n')))
    input_data = list(set(input_data))  #removed duplications

    print "Done: removing duplicates"
    input_data.sort() #inplace Timsort - combi of merge and insertion sort

    print "Done: sorting"

    result = 0
    for t in range(-10000, 10001):
        B = []
        for x in input_data:
            if (t-x) >= input_data[0] and (t-x)<=input_data[len(input_data)-1]:
                if x!=(t-x) and binary_search((t-x)) and (x and (t-x) not in B):
                    #search t-x in input_data
                    B.append(x)
                    B.append(t-x)
                    result += 1
    print result

def binary_search(a):
    i = 0
    j = len(input_data)-1
    return now_search(a,i,j)

def now_search(find_element,i,j):

    len_ij = j-i+1
    if len_ij <2:
        if input_data[j] == find_element: return True
        else: return False
    mid = int(math.floor((i+j) // 2))
    if find_element > input_data[mid]:
        value = now_search(find_element,mid+1,j)
    elif find_element < input_data[mid]:
        value = now_search(find_element,i, mid-1)
    elif find_element == input_data[mid]:
        return True
    return value

if __name__ == '__main__':
    main()