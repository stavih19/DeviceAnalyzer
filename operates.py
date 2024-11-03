import Range
from utilities import get_range

# operate class interface
class Component:
    def __init__(self, name, val, pattern):
        # name of the component
        self.name = name
        # value of the component (defalut)
        self.val = val
        # pattern of the component for search in lines file
        self.pattern = pattern

    # search the operate on the file
    def extract(self, file):
        return 0

    # save it, can be memory or dick
    def save(self, val):
        self.val = val
    
    # check if the component is valid by given parameters
    def check_if_valid(self, val):
        return self.val == val


# define component as two numbers that represent a range
class Range_Component(Component):
    def __init__(self, name, val, pattern):
        super().__init__(name, val, pattern)
        self.name = name
        self.val = val
        self.pattern = pattern

    def extract(self, file):
        min_val, max_val = get_range(file, self.pattern)
        if min_val is None or max_val is None:
            val = Range.Range(min_val, max_val)
        else:
            val = Range.Range(float(min_val), float(max_val))

        return val

    def save(self, val):
        self.val = val
    
    def check_if_valid(self, val):
        if self.val.min is None or self.val.max is None:
            return False
        return self.val.min <= val and val <= self.val.max
    
    def __str__(self) -> str:
        return str(self.name) + ": " + str(self.val)
    