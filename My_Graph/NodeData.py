class NodeData:
    def __init__(self, key: int = None, info: str = None, tag: float = None, pos: tuple = None, weight: float = None):
        self.key = key
        self.pos = pos
        self.info = info
        self.tag = tag
        self.weight = weight

    def __repr__(self):
        return '{"id" =%d,"pos"=%s}' % (self.key, self.pos)

    """
    Return the NodeData key
    """

    def get_key(self):
        key = self.key
        return key


    """
    Set the NodeData key (node_id)
    """

    def set_key(self, key):
        self.key = key

    """
    Return the NodeData info
    """

    def get_info(self):
        return self.info

    """
    Set NodeData info
    """

    def set_info(self, info):
        self.info = info

    """
    Return NodeData tag
    """

    def get_tag(self):
        return self.tag

    """
    Set NodeData tag
    """

    def set_tag(self, tag):
        self.tag = tag

    """
    Return the NodeData weight  
    """

    def get_weight(self):
        return self.weight

    """
    Set the NodeData wight
    """

    def set_weight(self, wight):
        self.weight = wight

    """
    Return the NodeData position (tuple)
    """

    def get_pos(self):
        pos = self.pos
        return pos

    """
    Set the node position
    """

    def set_pos(self, pos):
        self.pos = pos
