from tkinter import *
from PIL import Image, ImageTk
import cv2
import mysql.connector
import datetime
class FaceRecognition:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition")

        self.title = Label(self.root, text="Face Recognition", font=("Poppins", 45, "bold"), bg="light blue", fg="black")
        self.title.place(x=0, y=0, width=1530, height=100)


        img = Image.open("face-id.png")
        img = img.resize((300, 300))
        self.photoimg = ImageTk.PhotoImage(img)

        lbl = Label(self.root, image=self.photoimg)
        lbl.place(x=590, y=250, width=300, height=300)
        
        btn=Button(self.root,text="Face Recognizer",command=self.faceRecognition,cursor="hand2",bg="light blue",fg="black",width=23,font=("times new roman", 15, "bold"))
        btn.place(x=590,y=570,height=50)

    def faceRecognition(self):
        dbConnection = mysql.connector.connect(host="localhost", port="3307", username="root", password="root", database="Automatic_Attendance")
        cursor = dbConnection.cursor()
        def draw_boundary(img, classifier, scaleFactor, minNeighbours, color, text, clf):
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray, scaleFactor, minNeighbours)

            for (x, y, w, h) in features:
                cv2.rectangle(img, (x, y), (x + w, y + h), color, 3)
                gray_face = gray[y:y + h, x:x + w]
                id, predict = clf.predict(gray_face)
                confidence = int((100 * (1 - predict / 300)))
               

                cursor.execute("select name from Students Where roll_no=" + str(id))
                n=cursor.fetchone()
                if n is not None:
                   n = "+".join(n)
                else:
                    n = "Unknown"

                cursor.execute("select roll_no from Students Where roll_no=" + str(id))
                r = cursor.fetchone()
                if r is not None:
                    r = "+".join(r)
                else:
                    r = "Unknown"


                if confidence > 80:
                    current_date = datetime.date.today()
                    current_time = datetime.datetime.now().time()
                    status="Present"
                    
                    cv2.putText(img, f"Roll: {r}", (x, y - 55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img, f"Name: {n}", (x, y - 30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                
                    cursor.execute("UPDATE Attendance SET status = %s , time= %s, date = %s WHERE roll_no = %s", (status,current_time,current_date,str(id)))
                    # print("Recognized face ID:", id)  

                else:
                    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)
                    cv2.putText(img, "Student not enrolled", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    
       
        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")
        video_cap = cv2.VideoCapture(0)

        while True:
            ret, img = video_cap.read()
            draw_boundary(img, faceCascade, 1.1, 10, (255, 25, 255), "Face", clf)
            cv2.imshow("Welcome to Face Recognition", img)

            if cv2.waitKey(1) == 13:
                break  
        dbConnection.commit()  
        print(cursor.rowcount, "record(s) affected")       
        video_cap.release()
        cv2.destroyAllWindows()
    

if __name__ == "__main__":
    root = Tk()
    obj = FaceRecognition(root)
    root.mainloop()