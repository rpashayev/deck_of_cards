class Player:
    
    point_increment = 10
    players = []
    
    def __init__(self, name):
        self.name = name
        self.points = 0
        Player.players.append(self)
    
    def increase_points(self, i):
        self.points += i * Player.point_increment
        return self