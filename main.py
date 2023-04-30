from battleline import Army
from threading import Thread
import infantry
import random







        
   

#defender
print("Defender Side")
inf = int(input('Amount of infantry -'))
cav = int(input("Amount of cavalry - "))
art = int(input('Amount of artillery - '))
inf_combat = float(input("Infantry combat ability - "))
cav_combat = float(input("Cavalry combat ability - "))
art_combat = float(input("Artillery combat ability - "))
tech = int(input("Tech level - "))
moral = float(input("Morale - "))
discipline = float(input("Discipline - "))
ldr_fire = int(input("Leader Fire - "))
ldr_shock = int(input("leader shock - "))
print("==================")
#attack
print("Attacker Side")
attack_inf = int(input('Amount of infantry -'))
attack_cav = int(input("Amount of cavalry - "))
attack_art = int(input('Amount of artillery - '))
attack_inf_combat = float(input("Infantry combat ability - "))
attack_cav_combat = float(input("Cavalry combat ability - "))
attack_art_combat = float(input("Artillery combat ability - "))
attack_tech = int(input("Tech level - "))
attack_moral = float(input("Morale - "))
attack_discipline = float(input("Discipline - "))
attack_ldr_fire = int(input("Leader fire - "))
attack_ldr_shock = int(input("Leader shock - "))

terrain = int(input("Terrain modifier - "))

defender_army = Army(inf,inf_combat,cav_combat,art_combat,cav,art,tech,moral)
attacker_army = Army(attack_inf,attack_inf_combat,attack_cav_combat,attack_art_combat,attack_cav,attack_art,attack_tech,attack_moral)

#fill the front and backlines
defender_army.fill_front_back_line()
attacker_army.fill_front_back_line()

#army_size,moralesum = defender_army.morale_and_troop_count()
#attack_size,attack_m_sum = attacker_army.morale_and_troop_count()

army_size,moralesum = defender_army.tester()
attack_size,attack_m_sum = attacker_army.tester()


#need a way to replace units
#maybe just insert morale into the function and substract from it ?
#need to have units fight, fuck flanking 

fire_phase = True
shock_phase = False
total_days = 0
phase_interval = 0


