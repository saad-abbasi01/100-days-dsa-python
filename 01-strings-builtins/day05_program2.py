def build_lps_pattern_cheatcode(pattern:str)->list[int]:
    lps=[0] * len(pattern)
    length=0
    i=1
    #loop for start pattern reading
    while i < len(pattern):
        #condition only for match characters
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            #all things right now increment in loop
            i +=1
        else:
            if length != 0:
                length=lps[length - 1] #thats falling  apart or called teal point
            else:
                lps[i]=0
                i += 1
    #return lps for further kmp operation.....  
    return lps

def kmp_technique_of_str(text:str,pattern:str)->list[int]:
    
    if not pattern or not text:
        return []
    
    #lps calling
    lps=build_lps_pattern_cheatcode(pattern)
    matches=[]
    i=0
    j=0
    #now loop for match and mismatch
    while i < len(text):
        #now the condition for match first
        if pattern[j] == text[i]:
            i += 1
            j +=1
        # if len complete 
        if j ==len(pattern):
            matches.append(i-j)
            j=lps[j-1]
            
        elif i <= len(pattern) and pattern[j] != text[i]:
            if j != 0:
                j=lps[j-1]
            else:
                i += 1
    return matches
#testing unit...........
if __name__ =="__main__":
    text="ABABDABACDABABCABAB"
    search="ABABCABAB"
    found_indices=kmp_technique_of_str(text,search)
    print(f"Text for Kmp:{text}")
    print(f"Pattern for Kmp:{search}")
    print(f"Found the indices :{found_indices}")
            
        
    
        
    