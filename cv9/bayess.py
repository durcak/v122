from operator import mul

throws = [1,3,4,5,1,4,6,5,1,5,4,5]              #namerane data
prior1 = [ 1/3., 1/3., 1/3. ]			#verime vsetkym rovnako	
prior2 = [ 0.05, 0.05, 0.90 ]


def bayes(throws, pH):

    die1 = [0, 1/6.,1/6.,1/6.,1/6.,1/6.,1/6.]  #uniformna kocka
    die2 = [0, 1/6.,0,   1/6.,1/6.,2/6.,1/6.]  #miesto dvojky pada 5
    die3 = [0, 1/7.,1/7.,1/7.,1/7.,1/7.,2/7.]  #6 pada 2x castejsie ako ostatne cisla
    dice = [die1, die2, die3]
 
#   P(Hi/D) = P(D/Hi)*P(Hi) / P(D)
          
    pDH  = [ reduce(lambda acc,next: acc*die[next], throws) for die in dice ]

    #print pDH
    pD   = sum( [ pDH[i] * pH[i] for i in range(3) ])
    pHD  = [ pDH[i] * pH[i] / pD for i in range(3) ]
 
    
    print tuple([ round(p, 2) for p in pHD ])

bayes(throws, prior1)
#(0.06, 0.92, 0.02)

bayes(throws, prior2)
#(0.04, 0.68, 0.28)

#v oboch vysla najvacsia p pri kocke 2
