from tkinter import *
from tkinter import ttk
from PIL import ImageTk,Image
import main
 

root = Tk()
root.title("Europa Universalis IV Battle Simulator")
root.geometry("850x850")
root.resizable(0,0)
root.iconbitmap("C:/Users/bjaku/OneDrive/Desktop/EU4 sim/favicon.ico")

#updates group for defenders to show the western or eastern choice related to the tech level
def update_group(*args):
    group_teched = tech_group[tech_var.get()]
    group_var.set(group_teched[0])
    menu = optionmenu_b["menu"]
    menu.delete(0,'end')
    for group in group_teched:
        menu.add_command(label=group, command=lambda grouped_tech=group: group_var.set(grouped_tech))
        
    #updates group for attackers to show the western or eastern choice related to the tech level
def update_group2(*args):
    group_teched = tech_group[tech_var2.get()]
    group_var2.set(group_teched[0])
    menu = optionmenu_b2["menu"]
    menu.delete(0,'end')
    for group in group_teched:
        menu.add_command(label=group, command=lambda grouped_tech=group: group_var2.set(grouped_tech))      
#function that allows choice of defending units for inf regarding selected tech group
def update_inf(*args):
    free_units = inf_unit_group[group_var.get()]
    unit_var.set(free_units[0])
    menu = optionmenu_c["menu"]
    menu.delete(0,"end")
    for tech_unit in free_units:
        menu.add_command(label=tech_unit,command = lambda grouped_units = tech_unit : unit_var.set(grouped_units) )
#functions that allows choice of attacking units for inf regarding selected tech group
def update_inf2(*args):
    free_units = inf_unit_group[group_var2.get()]
    unit_var2.set(free_units[0])
    menu = optionmenu_c2["menu"]
    menu.delete(0,"end")
    for tech_unit in free_units:
        menu.add_command(label=tech_unit,command = lambda grouped_units = tech_unit : unit_var2.set(grouped_units) )
#function that allows choice of defending units cavalry regarding selected tech group
def update_cav(*args):
    free_units = cav_unit_group[group_var.get()]
    cav_unit_var.set(free_units[0])
    menu = optionmenu_cav["menu"]
    menu.delete(0,"end")
    for tech_unit in free_units:
        menu.add_command(label=tech_unit,command = lambda grouped_units = tech_unit : cav_unit_var.set(grouped_units) ) 
#function that allows choice of def units cavalry regarding selected tech group
def update_cav2(*args):
    free_units = cav_unit_group[group_var2.get()]
    cav_unit_var2.set(free_units[0])
    menu = optionmenu_cav2["menu"]
    menu.delete(0,"end")
    for tech_unit in free_units:
        menu.add_command(label=tech_unit,command = lambda grouped_units = tech_unit : cav_unit_var2.set(grouped_units) )
#function to update att art types        
def update_art(*args):
    free_units = art_unit_group[group_var.get()]
    art_unit_var.set(free_units[0])
    menu = optionmenu_art["menu"]
    menu.delete(0,"end")
    for tech_unit in free_units:
        menu.add_command(label=tech_unit,command = lambda grouped_units = tech_unit : art_unit_var.set(grouped_units) )    
        #att art 
def update_art2(*args):
    free_units = art_unit_group[group_var2.get()]
    art_unit_var2.set(free_units[0])
    menu = optionmenu_art2["menu"]
    menu.delete(0,"end")
    for tech_unit in free_units:
        menu.add_command(label=tech_unit,command = lambda grouped_units = tech_unit : art_unit_var2.set(grouped_units) )         
                                   
                       
                             

        
        
        
root.columnconfigure(0,minsize=10)
root.columnconfigure(1,minsize=87.5)
root.columnconfigure(2,minsize=10)
root.columnconfigure(3,minsize=87.5)
root.columnconfigure(4,minsize=87.5)
root.columnconfigure(5,minsize=87.5)
root.columnconfigure(6,minsize=10)
root.columnconfigure(7,minsize=87.5)
root.columnconfigure(8,minsize=87.5)
root.columnconfigure(9,minsize=87.5)
root.columnconfigure(10,minsize=87.5)
root.rowconfigure(0,minsize = 30)
root.rowconfigure(1,minsize = 30)
root.rowconfigure(2,minsize = 30)
root.rowconfigure(3,minsize = 30)
root.rowconfigure(4,minsize = 30)
root.rowconfigure(5,minsize = 30)
root.rowconfigure(6,minsize = 30)
root.rowconfigure(7,minsize = 30)
root.rowconfigure(8,minsize = 30)

