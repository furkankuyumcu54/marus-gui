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


def pause():
    # Code to pause
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
    window.showMaximized()

    # Camera setup
    cap = cv2.VideoCapture(0)
    ret, _ = cap.read()  # Read a frame to initialize the camera

    # Camera View
    camera_label = QLabel('Camera View')
    camera_label.setAlignment(Qt.AlignCenter)

    # Movement Buttons
    up_button = QPushButton('Up')
    down_button = QPushButton('Down')
    left_button = QPushButton('Left')
    right_button = QPushButton('Right')

    # Fire Mode Options
    fire_mode_label = QLabel('Fire Mode:')
    fire_mode_option1 = QPushButton('Option 1')
    fire_mode_option2 = QPushButton('Option 2')

    # Fire, Pause, Stop Buttons
    fire_button = QPushButton('Fire')
    pause_button = QPushButton('Pause')
    stop_button = QPushButton('Stop')

    # Movement Buttons Layout
    movement_button_layout = QVBoxLayout()
    movement_button_layout.addWidget(up_button)
    movement_button_layout.addWidget(down_button)
    movement_button_layout.addWidget(left_button)
    movement_button_layout.addWidget(right_button)

    # Fire Mode Options Layout
    fire_mode_layout = QHBoxLayout()
    fire_mode_layout.addWidget(fire_mode_label)
    fire_mode_layout.addWidget(fire_mode_option1)
    fire_mode_layout.addWidget(fire_mode_option2)

    # Fire, Pause, Stop Buttons Layout
    action_button_layout = QHBoxLayout()
    action_button_layout.addWidget(fire_button)
    action_button_layout.addWidget(pause_button)
    action_button_layout.addWidget(stop_button)

    # Add PNG image
    image_label = QLabel()
    pixmap = QPixmap('marus_logo.jpg')  # Change 'your_image.png' to the path of your PNG file
    pixmap_resized = pixmap.scaled(400, 400, Qt.KeepAspectRatio)  # Adjust the size as needed
    image_label.setPixmap(pixmap_resized)

    # Main Button Layout
    button_layout = QVBoxLayout()
    button_layout.addLayout(fire_mode_layout)
    button_layout.addLayout(movement_button_layout)
    button_layout.addStretch(1)

    # Layout for the PNG image
    image_layout = QHBoxLayout()
    image_layout.addStretch(2)  # Add space to align the image in the center
    image_layout.addWidget(image_label)
    image_layout.addStretch(1)  # Add space to align the image in the center
    button_layout.addLayout(image_layout)  # Add the image layout here

    button_layout.addStretch(1)  # Add space between image and action buttons
    button_layout.addLayout(action_button_layout)

    # Main Layout
    main_layout = QHBoxLayout()
    main_layout.addWidget(camera_label, 1)  # Add camera label, taking up most of the space
    main_layout.addLayout(button_layout)

    window.setLayout(main_layout)

    # Connect buttons to their respective functions
    up_button.clicked.connect(move_up)
    down_button.clicked.connect(move_down)
    left_button.clicked.connect(move_left)
    right_button.clicked.connect(move_right)
    fire_button.clicked.connect(fire)
    pause_button.clicked.connect(pause)
    stop_button.clicked.connect(stop)

    # Setup timer to update camera feed
    timer = QTimer()
    timer.timeout.connect(update_camera)
    timer.start(10)  # Update every 10 milliseconds

    window.show()  # Show the window

    sys.exit(app.exec_())
