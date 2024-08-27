from command import (
    LightOnCommand,
    LightOffCommand,
    DoorOpenCommand,
    DoorCloseCommand,
    StereoOnWithCDCommand,
    StereoOffWithCDCommand,
    FanOnCommand,
    FanOffCommand,
    FanHighSpeedCommand,
    FanMediumSpeedCommand,
    MacroCommand,
)
from device import Light, Door, Fan, Stereo
from control import SimpleRemoteControl, RemoteContyol

remote = SimpleRemoteControl()
light = Light("Свет на кухне")
light_on = LightOnCommand(light)
light_off = LightOffCommand(light)

door = Door("Дверь гоража")
door_open = DoorOpenCommand(door)
door_close = DoorCloseCommand(door)

stereo = Stereo("Стерео система")
stereo_on = StereoOnWithCDCommand(stereo)
stereo_off = StereoOffWithCDCommand(stereo)

fan = Fan("Вентилятор")
fan_on = FanOnCommand(fan)
fan_off = FanOffCommand(fan)
fan_high = FanHighSpeedCommand(fan)
fan_medium = FanMediumSpeedCommand(fan)

print("----------------------------")
remote.set_command(light_on)
remote.button_was_pressed()
remote.set_command(door_open)
remote.button_was_pressed()


remote2 = RemoteContyol()


remote2.set_command(0, stereo_on, stereo_off)
remote2.set_command(1, light_on, light_off)
remote2.set_command(2, door_open, door_close)
remote2.set_command(3, fan_on, fan_off)
remote2.set_command(4, fan_high, fan_medium)
print(remote2)

remote2.undo_button_was_pushed()

remote2.on_button_was_pushed(0)
remote2.undo_button_was_pushed()
remote2.on_button_was_pushed(1)
remote2.undo_button_was_pushed()
remote2.on_button_was_pushed(2)
remote2.undo_button_was_pushed()


print("---FAN---TEST---")

remote2.on_button_was_pushed(3)  # 2

remote2.on_button_was_pushed(4)  # 3
remote2.off_button_was_pushed(4)  # 2
remote2.undo_button_was_pushed()  # 3

remote2.off_button_was_pushed(4)  # 2
remote2.off_button_was_pushed(4)  # 2
remote2.undo_button_was_pushed()  # 3

print("---макрокоманды---")

party_on = (
    light_on,
    door_open,
    stereo_on,
    fan_on,
)
party_off = (
    light_off,
    door_close,
    stereo_off,
    fan_off,
)

party_on_command = MacroCommand(party_on)
party_off_command = MacroCommand(party_off)

remote2.set_command(6, party_on_command, party_off_command)
print(remote2)

remote2.on_button_was_pushed(6)
remote2.off_button_was_pushed(6)
