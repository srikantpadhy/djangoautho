# fac,fibo,primenum,re,s,combination,args,kwargs,decor,deepcopy,shallowcopy.

import pandas as pd
import multiprocessing as mp


# -1 day, 23:59:59.058517
# -1 day, 23:59:50.153324
# -1 day, 23:59:50.767708
def test(chunk):
    chunk['Footnotes'] = 'srikant'
    return chunk

def main():
    df = pd.read_csv(r"D:\srikant\businessop.csv", sep=',', chunksize=1000, encoding='cp1252')
    n_c = mp.cpu_count()
    print(n_c)

    with mp.Pool(n_c) as pool:
        n_v = pool.map(test,df)
    f_d = pd.concat(n_v)
    # print(f_d['Footnotes'])
import datetime
if __name__ =="__main__":
    s = datetime.datetime.now()
    main()
    r = datetime.datetime.now()
    print(s-r)
    print(r)

