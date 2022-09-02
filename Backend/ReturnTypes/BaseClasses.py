from functools import wraps
from pprint import pprint


class ReturnTypeBase:
    class _BaseClassCallException(Exception):
        pass

    @staticmethod
    def check_call(f):
        @wraps(f)
        def wrapper(self, *args, **kwargs):
            if self.__class__.__name__ == "BaseClass":
                raise self._BaseClassCallException("BaseClass should not be called")

            return f(self, *args, **kwargs)

        return wrapper

    @check_call
    def to_json(self) -> dict:
        all_attributes = self.__dict__
        json_data = all_attributes | {"type": self.__class__.__name__}
        return json_data

    @check_call
    def debug_json(self):
        pprint(self.to_json())

    @staticmethod
    @check_call
    def format_source(source_name: str, source_url: str):
        return {
            "name": source_name,
            "url": source_url
        }
