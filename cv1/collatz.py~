import matplotlib.pyplot as plt

def collatz_max(n):
    maxN = n # is max
    while n != 1:
        # maxN = max(maxN,n)

        if n % 2 == 0:
            n /= 2
        else:
            n = 3*n + 1

	maxN = max(maxN,n)
    return maxN

interval = range(1,1000)
values = list(map(collatz_max, interval))

plt.yscale('log')
plt.plot(interval, values, 'ko')
plt.savefig('collatz_max.png')