while army_size > 0 and attack_size > 0 and moralesum > 0 and attack_m_sum > 0:
    phase_interval +=1
    
    if fire_phase == True:
        deflen = len(defender_army.frontline)
        attlen = len(attacker_army.frontline)
        dice_roll = random.randint(0,9)
        att_dice_roll = random.randint(0,9) - terrain
        if att_dice_roll < 0 :  att_dice_roll=0
        
        if deflen <= attlen:
            for i in range(len(defender_army.frontline)):
                #how much damage defenders deal
                pips = dice_roll + max(0,ldr_fire-attack_ldr_fire) + defender_army.frontline[i].off_fire - attacker_army.frontline[i].def_fire
                multiplier = (defender_army.frontline[i].strength / 1000) * (defender_army.frontline[i].off_fire / attacker_army.frontline[i].tactics) * (1 + defender_army.frontline[i].combat_ability) * ( 1 + discipline) * (1 + (total_days+1)/100)
                morale_casualties = ((15 + 5 * pips) * multiplier * (defender_army.frontline[i].morale/540) + 0.03)/20
                str_casualties = ((15 + 5*pips) * multiplier)/20
                
                #how much dmg attacker deal
                att_pips = att_dice_roll + max(0,attack_ldr_fire-ldr_fire) + attacker_army.frontline[i].off_fire - defender_army.frontline[i].def_fire
                att_multiplier = (attacker_army.frontline[i].strength / 1000) * (attacker_army.frontline[i].off_fire / defender_army.frontline[i].tactics) * (1 + attacker_army.frontline[i].combat_ability) * ( 1 + attack_discipline) * (1 + (total_days+1)/100)
                att_morale_casualties = ((15 + 5 * att_pips) * att_multiplier * (attacker_army.frontline[i].morale/540) + 0.03)/20
                att_str_casualties = ((15 + 5*att_pips) * att_multiplier)/20
                
                defender_army.frontline[i].morale -= att_morale_casualties
                defender_army.frontline[i].strength -= att_str_casualties
                army_size -= att_str_casualties
                moralesum -= att_morale_casualties
                attacker_army.frontline[i].morale -= morale_casualties
                attacker_army.frontline[i].strength -= str_casualties
                attack_size -= str_casualties
                attack_m_sum -= morale_casualties
        elif attlen < deflen:
            for i in range(len(attacker_army.frontline)):
                #how much damage defenders deal
                pips = dice_roll + max(0,ldr_fire-attack_ldr_fire) + defender_army.frontline[i].off_fire - attacker_army.frontline[i].def_fire
                multiplier = (defender_army.frontline[i].strength / 1000) * (defender_army.frontline[i].off_fire / attacker_army.frontline[i].tactics) * (1 + defender_army.frontline[i].combat_ability) * ( 1 + discipline) * (1 + (total_days+1)/100)
                morale_casualties = ((15 + 5 * pips) * multiplier * (defender_army.frontline[i].morale/540) + 0.03)/20
                str_casualties = ((15 + 5*pips) * multiplier)/20
                
                #how much dmg attacker deal
                att_pips = att_dice_roll + max(0,attack_ldr_fire-ldr_fire) + attacker_army.frontline[i].off_fire - defender_army.frontline[i].def_fire
                att_multiplier = (attacker_army.frontline[i].strength / 1000) * (attacker_army.frontline[i].off_fire / defender_army.frontline[i].tactics) * (1 + attacker_army.frontline[i].combat_ability) * ( 1 + attack_discipline) * (1 + (total_days+1)/100)
                att_morale_casualties = ((15 + 5 * att_pips) * att_multiplier * (attacker_army.frontline[i].morale/540) + 0.03)/20
                att_str_casualties = ((15 + 5*att_pips) * att_multiplier)/20
                
                defender_army.frontline[i].morale -= att_morale_casualties
                defender_army.frontline[i].strength -= att_str_casualties
                army_size -= att_str_casualties
                moralesum -= att_morale_casualties
                attacker_army.frontline[i].morale -= morale_casualties
                attacker_army.frontline[i].strength -= str_casualties
                attack_size -= str_casualties
                attack_m_sum -= morale_casualties
        else: break                
                
       
        if len(defender_army.backline) <= len(attacker_army.backline):
            for i in range(len(defender_army.backline)):
                    #how much damage defender art does to attacker frontline
                if isinstance(defender_army.backline[i],infantry.Artillery):
                        #if index of the art matches up to an index of enemy front line
                    if (0 <= i) and (i <len(attacker_army.frontline)):
                        pips_art = dice_roll + max(0,ldr_fire-attack_ldr_fire) + defender_army.backline[i].off_fire - attacker_army.frontline[i].def_fire
                        multiplier_art = (defender_army.backline[i].strength/1000) * (defender_army.backline[i].off_fire / attacker_army.frontline[i].tactics) * (1 + defender_army.backline[i].combat_ability) * (1+discipline) * (1+(total_days+1/100))
                        morale_casualties_art = ((15+5*pips_art) * multiplier_art * (defender_army.backline[i].morale/540) + 0.03 )/40
                        str_casualties_art = ((15 + 5* pips_art) * multiplier_art)/40
                        attacker_army.frontline[i].morale -= morale_casualties_art
                        attacker_army.frontline[i].strength -= str_casualties_art
                        attack_size -= str_casualties_art
                        attack_m_sum -= morale_casualties_art
                                
                                
                        #how much dmg attacker art does to defender frontline
                if isinstance(attacker_army.backline[i],infantry.Artillery):
                            #if index of the art matches up to an index of enemy front line
                    if (0 <= i) and (i <len(defender_army.frontline)):
                        pips_art_at = att_dice_roll + max(0,attack_ldr_fire-ldr_fire) + attacker_army.backline[i].off_fire - defender_army.frontline[i].def_fire
                        multiplier_art_at = (attacker_army.backline[i].strength/1000) * (attacker_army.backline[i].off_fire / defender_army.frontline[i].tactics) * (1 + attacker_army.backline[i].combat_ability) * (1+attack_discipline) * (1+(total_days+1/100))
                        morale_casualties_art_at = ((15+5*pips_art_at) * multiplier_art_at * (attacker_army.backline[i].morale/540) + 0.03 )/40
                        str_casualties_art_at = ((15 + 5* pips_art_at) * multiplier_art_at)/40
                            
                        defender_army.frontline[i].morale -= morale_casualties_art_at
                        defender_army.frontline[i].strength -= str_casualties_art_at
                        army_size -= str_casualties_art_at                                
                        moralesum -= morale_casualties_art_at
                
                        
                        
        elif len(attacker_army.backline) < len(defender_army.backline):
            for i in range(len(attacker_army.backline)):
                    #how much damage defender art does to attacker frontline
                if isinstance(defender_army.backline[i],infantry.Artillery):
                        #if index of the art matches up to an index of enemy front line
                    if (0 <= i) and (i <len(attacker_army.frontline)):
                        pips_art = dice_roll + max(0,ldr_fire-attack_ldr_fire) + defender_army.backline[i].off_fire - attacker_army.frontline[i].def_fire
                        multiplier_art = (defender_army.backline[i].strength/1000) * (defender_army.backline[i].off_fire / attacker_army.frontline[i].tactics) * (1 + defender_army.backline[i].combat_ability) * (1+discipline) * (1+(total_days+1/100))
                        morale_casualties_art = ((15+5*pips_art) * multiplier_art * (defender_army.backline[i].morale/540) + 0.03 )/40
                        str_casualties_art = ((15 + 5* pips_art) * multiplier_art)/40
                        attacker_army.frontline[i].morale -= morale_casualties_art
                        attacker_army.frontline[i].strength -= str_casualties_art
                        attack_size -= str_casualties_art
                        attack_m_sum -= morale_casualties_art
                                
                                
                        #how much dmg attacker art does to defender frontline
                if isinstance(attacker_army.backline[i],infantry.Artillery):
                            #if index of the art matches up to an index of enemy front line
                    if (0 <= i) and (i <len(defender_army.frontline)):
                        pips_art_at = att_dice_roll + max(0,attack_ldr_fire-ldr_fire) + attacker_army.backline[i].off_fire - defender_army.frontline[i].def_fire
                        multiplier_art_at = (attacker_army.backline[i].strength/1000) * (attacker_army.backline[i].off_fire / defender_army.frontline[i].tactics) * (1 + attacker_army.backline[i].combat_ability) * (1+attack_discipline) * (1+(total_days+1/100))
                        morale_casualties_art_at = ((15+5*pips_art_at) * multiplier_art_at * (attacker_army.backline[i].morale/540) + 0.03 )/40
                        str_casualties_art_at = ((15 + 5* pips_art_at) * multiplier_art_at)/40
                            
                        defender_army.frontline[i].morale -= morale_casualties_art_at
                        defender_army.frontline[i].strength -= str_casualties_art_at
                        army_size -= str_casualties_art_at                                
                        moralesum -= morale_casualties_art_at
                  
        else: break                                
                        
        
        for i in range(len(attacker_army.backline)):
            #backline damage to morale        
                attacker_army.backline[i].morale = ((attack_moral/540) + 0.03)/20
                attack_m_sum -=  ((attack_moral/540) + 0.03)/20      
        for i in range(len(defender_army.backline)):
            #backline damage to morale        
                defender_army.backline[i].morale = ((moral/540) + 0.03)/20
                moralesum -=  ((moral/540) + 0.03)/20
        for i in range(len(defender_army.reserves)):
            #reserves dmg to morale
            defender_army.reserves[i].morale = ((moral/540) + 0.03)/20
            moralesum -=  ((moral/540) + 0.03)/20
        for i in range(len(attacker_army.reserves)):
            #reserves damage to morale        
                attacker_army.reserves[i].morale = ((attack_moral/540) + 0.03)/20
                attack_m_sum -=  ((attack_moral/540) + 0.03)/20      
        #will do for loops that go thro front and bacvklines and check if unit has morale less than 0 or str less than 0 then it will replacfe
        #will do 4 different for loops fo each thing                                                  
        
                #now replace depleted units                        
                #then copy it all into shock phase
                 #once i finish this battle, i will need to HARD CODE ALL UNITS AND GROUPS and ADD A GUI
            
    if shock_phase == True:
        pass
    
    
    total_days +=1
    #resets phases every 3 days
    if phase_interval ==3 and fire_phase == True:
        fire_phase = False
        phase_interval = 0
        shock_phase = True
    if phase_interval and shock_phase == True:
        fire_phase = True
        phase_interval = 0
        shock_phase = False    
    
print(total_days)    
for unit in range(len(attacker_army.frontline)):
    print(attacker_army.frontline[unit].morale)
    print(attacker_army.frontline[unit].strength)    
    
print('======')
for unit in range(len(defender_army.frontline)):
    print(defender_army.frontline[unit].morale)
    print(defender_army.frontline[unit].strength)
print('=====')    
print(moralesum)
print(army_size)
print(attack_size)
print(attack_m_sum)        
    

#THINGS TO FIX ONCE EVERYTHING IS FINISHED:
#for morale casualties it sohuld be max morale/540 not .morale/540
#need to use morale def and off pips for morale casualties


        