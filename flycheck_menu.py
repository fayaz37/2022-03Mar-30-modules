def menu(*args):                # all arguments will be put in the tuple, "args"
    while True:
        s = input(f'Enter choice (): ').strip()
        if s in args:               # is s a valid response? If so, return it
            return s

        print(f'Invalid choice {s}')
