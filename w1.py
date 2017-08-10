from tkinter import *
from tkinter import ttk

class HelloApp:

    def __init__(self, master):

        self.label = ttk.Label(master, text = "User Name:")
        self.label.place(x = 0, y = 0)

        self.label = ttk.Label(master, text = "Password:")
        self.label.place(x = 0, y = 45)

        self.label = Text(master, height=1, width=15)
        self.label.place(x=2, y=20)
        self.label.insert(END,"User Name")

        self.label = Text(master, height=1, width=15)
        self.label.place(x=2, y=65)
        self.label.insert(END,"Password")

        self.button = ttk.Button(master, text = "Login")
        self.button.place(x = 21, y = 89)

        def testVal(self,i,master):
            ind=int(i)
            if master == '1': #insert
                if not self[ind].isdigit():
                    return False
            return True

        #ttk.Button(master, text = "Hawaii",
         #          command = self.hawaii_hello).grid(row = 1, column = 1)

     #def login(self):
     #   self.label.config(text= 'a')

    #def hawaii_hello(self):
     #   self.label.config(text = 'Aloha, Tkinter!')

            
def main():            
    
    root = Tk()
    app = HelloApp(root)
    entry = Entry(root, validate="key")
    entry['validatecommand'] = (entry.register(testVal),'%P','%i','%d')
    entry.pack()
    #T = Text(root, height=1, width=15)
    #p=T.pack()
    #app1= HelloApp(p)
    #T.insert(END,"User Name")
    root.mainloop()
    
if __name__ == "__main__": main()
