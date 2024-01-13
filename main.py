# Importing the necessary modules
import sys
from PyQt5.QtWidgets import QApplication
from b_window import Window

# Main entry point of the application
if __name__ == "__main__":
    # Create a QApplication instance
    app = QApplication(sys.argv)

    # Create an instance of the Window class
    window = Window()
    
    # Show the main window
    window.show()

    # Start the application event loop
    sys.exit(app.exec_())
