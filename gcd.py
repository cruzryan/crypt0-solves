#Eucledian Algorithm

def gcd(a,b, num=None):
    nln = 0
    ln = a if a < b else b
    bn = a if a > b else b
    
    while bn > ln:
        nln += 1
        bn = bn - ln

    print(bn,ln)
    if bn == ln: 
        return bn
    else:
        gcd(bn, ln)

print(gcd(66528,52920))