separator = ttk.Separator(root, orient='vertical')
separator.place(relx=0.43, rely=.1, relwidth=0.2, relheight=.55)
 
tech_group = { "1": ["Western(1)","Eastern(1)","Anatolian(1)","Muslim(1)"], "2": ["Western(2)","Eastern(2)","Anatolian(2)","Muslim(2)"],
               "3": ["Western(3)","Eastern(3)","Anatolian(3)","Muslim(3)"], "4": ["Western(4)","Eastern(4)","Anatolian(4)","Muslim(4)"], "5": ["Western(5)","Eastern(5)","Anatolian(5)","Muslim(5)"],
               "6": ["Western(6)","Eastern(6)","Anatolian(6)","Muslim(6)"], "7": ["Western(7)","Eastern(7)","Anatolian(7)","Muslim(7)"], "8": ["Western(8)","Eastern(8)","Anatolian(8)","Muslim(8)"],
               "9": ["Western(9)","Eastern(9)","Anatolian(9)","Muslim(9)"], "10": ["Western(10)","Eastern(10)","Anatolian(10)","Muslim(10)"], "11": ["Western(11)","Eastern(11)","Anatolian(11)","Muslim(11)"],
               "12": ["Western(12)","Eastern(12)","Anatolian(12)","Muslim(12)"], "13": ["Western(13)","Eastern(13)","Anatolian(13)","Muslim(13)"], "14": ["Western(14)","Eastern(14)","Anatolian(14)","Muslim(14)"],
               "15": ["Western(15)","Eastern(15)","Anatolian(15)","Muslim(15)"], "16": ["Western(16)","Eastern(16)","Anatolian(16)","Muslim(16)"], "17": ["Western(17)","Eastern(17)","Anatolian(17)","Muslim(17)"],
               "18": ["Western(18)","Eastern(18)","Anatolian(18)","Muslim(18)"], "19": ["Western(19)","Eastern(19)","Anatolian(19)","Muslim(19)"], "20": ["Western(20)","Eastern(20)","Anatolian(20)","Muslim(20)"],
               "21": ["Western(21)","Eastern(21)","Anatolian(21)","Muslim(21)"], "22": ["Western(22)","Eastern(22)","Anatolian(22)","Muslim(22)"], "23": ["Western(23)","Eastern(23)","Anatolian(23)","Muslim(23)"],
               "24": ["Western(24)","Eastern(24)","Anatolian(24)","Muslim(24)"], "25": ["Western(25)","Eastern(25)","Anatolian(25)","Muslim(25)"], "26": ["Western(26)","Eastern(26)","Anatolian(26)","Muslim(26)"],
               "27": ["Western(27)","Eastern(27)","Anatolian(27)","Muslim(27)"], "28": ["Western(28)","Eastern(28)","Anatolian(28)","Muslim(28)"], "29": ["Western(29)","Eastern(29)","Anatolian(29)","Muslim(29)"],
                "30": ["Western(30)","Eastern(30)","Anatolian(30)","Muslim(30)"], "31": ["Western(31)","Eastern(31)","Anatolian(31)","Muslim(31)"], "32": ["Western(32)","Eastern(32)","Anatolian(32)","Muslim(32)"]
                }

