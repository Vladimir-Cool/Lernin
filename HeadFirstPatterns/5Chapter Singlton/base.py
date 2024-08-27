from typing import ClassVar


class Singleton:
    _instance: ClassVar["Singleton"] = None

    def __init__(self):
        pass

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
