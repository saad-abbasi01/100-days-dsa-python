#time complexity O(n)one list
#space complexity O(1)

def max_subarray_of_array(nums:list[int])->dict[int]:
    max_subarray_index=nums[0]
    current_max=nums[0]
    
    start=end=temp_start=0
    
    for i in range(1,len(nums)):
        if nums[i] > current_max + nums[i]:
            current_max=nums[i]
            temp_start=i
            
        else:
            current_max += nums[i]
            
        if current_max > max_subarray_index:
            max_subarray_index=current_max
            start=temp_start
            end= i
    return {
        "max_sum":max_subarray_index,
        "subarray":nums[start:end+1],
        "starting_point":start,
        "Ending_point":end
    }
    
if __name__=="__main__":
    list=[4,1,-10,3,4,5,6,7,8,-1]
    result=max_subarray_of_array(list)
    print(f"Max_subarray:{result['max_sum']}")
    print(f"Max subarray:{result['subarray']} starting_point:{result['starting_point']} Ending_point:{result['Ending_point']}")