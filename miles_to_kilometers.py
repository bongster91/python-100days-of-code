import tkinter

window = tkinter.Tk()
window.title('My first GUI Program')
window.minsize(width=600, height=400)

my_label = tkinter.Label(text="I am a label", font=('Arial', 24, 'bold'))
my_label.pack()

my_label['text'] = 'new text'
my_label.config(text='new text')

def button_clicked():
    my_label['text'] = user_input

button = tkinter.Button(text='Click me', command=button_clicked)
button.pack()

input = tkinter.Entry(width=10)
input.pack()
user_input = input.get()

window.mainloop()