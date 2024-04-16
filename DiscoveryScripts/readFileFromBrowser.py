from tkinter import filedialog, Tk
from vpython import *

# Function to read local file
def read_local_file(file_name):
    with open(file_name, 'r') as file:
        lines = file.readlines()
        return lines

# Function to visualize data
def visualize_data(data):
    for line in data:
        #Split the line into individual values
        #values = line.split()
        print(line)
        text_area.text = line
        scene.append_to_caption('\n')
        


# Function to handle file selection
def select_file():
    root = Tk()
    root.withdraw()  # Hide the root window
    file_path = filedialog.askopenfilename(title="Select a file", filetypes=[("Text files", "*.txt"),("Python Files","*.py")])
    if file_path:
        data = read_local_file(file_path)
        visualize_data(data)
    root.destroy()  # Destroy the root window after selecting a file

# Create a button to select a file
button(text="Select File", bind=select_file)
text_area = wtext(text='')

# Create scene
scene = canvas(title="File Data Visualization")


def check_events():
    scene.caption = "Waiting for events..."
    rate(30)  # Update the scene at 30 Hz
    root.update_idletasks()  # Process events in the Tkinter event queue
    root.after(100, check_events)  # Schedule the check_events function to run again after 100 milliseconds

# Start checking for events
root = Tk()
root.withdraw()  # Hide the root window initially
check_events()
root.mainloop()  # Start the Tkinter event loop


#while True:
#    pass