def contar(): 
    return (x for x in range(1,11))
    
for n in contar(): 
    print(n)


# Yield version 

def count(): 
    for x in range(1,11): 
        yield x 
    
for n in count(): 
    print(n)


print("\n")

def pares(): 
    for x in range(1,21): 
        if x % 2 == 0: 
            yield x 

for n in pares(): 
    print(n) 