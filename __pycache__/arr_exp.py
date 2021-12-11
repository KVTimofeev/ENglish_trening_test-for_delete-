import random


#сгенерируем множество случайных чисел не одно из которых не повторяется
it_rand_mass=[]
for i in range(8):
     it_rand_mass.append(random.randint(1,9))
print(it_rand_mass)