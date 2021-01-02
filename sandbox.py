def my_decorator(og_function):
    def wrap_fn():
        print('a bow')
        og_function()
        print('some tape')
    return wrap_fn


@my_decorator
def say_hello():
    print('hello!!!')


say_hello()
