#schema helps to cerealize and also convert mongodb format.json to our ui needed json

def studentEntity(db_item) -> dict:
    return {
        "id": str(db_item["_id"]),
        "name": db_item["student_name"],
        "email": db_item["student_email"],
        "phone": db_item["student_phone"]
    }

def listOfStudentEntity(db_item_list) -> list:
    listStudent_entity = []
    for item in db_item_list:
        listStudent_entity.append(studentEntity(item))

    return listStudent_entity