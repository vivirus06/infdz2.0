def adder(good=None, bad=None, ugly=None):
    if good is None and bad is None and ugly is None:
        return None 

    result = good if good is not None else ""     if bad is not None:
        result += bad
    if ugly is not None:
        result += ugly
    return result

print(adder(good=1, bad=2, ugly=3))
print(adder(good="a", bad="b", ugly="c"))
print(adder(good=1, bad=2))
print(adder(ugly=3, good=1))
print(adder())


def adder_arbitrary(**kwargs):
    result = ""
    for key, value in kwargs.items():
        result += str(value)  
    return result

print(adder_arbitrary(a=1, b=2, c=3))
print(adder_arbitrary(x="hello", y="world"))
