#time complexity constraints O(n) the pointers help us to achive optimal complexity
#space complexity O(1)  auxilary space same list modified form

def pointer_technique(heights:list[int])->dict:
    #having two pointers here for starting and ending
    left=0
    right=len(heights) - 1
    max_water=0
    best_left=left
    best_right=right
    #now loop for comparing from both sides
    
    while left < right:
        
        #we have to find the total best weight 
        width=right - left
        h=min(heights[left],heights[right])
        #current maximum for further operations
        current_water=h * width
        #condition till ending
        if current_water > max_water:
            max_water = current_water
            best_left=left
            best_right=right
            
        if heights[left] < heights[right]:
            left += 1
        else:
            right -= 1
            
    return {
        
        "max_water":max_water,
        "left_index":best_left,
        "right_index":best_right,
        "left_height":heights[best_left],
        "right_height":heights[best_right]
    }
#testing unit
if __name__ =="__main__":
    list=[1,8,3,4,5,6,7,8,9,2,2,3]
    #function calling
    result=pointer_technique(list)
    print(f"->Max_Area:{result['max_water']}")
    print(f"->Left Index:{result['left_index']} Left height:(H={result['left_height']}) Right Index:{result['right_index']} Right Height:(H={result['right_height']})")