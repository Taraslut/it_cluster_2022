def add(one=0, other=0, *args, **kwargs): #add(one, other, *args, third=1, forth=1,  **kwargs)
    print(f"args={args}")
    print(f"kwargs={kwargs}")
    rez = one + other
    for i in args:
        rez += i
    for key in kwargs:
        rez += kwargs[key]
    return rez


if __name__ == '__main__':
    print("=" * 100)
    total_rez = add()
    print(f"rez = {total_rez}")
    print("=" * 100)
    total_rez = add(100)
    print(f"rez = {total_rez}")

    print("=" * 100)
    total_rez = add(other=2, one=4)
    print(f"rez = {total_rez}")
    print("=" * 100)
    total_rez = add(one=2, other=4, third=6)
    print(f"rez = {total_rez}")
    print("=" * 100)
    total_rez = add(2, 4, 6, 10, 12, 12, 45, 67, 45)
    print(f"rez = {total_rez}")
