#function for uncompressed str to compressed one
def compress(uncompressed:str)->str:
    # if empty return empty str
    if not uncompressed:
        return ""
    #now here we placed the first index of str for further comparing 
    current_char=uncompressed[0]
    # for counting if loop condition is met
    count = 1
    #create a empty list for storing result
    compressed=[]
    
    #now loop with condition
    for i in range(1,len(uncompressed)):
        if uncompressed[i] == current_char:
            count +=1
        else:
            
            result=compressed.append(f"{current_char}{count}")
            current_char=uncompressed[i]
            count=1
            
    compressed.append(f"{current_char}{count}")
    result= "".join(compressed)

    return result if len(result) < len(uncompressed) else  uncompressed

if __name__ == "__main__":
    test_strings = ["aabcccccaaa", "abcd", "WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWW"]
    for text in test_strings:
          compressed_text = compress(text)
          print(f"Original  ({len(text)} chars) : {text}")
          print(f"Compressed ({len(compressed_text)} chars): {compressed_text}\n")
  