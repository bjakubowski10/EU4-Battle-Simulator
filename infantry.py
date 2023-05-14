from technology import Technology


class Infantry:#(Technology):
    def __init__(self,combat_ability,num,morale,unit_name :str):
        self.strength = 1000
        self.combat_ability = combat_ability
        self.morale = morale
        self.tactics = Technology(num).tactics
        
        if unit_name == "Halberd Infantry":
            self.off_fire = 0 + Technology(num).inf_fire
            self.def_fire = 0
            self.off_shock = 1 + Technology(num).inf_shock
            self.def_shock = 0
            self.off_morale = 1
            self.def_morale = 0
        elif unit_name == "Latin Medieval Infantry":
            self.off_fire = 0 + Technology(num).inf_fire
            self.def_fire = 0
            self.off_shock = 0 + Technology(num).inf_shock
            self.def_shock = 0
            self.off_morale = 1
            self.def_morale = 1
        elif unit_name == "Galloglaigh Infantry":
            self.off_fire = 0 + Technology(num).inf_fire
            self.def_fire = 0
            self.off_shock = 1 + Technology(num).inf_shock
            self.def_shock = 0
            self.off_morale = 2
            self.def_morale = 0
        elif unit_name == "Longbow":
            self.off_fire = 0 + Technology(num).inf_fire
            self.def_fire = 0
            self.off_shock = 1 + Technology(num).inf_shock
            self.def_shock = 0
            self.off_morale = 1
            self.def_morale = 1
        elif unit_name == "Condotta Infantry":
            self.off_fire = 0 + Technology(num).inf_fire
            self.def_fire = 0
            self.off_shock = 2 + Technology(num).inf_shock
            self.def_shock = 1
            self.off_morale = 1
            self.def_morale = 1
        elif unit_name == "Landsknechten Infantry":
            self.off_fire = 0 + Technology(num).inf_fire
            self.def_fire = 0
            self.off_shock = 1 + Technology(num).inf_shock
            self.def_shock = 1
            self.off_morale = 1
            self.def_morale = 2
        elif unit_name == "Reformed Galloglaigh Infantry":
            self.off_fire = 0 + Technology(num).inf_fire
            self.def_fire = 0
            self.off_shock = 2 + Technology(num).inf_shock
            self.def_shock = 0
            self.off_morale = 2
            self.def_morale = 1
        elif unit_name == "Free Shooter Infantry":
            self.off_fire = 1 + Technology(num).inf_fire
            self.def_fire = 2
            self.off_shock = 2 + Technology(num).inf_shock
            self.def_shock = 1
            self.off_morale = 3
            self.def_morale = 1
        elif unit_name == "Tercio Infantry":
            self.off_fire = 1 + Technology(num).inf_fire
            self.def_fire = 2
            self.off_shock = 1 + Technology(num).inf_shock
            self.def_shock = 2
            self.off_morale = 2
            self.def_morale = 2
        elif unit_name == "Charge Infantry":
            self.off_fire = 1 + Technology(num).inf_fire
            self.def_fire = 2
            self.off_shock = 3 + Technology(num).inf_shock
            self.def_shock = 1
            self.off_morale = 3
            self.def_morale = 2
        elif unit_name == "Maurician Infantry":
            self.off_fire = 2 + Technology(num).inf_fire
            self.def_fire = 2
            self.off_shock = 2 + Technology(num).inf_shock
            self.def_shock = 1
            self.off_morale = 3
            self.def_morale = 2
        elif unit_name == "Gustavian Infantry":
            self.off_fire = 3 + Technology(num).inf_fire
            self.def_fire = 2
            self.off_shock = 3 + Technology(num).inf_shock
            self.def_shock = 2
            self.off_morale = 3
            self.def_morale = 2
        elif unit_name == "Highlanders Infantry":
            self.off_fire = 2 + Technology(num).inf_fire
            self.def_fire = 2
            self.off_shock = 3 + Technology(num).inf_shock
            self.def_shock = 2
            self.off_morale = 4
            self.def_morale = 2
        elif unit_name == "Reformed Tercio":
            self.off_fire = 2 + Technology(num).inf_fire
            self.def_fire = 2
            self.off_shock = 2 + Technology(num).inf_shock
            self.def_shock = 3
            self.off_morale = 3
            self.def_morale = 3
        elif unit_name == "Caroline Infantry":
            self.off_fire = 3 + Technology(num).inf_fire
            self.def_fire = 2
            self.off_shock = 3 + Technology(num).inf_shock
            self.def_shock = 2
            self.off_morale = 3
            self.def_morale = 3
        elif unit_name == "Grenzer Infantry":
            self.off_fire = 2 + Technology(num).inf_fire
            self.def_fire = 3
            self.off_shock = 2 + Technology(num).inf_shock
            self.def_shock = 3
            self.off_morale = 3
            self.def_morale = 3
        elif unit_name == "Line Infantry":
            self.off_fire = 3 + Technology(num).inf_fire
            self.def_fire = 3
            self.off_shock = 2 + Technology(num).inf_shock
            self.def_shock = 2
            self.off_morale = 3
            self.def_morale = 3
        elif unit_name == "Blue Coat Infantry":
            self.off_fire = 3 + Technology(num).inf_fire
            self.def_fire = 3
            self.off_shock = 3 + Technology(num).inf_shock
            self.def_shock = 3
            self.off_morale = 4
            self.def_morale = 4
        elif unit_name == "Frederickian Infantry":
            self.off_fire = 4 + Technology(num).inf_fire
            self.def_fire = 3
            self.off_shock = 3 + Technology(num).inf_shock
            self.def_shock = 3
            self.off_morale = 4
            self.def_morale = 3
        elif unit_name == "Red Coat Infantry":
            self.off_fire = 3 + Technology(num).inf_fire
            self.def_fire = 4
            self.off_shock = 3 + Technology(num).inf_shock
            self.def_shock = 3
            self.off_morale = 4
            self.def_morale = 3
        elif unit_name == "White Coat Infantry":
            self.off_fire = 4 + Technology(num).inf_fire
            self.def_fire = 3
            self.off_shock = 3 + Technology(num).inf_shock
            self.def_shock = 3
            self.off_morale = 3
            self.def_morale = 4
        elif unit_name == "Impulse Infantry":
            self.off_fire = 4 + Technology(num).inf_fire
            self.def_fire = 3
            self.off_shock = 3 + Technology(num).inf_shock
            self.def_shock = 3
            self.off_morale = 4
            self.def_morale = 4
        elif unit_name == "Square Infantry":
            self.off_fire = 3 + Technology(num).inf_fire
            self.def_fire = 4
            self.off_shock = 3 + Technology(num).inf_shock
            self.def_shock = 3
            self.off_morale = 4
            self.def_morale = 4
        elif unit_name == "Drill Infantry":
            self.off_fire = 4 + Technology(num).inf_fire
            self.def_fire = 4
            self.off_shock = 3 + Technology(num).inf_shock
            self.def_shock = 3
            self.off_morale = 4
            self.def_morale = 4
        elif unit_name == "Jaeger Infantry":
            self.off_fire = 4 + Technology(num).inf_fire
            self.def_fire = 4
            self.off_shock = 4 + Technology(num).inf_shock
            self.def_shock = 3
            self.off_morale = 3
            self.def_morale = 4
        elif unit_name == "Mixed Order Infantry":
            self.off_fire = 4 + Technology(num).inf_fire
            self.def_fire = 3
            self.off_shock = 4 + Technology(num).inf_shock
            self.def_shock = 3
            self.off_morale = 4
            self.def_morale = 4
        elif unit_name == "Napoleonic Infantry":
            self.off_fire = 4 + Technology(num).inf_fire
            self.def_fire = 4
            self.off_shock = 4 + Technology(num).inf_shock
            self.def_shock = 3
            self.off_morale = 4
            self.def_morale = 3  
        elif unit_name == "Bardiche Infantry":
            self.off_fire = 0 + Technology(num).inf_fire
            self.def_fire = 0
            self.off_shock = 0 + Technology(num).inf_shock
            self.def_shock = 0
            self.off_morale = 1
            self.def_morale = 1
        elif unit_name == "Eastern Medieval Infantry":
            self.off_fire = 0 + Technology(num).inf_fire
            self.def_fire = 0
            self.off_shock = 1 + Technology(num).inf_shock
            self.def_shock = 0
            self.off_morale = 1
            self.def_morale = 0
        elif unit_name == "Eastern Militia":
            self.off_fire = 0 + Technology(num).inf_fire
            self.def_fire = 0
            self.off_shock = 1 + Technology(num).inf_shock
            self.def_shock = 1
            self.off_morale = 1
            self.def_morale = 1     
        elif unit_name == "Pike Infantry":
            self.off_fire = 0 + Technology(num).inf_fire
            self.def_fire = 0
            self.off_shock = 1 + Technology(num).inf_shock
            self.def_shock = 2
            self.off_morale = 1
            self.def_morale = 2
        elif unit_name == "Defensive Eastern Musketeers":
            self.off_fire = 2 + Technology(num).inf_fire
            self.def_fire = 2
            self.off_shock = 1 + Technology(num).inf_shock
            self.def_shock = 2
            self.off_morale = 2
            self.def_morale = 2
        elif unit_name == "Offensive Eastern Musketeers":
            self.off_fire = 2 + Technology(num).inf_fire
            self.def_fire = 1
            self.off_shock = 2 + Technology(num).inf_shock
            self.def_shock = 1
            self.off_morale = 3
            self.def_morale = 2
        elif unit_name == "Eastern Tercio":
            self.off_fire = 2 + Technology(num).inf_fire
            self.def_fire = 2
            self.off_shock = 1 + Technology(num).inf_shock
            self.def_shock = 2
            self.off_morale = 2
            self.def_morale = 3
        elif unit_name == "Soldaty Infantry":
            self.off_fire = 3 + Technology(num).inf_fire
            self.def_fire = 1
            self.off_shock = 2 + Technology(num).inf_shock
            self.def_shock = 1
            self.off_morale = 3
            self.def_morale = 2
        elif unit_name == "Saxon Infantry":
            self.off_fire = 3 + Technology(num).inf_fire
            self.def_fire = 2
            self.off_shock = 3 + Technology(num).inf_shock
            self.def_shock = 2
            self.off_morale = 2
            self.def_morale = 2   
        elif unit_name == "Petrine Infantry":
            self.off_fire = 2 + Technology(num).inf_fire
            self.def_fire = 3
            self.off_shock = 2 + Technology(num).inf_shock
            self.def_shock = 3
            self.off_morale = 3
            self.def_morale = 3
        elif unit_name == "Green Coat Infantry":
            self.off_fire = 3 + Technology(num).inf_fire
            self.def_fire = 3
            self.off_shock = 3 + Technology(num).inf_shock
            self.def_shock = 3
            self.off_morale = 4
            self.def_morale = 4
        elif unit_name == "Mass Infantry":
            self.off_fire = 4 + Technology(num).inf_fire
            self.def_fire = 3
            self.off_shock = 4 + Technology(num).inf_shock
            self.def_shock = 3
            self.off_morale = 4
            self.def_morale = 3
        else: 
            self.off_fire = 4 + Technology(num).inf_fire
            self.def_fire = 3
            self.off_shock = 4 + Technology(num).inf_shock
            self.def_shock = 3
            self.off_morale = 4
            self.def_morale = 3                                                                                               
                                                                                                                                                                                             
        
        
