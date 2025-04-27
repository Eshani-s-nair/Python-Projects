import random

def play():
    
    user=input("what's your choice?\n rock(r),paper(p) or scissors (s)\n").lower()
    computer=random.choice(['r','s','p'])
    if user ==computer:
        return "its a tie "
    if is_win(user,computer):
        return "you win"
    return " you lost !!"

#r>s s>p p>r
def is_win(player,opponent) :
    if(player=='r'and opponent=='s')or (player=='s' and opponent=='p') or (player=='p' and opponent=='r') :
        return True



for i in range(1,6): 
   print( play())

