from tkinter import *
import tkinter.messagebox as tmsg
from tkinter. filedialog import askopenfilename, asksaveasfilename
import os

def newFile():
   global file
   root.title("Untitle -- Editor")
   file= None
   TextArea.delete(1.0, END)

   
def openFile():
    global file
    file= askopenfilename(defaultextension=".txt",
     filetypes=[("All files","*.*"),
                ("Text Documents","*.txt")

    ])

    if file =="":
        file = None
    else:
        root.title(os.path.basename(file)+ "-- Editor")
        TextArea.delete(1.0, END)
        f = open(file, "r")
        TextArea.insert(1.0, f.read())
        f.close()



def saveFile():
    global file
    if file==None:
        file= asksaveasfilename(initialfile='Untitled.txt',
                                defaultextension=".txt",
                                filetypes=[("All files","*.*"),
                                       ("Text Documents","*.txt")])
        if file =="":
            file = None
        else:
            # Save as a new file
            f= open(file,"w")
            f.write(TextArea.get(1.0, END))
            f.close()
            root.title(os.path.basename(file)+"-- Editor")
            tmsg.showinfo("Alert!","File is saved successfully!")
    else:
        # Save the file
        f= open(file,"w")
        f.write(TextArea.get(1.0, END))
        f.close()


def quitApp():
    root.destroy()

# -------------------------------------------

def cut():
    TextArea.event_generate(("<<Cut>>"))


def copy():
    TextArea.event_generate(("<<Copy>>"))

def paste():
    TextArea.event_generate(("<<Paste>>"))

def about():
    tmsg.showinfo("About","This GUI is Made by BonggoHriday")



if __name__ =='__main__':
    # Basic code of tkinter
    root = Tk()
    root.title("Text Editor By Code With BonggoHriday")
    #  icons
    # root.wm_iconbitmap("logo.ico")

    root.geometry("644x500")


    #ADD TEXT AREA
    TextArea = Text(root, font="lucida 15", padx=10, pady=10)
    file = None
    TextArea.pack(expand=True, fill=BOTH)


    # ADDING SCROLL BAR ON TEXT AREA
    scroll = Scrollbar(TextArea)
    scroll.pack(side=RIGHT, fill=Y)
    scroll.config(command=TextArea.yview)
    TextArea.config(yscrollcommand=scroll.set)



    # LET'S CRETAE THE MENUBAR
    MenuBar=  Menu(root)

    # FILE MENUE STARTS
    # -------------------------------------------------
    FileMenue =  Menu(MenuBar, tearoff=0)

    # TO OPEN NEW FILE
    FileMenue.add_command(label="New", command=newFile)

    # TO OPEN ALREADY EXISTING FILE
    FileMenue.add_command(label="Open", command=openFile)

    # TO SAVE THE FILE
    FileMenue.add_command(label="Save", command=saveFile)
    FileMenue.add_separator()
    FileMenue.add_command(label="Exit", command=quitApp)
    MenuBar.add_cascade(label="File", menu =FileMenue)
    # ---------------------------------------------------
    # FILE MENUE ENDS

    # EDIT MENUE STARTS
    # -------------------------------------------------
    EditMenue = Menu(MenuBar, tearoff=0)

    # To give the features of cut, copy and paste
    EditMenue.add_command(label="Cut", command=cut)
    EditMenue.add_command(label="Copy", command=copy)
    EditMenue.add_command(label="Paste", command=paste)
    MenuBar.add_cascade(label="Edit", menu=EditMenue)
    # ---------------------------------------------------
    # EDIT MENUE ENDS

    # HELP MENUE STARTS
    # -------------------------------------------------
    HelpMenue = Menu(MenuBar, tearoff=0)
    HelpMenue.add_command(label="About", command=about)
    MenuBar.add_cascade(label="Help", menu=HelpMenue)

    # ---------------------------------------------------
    # HELP MENUE ENDS




    

    root.config(menu=MenuBar)





    root.mainloop()
