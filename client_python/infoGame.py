import My_Graph.GraphAlgo
import My_Graph.DiGraph


class infoGame:
    def __init__(self, pokemons: int = None, is_logged_in: bool = None, moves: int = None, grade: int = None,
                 game_level: int = None, max_user_level: int = None, id: int = None, agents: int = None):
        self.pokemons = pokemons
        self.is_logged_in = is_logged_in
        self.moves = moves
        self.grade = grade
        self.game_level = game_level
        self.max_user_level = max_user_level
        self.id = id
        self.agents = agents

    """
    Return the infoGame pokemons
    """

    def get_pokemons(self):
        return self.pokemons

    """
    Set the infoGame pokemons 
    """

    def set_pokemons(self, pokemons):
        self.pokemons = pokemons

    """
    Return the infoGame is_logged_in
    """

    def get_is_logged_in(self):
        return self.is_logged_in

    """
    Set infoGame is_logged_in
    """

    def set_is_logged_in(self, is_logged_in):
        self.is_logged_in = is_logged_in

    """
    Return infoGame moves
    """

    def get_moves(self):
        return self.moves

    """
    Set infoGame moves
    """

    def set_moves(self, moves):
        self.moves = moves

    """
    Return the infoGame grade  
    """

    def get_grade(self):
        return self.grade

    """
    Set the infoGame grade
    """

    def set_grade(self, grade):
        self.grade = grade

    """
    Return the infoGame game_level
    """

    def get_game_level(self):
        return self.game_level

    """
    Set the infoGame game_level
    """

    def set_game_level(self, game_level):
        self.game_level = game_level

    """
    Return the infoGame max_user_level
    """

    def get_max_user_level(self):
        return self.max_user_level

    """
    Set the infoGame max_user_level
    """

    def set_max_user_level(self, max_user_level):
        self.max_user_level = max_user_level

    """
    Return the infoGame id
    """

    def id(self):
        return self.id

    """
    Set infoGame id
    """

    def set_id(self, id):
        self.id = id

    """
    Return infoGame agents
    """

    def get_agents(self):
        return self.agents

    """
    Set infoGame agents
    """

    def set_agents(self, agents):
        self.agents = agents
