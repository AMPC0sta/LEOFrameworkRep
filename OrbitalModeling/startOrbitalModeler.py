from tkinter import *
from tkinter import filedialog, messagebox, ttk
from tkinter.font import Font
from tkcalendar import *
from widgets.datetime_picker import DateTimePicker
from datetime import datetime,timedelta
from pyorbital.orbital import Orbital
from os import *
from importlib.util import *

import pandas as pd
import subprocess
import tempfile

from missionPhaseParameters import *
from generatedMotion import *

sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'propagators'))

from propagators.propagatorSuperClass import PropagatorSuperClass

button_ptr=0            #create phase buttons auxiliary counter
button_index=0          #clicked button index
output_ptr=0
operations = []         #buttons array
mission = []
motion_propagators_list = ['SGP4::Base']
rv_coordinates = []
output = []
motion_to_be_passed = []
plugins_hashmap = [] # [(registering_name, plugin_class)]


base_path = getcwd() + '\\'
v_path = base_path  + 'OrbitsVisualizer\startVisualizer.py'
p_path = base_path +  'OrbitalModeling\propagators'
screen = Tk(className=' Low Earth Orbit Calculator')
screen.geometry('1600x800')


# plugins are python scripts .py
# their name shall start with plugin******.py
# they must be classes
# they shall inherit supper class PropagatorSuperClass
# they must implement super class abstract methods.
def available_plugins(directory):
    
    sys.path.insert(0, directory)  # Adiciona o diretório 'propagators' ao caminho de importação
    
    plugins = []
    for filename in os.listdir(directory):
        if filename.startswith("plugin") and filename.endswith(".py"):      # rules for plugins identification
            plugin_path = os.path.join(directory, filename)
            spec = spec_from_file_location("plugin_module", plugin_path)
            plugin_module = module_from_spec(spec)
            spec.loader.exec_module(plugin_module)

            for attr_name in dir(plugin_module):
                attr = getattr(plugin_module, attr_name)
                if isinstance(attr, type) and issubclass(attr, plugin_module.PropagatorSuperClass) and attr is not plugin_module.PropagatorSuperClass:
                    #plugin_instance = attr()
                    plugins.append(attr)
    #print (plugins)
    return plugins

            

# read frame title and font to backup it
def read_frame_title(frame):
    # Check if the frame has a title label attribute
    if hasattr(frame, 'title_label'):    
        # Return the text of the title label
        return (frame.title_label.cget("text"),frame.title_font)
    else:
        # Return None if there is no title label
        return None,None


# clear frame contents unless it's title
def clear_frame(frame):

    (t,f) = read_frame_title(frame)

    for widget in frame.winfo_children():
        widget.destroy()

    if t != None:
        lbl = Label(frame,text=t,font=f)
        lbl.pack(side='top')
        frame.title_label = lbl
        frame.title_font = f


# auxiliary GUI functions
def print_pair_label_value_on_frame(frame,position,label,value,font_regular,font_bold):
    pair_frame = Frame(frame)
    pair_frame.pack(side=position,fill=X, pady=2)  # Pack each pair frame vertically
    Label(pair_frame,text=f"{label}:",font=font_bold).pack(anchor='w',side=LEFT,padx=0)
    Label(pair_frame,text=value,font=font_regular).pack(anchor='w',side=RIGHT,padx=0)


#if phase button is pressed
def trigger_op_button_one_click(event):
    for button in operations:
        button.config(relief='raised',bg='SystemButtonFace')

    # selected button paints different
    event.widget.config(relief='sunken',bg='grey')
    clear_frame(frame_under_left)
    clear_frame(frame_under_mid)
    clear_frame(frame_under_right)
    button_index = operations.index(event.widget)

    frame_under_left.pack_propagate(False)             
    
    # copy object data to frame
    if mission[button_index].get_orbital_elements() != None:
        elements = mission[button_index].get_orbital_elements().to_show_on_widget()
    else:
        elements = None
    
    if elements != None:
        font_regular = Font(family="Helvetica", size=10)
        font_bold = Font(family="Helvetica", size=10,weight="bold")
  
        elements.reverse()
        elements.append(("TLE Filename",mission[button_index].get_orbital_elements().get_tle_filename().split('/')[-1]))
        elements.append(("Satellite Name",mission[button_index].get_orbital_elements().get_satellite_name()))
            
        for i, (label, value) in enumerate(elements):
            print_pair_label_value_on_frame(frame=frame_under_left,position=BOTTOM,label=label,value=value,font_regular=font_regular,font_bold=font_bold)
    else:
        clear_frame(frame_under_left)
        clear_frame(frame_under_mid)
        clear_frame(frame_under_right)
        
    start = mission[button_index].get_start_datetime()
    end = mission[button_index].get_end_datetime()
    propagator = mission[button_index].get_motion_descriptor()
    
    font_regular = Font(family="Helvetica", size=10)
    font_bold = Font(family="Helvetica", size=10,weight="bold")
    
    if (start != None) and (end != None):
        print_pair_label_value_on_frame(frame=frame_under_mid,position=TOP,label='Start Datetime:',value=start,font_regular=font_regular,font_bold=font_bold)
        print_pair_label_value_on_frame(frame=frame_under_mid,position=TOP,label='End Datetime:',value=end,font_regular=font_regular,font_bold=font_bold)
    
    if propagator != None:
        print_pair_label_value_on_frame(frame=frame_under_right,position=TOP,label='Motion Propagator',value=propagator,font_regular=font_regular,font_bold=font_bold)


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
    mission.append(MissionPhaseParameters(phase_position=button_ptr))
    button_ptr=button_ptr+1
    
    
