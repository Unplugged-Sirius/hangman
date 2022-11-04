print('''
888                                                           
888                                                           
888                                                           
88888b.    8888b.   88888b.    .d88b.   88888b.d88b.    8888b.   88888b.  
888 "88b      "88b  888 "88b  d88P"88b 888 "888 "88b     "88b8  88  "88b 
888  888  .d888888  888  888  88  888  888  888  888  .d888888  888   888 
888  888  888  888  888  88Y  88b 888  888  888  888  888  888  888   888 
888  888  "Y888888  888  888  "Y88888  888  888  888  "Y888888  888   888 
                                  888                              
                            Y8b  d88P                              
                              "Y8 8P"                               ''')
animes=["Naruto","OnePiece","Death Note","Hellsing","Dragonball","Get Backers","Blood+","Ghost","Code Geass", "Maid Sama"
"Toradora",
"Ouran High School Host Club",
"Clannad",
"Kimi Ni Todoke",
"Sket Dance",
"Melancholy of haruhi suzumiya"]
import random
choice=random.choice(animes)
count=5
print(choice)
print("make a first guess")
print("here are the blanks")
choice=choice.lower()
lens=len(choice)
choice1=[]
for q in range(0,lens):
    choice1.append("_")
print(choice1)
for k in choice:
    s= input("here take a guess")
    for i in range(0,lens):
        if(choice[i]==s):
            choice1[i]=s
    print(choice1)
    if(count==0):
        print("you loose the game")
        break
    elif(s not in choice):
        print(f"remaining guesses{count}")
        count=count-1