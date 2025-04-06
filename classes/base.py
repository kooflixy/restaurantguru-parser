from pydantic import BaseModel


class Base(BaseModel):
    name: str
    labels: dict = {}

    def __str__(self):
        return f'<{self.__class__.__name__} "{self.name}">'
    
    def model_dump(self, *, mode = 'python', include = None, exclude = None, context = None, by_alias = None, exclude_unset = False, exclude_defaults = False, exclude_none = False, round_trip = False, warnings = True, fallback = None, serialize_as_any = False):
        exclude = ['labels']
        dict = super().model_dump(mode=mode, include=include, exclude=exclude, context=context, by_alias=by_alias, exclude_unset=exclude_unset, exclude_defaults=exclude_defaults, exclude_none=exclude_none, round_trip=round_trip, warnings=warnings, fallback=fallback, serialize_as_any=serialize_as_any)
        for label in self.labels:
            if label in dict:
                dict[self.labels[label]] = dict.pop(label)
        return dict