# pop form
def open_input_operation_parameters_form():    

    # ask for tle file
    def select_tle_file():
        file_path = filedialog.askopenfilename(title="Select a TLE file", filetypes=(("TLE files", "*.tle"), ("All files", "*.*")))
        if file_path:
            tle_entry.delete(0, END)
            tle_entry.insert(0, file_path)
            popup.focus_force()
    
    # ask for parameters 
    def get_input():
        instance_name = name_entry.get()
        tle_file = tle_entry.get()
        start_datetime = start_date_entry.get_datetime()
        end_datetime = end_date_entry.get_datetime()
        propagator = propagator_combobox.get()
        
                
        # Basic validation
        if not instance_name:
            messagebox.showerror("Input Error", "Instance Name is required.")
            return
        
        #optional field
        if not tle_file:
            tle_file = None
            
        if not start_datetime:
            messagebox.showerror("Input Error", "Start Datetime is required.")
            return
        if not end_datetime:
            messagebox.showerror("Input Error", "End Datetime is required.")
            return
        
        operations[button_index].config(text='Phase '+str(button_index+1) + '\n' + instance_name)
                
        if mission[button_index].get_phase_name() == None:
            mission[button_index] = MissionPhaseParameters(phase_name=instance_name,tle_file=tle_file,phase_position=button_index)
            mission[button_index].load_TLE_data()
            mission[button_index].print_orbital_elements()
            mission[button_index].set_start_datetime(start_datetime)
            mission[button_index].set_end_datetime(end_datetime)
            mission[button_index].set_motion_descriptor(propagator)

            elements = mission[button_index].get_orbital_elements().to_show_on_widget()
            
            font_regular = Font(family="Helvetica", size=10)
            font_bold = Font(family="Helvetica", size=10,weight="bold")
  
            elements.reverse()
            elements.append(("TLE Filename",mission[button_index].get_orbital_elements().get_tle_filename().split('/')[-1]))
            elements.append(("Satellite Name",mission[button_index].get_orbital_elements().get_satellite_name()))
           
            frame_under_left.pack_propagate(False)             
            
            for i, (label, value) in enumerate(elements):
                print_pair_label_value_on_frame(frame=frame_under_left,position=BOTTOM,label=label,value=value,font_regular=font_regular,font_bold=font_bold)
                        
            print_pair_label_value_on_frame(frame=frame_under_mid,position=TOP,label='Start Datetime:',value=start_datetime,font_regular=font_regular,font_bold=font_bold)
            print_pair_label_value_on_frame(frame=frame_under_mid,position=TOP,label='End Datetime:',value=end_datetime,font_regular=font_regular,font_bold=font_bold)
    
            print_pair_label_value_on_frame(frame=frame_under_right,position=TOP,label='Motion Propagator',value=propagator,font_regular=font_regular,font_bold=font_bold)
            
        # Close the pop-up window
        popup.destroy()    
        
    # popup form raise up
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
    start_date_entry = DateTimePicker(popup)
    start_date_entry.grid(row=2, column=1, padx=5, pady=5)

    Label(popup, text="End Datetime:").grid(row=3, column=0, padx=5, pady=5, sticky="e")
    end_date_entry = DateTimePicker(popup)
    end_date_entry.grid(row=3, column=1, padx=5, pady=5)

    Label(popup, text="Motion Propagator:").grid(row=4, column=0, padx=5, pady=5, sticky="e")
    propagator_var = StringVar(value=motion_propagators_list[0])  # Default to the first option
    propagator_combobox = ttk.Combobox(popup, textvariable=propagator_var, values=motion_propagators_list, state='readonly',width=50)
    propagator_combobox.grid(row=4,column=1)

    popup.propagator_combobox = propagator_combobox


    # Create an OK button to submit the input
    ok_button = Button(popup, text="OK", command=get_input)
    ok_button.grid(row=5, column=0, columnspan=3, padx=5, pady=5)


