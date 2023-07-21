# -*- coding: utf-8 -*-
"""
Created on Sat Jan  2 19:27:52 2021

@author: Chirag Kumar, Megha Khangarot, Mohak Goyal
"""

#importing of all modules needed
import tkinter
import tkinter as tk
from tkinter import *
from tkinter import messagebox
import tkinter.font as font
from tkinter import messagebox
from PIL import Image, ImageTk
from playsound import playsound
from statemachine import StateMachine, State

#defination of statemachine class
class HomeSecuritySystem(StateMachine):
    sysTurnedOff = State('System Turned Off', initial=True)
    sysTurnedOn = State('System Turned On')
    passChecked = State('Passcode Checked')
    locked = State('Door Locked')
    unlocked = State('Door Unlocked')
            
    turnOn = sysTurnedOff.to(sysTurnedOn)
    checkCode = sysTurnedOn.to(passChecked)
    codeMatched = passChecked.to(unlocked)
    codeNotMatched = passChecked.to(locked)
    sysOff1 = unlocked.to(sysTurnedOff)
    sysOff2 = locked.to(sysTurnedOff)

securitySystem = HomeSecuritySystem()

#Using the TK() class
main_window = Tk()

main_window.geometry("300x400")
main_window.resizable(False,False)
main_window.title("Home Security System")

#creating image label
image1 = Image.open(r"./Camera.png")
camera = ImageTk.PhotoImage(image1)

label1 = Label(main_window, image=camera)
label1.image = camera
label1.place(x=50, y=8)

#created function for later use
def message_box():
    message_window = Tk()
    message_window.geometry("250x100")
    message_window.title("Error")
    error = Label(message_window, text="Please use the keypad provided!!", fg = "red", font = ("Times New Roman", 12))
    error.place(x = 20, y = 30)
    
    message_window.mainloop()

#command for press button
def press_action():
    # playsound(r'./Beep Sound1.mp3')
    
    #state changed for the first time
    securitySystem.run('turnOn')
    print(securitySystem.current_state)

    #using the same class Tk() for creating another window
    keypad = Tk()
    keypad.geometry("300x320")
    keypad.resizable(False, False)
    keypad.title("Enter Code")
    
    #command for button1 in keypad window
    def button1_action():
        # playsound(r'./Beep Sound1.mp3')
        try:
            code = int(code_text.get())
            code_text.delete(0, END)
            number = (code*10)+1
            code_text.insert(tk.END, number)
        except:
            code_text.insert(tk.END, 1)
     
    #command for button2 in keypad window
    def button2_action():
        # playsound(r'./Beep Sound1.mp3')
        try:
            code = int(code_text.get())
            code_text.delete(0, END)
            number = (code*10)+2
            code_text.insert(tk.END, number)
        except:
            code_text.insert(tk.END, 2)
                    
    #command for button3 in keypad window
    def button3_action():
        # playsound(r'./Beep Sound1.mp3')
        try:
            code = int(code_text.get())
            code_text.delete(0, END)
            number = (code*10)+3
            code_text.insert(tk.END, number)
        except:
            code_text.insert(tk.END, 3)

    #command for button4 in keypad window
    def button4_action():
        # playsound(r'./Beep Sound1.mp3')
        try:
            code = int(code_text.get())
            code_text.delete(0, END)
            number = (code*10)+4
            code_text.insert(tk.END, number)
        except:
            code_text.insert(tk.END, 4)

    #command for button5 in keypad window
    def button5_action():
        # playsound(r'./Beep Sound1.mp3')
        try:
            code = int(code_text.get())
            code_text.delete(0, END)
            number = (code*10)+5
            code_text.insert(tk.END, number)
        except:
            code_text.insert(tk.END, 5)

    #command for button6 in keypad window
    def button6_action():
        # playsound(r'./Beep Sound1.mp3')
        try:
            code = int(code_text.get())
            code_text.delete(0, END)
            number = (code*10)+6
            code_text.insert(tk.END, number)
        except:
            code_text.insert(tk.END, 6)

    #command for button7 in keypad window
    def button7_action():
        # playsound(r'./Beep Sound1.mp3')
        try:
            code = int(code_text.get())
            code_text.delete(0, END)
            number = (code*10)+7
            code_text.insert(tk.END, number)
        except:
            code_text.insert(tk.END, 7)

    #command for button8 in keypad window
    def button8_action():
        # playsound(r'./Beep Sound1.mp3')
        try:
            code = int(code_text.get())
            code_text.delete(0, END)
            number = (code*10)+8
            code_text.insert(tk.END, number)
        except:
            code_text.insert(tk.END, 8)

    #command for button9 in keypad window
    def button9_action():
        # playsound(r'./Beep Sound1.mp3')
        try:
            code = int(code_text.get())
            code_text.delete(0, END)
            number = (code*10)+9
            code_text.insert(tk.END, number)
        except:
            code_text.insert(tk.END, 9)

    #command for button0 in keypad window
    def button0_action():
        # playsound(r'./Beep Sound1.mp3')
        try:
            code = int(code_text.get())
            code_text.delete(0, END)
            number = (code*10)+0
            code_text.insert(tk.END, number)
        except:
            code_text.insert(tk.END, 0)

    #command for reset button in keypad window
    def reset_action():
        # playsound(r'./Beep Sound1.mp3')
        code_text.delete(0, END)

    #command for submit button in keypad window
    def submit_action():
        # playsound(r'./Beep Sound1.mp3')
        
        #changing state 2nd time
        securitySystem.run('checkCode')
        print(securitySystem.current_state)
        
        #to get the code entered in int form and remove all the errors
        try:
            x = int(code_text.get())
        except:
            #using the function created above
            message_box()
        
        #condition for checking the input
        if(x==8921):
            
            #changing state 3rd time
            securitySystem.run('codeMatched')
            print(securitySystem.current_state)
            
            #using the class Tk() for crating new window            
            result_window = Tk()
    
            result_window.geometry("300x400")
            result_window.resizable(False,False)
            result_window.title("Home Security System")
            
            #creating labels to place in resullt winodw
            image1 = Image.open(r"./CAMERA.png") 
            camera = ImageTk.PhotoImage(image1)
                
            label1 = Label(result_window, image=camera)
            label1.image = camera
            label1.place(x=50, y=8)
                
            result = Label(result_window, text = "Access Granted", fg = "white", bg = 'green')
            result.configure(font=("Bookman Old Style", 20))
            result.place(x = 50, y = 275)
            
            #closing of keypad and opening another window
            keypad.destroy()
            result_window.mainloop()
            
            #changing state for 4th time and resetting state
            securitySystem.run('sysOff1')
            print(securitySystem.current_state)
        else:
            
            #changing state 3rd time
            securitySystem.run('codeNotMatched')
            print(securitySystem.current_state)
            
            #using the class Tk() for crating new window            
            result_window = Tk()
    
            result_window.geometry("300x400")
            result_window.resizable(False,False)
            result_window.title("Home Security System")
                
            #creating labels to place in resullt winodw
            image1 = Image.open(r"./CAMERA.png") 
            camera = ImageTk.PhotoImage(image1)
            
            label1 = Label(result_window, image=camera)
            label1.image = camera
            label1.place(x=50, y=8)
            
            result = Label(result_window, text = "Access Denied", fg = "white", bg = 'red')
            result.configure(font=("Bookman Old Style", 20))
            result.place(x = 50, y = 275)
            
            #closing keypad window and opening another window
            keypad.destroy()
            result_window.mainloop()
            
            #if above condition fails then this condition will run and state will change here 4th time aand resetting state here
            securitySystem.run('sysOff2')
            print(securitySystem.current_state)
        

