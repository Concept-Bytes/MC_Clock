# MC_Clock
This project turns your Raspberry Pi 5 into a functional Minecraft-themed clock. It utilizes a 5-inch round display, Pygame, and Python libraries to create a visual clock that rotates the iconic Minecraft clock image based on the current time of day.

# Features

* Real-Time Clock: The clock displays the current time in a 12-hour format, where noon (12:00 PM) corresponds to 0 degrees, and midnight (12:00 AM) corresponds to 180 degrees.

* Custom Image Mapping: Uses the Minecraft clock image (mapped2.png), which rotates smoothly to reflect the current time.

* Grid-Based Resampling: The image is divided into a 10x10 grid, and each grid cell's color is resampled based on the most common color in that region.

* Debug Mode: Allows for easy development and testing by setting custom time values.

# Hardware Requirements

* Raspberry Pi 5

* 5-inch Round Display (linked in the build guide)

# Software Requirements

* Raspberry Pi OS (or a compatible Linux distribution)

* python 3.x

* Required Libraries:
  * pygame
  * Pillow
  * numpy

# Installation

Clone the Repository:

``` git clone https://github.com/Concept-Bytes/MC_Clock ```


# Controls

ESC or Q: Exit the application

# License
Distributed under the MIT License. See LICENSE for more information.

# Contact
Reach out with any feedback or support needs via GitHub or email.
