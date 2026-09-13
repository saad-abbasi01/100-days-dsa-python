def two_sum(nums:list,target:int)->list[int]:
    
    #first we have to create te empty dict for temperary storage
    seen={}
    
    #loop to check all the integers of  list one by one and also stored for further checking
    for index,num in enumerate(nums):
        complement=target - num
        if complement in seen:
            return [seen[complement],index]
        seen[num]=index
    
    return []
#testing point
if __name__ =="__main__":
    prices=[10,20,25,45,50,75]
    target=70
    solve=two_sum(prices,target)
    # first show data and target
    print(f"Dataset {prices} to target {target}")
    #condition
    if solve:
        print(f"Found at {solve} at {prices[solve[0]]} + {prices[solve[1]] }= {target}")
    else:
        print("Match not found!!!")