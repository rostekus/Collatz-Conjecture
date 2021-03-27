import csv
from tkinter import *
import time 
import matplotlib.pyplot as plt



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
    my_label.config(text = 'Stats')
    my_label.update()






root = Tk();
root.title("Collatz Conjecture")

e = Entry(root, text = 'Enter number')
e.grid(row =0, columnspan = 2)

start_button = Button(root, text = 'Start', command = collatz_fun)
start_button.grid(row =1, columnspan = 2)

root.mainloop()