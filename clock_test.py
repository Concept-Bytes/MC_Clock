import pygame
import sys
import numpy as np
from PIL import Image
from collections import Counter

# Configuration
IMAGE_PATH = 'mapped2.png'
WINDOW_SIZE = 1080
GRID_SIZE = 10
SCALING_FACTOR = 2.5
ANGLE_INCREMENT = 2  # Faster rotation

# Initialize pygame
pygame.init()

screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE), pygame.FULLSCREEN)
pygame.display.set_caption("Minecraft Clock Rotation - Time of Day Based")


# Load image with PIL
image = Image.open(IMAGE_PATH)

# Precompute parameters
cell_size = WINDOW_SIZE // GRID_SIZE
new_size = int(WINDOW_SIZE * SCALING_FACTOR)
angle = 0

# Scale the image once outside the main loop
scaled_image_bigger = image.resize((new_size, new_size), Image.NEAREST)

clock = pygame.time.Clock()
running = True

while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False

    # Create a black canvas
    canvas = np.zeros((WINDOW_SIZE, WINDOW_SIZE, 3), dtype=np.uint8)

    # Rotate the pre-scaled image
    rotated_image_bigger = scaled_image_bigger.rotate(angle)

    # Crop to 1080x1080
    left = (rotated_image_bigger.width - WINDOW_SIZE) / 2
    top = (rotated_image_bigger.height - WINDOW_SIZE) / 2
    right = (rotated_image_bigger.width + WINDOW_SIZE) / 2
    bottom = (rotated_image_bigger.height + WINDOW_SIZE) / 2
    cropped_image = rotated_image_bigger.crop((left, top, right, bottom))

    # Convert to numpy
    cropped_image_np = np.array(cropped_image)

    # Place the cropped image onto the canvas
    canvas[:cropped_image_np.shape[0], :cropped_image_np.shape[1]] = cropped_image_np

    # Resample by the most common color in each cell
    resampled_canvas = np.zeros_like(canvas)
    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            # Get cell boundaries
            start_row = row * cell_size
            end_row = start_row + cell_size
            start_col = col * cell_size
            end_col = start_col + cell_size

            # Extract the cell
            cell = canvas[start_row:end_row, start_col:end_col]

            # Find the most frequent color
            cell_flat = cell.reshape(-1, cell.shape[-1])
            most_common_color = Counter(map(tuple, cell_flat)).most_common(1)[0][0]

            # Fill the resampled canvas cell
            resampled_canvas[start_row:end_row, start_col:end_col] = most_common_color

    # Convert the resampled numpy array to a pygame surface
    surface = pygame.surfarray.make_surface(np.transpose(resampled_canvas, (1, 0, 2)))

    # Draw the image to the screen
    screen.blit(surface, (0,0))
    pygame.display.flip()

    # Update the angle (negative to reverse direction if needed)
    angle = (angle - ANGLE_INCREMENT) % 360

    # Attempt to run at ~60 FPS
    clock.tick(60)

pygame.quit()
sys.exit()

