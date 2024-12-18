A quick demo on integrating a constant data stream from python (in this case the X,Y position of a mouse cursor in a box) into unity. 

The python script is meant to mimic a datastream from an eyetracker which would output an X/Y position. 

This information is then written to a file, which is read in real time by unity. 

An empty gameobject is responsible for taking that information and sending it to the unity debug log console. 

Then, that data is parsed and moves a box around the screen to prove you can utilize this data. 

Once the box is in the middle of the screen, the screen turns green, and the "game" states you have completed the level.  
