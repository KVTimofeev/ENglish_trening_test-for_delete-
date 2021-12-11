import os #для показа текущего каталога
from pathlib import Path 
import MassiveWords
import random
import numpy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
import rand_mass
#kivy.require('1.0.7')




class MaketApp(App): 
     def UpdateAnswerButtosns(self):
          x=self.mass[self.order_index]
          Word=self.massive_m[x][0]
          Obj_rand_mass=rand_mass.Rand_mass()
          self.array_numbs_of_answers=Obj_rand_mass.func(self.mass,x)
          self.word.text=Word
          right_wort=self.massive_m[x][1]
          self.btn_right_answ.text=right_wort
          self.btn_answ.text=self.massive_m[self.array_numbs_of_answers[1]][1]
          self.btn_answ2.text=self.massive_m[self.array_numbs_of_answers[2]][1]

          self.main_layout_box.remove_widget(self.answers_box_layout)




          btn_right_answ=Button(text=right_wort)
          btn_right_answ.bind(on_press=self.click_right)
          btn_answ=Button(text=self.massive_m[self.array_numbs_of_answers[1]][1])
          btn_answ2=Button(text=self.massive_m[self.array_numbs_of_answers[2]][1])
          list_btns=[]
          list_btns.append(btn_answ)
          list_btns.append(btn_answ2)
          list_btns.append(btn_right_answ)
          random.shuffle(list_btns)
          #создаме горизонтальный макет внутри мактеа для ответов
          self.answers_box_layout=BoxLayout()
          self.answers_box_layout.add_widget(list_btns[0])
          self.answers_box_layout.add_widget(list_btns[1])
          self.answers_box_layout.add_widget(list_btns[2])
          self.main_layout_box.add_widget(self.answers_box_layout)

          #self.answers_box_layout.

     def click_right(self,*args):
          self.reit_balls=self.reit_balls+1
          self.order_index=self.order_index+1
          self.balls.text='Количество баллов {}'.format(self.reit_balls)
          self.UpdateAnswerButtosns()

     def __init__(self,*args):
          super().__init__(*args)
          #узнаем численный размер массива
          self.leng=len(MassiveWords.some_list)
          # здесь мы формируем массив из случайного набора чисел длины указанной в скобках
          #именно осюда будет править  главное слово и ответ на него
          self.mass=numpy.random.permutation(self.leng)
          #тут массив массивов с оригинальным словом и переводом
          self.massive_m=MassiveWords.some_list
          #x2 это случайное число от 0 до последнего индекса массива
          x2=random.randint(0,len(self.mass)-1);
          #количество баллов, увеличивается при правильном ответе
          self.reit_balls=0
          #первое слово который пользователь должен будет потом угадать
          #формат хранения [[a,b],[c,d]] где а и с это слова на англ. а вот  'b' 'd' это перевод
          #порядок индекса по которому пойдет верный ответ
          self.order_index=0
          # присвоем икс первое значения из массива mass
          x=self.mass[self.order_index]
          Word=self.massive_m[x][0]
          #вариант правильного ответа этого слова как видно вторая ячека тперь 1 т.е. 
          right_wort=self.massive_m[x][1]
          #назначаем основной макет в который будет вкладывать виджеты
          self.main_layout_box=BoxLayout(orientation='vertical')
          self.word=Label(text=Word)
          self.main_layout_box.add_widget(self.word)
          self.balls=Label(text='Количество баллов {}'.format(self.reit_balls))
          self.main_layout_box.add_widget(self.balls)                    
          #теперь сформируем макет из 3 ответов
          Obj_rand_mass=rand_mass.Rand_mass()
          #объявляю массив
          self.array_numbs_of_answers=Obj_rand_mass.func(self.mass,x)
          #arr=random.shuffle(self.array_numbs_of_answers)
          #далее я создаю три кнопки
          self.btn_right_answ=Button(text=right_wort)
          self.btn_right_answ.bind(on_press=self.click_right)
          self.btn_answ=Button(text=self.massive_m[self.array_numbs_of_answers[1]][1])
          self.btn_answ2=Button(text=self.massive_m[self.array_numbs_of_answers[2]][1])
          list_btns=[]
          list_btns.append(self.btn_answ)
          list_btns.append(self.btn_answ2)
          list_btns.append(self.btn_right_answ)
          random.shuffle(list_btns)
          #создаме горизонтальный макет внутри мактеа для ответов
          self.answers_box_layout=BoxLayout()
          self.answers_box_layout.add_widget(list_btns[0])
          self.answers_box_layout.add_widget(list_btns[1])
          self.answers_box_layout.add_widget(list_btns[2])
          self.main_layout_box.add_widget(self.answers_box_layout)
          
          #self.answers_box_layout.add_widget( self.btn_right_answ)
          #self.answers_box_layout.add_widget(self.btn_answ)
          #self.answers_box_layout.add_widget(self.btn_answ2)
          
          

          



     def work(self):
          pass

          

    
    
     def build(self):  
          layout_box=self.main_layout_box      
          return layout_box


if __name__ == '__main__':
    print("начало работы")
    MaketApp().run()

     
     