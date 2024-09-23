
list = [0,1]

def fibonnaci(n):
    for i in range(0,n-2):
        append = list[i] + list[i+1]
        list.append(append)
    return list

print(fibonnaci(5))
print(fibonnaci(10))


        
