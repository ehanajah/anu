from tkinter import *

morse = ["._", "_...", "_._.", "_..", ".", ".._.", "__.", "....", "..", ".___", "_._", "._..", "__", "_.", "___", ".__.", "__._", "._.", "...", "_", ".._", "..._", ".__", "_.._", "_.__", "__..", ".____", "..___", "...__", "...._", ".....", "_....", "__...", "___..", "____.", "_____"]
huruf = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

root = Tk()
root.title("Penerjemah Sandi Morse")
root.geometry("400x152")

nwframe = LabelFrame(root, text="Penerjemah Sandi Morse", padx=10, pady=10)
nwframe.place(x=15, y=10 )

samde = Label(nwframe, text="=").grid(row = 1,column=1)

e1 = Entry(nwframe, width=26)
e2 = Entry(nwframe, width=26)
e1.grid(row=1, column=0)
e2.grid(row=1, column=2)

def translate(ts):
    e2.delete(0,END)
    
    kotaksatu = cliked.get()
    kotakdua = cliked2.get()
    a = e1.get()      

    if kotaksatu == "Alfabet" and kotakdua == "Morse":
        b = list(a)
        c = []
        for i in range (len(b)):
            for j in range (len(huruf)):
                if b[i] == huruf[j]:
                    c.append(morse[j])

        hasil = " ".join(c)
    elif kotaksatu == "Morse" and kotakdua == "Alfabet":
        b = a.split(' ')
        c = []
        for i in range (len(b)):
            for j in range (len(morse)):
                if b[i] == morse[j]:
                    c.append(huruf[j])

        hasil = "".join(c)
    elif kotaksatu == "Alfabet" and kotakdua == "Alfabet":
        b = list(a)
        c = []
        for i in range (len(b)):
            for j in range (len(huruf)):
                if b[i] == huruf[j]:
                    c.append(huruf[j])

        hasil = "".join(c)
    elif kotaksatu == "Morse" and kotakdua == "Morse":
        b = a.split(' ')
        c = []
        for i in range (len(b)):
            for j in range (len(morse)):
                if b[i] == morse[j]:
                    c.append(morse[j])

        hasil = " ".join(c)

    e2.insert(0, hasil)
    




option = ["Alfabet","Morse"]
cliked = StringVar()
cliked.set(option[0])
drop = OptionMenu(nwframe,cliked,*option,command=translate)
drop.config(width=20)
drop.grid(row=2, column=0)

cliked2 = StringVar()
cliked2.set(option[1])
drop2 = OptionMenu(nwframe,cliked2,*option,command=translate)
drop2.config(width=20)
drop2.grid(row=2, column=2)

ket = Label(nwframe, text="*jika sandi lebih dari satu \nketikkan spasi di antara sandi")
btn = Button(nwframe,text="terjemahkan",command=lambda:translate("terjemahkan"))
ket.grid(row=3, column=0)
btn.grid(row=3, column=2)



root.mainloop()