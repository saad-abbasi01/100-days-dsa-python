#time complexity here is O(n)because same input as same steps
#space complexity here is O(1) cause not any auxilary space or another list

#function for separating zeros
def separating_zeros(num:list[int])->list[int]:
    #for collection of zeros
    slow=0
    
    #loop for checking one by one
    for fast in range(len(num)):
        if num[fast] != 0:
            num[slow],num[fast]= num[fast],num[slow]
            slow += 1
            
    return num
    #testing unit
if __name__ =="__main__":
    api_list=[0,320,0,45,676,0,7,5,6,7,8]
    
    print(f"Raw material:{api_list}")
    result=separating_zeros(api_list)
    print(f"After separation :{result}")