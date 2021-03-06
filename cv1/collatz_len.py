import matplotlib.pyplot as plt

def collatz_st(n):
    steps = 1
    while n != 1:
        steps += 1
        if n % 2 == 0:
            n /= 2
        else:
            n = 3*n + 1
    	print(steps)
    return steps


interval = range(1, 25)
values = list(map(collatz_st, interval))
plt.plot(interval, values, 'ko')
plt.savefig('collatz_len_25_2.png')
