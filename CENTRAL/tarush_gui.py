import pygame
import socket
import time

AXIS_LEFT_STICK_X = 0
AXIS_LEFT_STICK_Y = 1
AXIS_RIGHT_STICK_X = 2
AXIS_RIGHT_STICK_Y = 3
AXIS_R2 = 4
AXIS_L2 = 5
# Labels for DS4 controller buttons
# # Note that there are 14 buttons (0 to 13 for pygame, 1 to 14 for Windows setup)
BUTTON_SQUARE = 2
BUTTON_CROSS = 0
BUTTON_CIRCLE = 1
BUTTON_TRIANGLE = 3
BUTTON_L1 = 9
BUTTON_R1 = 10
BUTTON_L2 = 7
BUTTON_R2 = 8
BUTTON_SHARE = 8
BUTTON_OPTIONS = 6

BUTTON_LEFT_STICK = 10
BUTTON_RIGHT_STICK = 11

UP_ARROW = 11
DOWN_ARROW = 12
LEFT_ARROW = 13
RIGHT_ARROW = 14
BUTTON_PS = 5
BUTTON_PAD = 15


def map(value, fromLow, fromHigh, toLow, toHigh):
    # Calculate the scaled value
    scaled_value = (value - fromLow) * (toHigh - toLow) / \
        (fromHigh - fromLow) + toLow
    # Return the scaled value
    return scaled_value

# Initialize pygame
pygame.init()

# Set up the pygame window

# Set up the controller
pygame.joystick.init()
controller = pygame.joystick.Joystick(0)
print("Joystick Successfully Connected")
controller.init()

output_string = " m {L1} {L2} X {left_joystick_x} Y {left_joystick_y} S {R1} {R2} P {Triangle} {Cross} {Rectangle} {Circle} E"
# Set up the socket
HOST = '127.0.0.1'  # The host IP address
PORT = 8000       # The port to listen on
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    #server = "192.168.137.46"
    #port = 27339
    addr = (HOST, PORT)
    #client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(addr)

    # s.bind((HOST, PORT))
    # s.listen()
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        # Set up a timer and interval to send data
        timer = 0
        interval = 1  # Send data every 0.1 seconds

        running = True
        while running:
            # Check for events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.JOYAXISMOTION:
                    # One of the joystick axes was moved
                    data = f"Joystick axis {event.axis} moved to {event.value}."
                    conn.sendall(data.encode())
            # Update the timer and send data
            timer += 1 / 60  # 1/60 seconds have passed
            if timer >= interval:
                # The interval has passed, reset the timer and send data
                timer = 0
                # Get the state of the L1 and L2 buttons
                if m < 9:
                    # The L1 button has button index 4
                    l1 = controller.get_button(4)
                    m = +l1
                elif m > 0:
                    # The L2 button has button index 6
                    l2 = controller.get_button(6)
                    m -= l2
                m = l1 | l2  # The value of m is 1 if either button is pressed, and 0 otherwise
                # Get the position of the left joystick axes
                left_joystick_0 = controller.get_axis(0)
                # The x-axis of the left joystick has axis index 0
                left_joystick_x_0 = int(
                    map(left_joystick_0, -1, 1, -1023, 1023))
                left_joystick_x = str(left_joystick_x_0)
                # The y-axis of the left joystick has axis
                left_joystick_y_1 = (
                    map(controller.get_axis(1), -1, 1, -1023, 1023))
                left_joystick_y = str(left_joystick_y_1)
                R1 = controller.get_button(5)
                R2 = controller.get_button(7)
                Triangle = controller.get_button(12)
                Cross = controller.get_button(13)
                Rectangle = controller.get_button(14)
                Circle = controller.get_button(15)
                data = output_string.format(L1=l1, L2=l2, left_joystick_x=left_joystick_x, left_joystick_y=left_joystick_y,
                                            R1=R1, R2=R2, Triangle=Triangle, Cross=Cross, Rectangle=Rectangle, Circle=Circle, E=0)
                conn.sendall(data.encode())

# Quit pygame
pygame.quit()
