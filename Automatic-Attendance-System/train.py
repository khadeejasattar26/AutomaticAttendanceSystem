from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector  
import cv2
import os
import numpy as np



class train:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Train data set")

        self.title = Label(self.root, text="TRAIN DATA SET", font=("times new roman", 45, "bold"), bg="light blue", fg="black")
        self.title.place(x=0, y=0, width=1530, height=100)

        img = Image.open("trainingdata.jpeg")
        img = img.resize((300, 300))
        self.photoimg = ImageTk.PhotoImage(img)

        lbl = Label(self.root, image=self.photoimg)
        lbl.place(x=590, y=250, width=300, height=300)
        
        btn=Button(self.root,text="Train Data",command=self.train_classifier,cursor="hand2",bg="light blue",fg="black",width=23,font=("times new roman", 15, "bold"))
        btn.place(x=600,y=570,height=50)

       # btn1=Button(self.root,text="Train Data",command=self.train_classifier,cursor="hand2",font=("times new roman",15,"bold"),width=12,bg="#088F8F",fg="white")  
       # btn1.place(x=0,y=380,width=1530,height=60)



    def train_classifier(self):
        data_dir=("data")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]
        faces=[]
        ids=[]

        for image in path:
            img=Image.open(image).convert('L') #gray scale image
            imageNp=np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==13
        ids=np.array(ids)

       # ===Train classifiwe==
        clf = cv2.face.LBPHFaceRecognizer_create()

        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training datasets completed!")


        

if __name__ == "__main__":
    root = Tk()
    obj = train(root)
    root.mainloop()