#2.4.1 Print numbers from 1 to 20 and skip multiples of 4

for i in range(1, 21):
    if i % 4 == 0:
        continue
    print(i)
