import random
import numpy

class Rand_mass:
   # в массив будет входить, массив перемешанных индексов ответов mass, индекс правильного ответа x,
   # функция должна вернуть массив с тремя разными числами-индексами
    def func(self,mass,right_x):
        ret_arr=[]
        ret_arr.append(right_x)
        lenght=len(mass)        
        a=random.randint(0,lenght-1)
        while a==right_x:
            a=random.randint(0,lenght-1)
        ret_arr.append(a)
        b=random.randint(0,lenght-1)
        while (b in ret_arr):
            b=random.randint(0,lenght-1)
        ret_arr.append(b)
        return ret_arr
        
    


    def f(self,len_mass):
        i=len_mass
        mass=[]
        while i>0: 
            if len(mass)==len_mass:
                break
            while True:
                x=random.randint(0,len_mass-1)
                if not x in mass:
                    mass.append(x)
                    i=i-1
                    break
                else:
                    continue
        return mass

#if __name__ == '__main__':
    #s=Rand_mass()
    #massive=numpy.random.permutation(12)
    #x=4
    #t=s.func(massive,x)
    #print(t)



        #for x in mass:

        #x=random.randint(0,len_mass-1)
