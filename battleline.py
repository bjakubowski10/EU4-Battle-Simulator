from technology import Technology
from infantry import Infantry,Cavalry,Artillery
from unitfactory import UnitFactory

class Army:
    
    #frontline = list()
    #backline = list()
    
    
    def __init__(self,inf_amount : int, inf_combat, cav_combat, art_combat, cav_amount : int,art_amount : int,tech,morale):
        self.inf_list = UnitFactory.inf_factory(inf_amount,inf_combat,tech,morale)
        self.cav_list = UnitFactory.cav_factory(cav_amount,cav_combat,tech,morale)
        self.art_list = UnitFactory.art_factory(art_amount,art_combat,tech,morale)
        
        self.total_army = self.inf_list + self.cav_list + self.art_list
        self.reserves = list()
        
        self.tactics = Technology(tech).tactics
        self.combat_width = Technology(tech).combat_width
        self.improved_flank = Technology(tech).improved_flank
        self.frontline = list()
        self.backline = list()
        
    def fill_front_back_line(self):
        
        inf_count = len(self.inf_list)
        cav_count = len(self.cav_list)
        art_count = len(self.art_list)
        
                        
        if inf_count < self.combat_width: #if there is less inf than combat width, add all to frontline
            #add all the inf to the front    
            if len(self.inf_list) > 0:
                for unit in self.inf_list:
                    self.frontline.append(unit)
                    
                self.inf_list.clear()
                inf_count = 0
            #deploy as much cavalry as possible to the front
            space_remaining = self.combat_width - len(self.frontline)
            for empty_space in range(space_remaining):
                if cav_count > 0: 
                    self.frontline.append(self.cav_list[-1])
                    self.cav_list.pop()
                    cav_count -= 1
                else: break    
            #deploy all art in second row
            space_remaining = self.combat_width - len(self.backline)
            if art_count > 0: 
                for unit in range(space_remaining):
                    if art_count == 0: break
                    self.backline.append(self.art_list[-1])
                    self.art_list.pop()
                    art_count -= 1
            #if the backline is longer than frontline, we even it out     
            space_remaining = self.combat_width - len(self.frontline)
            if space_remaining > 0 and (len(self.backline) > len(self.frontline)):
                while(len(self.backline) > len(self.frontline)):
                        self.frontline.append(self.backline[-1])
                        self.backline.pop()
            #if there is space in the backline, add the remaining cavalry to it           
            space_remaining = self.combat_width - len(self.backline)
            if cav_count > 0:
                for empty_space in range(space_remaining):
                    if cav_count > 0:
                        self.backline.append(self.cav_list[-1])
                        self.cav_list.pop()
                        cav_count -= 1
                    else: break     
        
        if inf_count >= self.combat_width: #process of filling the army if there is as much inf as combat width allows           
            #if 4+ cav, insert 2 each on each side of the front line, and fill the middle with infantry
            if cav_count >= 4:
                self.frontline.append(self.cav_list[-1])
                self.cav_list.pop()
                self.frontline.append(self.cav_list[-1])
                self.cav_list.pop()
                cav_count -= 2
                space_remaining = self.combat_width - len(self.frontline)
                for unit in range(space_remaining-2):
                    self.frontline.append(self.inf_list[-1])
                    self.inf_list.pop()
                    inf_count -= 1
                self.frontline.append(self.cav_list[-1])
                self.cav_list.pop()
                self.frontline.append(self.cav_list[-1])
                self.cav_list.pop()
                cav_count -= 2
            
                
                #if 2 cav, we add one unit to the beginning and end of the list, if 3, we add one to the back and 2 to the end
            elif cav_count >= 2:
                self.frontline.append(self.cav_list[-1])
                self.cav_list.pop()
                cav_count -= 1
                if cav_count > 1:
                    space_remaining = self.combat_width - len(self.frontline)
                    for unit in range(space_remaining-2):
                        self.frontline.append(self.inf_list[-1])
                        self.inf_list.pop()
                        inf_count -= 1
                    self.frontline.append(self.cav_list[-1])
                    self.cav_list.pop()
                    self.frontline.append(self.cav_list[-1])
                    self.cav_list.pop()
                    cav_count -= 2
                elif cav_count == 1:
                    space_remaining = self.combat_width - len(self.frontline)
                    for unit in range(space_remaining-1):
                        self.frontline.append(self.inf_list[-1])
                        self.inf_list.pop()
                        inf_count -= 1
                    self.frontline.append(self.cav_list[-1])
                    self.cav_list.pop()
                    cav_count -= 1
                    
            #if one cav unit just add it to the beginning of the list        
            elif cav_count > 0:
                self.frontline.append(self.cav_list[-1])
                self.cav_list.pop()
                cav_count -=1
                
                space_remaining = self.combat_width - len(self.frontline)
                for unit in range(space_remaining):
                    self.frontline.append(self.inf_list[-1])
                    self.inf_list.pop()
                    inf_count -=1
               
                    
            #if no cav just add all inf to the army        
            else:
                for unit in range(self.combat_width):
                    self.frontline.append(self.inf_list[-1])
                    self.inf_list.pop()
                    inf_count -=1
              
            #if there is art, append all of it to the back
            if art_count > 0:
                space_remaining = self.combat_width - len(self.backline)
                for unit in range(space_remaining):
                    if art_count == 0: break
                    self.backline.append(self.art_list[-1])
                    self.art_list.pop()
                    art_count -= 1
            space_remaining = self.combat_width - len(self.backline)
            #if inf is remaining, add it to the available space in the back
            if inf_count > 0:
                for unit in range(space_remaining):
                    if inf_count == 0: break
                    self.backline.append(self.inf_list[-1])
                    self.inf_list.pop()
                    inf_count -= 1
            space_remaining = self.combat_width - len(self.backline)
            #if there is still cav, add it to the available space in the back
            if cav_count > 0:
                for unit in range(space_remaining):
                    if cav_count == 0: break
                    self.backline.append(self.cav_list[-1])
                    self.cav_list.pop()
                    cav_count -=1        
        
        self.reserves = self.inf_list + self.cav_list + self.art_list            
        print('front',len(self.frontline))
        print('back',len(self.backline))            
        print('infcount',inf_count)
        print('inflist',len(self.inf_list))
        print('cavcount',cav_count)
        print('cavlist',len(self.cav_list))
        print('artcount',art_count)
        print('artlist',len(self.art_list))
        print('total',len(self.reserves))                                 
                            
                        
    def morale_and_troop_count(self):
        army_size = 0
        total_morale = 0
        for i in range(len(self.total_army)):
            army_size += self.total_army[i].strength
            total_morale += self.total_army[i].morale
        return army_size,total_morale    
            
                        
    def tester(self):
        army_size = 0
        total_morale = 0
        for i in range(len(self.frontline)):
            army_size += self.frontline[i].strength
            total_morale += self.frontline[i].morale
        return army_size,total_morale                        
                    
                
                
            
            
            
          
                
                                
                            
        
            
        
       
    