inf_unit_group = {"Western(1)" : ["Halberd Infantry", "Latin Medieval Infantry"], "Western(2)" : ["Halberd Infantry", "Latin Medieval Infantry"], "Western(3)" : ["Halberd Infantry", "Latin Medieval Infantry"], "Western(4)" : ["Halberd Infantry", "Latin Medieval Infantry"], 
              "Western(5)" : ["Galloglaigh Infantry", "Longbow","Men at Arms"], "Western(6)" : ["Galloglaigh Infantry", "Longbow","Men at Arms"], "Western(7)" : ["Galloglaigh Infantry", "Longbow","Men at Arms"], "Western(8)" : ["Galloglaigh Infantry", "Longbow","Men at Arms"],
              "Western(9)" : ["Landsknechten Infantry", "Condotta Infantry","Reformed Galloglaigh Infantry"], "Western(10)" : ["Landsknechten Infantry", "Condotta Infantry","Reformed Galloglaigh Infantry"],   "Western(11)" : ["Landsknechten Infantry", "Condotta Infantry","Reformed Galloglaigh Infantry"],
              "Western(12)" : ["Free Shooter Infantry", "Tercio Infantry"], "Western(13)" : ["Free Shooter Infantry", "Tercio Infantry"],  "Western(14)" : ["Free Shooter Infantry", "Tercio Infantry"],        
              "Western(15)" : ["Charge Infantry", "Maurician Infantry"],  "Western(16)" : ["Charge Infantry", "Maurician Infantry"],   "Western(17)" : ["Charge Infantry", "Maurician Infantry"],   "Western(18)" : ["Charge Infantry", "Maurician Infantry"],   
              "Western(19)" : ["Gustavian Infantry", "Highlanders Infantry","Reformed Tercio"],  "Western(20)" : ["Gustavian Infantry", "Highlanders Infantry","Reformed Tercio"],    "Western(21)" : ["Gustavian Infantry", "Highlanders Infantry","Reformed Tercio"],    "Western(22)" : ["Gustavian Infantry", "Highlanders Infantry","Reformed Tercio"],       
              "Western(23)" : ["Grenzer Infantry", "Line Infantry","Caroline Infantry"], "Western(24)" : ["Grenzer Infantry", "Line Infantry","Caroline Infantry"],"Western(25)" : ["Grenzer Infantry", "Line Infantry","Caroline Infantry"],     
              "Western(26)" : ["Frederickian Infantry", "Red Coat Infantry","White Coat Infantry","Blue Coat Infantry"],  "Western(27)" : ["Frederickian Infantry", "Red Coat Infantry","White Coat Infantry","Blue Coat Infantry"],  
              "Western(28)" : ["Square Infantry", "Impulse Infantry"], "Western(29)" : ["Square Infantry", "Impulse Infantry"], 
              "Western(30)" : ["Drill Infantry", "Jaeger Infantry","Mixer Order Infantry","Napoleonic Square"], "Western(31)" : ["Drill Infantry", "Jaeger Infantry","Mixer Order Infantry","Napoleonic Square"],"Western(32)" : ["Drill Infantry", "Jaeger Infantry","Mixer Order Infantry","Napoleonic Square"],
              "Eastern(1)" : ["Bardiche Infantry", "Eastern Medieval Infantry"], "Eastern(2)" : ["Bardiche Infantry", "Eastern Medieval Infantry"], "Eastern(3)" : ["Bardiche Infantry", "Eastern Medieval Infantry"], "Eastern(4)" : ["Bardiche Infantry", "Eastern Medieval Infantry"], 
              "Eastern(5)" : ["Eastern Militia"], "Eastern(6)" : ["Eastern Militia"], "Eastern(7)" : ["Eastern Militia"], "Eastern(8)" : ["Eastern Militia"], 
              "Eastern(9)" : ["Pike Infantry"],  "Eastern(10)" : ["Pike Infantry"],  "Eastern(11)" : ["Pike Infantry"], 
              "Eastern(12)" : ["Defensive Eastern Musketeers", "Offensive Eastern Musketeers"],  "Eastern(13)" : ["Defensive Eastern Musketeers", "Offensive Eastern Musketeers"], "Eastern(14)" : ["Defensive Eastern Musketeers", "Offensive Eastern Musketeers"], 
              "Eastern(15)" : ["Eastern Tercio", "Soldaty Infantry"],  "Eastern(16)" : ["Eastern Tercio", "Soldaty Infantry"],  "Eastern(17)" : ["Eastern Tercio", "Soldaty Infantry"],  "Eastern(18)" : ["Eastern Tercio", "Soldaty Infantry"], 
              "Eastern(19)" : ["Saxon Infantry"], "Eastern(20)" : ["Saxon Infantry"], "Eastern(21)" : ["Saxon Infantry"], "Eastern(22)" : ["Saxon Infantry"], 
              "Eastern(23)" : ["Petrine Infantry"], "Eastern(24)" : ["Petrine Infantry"], "Eastern(25)" : ["Petrine Infantry"], 
              "Eastern(26)" : ["Green Coat Infantry"], "Eastern(27)" : ["Green Coat Infantry"], "Eastern(28)" : ["Green Coat Infantry"], "Eastern(29)" : ["Green Coat Infantry"],
              "Eastern(30)" : ["Mass Infantry"], "Eastern(31)" : ["Mass Infantry"], "Eastern(32)" : ["Mass Infantry"]
              }

