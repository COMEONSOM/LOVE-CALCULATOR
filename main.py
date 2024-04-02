# Project Name: Love Calculator
name1=input(str('Write your name:  ')) #input of username
name2=input(str('Write your partner name:  ')) #input of user's partner name
upname1=name1.upper() #uppercase of inserted first name
upname2=name2.upper() #uppercase of inserted second name
n1=(upname1.split(" ") ) [0] #name of the user
n2=(upname2.split(" ") ) [0] #name of the user's partner
s1=(upname1.split(" ") ) [1] #surname of the user
s2=(upname2.split(" ") ) [1] #surname of the user's partner
N1=n1[0:2] #first two letters of the user's name
N2=n2[0:2] #first two letters of the user's partner name
A1=s1[0:2] #first two letters of the user's surname
A2=s2[0:2] #first two letters of the user's partner surname
A3=name1.count(name1) #count of letters including space of inserted user name
A4=name2.count(name2) #count of letters including space of inserted user's partner name
import random #importing random to randomly pick between provided data
rand1 = random.randint (94,100)
rand2 = random.randint (88,93)
rand3 = random.randint (76,87)
rand4 = random. randint(56,75)
K = (n2,"sees you as a source of unwavering support."),("Your partner see you as a co-creator of a future built on mutual goals and ambitions."),("Your partner values the emotional intensity you bring to the relationship, embracing the fervent energy that fuels the flames of desire,making each moment an exploration of profound connection")
M = ("In moments of reflection, your partner appreciates the evolution you've undergone together."),("Your partner witness the growth, not only as individuals but as a united force navigating the ebb and flow of life."),("Your partner values the commitment and effort invested in the relationship, recognizing it as the foundation upon which your shared history is constructed."),(n2,"perceives you as a constant source of joy and companionship."),("Whether it's the everyday routines or special milestones, your partner revel in the happiness created by your presence."),("Your partner admires the way you navigate life with an unwavering commitment to authenticity.")
F = ("In the quiet moments of contemplation, your partner sees you as the most important part of life."),("Your life partner is enamored by the unique qualities that define you, finding irresistible charm in the nuances of your personality that evoke a sense of wonder and fascination."),("To your life partner, you are a firework of emotions, each burst reflecting the depth of your connection."),(n2,"cherish the vulnerability you share, considering it a sacred gift that binds you in a tapestry of trust and intimacy."),("Your partner revels in the passion that permeates every glance, touch, and whispered word, weaving a narrative of desire that transcends the ordinary."),("In the canvas of their thoughts, your life partner envisions a future marked by shared dreams and unbridled passion."),("Your better-half see you as a co-conspirator in the pursuit of a love that defies boundaries and expectations.")
if N1 == N2 and A1 == A2:
    print ('You are the Soul Mates.\n''Your Love Score is:  ',rand1,'%')
    print ('See What Tarrot Says............ ')
    print (random.choice(F))
elif N1 == N2 and A1 != A2:
    print ('Your Love Score is:  ',rand2,'%')
    print ('See What Tarrot Says............ ')
    print (random.choice(F))
elif A3 == A4:
    print ('Your Love Score is:  ',rand3,'%')
    print ('See What Tarrot Says............ ')
    print (random.choice(M))
else:
    print ('Your Love Score is:  ',rand4,'%')
    print ('See What Tarrot Says............ ')
    print (random.choice(K))