# to be used in event management (undefined events)
def do_nothing():
    pass


# generate a list of 4D points
def generate_motion():
    global rv_coordinates
    global output_ptr
    
    rv_coordinates = []
    
    if len(mission)==1:
        orb = mission[0].get_orbital_data()
        sat_name = mission[0].get_satellite_name()
        tle_name = mission[0].get_tle_filename()
        now = datetime.now().strftime('%Y%m%d%H%M%S')
        
        time_step = timedelta(minutes=1)
        start_time = datetime.strptime(mission[0].get_start_datetime(),'%Y-%m-%d %H:%M:%S')
        current_time = start_time
        end_time = datetime.strptime(mission[0].get_end_datetime(),'%Y-%m-%d %H:%M:%S')
        
        while current_time <= end_time:
            pos, vel = orb.get_position(current_time)
            rv_coordinates.append((current_time,pos,vel))
            current_time += time_step
            #print(current_time,pos,vel)
    
    output.append(GeneratedMotion(id="ID-"+sat_name+"."+now,tle_file=tle_name,start_datetime=start_time,end_datetime=end_time,motion_list=rv_coordinates))
    output_ptr = output_ptr + 1
    
    create_table(table_frame, output)


# create frames with labels
def create_frame(root, row, column, rowspan=1, columnspan=1, title=None):
    frame = Frame(root, bg="white", bd=1, relief=RAISED)
    frame.grid(row=row, column=column, rowspan=rowspan, columnspan=columnspan, sticky="nsew")
    
    # Add a label as the title
    if title:
        label = Label(frame, text=title, fg="black", font=("Arial", 12, "bold"))
        label.pack(padx=10, pady=5)  # Adjust padding as needed

        frame.title_label = label
        frame.title_font = ("Arial", 12, "bold")
    
    return frame

# store a list of tuples, one line per node
def write_tuples_to_file(tuples_array, filename):
    with open(filename, 'w') as file:
        for item in tuples_array:
            #line = ','.join(map(str, item))  # Convert each element of the tuple to string and join with commas
            file.write(str(item) + '\n')  # Write the line to the file



# event management - Menu -> Orbiting Object -> TLE Load
def open_tle_file_dialog():
    file_path = filedialog.askopenfilename(title="Select a file", filetypes=(("tle files", "*.tle"),("TLE files", "*.TLE"),("All files", "*.*")))
    if file_path:
        print("Selected file:", file_path)
        # Add your code to handle the selected file here


# 'see' buttons are being placed dinamically, if pressed
def see_action(row,column):
    global output,v_path
    global motion_to_be_passed,mission
    
    list = output[row].get_motion_list()
    (tms,pos,vel) = zip(*list)
    
    for i,t in enumerate(tms):
        x,y,z = pos[i]
        motion_to_be_passed.append((x,y,z,t))
      
    script_path = os.path.abspath(v_path)
    p = mission[0].get_orbital_elements().get_period()
    temp_file =  tempfile.NamedTemporaryFile(delete=False)
    write_tuples_to_file(motion_to_be_passed,temp_file.name)
       
    result = subprocess.run(["python",script_path,temp_file.name,str(p)],text=True,capture_output=True) 
    
    print("Standard Output:\n", result.stdout)
    print("Standard Error:\n", result.stderr)
    
    # Remove the temporary file
    os.unlink(temp_file.name)
    os.remove(temp_file.name)
    

# 'delete' buttons are being placed dinamically, if pressed
def del_action(row,column):
    global output, output_ptr
    
    del output[row]
    output_ptr = output_ptr - 1
    
    clear_frame(table_frame)        
    create_table(table_frame,output)


# Function to populate the frame with a table
def create_table(frame, output):
    
    header_font = Font(weight='bold')  # Create a bold font
    
    l = Label(frame, text="#", borderwidth=1, relief="solid", padx=10, pady=5,font=header_font)
    l.grid(row=0, column=0, sticky="nsew")
    
    l = Label(frame, text="Generation.ID", borderwidth=1, relief="solid", padx=10, pady=5,font=header_font)
    l.grid(row=0, column=1, sticky="nsew")
    
    l = Label(frame, text="TLE Files", borderwidth=1, relief="solid", padx=10, pady=5,font=header_font)
    l.grid(row=0, column=2, sticky="nsew")
    
    l = Label(frame, text="Start Motion", borderwidth=1, relief="solid", padx=10, pady=5,font=header_font)
    l.grid(row=0, column=3, sticky="nsew")
    
    l = Label(frame, text="End Motion", borderwidth=1, relief="solid", padx=10, pady=5,font=header_font)
    l.grid(row=0, column=4, sticky="nsew")
    
    l = Label(frame, text="Visualizer", borderwidth=1, relief="solid", padx=10, pady=5,font=header_font)
    l.grid(row=0, column=5, sticky="nsew")
    
    l = Label(frame, text="Delete", borderwidth=1, relief="solid", padx=10, pady=5,font=header_font)
    l.grid(row=0, column=6, sticky="nsew")
    
    
    for i, row in enumerate(output):
        
        label = Label(frame, text=str(i), borderwidth=1, relief="solid", padx=10, pady=5)
        label.grid(row=i+1, column=0, sticky="nsew")
        
        for j, value in enumerate([row.get_id(),row.get_tle_filename(),row.get_start_datetime(),row.get_end_datetime()]):
            label = Label(frame, text=value, borderwidth=1, relief="solid", padx=10, pady=5)
            label.grid(row=i+1, column=j+1, sticky="nsew")
            
        button = Button(frame, text="See",command=lambda i=i: see_action(i,4))
        button.grid(row=i+1, column=5, sticky="nsew", padx=5, pady=5)
            
        button = Button(frame, text="Delete",command=lambda i=i: del_action(i,5))
        button.grid(row=i+1, column=6, sticky="nsew", padx=5, pady=5)

    # Make columns expand equally
    for j in range(5):
        frame.grid_columnconfigure(j, weight=1)
        

