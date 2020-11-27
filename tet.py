from typing import ClassVar


def add_attribute(**kwargs):
    def inner(obj: ClassVar):
        for i, j in kwargs.items():
            setattr(obj, i, j)
        return obj

    return inner


@add_attribute(name='Me', values=1)
class A:
    static = 1

    def __init__(self):
        pass

    @property
    def x(self):
        print(A.static)


a = A()
print(a.name, a.values)
a.x
