import os

os.environ.setdefault("TEST", "42")
print(os.environ["TEST"])

os.environ.pop("TEST")

print(os.environ)
