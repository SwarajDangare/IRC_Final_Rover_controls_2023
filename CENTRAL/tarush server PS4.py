import pygame
import socket

# Initialize Pygame and the controller
pygame.init()
pygame.joystick.init()
if pygame.joystick.get_count() > 0:
    controller = pygame.joystick.Joystick(0)
    controller.init()

# Create a socket object
s = socket.socket()

# Bind the socket to a local host and port
s.bind(('localhost', 8000))

# Start listening for incoming connections
s.listen()

# Accept an incoming connection
conn, addr = s.accept()

# Send the controller data to the client
while True:
    for event in pygame.event.get():
        if event.type == pygame.JOYAXISMOTION:
            # Get the axis data for the event
            axis = event.axis
            value = event.value
            # Send the data to the client
            conn.send(f"axis {axis} {value}".encode())
        elif event.type == pygame.JOYBUTTONDOWN:
            # Get the button data for the event
            button = event.button
            # Send the data to the client
            conn.send(f"button {button}".encode())
