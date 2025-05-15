import tkinter as tk
import tkinter as tkk
from tkinter import Message ,Text
# from PIL import Image, ImageTk
import pandas as pd       
import tkinter.ttk as ttk
import tkinter.font as font
import tkinter.messagebox as tm
from PIL import Image, ImageTk
import cv2
import firebase_handler as fbh

import tkinter.messagebox as tm

import Detect as dt


bgcolor="#020f12"
bgcolor1="#05d7ff"
fgcolor="#ffffff"
btnTxt="#000000"


def Home():
        print("Started")
        global window
        
        window = tk.Tk()
        window.title("Real Time Coma Patient Monitoring Using Visual Perception System")

 
        window.geometry('1280x720')
        window.configure(background=bgcolor)
        #window.attributes('-fullscreen', True)

        window.grid_rowconfigure(0, weight=1)
        window.grid_columnconfigure(0, weight=1)


        # Frame 1 and 2
        frame1 = tk.Frame(window,bg=bgcolor)
        frame1.pack( pady=30,side="bottom",fill="x")
        

        message1 = tk.Label(window, text="Real Time Coma Patient Monitoring Using Visual Perception System" ,bg=bgcolor  ,fg=fgcolor  ,width=50  ,height=3,font=('times', 30, 'bold')) 
        message1.pack( pady=5,side="top")

        label =tk.Label(window)
        label.pack( pady=5,expand=True)
        cap= cv2.VideoCapture(0)

        # Define function to show frame
        def show_frames():
                # Get the latest frame and convert into Image
                global paused
                global isProcessing
                if not isProcessing:
                        if not paused:
                                ret, frame = cap.read()
                                frame = cv2.flip(frame, 1)
                                cv2image= cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
                                img = Image.fromarray(cv2image)

                                # Convert image to PhotoImage
                                imgtk = ImageTk.PhotoImage(image = img)
                                label.imgtk = imgtk
                                label.configure(image=imgtk)
                        label.after(20, show_frames)

        # Repeat after an interval to capture continiously
        # label.after(20, show_frames)
        
        global started
        started=False
        global paused
        paused=True
        global isProcessing
        isProcessing=False
        def preview():
                global started
                global paused
                global isProcessing
                isProcessing=False
                paused = not paused
                if not started:
                        started=True
                        show_frames()


        # def monitorprocess():
        #         dt.process()


                # frame = cv2.flip(frame, 1)
                # cv2image= cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
                # img = Image.fromarray(cv2image)
                # print("Calling")
                # # Convert image to PhotoImage
                # imgtk = ImageTk.PhotoImage(image = img)
                # label.imgtk = imgtk
                # label.configure(image=imgtk)

                # label.after(20, show_frames)   
                # 
        def monitorprocess():
                # Create a new Tkinter window
                window = tk.Tk()
                window.title("Monitor Process")
                window.geometry("300x150")  # Set window size

                # Function to call `dt.process` with the entered ID
                def on_submit():
                        user_input = entry.get()
                        if user_input.strip():  # Ensure the input is not empty
                                try:
                                        mo_number,partner_name=fbh.fetch_patient_and_spectator_data(str(user_input))
                                        if not mo_number:
                                                tk.messagebox.showwarning("Input Error", "Please enter a valid ID")
                                        else:
                                                window.destroy()
                                                
                                                dt.process(user_input,mo_number,partner_name)

                                except:
                                                tk.messagebox.showwarning("Input Error", "Please enter a valid ID")

                        else:
                                tk.messagebox.showwarning("Input Error", "Please enter a valid ID")


                # Label
                label = tk.Label(window, text="Enter Patient ID:")
                label.pack(pady=10)

                # Input Box
                entry = tk.Entry(window, width=30)
                entry.pack(pady=5)

                # Submit Button
                submit_button = tk.Button(window, text="Submit", command=on_submit)
                submit_button.pack(pady=10)

                # Run the Tkinter event loop
                window.mainloop() 


        def destroyprosses():
                dt.destroyProcess()
                window.destroy()
        
       
                
        browse = tk.Button(frame1, text="Start", command=monitorprocess  ,fg=btnTxt  ,bg=bgcolor1  ,width=26  ,height=2, activebackground = "Red" ,font=('times', 15, ' bold '))
        browse.pack(padx = 10, pady = 10, side = tk.LEFT,expand=True,)

        quitWindow = tk.Button(frame1, text="Quit", command=destroyprosses  ,fg=btnTxt   ,bg=bgcolor1  ,width=26 ,height=2, activebackground = "Red" ,font=('times', 15, ' bold '))
        quitWindow.pack(padx = 10, pady = 10, side = tk.LEFT,expand=True,)

        preview=tk.Button(frame1, text="Preview", command=preview  ,fg=btnTxt   ,bg=bgcolor1  ,width=26 ,height=2, activebackground = "Red" ,font=('times', 15, ' bold '))
        preview.pack(padx = 10, pady = 10, side = tk.LEFT,expand=True,)

          
        window.mainloop()
        
Home()

