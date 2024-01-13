import numpy as np
from PyQt5.QtWidgets import QDialog, QVBoxLayout, QTextBrowser

class WaveformGenerator:
    def __init__(self, plot, frequency_input, amplitude_slider, waveform_combobox, num):
        # Initialize the WaveformGenerator with necessary parameters
        # plot: PlotWidget to display the waveform
        # frequency_input: QLineEdit for user input of frequency
        # amplitude_slider: QSlider for adjusting the amplitude
        # waveform_combobox: QComboBox for selecting waveform type
        # num: Counter for updating the waveform dynamically
        self.plot = plot
        self.frequency_input = frequency_input
        self.waveform_combobox = waveform_combobox
        self.amplitude_slider = amplitude_slider
        self.num = num
        self.original_amplitude = 1.0  # Default amplitude

    def update_waveform(self):
        # Update the waveform based on user inputs and slider positions
        try:
            frequency = float(self.frequency_input.text())
        except ValueError:
            frequency = 1.0  # Default frequency if input is not a valid float

        # Scale amplitude to be between 0 and 2
        amplitude_scale = self.amplitude_slider.value() / 50.0
        waveform_type = self.waveform_combobox.currentText()

        # Generate time values
        t = np.linspace(0, 2 * np.pi, 1000)

        # Generate waveform based on selected type
        if waveform_type == "sin":
            waveform = self.original_amplitude * amplitude_scale * np.sin(2 * np.pi * frequency * t + self.num)
        elif waveform_type == "cosine":
            waveform = amplitude_scale * np.cos(2 * np.pi * frequency * t + self.num)
        elif waveform_type == "triangular":
            frequency = 0.5
            waveform = amplitude_scale * np.abs(2 * (t * frequency - np.floor(t * frequency + 0.5 + self.num)))
        elif waveform_type == "square":
            waveform = amplitude_scale * np.sign(np.sin(2 * np.pi * frequency * t + self.num))
        elif waveform_type == "sawtooth":
            waveform = amplitude_scale * (2 * (t * frequency - np.floor(t * frequency + 0.5 + self.num)))
        elif waveform_type == "pulse":
            waveform = amplitude_scale * np.where(np.sin(2 * np.pi * frequency * t + self.num) > 0, 1, -1)
        else:
            waveform = np.zeros_like(t) + self.num

        # Update the plot with the generated waveform
        self.plot.setData(t, waveform)
        self.num = self.num + 0.01  # Increment the counter for dynamic update

    def open_user_guide(self):
        # Open a user guide dialog with instructions on using the waveform generator
        dialog = QDialog()
        dialog.setWindowTitle("User Guide")
        layout = QVBoxLayout()

        text_browser = QTextBrowser()
        text_browser.setOpenExternalLinks(True)
        text_browser.setHtml(
            "<h2>Waveform Generator User Guide</h2>"
            "<p>This application allows you to generate different types of waveforms:</p>"
            "<ul>"
            "<li><b>Sin:</b> Sine waveform</li>"
            "<li><b>Cosine:</b> Cosine waveform</li>"
            "<li><b>Triangular:</b> Triangular waveform</li>"
            "<li><b>Square:</b> Square waveform</li>"
            "<li><b>Sawtooth:</b> Sawtooth waveform</li>"
            "<li><b>Pulse:</b> Pulse waveform</li>"
            "</ul>"
            "<p>Instructions:</p>"
            "<ol>"
            "<li>Choose the waveform type from the dropdown menu.</li>"
            "<li>Adjust the frequency using the frequency input field.</li>"
            "<li>Set the amplitude using the amplitude slider.</li>"
            "<li>Observe the generated waveform in the plot.</li>"
            "</ol>"
        )
        layout.addWidget(text_browser)

        dialog.setLayout(layout)
        dialog.exec_()
