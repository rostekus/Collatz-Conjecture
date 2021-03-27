import csv
from tkinter import *
import time 
import matplotlib.pyplot as plt
import numpy as np

def end_fun():
    end_label = Label(root, row = 3, column = 0)

def array_collatz(number):
    i = 0
    x = []
    y = []
    x.append(number)
    y.append(i)
    while number != 1:
        if number % 2 == 0:
            number //= 2
        else:
            number = 3*number +1
        i += 1
        x.append(number)
        y.append(i)
        
    return x,y

    

def graph(x,y):
    plt.plot(x,y)
    plt.show()


def save_to_csv():
    with open('collatz.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Step", "Number"])

def collatz_fun():
    start = e.get()
    start_num = int(start)
    step = 0
    i = 2
 
    my_label = Label(root, text =str(start_num))
    my_label.grid(row = 3, column = 1)

    while start_num != 1:
        print(start_num)
        if(start_num %2 == 0):
            start_num //= 2
        else:
            start_num = 3*start_num +1 
        i +=1
        my_label.config(text = str(start_num))
        my_label.update()
        root.after(1000)
    






root = Tk();
root.title("Collatz Conjecture")

e = Entry(root, text = 'Enter number')
e.grid(row =0, columnspan = 2)

start_button = Button(root, text = 'Graph', command = collatz_fun)
start_button = Button(root, text = 'Save to csv', command = save_to_csv)

start_button.grid(row =1, columnspan = 2)


x,y= array_collatz(10)
print(x)
print(y)
graph(y,x)

root.mainloop()