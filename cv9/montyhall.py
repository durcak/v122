import random

def montyhall(N):
    staywins   = 0
    changewins  = 0
    randomwins = 0
    doors      = [1,2,3]
     
    for _ in xrange(N):
        treasure = random.choice(doors)  # cislo dvier kde je poklad
        guess   = random.choice(doors)  # moja prva volba
 	
        shown   = random.choice(filter(lambda d: d!=treasure and d!=guess, doors))   # otvorim dvere, kde nieje poklad
        other   =               filter(lambda d: d!=shown   and d!=guess, doors)[0] # dvere ktore este neboli vybrate
         
        randomwins += treasure == random.choice([guess, other])
        staywins   += treasure == guess
        changewins  += treasure == other

 
    print ('Stay:  %d wins' % staywins, '=', staywins * 100 / N, '%')
    print ('Change: %d wins' % changewins, '=', changewins * 100 / N, '%')
    print ('Random: %d wins' % randomwins, '=', randomwins * 100 / N, '%')

montyhall(100000)


#*vysledok
#('Stay:  33276 wins', '=', 33, '%')
#('Change: 66724 wins', '=', 66, '%')
#('Random: 49975 wins', '=', 49, '%')

