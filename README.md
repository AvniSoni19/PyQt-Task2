# PyQt-Task2
Assignment Task 2
<h2> Functionalities </h2>
<ul>
<li>GUI: The GUI includes widgets such as dropdown menus, input fields, sliders, and buttons.</li><br>
<li>Waveform Generation: The application generates various types of waveforms, including sine, cosine, triangular, square, sawtooth, and pulse.</li><br>
<li>Real-time Updating: The generated waveform is updated in real-time on the PyQtGraph PlotWidget based on user input. The update occurs at a fixed interval using a QTimer.</li><br>
<li>User Guide: The user guide includes details on waveform types, instructions on using the GUI, and the purpose of different controls.</li><br>
<li>Error Handling: The application handles errors, such as invalid input for frequency, by providing default values.</li><br>
<li>Continuous Waveform Update:The waveform is continuously updated with a time-dependent phase offset (num) to create an animation effect.</li><br>
</ul>

<h2>Technologies Used</h2>
<ul>
<li>PyQt5: Used for building the graphical user interface.</li><br>
<li>pyqtgraph: Utilized for generating interactive plots within the application.</li><br>
<li>NumPy: Used particularly for generating waveforms and handling numerical data.</li><br>
</ul>

<h2>Installation</h2>
To run, ensure you have the following prerequisites installed:<br>
<ul>
<li>Python 3.x</li><br>
<li>PyQt5 ('pip install PyQt5')</li><br>
<li>pyqtgraph ('pip install pyqtgraph')</li><br>
<li>numpy ('pip install numpy')</li><br>
</ul>

<h2>Running the Application</h2>
To launch the application:<br>
<ul>
<li>Clone the repository or download the source code.</li><br>
<li>Ensure all dependencies are installed.</li><br>
<li>Run the main.py file using Python.</li><br>
</ul>

<h2>File Details</h2>
<ul>
<li>main.py: This is the main entry point of the application.</li><br>
<li>b_window.py: This file defines the main window class, 'Window', and sets up the GUI elements.</li><br>
<li>a_waveform_generator.py: Responsible for generating waveforms and displaying a user guide.</li><br>
<li>Sample.mp4: It is the sample video of implementation of the application showing the functionalities like types of waveforms, input frequency, amplitude slider, dynamic changes in the graph and user guide.</li><br>
</ul>