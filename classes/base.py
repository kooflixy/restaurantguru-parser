from pydantic import BaseModel


class Base(BaseModel):
    name: str

    def __str__(self):
        return f'<{self.__class__.__name__} "{self.name}">'