#store all general changes then a child class with have inf, cav etc stats 


class Technology:
    #enter technology 
    def __init__(self, num : int):
        if num == 0:
            self.inf_fire = 0.25
            self.cav_fire=0
            self.art_fire=0
            self.inf_shock = 0.20
            self.cav_shock = 0.8
            self.art_shock = 0
            self.tactics = 0.5
            self.combat_width = 15
            self.improved_flank = 0
        elif num == 1:
            self.inf_fire = 0.35
            self.cav_fire=0
            self.art_fire=0
            self.inf_shock = 0.30
            self.cav_shock = 0.8
            self.art_shock = 0
            self.tactics = 0.5
            self.combat_width = 15
            self.improved_flank = 0
        elif num == 2:
            self.inf_fire = 0.35
            self.cav_fire=0
            self.art_fire=0
            self.inf_shock = 0.50
            self.cav_shock = 1.0
            self.art_shock = 0
            self.tactics = 0.5
            self.combat_width = 20
            self.improved_flank = 0
        elif num == 3:
            self.inf_fire = 0.35
            self.cav_fire=0
            self.art_fire=0
            self.inf_shock = 0.50
            self.cav_shock = 1.0
            self.art_shock = 0
            self.tactics = 0.5
            self.combat_width = 20
            self.improved_flank = 0
        elif num == 4:
            self.inf_fire = 0.35
            self.cav_fire=0
            self.art_fire=0
            self.inf_shock = 0.50
            self.cav_shock = 1.0
            self.art_shock = 0
            self.tactics = 0.75
            self.combat_width = 20
            self.improved_flank = 0
        elif num == 5:
            self.inf_fire = 0.35
            self.cav_fire=0
            self.art_fire=0
            self.inf_shock = 0.65
            self.cav_shock = 1.2
            self.art_shock = 0
            self.tactics = 0.75
            self.combat_width = 22
            self.improved_flank = 0
        elif num == 6:
            self.inf_fire = 0.55
            self.cav_fire=0
            self.art_fire=0
            self.inf_shock = 0.95
            self.cav_shock = 1.2
            self.art_shock = 0
            self.tactics = 1.0
            self.combat_width = 24
            self.improved_flank = 0   
        elif num == 7:
            self.inf_fire = 0.55
            self.cav_fire=0
            self.art_fire=1.0
            self.inf_shock = 0.95
            self.cav_shock = 1.2
            self.art_shock = 0.05
            self.tactics = 1.25
            self.combat_width = 24
            self.improved_flank = 0   
        elif num == 8:
            self.inf_fire = 0.80
            self.cav_fire=0
            self.art_fire=1.0
            self.inf_shock = 0.95
            self.cav_shock = 2.0
            self.art_shock = 0.05
            self.tactics = 1.25
            self.combat_width = 24
            self.improved_flank = 0   
        elif num == 9:
            self.inf_fire = 0.80
            self.cav_fire=0
            self.art_fire=1.0
            self.inf_shock = 0.95
            self.cav_shock = 2.0
            self.art_shock = 0.05
            self.tactics = 1.50
            self.combat_width = 25
            self.improved_flank = 0   
        elif num == 10:
            self.inf_fire = 0.80
            self.cav_fire=0
            self.art_fire=1.0
            self.inf_shock = 0.95
            self.cav_shock = 2.0
            self.art_shock = 0.05
            self.tactics = 1.50
            self.combat_width = 25
            self.improved_flank = 0.25   
        elif num == 11:
            self.inf_fire = 0.80
            self.cav_fire=0.50
            self.art_fire=1.0
            self.inf_shock = 1.15
            self.cav_shock = 2.0
            self.art_shock = 0.05
            self.tactics = 1.50
            self.combat_width = 27
            self.improved_flank = 0.25
        elif num == 12:
            self.inf_fire = 0.80
            self.cav_fire=0.50
            self.art_fire=1.0
            self.inf_shock = 1.15
            self.cav_shock = 2.0
            self.art_shock = 0.05
            self.tactics = 1.75
            self.combat_width = 27
            self.improved_flank = 0.25   
        elif num == 13:
            self.inf_fire = 0.80
            self.cav_fire=0.50
            self.art_fire=1.4
            self.inf_shock = 1.15
            self.cav_shock = 2.0
            self.art_shock = 0.15
            self.tactics = 1.75
            self.combat_width = 27
            self.improved_flank = 0.25     
        elif num == 14:
            self.inf_fire = 1.10
            self.cav_fire=0.50
            self.art_fire=1.4
            self.inf_shock = 1.15
            self.cav_shock = 2.0
            self.art_shock = 0.15
            self.tactics = 1.75
            self.combat_width = 29
            self.improved_flank = 0.25     
        elif num == 15:
            self.inf_fire = 1.10
            self.cav_fire=0.50
            self.art_fire=1.4
            self.inf_shock = 1.15
            self.cav_shock = 2.0
            self.art_shock = 0.15
            self.tactics = 2.0
            self.combat_width = 29
            self.improved_flank = 0.25    
        elif num == 16:
            self.inf_fire = 1.10
            self.cav_fire=0.50
            self.art_fire=2.4
            self.inf_shock = 1.15
            self.cav_shock = 2.0
            self.art_shock = 0.25
            self.tactics = 2.0
            self.combat_width = 30
            self.improved_flank = 0.25  
        elif num == 17:
            self.inf_fire = 1.10
            self.cav_fire=0.50
            self.art_fire=2.4
            self.inf_shock = 1.15
            self.cav_shock = 3.0
            self.art_shock = 0.25
            self.tactics = 2.0
            self.combat_width = 30
            self.improved_flank = 0.25  
        elif num == 18:
            self.inf_fire = 1.10
            self.cav_fire=0.50
            self.art_fire=2.4
            self.inf_shock = 1.15
            self.cav_shock = 3.0
            self.art_shock = 0.25
            self.tactics = 2.0
            self.combat_width = 32
            self.improved_flank = 0.50 
        elif num == 19:
            self.inf_fire = 1.10
            self.cav_fire=0.50
            self.art_fire=2.4
            self.inf_shock = 1.15
            self.cav_shock = 3.0
            self.art_shock = 0.25
            self.tactics = 2.25
            self.combat_width = 32
            self.improved_flank = 0.50   
        elif num == 20:
            self.inf_fire = 1.60
            self.cav_fire=0.50
            self.art_fire=2.4
            self.inf_shock = 1.15
            self.cav_shock = 3.0
            self.art_shock = 0.25
            self.tactics = 2.25
            self.combat_width = 34
            self.improved_flank = 0.50   
        elif num == 21:
            self.inf_fire = 1.60
            self.cav_fire=0.50
            self.art_fire=2.4
            self.inf_shock = 1.65
            self.cav_shock = 3.0
            self.art_shock = 0.25
            self.tactics = 2.50
            self.combat_width = 34
            self.improved_flank = 0.50  
        elif num == 22:
            self.inf_fire = 1.60
            self.cav_fire=1.0
            self.art_fire=4.4
            self.inf_shock = 1.65
            self.cav_shock = 3.0
            self.art_shock = 0.35
            self.tactics = 2.50
            self.combat_width = 36
            self.improved_flank = 0.50   
        elif num == 23:
            self.inf_fire = 1.60
            self.cav_fire=1.0
            self.art_fire=4.4
            self.inf_shock = 1.65
            self.cav_shock = 4.0
            self.art_shock = 0.35
            self.tactics = 2.75
            self.combat_width = 36
            self.improved_flank = 1.0      
        elif num == 24:
            self.inf_fire = 1.60
            self.cav_fire=1.0
            self.art_fire=4.4
            self.inf_shock = 1.65
            self.cav_shock = 4.0
            self.art_shock = 0.35
            self.tactics = 3.0
            self.combat_width = 38
            self.improved_flank = 1.0     
        elif num == 25:
            self.inf_fire = 1.60
            self.cav_fire=1.0
            self.art_fire=6.4
            self.inf_shock = 1.65
            self.cav_shock = 4.0
            self.art_shock = 0.45
            self.tactics = 3.0
            self.combat_width = 38
            self.improved_flank = 1.0   
        elif num == 26:
            self.inf_fire = 1.60
            self.cav_fire=1.0
            self.art_fire=6.4
            self.inf_shock = 1.65
            self.cav_shock = 4.0
            self.art_shock = 0.45
            self.tactics = 3.0
            self.combat_width = 40
            self.improved_flank = 1.0     
        elif num == 27:
            self.inf_fire = 2.10
            self.cav_fire=1.0
            self.art_fire=6.4
            self.inf_shock = 1.65
            self.cav_shock = 4.0
            self.art_shock = 0.45
            self.tactics = 3.0
            self.combat_width = 40
            self.improved_flank = 1.0   
        elif num == 28:
            self.inf_fire = 2.10
            self.cav_fire=1.0
            self.art_fire=6.4
            self.inf_shock = 2.15
            self.cav_shock = 4.0
            self.art_shock = 0.45
            self.tactics = 3.0
            self.combat_width = 40
            self.improved_flank = 1.25
        elif num == 29:
            self.inf_fire = 2.10
            self.cav_fire=1.0
            self.art_fire=6.4
            self.inf_shock = 2.15
            self.cav_shock = 4.0
            self.art_shock = 0.45
            self.tactics = 3.0
            self.combat_width = 40
            self.improved_flank = 1.25
        elif num == 30:
            self.inf_fire = 2.10
            self.cav_fire=1.0
            self.art_fire=6.4
            self.inf_shock = 2.15
            self.cav_shock = 4.0
            self.art_shock = 0.45
            self.tactics = 3.25
            self.combat_width = 40
            self.improved_flank = 1.50     
        elif num == 31:
            self.inf_fire = 3.10
            self.cav_fire=1.0
            self.art_fire=6.4
            self.inf_shock = 2.15
            self.cav_shock = 5.0
            self.art_shock = 0.45
            self.tactics = 3.25
            self.combat_width = 40
            self.improved_flank = 1.50
        else:
            #defaulting to tech being 32
            self.inf_fire = 3.10
            self.cav_fire=1.0
            self.art_fire=8.4
            self.inf_shock = 2.15
            self.cav_shock = 5.0
            self.art_shock = 0.55
            self.tactics = 3.50
            self.combat_width = 40
            self.improved_flank = 1.50  
                                   

                    