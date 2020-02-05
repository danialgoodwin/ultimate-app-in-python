from tkinter import *


def start():
    print('start()')
    root = Tk('Ultimate App')
    text = Text(root)
    text.grid()
    root.mainloop()


def main():
    print('main()')
    start()


if __name__ == '__main__':
    main()
