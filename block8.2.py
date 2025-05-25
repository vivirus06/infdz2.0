def Public(*args): return args[0] # Нет изменений
def Private(*args):
    if not __debug__:  # Если флаг -O указан
        return args[0]

    def onDecorator(aClass):
        class wrapper:
            def __init__(self, *args, **kwargs):
                self._wrapped = aClass(*args, **kwargs)
            def __getattr__(self, name):
                print('Trace:', name)  # Added trace
                if name.startswith('_'):
                    raise AttributeError('private attribute fetch: ' + name)
                else:
                    return getattr(self._wrapped, name)
        return wrapper
    return onDecorator

# Тестирование
if __name__ == '__main__':
    @Private()
    class C:
        def __init__(self, x, y):
            self.a = x
            self._b = y

        def m(self):
            pass

    x = C(1, 2) # Создание экземпляра класса
    print(x.a)
    try:
        x._b
    except AttributeError as e:
        print(e)
    x.m()
