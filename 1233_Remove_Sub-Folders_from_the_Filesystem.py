def removeSubfolders():
    folders = ["/a","/a/b","/c/d","/c/d/e","/c/f"]
    folder_set = set(folders)
    result = []
    
    for folder in folders:
        is_a_sub_folder = False
        prefix = folder
        
        while not prefix == "":
            pos = prefix.rfind("/")
            if pos == -1:
                break
            
            prefix = prefix[0:pos]
            if prefix in folder_set:
                is_a_sub_folder = True
                break
        
        if not is_a_sub_folder:
            result.append(folder)
    return result
    
result = removeSubfolders()
print(result)