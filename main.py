import tkinter
window = tkinter.Tk()
window.title("Miles to Kilometer Converter")
window.minsize(width=100,height=100)
window.config(padx=50,pady=100)
#
#Label
is_equal_to_label=tkinter.Label(text="My label",font=("Arial","10","bold"))
is_equal_to_label.pack()#centers the text on screen automatically
is_equal_to_label["text"]="is equal to"
is_equal_to_label.grid(column=0,row=1) 

#Entry
entry = tkinter.Entry(width=10)
entry.grid(column=3,row=0)

#Miles  Label
miles_label=tkinter.Label(text="My label",font=("Arial","10","bold"))
miles_label["text"]="Miles"
miles_label.grid(column=4,row=0)

#Calculated Value Label
value_label=tkinter.Label(text="My label",font=("Arial","10","bold"))
value_label["text"]=0
value_label.grid(column=3,row=1)

#Km  Label
Km_label=tkinter.Label(text="My label",font=("Arial","10","bold"))
Km_label["text"]="Km"
Km_label.grid(column=4,row=1)

#Button
def button_clicked():
    if entry.get().isalpha() ==True:
        print("Must be a number.")
    else:
        km = round(float(entry.get()) * 1.60934) #Conversion from Miles to Km
        value_label["text"] = km


button=tkinter.Button(text="Calculate",command=button_clicked)
button.grid(column=3,row=2)

window.mainloop() #keep the screen open;listens to the user
