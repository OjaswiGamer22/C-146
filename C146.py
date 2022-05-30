from tkinter import *
root=Tk()
root.title("Fibonacci Series")
root.geometry("500x500")
input_no=Entry(root)
input_no.pack()
label1= Label(root,text="Fibonacci series")
label1.pack()
label2=Label(root,text="Fibonacci Sum")
label2.pack()
def showfibonacci():
    input_value=int(input_no.get())
    num1=0
    num2=1
    sum1=0
    sum2=0
    counter=1
    while(counter <=input_value):
        label1["text"]+=str(sum1)+" "
        label2["text"]=str(sum2)
        counter=counter+1
        num1=num2
        num2=sum1
        sum1=num1+num2
        sum2=sum2+sum1
button1=Button(root,text="Show Fibonacci", command=showfibonacci,bg="blue",fg="white")
button1.pack()
root.mainloop()


