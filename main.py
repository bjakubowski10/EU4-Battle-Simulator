from battleline import Army
from threading import Thread
import infantry
import random


#defender
#print("Defender Side")
#inf = int(input('Amount of infantry -'))
#cav = int(input("Amount of cavalry - "))
#art = int(input('Amount of artillery - '))
#inf_combat = float(input("Infantry combat ability - "))
#cav_combat = float(input("Cavalry combat ability - "))
#art_combat = float(input("Artillery combat ability - "))
#tech = int(input("Tech level - "))
#moral = float(input("Morale - "))
#discipline = float(input("Discipline - "))
#ldr_fire = int(input("Leader Fire - "))
#ldr_shock = int(input("leader shock - "))
#inf_u_name = input("Infantry Unit name -")
#cav_u_name = input("Cavalry Unit name - ")
#art_u_name = input("Artillery Unit name - ")
#print("==================")
#attack
#print("Attacker Side")

#attack_inf = int(input('Amount of infantry -'))
#attack_cav = int(input("Amount of cavalry - "))
#attack_art = int(input('Amount of artillery - '))
#attack_inf_combat = float(input("Infantry combat ability - "))
#attack_cav_combat = float(input("Cavalry combat ability - "))
#attack_art_combat = float(input("Artillery combat ability - "))
#attack_tech = int(input("Tech level - "))
#attack_moral = float(input("Morale - "))
#attack_discipline = float(input("Discipline - "))
#attack_ldr_fire = int(input("Leader fire - "))
#attack_ldr_shock = int(input("Leader shock - "))
#attack_inf_u_name = input("Infantry Unit name -")
#attack_cav_u_name = input("Cavalry Unit name - ")
#attack_art_u_name = input("Artillery Unit name - ")

#terrain = int(input("Terrain modifier - "))

