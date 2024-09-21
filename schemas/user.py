def userentity(item) -> dict:
    return {
        "id":str(item["_id"]),
        "name":item["name"],
        "email": item["email"],
        "password":item["password"]
    }
    
def userEntity(entity) -> list:
    return [userEntity(item) for item in entity]