import pygame
import sys

# Initialize pygame
pygame.init()

# Set up the window
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Cursor Tracker")

# Open a file for writing cursor data
output_file = open("D:\suchaklutch\Dr.Constantinidis-PythonDS-Unity-Integration-Demo\DrConstantinidisExample\cursor_data.txt", "w")

# Main loop
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get the cursor's position
    x, y = pygame.mouse.get_pos()

    # Write the coordinates to the file
    output_file.seek(0)  # Reset file position to overwrite
    output_file.write(f"{x},{y}\n")
    output_file.flush()  # Ensure data is written immediately

    # Fill the screen with a color (optional, for visualization)
    screen.fill((30, 30, 30))

    # Draw a small circle where the cursor is (optional, for visualization)
    pygame.draw.circle(screen, (255, 0, 0), (x, y), 5)

    # Update the display
    pygame.display.flip()

# Clean up
output_file.close()
pygame.quit()
sys.exit()
