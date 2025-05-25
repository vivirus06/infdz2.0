def adder(*args):
    if not args:
        return 0  

    first = args[0]
    for arg in args[1:]:
        first += arg
    return first


print(adder(1, 2, 3))
print(adder("a", "b", "c", "d"))
print(adder([1], [2, 3], [4, 5, 6]))
print(adder()) 


result = adder(1, 2, 3)
print(type(result))

result = adder("a", "b")
print(type(result))