#search for available propagators
directory = os.path.join(os.path.dirname(__file__), "propagators")
plugins= available_plugins(directory)

# register plugins into an internal Hashmaps
for plugin_cls in plugins:
    p = plugin_cls()
    p_name = p.name_to_register_plugin()+'::Plugin'
    motion_propagators_list.append(p_name)
    plugins_hashmap.append((p_name,p))


# Split screens horizontally
screen.grid_rowconfigure(0,weight=1)
screen.grid_rowconfigure(1,weight=40)
screen.grid_columnconfigure(0, weight=1)

frame_top = create_frame(screen,0,0,title='Mission Timeline')
frame_under = create_frame(screen,1,0)

# Split bottom area vertically into 3 areas
frame_under.grid_columnconfigure(0,weight=1)
frame_under.grid_columnconfigure(1,weight=1)
frame_under.grid_columnconfigure(2,weight=2)
frame_under.grid_rowconfigure(0,weight=2)

frame_under_left = create_frame(frame_under,0,0,title='Satellite Parameters')
frame_under_mid = create_frame(frame_under,0,1,title='Phase Parameters')
frame_under_r = create_frame(frame_under,0,2)

frame_under_r.grid_rowconfigure(0,weight=30)
frame_under_r.grid_rowconfigure(1,weight=90)
frame_under_r.grid_columnconfigure(0,weight=1)

frame_under_right = create_frame(frame_under_r,0,0,title='Motion Propagator Parameters')
frame_to_data_output = create_frame(frame_under_r,1,0,title='Output Dashboard:Simulation Results')

# Draw menus
top_menu_bar = Menu(screen)

file_group = Menu(top_menu_bar,tearoff=0)
file_group.add_command(label='New',command=do_nothing)
file_group.add_command(label='Open',command=do_nothing)
file_group.add_command(label='Save',command=do_nothing)
file_group.add_command(label='Save As',command=do_nothing)
file_group.add_command(label='Close',command=do_nothing)
file_group.add_separator()
file_group.add_command(label='Exit',command=screen.quit)
top_menu_bar.add_cascade(label='Mission Project',menu=file_group)

prop_group = Menu(top_menu_bar,tearoff=0)   
prop_group.add_command(label='Wizard',command=do_nothing)
prop_group.add_separator()
prop_group.add_command(label='Insert Phase',command=insert_mission_ops_button)
prop_group.add_command(label='Insert Phase Before',command=do_nothing)
top_menu_bar.add_cascade(label='Mission Setup',menu=prop_group)

gen_group = Menu(top_menu_bar,tearoff=0)
gen_group.add_command(label='Timeline Verification')
gen_group.add_command(label='Generate Motion',command=generate_motion)
gen_group.add_separator()
gen_group.add_command(label='Call Motion Visualizer')
top_menu_bar.add_cascade(label='Execute',menu=gen_group)

custom_group = Menu(top_menu_bar,tearoff=0)
custom_group.add_command(label='New',command=do_nothing)
custom_group.add_command(label='Open',command=do_nothing)
custom_group.add_command(label='Save',command=do_nothing)
custom_group.add_command(label='Save As',command=do_nothing)
custom_group.add_command(label='Close Model',command=do_nothing)
top_menu_bar.add_cascade(label='Custom Models',menu=custom_group)

frame_to_data_output.pack_propagate(False)
table_frame = Frame(frame_to_data_output, bg='lightgray')
table_frame.pack(side='bottom',padx=10, pady=10, fill='x', expand=True,anchor='s')

create_table(table_frame, output)

# looper
screen.config(menu=top_menu_bar)
screen.mainloop()

