from pydantic import BaseModel


class Base(BaseModel):
    name: str

    def __str__(self):
        # info = ', '.join(self.name)
        return f'<{self.__class__.__name__} "{self.name}">'