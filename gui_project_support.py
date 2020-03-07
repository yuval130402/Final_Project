#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# Support module generated by PAGE version 4.26
#  in conjunction with Tcl version 8.6
#    Jan 19, 2020 05:02:54 PM +0200  platform: Windows NT
#    Feb 28, 2020 04:59:19 PM +0200  platform: Windows NT

import sys
import common
import threading
import time
from threading import Thread
import server_big_project
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

def lock_button(p1):
    common.selected_clients = selection_list()
    if len(common.selected_clients) != 0:
        common.conn_q.put("lock")
    # sys.stdout.flush()

def unlock_button(p1):
    common.selected_clients = selection_list()
    if len(common.selected_clients) != 0:
        common.conn_q.put("unlock")
    # sys.stdout.flush()

def start_share_screen(p1):
    common.selected_clients = selection_list()
    if len(common.selected_clients) != 0:
        common.conn_q.put("send_screen")
        common.picture_flag = 1
    # sys.stdout.flush()

def stop_share_screen(p1):
    common.picture_flag = 0
    time.sleep(0.5)
    common.conn_q.put("send_stop")
    # sys.stdout.flush()

def send_file(p1):
    print('gui_project_support.send_file')
    # sys.stdout.flush()

def turn_off(p1):
    common.conn_q.put("turn_off")
    sys.stdout.flush()

def turn_on(p1):
    print('gui_project_support.turn_on')
    sys.stdout.flush()

def watch_client(p1):
    print('gui_project_support.watch_client')
    sys.stdout.flush()

def init(top, gui, *args, **kwargs):
    global w, top_level, root
    w = gui
    top_level = top
    root = top
    import server_big_project
    main_connected = threading.Thread(target=server_big_project.main(), args=())
    main_connected.start()
    top.after(100, on_after_elapsed)

def destroy_window():
    # Function which closes the window.
    global top_level
    top_level.destroy()
    top_level = None

def on_after_elapsed():
    global w, top_level
    if common.gui_q.empty() is False:
        text = common.gui_q.get()
        to = w.Clients_List
        to.insert('end', text)
        print("size: " + str(to.size_()))
    top_level.after(1000, on_after_elapsed)

def selection_list():
    global w, top_level
    cl = w.Clients_List
    selected = cl.curselection()
    selected_list = []
    if selected:  # only do stuff if user made a selection
        print(selected)
        for index in selected:
            selected_list.append(cl.get(index))  # how you get the value of the selection from a listbox
    print(selected_list)
    return selected_list

def select_all_clients(p1):
    global w, top_level
    cl = w.Clients_List
    cl.select_set(0, 'end')  # select all
    print("select all")
    # sys.stdout.flush()

def clear_selection_listbox(p1):
    global w, top_level
    cl = w.Clients_List
    cl.select_clear(0, 'end')  # unselect all
    print("unselect all")
    # sys.stdout.flush()

if __name__ == '__main__':
    import gui_project
    gui_project.vp_start_gui()




