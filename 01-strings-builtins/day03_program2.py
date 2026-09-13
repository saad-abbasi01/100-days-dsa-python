def paginate_list(items:list,page:int,page_size:int)->dict:
    # first condition hre
    if page < 1 and page_size < 1:
        raise ValueError 
    
    total_items=len(items)
    total_pages= (total_items + page_size -1) //page_size if total_items > 0 else 0

    #start and end index
    start_index=(page - 1) * page_size
    end_index=start_index + page_size
    
    page_data=items[start_index : end_index]
    
    return {
        "page":page,
        "page_size":page_size,
        "total_items":total_items,
        "total_pages":total_pages,
        "has_next":page < total_pages,
        "has_pre": page > 1,
        "data":page_data
    }
if __name__ =="__main__":
    users=[f"User_{i}" for i in range(1,26)]
    response=paginate_list(users,page=3,page_size=10)
    
    print("API pagination response")
    print(f" -> Current Page: {response['page']} of {response['total_pages']}")
    print(f" -> Has Next: {response['has_next']} | Has Prev: {response['has_pre']}")
    print(f" -> Data: {response['data']}")