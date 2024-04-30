Running over an Anaconda environment with Python 3.11.8:
  Libraries:
    vpython      = 7.6.3
    numpy        = 1.26.4
    tk           = 8.6.12
    pyorbital    = 1.8.2

Installations steps:
 1) Install Anaconda
 2) Setup an environment with Anaconda
 3) Install Visual Studio Code
 4) Install Python extensions for VSC
 5) Setup VSC to point to the created environment (step 2)
 6) Install libraries on the created environment terminal:
      pip install vpyton
      pip install numpy
      pip install tk
      pip install pyorbital

How to run?:
  These scripts are being executed in an environment configured through Anaconda, and being coded with Visual Studio Code IDE, with python extensions.
  However it can be executed in different environment as long, as it has python 3 interpreter and the listed libraries.


How to use?:
  On browser tab that is opened when script is executed, explore the available controls. 
  Mouse scrool wheel will zoom in and out objects.
  Mouse right button will allow to change the camera viewing position


DiscoveryScripts:  --> Folder with the documented learning process (while coding)
  earthModelVpython.py      -- Testing script, how to code an earth model for satellite orbiting with VPyton.  
  layoutCanvas.py           -- How to manage multiple canvas with vpython
  visualizerLayout.py       -- Mockup for the final orbit visualizer
  readFileFromBrowser.py    -- Open a file dialog box

Orbits Visualizer:  --> Folder with the orbits visualizer developments
  startVisualizer.py        -- Starter
  visualizerParameters.py   -- Object definition to hold/manage parameters
  coordinateSystem.py       -- Holds design, maths and visual for coordinate systems
  earthModel.py             -- Where Earth "design" is coded

Images:            --> Folder with the resultant images.


