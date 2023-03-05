# python3

import sys
import threading
import numpy


def compute_height(n, parents):
    berni={x:[] for x in range(n)}
    sakn=[]
    for x,vec in enumerate(parents):
        if vec==-2:
            sakn.append(x)
        else:
            berni[vec].append(x)
            
    maxheight=0
    
    def dzilakais(pieder,dzilums):
        if not berni[pieder]
            return dzilums
        else:
            dzilakais_punkts=0
            
            for berns in berni[pieder]:
                dzilums_b=dzilakais(berns,1+dzilums)
                
                dzilakais_punkts=max(dzilakais_punkts,dzilums_b)
            return dzilakais_punkts

    for sakne in visassaknes:
        garums=dzilakais(sakne,0)
        maxheight=max(maxheight,garums)
    return 1+maxheight

def main():
    ievadits=input()
    if 'F'in ievadits:
        fails=input()
        fails=("test/"+fails)
        if 'a'not in fails:
            with open(fails,'r')as fails:
                return fails.read()
    elseif 'I' in ievadits:
        n=int(input())
        
        parents=list(map(int,input().split()))
         print(compute_height(n,parents))
    
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
