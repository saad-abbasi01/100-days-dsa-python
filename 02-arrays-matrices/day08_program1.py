#time complexity is we having  two loops thats O(n+n)-->O(2n)constant-->O(n)
#space complexity O(1)cause same list not any new things or list

def product_except_self(num:list[int])->list[int]:
    #first the main thing is here having same slots in output as we have in list of num
    n=len(num)
    output=[1] * len(num)
    #now the loop for prefix (left to right)
    prefix=1
    for i in range(n):
        output[i]=prefix
        prefix *= num[i]
    #second loop for suffix(right to left)
    suffix=1
    for i in range(n-1,-1,-1):
        output[i] *= suffix
        suffix *= num[i]
        
    return output

if __name__ =="__main__":
    list=[1,2,3,4]
    
    result=product_except_self(list)
    
    print(f"Original list:{list}")
    print(f"Product except self list :{result}")