cav_unit_group = { "Western(1)" : ["Chevauchee","Western Medieval Knights"],"Western(2)" : ["Chevauchee","Western Medieval Knights"],"Western(3)" : ["Chevauchee","Western Medieval Knights"],"Western(4)" : ["Chevauchee","Western Medieval Knights"],"Western(5)" : ["Chevauchee","Western Medieval Knights"],
                  "Western(6)" : ["Chevauchee","Western Medieval Knights"],"Western(7)" : ["Chevauchee","Western Medieval Knights"],"Western(8)" : ["Chevauchee","Western Medieval Knights"],"Western(9)" : ["Chevauchee","Western Medieval Knights"],
                  "Western(10)" : ["Schwarze Reiter"],  "Western(11)" : ["Schwarze Reiter"], "Western(12)" : ["Schwarze Reiter"], "Western(13)" : ["Schwarze Reiter"],
                  "Western(14)" : ["Latin Caracole Cavalry"], "Western(15)" : ["Latin Caracole Cavalry"],"Western(16)" : ["Latin Caracole Cavalry"],"Western(17)" : ["Latin Caracole Cavalry"],   
                  "Western(18)" : ["Gallop Cavalry"],"Western(19)" : ["Gallop Cavalry"],"Western(20)" : ["Gallop Cavalry"],"Western(21)" : ["Gallop Cavalry"],"Western(22)" : ["Gallop Cavalry"],
                  "Western(23)" : ["Armee Blanche Cavalry","Latin Dragoons","Latin Hussars"], "Western(24)" : ["Armee Blanche Cavalry","Latin Dragoons","Latin Hussars"], "Western(25)" : ["Armee Blanche Cavalry","Latin Dragoons","Latin Hussars"], 
                  "Western(26)" : ["Carabiners","Reformed Latin Hussars","Uhlan Cavalry"], "Western(27)" : ["Carabiners","Reformed Latin Hussars","Uhlan Cavalry"],
                  "Western(28)" : ["Latin Chasseur","Latin Cuirassiers","Latin Lancers"], "Western(29)" : ["Latin Chasseur","Latin Cuirassiers","Latin Lancers"], "Western(30)" : ["Latin Chasseur","Latin Cuirassiers","Latin Lancers"],
                   "Western(31)" : ["Latin Chasseur","Latin Cuirassiers","Latin Lancers"], "Western(32)" : ["Latin Chasseur","Latin Cuirassiers","Latin Lancers"],
                   "Eastern(1)" : ["Druzhina Cavalry","Eastern Knights"],"Eastern(2)" : ["Druzhina Cavalry","Eastern Knights"],"Eastern(3)" : ["Druzhina Cavalry","Eastern Knights"],"Eastern(4)" : ["Druzhina Cavalry","Eastern Knights"],"Eastern(5)" : ["Druzhina Cavalry","Eastern Knights"],
                   "Eastern(6)" : ["Stratioti Cavalry"], "Eastern(7)" : ["Stratioti Cavalry"], "Eastern(8)" : ["Stratioti Cavalry"], "Eastern(9)" : ["Stratioti Cavalry"],
                    "Eastern(10)" : ["Eastern Hussar"],"Eastern(11)" : ["Eastern Hussar"],"Eastern(12)" : ["Eastern Hussar"],"Eastern(13)" : ["Eastern Hussar"],
                    "Eastern(14)" : ["Eastern Caracole","Reformed Eastern Hussars","Southern Cossacks"],"Eastern(15)" : ["Eastern Caracole","Reformed Eastern Hussars","Southern Cossacks"],"Eastern(16)" : ["Eastern Caracole","Reformed Eastern Hussars","Southern Cossacks"],"Eastern(17)" : ["Eastern Caracole","Reformed Eastern Hussars","Southern Cossacks"],
                    "Eastern(18)" : ["Eastern Caracole","Reformed Eastern Hussars","Southern Cossacks"],"Eastern(19)" : ["Eastern Caracole","Reformed Eastern Hussars","Southern Cossacks"],"Eastern(20)" : ["Eastern Caracole","Reformed Eastern Hussars","Southern Cossacks"],
                    "Eastern(21)" : ["Eastern Caracole","Reformed Eastern Hussars","Southern Cossacks"],
                     "Eastern(22)" : ["Cossack Cavalry","Winged Hussars"],"Eastern(23)" : ["Cossack Cavalry","Winged Hussars"],"Eastern(24)" : ["Cossack Cavalry","Winged Hussars"],"Eastern(25)" : ["Cossack Cavalry","Winged Hussars"],
                     "Eastern(26)" : ["Lancers","Reformed Cossack Cavalry"], "Eastern(27)" : ["Lancers","Reformed Cossack Cavalry"],
                      "Eastern(28)" : ["Eastern Cuirassiers","Advanced Cossack Cavalry"],"Eastern(29)" : ["Eastern Cuirassiers","Advanced Cossack Cavalry"],"Eastern(30)" : ["Eastern Cuirassiers","Advanced Cossack Cavalry"],
                      "Eastern(31)" : ["Eastern Cuirassiers","Advanced Cossack Cavalry"],"Eastern(32)" : ["Eastern Cuirassiers","Advanced Cossack Cavalry"]

}

