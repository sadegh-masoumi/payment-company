from typing import Union

from pymongo import MongoClient, database, typings
from django.conf import settings


class Database:
    clients = {}

    def __new__(cls, *args, **kwargs):
        if not kwargs.get("db_name", None):
            kwargs["db_name"] = getattr(settings, "DATABASES")["mongodb"]["NAME"]
        if not kwargs.get("host", None):
            kwargs["host"] = getattr(settings, "DATABASES")["mongodb"]["HOST"]
        if not kwargs.get("port", None):
            kwargs["port"] = getattr(settings, "DATABASES")["mongodb"]["PORT"]
        if not kwargs.get("username", None):
            kwargs["username"] = getattr(settings, "DATABASES")["mongodb"]["USERNAME"]
        if not kwargs.get("password", None):
            kwargs["password"] = getattr(settings, "DATABASES")["mongodb"]["PASSWORD"]

        url = "mongodb://{username}:{password}@{host}:{port}/{db_name}?".format(**kwargs)

        if Database.clients.get(url, None):
            return Database.clients.get(url)

        obj = super(Database, cls).__new__(cls)
        Database.clients[url] = obj
        return obj

    def __init__(
            self,
            db_name: Union[str, None] = None,
            host: Union[str, None] = None,
            port: Union[int, None] = None,
            username: Union[str, None] = None,
            password: Union[str, None] = None,
            **kwargs
    ):

        if db_name is None:
            db_name = getattr(settings, "DATABASES")["mongodb"]["NAME"]
        if host is None:
            host = getattr(settings, "DATABASES")["mongodb"]["HOST"]
        if port is None:
            port = getattr(settings, "DATABASES")["mongodb"]["PORT"]
        if username is None:
            username = getattr(settings, "DATABASES")["mongodb"]["USERNAME"]
        if password is None:
            password = getattr(settings, "DATABASES")["mongodb"]["PASSWORD"]

        client = MongoClient(
            host=host, port=int(port), username=username, password=password
        )
        db = client[db_name]
        url = f"mongodb://{username}:{password}@{host}:{port}/{db_name}?"
        self.clients[url] = db
        self.url = url

    def get_db(self) -> database.Database:
        return self.clients[self.url]
