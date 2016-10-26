import sys
def main():

    filename = sys.argv[1]
    f = open(filename, 'rU')

    input_dict = {}

    for nums in f:
        input_dict[int(nums.rstrip('\n'))] = 1

    #print input_dict
    result = 0
    for t in range(-10000,10001):
        B = []
        for x in input_dict.keys():
            if x!=(t-x) and input_dict.has_key(t-x) and (x and (t-x) not in B):
                B.append(x)
                B.append(t-x)
                result += 1
    print result
if __name__ == '__main__':
    main()