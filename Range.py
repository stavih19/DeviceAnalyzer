# define Range class for make easy working
class Range:
    def __init__(self, min, max):
        self.min = min
        self.max = max

    def get(self):
        return [self.min, self.max]
    
    def is_equal(self, other):
        return self.min == other.min and self.max == other.max
    
    def __str__(self) -> str:
        return "Min: " + str(self.min) + ", Max: " + str(self.max)