art_unit_group = {"Western(1)" : ["NaN"], "Western(2)" : ["NaN"], "Western(3)" : ["NaN"], "Western(4)" : ["NaN"], "Western(5)" : ["NaN"], "Western(6)" : ["NaN"],
                  "Eastern(1)" : ["NaN"], "Eastern(2)" : ["NaN"], "Eastern(3)" : ["NaN"], "Eastern(4)" : ["NaN"], "Eastern(5)" : ["NaN"], "Eastern(6)" : ["NaN"],  
                  "Western(7)": [ "Houfnice","Large Cast Bronze Mortar"],"Western(8)": [ "Houfnice","Large Cast Bronze Mortar"],"Western(9)": [ "Houfnice","Large Cast Bronze Mortar"],
                  "Eastern(7)": [ "Houfnice","Large Cast Bronze Mortar"],"Eastern(8)": [ "Houfnice","Large Cast Bronze Mortar"],"Eastern(9)": [ "Houfnice","Large Cast Bronze Mortar"],
                  "Western(10)": [ "Culverin","Pedrero"],  "Western(11)": [ "Culverin","Pedrero"], "Western(12)": [ "Culverin","Pedrero"],
                  "Eastern(10)": [ "Culverin","Pedrero"],  "Eastern(11)": [ "Culverin","Pedrero"], "Eastern(12)": [ "Culverin","Pedrero"],
                  "Western(13)" : ["Large Cast Iron Cannon","Small Cast Iron Cannon"],"Western(14)" : ["Large Cast Iron Cannon","Small Cast Iron Cannon"],"Western(15)" : ["Large Cast Iron Cannon","Small Cast Iron Cannon"],
                  "Eastern(13)" : ["Large Cast Iron Cannon","Small Cast Iron Cannon"],"Eastern(14)" : ["Large Cast Iron Cannon","Small Cast Iron Cannon"],"Eastern(15)" : ["Large Cast Iron Cannon","Small Cast Iron Cannon"],
                  "Western(16)" : ["Chambered Demi Cannon","Demi-Culverin"], "Western(17)" : ["Chambered Demi Cannon","Demi-Culverin"], 
                  "Eastern(16)" : ["Chambered Demi Cannon","Demi-Culverin"], "Eastern(17)" : ["Chambered Demi Cannon","Demi-Culverin"],
                  "Western(18)" : ["Leather Cannon","Chambered Cannon"],  "Western(19)" : ["Leather Cannon","Chambered Cannon"],
                  "Eastern(18)" : ["Leather Cannon","Chambered Cannon"],  "Eastern(19)" : ["Leather Cannon","Chambered Cannon"], 
                  "Western(20)" : ["Swivel Cannon","Howitzer"],  "Western(21)" : ["Swivel Cannon","Howitzer"], 
                  "Eastern(20)" : ["Swivel Cannon","Howitzer"],  "Eastern(21)" : ["Swivel Cannon","Howitzer"], 
                  "Western(22)" : ["Coehorn Mortar","Horse Artillery"],  "Western(23)" : ["Coehorn Mortar","Horse Artillery"],  "Western(24)" : ["Coehorn Mortar","Horse Artillery"], 
                   "Eastern(22)" : ["Coehorn Mortar","Horse Artillery"],  "Eastern(23)" : ["Coehorn Mortar","Horse Artillery"],  "Eastern(24)" : ["Coehorn Mortar","Horse Artillery"], 
                   "Western(25)" : ["Royal Mortar","Licorne"], "Western(26)" : ["Royal Mortar","Licorne"], "Western(27)" : ["Royal Mortar","Licorne"], "Western(28)" : ["Royal Mortar","Licorne"], 
                    "Eastern(25)" : ["Royal Mortar","Licorne"], "Eastern(26)" : ["Royal Mortar","Licorne"], "Eastern(27)" : ["Royal Mortar","Licorne"], "Eastern(28)" : ["Royal Mortar","Licorne"], 
                    "Western(29)" : ["Flying Battery","Grand Battery"],"Western(30)" : ["Flying Battery","Grand Battery"],"Western(31)" : ["Flying Battery","Grand Battery"],"Western(32)" : ["Flying Battery","Grand Battery"],
                    "Eastern(29)" : ["Flying Battery","Grand Battery"],"Eastern(30)" : ["Flying Battery","Grand Battery"],"Eastern(31)" : ["Flying Battery","Grand Battery"],"Eastern(32)" : ["Flying Battery","Grand Battery"],                  
                  
    
    
}