class Cavalry:#(Technology):
    def __init__(self,combat_ability,num,morale,unit_name : str):
        self.strength = 1000
        self.combat_ability = combat_ability
        self.morale = morale
        self.tactics = Technology(num).tactics
        
        if unit_name == "Druzhina Cavalry":
            self.off_fire = 0 + Technology(num).cav_fire
            self.def_fire = 0
            self.off_shock = 0 + Technology(num).cav_shock
            self.def_shock = 1
            self.off_morale = 1
            self.def_morale = 1
        elif unit_name == "Eastern Knights":
            self.off_fire = 0 + Technology(num).cav_fire
            self.def_fire = 0
            self.off_shock = 1 + Technology(num).cav_shock
            self.def_shock = 0
            self.off_morale = 1
            self.def_morale = 1
        elif unit_name == "Stratioti Cavalry":
            self.off_fire = 0 + Technology(num).cav_fire
            self.def_fire = 0
            self.off_shock = 2 + Technology(num).cav_shock
            self.def_shock = 1
            self.off_morale = 1
            self.def_morale = 1
        elif unit_name == "Eastern Hussar":
            self.off_fire = 0 + Technology(num).cav_fire
            self.def_fire = 0
            self.off_shock = 2 + Technology(num).cav_shock
            self.def_shock = 2
            self.off_morale = 3
            self.def_morale = 2
        elif unit_name == "Eastern Caracole":
            self.off_fire = 2 + Technology(num).cav_fire
            self.def_fire = 0
            self.off_shock = 2 + Technology(num).cav_shock
            self.def_shock = 2
            self.off_morale = 3
            self.def_morale = 3
        elif unit_name == "Reformed Eastern Hussars":
            self.off_fire = 1 + Technology(num).cav_fire
            self.def_fire = 1
            self.off_shock = 3 + Technology(num).cav_shock
            self.def_shock = 3
            self.off_morale = 2
            self.def_morale = 2
        elif unit_name == "Southern Cossacks":
            self.off_fire = 0 + Technology(num).cav_fire
            self.def_fire = 1
            self.off_shock = 4 + Technology(num).cav_shock
            self.def_shock = 2
            self.off_morale = 2
            self.def_morale = 3    
        elif unit_name == "Cossack Cavalry":
            self.off_fire = 1 + Technology(num).cav_fire
            self.def_fire = 1
            self.off_shock = 4 + Technology(num).cav_shock
            self.def_shock = 3
            self.off_morale = 4
            self.def_morale = 4
        elif unit_name == "Winged Hussars":
            self.off_fire = 0 + Technology(num).cav_fire
            self.def_fire = 1
            self.off_shock = 5 + Technology(num).cav_shock
            self.def_shock = 4
            self.off_morale = 4
            self.def_morale = 3
        elif unit_name == "Lancers":
            self.off_fire = 0 + Technology(num).cav_fire
            self.def_fire = 1
            self.off_shock = 5 + Technology(num).cav_shock
            self.def_shock = 4
            self.off_morale = 4
            self.def_morale = 4 
        elif unit_name == "Reformed Cossack Cavalry":
            self.off_fire = 1 + Technology(num).cav_fire
            self.def_fire = 1
            self.off_shock = 4 + Technology(num).cav_shock
            self.def_shock = 4
            self.off_morale = 4
            self.def_morale = 4
        elif unit_name == "Advanced Cossack Cavalry":
            self.off_fire = 2 + Technology(num).cav_fire
            self.def_fire = 1
            self.off_shock = 4 + Technology(num).cav_shock
            self.def_shock = 4
            self.off_morale = 5
            self.def_morale = 4
        elif unit_name == "Eastern Cuirassiers":
            self.off_fire = 1 + Technology(num).cav_fire
            self.def_fire = 2
            self.off_shock = 5 + Technology(num).cav_shock
            self.def_shock = 4
            self.off_morale = 4
            self.def_morale = 4
        elif unit_name == "Chevauchee":
            self.off_fire = 0 + Technology(num).cav_fire
            self.def_fire = 0
            self.off_shock = 1 + Technology(num).cav_shock
            self.def_shock = 1
            self.off_morale = 0
            self.def_morale = 1
        elif unit_name == "Western Medieval Knights":
            self.off_fire = 0 + Technology(num).cav_fire
            self.def_fire = 0
            self.off_shock = 1 + Technology(num).cav_shock
            self.def_shock = 0
            self.off_morale = 1
            self.def_morale = 1
        elif unit_name == "Schwarze Reiter":
            self.off_fire = 1 + Technology(num).cav_fire
            self.def_fire = 0
            self.off_shock = 2 + Technology(num).cav_shock
            self.def_shock = 1
            self.off_morale = 2
            self.def_morale = 2
        elif unit_name == "Latin Caracole Cavalry":
            self.off_fire = 1 + Technology(num).cav_fire
            self.def_fire = 0
            self.off_shock = 3 + Technology(num).cav_shock
            self.def_shock = 2
            self.off_morale = 2
            self.def_morale = 2
        elif unit_name == "Gallop Cavalry":
            self.off_fire = 1 + Technology(num).cav_fire
            self.def_fire = 1
            self.off_shock = 4 + Technology(num).cav_shock
            self.def_shock = 3
            self.off_morale = 3
            self.def_morale = 3
        elif unit_name == "Armee Blanche Cavalry":
            self.off_fire = 1 + Technology(num).cav_fire
            self.def_fire = 1
            self.off_shock = 5 + Technology(num).cav_shock
            self.def_shock = 3
            self.off_morale = 5
            self.def_morale = 3
        elif unit_name == "Latin Dragoons":
            self.off_fire = 1 + Technology(num).cav_fire
            self.def_fire = 1
            self.off_shock = 4 + Technology(num).cav_shock
            self.def_shock = 4
            self.off_morale = 4
            self.def_morale = 4
        elif unit_name == "Latin Hussars":
            self.off_fire = 1 + Technology(num).cav_fire
            self.def_fire = 2
            self.off_shock = 4 + Technology(num).cav_shock
            self.def_shock = 3
            self.off_morale = 4
            self.def_morale = 4
        elif unit_name == "Carabiners":
            self.off_fire = 2 + Technology(num).cav_fire
            self.def_fire = 1
            self.off_shock = 5 + Technology(num).cav_shock
            self.def_shock = 4
            self.off_morale = 3
            self.def_morale = 4
        elif unit_name == "Reformed Latin Hussars":
            self.off_fire = 1 + Technology(num).cav_fire
            self.def_fire = 2
            self.off_shock = 4 + Technology(num).cav_shock
            self.def_shock = 4
            self.off_morale = 4
            self.def_morale = 4
        elif unit_name == "Uhlan Cavalry":
            self.off_fire = 1 + Technology(num).cav_fire
            self.def_fire = 2
            self.off_shock = 5 + Technology(num).cav_shock
            self.def_shock = 4
            self.off_morale = 4
            self.def_morale = 3
        elif unit_name == "Latin Chasseur":
            self.off_fire = 2 + Technology(num).cav_fire
            self.def_fire = 1
            self.off_shock = 4 + Technology(num).cav_shock
            self.def_shock = 4
            self.off_morale = 5
            self.def_morale = 5
        elif unit_name == "Latin Cuirassiers":
            self.off_fire = 1 + Technology(num).cav_fire
            self.def_fire = 2
            self.off_shock = 5 + Technology(num).cav_shock
            self.def_shock = 4
            self.off_morale = 4
            self.def_morale = 5
        elif unit_name == "Latin Lancers":
            self.off_fire = 0 + Technology(num).cav_fire
            self.def_fire = 2
            self.off_shock = 6 + Technology(num).cav_shock
            self.def_shock = 4
            self.off_morale = 5
            self.def_morale = 4
        else:
            self.off_fire = 0 + Technology(num).cav_fire
            self.def_fire = 2
            self.off_shock = 6 + Technology(num).cav_shock
            self.def_shock = 4
            self.off_morale = 5
            self.def_morale = 4
                            
                                                                                                    
                                                                                            
        

      
