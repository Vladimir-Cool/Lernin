class Sytki:
    name: str
    time_metric: str

    day: int = 1

    def __init__(self, name: str, time_metric: str):
        self.name = name
        self.time_metric = time_metric

    @property
    def length(self):
        if self.time_metric == "hours":
            return f"{self.day * 24} {self.time_metric}"


day = Sytki("Monday", "hours")
x = day.length
print(x)
