
def checkrandom():
    for i in range(1,8):
        filename  = 'random%d.txt' % i
        txtfile   = open(filename)
        cisla   = map(int, txtfile.read().split())
        count     = len(cisla)
        pocetnost = [0, 0, 0, 0, 0, 0]
        sused     = [ [0]*6 for _ in range(6) ]
	print pocetnost
	print sused
 
        for i in range(count-1):
            p = cisla[i]
            s = cisla[i+1]
            sused[p-1][s-1] += 1
            pocetnost[p-1]  += 1
 
        print filename
        for i in range(6):
            #print '%d x %d, parovanie = %s' % (i+1, pocetnost[i], sused[i])
	    print '%d x %d' % (i+1, pocetnost[i])
 
        txtfile.close()

checkrandom()

#vysledky
"""
random1.txt
1 x 833
2 x 834
3 x 833
4 x 833
5 x 833
6 x 833
random2.txt
1 x 855
2 x 428
3 x 829
4 x 845
5 x 1244
6 x 798
random3.txt
1 x 819
2 x 836
3 x 850
4 x 823
5 x 821
6 x 850
random4.txt
1 x 852
2 x 827
3 x 828
4 x 850
5 x 819
6 x 823
random5.txt
1 x 807
2 x 836
3 x 812
4 x 843
5 x 842
6 x 859
random6.txt
1 x 849
2 x 850
3 x 849
4 x 846
5 x 803
6 x 802
random7.txt
1 x 838
2 x 842
3 x 823
4 x 834
5 x 832
6 x 830
"""

