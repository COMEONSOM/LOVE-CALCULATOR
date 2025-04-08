# Love Calculator
import random

name1 = input('Write your name:  ')
name2 = input('Write your partner name:  ')

upname1 = name1.upper()
upname2 = name2.upper()

parts1 = upname1.split(" ")
parts2 = upname2.split(" ")

n1 = parts1[0]
n2 = parts2[0]
s1 = parts1[1] if len(parts1) > 1 else ""
s2 = parts2[1] if len(parts2) > 1 else ""

N1 = n1[0:2]
N2 = n2[0:2]
A1 = s1[0:2]
A2 = s2[0:2]

A3 = len(name1)
A4 = len(name2)

rand1 = random.randint(94, 100)
rand2 = random.randint(88, 93)
rand3 = random.randint(76, 87)
rand4 = random.randint(56, 75)

K = [
    f"{n2} sees you as a source of unwavering support.",
    "Your partner sees you as a co-creator of a future built on mutual goals and ambitions.",
    "Your partner values the emotional intensity you bring to the relationship, embracing the fervent energy that fuels the flames of desire."
]

M = [
    "In moments of reflection, your partner appreciates the evolution you've undergone together.",
    "Your partner witnesses the growth, not only as individuals but as a united force navigating life.",
    "Your partner values the commitment and effort invested in the relationship.",
    f"{n2} perceives you as a constant source of joy and companionship.",
    "Your partner revels in the happiness created by your presence.",
    "Your partner admires your authenticity."
]

F = [
    "In the quiet moments of contemplation, your partner sees you as the most important part of life.",
    "Your life partner is enamored by your unique qualities.",
    "To your life partner, you are a firework of emotions.",
    f"{n2} cherishes the vulnerability you share.",
    "Your partner revels in the passion that permeates every glance and whisper.",
    "In their thoughts, your partner envisions a future filled with shared dreams.",
    "Your better-half sees you as a co-conspirator in a love that defies expectations."
]

print("\n🔮 See What Tarot Says...")

if N1 == N2 and A1 == A2:
    print(f"You are Soul Mates!\nYour Love Score is: {rand1}%")
    print(random.choice(F))
elif N1 == N2 and A1 != A2:
    print(f"Your Love Score is: {rand2}%")
    print(random.choice(F))
elif A3 == A4:
    print(f"Your Love Score is: {rand3}%")
    print(random.choice(M))
else:
    print(f"Your Love Score is: {rand4}%")
    print(random.choice(K))
