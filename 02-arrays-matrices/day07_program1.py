#time complexity O(n+m)
#space complexity O(1)

def merge_sorted_array(num1:list[int],m:int,num2:list[int],n:int):
    #m is a total real numbers
    #n total numbers
    #tecnique three pointer tech
    p1=m - 1
    p2=n -1
    p= m + n -1
    
    #condition end till negative values
    while p1 >= 0 and p2 >= 0 :
        if num1[p1] > num2[p2] :
            num1[p] = num1[p1]
            p1 -= 1
        else:
            num1[p]=num2[p2]
            p2 -= 1
            
        #p always decrese by 1 in both condition
        p -= 1
        
    while p2 >= 0:
        num1[p]=num2[p2]
        p -= 1
        p2 -= 1
            
    return num1

if __name__ =="__main__":
    arr1=[3,4,5,9,0,0]
    m=4
    arr2=[1,2]
    
    n=2
    result=merge_sorted_array(arr1,m,arr2,n)
    
    print(f"Merged_sorted_array:{result}")
    