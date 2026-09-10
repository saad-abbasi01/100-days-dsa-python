def is_palindrome(input_str:str)->dict:

    cleaned="".join(char.lower() for char in input_str if char.isalnum())
    # now reversed the string
    reversed=cleaned[::-1]
    # now check is it plaindrome or not
    is_same = cleaned == reversed
    return{
    
    "input": input_str,
    "cleaned": cleaned, 
    "reversed": reversed,
    "is_same": is_same
    }

if __name__ =="__name__":
    text=["A man, a plan, a canal: Panama",
            "race a car",
          "No lemon, no melon",
          "Was it a car or a cat I saw?",]

for t in text:
    result=is_palindrome(t)
    print(f"Input: {result['input']}")
    print(f"Cleaned: {result['cleaned']}")
    print(f"Reversed: {result['reversed']}")
    print(f"Is Palindrome: {result['is_same']}")
    print("-"*30)