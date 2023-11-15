class GameStats:
    def __init__(self, player, position, ftm, fta, two_pm, two_pa, three_pm, three_pa, reb, blk, ast, stl, tov):
        self.player = player
        self.position = position
        self.ftm = int(ftm)
        self.fta = int(fta)
        self.two_pm = int(two_pm)
        self.two_pa = int(two_pa)
        self.three_pm = int(three_pm)
        self.three_pa = int(three_pa)
        self.reb = int(reb)
        self.blk = int(blk)
        self.ast = int(ast)
        self.stl = int(stl)
        self.tov = int(tov)