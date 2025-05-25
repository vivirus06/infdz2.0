
def countLines(name):
    """Counts the number of lines in a file."""
    with open(name, 'r') as file:
        return len(file.readlines())

def countChars(name):
    """Counts the number of characters in a file."""
    with open(name, 'r') as file:
        return len(file.read())

def test(name):
    """Tests the countLines and countChars functions with a given file."""
    lines = countLines(name)
    chars = countChars(name)
    print(f"Lines: {lines}, Characters: {chars}")


# Чтобы улучшить, можно передать объект открытого файла:
def countLines_improved(file):
    """Counts the number of lines in an already opened file."""
    return len(file.readlines())

def countChars_improved(file):
    """Counts the number of characters in an already opened file."""
    return len(file.read())


def test_improved(name):
    """Tests the countLines and countChars functions with a given file,
    passing the file object.
    """
    with open(name, 'r') as file:
        lines = countLines_improved(file)
        file.seek(0) # Возврат в начало файла
        chars = countChars_improved(file)
        print(f"Lines: {lines}, Characters: {chars}")


# Тестирование (в интерактивном сеансе):
# import mymod
# mymod.test("mymod.py") # Или mymod.test_improved("mymod.py")
