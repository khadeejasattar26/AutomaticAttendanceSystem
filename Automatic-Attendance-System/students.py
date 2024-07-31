from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector  
import cv2
import datetime



class Students_Screen:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Students Enrollment")

        
        self.status=False
        # variables
        self.var_name=StringVar()
        self.var_roll_no=StringVar()
        self.var_section=StringVar()
        self.var_gender=StringVar()
        self.var_batch=StringVar()
        self.var_course=StringVar()
        self.var_department=StringVar()
        self.var_dob=StringVar()

        self.canvas = Canvas(self.root, width=1530, height=790)
        self.canvas.pack()

    
        self.canvas.configure(bg="#FAF9F6")

        self.title = Label(self.root, text="Student Enrollment", font=("Poppins", 45, "bold"), bg="#088F8F", fg="white")
        self.title.place(x=0, y=0, width=1530, height=100)

        label1=Label(self.canvas,text="Department",font=("Poppins",12,"bold"),fg="black")
        label1.place(x=200,y=120)
        department = ttk.Combobox(self.canvas,textvariable=self.var_department, font=("Poppins",10), width=17,state="readonly")
        department["values"]=("Select Department","Computer Science","Electrical Eng","BBA")
        department.current(0)
        department.place(x=200, y=150) 

        label2=Label(self.canvas,text="Courses",font=("Poppins",12,"bold"),fg="black")
        label2.place(x=400,y=120)
        courses = ttk.Combobox(self.canvas,textvariable=self.var_course, font=("Poppins",10), width=17,state="readonly")
        courses["values"]=("Select Course","PF","OOP","ICT")
        courses.current(0)
        courses.place(x=400, y=150) 

        label3=Label(self.canvas,text="Batch",font=("Poppins",12,"bold"),fg="black")
        label3.place(x=200,y=220)
        batch = ttk.Combobox(self.canvas,textvariable=self.var_batch, font=("Poppins",10), width=17,state="readonly")
        batch["values"]=("Select Batch","FA21","SP22","FA23","SP23","FA23","SP24")
        batch.current(0)
        batch.place(x=200, y=250) 

        label4=Label(self.canvas,text="Section",font=("Poppins",12,"bold"),fg="black")
        label4.place(x=400,y=220)
        section = ttk.Combobox(self.canvas,textvariable=self.var_section, font=("Poppins",10), width=17,state="readonly")
        section["values"]=("Select Section","A","B","C","D")
        section.current(0)
        section.place(x=400, y=250) 

        # Student Information

        id_label=Label(self.canvas,text="Roll No",font=("Poppins",12,"bold"),fg="black")
        id_label.place(x=200,y=320)

        idText=ttk.Entry(self.canvas,textvariable=self.var_roll_no,width=20,font=("Poppins",13))
        idText.place(x=200,y=350)

        name_label=Label(self.canvas,text="Student Name",font=("Poppins",12,"bold"),fg="black")
        name_label.place(x=500,y=320)

        nameText=ttk.Entry(self.canvas,textvariable=self.var_name,width=20,font=("Poppins",13),)
        nameText.place(x=500,y=350)

        dob_label=Label(self.canvas,text="DOB",font=("Poppins",12,"bold"),fg="black")
        dob_label.place(x=200,y=420)

        dobText=ttk.Entry(self.canvas,textvariable=self.var_dob,width=20,font=("Poppins",13))
        dobText.place(x=200,y=450)
        

        label5=Label(self.canvas,text="Gender",font=("Poppins",12,"bold"),fg="black")
        label5.place(x=500,y=420)
        gender = ttk.Combobox(self.canvas,textvariable=self.var_gender, font=("Poppins",10), width=25,height=28,state="readonly")
        gender["values"]=("Select Gender","Male","Female")
        gender.current(0)
        gender.place(x=500,y=450)


        # Buttons

        savebtn=Button(self.canvas,text="Save",command=self.add_student,font=("Poppins",13,"bold"),width=12,bg="#088F8F",fg="white")  
        savebtn.place(x=535,y=550)

        picbtn=Button(self.canvas,text="Take Picture",command=self.generateDataSet,font=("Poppins",13,"bold"),width=12,bg="#088F8F",fg="white")  
        picbtn.place(x=200,y=550)


        updbtn=Button(self.canvas,text="Update Picture",font=("Poppins",13,"bold"),width=15,bg="#088F8F",fg="white")
        updbtn.place(x=350,y=550)

        clear_fields=Button(self.canvas,text="Clear Fields",command=self.clearFields,font=("Poppins",13,"bold"),width=12,bg="#088F8F",fg="white")
        clear_fields.place(x=685,y=550)
    
    # Functions
    def add_student(self):
        if self.var_department.get()=="Select Department" or self.var_name.get()=="" or self.var_batch.get()=="Select Batch" or self.var_section.get()=="Select Section" or self.var_course.get()=="Select Course" or self.var_roll_no.get()=="" or self.var_dob.get()=="" or self.var_gender.get()=="":
            messagebox.showerror("Error","All Fields are required",parent=self.root)
        elif self.status == True :
            try:
                dbConnection=mysql.connector.connect(host="localhost",port="3307",username="root",password="root",database="Automatic_Attendance")
                cursor=dbConnection.cursor()
                cursor.execute("INSERT INTO Students VALUES(%s,%s,%s,%s,%s,%s,%s,%s)",(self.var_name.get(),self.var_roll_no.get(),self.var_section.get(),self.var_gender.get(),self.var_batch.get(),self.var_course.get(),self.var_department.get(),self.var_dob.get()))
                current_date = datetime.date.today()
                current_time = datetime.datetime.now().time()
                cursor.execute("INSERT INTO Attendance (time, date, status, roll_no, course_name,batch,department,section) VALUES (%s, %s, %s, %s, %s,%s,%s,%s)", (current_time, current_date, "Absent", self.var_roll_no.get(), self.var_course.get(),self.var_batch.get(),self.var_department.get(),self.var_section.get()))
                dbConnection.commit()
                dbConnection.close()

                self.var_name.set("")
                self.var_roll_no.set("")
                self.var_section.set("Select Section")
                self.var_gender.set("Select Gender")
                self.var_batch.set("Select Batch")
                self.var_course.set("Select Course")
                self.var_department.set("Select Department")
                self.var_dob.set("")

                messagebox.showinfo("Success","Student Added Successfully",parent=self.root)
                self.status=False
    
            except Exception as es:
                messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)
        else : 
            messagebox.showwarning("Caution","Please take photo samples first")
       
       
    def clearFields(self):
            if self.var_department.get()=="Select Department" and self.var_name.get()=="" and self.var_batch.get()=="Select Batch" and self.var_section.get()=="Select Section" and self.var_course.get()=="Select Course" and self.var_roll_no.get()=="" and self.var_dob.get()=="" and self.var_gender.get()=="Select Gender":
              messagebox.showinfo("Error","All Fields are already cleared",parent=self.root)
            else :
                self.var_name.set("")
                self.var_roll_no.set("")
                self.var_section.set("Select Section")
                self.var_gender.set("Select Gender")
                self.var_batch.set("Select Batch")
                self.var_course.set("Select Course")
                self.var_department.set("Select Department")
                self.var_dob.set("")
       
       
        # add student icon

        # img=Image.open("add-user.png")
        # img = img.resize((150, 150))  # Resize the img
        # self.icon = ImageTk.PhotoImage(img)  # Convert the img to Tkinter PhotoImage
        # add_student_icon = Label(self.canvas, image=self.icon)
        # add_student_icon.place(x=1000, y=150)
    def generateDataSet(self):
        if self.var_department.get()=="Select Department" or self.var_name.get()=="" or self.var_batch.get()=="Select Batch" or self.var_section.get()=="Select Section" or self.var_course.get()=="Select Course" or self.var_roll_no.get()=="" or self.var_dob.get()=="" or self.var_gender.get()=="":
            messagebox.showerror("Error","First fill out all the fields then take picture",parent=self.root)
        else:
            try:
                
                #=====load data on face frontals from cv======
                
                face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_cropped(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2BGRA)
                    faces=face_classifier.detectMultiScale(gray,1.3,5)

                    for(x,y,w,h) in faces:
                        face_cropped=img[y:y+h,x:x+w]
                        return face_cropped

                cap=cv2.VideoCapture(0)
                img_id=0
                while True:
                    ret,my_frame=cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id+=1
                        face=cv2.resize(face_cropped(my_frame),(450,450))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2BGRA)
                        file_name_path="data/user."+str(self.var_roll_no.get())+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("Cropped Face",face)
                        if cv2.waitKey(1)==13 or int(img_id)==100:
                            break
                cap.release()    
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating Dataset Completed!")
                self.status=True
            
            except Exception as es:
                messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)



    

        






if __name__ == "__main__":
    root = Tk()
    obj = Students_Screen(root)
    root.mainloop()