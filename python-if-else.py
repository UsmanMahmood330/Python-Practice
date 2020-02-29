import math
import os
import random
import re
import sys



if __name__ == '__main__':
    #Adding Comments
    print(sys.argv[0])
    n = int(sys.argv[1])
    l = n % 2
    if (l == 1) or (n % 2 == 0 and n>= 6 and n<= 20):
        print("Weird")
    elif (l == 0) and ((n >= 2 and n <= 5) or  (n>20) ):
        print("Not Weird")

    
