
from technology import Technology
from infantry import Infantry,Cavalry,Artillery


class UnitFactory:

    def inf_factory(number : int,combat_ability,tech_num : int,morale):
        infantry_amount = list()
        for i in range(number):
            infantry_amount.append(Infantry(combat_ability,tech_num,morale))
        return infantry_amount    
            
    def cav_factory(number : int,combat_ability,tech_num : int,morale):
        cavalry_amount = list()
        for i in range(number):
            cavalry_amount.append(Cavalry(combat_ability,tech_num,morale))
        return cavalry_amount    
    def art_factory(number : int,combat_ability,tech_num : int,morale):
        artillery_amount = list()
        for i in range(number):
            artillery_amount.append(Artillery(combat_ability,tech_num,morale))
        return artillery_amount    



    
