class EdgeData:
    def __init__(self, src: int = None, dest: int = None, weight: float = None):
        self.src = src
        self.dest = dest
        self.weight = weight

    def __repr__(self):
        return '{"src" =%d,"dest"=%d, "wight"=%s}' % (self.src, self.dest, self.weight)

    """
    Return the EdgeData src
    """
    def get_src(self):
        return self.src

    """
    Return EdgeData dest
    """
    def get_dest(self):
        dest = self.dest
        return dest

    """
    Return the EdgeData src
    """
    def get_weight(self):
        weight = self.weight
        return weight

    """
    Set the EdgeData weight 
    """
    def set_weight(self, weight):
        self.weight = weight

    """
    Set the EdgeData src
    """
    def set_src(self, src):
        self.src = src

    """
    Set EdgeData dest
    """
    def set_dest(self, dest):
        self.dest = dest
