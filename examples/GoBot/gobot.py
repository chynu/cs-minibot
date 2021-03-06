"""
GoBot Example
"""

from minibot.bot import Bot
from minibot.hardware.rpi.gpio import DigitalOutput, PWM
from minibot.interface.servo import Servo
from minibot.peripherals.hbridge import HBridge

class GoBot(Bot):
    """
    GoBot
    """
    def __init__(self):
        Bot.__init__(self, "GoBot")
        self.motors = HBridge(
            DigitalOutput(10),
            PWM(13),
            DigitalOutput(24),
            PWM(18)
        )
        self.motors.set_speed(0.5, 0.5)

    def run(self):
        pass

if __name__ == "__main__":
    bot = GoBot()
    while True:
        bot.run()
