  

leader_fire = 2
leader_shock = 2


enldr_fire = 2
enldr_shock = 2
morale = 6
enmorale = 6




count = 0
count2 = 0

    #test
        
infstr_sum=0
infmorale_sum=0        
for i in inf_front:
    infstr_sum += int(i.strength)
    infmorale_sum += morale
for i in inf_back:
    infstr_sum+= int(i.strength)
    infmorale_sum += morale
    
eninfstr_sum = 0
eninfmorale_sum=0    
for i in eninf_front:
    eninfstr_sum += int(i.strength)
    eninfmorale_sum += enmorale
for i in eninf_back:
    eninfstr_sum+= int(i.strength)
    eninfmorale_sum+= enmorale   

print(infstr_sum)
print(infmorale_sum)
print(eninfstr_sum)
print(eninfmorale_sum)


fire_phase = True
shock_phase = False
count_phase = 0    
#test = 0
#test1 = 0     
round = 0    
while infmorale_sum > 0 and eninfmorale_sum > 0 and infstr_sum > 0 and eninfstr_sum > 0:
    for i in range(3):
        round +=1
        count_phase +=1
        if fire_phase == True:
            for unit in range(len(inf_front)-1):
                #if test == 10:
                 #   break
                
                if len(eninf_front)-1 < unit:
                    #test+=1
                  #  print(test)
                    continue
                else: 
                    
            for enemy_unit in range(len(eninf_front)-1):
                #if test1 == 10:
                 #   break
                if len(inf_front)-1 < enemy_unit:
                    #test1+=1
                    continue
                else:
                
        if shock_phase == True:    
            pass
    if count_phase == 3 and fire_phase == True:
        fire_phase = False
        shock_phase = True
    elif count_phase == 3 and shock_phase == True:
        fire_phase = True
        shock_phase = False            
    count_phase=0
    
    

print(infstr_sum)
print(infmorale_sum)
print(eninfstr_sum)
print(eninfmorale_sum)
       
       
                
#need 2 loops
#first one to go through the battle and end if no troops or morale on one side is gone
#the the one inside to go through the 3 rounds in each phase
#for now only attack the ones on top of eachother






        

              