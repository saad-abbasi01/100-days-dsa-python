def flatten_dict(d:dict,parent_key:str="",sep:str='.')->list:
    
    #first create a empty list for storing results
    items=[]
    #loop for seperating the key and value
    for key,value in d.items():
        new_key=f"{parent_key}{sep}{key}" if parent_key else str(key)
        # for recursive (minor loop until value-->dict)
        if isinstance(value,dict):
            items.extend(flatten_dict(value,new_key,sep=sep).items())
        else:
            items.append((new_key,value))
            
    return dict(items)
#testing unit
if __name__ =="__main__":
     nested_config = {
        "user": {
            "profile": {
                "name": "Alice",
                "age": 28
            },
            "roles": ["admin", "editor"]
        },
        "version": "1.0.0"
    }
     flattend=flatten_dict(nested_config)
     print("Flattend_dict with Dot(.) Notation")
     # use this function to ransfer into key and value
     for k,v in flattend.items():
         print(f"->{k}:{v}")