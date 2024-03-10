from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


# Function to initialize OpenGL
def init():
    glClearColor(1.0, 1.0, 1.0, 1.0)  # Set the background color to white
    gluOrtho2D(0, 8, 0, 8)  # Set the orthographic viewing volume


# Function to draw the chessboard
def drawChessboard():
    # Loop through the rows and columns to draw squares
    for i in range(8):
        for j in range(8):
            # Alternate between brown and white colors
            if (i + j) % 2 == 0:
                glColor3f(1.0, 1.0, 0.0)  # yellow color
            else:
                glColor3f(0.0, 0.0, 1.0)  # blue color
            # Draw a square at each cell of the chessboard
            glBegin(GL_QUADS)
            glVertex2i(i, j)
            glVertex2i(i + 1, j)
            glVertex2i(i + 1, j + 1)
            glVertex2i(i, j + 1)
            glEnd()


# Function to display content on the screen
def display():
    glClear(GL_COLOR_BUFFER_BIT)  # Clear the color buffer
    drawChessboard()  # Draw the chessboard
    glFlush()  # Flush OpenGL buffer


# Main function
def main():
    print(bool(glutInit))
     # Initialize GLUT
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)  # Set display mode
    glutInitWindowSize(800, 800)  # Set window size
    glutInitWindowPosition(100, 100)  # Set window position
    glutCreateWindow(b"Chessboard")  # Create window with title
    glutDisplayFunc(display)  # Register display function
    init()  # Call initialization function
    glutMainLoop()  # Enter the event-processing loop


if __name__ == "__main__":
    main()