tech_var = StringVar()
tech_var2 = StringVar()

tech_var.trace('w',update_group)
tech_var2.trace('w',update_group2)
#tech option menu
optionmenu_a = OptionMenu(root,tech_var,*tech_group.keys())
optionmenu_a2 = OptionMenu(root,tech_var2,*tech_group.keys())

group_var = StringVar()
group_var2 = StringVar()
group_var.trace('w',update_inf)
group_var2.trace('w',update_inf2)
#group option menu
optionmenu_b = OptionMenu(root,group_var,'')
optionmenu_b2 = OptionMenu(root,group_var2,'')

unit_var = StringVar()
unit_var2 = StringVar()
#infantry option menu
optionmenu_c = OptionMenu(root,unit_var,'')
optionmenu_c2 = OptionMenu(root,unit_var2,'')

#cav option menu
group_var.trace('w',update_cav)
cav_unit_var = StringVar()
optionmenu_cav = OptionMenu(root,cav_unit_var,"")

group_var2.trace('w',update_cav2)
cav_unit_var2 = StringVar()
optionmenu_cav2 = OptionMenu(root,cav_unit_var2,"")


#art option menu
group_var.trace('w',update_art)
art_unit_var = StringVar()
optionmenu_art = OptionMenu(root,art_unit_var,"")

group_var2.trace('w',update_art2)
art_unit_var2 = StringVar()
optionmenu_art2 = OptionMenu(root,art_unit_var2,"")

tech_var.set("1")
tech_var2.set("1")



#terrain, attack and ddef
terrain = Entry(root,width=15,borderwidth=8)
terrain.insert(0,"Enter the terrain modifier")
terrain.grid(row=0,column = 1,columnspan=8,padx=10,pady=10,sticky='we')
defend = Label(root,text = "Defender")
defend.grid(row=1,column = 1,columnspan=2)
attack = Label(root,text = "Attacker")
attack.grid(row=1,column = 7,columnspan=2)


#if u wanna put in params into your function,  for command do Lambda: function()
#technology
img_tech = ImageTk.PhotoImage(Image.open("C:/Users/bjaku/OneDrive/Desktop/EU4 sim/36px-mil_tech.png"))
img_label = Label(image=img_tech)
img_label1 = Label(image=img_tech)
tech = Label(root,text = "Technology")
techatt = Label(root,text="Technology")

#technology choice
tech.grid(row=2,column = 1)
img_label.grid(row=3,column=0)
optionmenu_a.grid(row=3,column=1)
img_label1.grid(row=3,column=6)
techatt.grid(row=2,column=7 )
optionmenu_a2.grid(row=3,column=7)

#morale,discipline
img_moral = ImageTk.PhotoImage(Image.open("C:/Users/bjaku/OneDrive/Desktop/EU4 sim/morale.png"))
moralimg_label = Label(image = img_moral)
moraleimg_label1 = Label(image=img_moral)
moralebox = Spinbox(root,from_=0,to=16.5,increment=0.1,width=4)
moralebox1 = Spinbox(root,from_=0,to=16.5,increment=0.1,width = 4)

moralimg_label.grid(row=4,column =0)
moralebox.grid(row=4,column=1)

moraleimg_label1.grid(row=4,column = 6)
moralebox1.grid(row=4,column = 7)

img_disci = ImageTk.PhotoImage(Image.open("C:/Users/bjaku/OneDrive/Desktop/EU4 sim/Discipline.png"))
discimg_label = Label(image = img_disci)
discimg_label1 = Label(image=img_disci)
discbox = Spinbox(root,from_=1,to=2,increment=0.05,width=4)
discbox1 = Spinbox(root,from_=1,to=2,increment=0.05,width = 4)

discimg_label.grid(row=5,column=0)
discbox.grid(row=5,column=1)

discimg_label1.grid(row=5,column = 6)
discbox1.grid(row=5,column=7)

#combat ability inf
img_inf_c = ImageTk.PhotoImage(Image.open("C:/Users/bjaku/OneDrive/Desktop/EU4 sim/infantry.png"))
inf_combat_img = Label(image=img_inf_c)
inf2_combat_img = Label(image=img_inf_c)
inf_combat_box = Spinbox(root,from_=0,to=1,increment=0.05,width=4)
inf_combat_box2 = Spinbox(root,from_=0,to=1,increment=0.05,width = 4)

