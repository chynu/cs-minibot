"""
Color Sensor for the MiniBot.
"""

import logging
from minibot.utils import Utils
import Adafruit_TCS34725 as CSensor

# Abstract class representing a sensor
class ColorSensor():
    """
    Color Sensor class.
    """
    def __init__(self, name):
        """
        Constructor.
        :param name: Name of sensor.
        """
        self.name = name
        self.pin_number = pin_number
        self.color_sensor = CSensor()
        self.colors = {
            "RED": (171, 76, 78),
            "BLUE": (86, 161, 194),
            "GREEN": (98, 210, 173),
            "YELLOW": (210, 203, 100),
            "VIOLET": (142, 140, 160),
            "WHITE": (344, 450, 372)
            # "PINK":(195,157,156),
            # "ORANGE":(140,83,51)
        }
        logging.warning("Sensor being registered: " + str(self.name))

    def get_name(self):
        """
        Gets name of sensor.
        """
        return self.name

    def calibrate(self):
        """
        Calibrates colors. Takes 100 inputs per color, stores normalized average.
        """

        """ UPDATE: calibrate() no longer actually calibrates sensors. Method name is kept in case we
        do need calibration in the future. As of now, calibrate() normalizes the vectors during ColorSensor
        initialization. """

        #         print "================== COLOR CALIBRATION =================="
        #         print """Before color-sensing, we must calibrate the colors. Please place
        # the corresponding color under the color sensor at recommended distance
        # (with wheels touching the ground) before pressing enter."""

        #         for color in self.colors:
        #             if len(raw_input("\nPlease place the " +color.lower() + " mat under the sensor and press enter."))>-1:
        #                 self.colors[color] = normalize(self.super_read(100))
        #                 time.sleep(0.01)
        #                 print "Calibrated!"

        #         print "Thank you! All of the colors have been calibrated.\n"

        for c in self.colors:
            self.colors[c] = Utils.normalize(self.colors[c])

    def super_read(self, n):
        """
        Reads from the color sensor n times, and returns the non-normalized average.
        """
        color_data = {"R":0,"G":0,"B":0}
        for i in range(n):
            read = self.read()
            color_data["R"] += read[0]
            color_data["G"] += read[1]
            color_data["B"] += read[2]
        color_data["R"] = color_data["R"]/n
        color_data["G"] = color_data["G"]/n
        color_data["B"] = color_data["B"]/n
        return color_data["R"], color_data["G"], color_data["B"]

    def read(self):
        """
        Returns a NON-NORMALIZED 3-tuple of RGB value.
        """
        rd = self.color_sensor.get_raw_data()
        return rd[0], rd[1], rd[2]

    def read_color_name(self):
        """
        Returns string of color name.
        """
        color_guess = ("", 99999999999999999999999999)  # tuple of (color, distance from color to input)
        color_actual = Utils.normalize(self.read())
        for c in self.colors:
            dist = Utils.distance(self.colors[c], color_actual)
            if (dist < color_guess[1]):
                color_guess = (c, dist)
        return color_guess[0]