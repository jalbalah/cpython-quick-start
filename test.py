

import os
from time import time

def hello2():
    c = int(1e9)
    while c > 0:
        c -= 1

def panda2():
    import pandas as pd
    df = pd.DataFrame([x for x in range(0, 100000000)])
    for i in range(0, len(df.values)):
        x = i
    return x

if __name__ == "__main__":
    os.system('sh build.sh')
    from module import hello
    from module import panda
    start = time()
    # hello()
    panda()
    end = time()
    print('cpp took {} seconds'.format(end - start))

    start = time()
    # hello2()
    panda2()
    end = time()
    print('python took {} seconds'.format(end - start))
