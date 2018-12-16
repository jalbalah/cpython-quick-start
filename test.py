

import os
from time import time

def hello2():
    c = -999999999999999999999999
    for i in range(0, int(10e9)):
        c += i
    print(c)


if __name__ == "__main__":
    os.system('sh build.sh')
    from module import hello
    start = time()
    hello()
    end = time()
    print('cpp took {} seconds'.format(end - start))

    start = time()
    hello2()
    end = time()
    print('python took {} seconds'.format(end - start))