class agentData:

    def __init__(self, id: int = None, value: float = None, src: int = None, dest: int = None, speed: float = None,
                 pos: tuple = None):
        self.id = id
        self.value = value
        self.src = src
        self.dest = dest
        self.speed = speed
        self.pos = pos

    def __repr__(self):
        return 'Agent %d{"value="%d, "src="%d, "dest="%d, "speed="%d, "pos="%s}' \
               % (self.id, self.value, self.src, self.dest, self.speed, self.pos)

    """
    Return the AgentData id
    """

    def get_id(self):
        return self.id

    """
    Set the AgentData id 
    """

    def set_id(self, id):
        self.id = id

    """
    Return the AgentData value
    """

    def get_value(self):
        return self.value

    """
    Set AgentData value
    """

    def set_value(self, value):
        self.value = value

    """
    Return AgentData src
    """

    def get_src(self):
        return self.src

    """
    Set AgentData src
    """

    def set_src(self, src):
        self.src = src

    """
    Return the AgentData dest  
    """

    def get_dest(self):
        return self.dest

    """
    Set the AgentData dest
    """

    def set_dest(self, dest):
        self.dest = dest

    """
       Return the AgentData speed  
    """

    def get_speed(self):
        return self.speed

    """
    Set the AgentData speed
    """

    def set_speed(self, speed):
        self.speed = speed

    """
    Return the AgentData position (tuple)
    """

    def get_pos(self):
        pos = self.pos
        return pos

    """
    Set the AgentData position (tuple)
    """

    def set_pos(self, pos):
        self.pos = pos
