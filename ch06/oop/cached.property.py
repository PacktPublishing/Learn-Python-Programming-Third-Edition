# oop/cached.property.py
from functools import cached_property


class Client:
    def __init__(self):
        print("Setting up the client...")

    def query(self, **kwargs):
        print(f"Performing a query: {kwargs}")


class Manager:
    @property
    def client(self):
        return Client()

    def perform_query(self, **kwargs):
        return self.client.query(**kwargs)


class ManualCacheManager:
    @property
    def client(self):
        if not hasattr(self, '_client'):
            self._client = Client()
        return self._client

    def perform_query(self, **kwargs):
        return self.client.query(**kwargs)


class CachedPropertyManager:
    @cached_property
    def client(self):
        return Client()

    def perform_query(self, **kwargs):
        return self.client.query(**kwargs)


manager = CachedPropertyManager()
manager.perform_query(object_id=42)
manager.perform_query(name_ilike='%Python%')

del manager.client  # This causes a new Client on next call
manager.perform_query(age_gte=18)


"""
$ python cached.property.py
Setting up the client...                         # New Client
Performing a query: {'object_id': 42}            # first query
Performing a query: {'name_ilike': '%Python%'}   # second query
Setting up the client...                         # Another Client
Performing a query: {'age_gte': 18}              # Third query
"""
