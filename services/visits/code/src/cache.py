import redis
import pydantic
from typing import Type

class Cache:
    def __init__(self, connection_write: str = None, connection_read: str = None) -> None:
        self.connection_write = connection_write
        self.connection_read = connection_read
        self.connect()

    def connect(self):
        try:
            self.read = redis.from_url(self.connection_read)
            self.write = redis.from_url(self.connection_write)
        except Exception as e:
            print(f"Error connecting to cache: {e}")

    def get(self, key: str, model: Type[pydantic.BaseModel]):
        try:
            value = self.read.get(key)
            if value:
                return model.model_validate_json(value)
        except Exception as e:
            print(f"Error getting value from cache: {e}")
        return None

    def set(self, key: str, value: pydantic.BaseModel):
        try:
            self.write.set(key, value.model_dump_json())
        except Exception as e:
            print(f"Error setting value in cache: {e}")
