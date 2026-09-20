def reverse_list(num:list,start:int,end:int)->None:
    #we having a loop taht we used fir start the integer list until end
    
    while start < end:
        num[start],num[end] == num[end],num[start]
        start += 1
        end -= 1
        
def rotate_array(list:list,k:int):
    if not list:
        return []
    
    n=len(list)
    k=k % n
    #reverse the list 
    reverse_list(list,0,n-1)
    # reverse the k elements
    reverse_list(list,0,k-1)
    #reverse the remainig k element
    reverse_list(list,k,n-1)
    return list
#testing unit
if __name__== "__main__":
    num_list=[1,2,3,4,5,6,7,8,9]
    shift=3
result=rotate_array(num_list,shift)        
print(f"The Rotating list result:{result}")