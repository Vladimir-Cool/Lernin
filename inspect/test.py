import inspect


def example_function(a, b):
    c = a + b
    frame = inspect.currentframe()
    args = inspect.getargvalues(frame)
    print(f"Arguments: {args.args}")
    print(f"Locals: {args.locals}")


# example_function(1, 2)


def example_function():
    frame = inspect.currentframe()
    stack = inspect.getouterframes(frame)
    for record in stack:
        print(record.filename, record.lineno, record.function)


# example_function()


def example_function():
    frame = inspect.currentframe()
    print(frame)


example_function()
