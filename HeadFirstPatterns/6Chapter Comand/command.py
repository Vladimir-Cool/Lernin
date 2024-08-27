from typing import Protocol, ClassVar, List, Tuple

from device import Light, Stereo, Door, Fan
from mixin import UndoFanMixin


class Command(Protocol):
    """База для команд"""

    def execute(self):
        pass

    def undo(self):
        pass


class NoCommand(Command):
    """Пустая команда"""

    def execute(self):
        print("Нет команды")

    def undo(self):
        print("Нет команды")


""" --------Light-----"""


class LightOnCommand(Command):
    light: Light

    def __init__(self, light: Light):
        self.light = light

    def execute(self):
        self.light.on()

    def undo(self):
        self.light.off()


class LightOffCommand(Command):
    light: Light

    def __init__(self, light: Light):
        self.light = light

    def execute(self):
        self.light.off()

    def undo(self):
        self.light.on()


""" --------Stereo-----"""


class StereoOnWithCDCommand(Command):
    """Команда включения стерео системы"""

    stereo: Stereo

    def __init__(self, stereo: Stereo):
        self.stereo = stereo

    def execute(self):
        self.stereo.on()
        self.stereo.set_cd()
        self.stereo.set_volume(11)

    def undo(self):
        self.stereo.off()


class StereoOffWithCDCommand(Command):
    """Команда отключения стерео системы"""

    stereo: Stereo

    def __init__(self, stereo: Stereo):
        self.stereo = stereo

    def execute(self):
        self.stereo.off()

    def undo(self):
        self.stereo.on()
        self.stereo.set_cd()
        self.stereo.set_volume(11)


""" --------Door-----"""


class DoorOpenCommand(Command):
    door: Door

    def __init__(self, door: Door):
        self.door = door

    def execute(self):
        self.door.open()

    def undo(self):
        self.door.close()


class DoorCloseCommand(Command):
    door: Door

    def __init__(self, door: Door):
        self.door = door

    def execute(self):
        self.door.close()

    def undo(self):
        self.door.open()


""" --------Fan-----"""


class FanOnCommand(UndoFanMixin, Command):
    fan: Fan

    def __init__(self, fan: Fan):
        self.fan = fan

    def execute(self):
        self.fan.on()


class FanHighSpeedCommand(UndoFanMixin, Command):
    fan: Fan
    prev_speed: int

    def __init__(self, fan: Fan):
        self.fan = fan
        self.prev_speed = fan.OFF

    def execute(self):
        if self.fan.get_speed() != self.fan.HIGH:
            self.prev_speed = self.fan.get_speed()
        self.fan.high()


class FanMediumSpeedCommand(UndoFanMixin, Command):
    fan: Fan
    prev_speed: int

    def __init__(self, fan: Fan):
        self.fan = fan
        self.prev_speed = fan.OFF

    def execute(self):
        if self.fan.get_speed() != self.fan.MEDIUM:
            self.prev_speed = self.fan.get_speed()

        self.fan.medium()


class FanOffCommand(Command):
    fan: Fan

    def __init__(self, fan: Fan):
        self.fan = fan

    def execute(self):
        self.fan.off()

    def undo(self):
        self.fan.on()


class MacroCommand(Command):
    commands: Tuple[Command]

    def __init__(self, commands: Tuple[Command]):
        self.commands = commands

    def execute(self):
        for com in self.commands:
            com.execute()
