from tkinter import*
import tkinter as ttk
import random

class Chatbot:
    def __init__(self,root):
        self.root = root
        self.root.geometry('700x600+310+30')#(h,w,xaxis,yaxis)
        self.root.title('My ChatGpt')
        #---------Title--------
        lbl_title = Label(self.root,text='ChatGpt Developed By Prachiti Patil',font=('times new roman',20,'bold'))
        lbl_title.place(x=130,y=10)

        #--------main frame with scroll bar and text area--------
        main_frame =Frame(self.root,bd=2,relief=RAISED,bg='aquamarine3')#var named as main_frame
        main_frame.place(x=0,y=60,width=700,height=400)#placing it

        #----------Text area------------
        self.scroll_y = ttk.Scrollbar(main_frame, orient=VERTICAL)#variable as
        self.text = Text(main_frame, width=65, height=20, font=('arial', 14),bg='aquamarine3', relief=RAISED,
                         yscrollcommand=self.scroll_y.set)
        self.scroll_y.pack(side=RIGHT, fill=Y)
        self.text.pack()

        #-------------search label-----------
        lbl_search = Label(self.root,text='Search Here',font=('times new roman',17,'bold'))
        lbl_search.place(x=30,y=500)

        #-----------Entry Area--------
        self.entry=ttk.Entry(self.root,font=('times new roman',15,'bold'))
        self.entry.place(x=200,y=480,width=400,height=35)

        # =====btn save
        self.btn_send = ttk.Button(self.root,command=self.send,  width=20, text='Send',
                                   font=('times new roman', 14, 'bold'), bg='black', fg='white')
        self.btn_send.place(x=200, y=520, width=200, height=30)

        # =====btn clr
        self.btn_clr = ttk.Button(self.root, width=20, text='Clear',
                                  font=('times new roman', 14, 'bold'), bg='black', fg='white')
        self.btn_clr.place(x=410, y=520, width=200, height=30)

#------------Functions Starts(Backend)--------------------
    def send(self):
       user_input = "\t\t\t" + "You: " + self.entry.get()
       self.text.insert(END, "\n" + user_input)

       input_list = ['hi', 'hey', 'helo', 'how are you', 'whats up']
       output_list = ['hi', 'I am good', 'nice to see you', 'helo','I am fine']

       for mess in input_list:
           if self.entry.get() == mess:
               mess_into_text = random.choice(output_list)#mess_into_text var
               self.text.insert(END,'\n\n'+"Bot :"+mess_into_text)
       data_sience = "data science is a growing field now a days. It has many \n" \
                     "application in daily life. it has the following branches \n1: machine learning\n2: deep learning \n3: NLP"
       if self.entry.get() == "what is data science" or self.entry.get() == "about data science":
           self.text.insert(END, '\n\n' + data_sience)
       google = "Google is a big tech company throghout the world.\nchrome is the leading app of google."
       if self.entry.get() == "google" or self.entry.get() == "about google":
           self.text.insert(END, '\n\n' + google)

       if self.entry.get() == "richest person of the world" or self.entry.get() == "richest person":
           self.text.insert(END, '\n\n' + "Elon must with $10,000 Bilion")
       # else:
       #     self.text.insert(END,'\n\n'+'Sorry! I didnt get you')


#////////////////////////////
if __name__ == "__main__":  #main function in python
    root = Tk() #object named as root having in tkinter
    obj = Chatbot(root)  #obj of chatbot class ans passing root into it
    root.mainloop()
