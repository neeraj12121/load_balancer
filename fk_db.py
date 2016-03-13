#Count number of square in m*n rectangle

import time


def count_sq(m,n):
    if (n<m):
        a,b=n,m
    print("HIT DB")
    return int(m*(m+1)*(2*m+1)/6+(n-m)*m*(m+1)/2)

def test_count_sq():
    start_time=time.time()
    print (count_sq(7,4))
    print("For Counting Number of Square Algorithm took {0} seconds".format(time.time-start_time))
    assert count_sq(5,4) == 20


if __name__=="__main__":
    test_count_sq()
