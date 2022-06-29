import datetime


def time_track(foo):
    def wrapper_foo(*args, **kwargs):
        # start timer
        start = datetime.datetime.now()
        rez = foo(*args, **kwargs)
        # finish timer
        finish = datetime.datetime.now()
        print(f"call {foo.__name__} lasts {finish - start}sec.")
        return rez

    return wrapper_foo


def info_decorator(f_name):
    def inner(*args, **kwargs):
        print("=" * 100)
        print(f"Call {f_name.__name__}")
        print(f"with params {args}, {kwargs}")
        rez = f_name(*args, **kwargs)
        print(f"The rezult of function is =>> {rez}")
        return rez

    return inner


@info_decorator
@time_track
def foo(name=None):
    if name:
        return f"Hello {name}"
    return "Hello Unknown user"


@info_decorator
@time_track
def add(a, b):
    return a + b


def send_sms(foo):
    def inner(*args, **kwargs):
        # send user sms
        print(f"send sms to {kwargs.get('user')}")
        return foo(*args, **kwargs)

    return inner


@send_sms
@info_decorator

def send_email(user, text):
    print(f"send Email to {user}")
    return user


# send_email = send_sms(info_decor)(send_email)


# foo = info_decor(foo)


if __name__ == '__main__':
    # print(foo())
    print(foo("Ivan"))
    #
    print(add(2, 4))

    send_email(user="Ivan", text="Activate account")
