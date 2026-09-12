def is_anagram(s1:str,s2:str)->bool:
    #first we have to change s1& s2 int str1 $ str2 for further processing in this program
    str1="".join(char.lower() for char in s1 if char.isalnum())
    str2="".join(char.lower() for char in s2 if char.isalnum())
    
    # check the len both str is it equal or not if not then return bool false
    if len(str1) != len(str2):
        return False
    
    # now make str1 dict
    counts={}
    for char in str1:
        counts[char]=counts.get(char,0) + 1
        
    # now check anagram using str2
    for  char in str2:
        if char not in counts or counts[char]==0:
            return False
        counts[char] =-1
        return True
    
if __name__ == "__main__":
    pairs=[
        ("listen","silent"),
        ('Triangle',"integral")
        
    ] 
    for word1 , word2 in pairs:
        result=is_anagram(word1,word2)
        print(f"{word1}&{word2} ->Anagram:{result} ")
        