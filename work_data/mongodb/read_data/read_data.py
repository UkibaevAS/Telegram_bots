from work_data.mongodb.database_access import col


async def read_data(data: dict[str, str]):
    return col.find(data)


async def check_len(data) -> int:
    return len(data)
