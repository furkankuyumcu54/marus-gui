import sys
import cv2
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QLabel
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtCore import Qt, QTimer


def move_up():
    # Code to move turret up
    pass


def move_down():
    # Code to move turret down
    pass


def move_left():
    # Code to move turret left
    pass


def move_right():
    # Code to move turret right
    pass


def fire():
    # Code to fire turret
    pass


def stop():
    # Code to stop turret movement
    pass


def update_camera():
    ret, frame = cap.read()
    if ret:
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        h, w, ch = frame.shape
        bytesPerLine = ch * w
        convert_to_qt_format = QImage(frame.data, w, h, bytesPerLine, QImage.Format_RGB888)
        pixmap = QPixmap.fromImage(convert_to_qt_format)
        camera_label.setPixmap(pixmap.scaled(camera_label.width(), camera_label.height(), Qt.KeepAspectRatio))
    else:
        print("Error: Could not read frame")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QWidget()
    window.setWindowTitle('Mar-US GUI')
    window.resize(800, 600)  # Set a fixed size for the window

    # Camera setup
    cap = cv2.VideoCapture(0)
    ret, _ = cap.read()  # Read a frame to initialize the camera

    # Camera View
    camera_label = QLabel('Camera View')
    camera_label.setAlignment(Qt.AlignCenter)

    # Buttons
    up_button = QPushButton('Up')
    down_button = QPushButton('Down')
    left_button = QPushButton('Left')
    right_button = QPushButton('Right')
    fire_button = QPushButton('Fire')
    stop_button = QPushButton('Stop')

    # Button Layout
    button_layout = QHBoxLayout()
    button_layout.addWidget(up_button)
    button_layout.addWidget(down_button)
    button_layout.addWidget(left_button)
    button_layout.addWidget(right_button)
    button_layout.addWidget(fire_button)
    button_layout.addWidget(stop_button)

    # Main Layout
    main_layout = QVBoxLayout()
    main_layout.addWidget(camera_label)
    main_layout.addLayout(button_layout)

    window.setLayout(main_layout)

    # Connect buttons to their respective functions
    up_button.clicked.connect(move_up)
    down_button.clicked.connect(move_down)
    left_button.clicked.connect(move_left)
    right_button.clicked.connect(move_right)
    fire_button.clicked.connect(fire)
    stop_button.clicked.connect(stop)

    # Setup timer to update camera feed
    timer = QTimer()
    timer.timeout.connect(update_camera)
    timer.start(100)  # Update every 100 milliseconds

    window.show()  # Show the window

    sys.exit(app.exec_())
