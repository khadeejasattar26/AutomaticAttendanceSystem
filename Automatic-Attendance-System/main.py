from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from students import Students_Screen
from train import train
from face_recognition import FaceRecognition
from attedance import Attendance_Screen

import os



class Face_Recognition_System:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("FACE RECOGNITION SYSTEM")

        img = Image.open(r"AMS.jpeg")
        img = img.resize((1530, 790))  # Resize the image to fit window
        self.photoimg = ImageTk.PhotoImage(img)

        bg_img = Label(self.root, image=self.photoimg)
        bg_img.place(x=0, y=0, relwidth=1, relheight=1)

        title_lbl=Label(self.root, text="FACE RECOGNITION ATTENDANCE SYSTEM", font=("times new roman", 35, "bold"), bg="light blue", fg="black")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        #student button
        img = Image.open(r"student.jpg")
        img = img.resize((220, 220))  # Resize the image to fit window
        self.photoimg = ImageTk.PhotoImage(img)

        b1= Button(bg_img,image=self.photoimg,command=self.student_details,cursor="hand2")
        b1.place(x=200,y=100,width=220,height=220) 

        
        b1= Button(bg_img,text="Student Details",command=self.student_details,cursor="hand2",font=("times new roman", 15, "bold"), bg="light blue", fg="black")
        b1.place(x=200,y=300,width=220,height=40) 


        
         #Detect Face button
        img2 = Image.open(r"faceDetect.jpg")
        img2 = img2.resize((220, 220))  # Resize the image to fit window
        self.photoimg2 = ImageTk.PhotoImage(img2)

        b1= Button(bg_img,image=self.photoimg2,command=self.faceRecognitionScreen,cursor="hand2")
        b1.place(x=500,y=100,width=220,height=220) 

        
        b1= Button(bg_img,text="Face Detector",command=self.faceRecognitionScreen,cursor="hand2",font=("times new roman", 15, "bold"), bg="light blue", fg="black")
        b1.place(x=500,y=300,width=220,height=40) 


        #Attendance button
        img3 = Image.open(r"attendance.png")
        img3 = img3.resize((220, 220))  # Resize the image to fit window
        self.photoimg3 = ImageTk.PhotoImage(img3)

        b1= Button(bg_img,image=self.photoimg3,command=self.Attendance_details,cursor="hand2")
        b1.place(x=800,y=100,width=220,height=220) 

        
        b1= Button(bg_img,text="Attendance",command=self.Attendance_details,cursor="hand2",font=("times new roman", 15, "bold"), bg="light blue", fg="black")
        b1.place(x=800,y=300,width=220,height=40) 


         #help button
        img4 = Image.open(r"help.png")
        img4 = img4.resize((220, 220))  # Resize the image to fit window
        self.photoimg4 = ImageTk.PhotoImage(img4)

        b1= Button(bg_img,image=self.photoimg4,cursor="hand2")
        b1.place(x=1100,y=100,width=220,height=220) 

        
        b1= Button(bg_img,text="Help Desk",cursor="hand2",font=("times new roman", 15, "bold"), bg="light blue", fg="black")
        b1.place(x=1100,y=300,width=220,height=40)


         #Train button
        img5 = Image.open(r"trainData.png")
        img5 = img5.resize((220, 220))  # Resize the image to fit window
        self.photoimg5 = ImageTk.PhotoImage(img5)

        b1= Button(bg_img,image=self.photoimg5,command=self.trainData,cursor="hand2")
        b1.place(x=200,y=380,width=220,height=220) 

        
        b1= Button(bg_img,text="Train Data",command=self.trainData,cursor="hand2",font=("times new roman", 15, "bold"), bg="light blue", fg="black")
        b1.place(x=200,y=580,width=220,height=40) 


        #Photos button
        img6 = Image.open(r"photos.png")
        img6 = img6.resize((220, 220))  # Resize the image to fit window
        self.photoimg6 = ImageTk.PhotoImage(img6)

        b1= Button(bg_img,image=self.photoimg6,cursor="hand2",command=self.open_img)
        b1.place(x=500,y=380,width=220,height=220) 

        
        b1= Button(bg_img,text="Photos",command=self.open_img,cursor="hand2",font=("times new roman", 15, "bold"), bg="light blue", fg="black")
        b1.place(x=500,y=580,width=220,height=40) 


        #Developer button
        img7 = Image.open(r"developer.jpg")
        img7 = img7.resize((220, 220))  # Resize the image to fit window
        self.photoimg7 = ImageTk.PhotoImage(img7)

        b1= Button(bg_img,image=self.photoimg7,cursor="hand2")
        b1.place(x=800,y=380,width=220,height=220) 

        
        b1= Button(bg_img,text="Developer",cursor="hand2",font=("times new roman", 15, "bold"), bg="light blue", fg="black")
        b1.place(x=800,y=580,width=220,height=40) 


         #Exit button
        img8 = Image.open(r"exit.jpg")
        img8 = img8.resize((220, 220))  # Resize the image to fit window
        self.photoimg8 = ImageTk.PhotoImage(img8)

        b1= Button(bg_img,image=self.photoimg8,cursor="hand2")
        b1.place(x=1100,y=380,width=220,height=220) 

        
        b1= Button(bg_img,text="Exit",cursor="hand2",font=("times new roman", 15, "bold"), bg="light blue", fg="black")
        b1.place(x=1100,y=580,width=220,height=40) 



    def open_img(self):
          os.startfile("data")


# function buttons
    def student_details(self):
        self.new_windwow=Toplevel(self.root)
        self.app=Students_Screen(self.new_windwow)


    def Attendance_details(self):
        self.new_windwow=Toplevel(self.root)
        self.app=Attendance_Screen(self.new_windwow)

    def trainData(self):
        self.new_windwow=Toplevel(self.root)
        self.app=train(self.new_windwow)

    def faceRecognitionScreen(self):
        self.new_windwow=Toplevel(self.root)
        self.app=FaceRecognition(self.new_windwow)




if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition_System(root)
    root.mainloop()

 

