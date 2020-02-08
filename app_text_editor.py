#!/usr/bin/env python3

import logging
from tkinter import *
from tkinter import filedialog, messagebox


class TextEditor:
    def __init__(self, root):
        self.root = root
        self.root.title('Ultimate App')
        self.filename = None
        self.title = StringVar()
        self.status = StringVar()

        self.titlebar = Label(self.root, textvariable=self.title, bd=2, relief=GROOVE)
        self.titlebar.pack(side=TOP, fill=BOTH)
        self.set_title()

        self.statusbar = Label(self.root, textvariable=self.status, bd=2, relief=GROOVE)
        self.statusbar.pack(side=BOTTOM, fill=BOTH)
        self.status.set('Welcome to Ultimate App!')

        self.menubar = Menu(self.root, activebackground='skyblue')
        self.root.config(menu=self.menubar)

        self.filemenu = Menu(self.menubar, tearoff=0)
        self.filemenu.add_command(label='New', accelerator='Ctrl+N', command=self.newfile)
        self.filemenu.add_command(label='Open', accelerator='Ctrl+O', command=self.openfile)
        self.filemenu.add_command(label='Save', accelerator='Ctrl+S', command=self.savefile)
        self.filemenu.add_separator()
        self.filemenu.add_command(label='Quit', accelerator='Ctrl+Q', command=self.quit)
        self.menubar.add_cascade(label='File', menu=self.filemenu)
        self.helpmenu = Menu(self.menubar, tearoff=0)
        self.helpmenu.add_command(label='About', command=self.infoabout)
        self.menubar.add_cascade(label='Help', menu=self.helpmenu)

        scroll_y = Scrollbar(self.root, orient=VERTICAL)
        self.text_input_view = Text(self.root, yscrollcommand=scroll_y.set, state='normal', relief=GROOVE)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_y.config(command=self.text_input_view.yview)
        self.text_input_view.pack(fill=BOTH, expand=1)

        self.shortcuts()

    def set_title(self):
        if self.filename:
            self.title.set(self.filename)
        else:
            self.title.set('Untitled')

    def newfile(self, *args):
        self.text_input_view.delete('1.0', END)
        self.filename = None
        self.set_title()
        self.status.set('New file created')

    def openfile(self, *args):
        try:
            self.filename = filedialog.askopenfilename(
                title='Select file',
                filetypes=(('All Files', '*.*'), ('Text Files', '*.txt'), ('Python Files', '*.py'))
            )
            if self.filename:
                with open(self.filename) as f:
                    self.text_input_view.delete('1.0', END)
                    for line in f:
                        self.text_input_view.insert(END, line)
                    self.set_title()
                    self.status.set('Opened successfully')
        except Exception as e:
            messagebox.showerror('Exception', e)

    def savefile(self, *args):
        try:
            if self.filename:
                data = self.text_input_view.get('1.0', END)
                with open(self.filename, 'w') as f:
                    f.write(data)
                self.set_title()
                self.status.set('Saved successfully')
            else:
                self.saveasfile()
        except Exception as e:
            messagebox.showerror('Exception', e)

    def saveasfile(self, *args):
        try:
            untitledfile = filedialog.asksaveasfilename(
                title="Save file As",
                defaultextension=".txt",
                initialfile="Untitled.txt",
                filetypes=(("All Files", "*.*"), ("Text Files", "*.txt"), ("Python Files", "*.py"))
            )
            data = self.text_input_view.get("1.0", END)
            with open(untitledfile, "w") as f:
                f.write(data)
            self.filename = untitledfile
            self.set_title()
            self.status.set("Saved Successfully")
        except Exception as e:
            messagebox.showerror('Exception', e)

    def quit(self, *args):
        op = messagebox.askyesno('Warning', 'Your unsaved data may be lost!')
        if op > 0:
            self.root.destroy()
        else:
            return

    def infoabout(self):
        messagebox.showinfo('About Ultimate App', 'A simple everything app.\nCreate using Python.')

    def shortcuts(self):
        self.text_input_view.bind("<Control-n>", self.newfile)
        self.text_input_view.bind("<Control-o>", self.openfile)
        self.text_input_view.bind("<Control-s>", self.savefile)
        self.text_input_view.bind("<Control-a>", self.saveasfile)
        self.text_input_view.bind("<Control-q>", self.quit)
        # self.text_input_view.bind("<Control-x>",self.cut)
        # self.text_input_view.bind("<Control-c>",self.copy)
        # self.text_input_view.bind("<Control-v>",self.paste)
        # self.text_input_view.bind("<Control-u>",self.undo)


# =============================================
# =============================================


def on_quit():
    logging.debug('on_quit()')
    pass


def on_save(text: str, file: str = ''):
    if not file:
        pass
    with open(file, 'w') as f:
        f.write(text)


def on_open():
    pass


def on_cut():
    pass


def on_copy():
    pass


def on_paste():
    pass


def on_undo():
    pass


def on_redo():
    pass


def on_find():
    pass


def show():
    root = Tk()
    TextEditor(root)
    root.mainloop()


def main():
    show()


if __name__ == '__main__':
    main()
