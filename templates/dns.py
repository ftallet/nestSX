# create DNS entries for lab 1-9, and potential hosts 1-9
maxn=3
maxi=5
domain="wood.lab"
prefix='172.22.'
subnet='172.22.1'
for n in range(1,maxn+1):
    base = 50 + 20 * (n-1)
    print(f'add address={subnet}.{base+1} name=vcsa{n}.{domain}')
    print(f'add address={subnet}.{base+2} name=vcsa{n}2.{domain}')
    print(f'add address={subnet}.{base+3} name=nsxm{n}.{domain}')
    print(f'add address={subnet}.{base+4} name=nsxm{n}2.{domain}')
    print(f'add address={subnet}.{base+5} name=nsxm{n}3.{domain}')
    print(f'add address={subnet}.{base+6} name=edge{n}1.{domain}')
    print(f'add address={subnet}.{base+7} name=edge{n}2.{domain}')
    print(f'add address={subnet}.{base+8} name=edge{n}3.{domain}')
    print(f'add address={subnet}.{base+9} name=edge{n}4.{domain}')
    for i in range(0,10):
        print(f'add address={subnet}.{base+10+i} name=esxi{n}{i}.{domain}')
        