

def hello():
    c = int(1e9)
    while c > 0:
        c -= 1

def panda():
    import pandas as pd
    df = pd.DataFrame([x for x in range(0, 100000000)])
    for i in range(0, len(df.values)):
        x = i
    return x

