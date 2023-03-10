# python3

import sys
import threading
import numpy


def compute_height(n, parents):
    berni={x:[] for x in range(n)}
    visassaknes=[]
    for x,vec in enumerate(parents):
        if vec==-1:
            visassaknes.append(x)
        else:
            berni[vec].append(x)
            
    
    def dzilakais(pieder,dzilums):
        if not berni[pieder]:
            return dzilums
        else:
            dzilakais_punkts=0
            
            for berns in berni[pieder]:
                dzilums_b=dzilakais(berns,dzilums+1)
                
                dzilakais_punkts=max(dzilakais_punkts,dzilums_b)
            return dzilakais_punkts
        
    maxheight=float('-inf')
    for sakne in visassaknes:
        garums=dzilakais(sakne,0)
        maxheight=max(maxheight,garums)
    return maxheight+1

def main():
    ievadits=input()
    
   
    if 'I' in ievadits:
        n=int(input())
        parents=list(map(int,input().split()))
        print(compute_height(n,parents))
    elif 'F'in ievadits:
        fails=input()
        fails=("test/"+fails)
        if 'a'not in fails:
            with open(fails,'r')as f:
                print(f.read())
    
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
