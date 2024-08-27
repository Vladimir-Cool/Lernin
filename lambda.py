

l = ["один", "Три", 9, "пять", 4, "десять"]

def test_arg(*args):
    string = [i for i in args[0] if type(i) is str]
    print(string)
    print(args)

test_arg(l)
