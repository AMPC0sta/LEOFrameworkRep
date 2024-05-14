from tkinter import *
from tkinter import filedialog

# to be used in event management (undefined events)
def do_nothing():
    pass


# create frames with labels
def create_frame(root, row, column, rowspan=1, columnspan=1, title=None):
    frame = Frame(root, bg="white", bd=1, relief=RAISED)
    frame.grid(row=row, column=column, rowspan=rowspan, columnspan=columnspan, sticky="nsew")
    
    # Add a label as the title
    if title:
        label = Label(frame, text=title, fg="black", font=("Arial", 12, "bold"))
        label.pack(padx=10, pady=5)  # Adjust padding as needed
    
    return frame

def open_tle_file_dialog():
    file_path = filedialog.askopenfilename(title="Select a file", filetypes=(("tle files", "*.tle"),("TLE files", "*.TLE"),("All files", "*.*")))
    if file_path:
        print("Selected file:", file_path)
        # Add your code to handle the selected file here


screen = Tk(className=' Low Earth Orbit Calculator')
screen.geometry('1600x800')

top_menu_bar = Menu(screen)

file_group = Menu(top_menu_bar,tearoff=0)
file_group.add_command(label='New',command=do_nothing)
file_group.add_command(label='Open',command=do_nothing)
file_group.add_command(label='Save',command=do_nothing)
file_group.add_command(label='Save As',command=do_nothing)
file_group.add_command(label='Close',command=do_nothing)
file_group.add_separator()
file_group.add_command(label='Exit',command=screen.quit)
top_menu_bar.add_cascade(label='Project',menu=file_group)


prop_group = Menu(top_menu_bar,tearoff=0)
prop_group.add_command(label='PyOrbital',command=do_nothing)
prop_group.add_command(label='SGP4',command=do_nothing)
prop_group.add_separator()
prop_group.add_command(label='Custom',command=do_nothing)
top_menu_bar.add_cascade(label='Propagators',menu=prop_group)

o_elem_group = Menu(top_menu_bar,tearoff=0)
o_elem_group.add_command(label='Keplerian Elements')
o_elem_group.add_command(label='Load TLE',command=open_tle_file_dialog)
top_menu_bar.add_cascade(label='Orbiting Object',menu=o_elem_group)


gen_group = Menu(top_menu_bar,tearoff=0)
gen_group.add_command(label='List of Points')
top_menu_bar.add_cascade(label='Calculate',menu=gen_group)

custom_group = Menu(top_menu_bar,tearoff=0)
custom_group.add_command(label='New',command=do_nothing)
custom_group.add_command(label='Open',command=do_nothing)
custom_group.add_command(label='Save',command=do_nothing)
custom_group.add_command(label='Save As',command=do_nothing)
custom_group.add_command(label='Close Model',command=do_nothing)
top_menu_bar.add_cascade(label='Custom Models',menu=custom_group)



# Split screens horizontally
screen.grid_rowconfigure(0,weight=1)
screen.grid_rowconfigure(1,weight=3)
screen.grid_columnconfigure(0, weight=1)

frame_top = create_frame(screen,0,0,title='Operative Sequence')
frame_under = create_frame(screen,1,0)


# Split bottom area vertically into 3 areas
frame_under.grid_columnconfigure(0,weight=1)
frame_under.grid_columnconfigure(1,weight=2)
frame_under.grid_columnconfigure(2,weight=2)
frame_under.grid_rowconfigure(0,weight=1)

frame_under_left = create_frame(frame_under,0,0,title='Project Information')
frame_under_left = create_frame(frame_under,0,1,title='Satellite Parameters')
frame_under_left = create_frame(frame_under,0,2,title='Propagator Parameters')

screen.config(menu=top_menu_bar)
screen.mainloop()

