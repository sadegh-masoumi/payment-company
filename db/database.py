from pymongo import MongoClient


def get_db_handle(db_name: str, host: str, port: int, username: str, password: str):
    client = MongoClient(
        host=host, port=int(port), username=username, password=password
    )
    db_handle = client[db_name]
    return db_handle, client
