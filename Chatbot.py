from tkinter import *

root = Tk()
root.title('IT SOURCCODE SIMPLE CHATBOT')
root.mainloop()


def send(text):
    send = "You:"+ e.get()
    text.insert(END,"\n" + send)
    if(e.get()=='hi'):
        text.insert(END, "\n" + "Bot: hello")
    elif(e.get()=='hello'):
        text.insert(END, "\n" + "Bot: hi")
    elif (e.get() == 'how are you?'):
        text.insert(END, "\n" + "Bot: i'm fine and you?")
    elif (e.get() == "i'm fine too"):
        text.insert(END, "\n" + "Bot: nice to hear that")
    else:
        text.insert(END, "\n" + "Bot: Sorry I didnt get it.")
text = Text(root,bg='light blue')
text.grid(row=0,column=0,columnspan=2)
e = Entry(root,width=80)
send = Button(root,text='Send',bg='blue',width=20,command=send).grid(row=1,column=1)
e.grid(row=1,column=0)
root = Tk()
root.title('IT SOURCCODE SIMPLE CHATBOT')
root.mainloop()