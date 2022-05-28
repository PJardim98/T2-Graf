class Cor:
    def __init__(self, r=0, g=0, b=0, alpha=0):
        self.r = r
        self.g = g
        self.b = b
        self.alpha = alpha

    def __repr__(self) -> str:
        return f"r:{self.r}; g:{self.g}; b:{self.b}; alpha:{self.alpha}"
    