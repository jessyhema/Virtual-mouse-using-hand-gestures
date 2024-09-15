# Virtual-mouse-using-hand-gestures
A virtual mouse uses hand gestures to perform mouse movements and clicks.

## USAGE
Users who don't have a physical mouse can nevertheless use a virtual mouse to control their 
computer. Because it utilises a normal webcam, it may be viewed as hardware. Input devices like a genuine mouse or a computer keyboard can be utilised with a virtual mouse. A camera-controlled virtual mouse uses a variety of image processing methods. Mouse clicks are interpreted from user hand motions. The default setting on a web camera is for continuous image capturing. Facial recognition security software has recently started being used on PCs using webcams
### ALGORITHM
* Step 1:Start the program
* Step 2: Open some libraries installed for the code run the program
* Step 3: Uisng some libraries installed for the code run the program
* Step 4:Initialize the system and start the video capturing of WEBCAM
* Step 5:Capture frames using WEBCAM
* Step 6:Detect hands and hand tips using Media Pipe and OpenCV
* Step 7:Detect which finger is UP
* Step 8:Recognizing the gesture
* Step 9:Perform mouse operations according to gesture
* Step 10:Stop the program
###   Modules Used
* OpenCV
* Media Pipe
* PyAutoGUI
* Math
* Time
### OpenCV
A computer vision package called OpenCV contains techniques for processing images that detect objects. Real-time computer vision applications may be made using the Python computer vision package known as OpenCV. The OpenCV library is used to analyze data from photos and videos, including face and object detection. A free and open-source software library for computer vision and machine learning is called OpenCV. A standard infrastructure for computer vision applications was created with OpenCV in order to speed up the incorporation of artificial intelligence into products
### Media Pipe
A framework called Media Pipe is a Google open-source framework that is applied in a machine 
learning pipeline. Since the Media Pipe framework was created utilizing time series data, it maybe used for cross-platform programming. The Media Pipe architecture supports several audio and video formats since it is multimodal. The Media Pipe framework is used by the developer to create and analyze systems using graphs as well as to create systems for application-related purposes. The pipeline configuration is where the actions in the Media Pipe using system are carried out. Scalability on desktops and mobile devices is made possible by the pipeline's flexibility to execute on several platforms. The three essential components that make up the Media Pipe framework are performance evaluation, a system for accessing sensor data, and a group of reusable pieces known as calculators. A pipeline is a graph made of units called calculators that are connected to one another by streams via which data packets pass. In order to create their ownapplication, developers can add, remove, or redefine custom calculators anywhere in the graph.
### PyAutoGUI
In essence, PyAutoGUI is a Python software that runs on Windows, MacOS X, and Linux and allows users to imitate keyboard button pushes as well as mouse cursor movements and clicks. A Python package for cross-platform GUI automation for people is called PyAutoGUI. A Python automation module called PyAutoGUI may be used to click, drag, scroll, move, etc. It may be used to click precisely where you want. used to automate the control of the keyboard and mouse. There are several techniques to programmatically control the mouse and keyboard in each of the three main operating systems (Windows, macOS, and Linux). This frequently involves complex, enigmatic, and highly technical elements. PyAutoGUI's role is to conceal all of this complexity behind a straightforward API
### Math
A crucial component created to deal with mathematical operations is the Python math module. 
It has always been there and is supplied with the default Python version. The majority of the 
mathematical functions in the math module are only thin wrappers for the C platform's equivalents. The math module is effective and adheres to the C standard since its underlying functions are built in CPython. The Python math module gives you the possibility to perform common and useful mathematical operations within your programme. The Python math module offers a number of pre-set constants. There are many advantages to having access to these constants. One advantage is that by not having to manually hardcode them into your programme, you might save a lot of time
## CONCLUSION
The virtual mouse system's main objective is to eliminate the need for a hardware mouse by allowing users to manage mouse cursor functions with hand gestures instead. The described method can be used with a webcam or an integrated camera that analyses frames to
recognise hand movements and hand tips and execute specific mouse actions. The model has some 
shortcomings, including some difficulties with dragging and clicking to select text and a slight loss of precision in right-click mouse capabilities
Here's a sample code for it:
