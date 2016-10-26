import sys
import random
import math

def findMinCut(dict):

#    list = [7,8,2,3,6,5,4,2,7,6,1,4]
    replace_list = []
    while len(dict.keys()) > 2:     # and i<len(list):
        a,b= random.sample(dict.keys(),2)

        #a = list[i]
        #b = list[i+1]

        replace_list.append(a)
        replace_list.append(b)
        if a in dict.keys() and b in dict.keys():   #always true if condition
            dict[a] += dict[b]
            while a in dict[a]:
                dict[a].remove(a)
            while b in dict[a]:
                dict[a].remove(b)
#            print a,b
#            print dict
            del dict[b]
#    print
#        i += 2
#    print dict

    key = dict.keys()
    l1 = dict[key[0]]
    l2 = dict[key[1]]


    for i in range(0,len(replace_list),2):
        for index_1 in range(0, len(l1)):
            if l1[index_1] == replace_list[i+1]:
                l1[index_1] = replace_list[i]
        for index_2 in range(0, len(l2)):
            if l2[index_2] == replace_list[i+1]:
                l2[index_2] = replace_list[i]
#    print l1
#    print l2

    i = 0
    j = 0
    len_key1 = 0
    len_key2 = 0

    while i < len(l1):
        if key[1] == l1[i]:
            len_key1 += 1
        i += 1
    while j < len(l2):
        if key[0] == l2[j]:
            len_key2 += 1
        j += 1

    #print "key1:" + str(len_key1)
    #print "key2:" + str(len_key2)

    if len_key1 == len_key2:
        return len_key1
    else:
        print "unequal" + str(len_key2) + str(len_key1)

def main():
    filename = sys.argv[1]
    f = open(filename, 'rU')

    dict = {}
    for nums in f:
        nums = nums.split()
        dict[int(nums[0])] = map(int,nums[1:len(nums)])

    N = (len(dict.keys()))
    #N = N*N
    #N = 1
    N = int(math.ceil(N*N * math.log(N)))

    true_min = findMinCut(dict)

    for i in range(0,N):
        f = open(filename, 'rU')
        print i
        for nums in f:
            nums = nums.split()
            dict[int(nums[0])] = map(int, nums[1:len(nums)])
        min_cut = findMinCut(dict)
        if true_min > min_cut:
            true_min = min_cut
    print true_min

if __name__ == '__main__':
    main()