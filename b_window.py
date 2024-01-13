import numpy as np
import pyqtgraph as pg
from PyQt5.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QSlider,
    QLineEdit,
    QComboBox,
    QPushButton
)
from PyQt5.QtCore import QTimer, Qt
from PyQt5.QtGui import QDoubleValidator
from a_waveform_generator import WaveformGenerator

class Window(QWidget):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Chara Technologies Assignment") # Setting the Window Title
        
        # Initialize the main plot widget and set labels
        self.plot_widget = pg.PlotWidget()
        self.plot_widget.setLabel("left", "Amplitude")
        self.plot_widget.setLabel("bottom", "Time")
        self.plot = self.plot_widget.plot(pen="b")  # Blue line plot

        # Create the main layout for the window
        layout = QVBoxLayout(self)

        # Waveform type dropdown menu
        self.waveform_label = QLabel("Waveform Type:")
        self.waveform_combobox = QComboBox()
        self.waveform_combobox.addItems(["sin", "cosine", "triangular", "square", "sawtooth", "pulse"])
        layout.addWidget(self.waveform_label)
        layout.addWidget(self.waveform_combobox)

        # Frequency input field
        self.frequency_label = QLabel("Frequency:")
        self.frequency_input = QLineEdit()
        self.frequency_input.setValidator(QDoubleValidator())
        self.frequency_input.setText("1.0")  # Default frequency
        layout.addWidget(self.frequency_label)
        layout.addWidget(self.frequency_input)

        # Amplitude slider
        self.amplitude_label = QLabel("Amplitude:")
        self.amplitude_slider = QSlider(Qt.Horizontal)
        self.amplitude_slider.setMinimum(0)
        self.amplitude_slider.setMaximum(100)
        self.amplitude_slider.setValue(50)  # Default amplitude
        layout.addWidget(self.amplitude_label)
        layout.addWidget(self.amplitude_slider)

        # Add the plot widget to the layout
        layout.addWidget(self.plot_widget)

        # Set up a timer for periodic waveform updates
        self.time = 1000 // 60  # Update interval in milliseconds
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_waveform)
        self.timer.start(self.time)

        # Initialize a variable for waveform animation
        self.num = 0.01

        # Button to open the user guide
        self.user_guide_button = QPushButton("User Guide")
        self.user_guide_button.clicked.connect(self.open_user_guide)
        layout.addWidget(self.user_guide_button)

        # Create a waveform generator instance
        self.waveform_generator = WaveformGenerator(self.plot, self.frequency_input, self.amplitude_slider, self.waveform_combobox, self.num)

    def update_waveform(self):
        # Call the waveform generator's update method on timer timeout
        self.waveform_generator.update_waveform()

    def open_user_guide(self):
        # Call the waveform generator's user guide method
        self.waveform_generator.open_user_guide()
