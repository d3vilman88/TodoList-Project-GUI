import tkinter
import random


def update_tasks():
    clear_listbox()
    for task in tasks:
        lb_tasks.insert("end", task)


def clear_listbox():
    lb_tasks.delete(0, "end")


def add_task():
    label_dsply["text"] = ""
    Ntask = text_input.get()
    if Ntask != "":
        tasks.append(Ntask)
        update_tasks()
    else:
        label_dsply["text"] = "please enter the text"
    text_input.delete(0, 'end')


def delete_all():
    global tasks
    tasks = []
    update_tasks()


def delete_one():
    de = lb_tasks.get("active")
    if de in tasks:
        tasks.remove(de)
    update_tasks()


def sort_asc():
    tasks.sort()
    update_tasks()


def sort_dsc():
    tasks.sort(reverse=True)
    update_tasks()


def random_task():
    randtask = random.choice(tasks)
    label_dsply["text"] = randtask


def number_task():
    numtask = len(tasks)
    label_dsply["text"] = numtask


def exit_app():
    pass


root = tkinter.Tk()
# change root background col and ect
root.configure(bg="white")
root.title("my to do list")
root.geometry("200x500")
# database
# tasks = []
tasks = ['tes 1', 'best2', 'dest3']


# GUI (graphical user interface)
# main root app


label_title = tkinter.Label(root, text="Todo List", bg="white")
label_title.pack()

label_dsply = tkinter.Label(root, text="", bg="white")
label_dsply.pack()

text_input = tkinter.Entry(root, width=15)
text_input.pack()

# button section
text_add_bttn = tkinter.Button(
    root, text="add todo", bg="white", fg="green", command=add_task)
text_add_bttn.pack()

delone_bttn = tkinter.Button(
    root, text="Delete", bg="white", command=delete_one)
delone_bttn.pack()

delall_bttn = tkinter.Button(
    root, text="Delete all", bg="white", command=delete_all)
delall_bttn.pack()

sort_asc = tkinter.Button(root, text="sort (ASC)",
                          bg="White", command=sort_asc)
sort_asc.pack()

sort_dsc = tkinter.Button(root, text="sort (DSC)",
                          bg="White", command=sort_dsc)
sort_dsc.pack()

random_bttn = tkinter.Button(
    root, text="random task", bg="White", command=random_task)
random_bttn.pack()

number_task = tkinter.Button(
    root, text="Number of Task", bg="white", command=number_task)
number_task.pack()

exit_bttn = tkinter.Button(root, text="exit app",
                           bg="white", command=exit_app)
exit_bttn.pack()

lb_tasks = tkinter.Listbox(root)
lb_tasks.pack()


# main loop
root.mainloop()
