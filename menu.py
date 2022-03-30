def menu(*args):                # all arguments will be put in the tuple, "args"
    while True:
        s = input(f'Enter choice {args}: ').strip()
        if s in args:               # is s a valid response? If so, return it
            return s

        print(f'Invalid choice {s}')


if __name__ == '__main__':
    user_choice = menu('a', 'b', 'c')
    print(f'You chose {user_choice}')
