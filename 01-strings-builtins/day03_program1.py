import re

def extract_tags(content:str)->list[str]:
    
    #we have a pattern first
    pattern=r'#\w+'
    
    #now themain thing is how we find all 
    #using our pattern to find from the content
    raw_tags=re.findall(pattern,content)
    
    #now we have to convert it  into set (unordered,No duplicates)
    unique_tags={tag.lower() for tag in raw_tags}
    
    #sorted Unordered set
    return sorted(list(unique_tags))

if __name__ == "__main__":
    sample_text="""Building modern web apps with #Python and #FastAPI is fast and efficient! 
    Check out our new tutorial on #Python backend services and #WebDev tips. 
    Follow for more #python and #coding updates!
    """
    
    tags=extract_tags(sample_text)
    print(f"Extracted Tags {len(tags)} unique : {tags}")
    