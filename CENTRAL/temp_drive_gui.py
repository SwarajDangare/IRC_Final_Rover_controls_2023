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
GEARUP = 5
GEARDOWN = 4
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
m = 0
GEARUP_toggle = True
GEARDOWN_toggle = True
GD = 0
GU = 0


def map(value, fromLow, fromHigh, toLow, toHigh):
    # Calculate the scaled value
    scaled_value = (value - fromLow) * (toHigh - toLow) / \
        (fromHigh - fromLow) + toLow
    # Return the scaled value
    return round(scaled_value)

# Initialize pygame
pygame.init()

# Set up the pygame window

# Set up the controller
pygame.joystick.init()
controller = pygame.joystick.Joystick(0)
print("Joystick Successfully Connected")
controller.init()

# S {R1} {R2} P {Triangle} {Cross} {Rectangle} {Circle} "
output_string = " m{m}X{left_joystick_x}Y{left_joystick_y}E"
# Set up the socket
HOST = '192.168.78.190'  # The host IP address
PORT = 27339      # The port to listen on
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    addr = (HOST, PORT)
    s.connect(addr)
    conn, addr1 = s.accept()
    with conn:
        print('Connected by', addr1)
        # Set up a timer and interval to send data
        timer = 0
        interval = 1  # Send data every 0.1 seconds

        running = True
        while running:
            # Check for events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                # elif event.type == pygame.JOYAXISMOTION:

                    # One of the joystick axes was moved
                    # data = f"Joystick axis {event.axis} moved to {event.value}."
                    # conn.sendall(data.encode())
                elif event.type == pygame.JOYBUTTONUP:
                    GEARUP_toggle = True
                    GEARDOWN_toggle = True

            # Update the timer and send data
            timer += 1 / 60  # 1/60 seconds have passed
            if timer >= interval:
                # The interval has passed, reset the timer and send data
                timer = 0
                # Get the state of the L1 and L2 buttons
                l1 = controller.get_button(GEARUP)
                l2 = controller.get_button(GEARDOWN)
                if m < 9:
                    # The L1 button has button index 4
                    if GEARUP_toggle and l1:
                        GEARUP_toggle = False
                        m += l1
                if m > 0:
                    # The L2 button has button index 5
                    if GEARDOWN_toggle and l2:
                        GEARDOWN_toggle = False
                        m -= l2
                # m = l1 | l2  # The value of m is 1 if either button is pressed, and 0 otherwise
                # Get the position of the left joystick axes
                left_joystick_0 = controller.get_axis(AXIS_LEFT_STICK_X)
                # The x-axis of the left joystick has axis index 0
                left_joystick_x_0 = int(
                    map(left_joystick_0, -1, 1, -1023, 1023))
                left_joystick_x = str(left_joystick_x_0)
                # The y-axis of the left joystick has axis

                left_joystick_y_1 = (
                    map(controller.get_axis(AXIS_LEFT_STICK_Y), -1, 1, -1023, 1023))
                left_joystick_y = str(left_joystick_y_1)
                # R1 = controller.get_button(5)
                # R2 = controller.get_button(7)
                # Triangle = controller.get_button(12)
                # Cross = controller.get_button(13)
                # Rectangle = controller.get_button(14)
                # Circle = controller.get_button(15)
                data = output_string.format(
                    m=m, left_joystick_x=left_joystick_x, left_joystick_y=left_joystick_y, E=0)
                # R1=R1, R2=R2, Triangle=Triangle, Cross=Cross,
                # Rectangle=Rectangle, Circle=Circle, E=0)
                conn.sendall(data.encode())

# Quit pygame
pygame.quit()
