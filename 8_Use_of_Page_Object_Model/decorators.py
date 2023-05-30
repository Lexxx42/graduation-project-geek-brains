# def print_hello():
#     print('hello')

def wrapper(func):
    print('i\'ll do the job')
    func()
    print('job done')


# wrapper(print_hello)

# i'll do the job
# hello
# job done


def decorator_function(func):
    wrapper(func)
    return wrapper


@decorator_function
def print_hello():
    print('hello')
