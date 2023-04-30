from technology import Technology


class Infantry:#(Technology):
    def __init__(self,combat_ability,num,morale):
        #super().__init__(num)
        self.strength = 1000
        self.combat_ability = combat_ability
        self.off_fire = 3 + Technology(num).inf_fire
        self.def_fire = 4 + Technology(num).inf_fire
        self.off_shock = 3 + Technology(num).inf_shock
        self.def_shock = 3 + Technology(num).inf_shock
        self.off_morale = 4
        self.def_morale = 4
        self.morale = morale
        self.tactics = Technology(num).tactics
        
class Cavalry:#(Technology):
    def __init__(self,combat_ability,num,morale):
        #super().__init__(num)
        self.strength = 1000
        self.combat_ability = combat_ability
        self.off_fire = 2 + Technology(num).cav_fire
        self.def_fire = 1 + Technology(num).cav_fire
        self.off_shock = 5 + Technology(num).cav_shock
        self.def_shock = 4 + Technology(num).cav_shock
        self.off_morale = 3
        self.def_morale = 4
        self.morale = morale
        self.tactics = Technology(num).tactics

      
class Artillery:#(Technology):
    def __init__(self,combat_ability,num,morale):
        #super().__init__(num)
        self.strength = 1000
        self.combat_ability = combat_ability
        self.off_fire = 4 + Technology(num).art_fire
        self.def_fire = 3 + Technology(num).art_fire
        self.off_shock = 1 + Technology(num).art_shock
        self.def_shock = 1 + Technology(num).art_shock
        self.off_morale = 5
        self.def_morale=2
        self.morale = morale
        self.tactics = Technology(num).tactics

                        