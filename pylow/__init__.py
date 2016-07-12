from fn.underscore import _Callable
from fn import _
import inspect

def get_type(cls, attr):
    try:
        return [a.kind for a in inspect.classify_class_attrs(cls) if a.name == attr][0]
    except IndexError:
        return None

# symbol object
# is the representnation of a name --------------------------------------------
class Symbol(_Callable):
    def __call__(self, x):
        if not isinstance(self._callback, tuple):
            return self._callback(x)

        f, left, right = self._callback
        return f(left(x), right(x))

    def __str__(self):
        """Build readable representation for function
        (_ < 7): (x1) => (x1 < 7)
        (_ + _*10): (x1, x2) => (x1 + (x2*10))
        """
        # args iterator with produce infinite sequence
        # args -> (x1, x2, x3, ...)
        l, r = [], self._format
        # replace all "_" signs from left to right side
        l = ["x"] * r.count("_")
        r = r.replace("_", "x")

        r = r % self._format_args
        return "({left}) => {right}".format(left=", ".join(l), right=r)

# curry object ----------------------------------------------------------------
# wrap function
#   make position args default to symbol
#   if arguments are symbol, defer but partial others
def curry(f):
    pos_args = inspect.getargspect(f).args
    def wrapper(*args, **kwargs):
        for arg in args:
            pass


def tapply():
    pass

#tapply(range(6), ['a']*3 + ['b']*3, mean(X))


