from tkinter import *
from tkinter import filedialog, messagebox
from tkinter.font import Font
from  tkcalendar import *

from missionPhaseParameters import *


button_ptr=0            #create phase buttons auxiliary counter
button_index=0          #clicked button index
operations = []         #buttons array
mission = []

screen = Tk(className=' Low Earth Orbit Calculator')
screen.geometry('1600x800')

#if phase button is pressed
def trigger_op_button_one_click(event):
    pass

#if phase button is double pressed
def trigger_op_button_double_click(event):
    global operations,mission
    global button_index
    
    button_index = operations.index(event.widget)
    open_input_operation_parameters_form()


#creating phase buttons
def insert_mission_ops_button():
    global button_ptr
    global operations,mission   
    
    bold_font = Font(family="Helvetica", size=10, weight="bold")
    
    #creating button
    operations.append(Button(frame_top, text='Phase '+str(button_ptr+1)+'\nDouble click to Edit',font=bold_font,justify='left'))
    operations[button_ptr].pack(side=LEFT, padx=2, pady=5, expand=True, fill=X)
    operations[button_ptr].bind('<Button-1>',trigger_op_button_one_click)
    operations[button_ptr].bind('<Double-1>',trigger_op_button_double_click)
    mission.append(MissionPhaseParameters())
    button_ptr=button_ptr+1
    
    
def open_input_operation_parameters_form():    
    
    def select_tle_file():
        file_path = filedialog.askopenfilename(title="Select a TLE file", filetypes=(("TLE files", "*.tle"), ("All files", "*.*")))
        if file_path:
            tle_entry.delete(0, END)
            tle_entry.insert(0, file_path)
            popup.focus_force()
    
    def get_input():
        instance_name = name_entry.get()
        tle_file = tle_entry.get()
        start_datetime = start_date_entry.get()
        end_datetime = end_date_entry.get()
        
        # Basic validation
        if not instance_name:
            messagebox.showerror("Input Error", "Instance Name is required.")
            return
        if not tle_file:
            tle_file = None
            
        if not start_datetime:
            messagebox.showerror("Input Error", "Start Datetime is required.")
            return
        if not end_datetime:
            messagebox.showerror("Input Error", "End Datetime is required.")
            return
        

        # Print the inputs for now (you can replace this with actual logic to handle the inputs)
        #print("Instance Name:", instance_name)
        #print("TLE File:", tle_file)
        #print("Start Datetime:", start_datetime)
        #print("End Datetime:", end_datetime)

        #print(button_index)
        operations[button_index].config(text='Phase '+str(button_index+1) + '\n' + instance_name)
        
        if mission[button_index].get_phase_name() == None:
            mission[button_index] = MissionPhaseParameters(instance_name,tle_file)
            mission[button_index].load_TLE_data()
            mission[button_index].print_orbital_elements()
          
            
            
            
        # Close the pop-up window
        popup.destroy()    
        
    
        
    
    popup = Toplevel(screen)
    popup.geometry('500x350')
    popup.title("Setup Mission Phase")
    
    Label(popup, text="Instance Name:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
    name_entry = Entry(popup)
    name_entry.grid(row=0, column=1, padx=5, pady=5)
    
    Label(popup, text="TLE File:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
    tle_entry = Entry(popup)
    tle_entry.grid(row=1, column=1, padx=5, pady=5)
    tle_button = Button(popup, text="Browse", command= lambda: select_tle_file() or popup.wait_window())
    tle_button.grid(row=1, column=2, padx=5, pady=5)

    Label(popup, text="Start Datetime:").grid(row=2, column=0, padx=5, pady=5, sticky="e")
    start_date_entry = DateEntry(popup, selectmode='day', date_pattern='yyyy-mm-dd')
    start_date_entry.grid(row=2, column=1, padx=5, pady=5)

    Label(popup, text="End Datetime:").grid(row=3, column=0, padx=5, pady=5, sticky="e")
    end_date_entry = DateEntry(popup, selectmode='day', date_pattern='yyyy-mm-dd')
    end_date_entry.grid(row=3, column=1, padx=5, pady=5)

    # Create an OK button to submit the input
    ok_button = Button(popup, text="OK", command=get_input)
    ok_button.grid(row=5, column=0, columnspan=3, padx=5, pady=5)

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

# event management - Menu -> Orbiting Object -> TLE Load
def open_tle_file_dialog():
    file_path = filedialog.askopenfilename(title="Select a file", filetypes=(("tle files", "*.tle"),("TLE files", "*.TLE"),("All files", "*.*")))
    if file_path:
        print("Selected file:", file_path)
        # Add your code to handle the selected file here




# Split screens horizontally
screen.grid_rowconfigure(0,weight=1)
screen.grid_rowconfigure(1,weight=40)
screen.grid_columnconfigure(0, weight=1)

frame_top = create_frame(screen,0,0,title='Mission Timeline')
frame_under = create_frame(screen,1,0)


# Split bottom area vertically into 3 areas
frame_under.grid_columnconfigure(0,weight=1)
frame_under.grid_columnconfigure(1,weight=2)
frame_under.grid_columnconfigure(2,weight=2)
frame_under.grid_rowconfigure(0,weight=1)

frame_under_left = create_frame(frame_under,0,0,title='Mission Information')
frame_under_left = create_frame(frame_under,0,1,title='Satellite Parameters')
frame_under_left = create_frame(frame_under,0,2,title='Motion Propagator Parameters')



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
prop_group.add_command(label='Wizard',command=do_nothing)
prop_group.add_separator()
prop_group.add_command(label='Insert Operation',command=insert_mission_ops_button)
prop_group.add_command(label='Insert Op.Before',command=do_nothing)
prop_group.add_command(label='Insert Op.After',command=do_nothing)
top_menu_bar.add_cascade(label='Mission Setup',menu=prop_group)

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






screen.config(menu=top_menu_bar)
screen.mainloop()

