"""
This project aims to  create an environment for students to participate in a
speed typing competition where students names are retrieved from a txt file
student.txt. The environment is provided usig tkinter and each student's time is
recorded.All students are given equal length of sentence and speed is recorded.
The speed is stored in a dictionary to pushed to pickle file for storage and further use.
The data from the pickle file is retreived to calculate the winner.The names v/s speed graph
is made with help of data visualization concept to give a good presentation.And finally is winner
is announced in an GUI environment.

"""
import tkinter as tk
import time
import matplotlib.pyplot as plt
import pickle as pkl
import random
class TypingSpeedTest:
    def __init__(self):
        self.student_names = self.get_student_names()#returns student names
        self.typing_speeds = self.prompt_students_to_type()
        #provide an environment to type

    def get_student_names(self):
        with open('students.txt', 'r') as f:
            student_names = f.readlines()

        student_names = [name.strip() for name in student_names]
        #returns student list
        #print(type(student_names))
        return student_names

    def prompt_students_to_type(self):
        sentences = ["Abc fed jio kol lop jio","qwe klo fed sop vbn mio"
                        ,"ert klo def gyh bnm dsa","iok hui jkl grf des hjk"]
        typing_speeds = {}

        for student_name in self.student_names:
            root = tk.Tk()
            root.configure(bg="steel blue")
            image = tk.PhotoImage(file="eg.png")
            tk.label = tk.Label(root, image=image)
            tk.label.pack()
            ww=500  #logic to middle the tkinter window
            wh=500
            sw=root.winfo_screenwidth()
            sh=root.winfo_screenheight()
            x=sw/2-ww/2
            y=sh/2-wh/2
            root.title(f"{student_name}, please type this sentence")
            root.geometry('%dx%d+%d+%d'%(ww,wh,x,y))
            sentence = random.choice(sentences)#to randomize the list of sentences
            input_text = tk.StringVar()
            start_time = time.time()

            def submit():
                typed_sentence = input_text.get()#to get back the input for checking
                end_time = time.time()
                typing_time = end_time - start_time
                typing_speed = len(typed_sentence) / typing_time #distance/time=speed
                if typed_sentence == sentence:
                     typing_speeds[student_name] = typing_speed
                     root.destroy()
                else:
                    error_label = tk.Label(root, text="Please type the correct sentence!", fg="red")
                    error_label.pack()
                

            tk.Label(root, text=sentence,font=("Arial", 16)).pack()
            e=tk.Entry(root, textvariable=input_text,width=400)#enter key logic
            e.bind("<Return>", submit).pack()
            tk.Button(root, text="Submit", command=submit).pack()
            root.mainloop()

        return typing_speeds
    def store_data(self):
        try:
            pkl_fdr=open("a_pickle","wb")    #function to store results to a pckle file
            pkl.dump(self.typing_speeds,pkl_fdr)     
        except:
            pkl_fdr.close()
    def get_winner(self):
        print(self.typing_speeds)
        pkl_fdr=open("a_pickle","rb")    #function to load back the results from  pickle file
        try:
            while(True):
                temp=pkl.load(pkl_fdr)
                #print(temp)
        except:
            pkl_fdr.close()
        winner = max(temp, key=temp.get)
        return winner, temp[winner]
    
    def visualize_data(self):
        keys = list(self.typing_speeds.keys())   #concept of data visualization
        values = list(self.typing_speeds.values())
        plt.bar(keys, values)
        plt.title("Graphical view of winners")
        plt.xlabel("Names")
        plt.ylabel("Typing speed")
        plt.show()

typing_speed_test = TypingSpeedTest()
typing_speed_test.store_data()
winner, speed = typing_speed_test.get_winner()
typing_speed_test.visualize_data()
p=f"The winner is {winner} with a typing speed of {speed:.2f} characters per second."
root = tk.Tk()
root.title("Winner announcement")
image = tk.PhotoImage(file="winner.png")
tk.label = tk.Label(root, image=image)  #to create a GUI window to declare the winner
tk.label.pack()
tk.Label(root, text=p,height=400,width=400,font=("Arial", 40)).pack()
root.mainloop()

