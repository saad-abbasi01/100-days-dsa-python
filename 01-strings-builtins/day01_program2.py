import re

def count_word_frequency(text:str)->dict[str,int]:
    
    words=re.findall(r'\b\w+\b',text.lower())
    
    frequency_map={}
    for word in words:
        frequency_map[word]=frequency_map.get(word,0) + 1
        
    return frequency_map
    
#min program here for testing
if __name__ =="__main__":
    
    sample_text="This is a sample text. This text is for testing the word frequency counter."
    word_counts=count_word_frequency(sample_text)
    sorted=dict(sorted(word_counts.items(),key=lambda x:x[1],reverse=True))
    
    for word ,count in sorted.items():
        print(f"{word}:{count}")