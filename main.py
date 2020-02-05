from tkinter import *
import tkinter.filedialog


text = None


def save():
    print('save()')
    global text
    t = text.get('1.0', 'end-1c')
    save_location = tkinter.filedialog.asksaveasfilename()
    with open(save_location, 'w+') as f:
        f.write(t)


def start():
    print('start()')
    global text
    root = Tk('Ultimate App')
    text = Text(root)
    text.grid()
    button = Button(root, text='Save', command=save)
    button.grid()
    root.mainloop()


def main():
    print('main()')
    start()


if __name__ == '__main__':
    main()
