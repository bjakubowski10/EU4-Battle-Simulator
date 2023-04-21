from battleline import Army




test = Army(120,0,0,0,4,80,15)

test.fill_front_back_line()

count = 1
for unit in test.frontline:
    
    print(count,unit.off_shock)
    count +=1
print('\n\n\n\n\n')   
check = 1 
for unit in test.backline:
    print(check,unit.off_shock)
    check +=1
        
        
#need morale for both, need troops combat ability, need tech, need amounts of troops, need discpline
#



fire_phase = True
shock_phase = False
        