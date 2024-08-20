import segno
from ttkbootstrap import *
from PIL import Image, ImageTk

# QR Code Layout Class
class QRCodeApp:
    def __init__(self):
        #Root Window
        self.root = Window(themename="vapor")
        self.root.geometry("800x500")
        self.root.title("QRCode!")

        #Entry
        self.Entry = Entry(self.root, font=("Trebuchet MS", 18))
        self.Entry.place(relx = 0.4, rely = 0.65, anchor = "center")
        self.Entry.insert(0, "QR Code Info")
        my = Style()
        my.configure("default.TButton", font=("Trebuchet MS", 18))
        #Button
        self.Button = Button(self.root, style="default.TButton", width = 5, text = "OK")
        self.Button.place(relx = 0.72, rely = 0.65, anchor = "center")
        #Label with Image
        self.Label = Label(self.root)
        self.Label.place(relx=0.5, rely=0.3, anchor="center")
        self.image: None = None

    # Show self.root
    def run(self):
        self.root.mainloop()

#Instance of the QR Code
QR = QRCodeApp()

# Function for chaning self.Label's Image
def Make_QR(Operate: QRCodeApp = QR):
        Q4R = segno.make_qr(Operate.Entry.get(), version=5) #Create it
        Q4R.save(f"QR.png") #Save it
        I1 = Image.open(f"QR.png").resize((200, 200))
        #Saving it to self.image
        Operate.image = ImageTk.PhotoImage(I1)
        Operate.Label.configure(image=Operate.image)

#Changing Self.Button Function
QR.Button.configure(command=Make_QR)

if __name__ == '__main__':
    QR.run()
