def length_of_longest_substring(s:str)->dict:
    char_map={}
    max_length=0
    left=0
    best_start=0
    
    for right,char in enumerate(s):
        if char in char_map and char_map[char] >= left:
            left=char_map[char] + 1
        
        char_map[char]=right
        
        current_max_length=right -left + 1
        if current_max_length > max_length:
            max_length=current_max_length
            best_start=left
            
    longest_substring=s[best_start:best_start + max_length]
        
    return{
            "String":s,
            "Substring":longest_substring
        }
        
if __name__=="__main__":
    str_text=["abdbjnkmhkbj","sbjcbjc"]
    
    for text in str_text:
        result_str=length_of_longest_substring(text)
        print(f"Original_str:{text} and Sub_str:{result_str}")     