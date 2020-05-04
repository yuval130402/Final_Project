#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 4.26
#  in conjunction with Tcl version 8.6
#    Apr 09, 2020 11:46:25 PM +0300  platform: Windows NT

import sys

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

from PIL import Image, ImageTk

import gui_project_support
import os.path

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    global prog_location
    prog_call = sys.argv[0]
    prog_location = os.path.split(prog_call)[0]
    root = tk.Tk()
    top = Toplevel1 (root)
    gui_project_support.init(root, top)
    root.mainloop()

w = None
def create_Toplevel1(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    global prog_location
    prog_call = sys.argv[0]
    prog_location = os.path.split(prog_call)[0]
    rt = root
    w = tk.Toplevel (root)
    top = Toplevel1 (w)
    gui_project_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Toplevel1():
    global w
    w.destroy()
    w = None

class Toplevel1:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        font9 = "-family Calibri -size 14 -weight bold -slant roman "  \
            "-underline 0 -overstrike 0"
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

        top.geometry("973x754+447+116")
        top.minsize(148, 1)
        top.maxsize(1924, 1055)
        top.resizable(1, 1)
        top.title("ControlNet")
        top.configure(background="#70b8b8")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.Frame_Features = tk.Frame(top)
        self.Frame_Features.place(relx=0.01, rely=0.013, relheight=0.975
                , relwidth=0.982)
        self.Frame_Features.configure(relief='ridge')
        self.Frame_Features.configure(borderwidth="2")
        self.Frame_Features.configure(relief="ridge")
        self.Frame_Features.configure(background="#d9d9d9")
        self.Frame_Features.configure(highlightbackground="#d9d9d9")
        self.Frame_Features.configure(highlightcolor="black")

        self.Lock_Button = tk.Button(self.Frame_Features)
        self.Lock_Button.place(relx=0.01, rely=0.014, height=160, width=160)
        self.Lock_Button.configure(activebackground="#ececec")
        self.Lock_Button.configure(activeforeground="#000000")
        self.Lock_Button.configure(background="#d9d9d9")
        self.Lock_Button.configure(cursor="hand2")
        self.Lock_Button.configure(disabledforeground="#a3a3a3")
        self.Lock_Button.configure(foreground="#000000")
        self.Lock_Button.configure(highlightbackground="#d9d9d9")
        self.Lock_Button.configure(highlightcolor="black")
        photo_location = os.path.join(prog_location,"../images/Lock2.jpg")
        global _img0
        _img0 = ImageTk.PhotoImage(file=photo_location)
        self.Lock_Button.configure(image=_img0)
        self.Lock_Button.configure(pady="0")
        self.Lock_Button.bind('<Button-1>',lambda e:gui_project_support.lock_button(e))

        self.Unlock_button = tk.Button(self.Frame_Features)
        self.Unlock_button.place(relx=0.01, rely=0.259, height=160, width=160)
        self.Unlock_button.configure(activebackground="#ececec")
        self.Unlock_button.configure(activeforeground="#000000")
        self.Unlock_button.configure(background="#d9d9d9")
        self.Unlock_button.configure(cursor="hand2")
        self.Unlock_button.configure(disabledforeground="#a3a3a3")
        self.Unlock_button.configure(foreground="#000000")
        self.Unlock_button.configure(highlightbackground="#d9d9d9")
        self.Unlock_button.configure(highlightcolor="black")
        photo_location = os.path.join(prog_location,"../images/Unlock1.jpg")
        global _img1
        _img1 = ImageTk.PhotoImage(file=photo_location)
        self.Unlock_button.configure(image=_img1)
        self.Unlock_button.configure(pady="0")
        self.Unlock_button.bind('<Button-1>',lambda e:gui_project_support.unlock_button(e))

        self.Start_Sharing = tk.Button(self.Frame_Features)
        self.Start_Sharing.place(relx=0.199, rely=0.014, height=160, width=160)
        self.Start_Sharing.configure(activebackground="#ececec")
        self.Start_Sharing.configure(activeforeground="#000000")
        self.Start_Sharing.configure(background="#d9d9d9")
        self.Start_Sharing.configure(cursor="hand2")
        self.Start_Sharing.configure(disabledforeground="#a3a3a3")
        self.Start_Sharing.configure(foreground="#000000")
        self.Start_Sharing.configure(highlightbackground="#d9d9d9")
        self.Start_Sharing.configure(highlightcolor="black")
        photo_location = os.path.join(prog_location,"../images/start_transfer.png")
        global _img2
        _img2 = tk.PhotoImage(file=photo_location)
        self.Start_Sharing.configure(image=_img2)
        self.Start_Sharing.configure(pady="0")
        self.Start_Sharing.bind('<Button-1>',lambda e:gui_project_support.start_share_screen(e))

        self.Stop_Sharing = tk.Button(self.Frame_Features)
        self.Stop_Sharing.place(relx=0.199, rely=0.259, height=160, width=160)
        self.Stop_Sharing.configure(activebackground="#ececec")
        self.Stop_Sharing.configure(activeforeground="#000000")
        self.Stop_Sharing.configure(background="#d9d9d9")
        self.Stop_Sharing.configure(cursor="hand2")
        self.Stop_Sharing.configure(disabledforeground="#a3a3a3")
        self.Stop_Sharing.configure(foreground="#000000")
        self.Stop_Sharing.configure(highlightbackground="#d9d9d9")
        self.Stop_Sharing.configure(highlightcolor="black")
        photo_location = os.path.join(prog_location,"../images/stop_transfer.png")
        global _img3
        _img3 = tk.PhotoImage(file=photo_location)
        self.Stop_Sharing.configure(image=_img3)
        self.Stop_Sharing.configure(pady="0")
        self.Stop_Sharing.bind('<Button-1>',lambda e:gui_project_support.stop_share_screen(e))

        self.TurnOn_Button = tk.Button(self.Frame_Features)
        self.TurnOn_Button.place(relx=0.387, rely=0.014, height=160, width=160)
        self.TurnOn_Button.configure(activebackground="#ececec")
        self.TurnOn_Button.configure(activeforeground="#000000")
        self.TurnOn_Button.configure(background="#d9d9d9")
        self.TurnOn_Button.configure(cursor="hand2")
        self.TurnOn_Button.configure(disabledforeground="#a3a3a3")
        self.TurnOn_Button.configure(foreground="#000000")
        self.TurnOn_Button.configure(highlightbackground="#d9d9d9")
        self.TurnOn_Button.configure(highlightcolor="black")
        photo_location = os.path.join(prog_location,"../images/turn_on1.png")
        global _img4
        _img4 = tk.PhotoImage(file=photo_location)
        self.TurnOn_Button.configure(image=_img4)
        self.TurnOn_Button.configure(pady="0")
        self.TurnOn_Button.bind('<Button-1>',lambda e:gui_project_support.turn_on(e))

        self.TurnOff_Button = tk.Button(self.Frame_Features)
        self.TurnOff_Button.place(relx=0.387, rely=0.259, height=160, width=160)
        self.TurnOff_Button.configure(activebackground="#ececec")
        self.TurnOff_Button.configure(activeforeground="#000000")
        self.TurnOff_Button.configure(background="#d9d9d9")
        self.TurnOff_Button.configure(cursor="hand2")
        self.TurnOff_Button.configure(disabledforeground="#a3a3a3")
        self.TurnOff_Button.configure(foreground="#000000")
        self.TurnOff_Button.configure(highlightbackground="#d9d9d9")
        self.TurnOff_Button.configure(highlightcolor="black")
        photo_location = os.path.join(prog_location,"../images/turn_off1.png")
        global _img5
        _img5 = tk.PhotoImage(file=photo_location)
        self.TurnOff_Button.configure(image=_img5)
        self.TurnOff_Button.configure(pady="0")
        self.TurnOff_Button.bind('<Button-1>',lambda e:gui_project_support.turn_off(e))

        self.SendFile_Button = tk.Button(self.Frame_Features)
        self.SendFile_Button.place(relx=0.576, rely=0.014, height=160, width=160)

        self.SendFile_Button.configure(activebackground="#ececec")
        self.SendFile_Button.configure(activeforeground="#000000")
        self.SendFile_Button.configure(background="#d9d9d9")
        self.SendFile_Button.configure(cursor="hand2")
        self.SendFile_Button.configure(disabledforeground="#a3a3a3")
        self.SendFile_Button.configure(foreground="#000000")
        self.SendFile_Button.configure(highlightbackground="#d9d9d9")
        self.SendFile_Button.configure(highlightcolor="black")
        photo_location = os.path.join(prog_location,"../images/send_file.png")
        global _img6
        _img6 = tk.PhotoImage(file=photo_location)
        self.SendFile_Button.configure(image=_img6)
        self.SendFile_Button.configure(pady="0")
        self.SendFile_Button.bind('<Button-1>',lambda e:gui_project_support.send_file(e))

        self.WatchScreen_Button = tk.Button(self.Frame_Features)
        self.WatchScreen_Button.place(relx=0.576, rely=0.259, height=160
                , width=160)
        self.WatchScreen_Button.configure(activebackground="#ececec")
        self.WatchScreen_Button.configure(activeforeground="#000000")
        self.WatchScreen_Button.configure(background="#d9d9d9")
        self.WatchScreen_Button.configure(cursor="hand2")
        self.WatchScreen_Button.configure(disabledforeground="#a3a3a3")
        self.WatchScreen_Button.configure(foreground="#000000")
        self.WatchScreen_Button.configure(highlightbackground="#d9d9d9")
        self.WatchScreen_Button.configure(highlightcolor="black")
        photo_location = os.path.join(prog_location,"../images/watch_screen.png")
        global _img7
        _img7 = tk.PhotoImage(file=photo_location)
        self.WatchScreen_Button.configure(image=_img7)
        self.WatchScreen_Button.configure(pady="0")
        self.WatchScreen_Button.bind('<Button-1>',lambda e:gui_project_support.watch_client(e))

        self.Clients_List = ScrolledListBox(self.Frame_Features)
        self.Clients_List.place(relx=0.01, rely=0.49, relheight=0.499
                , relwidth=0.487)
        self.Clients_List.configure(background="#ffffbd")
        self.Clients_List.configure(disabledforeground="#a3a3a3")
        self.Clients_List.configure(font=font9)
        self.Clients_List.configure(foreground="#0080ff")
        self.Clients_List.configure(highlightbackground="#d9d9d9")
        self.Clients_List.configure(highlightcolor="#d9d9d9")
        self.Clients_List.configure(selectbackground="#ffff0b")
        self.Clients_List.configure(selectforeground="#0000a0")
        self.Clients_List.configure(selectmode='multiple')

        self.Select_All = tk.Button(self.Frame_Features)
        self.Select_All.place(relx=0.524, rely=0.531, height=53, width=196)
        self.Select_All.configure(activebackground="#ececec")
        self.Select_All.configure(activeforeground="#000000")
        self.Select_All.configure(background="#83b4fc")
        self.Select_All.configure(cursor="hand2")
        self.Select_All.configure(disabledforeground="#a3a3a3")
        self.Select_All.configure(font="-family {Segoe UI} -size 10 -weight bold")
        self.Select_All.configure(foreground="#000080")
        self.Select_All.configure(highlightbackground="#d9d9d9")
        self.Select_All.configure(highlightcolor="black")
        self.Select_All.configure(pady="0")
        self.Select_All.configure(text='''Select All Clients''')
        self.Select_All.bind('<Button-1>',lambda e:gui_project_support.select_all_clients(e))

        self.Clear_Selection = tk.Button(self.Frame_Features)
        self.Clear_Selection.place(relx=0.524, rely=0.639, height=53, width=196)
        self.Clear_Selection.configure(activebackground="#ececec")
        self.Clear_Selection.configure(activeforeground="#000000")
        self.Clear_Selection.configure(background="#83b4fc")
        self.Clear_Selection.configure(cursor="hand2")
        self.Clear_Selection.configure(disabledforeground="#a3a3a3")
        self.Clear_Selection.configure(font="-family {Segoe UI} -size 10 -weight bold")
        self.Clear_Selection.configure(foreground="#000080")
        self.Clear_Selection.configure(highlightbackground="#d9d9d9")
        self.Clear_Selection.configure(highlightcolor="black")
        self.Clear_Selection.configure(pady="0")
        self.Clear_Selection.configure(text='''Clear Selection''')
        self.Clear_Selection.bind('<Button-1>',lambda e:gui_project_support.clear_selection_listbox(e))

# The following code is added to facilitate the Scrolled widgets you specified.
class AutoScroll(object):
    '''Configure the scrollbars for a widget.'''

    def __init__(self, master):
        #  Rozen. Added the try-except clauses so that this class
        #  could be used for scrolled entry widget for which vertical
        #  scrolling is not supported. 5/7/14.
        try:
            vsb = ttk.Scrollbar(master, orient='vertical', command=self.yview)
        except:
            pass
        hsb = ttk.Scrollbar(master, orient='horizontal', command=self.xview)

        #self.configure(yscrollcommand=_autoscroll(vsb),
        #    xscrollcommand=_autoscroll(hsb))
        try:
            self.configure(yscrollcommand=self._autoscroll(vsb))
        except:
            pass
        self.configure(xscrollcommand=self._autoscroll(hsb))

        self.grid(column=0, row=0, sticky='nsew')
        try:
            vsb.grid(column=1, row=0, sticky='ns')
        except:
            pass
        hsb.grid(column=0, row=1, sticky='ew')

        master.grid_columnconfigure(0, weight=1)
        master.grid_rowconfigure(0, weight=1)

        # Copy geometry methods of master  (taken from ScrolledText.py)
        if py3:
            methods = tk.Pack.__dict__.keys() | tk.Grid.__dict__.keys() \
                  | tk.Place.__dict__.keys()
        else:
            methods = tk.Pack.__dict__.keys() + tk.Grid.__dict__.keys() \
                  + tk.Place.__dict__.keys()

        for meth in methods:
            if meth[0] != '_' and meth not in ('config', 'configure'):
                setattr(self, meth, getattr(master, meth))

    @staticmethod
    def _autoscroll(sbar):
        '''Hide and show scrollbar as needed.'''
        def wrapped(first, last):
            first, last = float(first), float(last)
            if first <= 0 and last >= 1:
                sbar.grid_remove()
            else:
                sbar.grid()
            sbar.set(first, last)
        return wrapped

    def __str__(self):
        return str(self.master)

def _create_container(func):
    '''Creates a ttk Frame with a given master, and use this new frame to
    place the scrollbars and the widget.'''
    def wrapped(cls, master, **kw):
        container = ttk.Frame(master)
        container.bind('<Enter>', lambda e: _bound_to_mousewheel(e, container))
        container.bind('<Leave>', lambda e: _unbound_to_mousewheel(e, container))
        return func(cls, container, **kw)
    return wrapped

class ScrolledListBox(AutoScroll, tk.Listbox):
    '''A standard Tkinter Listbox widget with scrollbars that will
    automatically show/hide as needed.'''
    @_create_container
    def __init__(self, master, **kw):
        tk.Listbox.__init__(self, master, **kw)
        AutoScroll.__init__(self, master)
    def size_(self):
        sz = tk.Listbox.size(self)
        return sz

import platform
def _bound_to_mousewheel(event, widget):
    child = widget.winfo_children()[0]
    if platform.system() == 'Windows' or platform.system() == 'Darwin':
        child.bind_all('<MouseWheel>', lambda e: _on_mousewheel(e, child))
        child.bind_all('<Shift-MouseWheel>', lambda e: _on_shiftmouse(e, child))
    else:
        child.bind_all('<Button-4>', lambda e: _on_mousewheel(e, child))
        child.bind_all('<Button-5>', lambda e: _on_mousewheel(e, child))
        child.bind_all('<Shift-Button-4>', lambda e: _on_shiftmouse(e, child))
        child.bind_all('<Shift-Button-5>', lambda e: _on_shiftmouse(e, child))

def _unbound_to_mousewheel(event, widget):
    if platform.system() == 'Windows' or platform.system() == 'Darwin':
        widget.unbind_all('<MouseWheel>')
        widget.unbind_all('<Shift-MouseWheel>')
    else:
        widget.unbind_all('<Button-4>')
        widget.unbind_all('<Button-5>')
        widget.unbind_all('<Shift-Button-4>')
        widget.unbind_all('<Shift-Button-5>')

def _on_mousewheel(event, widget):
    if platform.system() == 'Windows':
        widget.yview_scroll(-1*int(event.delta/120),'units')
    elif platform.system() == 'Darwin':
        widget.yview_scroll(-1*int(event.delta),'units')
    else:
        if event.num == 4:
            widget.yview_scroll(-1, 'units')
        elif event.num == 5:
            widget.yview_scroll(1, 'units')

def _on_shiftmouse(event, widget):
    if platform.system() == 'Windows':
        widget.xview_scroll(-1*int(event.delta/120), 'units')
    elif platform.system() == 'Darwin':
        widget.xview_scroll(-1*int(event.delta), 'units')
    else:
        if event.num == 4:
            widget.xview_scroll(-1, 'units')
        elif event.num == 5:
            widget.xview_scroll(1, 'units')

if __name__ == '__main__':
    vp_start_gui()