inf_combat_img.grid(row=3,column = 2)
inf_combat_box.grid(row=3,column=3)

inf2_combat_img.grid(row=3,column =8 )
inf_combat_box2.grid(row=3,column=9)
#combat ability horse

img_cav = ImageTk.PhotoImage(Image.open("C:/Users/bjaku/OneDrive/Desktop/EU4 sim/cavalry.png"))
cav_combat_img = Label(image=img_cav)
cav2_combat_img = Label(image=img_cav)
cav_combat_box = Spinbox(root,from_=0,to=1,increment=0.05,width=4)
cav_combat_box2 = Spinbox(root,from_=0,to=1,increment=0.05,width = 4)

cav_combat_img.grid(row=4,column = 2)
cav_combat_box.grid(row=4,column=3)

cav2_combat_img.grid(row=4,column =8 )
cav_combat_box2.grid(row=4,column=9)

#combat ability arti
img_art = ImageTk.PhotoImage(Image.open("C:/Users/bjaku/OneDrive/Desktop/EU4 sim/artillery.png"))
art_combat_img = Label(image=img_art)
art_combat_img2 = Label(image=img_art)
art_combat_box = Spinbox(root,from_=0,to=1,increment=0.05,width=4)
art_combat_box2 = Spinbox(root,from_=0,to=1,increment=0.05,width = 4)

art_combat_img.grid(row=5,column = 2)
art_combat_box.grid(row=5,column=3)

art_combat_img2.grid(row=5,column =8 )
art_combat_box2.grid(row=5,column=9)

#leader stats
#def gen is actually thr attacking general while att general is actually the defending general
att_gen_info = Label(root,text="Leader")
def_gen_info = Label(root,text= "Leader")
def_gen_info.grid(row=6,column=7)
att_gen_info.grid(row=6,column=1)
#ldr fire
img_ldr_fire = ImageTk.PhotoImage(Image.open("C:/Users/bjaku/OneDrive/Desktop/EU4 sim/land_fire.png"))
ldr_fire_img = Label(image=img_ldr_fire)
ldr_fire_img2 = Label(image=img_ldr_fire)
ldr_fire= Spinbox(root,from_=0,to=6,increment=1,width=4)
ldr_fire2 = Spinbox(root,from_=0,to=6,increment=1,width = 4)

ldr_fire_img.grid(row=7,column = 0)
ldr_fire.grid(row=7,column=1)

ldr_fire_img2.grid(row=7,column =6 )
ldr_fire2.grid(row=7,column=7)
#ldr shock

img_ldr_shock = ImageTk.PhotoImage(Image.open("C:/Users/bjaku/OneDrive/Desktop/EU4 sim/land_shock.png"))
ldr_shock_img = Label(image=img_ldr_shock)
ldr_shock_img2 = Label(image=img_ldr_shock)
ldr_shock= Spinbox(root,from_=0,to=6,increment=1,width=4)
ldr_shock2 = Spinbox(root,from_=0,to=6,increment=1,width = 4)

ldr_shock_img.grid(row=7,column = 2)
ldr_shock.grid(row=7,column=3)

ldr_shock_img2.grid(row=7,column =8 )
ldr_shock2.grid(row=7,column=9)

#unit group
group_choice = Label(root,text="Tech Group")
group_choice2 = Label(root,text="Tech Group")
group_choice.grid(row=8,column=1)
group_choice2.grid(row=8,column=7)

optionmenu_b.grid(row=9,column=0,columnspan=2)
optionmenu_b2.grid(row=9,column=6,columnspan=2)


#units
regiments = Label(root,text="Regiments")
regiments2 = Label(root,text="Regiments")
regiments.grid(row=10,column=1)
regiments2.grid(row=10,column=7)
#inf
img_inf_unit = ImageTk.PhotoImage(Image.open("C:/Users/bjaku/OneDrive/Desktop/EU4 sim/inf_unit.png"))
inf_unit_img = Label(image=img_inf_unit)
inf_unit_img2 = Label(image=img_inf_unit)

inf_unit_img.grid(row=11,column=0)
inf_unit_img2.grid(row=11,column=6)

optionmenu_c.grid(row=11,column=1,columnspan=3)
optionmenu_c2.grid(row=11,column=7,columnspan=3)
#cav
img_cav_unit = ImageTk.PhotoImage(Image.open("C:/Users/bjaku/OneDrive/Desktop/EU4 sim/cav_unit.png"))
cav_unit_img = Label(image=img_cav_unit)
cav_unit_img2 = Label(image=img_cav_unit)
cav_unit_img.grid(row=12,column=0)
cav_unit_img2.grid(row=12,column=6)

