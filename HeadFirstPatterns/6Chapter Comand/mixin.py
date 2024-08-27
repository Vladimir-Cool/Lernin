class UndoFanMixin:
    """Реализация метода undo() для класса вентиляторы"""

    def undo(self):
        if self.prev_speed == self.fan.HIGH:
            self.prev_speed = self.fan.get_speed()
            self.fan.high()

        elif self.prev_speed == self.fan.MEDIUM:
            self.prev_speed = self.fan.get_speed()
            self.fan.medium()

        elif self.prev_speed == self.fan.LOW:
            self.prev_speed = self.fan.get_speed()
            self.fan.low()

        elif self.prev_speed == self.fan.OFF:
            self.prev_speed = self.fan.get_speed()
            self.fan.off()
