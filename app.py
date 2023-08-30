# Importing the required module from tkinter library
from tkinter import *
from my_db import Database
from tkinter import messagebox
from myapi import API
import os

# Define the Nlp class
class Nlp:

    def __init__(self):
        # Creating an instance of the Tk class

        self.my_cursor = Tk()

        # Creating database Object
        self.mydbo = Database()

        self.apio = API()

        # Set the icon for the window
        self.my_cursor.iconbitmap('Resources/favicon.ico')

        # Change the color of the background
        self.my_cursor.config(bg='#2E4053')

        # Set geometry
        self.my_cursor.geometry("400x700")

        # Setting the title of the window
        self.my_cursor.title("NLP Application")

        # Call method of login gui method
        self.gui()

        # Start the event loop of the application
        self.my_cursor.mainloop()

    def gui(self):
        self.clear()
        heading = Label(self.my_cursor, text="NLP APP", bg='#2E4053', fg="white", font=('verdana', 24, 'bold'))
        heading.pack(pady=(20, 20))

        label1 = Label(self.my_cursor, text='Enter Your Email', font=('verdana', 12))
        label1.pack(pady=(20, 5))

        entry1 = Entry(self.my_cursor, width=30, font=('verdana', 12))
        entry1.pack(pady=(2, 20), ipady=5)

        label2 = Label(self.my_cursor, text='Password', font=('verdana', 12))
        label2.pack(pady=(20, 5))

        entry2 = Entry(self.my_cursor, width=30, show='*', font=('verdana', 12))
        entry2.pack(pady=(2, 20), ipady=5)

        button = Button(self.my_cursor, text='Login', font=('verdana', 12), bg='#4CAF50', fg='white',
                        command=self.perform_login)
        button.pack(pady=(2, 20))

        label2 = Label(self.my_cursor, text='Not a Member?', font=('verdana', 12))
        label2.pack(pady=(20, 5))

        Re_button = Button(self.my_cursor, text='Register', font=('verdana', 12), bg='#4CAF50', fg='white',
                           command=self.register_gui)
        Re_button.pack(pady=(2, 20))

        # Storing email and password
        self.email = entry1
        self.password = entry2

    def register_gui(self):
        self.clear()

        heading = Label(self.my_cursor, text="NLP", bg='#2E4053', fg="white", font=('verdana', 24, 'bold'))
        heading.pack(pady=(20, 20))

        label1 = Label(self.my_cursor, text='Enter Your Name', font=('verdana', 12))
        label1.pack(pady=(20, 5))

        entry1 = Entry(self.my_cursor, width=30, font=('verdana', 12))
        entry1.pack(pady=(2, 20), ipady=5)

        label2 = Label(self.my_cursor, text='Enter Your Email', font=('verdana', 12))
        label2.pack(pady=(20, 5))

        entry2 = Entry(self.my_cursor, width=30, font=('verdana', 12))
        entry2.pack(pady=(2, 20), ipady=5)

        label3 = Label(self.my_cursor, text='Password', font=('verdana', 12))
        label3.pack(pady=(20, 5))

        entry3 = Entry(self.my_cursor, width=30, show='*', font=('verdana', 12))
        entry3.pack(pady=(2, 20), ipady=5)

        Re_button = Button(self.my_cursor, text='Register', font=('verdana', 12), bg='#4CAF50', fg='white',
                           command=self.perform_registion)
        Re_button.pack(pady=(2, 20))

        label4 = Label(self.my_cursor, text='Already a Member?', font=('verdana', 12))
        label4.pack(pady=(20, 5))

        button = Button(self.my_cursor, text='Login Now', font=('verdana', 12), bg='#4CAF50', fg='white',
                        command=self.gui)
        button.pack(pady=(2, 20))

        # Storing name, email, and password
        self.name = entry2
        self.email = entry1
        self.password = entry3

    def perform_registion(self):
        name = self.name.get()
        email = self.email.get()
        password = self.password.get()
        response = self.mydbo.add_data(name, email, password)
        if response:
            messagebox.showinfo('success', 'Registration Successful, Now you can Proceed')
        else:
            messagebox.showerror('Error', 'email is Already Exists')

    def perform_login(self):

        email = self.email.get()
        password = self.password.get()
        response = self.mydbo.search(email, password)
        if response:
            messagebox.showinfo('Success', 'Login successfully')
            self.home_gui()
        else:
            messagebox.showerror('Error', 'incorrect password/email')

    def home_gui(self):
        self.clear()
        heading = Label(self.my_cursor, text="NLP", bg='#2E4053', fg="white", font=('verdana', 24, 'bold'))
        heading.pack(pady=(20, 20))

        button1 = Button(text='Sentiment Analysis', font=('verdana', 12), bg='#4CAF50', fg='white',
                         command=self.sentiment_analysis)

        button1.pack(pady=(20, 20))

        button2 = Button(text='Named Entity Recognition', font=('verdana', 12), bg='#4CAF50', fg='white',
                         command=self.named_entity_recognition)

        button2.pack(pady=(20, 20))

        button3 = Button(text='Emotion Prediction', font=('verdana', 12), bg='#4CAF50', fg='white',
                         command=self.emotion_prediction)
        button3.pack(pady=(20, 20))

        # Logout Buttom and redirect to home screen
        button4 = Button(text='LogOut', font=('verdana', 12), bg='#4CAF50', fg='white', command=self.gui, width=5,
                         height=1)
        button4.pack(pady=(20, 20))

    def clear(self):
        # Clear the existing objects
        for i in self.my_cursor.pack_slaves():
            i.destroy()

    def sentiment_analysis(self):

        self.clear()
        heading = Label(self.my_cursor, text="NLP", bg='#2E4053', fg="white", font=('verdana', 24, 'bold'))
        heading.pack(pady=(20, 20))

        label2 = Label(self.my_cursor, text="Sentiment Analysis", bg='#2E4053', fg="white",
                       font=('verdana', 12, 'bold'))
        label2.pack(pady=(20, 20))

        label2 = Label(self.my_cursor, text="Enter Your Text", bg='#2E4053', fg="white",
                       font=('verdana', 12, 'bold'))
        label2.pack(pady=(20, 20))

        self.sentiment_input = Entry(self.my_cursor, width=30, font=('verdana', 12))
        self.sentiment_input.pack(pady=(2, 20), ipady=5)

        self.result_sentiment_analysis = Label(text='', bg="#2E4053", fg='white', font=('verdana', 12))
        self.result_sentiment_analysis.pack(pady=(20, 20))

        button3 = Button(text='Sentiment Analysis', font=('verdana', 12), bg='#4CAF50', fg='white',
                         command=self.do_sentiment,
                         height=1)
        button3.pack(pady=(20, 20))

        button4 = Button(text='Back', font=('verdana', 12), bg='#4CAF50', fg='white', command=self.home_gui, width=5,
                         height=1)
        button4.pack(pady=(20, 20))

    def named_entity_recognition(self):

        self.clear()
        heading = Label(self.my_cursor, text="NLP", bg='#2E4053', fg="white", font=('verdana', 24, 'bold'))
        heading.pack(pady=(20, 20))

        label2 = Label(self.my_cursor, text="Named Entity Recognition", bg='#2E4053', fg="white",
                       font=('verdana', 12, 'bold'))
        label2.pack(pady=(20, 20))

        label2 = Label(self.my_cursor, text="Enter Your Text", bg='#2E4053', fg="white",
                       font=('verdana', 12, 'bold'))
        label2.pack(pady=(20, 20))

        self.name_input = Entry(self.my_cursor, width=30, font=('verdana', 12))
        self.name_input.pack(pady=(2, 20), ipady=5)

        self.result_name_entity = Label(text='', bg="#2E4053", fg='white', font=('verdana', 12))
        self.result_name_entity.pack(pady=(20, 20))

        button3 = Button(text='Named_Entity_Recognition', font=('verdana', 12), bg='#4CAF50', fg='white',
                         command=self.do_named_entity_recognition)
        button3.pack(pady=(20, 20))

        button4 = Button(text='Back', font=('verdana', 12), bg='#4CAF50', fg='white', command=self.home_gui, width=5,
                         height=1)
        button4.pack(pady=(20, 20))

    def emotion_prediction(self):
        self.clear()
        heading = Label(self.my_cursor, text="NLP", bg='#2E4053', fg="white", font=('verdana', 24, 'bold'))
        heading.pack(pady=(20, 20))

        label2 = Label(self.my_cursor, text="Emotion Prediction", bg='#2E4053', fg="white",
                       font=('verdana', 12, 'bold'))
        label2.pack(pady=(20, 20))

        label2 = Label(self.my_cursor, text="Enter Your Text", bg='#2E4053', fg="white",
                       font=('verdana', 12, 'bold'))
        label2.pack(pady=(20, 20))

        self.emotion_input = Entry(self.my_cursor, width=30, font=('verdana', 12))
        self.emotion_input.pack(pady=(2, 20), ipady=5)

        self.result_emotion = Label(text='', bg="#2E4053", fg='white', font=('verdana', 12))
        self.result_emotion.pack(pady=(20, 20))

        button3 = Button(text='Emotion Prediction', font=('verdana', 12), bg='#4CAF50', fg='white',
                         command=self.do_emotion_prediction)
        button3.pack(pady=(20, 20))

        button4 = Button(text='Back', font=('verdana', 12), bg='#4CAF50', fg='white', command=self.home_gui, width=5,
                         height=1)
        button4.pack(pady=(20, 20))

    def do_sentiment(self):
        txt = self.sentiment_input
        result = self.apio.sentiment_result(txt)

        string = ''
        for i in result['sentiment']:
            string = string + i + ' -> ' + str(result['sentiment'][i]) + '\n'

        self.result_sentiment_analysis['text'] = string

    def do_named_entity_recognition(self):
        txt = self.name_input
        result = self.apio.ner(txt.get())
        print(result)
        entities_list = []
        for entity in result['entities']:
            entity_name = entity['name']
            entity_category = entity['category']
            entity_info = f"{entity_category}:{entity_name}"
            entities_list.append(entity_info)
        string = '\n'.join(entities_list)
        print(string)
        self.result_name_entity['text'] = string

    def do_emotion_prediction(self):
        txt = self.emotion_input.get()
        result = self.apio.emotion([txt])
        emotions = result['emotion'][0]
        highest_value = max(emotions, key=lambda x: emotions[x])

        self.result_emotion['text'] = highest_value


app = Nlp()
gg