optionmenu_cav.grid(row=12,column=1,columnspan=3)
optionmenu_cav2.grid(row=12,column=7,columnspan=3)

#art
img_art_unit = ImageTk.PhotoImage(Image.open("C:/Users/bjaku/OneDrive/Desktop/EU4 sim/art_unit.png"))
art_unit_img = Label(image=img_art_unit)
art_unit_img2 = Label(image=img_art_unit)
art_unit_img.grid(row=13,column=0)
art_unit_img2.grid(row=13,column=6)

optionmenu_art.grid(row=13,column = 1,columnspan=3)
optionmenu_art2.grid(row=13,column=7,columnspan=3)

#amounts of cav art and inf
inf_amt = Spinbox(root,from_=0,to=150,increment=1,width=4)
cav_amt = Spinbox(root,from_=0,to=150,increment=1,width=4)
art_amt = Spinbox(root,from_=0,to=150,increment=1,width=4)
inf_amt.grid(row=11,column=4)
cav_amt.grid(row=12,column=4)
art_amt.grid(row=13,column=4)

inf_amt2 = Spinbox(root,from_=0,to=150,increment=1,width=4)
cav_amt2 = Spinbox(root,from_=0,to=150,increment=1,width=4)
art_amt2 = Spinbox(root,from_=0,to=150,increment=1,width=4)
inf_amt2.grid(row=11,column=10)
cav_amt2.grid(row=12,column=10)
art_amt2.grid(row=13,column=10)



def run_calculations():
    inf = int(inf_amt.get())
    cav = int(cav_amt.get())
    art = int(art_amt.get())
    inf_combat = float(inf_combat_box.get())
    cav_combat = float(cav_combat_box.get())
    art_combat = float(art_combat_box.get())
    tech = int(tech_var.get())
    moral = float(moralebox.get())
    inf_u_name = unit_var.get()
    cav_u_name = cav_unit_var.get()
    art_u_name = art_unit_var.get()
    attack_inf = int(inf_amt2.get())
    attack_cav = int(cav_amt2.get())
    discipline = float(discbox.get())
    attack_art = int(art_amt2.get())
    attack_inf_combat = float(inf_combat_box2.get())
    attack_cav_combat =float(cav_combat_box2.get())
    attack_art_combat = float(art_combat_box2.get())
    attack_tech = int(tech_var2.get())
    attack_moral = float(moralebox1.get())
    attack_inf_u_name = unit_var2.get()
    attack_discipline = float(discbox1.get())
    attack_cav_u_name = cav_unit_var2.get()
    attack_art_u_name = art_unit_var2.get()
    terrainn = int(terrain.get())
    ldrr_fire = int(ldr_fire.get())
    ldrr_shock = int(ldr_shock.get())
    attack_ldr_fire = int(ldr_fire2.get())
    attack_ldr_shock = int(ldr_shock2.get())
    
    win,att_loss, def_loss = main.entire_battle_calculation(inf,cav,art,inf_combat,cav_combat,art_combat,tech,moral,inf_u_name,cav_u_name,
                                   art_u_name,attack_inf,attack_cav,discipline,attack_art,attack_inf_combat,
                                   attack_cav_combat,attack_art_combat,attack_tech,attack_moral,attack_inf_u_name,
                                   attack_discipline,attack_cav_u_name,attack_art_u_name,terrainn,ldrr_fire,ldrr_shock,
                                   attack_ldr_fire,attack_ldr_shock)  
    casualty_tab.config(text=def_loss)
    casualty_tab2.config(text=att_loss)  
    winner.config(text=win)
    print(win)
    print(att_loss)
    print(def_loss)
    
   

cas = Label(root,text = "Casualties")
cas.grid(row=14,column=1)
casualty_tab = Label(root,text="")
casualty_tab.grid(row=15,column =1,padx=6,columnspan=2)
cas2 = Label(root,text="Casualties")
cas2.grid(row=14,column = 7)
casualty_tab2 = Label(root,text="")
casualty_tab2.grid(row=15,column=7,padx=6,columnspan=2)

winner = Label(root,text="")
winner.grid(row = 16,column = 4,columnspan = 2)
start_button = Button(root,text="Simulate",command=run_calculations)
start_button.grid(row=17,column=4,columnspan=2)
root.mainloop()


#make sure to mention in the readme that the variables are flipped in gui visualization file 
#code works just the file looks confusing