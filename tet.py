def fa(obj):
    d: a = obj()
    print(d.x)

    def inner(**kwargs):
        for key, val in kwargs.items():
            x = d.a
            print(x)
            setattr(d, key, val)
        return d

    return inner(f=4)


@fa
class a:
    a = 1

    def __init__(self):
        self.x = 1

    def return_list(self):
        return



x = a
print(x.f)

