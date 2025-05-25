def countLines(name):
    with open(name, 'r') as file:
        return len(file.readlines())

def countChars(name):
    with open(name, 'r') as file:
        return len(file.read())

def test(name):
    lines = countLines(name)
    chars = countChars(name)
    print(f"Lines: {lines}, Characters: {chars}")

if __name__ == "__main__":
    test("mymod.py")
