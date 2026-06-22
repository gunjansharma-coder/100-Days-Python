from tkinter import *

window= Tk()
window.title("Miles to Kilometer Converter")

#Entry
input_entry=Entry()
input_entry.grid(column=1,row=0)

#Label=Miles
label=Label(text="Miles")
label.grid(column=2,row=0)

#Label 2= is equal to
label_2=Label(text="is equal to")
label_2.grid(column=0,row=1)

#Label 3 = value of km
result=Label(text="0")
result.grid(column=1,row=1)

#Label 4 = km
km=Label(text="km")
km.grid(column=2,row=1)


def calculate_km():
    user_input= float(input_entry.get())
    value=round((user_input*1.6),2)

    result.config(text=value)
#Button
button=Button(text="Calculate",command=calculate_km)
button.grid(column=1,row=2)
window.mainloop()