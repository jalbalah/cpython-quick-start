

import os
from time import time

def hello2():
    c = int(1e9)
    while c > 0:
        c -= 1


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