from command import Command, NoCommand


class RemoteContyol:
    """Контролер с 7-ю кнопками"""

    on_commands: list[Command]
    off_commands: list[Command]
    undo_command: Command

    def __init__(self):
        self.on_commands = list()
        self.off_commands = list()
        empty_command = NoCommand()
        for i in range(7):
            self.on_commands.append(empty_command)
            self.off_commands.append(empty_command)
        self.undo_command = empty_command

    def set_command(self, slot: int, on_command: Command, off_command: Command):
        self.on_commands[slot] = on_command
        self.off_commands[slot] = off_command

    def on_button_was_pushed(self, slot: int):
        self.on_commands[slot].execute()
        self.undo_command = self.on_commands[slot]

    def off_button_was_pushed(self, slot: int):
        self.off_commands[slot].execute()
        self.undo_command = self.off_commands[slot]

    def undo_button_was_pushed(self):
        self.undo_command.undo()

    def __str__(self):
        result_srt = "\n-----Remote Control-----\n"
        for i in range(7):
            result_srt += f"[slot {i} | {self.on_commands[i].__class__.__name__} | {self.off_commands[i].__class__.__name__}]\n"
        result_srt += f"[undo   | {self.undo_command.__class__.__name__}]"
        return result_srt


class SimpleRemoteControl:
    """Тест контроллера"""

    slot: Command

    def __init__(self):
        pass

    def set_command(self, command: Command):
        self.slot = command

    def button_was_pressed(self):
        self.slot.execute()
