import time

def timer(label='', trace=True):
    def timer_decorator(func):
        def timer_wrapper(*args, **kwargs):
            start = time.perf_counter()
            result = func(*args, **kwargs)
            end = time.perf_counter()
            elapsed = end - start
            timer_wrapper.alltime += elapsed  
            if trace:
                print(f"{label}: {func.__name__} took {elapsed:.5f} seconds")
            return result
        timer_wrapper.alltime = 0
        return timer_wrapper
    return timer_decorator

# Тестирование
if __name__ == '__main__':
    @timer(label='Module')
    def listcomp(N):  
        return [x * 2 for x in range(N)]

    @timer(label='Module')
    def mapcall(N):  
        return list(map(lambda x: x * 2, range(N)))

    result = listcomp(5)
    print(result)
    result = mapcall(5)
    print(result)
    print(f"listcomp alltime = {listcomp.alltime}")  
    print(f"mapcall alltime = {mapcall.alltime}")  

    class Spam:
        @timer(label='Class')
        def method(self, N):  
            return [x * 2 for x in range(N)]

    X = Spam()
    result = X.method(5)
    print(result)
    print(f"Spam.method alltime = {Spam.method.alltime}")