def entire_battle_calculation(inf,cav,art,inf_combat,cav_combat,art_combat,tech,moral,inf_u_name,cav_u_name,art_u_name,attack_inf,attack_cav,discipline,attack_art,
                              attack_inf_combat,attack_cav_combat,attack_art_combat,attack_tech,attack_moral,attack_inf_u_name,attack_discipline,attack_cav_u_name,attack_art_u_name,terrain,ldr_fire,ldr_shock,attack_ldr_fire,attack_ldr_shock):

   defender_army = Army(inf,inf_combat,cav_combat,art_combat,cav,art,tech,moral,inf_u_name,cav_u_name,art_u_name)
   attacker_army = Army(attack_inf,attack_inf_combat,attack_cav_combat,attack_art_combat,attack_cav,attack_art,attack_tech,attack_moral,attack_inf_u_name,attack_cav_u_name,attack_art_u_name)
   
   #fill the front and backlines
   defender_army.fill_front_back_line()
   attacker_army.fill_front_back_line()
   
   army_size,moralesum = defender_army.morale_and_troop_count()
   attack_size,attack_m_sum = attacker_army.morale_and_troop_count()
   
   #army_size,moralesum = defender_army.tester()
   #attack_size,attack_m_sum = attacker_army.tester()
   
   
   #need a way to replace units
   #maybe just insert morale into the function and substract from it ?
   #need to have units fight, fuck flanking 
   losses_def = 0
   losses_att = 0
   fire_phase = True
   shock_phase = False
   total_days = 0
   phase_interval = 0
   
   
   while (army_size > 0 and attack_size > 0 and moralesum > 0 and attack_m_sum > 0):
       
       phase_interval +=1
       if fire_phase == True:
           deflen = len(defender_army.frontline)
           attlen = len(attacker_army.frontline)
           dice_roll = random.randint(0,9)
           att_dice_roll = max(0,random.randint(0,9) - terrain)
           #if att_dice_roll < 0 :  att_dice_roll=0
           
           if deflen <= attlen:
               for i in range(len(defender_army.frontline)):
                   #how much damage defenders deal
                   pips = dice_roll + max(0,ldr_fire-attack_ldr_fire) + defender_army.frontline[i].off_fire - attacker_army.frontline[i].def_fire
                   multiplier = (defender_army.frontline[i].strength / 1000) * (defender_army.frontline[i].off_fire / attacker_army.frontline[i].tactics) * (1 + defender_army.frontline[i].combat_ability) * ( 1 + discipline) * (1 + (total_days+1)/100)
                   morale_casualties = ((15 + 5 * pips) * multiplier * (defender_army.frontline[i].morale/540) + 0.03)/25
                   str_casualties = ((15 + 5*pips) * multiplier)/25
                   
                   #how much dmg attacker deal
                   att_pips = att_dice_roll + max(0,attack_ldr_fire-ldr_fire) + attacker_army.frontline[i].off_fire - defender_army.frontline[i].def_fire
                   att_multiplier = (attacker_army.frontline[i].strength / 1000) * (attacker_army.frontline[i].off_fire / defender_army.frontline[i].tactics) * (1 + attacker_army.frontline[i].combat_ability) * ( 1 + attack_discipline) * (1 + (total_days+1)/100)
                   att_morale_casualties = ((15 + 5 * att_pips) * att_multiplier * (attacker_army.frontline[i].morale/540) + 0.03)/25
                   att_str_casualties = ((15 + 5*att_pips) * att_multiplier)/25
                   
                   
                   if att_morale_casualties > defender_army.frontline[i].morale: 
                       moralesum -= defender_army.frontline[i].morale
                       defender_army.frontline[i].morale -= att_morale_casualties
                   else: 
                       defender_army.frontline[i].morale -= att_morale_casualties
                       moralesum -= att_morale_casualties
                   if att_str_casualties > defender_army.frontline[i].strength:
                       army_size -= defender_army.frontline[i].strength
                       defender_army.frontline[i].strength -= att_str_casualties
                   else:
                       defender_army.frontline[i].strength -= att_str_casualties
                       army_size -= att_str_casualties
                   
                   if morale_casualties > attacker_army.frontline[i].morale:
                       attack_m_sum -= attacker_army.frontline[i].morale
                       attacker_army.frontline[i].morale -= morale_casualties
                       
                   else:
                       attacker_army.frontline[i].morale -= morale_casualties
                       attack_m_sum -= morale_casualties
                   if str_casualties > attacker_army.frontline[i].strength:
                       attack_size -= attacker_army.frontline[i].strength
                       attacker_army.frontline[i].strength -= str_casualties
                       
                   else:
                       attacker_army.frontline[i].strength -= str_casualties
                       attack_size -= str_casualties
                   losses_att += str_casualties
                   losses_def += att_str_casualties                    
                           
                   
           elif attlen < deflen:
               for i in range(len(attacker_army.frontline)):
                   #how much damage defenders deal
                   pips = dice_roll + max(0,ldr_fire-attack_ldr_fire) + defender_army.frontline[i].off_fire - attacker_army.frontline[i].def_fire
                   multiplier = (defender_army.frontline[i].strength / 1000) * (defender_army.frontline[i].off_fire / attacker_army.frontline[i].tactics) * (1 + defender_army.frontline[i].combat_ability) * ( 1 + discipline) * (1 + (total_days+1)/100)
                   morale_casualties = ((15 + 5 * pips) * multiplier * (defender_army.frontline[i].morale/540) + 0.03)/25
                   str_casualties = ((15 + 5*pips) * multiplier)/25
                   
                   #how much dmg attacker deal
                   att_pips = att_dice_roll + max(0,attack_ldr_fire-ldr_fire) + attacker_army.frontline[i].off_fire - defender_army.frontline[i].def_fire
                   att_multiplier = (attacker_army.frontline[i].strength / 1000) * (attacker_army.frontline[i].off_fire / defender_army.frontline[i].tactics) * (1 + attacker_army.frontline[i].combat_ability) * ( 1 + attack_discipline) * (1 + (total_days+1)/100)
                   att_morale_casualties = ((15 + 5 * att_pips) * att_multiplier * (attacker_army.frontline[i].morale/540) + 0.03)/25
                   att_str_casualties = ((15 + 5*att_pips) * att_multiplier)/25
                   
                   if att_morale_casualties > defender_army.frontline[i].morale: 
                       moralesum -= defender_army.frontline[i].morale
                       defender_army.frontline[i].morale -= att_morale_casualties
                       
                   else: 
                       defender_army.frontline[i].morale -= att_morale_casualties
                       moralesum -= att_morale_casualties
                   if att_str_casualties > defender_army.frontline[i].strength:
                       army_size -= defender_army.frontline[i].strength
                       defender_army.frontline[i].strength =- att_str_casualties
                       
                   else:
                       defender_army.frontline[i].strength -= att_str_casualties
                       army_size -= att_str_casualties
                   
                   if morale_casualties > attacker_army.frontline[i].morale:
                       attack_m_sum -= attacker_army.frontline[i].morale
                       attacker_army.frontline[i].morale -= morale_casualties
                       
                   else:
                       attacker_army.frontline[i].morale -= morale_casualties
                       attack_m_sum -= morale_casualties
                   if str_casualties > attacker_army.frontline[i].strength:
                       attack_size -= attacker_army.frontline[i].strength
                       attacker_army.frontline[i].strength -=str_casualties
                       
                   else:
                       attacker_army.frontline[i].strength -= str_casualties
                       attack_size -= str_casualties
                   losses_att += str_casualties
                   losses_def += att_str_casualties                    
           else: break                
                   
          
           if len(defender_army.backline) < len(attacker_army.backline):
               for i in range(len(defender_army.backline)):
                       #how much damage defender art does to attacker frontline
                   if isinstance(defender_army.backline[i],infantry.Artillery):
                           #if index of the art matches up to an index of enemy front line
                       if (0 <= i) and (i <len(attacker_army.frontline)):
                           pips_art = dice_roll + max(0,ldr_fire-attack_ldr_fire) + defender_army.backline[i].off_fire - attacker_army.frontline[i].def_fire
                           multiplier_art = (defender_army.backline[i].strength/1000) * (defender_army.backline[i].off_fire / attacker_army.frontline[i].tactics) * (1 + defender_army.backline[i].combat_ability) * (1+discipline) * (1+(total_days+1/100))
                           morale_casualties_art = ((15+5*pips_art) * multiplier_art * (defender_army.backline[i].morale/540) + 0.03 )/50
                           str_casualties_art = ((15 + 5* pips_art) * multiplier_art)/50
                           
                           if morale_casualties_art > attacker_army.frontline[i].morale:
                               attack_m_sum -= attacker_army.frontline[i].morale
                               attacker_army.frontline[i].morale -= morale_casualties_art
                               
                           else:
                               attacker_army.frontline[i].morale -= morale_casualties_art
                               attack_m_sum -= morale_casualties_art
                           if str_casualties_art > attacker_army.frontline[i].strength:
                               attack_size -= attacker_army.frontline[i].strength
                               attacker_army.frontline[i].strength -= str_casualties_art
                               
                           else: 
                               attacker_army.frontline[i].strength -= str_casualties_art
                               attack_size -= str_casualties_art
                           losses_att += str_casualties_art
                                   
                                   
                           #how much dmg attacker art does to defender frontline
                   if isinstance(attacker_army.backline[i],infantry.Artillery):
                               #if index of the art matches up to an index of enemy front line
                       if (0 <= i) and (i <len(defender_army.frontline)):
                           pips_art_at = att_dice_roll + max(0,attack_ldr_fire-ldr_fire) + attacker_army.backline[i].off_fire - defender_army.frontline[i].def_fire
                           multiplier_art_at = (attacker_army.backline[i].strength/1000) * (attacker_army.backline[i].off_fire / defender_army.frontline[i].tactics) * (1 + attacker_army.backline[i].combat_ability) * (1+attack_discipline) * (1+(total_days+1/100))
                           morale_casualties_art_at = ((15+5*pips_art_at) * multiplier_art_at * (attacker_army.backline[i].morale/540) + 0.03 )/50
                           str_casualties_art_at = ((15 + 5* pips_art_at) * multiplier_art_at)/50
                               
                           if morale_casualties_art_at > defender_army.frontline[i].morale:
                               moralesum -= defender_army.frontline[i].morale
                               defender_army.frontline[i].morale -= morale_casualties_art_at
                               
                           else:
                               defender_army.frontline[i].morale -= morale_casualties_art_at
                               moralesum -= morale_casualties_art_at
                           if str_casualties_art_at > defender_army.frontline[i].strength:
                               
                               army_size -= defender_army.frontline[i].strength
                               defender_army.frontline[i].strength -= str_casualties_art_at
                               
                           else: 
                               defender_army.frontline[i].strength -= str_casualties_art_at
                               army_size -= str_casualties_art_at
                           losses_def += str_casualties_art_at    
                       else: continue           
                               
               for i in range(len(defender_army.backline),len(attacker_army.backline)):
                   if isinstance(attacker_army.backline[i],infantry.Artillery):
                       if (0 <= i) and (i <len(defender_army.frontline)):
                           pips_art_at = att_dice_roll + max(0,attack_ldr_fire-ldr_fire) + attacker_army.backline[i].off_fire - defender_army.frontline[i].def_fire
                           multiplier_art_at = (attacker_army.backline[i].strength/1000) * (attacker_army.backline[i].off_fire / defender_army.frontline[i].tactics) * (1 + attacker_army.backline[i].combat_ability) * (1+attack_discipline) * (1+(total_days+1/100))
                           morale_casualties_art_at = ((15+5*pips_art_at) * multiplier_art_at * (attacker_army.backline[i].morale/540) + 0.03 )/50
                           str_casualties_art_at = ((15 + 5* pips_art_at) * multiplier_art_at)/50
                               
                           if morale_casualties_art_at > defender_army.frontline[i].morale:
                               moralesum -= defender_army.frontline[i].morale
                               defender_army.frontline[i].morale -= morale_casualties_art_at
                               
                           else:
                               defender_army.frontline[i].morale -= morale_casualties_art_at
                               moralesum -= morale_casualties_art_at
                           if str_casualties_art_at > defender_army.frontline[i].strength:
                               army_size -= defender_army.frontline[i].strength
                               defender_army.frontline[i].strength -= str_casualties_art_at
                               
                           else: 
                               defender_army.frontline[i].strength -= str_casualties_art_at
                               army_size -= str_casualties_art_at  
                           losses_def += str_casualties_art_at     
                       else: continue    
                           
           elif len(attacker_army.backline) < len(defender_army.backline):
               for i in range(len(attacker_army.backline)):
                       #how much damage defender art does to attacker frontline
                   if isinstance(defender_army.backline[i],infantry.Artillery):
                           #if index of the art matches up to an index of enemy front line
                       if (0 <= i) and (i <len(attacker_army.frontline)):
                           pips_art = dice_roll + max(0,ldr_fire-attack_ldr_fire) + defender_army.backline[i].off_fire - attacker_army.frontline[i].def_fire
                           multiplier_art = (defender_army.backline[i].strength/1000) * (defender_army.backline[i].off_fire / attacker_army.frontline[i].tactics) * (1 + defender_army.backline[i].combat_ability) * (1+discipline) * (1+(total_days+1/100))
                           morale_casualties_art = ((15+5*pips_art) * multiplier_art * (defender_army.backline[i].morale/540) + 0.03 )/50
                           str_casualties_art = ((15 + 5* pips_art) * multiplier_art)/50
                           
                           if morale_casualties_art > attacker_army.frontline[i].morale:
                               attack_m_sum -= attacker_army.frontline[i].morale
                               attacker_army.frontline[i].morale -= morale_casualties_art
                               
                           else:
                               attacker_army.frontline[i].morale -= morale_casualties_art
                               attack_m_sum -= morale_casualties_art
                           if str_casualties_art > attacker_army.frontline[i].strength:
                               attack_size -= attacker_army.frontline[i].strength
                               attacker_army.frontline[i].strength -= str_casualties_art
                               
                           else: 
                               attacker_army.frontline[i].strength -= str_casualties_art
                               attack_size -= str_casualties_art
                           losses_att += str_casualties_art
                           #how much dmg attacker art does to defender frontline
                   if isinstance(attacker_army.backline[i],infantry.Artillery):
                               #if index of the art matches up to an index of enemy front line
                       if (0 <= i) and (i <len(defender_army.frontline)):
                           pips_art_at = att_dice_roll + max(0,attack_ldr_fire-ldr_fire) + attacker_army.backline[i].off_fire - defender_army.frontline[i].def_fire
                           multiplier_art_at = (attacker_army.backline[i].strength/1000) * (attacker_army.backline[i].off_fire / defender_army.frontline[i].tactics) * (1 + attacker_army.backline[i].combat_ability) * (1+attack_discipline) * (1+(total_days+1/100))
                           morale_casualties_art_at = ((15+5*pips_art_at) * multiplier_art_at * (attacker_army.backline[i].morale/540) + 0.03 )/50
                           str_casualties_art_at = ((15 + 5* pips_art_at) * multiplier_art_at)/50
                               
                           if morale_casualties_art_at > defender_army.frontline[i].morale:
                               moralesum -= defender_army.frontline[i].morale
                               defender_army.frontline[i].morale -= morale_casualties_art_at
                               
                           else:
                               defender_army.frontline[i].morale -= morale_casualties_art_at
                               moralesum -= morale_casualties_art_at
                           if str_casualties_art_at > defender_army.frontline[i].strength:
                               army_size -= defender_army.frontline[i].strength
                               defender_army.frontline[i].strength -= str_casualties_art_at
                               
                           else: 
                               defender_army.frontline[i].strength -= str_casualties_art_at
                               army_size -= str_casualties_art_at 
                           losses_def += str_casualties_art_at      
                   else: continue          
               for i in range(len(attacker_army.backline),len(defender_army.backline)):
                   if isinstance(defender_army.backline[i],infantry.Artillery):
                        if (0 <= i) and (i <len(attacker_army.frontline)):
                           pips_art = dice_roll + max(0,ldr_fire-attack_ldr_fire) + defender_army.backline[i].off_fire - attacker_army.frontline[i].def_fire
                           multiplier_art = (defender_army.backline[i].strength/1000) * (defender_army.backline[i].off_fire / attacker_army.frontline[i].tactics) * (1 + defender_army.backline[i].combat_ability) * (1+discipline) * (1+(total_days+1/100))
                           morale_casualties_art = ((15+5*pips_art) * multiplier_art * (defender_army.backline[i].morale/540) + 0.03 )/50
                           str_casualties_art = ((15 + 5* pips_art) * multiplier_art)/50
                           
                           if morale_casualties_art > attacker_army.frontline[i].morale:
                               attack_m_sum -= attacker_army.frontline[i].morale
                               attacker_army.frontline[i].morale -= morale_casualties_art
                               
                           else:
                               attacker_army.frontline[i].morale -= morale_casualties_art
                               attack_m_sum -= morale_casualties_art
                           if str_casualties_art > attacker_army.frontline[i].strength:
                               attack_size -= attacker_army.frontline[i].strength
                               attacker_army.frontline[i].strength -= str_casualties_art
                               
                           else: 
                               attacker_army.frontline[i].strength -= str_casualties_art
                               attack_size -= str_casualties_art  
                           losses_att += str_casualties_art
                   else: continue          
           else:
                     
               for i in range(len(attacker_army.backline)):
                       #how much damage defender art does to attacker frontline
                   if isinstance(defender_army.backline[i],infantry.Artillery):
                           #if index of the art matches up to an index of enemy front line
                       if (0 <= i) and (i <len(attacker_army.frontline)):
                           pips_art = dice_roll + max(0,ldr_fire-attack_ldr_fire) + defender_army.backline[i].off_fire - attacker_army.frontline[i].def_fire
                           multiplier_art = (defender_army.backline[i].strength/1000) * (defender_army.backline[i].off_fire / attacker_army.frontline[i].tactics) * (1 + defender_army.backline[i].combat_ability) * (1+discipline) * (1+(total_days+1/100))
                           morale_casualties_art = ((15+5*pips_art) * multiplier_art * (defender_army.backline[i].morale/540) + 0.03 )/50
                           str_casualties_art = ((15 + 5* pips_art) * multiplier_art)/50
                           
                           if morale_casualties_art > attacker_army.frontline[i].morale:
                               attack_m_sum -= attacker_army.frontline[i].morale
                               attacker_army.frontline[i].morale -= morale_casualties_art
                               
                           else:
                               attacker_army.frontline[i].morale -= morale_casualties_art
                               attack_m_sum -= morale_casualties_art
                           if str_casualties_art > attacker_army.frontline[i].strength:
                               attack_size -= attacker_army.frontline[i].strength
                               attacker_army.frontline[i].strength -= str_casualties_art
                               
                           else: 
                               attacker_army.frontline[i].strength -= str_casualties_art
                               attack_size -= str_casualties_art
                           losses_att += str_casualties_art
                                   
                           #how much dmg attacker art does to defender frontline
                   if isinstance(attacker_army.backline[i],infantry.Artillery):
                               #if index of the art matches up to an index of enemy front line
                       if (0 <= i) and (i <len(defender_army.frontline)):
                           pips_art_at = att_dice_roll + max(0,attack_ldr_fire-ldr_fire) + attacker_army.backline[i].off_fire - defender_army.frontline[i].def_fire
                           multiplier_art_at = (attacker_army.backline[i].strength/1000) * (attacker_army.backline[i].off_fire / defender_army.frontline[i].tactics) * (1 + attacker_army.backline[i].combat_ability) * (1+attack_discipline) * (1+(total_days+1/100))
                           morale_casualties_art_at = ((15+5*pips_art_at) * multiplier_art_at * (attacker_army.backline[i].morale/540) + 0.03 )/50
                           str_casualties_art_at = ((15 + 5* pips_art_at) * multiplier_art_at)/50
                               
                           if morale_casualties_art_at > defender_army.frontline[i].morale:
                               moralesum -= defender_army.frontline[i].morale
                               defender_army.frontline[i].morale -= morale_casualties_art_at
                               
                           else:
                               defender_army.frontline[i].morale -= morale_casualties_art_at
                               moralesum -= morale_casualties_art_at
                           if str_casualties_art_at > defender_army.frontline[i].strength:
                               army_size -= defender_army.frontline[i].strength
                               defender_army.frontline[i].strength -= str_casualties_art_at
                               
                           else: 
                               defender_army.frontline[i].strength -= str_casualties_art_at
                               army_size -= str_casualties_art_at 
                           losses_def += str_casualties_art_at                              
                   else:continue        
           
           for i in range(len(attacker_army.backline)):
               #backline damage to morale
               if ( ((attack_moral/540) + 0.03)*5) > attacker_army.backline[i].morale:
                   attack_m_sum -= abs(attacker_army.backline[i].morale)
                   attacker_army.backline[i].morale -= ((attack_moral/540) + 0.03)*2
               else:         
                   attacker_army.backline[i].morale -= ((attack_moral/540) + 0.03)*2
                   attack_m_sum -=  ((attack_moral/540) + 0.03)*2   
           for i in range(len(defender_army.backline)):
               
               #backline damage to morale
               if (((moral/540) + 0.03)*5) > defender_army.backline[i].morale:
                   moralesum -= abs(defender_army.backline[i].morale)
                   defender_army.backline[i].morale -= (((moral/540) + 0.03)*2)
               else:             
                   defender_army.backline[i].morale -= ((moral/540) + 0.03)*2
                   moralesum -=  ((moral/540) + 0.03)*2
           for i in range(len(defender_army.reserves)):
               #reserves dmg to morale
               if (((moral/540) + 0.03)*5) > defender_army.reserves[i].morale:
                   moralesum -= abs(defender_army.reserves[i].morale)
                   defender_army.reserves[i].morale -= ((moral/540) + 0.03)*2
               else:
                   defender_army.reserves[i].morale -= ((moral/540) + 0.03)*2
                   moralesum -=  ((moral/540) + 0.03)*2
           for i in range(len(attacker_army.reserves)):
               #reserves damage to morale
               if (((attack_moral/540) + 0.03)*5) > attacker_army.reserves[i].morale:
                   attack_m_sum -=  abs(attacker_army.reserves[i].morale)
                   attacker_army.reserves[i].morale -= ((attack_moral/540) + 0.03)*2
               else:           
                   attacker_army.reserves[i].morale -= ((attack_moral/540) + 0.03)*2
                   attack_m_sum -=  ((attack_moral/540) + 0.03)*2   
          
                                     
                   #then copy it all into shock phase 
                   
            #checking for units in need of replacement
           ii = 0              
           while ii < len(attacker_army.frontline):
               if attacker_army.frontline[ii].morale <= 0 or attacker_army.frontline[ii].strength <= 0:
                   if attacker_army.frontline[ii].morale > 0:
                       attack_m_sum -= attacker_army.frontline[ii].morale
                   if attacker_army.frontline[ii].strength > 0:
                       attack_size -= attacker_army.frontline[ii].strength     
                   
                   if len(attacker_army.reserves) > 0:
                       #attacker_army.frontline[ii] = attacker_army.reserves[0]
                       attacker_army.frontline.append(attacker_army.reserves[0])
                       attacker_army.reserves.remove(attacker_army.reserves[0])
                       attacker_army.frontline.remove(attacker_army.frontline[ii])
                       #ii-=1
                       
                   else:    
                       attacker_army.frontline.remove(attacker_army.frontline[ii])
                       #ii -= 1
               else:ii += 1
               if ii < 0 : ii=0
           ii = 0        
           while ii < len(attacker_army.backline):
               if attacker_army.backline[ii].morale <= 0 or attacker_army.backline[ii].strength <= 0:
                   if attacker_army.backline[ii].morale > 0:
                       attack_m_sum -= attacker_army.backline[ii].morale
                   if attacker_army.backline[ii].strength > 0:
                       attack_size -= attacker_army.backline[ii].strength
                   if len(attacker_army.reserves) > 0:
                       #attacker_army.backline[ii] = attacker_army.reserves[0]
                       attacker_army.backline.append(attacker_army.reserves[-1])
                       attacker_army.reserves.remove(attacker_army.reserves[-1])
                       attacker_army.backline.remove(attacker_army.backline[ii])
                       #ii-=1
                   else:    
                       attacker_army.backline.remove(attacker_army.backline[ii])
                       #ii -= 1
               else:ii += 1
               if ii < 0: ii = 0
           ii = 0        
           while ii < len(defender_army.frontline):
               if defender_army.frontline[ii].morale <= 0 or defender_army.frontline[ii].strength <= 0:
                   if defender_army.frontline[ii].morale > 0:
                       moralesum -= defender_army.frontline[ii].morale
                   if defender_army.frontline[ii].strength > 0:
                       army_size -= defender_army.frontline[ii].strength
                   if len(defender_army.reserves) > 0:
                       #defender_army.frontline[ii] = defender_army.reserves[0]
                       #defender_army.reserves.remove(defender_army.reserves[0])
                       defender_army.frontline.append(defender_army.reserves[0])
                       defender_army.reserves.remove(defender_army.reserves[0])
                       defender_army.frontline.remove(defender_army.frontline[ii])
                       #ii-=1
                   else:    
                       defender_army.frontline.remove(defender_army.frontline[ii])
                       #ii -= 1
               else:ii += 1
               if ii < 0: ii = 0 
           ii = 0       
           while ii < len(defender_army.backline):
               if defender_army.backline[ii].morale <= 0 or defender_army.backline[ii].strength <= 0:
                   if defender_army.backline[ii].morale > 0:
                       moralesum -= defender_army.backline[ii].morale
                   if defender_army.backline[ii].strength > 0:
                       army_size -= defender_army.backline[ii].strength
                   if len(defender_army.reserves) > 0:
                       #defender_army.backline[ii] = defender_army.reserves[0]
                       #defender_army.reserves.remove(defender_army.reserves[0])
                       defender_army.backline.append(defender_army.reserves[-1])
                       defender_army.reserves.remove(defender_army.reserves[-1])
                       defender_army.backline.remove(defender_army.backline[ii])
                       #ii-=1
                   else:    
                       defender_army.backline.remove(defender_army.backline[ii])
                       #ii -= 1
               else:ii += 1
               if ii < 0: ii = 0                      
                            
               
       if shock_phase == True:
           deflen = len(defender_army.frontline)
           attlen = len(attacker_army.frontline)
           dice_roll = random.randint(0,9)
           att_dice_roll = max(0,random.randint(0,9) - terrain)
           #if att_dice_roll < 0 :  att_dice_roll=0
           
           if deflen <= attlen:
               for i in range(len(defender_army.frontline)):
                   #how much damage defenders deal
                   pips = dice_roll + max(0,ldr_shock-attack_ldr_shock) + defender_army.frontline[i].off_shock - attacker_army.frontline[i].def_shock
                   multiplier = (defender_army.frontline[i].strength / 1000) * (defender_army.frontline[i].off_shock / attacker_army.frontline[i].tactics) * (1 + defender_army.frontline[i].combat_ability) * ( 1 + discipline) * (1 + (total_days+1)/100)
                   morale_casualties = ((15 + 5 * pips) * multiplier * (defender_army.frontline[i].morale/540) + 0.03)/25
                   str_casualties = ((15 + 5*pips) * multiplier)/25
                   
                   #how much dmg attacker deal
                   att_pips = att_dice_roll + max(0,attack_ldr_shock-ldr_shock) + attacker_army.frontline[i].off_shock - defender_army.frontline[i].def_shock
                   att_multiplier = (attacker_army.frontline[i].strength / 1000) * (attacker_army.frontline[i].off_shock / defender_army.frontline[i].tactics) * (1 + attacker_army.frontline[i].combat_ability) * ( 1 + attack_discipline) * (1 + (total_days+1)/100)
                   att_morale_casualties = ((15 + 5 * att_pips) * att_multiplier * (attacker_army.frontline[i].morale/540) + 0.03)/25
                   att_str_casualties = ((15 + 5*att_pips) * att_multiplier)/25
                   
                   
                   if att_morale_casualties > defender_army.frontline[i].morale: 
                       moralesum -= defender_army.frontline[i].morale
                       defender_army.frontline[i].morale -= att_morale_casualties
                   else: 
                       defender_army.frontline[i].morale -= att_morale_casualties
                       moralesum -= att_morale_casualties
                   if att_str_casualties > defender_army.frontline[i].strength:
                       army_size -= defender_army.frontline[i].strength
                       defender_army.frontline[i].strength -= att_str_casualties
                   else:
                       defender_army.frontline[i].strength -= att_str_casualties
                       army_size -= att_str_casualties
                   
                   if morale_casualties > attacker_army.frontline[i].morale:
                       attack_m_sum -= attacker_army.frontline[i].morale
                       attacker_army.frontline[i].morale -= morale_casualties
                       
                   else:
                       attacker_army.frontline[i].morale -= morale_casualties
                       attack_m_sum -= morale_casualties
                   if str_casualties > attacker_army.frontline[i].strength:
                       attack_size -= attacker_army.frontline[i].strength
                       attacker_army.frontline[i].strength -= str_casualties
                       
                   else:
                       attacker_army.frontline[i].strength -= str_casualties
                       attack_size -= str_casualties   
                   losses_att += str_casualties
                   losses_def += att_str_casualties                 
                           
                   
           elif attlen < deflen:
               for i in range(len(attacker_army.frontline)):
                   #how much damage defenders deal
                   pips = dice_roll + max(0,ldr_shock-attack_ldr_shock) + defender_army.frontline[i].off_shock - attacker_army.frontline[i].def_shock
                   multiplier = (defender_army.frontline[i].strength / 1000) * (defender_army.frontline[i].off_shock / attacker_army.frontline[i].tactics) * (1 + defender_army.frontline[i].combat_ability) * ( 1 + discipline) * (1 + (total_days+1)/100)
                   morale_casualties = ((15 + 5 * pips) * multiplier * (defender_army.frontline[i].morale/540) + 0.03)/25
                   str_casualties = ((15 + 5*pips) * multiplier)/25
                   
                   #how much dmg attacker deal
                   att_pips = att_dice_roll + max(0,attack_ldr_shock-ldr_shock) + attacker_army.frontline[i].off_shock - defender_army.frontline[i].def_shock
                   att_multiplier = (attacker_army.frontline[i].strength / 1000) * (attacker_army.frontline[i].off_shock / defender_army.frontline[i].tactics) * (1 + attacker_army.frontline[i].combat_ability) * ( 1 + attack_discipline) * (1 + (total_days+1)/100)
                   att_morale_casualties = ((15 + 5 * att_pips) * att_multiplier * (attacker_army.frontline[i].morale/540) + 0.03)/25
                   att_str_casualties = ((15 + 5*att_pips) * att_multiplier)/25
                   
                   if att_morale_casualties > defender_army.frontline[i].morale: 
                       moralesum -= defender_army.frontline[i].morale
                       defender_army.frontline[i].morale -= att_morale_casualties
                       
                   else: 
                       defender_army.frontline[i].morale -= att_morale_casualties
                       moralesum -= att_morale_casualties
                   if att_str_casualties > defender_army.frontline[i].strength:
                       army_size -= defender_army.frontline[i].strength
                       defender_army.frontline[i].strength =- att_str_casualties
                       
                   else:
                       defender_army.frontline[i].strength -= att_str_casualties
                       army_size -= att_str_casualties
                   
                   if morale_casualties > attacker_army.frontline[i].morale:
                       attack_m_sum -= attacker_army.frontline[i].morale
                       attacker_army.frontline[i].morale -= morale_casualties
                       
                   else:
                       attacker_army.frontline[i].morale -= morale_casualties
                       attack_m_sum -= morale_casualties
                   if str_casualties > attacker_army.frontline[i].strength:
                       attack_size -= attacker_army.frontline[i].strength
                       attacker_army.frontline[i].strength -=str_casualties
                       
                   else:
                       attacker_army.frontline[i].strength -= str_casualties
                       attack_size -= str_casualties  
                   losses_att += str_casualties
                   losses_def += att_str_casualties                  
           else: break                
                   
          
           if len(defender_army.backline) < len(attacker_army.backline):
               for i in range(len(defender_army.backline)):
                       #how much damage defender art does to attacker frontline
                   if isinstance(defender_army.backline[i],infantry.Artillery):
                           #if index of the art matches up to an index of enemy front line
                       if (0 <= i) and (i <len(attacker_army.frontline)):
                           pips_art = dice_roll + max(0,ldr_shock-attack_ldr_shock) + defender_army.backline[i].off_shock - attacker_army.frontline[i].def_shock
                           multiplier_art = (defender_army.backline[i].strength/1000) * (defender_army.backline[i].off_shock / attacker_army.frontline[i].tactics) * (1 + defender_army.backline[i].combat_ability) * (1+discipline) * (1+(total_days+1/100))
                           morale_casualties_art = ((15+5*pips_art) * multiplier_art * (defender_army.backline[i].morale/540) + 0.03 )/50
                           str_casualties_art = ((15 + 5* pips_art) * multiplier_art)/50
                           
                           if morale_casualties_art > attacker_army.frontline[i].morale:
                               attack_m_sum -= attacker_army.frontline[i].morale
                               attacker_army.frontline[i].morale -= morale_casualties_art
                               
                           else:
                               attacker_army.frontline[i].morale -= morale_casualties_art
                               attack_m_sum -= morale_casualties_art
                           if str_casualties_art > attacker_army.frontline[i].strength:
                               attack_size -= attacker_army.frontline[i].strength
                               attacker_army.frontline[i].strength -= str_casualties_art
                               
                           else: 
                               attacker_army.frontline[i].strength -= str_casualties_art
                               attack_size -= str_casualties_art
                           losses_att += str_casualties_art
                                   
                                   
                           #how much dmg attacker art does to defender frontline
                   if isinstance(attacker_army.backline[i],infantry.Artillery):
                               #if index of the art matches up to an index of enemy front line
                       if (0 <= i) and (i <len(defender_army.frontline)):
                           pips_art_at = att_dice_roll + max(0,attack_ldr_shock-ldr_shock) + attacker_army.backline[i].off_shock - defender_army.frontline[i].def_shock
                           multiplier_art_at = (attacker_army.backline[i].strength/1000) * (attacker_army.backline[i].off_shock / defender_army.frontline[i].tactics) * (1 + attacker_army.backline[i].combat_ability) * (1+attack_discipline) * (1+(total_days+1/100))
                           morale_casualties_art_at = ((15+5*pips_art_at) * multiplier_art_at * (attacker_army.backline[i].morale/540) + 0.03 )/50
                           str_casualties_art_at = ((15 + 5* pips_art_at) * multiplier_art_at)/50
                               
                           if morale_casualties_art_at > defender_army.frontline[i].morale:
                               moralesum -= defender_army.frontline[i].morale
                               defender_army.frontline[i].morale -= morale_casualties_art_at
                               
                           else:
                               defender_army.frontline[i].morale -= morale_casualties_art_at
                               moralesum -= morale_casualties_art_at
                           if str_casualties_art_at > defender_army.frontline[i].strength:
                               
                               army_size -= defender_army.frontline[i].strength
                               defender_army.frontline[i].strength -= str_casualties_art_at
                               
                           else: 
                               defender_army.frontline[i].strength -= str_casualties_art_at
                               army_size -= str_casualties_art_at
                           losses_def += str_casualties_art_at    
                       else: continue           
                               
               for i in range(len(defender_army.backline),len(attacker_army.backline)):
                   if isinstance(attacker_army.backline[i],infantry.Artillery):
                       if (0 <= i) and (i <len(defender_army.frontline)):
                           pips_art_at = att_dice_roll + max(0,attack_ldr_shock-ldr_shock) + attacker_army.backline[i].off_shock - defender_army.frontline[i].def_shock
                           multiplier_art_at = (attacker_army.backline[i].strength/1000) * (attacker_army.backline[i].off_shock / defender_army.frontline[i].tactics) * (1 + attacker_army.backline[i].combat_ability) * (1+attack_discipline) * (1+(total_days+1/100))
                           morale_casualties_art_at = ((15+5*pips_art_at) * multiplier_art_at * (attacker_army.backline[i].morale/540) + 0.03 )/50
                           str_casualties_art_at = ((15 + 5* pips_art_at) * multiplier_art_at)/50
                               
                           if morale_casualties_art_at > defender_army.frontline[i].morale:
                               moralesum -= defender_army.frontline[i].morale
                               defender_army.frontline[i].morale -= morale_casualties_art_at
                               
                           else:
                               defender_army.frontline[i].morale -= morale_casualties_art_at
                               moralesum -= morale_casualties_art_at
                           if str_casualties_art_at > defender_army.frontline[i].strength:
                               army_size -= defender_army.frontline[i].strength
                               defender_army.frontline[i].strength -= str_casualties_art_at
                               
                           else: 
                               defender_army.frontline[i].strength -= str_casualties_art_at
                               army_size -= str_casualties_art_at   
                           losses_def += str_casualties_art_at    
                       else: continue    
                           
           elif len(attacker_army.backline) < len(defender_army.backline):
               for i in range(len(attacker_army.backline)):
                       #how much damage defender art does to attacker frontline
                   if isinstance(defender_army.backline[i],infantry.Artillery):
                           #if index of the art matches up to an index of enemy front line
                       if (0 <= i) and (i <len(attacker_army.frontline)):
                           pips_art = dice_roll + max(0,ldr_shock-attack_ldr_shock) + defender_army.backline[i].off_shock - attacker_army.frontline[i].def_shock
                           multiplier_art = (defender_army.backline[i].strength/1000) * (defender_army.backline[i].off_shock / attacker_army.frontline[i].tactics) * (1 + defender_army.backline[i].combat_ability) * (1+discipline) * (1+(total_days+1/100))
                           morale_casualties_art = ((15+5*pips_art) * multiplier_art * (defender_army.backline[i].morale/540) + 0.03 )/50
                           str_casualties_art = ((15 + 5* pips_art) * multiplier_art)/50
                           
                           if morale_casualties_art > attacker_army.frontline[i].morale:
                               attack_m_sum -= attacker_army.frontline[i].morale
                               attacker_army.frontline[i].morale -= morale_casualties_art
                               
                           else:
                               attacker_army.frontline[i].morale -= morale_casualties_art
                               attack_m_sum -= morale_casualties_art
                           if str_casualties_art > attacker_army.frontline[i].strength:
                               attack_size -= attacker_army.frontline[i].strength
                               attacker_army.frontline[i].strength -= str_casualties_art
                               
                           else: 
                               attacker_army.frontline[i].strength -= str_casualties_art
                               attack_size -= str_casualties_art
                           losses_att += str_casualties_art
                           #how much dmg attacker art does to defender frontline
                   if isinstance(attacker_army.backline[i],infantry.Artillery):
                               #if index of the art matches up to an index of enemy front line
                       if (0 <= i) and (i <len(defender_army.frontline)):
                           pips_art_at = att_dice_roll + max(0,attack_ldr_shock-ldr_shock) + attacker_army.backline[i].off_shock - defender_army.frontline[i].def_shock
                           multiplier_art_at = (attacker_army.backline[i].strength/1000) * (attacker_army.backline[i].off_shock / defender_army.frontline[i].tactics) * (1 + attacker_army.backline[i].combat_ability) * (1+attack_discipline) * (1+(total_days+1/100))
                           morale_casualties_art_at = ((15+5*pips_art_at) * multiplier_art_at * (attacker_army.backline[i].morale/540) + 0.03 )/50
                           str_casualties_art_at = ((15 + 5* pips_art_at) * multiplier_art_at)/50
                               
                           if morale_casualties_art_at > defender_army.frontline[i].morale:
                               moralesum -= defender_army.frontline[i].morale
                               defender_army.frontline[i].morale -= morale_casualties_art_at
                               
                           else:
                               defender_army.frontline[i].morale -= morale_casualties_art_at
                               moralesum -= morale_casualties_art_at
                           if str_casualties_art_at > defender_army.frontline[i].strength:
                               army_size -= defender_army.frontline[i].strength
                               defender_army.frontline[i].strength -= str_casualties_art_at
                               
                           else: 
                               defender_army.frontline[i].strength -= str_casualties_art_at
                               army_size -= str_casualties_art_at
                           losses_def += str_casualties_art_at       
                   else: continue          
               for i in range(len(attacker_army.backline),len(defender_army.backline)):
                   if isinstance(defender_army.backline[i],infantry.Artillery):
                        if (0 <= i) and (i <len(attacker_army.frontline)):
                           pips_art = dice_roll + max(0,ldr_shock-attack_ldr_shock) + defender_army.backline[i].off_shock - attacker_army.frontline[i].def_shock
                           multiplier_art = (defender_army.backline[i].strength/1000) * (defender_army.backline[i].off_shock / attacker_army.frontline[i].tactics) * (1 + defender_army.backline[i].combat_ability) * (1+discipline) * (1+(total_days+1/100))
                           morale_casualties_art = ((15+5*pips_art) * multiplier_art * (defender_army.backline[i].morale/540) + 0.03 )/50
                           str_casualties_art = ((15 + 5* pips_art) * multiplier_art)/50
                           
                           if morale_casualties_art > attacker_army.frontline[i].morale:
                               attack_m_sum -= attacker_army.frontline[i].morale
                               attacker_army.frontline[i].morale -= morale_casualties_art
                               
                           else:
                               attacker_army.frontline[i].morale -= morale_casualties_art
                               attack_m_sum -= morale_casualties_art
                           if str_casualties_art > attacker_army.frontline[i].strength:
                               attack_size -= attacker_army.frontline[i].strength
                               attacker_army.frontline[i].strength -= str_casualties_art
                               
                           else: 
                               attacker_army.frontline[i].strength -= str_casualties_art
                               attack_size -= str_casualties_art
                           losses_att += str_casualties_art
                                     
                   else: continue          
           else:
                   
               for i in range(len(attacker_army.backline)):
                       #how much damage defender art does to attacker frontline
                   if isinstance(defender_army.backline[i],infantry.Artillery):
                           #if index of the art matches up to an index of enemy front line
                       if (0 <= i) and (i <len(attacker_army.frontline)):
                           pips_art = dice_roll + max(0,ldr_shock-attack_ldr_shock) + defender_army.backline[i].off_shock - attacker_army.frontline[i].def_shock
                           multiplier_art = (defender_army.backline[i].strength/1000) * (defender_army.backline[i].off_shock / attacker_army.frontline[i].tactics) * (1 + defender_army.backline[i].combat_ability) * (1+discipline) * (1+(total_days+1/100))
                           morale_casualties_art = ((15+5*pips_art) * multiplier_art * (defender_army.backline[i].morale/540) + 0.03 )/50
                           str_casualties_art = ((15 + 5* pips_art) * multiplier_art)/50
                           
                           if morale_casualties_art > attacker_army.frontline[i].morale:
                               attack_m_sum -= attacker_army.frontline[i].morale
                               attacker_army.frontline[i].morale -= morale_casualties_art
                               
                           else:
                               attacker_army.frontline[i].morale -= morale_casualties_art
                               attack_m_sum -= morale_casualties_art
                           if str_casualties_art > attacker_army.frontline[i].strength:
                               attack_size -= attacker_army.frontline[i].strength
                               attacker_army.frontline[i].strength -= str_casualties_art
                               
                           else: 
                               attacker_army.frontline[i].strength -= str_casualties_art
                               attack_size -= str_casualties_art
                           losses_att += str_casualties_art
                                   
                           #how much dmg attacker art does to defender frontline
                   if isinstance(attacker_army.backline[i],infantry.Artillery):
                               #if index of the art matches up to an index of enemy front line
                       if (0 <= i) and (i <len(defender_army.frontline)):
                           pips_art_at = att_dice_roll + max(0,attack_ldr_shock-ldr_shock) + attacker_army.backline[i].off_shock - defender_army.frontline[i].def_shock
                           multiplier_art_at = (attacker_army.backline[i].strength/1000) * (attacker_army.backline[i].off_shock / defender_army.frontline[i].tactics) * (1 + attacker_army.backline[i].combat_ability) * (1+attack_discipline) * (1+(total_days+1/100))
                           morale_casualties_art_at = ((15+5*pips_art_at) * multiplier_art_at * (attacker_army.backline[i].morale/540) + 0.03 )/50
                           str_casualties_art_at = ((15 + 5* pips_art_at) * multiplier_art_at)/50
                               
                           if morale_casualties_art_at > defender_army.frontline[i].morale:
                               moralesum -= defender_army.frontline[i].morale
                               defender_army.frontline[i].morale -= morale_casualties_art_at
                               
                           else:
                               defender_army.frontline[i].morale -= morale_casualties_art_at
                               moralesum -= morale_casualties_art_at
                           if str_casualties_art_at > defender_army.frontline[i].strength:
                               army_size -= defender_army.frontline[i].strength
                               defender_army.frontline[i].strength -= str_casualties_art_at
                               
                           else: 
                               defender_army.frontline[i].strength -= str_casualties_art_at
                               army_size -= str_casualties_art_at
                           losses_def += str_casualties_art_at                               
                   else:continue        
           
           for i in range(len(attacker_army.backline)):
               #backline damage to morale
               if ( ((attack_moral/540) + 0.03)*5) > attacker_army.backline[i].morale:
                   attack_m_sum -= abs(attacker_army.backline[i].morale)
                   attacker_army.backline[i].morale -= ((attack_moral/540) + 0.03)*2
               else:         
                   attacker_army.backline[i].morale -= ((attack_moral/540) + 0.03)*2
                   attack_m_sum -=  ((attack_moral/540) + 0.03)*2   
           for i in range(len(defender_army.backline)):
               
               #backline damage to morale
               if (((moral/540) + 0.03)*5) > defender_army.backline[i].morale:
                   moralesum -= abs(defender_army.backline[i].morale)
                   defender_army.backline[i].morale -= (((moral/540) + 0.03)*2)
               else:             
                   defender_army.backline[i].morale -= ((moral/540) + 0.03)*2
                   moralesum -=  ((moral/540) + 0.03)*2
           for i in range(len(defender_army.reserves)):
               #reserves dmg to morale
               if (((moral/540) + 0.03)*5) > defender_army.reserves[i].morale:
                   moralesum -= abs(defender_army.reserves[i].morale)
                   defender_army.reserves[i].morale -= ((moral/540) + 0.03)*2
               else:
                   defender_army.reserves[i].morale -= ((moral/540) + 0.03)*2
                   moralesum -=  ((moral/540) + 0.03)*2
           for i in range(len(attacker_army.reserves)):
               #reserves damage to morale
               if (((attack_moral/540) + 0.03)*5) > attacker_army.reserves[i].morale:
                   attack_m_sum -=  abs(attacker_army.reserves[i].morale)
                   attacker_army.reserves[i].morale -= ((attack_moral/540) + 0.03)*2
               else:           
                   attacker_army.reserves[i].morale -= ((attack_moral/540) + 0.03)*2
                   attack_m_sum -=  ((attack_moral/540) + 0.03)*2   
          
                                     
                   #then copy it all into shock phase 
                   
            #checking for units in need of replacement
           ii = 0              
           while ii < len(attacker_army.frontline):
               if attacker_army.frontline[ii].morale <= 0 or attacker_army.frontline[ii].strength <= 0:
                   if attacker_army.frontline[ii].morale > 0:
                       attack_m_sum -= attacker_army.frontline[ii].morale
                   if attacker_army.frontline[ii].strength > 0:
                       attack_size -= attacker_army.frontline[ii].strength     
                   
                   if len(attacker_army.reserves) > 0:
                       #attacker_army.frontline[ii] = attacker_army.reserves[0]
                       attacker_army.frontline.append(attacker_army.reserves[0])
                       attacker_army.reserves.remove(attacker_army.reserves[0])
                       attacker_army.frontline.remove(attacker_army.frontline[ii])
                       #ii-=1
                       
                   else:    
                       attacker_army.frontline.remove(attacker_army.frontline[ii])
                       #ii -= 1
               else:ii += 1
               if ii < 0 : ii=0
           ii = 0        
           while ii < len(attacker_army.backline):
               if attacker_army.backline[ii].morale <= 0 or attacker_army.backline[ii].strength <= 0:
                   if attacker_army.backline[ii].morale > 0:
                       attack_m_sum -= attacker_army.backline[ii].morale
                   if attacker_army.backline[ii].strength > 0:
                       attack_size -= attacker_army.backline[ii].strength
                   if len(attacker_army.reserves) > 0:
                       #attacker_army.backline[ii] = attacker_army.reserves[0]
                       attacker_army.backline.append(attacker_army.reserves[-1])
                       attacker_army.reserves.remove(attacker_army.reserves[-1])
                       attacker_army.backline.remove(attacker_army.backline[ii])
                       #ii-=1
                   else:    
                       attacker_army.backline.remove(attacker_army.backline[ii])
                       #ii -= 1
               else:ii += 1
               if ii < 0: ii = 0
           ii = 0        
           while ii < len(defender_army.frontline):
               if defender_army.frontline[ii].morale <= 0 or defender_army.frontline[ii].strength <= 0:
                   if defender_army.frontline[ii].morale > 0:
                       moralesum -= defender_army.frontline[ii].morale
                   if defender_army.frontline[ii].strength > 0:
                       army_size -= defender_army.frontline[ii].strength
                   if len(defender_army.reserves) > 0:
                       #defender_army.frontline[ii] = defender_army.reserves[0]
                       #defender_army.reserves.remove(defender_army.reserves[0])
                       defender_army.frontline.append(defender_army.reserves[0])
                       defender_army.reserves.remove(defender_army.reserves[0])
                       defender_army.frontline.remove(defender_army.frontline[ii])
                       #ii-=1
                   else:    
                       defender_army.frontline.remove(defender_army.frontline[ii])
                       #ii -= 1
               else:ii += 1
               if ii < 0: ii = 0 
           ii = 0       
           while ii < len(defender_army.backline):
               if defender_army.backline[ii].morale <= 0 or defender_army.backline[ii].strength <= 0:
                   if defender_army.backline[ii].morale > 0:
                       moralesum -= defender_army.backline[ii].morale
                   if defender_army.backline[ii].strength > 0:
                       army_size -= defender_army.backline[ii].strength
                   if len(defender_army.reserves) > 0:
                       #defender_army.backline[ii] = defender_army.reserves[0]
                       #defender_army.reserves.remove(defender_army.reserves[0])
                       defender_army.backline.append(defender_army.reserves[-1])
                       defender_army.reserves.remove(defender_army.reserves[-1])
                       defender_army.backline.remove(defender_army.backline[ii])
                       #ii-=1
                   else:    
                       defender_army.backline.remove(defender_army.backline[ii])
                       #ii -= 1
               else:ii += 1
               if ii < 0: ii = 0                      
       
       
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
           
       
   
       
   print(moralesum)
   print(army_size)
   print(attack_size)
   print(attack_m_sum)
   
   print("defender losses",losses_def)
   print("attacker losses",losses_att)
   victory = ""
   if moralesum > attack_m_sum:
       victory = "Defenders won!!"
   elif attack_m_sum > moralesum:
       victory = "Attackers won!!"  
       
   print(total_days)    
   return [victory,losses_att,losses_def]         
       
   
#THINGS TO FIX ONCE EVERYTHING IS FINISHED:
#for morale casualties it sohuld be max morale/540 not .morale/540
#need to use morale def and off pips for morale casualties
#dice roll at start of each phase not day