#creation and placing of all the labels, buttons and entry widgets
    label2 = Label(keypad, text = "Enter the code to enter:")
    label2.place(x = 20, y = 20)
    
    code_text = Entry(keypad, show = "*", font = ('Times New Roman',18))
    code_text.place(x = 28, y = 50)
    code_text.insert(tk.END, "")
    
    button1 = Button(keypad, text = "1", height = 2, width = 9, command = button1_action)
    button1.place(x = 23, y = 110)
    
    button2 = Button(keypad, text = "2", height = 2, width = 9, command = button2_action)
    button2.place(x = 113, y = 110)
    
    button3 = Button(keypad, text = "3", height = 2, width = 9, command = button3_action)
    button3.place(x = 203, y = 110)

    button4 = Button(keypad, text = "4", height = 2, width = 9, command = button4_action)
    button4.place(x = 23, y = 160)

    button5 = Button(keypad, text = "5", height = 2, width = 9, command = button5_action)
    button5.place(x = 113, y = 160)

    button6 = Button(keypad, text = "6", height = 2, width = 9, command = button6_action)
    button6.place(x = 203, y = 160)

    button7 = Button(keypad, text = "7", height = 2, width = 9, command = button7_action)
    button7.place(x = 23, y = 210)

    button8 = Button(keypad, text = "8", height = 2, width = 9, command = button8_action)
    button8.place(x = 113, y = 210)

    button9 = Button(keypad, text = "9", height = 2, width = 9, command = button9_action)
    button9.place(x = 203, y = 210)
    
    reset = Button(keypad, text = "Reset", height = 2, width = 9, command = reset_action)
    reset.place(x = 23, y = 260)
    
    button0 = Button(keypad, text = "0", height = 2, width = 9, command = button0_action)
    button0.place(x = 113, y = 260)

    submit = Button(keypad, text = "Submit", height = 2, width = 9, command = submit_action)
    submit.place(x = 203, y = 260)

#closing main window and opening next window
    main_window.destroy()
    keypad.mainloop()
    
press_button = Button(main_window, text = "Press", command = press_action)
press_button.configure(font=("Bookman Old Style", 20))
press_button.place(x = 100, y = 275)

#printing the current state at initial state
print(securitySystem.current_state)

mainloop()
