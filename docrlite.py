#OoO;;
from sys import argv as a;o=open
def f(c):
    l=c.split('\n');s=l.pop(0)[2];l=list(map((lambda x:int(x[0])+'|'+'|'.join(x[1:]).replace(s,' ')), l.split('|')));r,n='',1
    for i,j in l:
        if n!=i:n,r=i,r+'\n'
        r+=j
    return r
c = lambda x,y:o(y,'w').write(f(o(x).read()));m = lambda :c(*a[1:])
if __name__=="__main__":m()
