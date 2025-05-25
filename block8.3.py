def validator(**argvalidators):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for argname, validator in argvalidators.items():
                # Получаем значение аргумента
                if argname in kwargs:
                    argvalue = kwargs[argname]
                elif len(args) > list(func.__code__.co_varnames).index(argname):
                    argvalue = args[list(func.__code__.co_varnames).index(argname)]
                else:
                    raise ValueError(f"Argument {argname} not found")

                # Проверяем аргумент
                if not validator(argvalue):
                    raise ValueError(f"Invalid value for argument {argname}: {argvalue}")
            return func(*args, **kwargs)
        return wrapper
    return decorator

#Примеры валидаторов:
def is_positive(x):
    return x > 0

def is_string(x):
    return isinstance(x, str)

def is_in_range(min_val, max_val):
    def validate(x):
        return min_val <= x <= max_val
    return validate

def is_type(expected_type):
    def validate(x):
        return isinstance(x, expected_type)
    return validate
#Тестирование:

@validator(age=is_positive, name=is_string)
def create_user(name, age):
    print(f"Creating user {name} with age {age}")
    return {"name": name, "age": age}

@validator(value=is_in_range(0, 100))
def set_value(value):
    print(f"Setting value to {value}")
    return value

@validator(data = is_type(list))
def process_data(data):
  print("Processing data: ", data)

# Пример использования
try:
    user = create_user(name="Alice", age=30)  # OK
    user = create_user(name="Bob", age=-5)  # ValueError: Invalid value for argument age: -5
except ValueError as e:
    print(e)

try:
    value = set_value(50)  # OK
    value = set_value(150)  # ValueError: Invalid value for argument value: 150
except ValueError as e:
    print(e)

try:
    process_data(data=[1,2,3])
    process_data(data="hello")
except ValueError as e:
    print(e)
