Running over an Anaconda environment with Python 3.11.8:
  Libraries:
    - vpython      = 7.6.3
    - numpy        = 1.26.4
    - tk           = 8.6.12
    - pyorbital    = 1.8.2
    - tkcalendar   = 1.6.1

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
      pip install tkcalendar

How to run?:
  These scripts are being executed in an environment configured through Anaconda, and being coded with Visual Studio Code IDE, with python extensions.
  However it can be executed in different environment as long, as it has python 3 interpreter and the listed libraries.


How to use?:
  On browser tab that is opened when script is executed, explore the available controls. 
  Mouse scrool wheel will zoom in and out objects.
  Mouse right button will allow to change the camera viewing position


Common             --> Folder with shared classes
  celestrakObjects.py           -- Manage and connects orbiting objects on www.celestrak.org 
  orbitalMechanics.py           -- Keplerian calculations 


DiscoveryScripts:  --> Folder with the documented learning process (while coding)
  earthModelVpython.py          -- Testing script, how to code an earth model for satellite orbiting with VPyton.  
  layoutCanvas.py               -- How to manage multiple canvas with vpython
  visualizerLayout.py           -- Mockup for the final orbit visualizer
  readFileFromBrowser.py        -- Open a file dialog box


OrbitsVisualizer:  --> Folder with the orbits visualizer developments
  startVisualizer.py            -- Starter
  visualizerParameters.py       -- Object definition to hold/manage parameters
  coordinateSystem.py           -- Holds design, maths and visual for coordinate systems
  earthModel.py                 -- Where Earth "design" is coded
  satelliteRepresentation.py    -- Draw of a sat unit.


OrbitalModeling    --> GUI to parameterize and generate new orbits and propagators.
   mission.py                   -- Setup of missions (aggregator project)
   missionPhaseParameters.py    -- Each mission is an agregation of phases
   startOrbitalModeler.py       -- starting script (GUI)


TLE_files          --> Data folder with two element lines files (TLE's)


Images & Videos:     --> Folder with the resultant images, higher the X, recent the code
  draft_animation_X.mp4         -- Videos with visualizar sequences.
  orbit-visualizer-draft-X.png  
  orbit-modeler-draft_X.png 

