class pokemonData:
    def __init__(self, value: float = None, type: int = None, pos: tuple = None):
        self.value = value
        self.type = type
        self.pos = pos

    def __repr__(self):
        return '{"value="%d, "type="%d, "pos="%s}' \
               % (self.value, self.type, self.pos)

    """
    Return the pokemonData value
    """

    def get_value(self):
        return self.value

    """
    Set pokemonData value
    """

    def set_value(self, value):
        self.value = value

    """
    Return the pokemonData type
    """

    def get_type(self):
        return self.type

    """
    Set the pokemonData type 
    """

    def set_type(self, type):
        self.type = type

    """
    Return the pokemonData position (tuple)
    """

    def get_pos(self):
        pos = self.pos
        return pos

    """
    Set the pokemonData position (tuple)
    """

    def set_pos(self, pos):
        self.pos = pos