class Artillery:#(Technology):
    def __init__(self,combat_ability,num,morale,unit_name: str):
        self.strength = 1000
        self.combat_ability = combat_ability
        self.morale = morale
        self.tactics = Technology(num).tactics

        
        if unit_name == "Houfnice":
            self.off_fire = 1 + Technology(num).art_fire
            self.def_fire = 0
            self.off_shock = 0 + Technology(num).art_shock
            self.def_shock = 0
            self.off_morale = 0
            self.def_morale=1
        elif unit_name == "Large Cast Bronze Mortar":
            self.off_fire = 0 + Technology(num).art_fire
            self.def_fire = 0
            self.off_shock = 0 + Technology(num).art_shock
            self.def_shock = 0
            self.off_morale = 0
            self.def_morale=2
        elif unit_name == "Culverin":
            self.off_fire = 2 + Technology(num).art_fire
            self.def_fire = 1
            self.off_shock = 0 + Technology(num).art_shock
            self.def_shock = 1
            self.off_morale = 0
            self.def_morale = 0
        elif unit_name == "Pedrero":
            self.off_fire = 1 + Technology(num).art_fire
            self.def_fire = 0
            self.off_shock = 0 + Technology(num).art_shock
            self.def_shock = 2
            self.off_morale = 1
            self.def_morale = 0
        elif unit_name == "Large Cast Iron Cannon":
            self.off_fire = 1 + Technology(num).art_fire
            self.def_fire = 1
            self.off_shock = 0 + Technology(num).art_shock
            self.def_shock = 1
            self.off_morale = 2
            self.def_morale = 0
        elif unit_name == "Small Cast Iron Cannon":
            self.off_fire = 1 + Technology(num).art_fire
            self.def_fire = 1
            self.off_shock = 0 + Technology(num).art_shock
            self.def_shock = 2
            self.off_morale = 1
            self.def_morale = 1
        elif unit_name == "Chambered Demi Cannon":
            self.off_fire = 2 + Technology(num).art_fire
            self.def_fire = 2
            self.off_shock = 0 + Technology(num).art_shock
            self.def_shock = 1
            self.off_morale = 2
            self.def_morale = 1 
        elif unit_name == "Demi-Culverin":
            self.off_fire = 1 + Technology(num).art_fire
            self.def_fire = 2
            self.off_shock = 0 + Technology(num).art_shock
            self.def_shock = 2
            self.off_morale = 2
            self.def_morale = 1    
        elif unit_name == "Leather Cannon":
            self.off_fire = 3 + Technology(num).art_fire
            self.def_fire = 2
            self.off_shock = 1 + Technology(num).art_shock
            self.def_shock = 1
            self.off_morale = 2
            self.def_morale = 1
        elif unit_name == "Chambered Cannon":
            self.off_fire = 3 + Technology(num).art_fire
            self.def_fire = 2
            self.off_shock = 1 + Technology(num).art_shock
            self.def_shock = 2
            self.off_morale = 1
            self.def_morale = 1 
        elif unit_name == "Swivel Cannon":
            self.off_fire = 3 + Technology(num).art_fire
            self.def_fire = 2
            self.off_shock = 1 + Technology(num).art_shock
            self.def_shock = 2
            self.off_morale = 3
            self.def_morale = 1
        elif unit_name == "Howitzer":
            self.off_fire = 3 + Technology(num).art_fire
            self.def_fire = 2
            self.off_shock = 1 + Technology(num).art_shock
            self.def_shock = 2
            self.off_morale = 2
            self.def_morale = 2
        elif unit_name == "Coehorn Mortar":
            self.off_fire = 2 + Technology(num).art_fire
            self.def_fire = 4
            self.off_shock = 1 + Technology(num).art_shock
            self.def_shock = 2
            self.off_morale = 2
            self.def_morale = 3
        elif unit_name == "Horse Artillery":
            self.off_fire = 3 + Technology(num).art_fire
            self.def_fire = 3
            self.off_shock = 1 + Technology(num).art_shock
            self.def_shock = 1
            self.off_morale = 4
            self.def_morale = 2
        elif unit_name == "Royal Mortar":
            self.off_fire = 4 + Technology(num).art_fire
            self.def_fire = 3
            self.off_shock = 1 + Technology(num).art_shock
            self.def_shock = 1
            self.off_morale = 5
            self.def_morale = 2   
        elif unit_name == "Licorne":
            self.off_fire = 3 + Technology(num).art_fire
            self.def_fire = 4
            self.off_shock = 1 + Technology(num).art_shock
            self.def_shock = 2
            self.off_morale = 3
            self.def_morale = 3
        elif unit_name == "Flying Battery":
            self.off_fire = 5 + Technology(num).art_fire
            self.def_fire = 4
            self.off_shock = 2 + Technology(num).art_shock
            self.def_shock = 2
            self.off_morale = 4
            self.def_morale = 3
        elif unit_name == "Grand Battery":
            self.off_fire = 4 + Technology(num).art_fire
            self.def_fire = 4
            self.off_shock = 2 + Technology(num).art_shock
            self.def_shock = 4
            self.off_morale = 3
            self.def_morale = 3
        else:
            self.off_fire = 4 + Technology(num).art_fire
            self.def_fire = 4
            self.off_shock = 2 + Technology(num).art_shock
            self.def_shock = 4
            self.off_morale = 3
            self.def_morale = 3
                                                                                                                                                            
            
            
        
        

                        