#!/usr/bin/env python3
"""
Task: Working with Redis
"""
import redis
from typing import Union


class Cache:
    def __init__(self, host='localhost', port=6379, db=0):
        self._redis = redis.Redis(host=host, port=port, db=db)
    
    def store(self, value: Union[str, bytes, int]) -> str:
        key = self._redis.incr('cache:key-counter')
        self._redis.set(f'cache:key-{key}', value)
        return str(key)
    
    def get(self, key: str, fn: Optional[Callable[[bytes], any]] = None) -> Union[str, bytes, int, None]:
        value = self._redis.get(f'cache:key-{key}')
        if value is None:
            return None
        if fn is not None:
            value = fn(value)
        return value
    
    def get_str(self, key: str) -> Union[str, None]:
        return self.get(key, fn=lambda x: x.decode('utf-8'))
    
    def get_int(self, key: str) -> Union[int, None]:
        return self.get(key, fn=lambda x: int(x))
