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


def select_font_arial():
    global text
    text.config(font='Arial')


def select_font_monospace():
    global text
    # text.config(font='Mono')
    text.config(font='JetBrainsMono')


def start():
    print('start()')
    global text
    root = Tk('Ultimate App')
    text = Text(root)
    text.grid()
    button = Button(root, text='Save', command=save)
    button.grid()
    font_view = Menubutton(root, text='Font')
    font_view.grid()
    font_view.menu = Menu(font_view, tearoff=0)
    font_view['menu'] = font_view.menu
    arial = IntVar()
    monospace = IntVar()
    font_view.menu.add_checkbutton(label='Arial', variable=arial, command=select_font_arial())
    font_view.menu.add_checkbutton(label='Monospace', variable=monospace, command=select_font_monospace())
    root.mainloop()


def main():
    print('main()')
    start()


if __name__ == '__main__':
    main()
