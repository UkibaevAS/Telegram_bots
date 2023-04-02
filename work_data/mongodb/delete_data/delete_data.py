from work_data.mongodb.database_access import col


async def delete_data(text: str, data) -> bool:
    for i_rec in data:
        if text in i_rec.values():
            col.delete_one(i_rec)
            return True
    return False
