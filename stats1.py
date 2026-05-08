import random
import matplotlib.pyplot as plt

result = []
curr_prop = []
prop_sum = 0

xaxis = []

# 1 = head 0 = tail
for i in range(1, 10001):
    xaxis.append(i)
    x = random.randint(0, 1)
    prop_sum += x
    curr_prop.append(prop_sum / i)
    result.append(x)

head = sum(result) / len(result)
tail = (len(result) - sum(result)) / len(result)

print(head*100, tail*100)

fig, ax = plt.subplots(1, 1)

ax.set_title("Line graph for proportions")
ax.plot(xaxis, curr_prop)
plt.show()
