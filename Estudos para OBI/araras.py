n,m = map(int, input().split())
gaiolas_necessarias = 1 + (n-1)*5

if gaiolas_necessarias <= m:
    print("S")
else:
    print("N")

