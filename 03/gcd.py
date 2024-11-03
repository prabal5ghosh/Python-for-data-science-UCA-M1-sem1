class Contract:
    @classmethod
    def check(cls, value):
        pass

class Typed(Contract):
    _type = None

    @classmethod
    def check(cls, value):
        assert isinstance(value, cls._type), f"Expected {cls._type}"
        super().check(value)


class Integer(Typed):
    _type = int

class Float(Typed):
    _type = float

class String(Typed):
    _type = str


class Positive(Contract):
    @classmethod
    def check(cls, value):
        assert value > 0, "Must be > 0"
        super().check(value)


class Nonempty(Contract):
    @classmethod
    def check(cls, value):
        assert len(value) > 0, "Must be nonempty"
        super().check(value)

class PositiveInteger(Integer, Positive):
    pass


from inspect import signature
from functools import wraps

def checked(func):
    sig = signature(func)
    ann = func.__annotations__
    @wraps(func)
    def wrapper(*args, **kwargs):
        bound = sig.bind(*args, **kwargs)
        for name, val in bound.arguments.items():
            if name in ann:
                ann[name].check(val)
        return func(*args, **kwargs)
    return wrapper


@checked
def gcd(a: PositiveInteger, b: PositiveInteger):
    while b:
        a, b = b, a % b
    return a
