__author__ = 'Yuval Cohen'
"""The main file on the client computer. Includes the Client class, 
his commands and his communication with the server."""
import sys
import threading
from threading import Thread
from zlib import compress
from zlib import decompress
from mss import mss
import ctypes
from socket import socket
import socket
import pygame
import time
from pynput.mouse import Button, Controller as MouseController, Listener as MouseListener
import os
import tkinter as tk
import subprocess
from pathlib import Path
from getmac import get_mac_address as gma
from project_variables import *
from block_input import *
from finals import Finals as final
import pathlib
import shutil
import gui_client
import gui_client_support
import send_gui
import send_gui_support
import win32console
import win32gui
try:
    import httplib
except:
    import http.client as httplib

from ctypes import windll
SetWindowPos = windll.user32.SetWindowPos
NOSIZE = 1
NOMOVE = 2
TOPMOST = -1
NOT_TOPMOST = -2

# prog_call = r'%s' % str(Path(__file__).absolute()).replace('\\', '/')
# prog_location = os.path.split(prog_call)[0]
prog_call = sys.argv[0]
prog_location = os.path.split(prog_call)[0]
WOL_SETTINGS_FILE = "Enable-WOLWindowsNICSettings.ps1"
MAC_ADDRESS = gma().replace(":", "")
BUFFER_SIZE = 1024
MAX_BYTES = 65000

# convert to exe file -
# pyinstaller --onefile --uac-admin client_big_project.py -r prog.exe.manifest,1

"""src = sys.executable
print(src)
config_name = 'client_big_project.exe'

# determine if application is a script file or frozen exe
if getattr(sys, 'frozen', False):
    application_path = os.path.dirname(sys.executable)
else:
    application_path = os.path.dirname(__file__)
print(application_path)
config_path = os.path.join(application_path, config_name)
print(config_path)"""

# Hide the Console
window = win32console.GetConsoleWindow()
win32gui.ShowWindow(window, 0)


def get_network_data(pattern):
    try:
        read_con = open(final.first_setup_path + "\\network_data.txt", "r")
    except:
        read_con = open(prog_location + "\\network_data.txt", "r")
    content = read_con.read()
    lines = content.split("\n")
    for line in lines:
        parts = line.split(",")
        if str(parts[0]) == str(pattern):
            read_con.close()
            return parts[1].strip("\n")
    read_con.close()


class NetworkData:
    BROADCAST_IP = '<broadcast>'
    SERVER_IP = str(get_network_data("SERVER_IP"))
    SERVER_PORT = int(get_network_data("SERVER_PORT"))
    SECONDARY_PORT = int(get_network_data("SECONDARY_PORT"))
    THIRD_PORT = int(get_network_data("THIRD_PORT"))
    TCP_PORT = int(get_network_data("TCP_PORT"))
    TCP_PORT2 = int(get_network_data("TCP_PORT2"))


def add_to_startup():
    # copy the files of the project to the startup folder
    try:
        # file_folder = str(pathlib.Path(__file__).parent.absolute())
        file_folder = prog_location
        print(file_folder)
        devconMove = final.main_path + "\\devcon.exe"
        file_path_move = final.main_path + "\\client_big_project.exe"
        image_move = final.first_setup_path + "\\fe_icon.png"
        wol_settings_move = "C:\\%s" % WOL_SETTINGS_FILE
        network_data_move = final.first_setup_path + "\\network_data.txt"
        devconCurrent = file_folder + "\\devcon.exe"
        file_path_current = file_folder + "\\client_big_project.exe"
        image_current = file_folder + "\\fe_icon.png"
        wol_setting_current = file_folder + "\\%s" % WOL_SETTINGS_FILE
        network_data_current = file_folder + "\\network_data.txt"
        try:
            shutil.copy(image_current, image_move)
        except Exception as e:
            print(e)
        try:
            shutil.copy(file_path_current, file_path_move)
        except Exception as e:
            print(e)
        try:
            shutil.copy(devconCurrent, devconMove)
            shutil.copy(devconMove, r"C:\Windows\System32\devcon.exe")
            shutil.copy(devconMove, r"C:\Windows\SysWOW64\devcon.exe")
        except Exception as e:
            print(e)
        try:
            shutil.copy(wol_setting_current, wol_settings_move)
        except Exception as e:
            print(e)
        try:
            shutil.copy(network_data_current, network_data_move)
        except Exception as e:
            print(e)
    except:
        pass


def control_mss():
    # the function photographs the student's screen and sends it to the teacher
    global watch_client_socket, sharing
    sharing = True
    watch_client_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
    watch_client_socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    screen_size = "{},{}".format(client.WIDTH, client.HEIGHT)
    watch_client_socket.sendto(screen_size.encode(), (NetworkData.SERVER_IP, NetworkData.THIRD_PORT))
    time.sleep(0.5)
    with mss() as sct:
        rect = {'top': 0, 'left': 0, 'width': client.WIDTH, 'height': client.HEIGHT}
        while True:
            try:
                if sharing:
                    img = sct.grab(rect)
                    pixels = compress(img.rgb, 6)
                    size = len(pixels)
                    size_len = (size.bit_length() + 7) // 8
                    size_bytes = size.to_bytes(size_len, 'big')
                    watch_client_socket.sendto(size_bytes, (NetworkData.SERVER_IP, NetworkData.THIRD_PORT))
                    sleep = False
                    if size > 100000:
                        sleep = True
                    while client.max_bytes < len(pixels):
                        part_pixels = pixels[:client.max_bytes]
                        watch_client_socket.sendto(part_pixels, (NetworkData.SERVER_IP, NetworkData.THIRD_PORT))
                        if sleep:
                            time.sleep(0.001)
                        pixels = pixels[client.max_bytes:]
                    watch_client_socket.sendto(pixels, (NetworkData.SERVER_IP, NetworkData.THIRD_PORT))
                else:
                    break
            except FileNotFoundError:
                continue
            except Exception:
                pass
            time.sleep(0.01)
    print("end")
    watch_client_socket.close()


def control_mouse(data):
    # gets the position of the teacher's mouse and change the mouse to this position
    if len(data) == 2:
        x1, y1 = data
        x, y = change_xy(x1, y1)
        client.mouse.position = (int(x), int(y))


def change_xy(x, y):
    # adjust x and y size to the other computer size
    x = int(float(x) * prop_x)
    y = int(float(y) * prop_y)
    return x, y


def show_mouse():
    # create a connection with the server mouse socket,
    # loop of recieves the position of the teacher's mouse and change the mouse to this position
    while client.width == -1:  # wait for recieve_screen and then start the listeners
        time.sleep(0.1)
    global prop_x, prop_y
    prop_x = client.width / client.WIDTH
    prop_y = client.height / client.HEIGHT
    mouse_client_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
    mouse_client_socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    time.sleep(0.3)
    mouse_client_socket.sendto("connected".encode(), (NetworkData.SERVER_IP, NetworkData.SECONDARY_PORT))
    print("yes")
    while True:
        data, address = mouse_client_socket.recvfrom(MAX_BYTES)
        data = data.decode()
        if data == "stop_mouse":
            print("stop_send_screen")
            replace(final.command_execute, "watch_stop")
            # check_q.put("stop_send")
            break
        data = data.split(",")
        control_mouse(data)
    mouse_client_socket.close()


def exb():
    pass


def waitingwindow():
    # create a window showing 'lock computer'
    wa = tk.Tk()
    wa.title('ControlNet - YOUR COMPUTER IS LOCKED')
    wa.state('zoomed')
    wa.focus_set()  # <-- move focus to this widget
    wa.protocol("WM_DELETE_WINDOW", exb)  # hide close button
    wa.protocol("WM_MINIMIZE_WINDOW", exb)  # hide minimize button
    x = wa.winfo_screenwidth()
    y = wa.winfo_screenheight()
    wa.geometry("%dx%d" % (x, y))  # full screen
    lb1 = tk.Label(wa, text="YOUR COMPUTER IS LOCKED\n", font=("Arial Bold", 70), pady=200, fg="RED")
    lb1.pack()
    wa.call('wm', 'attributes', '.', '-topmost', '1')  # lift to the top
    wa.attributes("-topmost", True)
    wa.overrideredirect(1)
    # wa.lift()
    while str(get(final.active_field)) == "1":
        wa.update()
        time.sleep(0.1)
    print("destroy")
    wa.destroy()


def get_file():
    tcp_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_client.connect((NetworkData.SERVER_IP, NetworkData.TCP_PORT))
    file_path = tcp_client.recv(BUFFER_SIZE).decode()
    file_name = os.path.split(file_path)[1]
    print(file_name)
    print(final.files_from_server_path)
    with open(final.files_from_server_path + file_name, 'wb') as f:
        print('file opened')
        while True:
            # print('receiving data...')
            data = tcp_client.recv(BUFFER_SIZE)
            # print('data=%s', (data))
            if not data:
                f.close()
                print('file close()')
                break
            # write data to a file
            f.write(data)

    print('Successfully get the file')
    tcp_client.close()


def client_send():
    # The function is responsible for sending information from the client
    while True:
        if final.conn_q.empty() is False:
            data = final.conn_q.get()
            if str(data) == "stop_system":
                break
            if str(data).startswith("new client"):
                replace(final.client_name, str(data[10:]))
                data = data + "    " + client.mac
                print("client_send:" + data)
            client.socket_send(client.client_socket, data)
        time.sleep(0.05)  # sleep a little before check the queue again


def set_taskmgr(status):
    # enable/disable the task manager
    subprocess.Popen(
        "reg.exe add HKCU\Software\Microsoft\Windows\CurrentVersion\Policies\System /v DisableTaskMgr /t REG_DWORD /d %s /f" % status)


def set_uac_message(status):
    # enable/disable the uac message
    subprocess.Popen(
        "reg.exe ADD HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System /v EnableLUA /t REG_DWORD /d %s /f" % status)


class Client(Thread):
    def __init__(self, max_bytes):
        Thread.__init__(self)
        user32 = ctypes.windll.user32
        user32.SetProcessDPIAware()
        self.width = -1
        self.height = -1
        self.WIDTH = user32.GetSystemMetrics(0)
        self.HEIGHT = user32.GetSystemMetrics(1)
        self.max_bytes = max_bytes
        self.server_ip = NetworkData.SERVER_IP
        self.port = NetworkData.SERVER_PORT
        self.mac = MAC_ADDRESS
        self.mouse = MouseController()
        self.client_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
        self.client_socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        send_thread = threading.Thread(target=client_send, args=())
        send_thread.start()

    def socket_send(self, conn_socket, message):
        # gets the socket object and the message to send, and send it to the server.
        connection_address_port = (self.server_ip, self.port)
        conn_socket.sendto(message.encode(), connection_address_port)

    def socket_recv(self, conn_socket, msgsize):
        # gets the socket object and the max size of recv, returns the recieved message.
        full_message, address = conn_socket.recvfrom(msgsize)
        return full_message

    def recvall(self, length):
        # gets the size(length) of the picture, returns the pixels of the picture.
        buf = b''
        while len(buf) < length:
            data = self.client_socket.recvfrom(self.max_bytes)
            data = data[0]
            if not data:
                return data
            buf += data
        return buf

    def recieve_screen(self):
        # display on the client's screen the screen of the server.
        def alwaysOnTop(yesOrNo):
            # in order to set the pygame window always on top of all the windows.
            zorder = (NOT_TOPMOST, TOPMOST)[yesOrNo]  # choose a flag according to bool
            hwnd = pygame.display.get_wm_info()['window']  # handle to the window
            SetWindowPos(hwnd, zorder, 0, 0, 0, 0, NOMOVE | NOSIZE)

        if int(get(final.width_screen)) == -1:
            data = self.socket_recv(self.client_socket, 1024).decode()
            print(data)
            self.width, self.height = data.split(",")
            self.width = int(self.width)
            self.height = int(self.height)
            replace(final.width_screen, self.width)
            replace(final.height_screen, self.height)
        else:
            self.width = int(get(final.width_screen))
            self.height = int(get(final.height_screen))
        # open the window
        pygame.init()
        screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT), pygame.FULLSCREEN)
        clock = pygame.time.Clock()
        self.client_socket.settimeout(3)
        watching = True
        # print other computer screen
        try:
            while watching:
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            pass
                alwaysOnTop(1)
                size = int.from_bytes(self.socket_recv(self.client_socket, self.max_bytes), byteorder='big')
                while size > 10000000:  # checks if it is a size and not part of the pixels
                    size = int.from_bytes(self.socket_recv(self.client_socket, self.max_bytes), byteorder='big')
                temp_pixels = self.recvall(size)
                try:
                    pixels = decompress(temp_pixels)
                    # Create the Surface from raw pixels
                    img = pygame.image.fromstring(pixels, (self.width, self.height), 'RGB')
                    picture = pygame.transform.scale(img, (self.WIDTH, self.HEIGHT))
                    # Display the picture
                    screen.blit(picture, (0, 0))
                    pygame.display.flip()
                    clock.tick(60)
                except:
                    pass
        except:
            pass
        finally:
            print("pygame quit")
            replace(final.active_field, 0)
            replace(final.command_execute, "stop_send_screen")
            pygame.quit()
            self.client_socket.settimeout(None)

    def command_response(self, command):
        # gets a string of the selected command and handle it.
        global sharing
        if command == "send_screen":
            print("send_screen")
            mouse_thread = threading.Thread(target=show_mouse, args=())
            mouse_thread.start()
            replace(final.active_field, 1)
            replace(final.command_execute, "send_screen")
            run1_thread = threading.Thread(target=lock_settings, args=())
            run1_thread.start()
            self.recieve_screen()
        if command == "lock_screen":
            print("lock")
            replace(final.active_field, 1)
            replace(final.command_execute, "lock_screen")
            run2_thread = threading.Thread(target=lock_settings, args=())
            run2_thread.start()
            time.sleep(0.5)
            lock_thread = threading.Thread(target=waitingwindow, args=())
            lock_thread.start()
        if command == "unlock_screen":
            print("unlock")
            replace(final.active_field, 0)
            replace(final.command_execute, "unlock_screen")
        if command == "turn_off_computer":
            print("turn off computer")
            replace(final.command_execute, "turn_off_computer")
            time.sleep(1)
            os.system('shutdown /p /f')
        if command == "watch_screen":
            print("watch_screen")
            replace(final.command_execute, "watch_screen")
            time.sleep(1)
            watch_thread = threading.Thread(target=control_mss, args=())
            watch_thread.start()
        if command == "watch_stop":
            print("watch_stop")
            replace(final.command_execute, "watch_stop")
            sharing = False
        if command == "send_file":
            print("send_file")
            replace(final.command_execute, "get_file")
            watch_thread = threading.Thread(target=get_file, args=())
            watch_thread.start()

    def first_connection(self):
        self.client_socket.settimeout(4)
        while True:
            try:
                self.client_socket.sendto("new client".encode(), (self.server_ip, self.port))
                print("first send")
                data, address = self.client_socket.recvfrom(self.max_bytes)
                self.client_socket.settimeout(None)
                break
            except:
                pass
        if data.decode() != "connected":
            guiname_thread = threading.Thread(target=gui_client.vp_start_gui, args=())
            guiname_thread.start()
            while True:
                data, address = self.client_socket.recvfrom(self.max_bytes)
                if data.decode() == "welcome":
                    final.error_message = ""
                    break
                final.error_message = str(data.decode())
            guiname_thread.join()

    def run(self):
        # runs client listening.
        self.first_connection()
        send_gui_thread = threading.Thread(target=send_gui.vp_start_gui, args=())
        send_gui_thread.start()

        """if int(get(final.width_screen)) == -1:
            server_screen_size = self.socket_recv(self.client_socket, 1024).decode()
            print(server_screen_size)
            self.width, self.height = server_screen_size.split(",")
            self.width = int(self.width)
            self.height = int(self.height)
            replace(final.width_screen, self.width)
            replace(final.height_screen, self.height)"""

        if str(get(final.command_execute)) == "lock_screen":
            self.command_response("lock_screen")
        if str(get(final.command_execute)) == "send_screen":
            self.command_response("send_screen")

        while True:
            try:
                print("run")
                data, address = self.client_socket.recvfrom(self.max_bytes)
                data = data.decode()
                print(data)
                if data == "system_quit":
                    final.conn_q.put("stop_system")
                    break
                self.command_response(data)
            except:
                pass
            time.sleep(0.1)

        final.end_gui = True
        set_uac_message("1")
        set_taskmgr("0")
        send_gui_thread.join()
        self.client_socket.close()
        os._exit(1)


def hide_folder():
    # hide the folder of the project.
    try:
        subprocess.Popen("attrib +s +h \"%s\"" % final.first_setup_path)
        subprocess.Popen("attrib +s +h \"%s\"" % final.main_path)
        subprocess.Popen("attrib +s +h \"C:\\%s\"" % WOL_SETTINGS_FILE)
    except:
        pass


def define_wol_settings():
    # run the powershell file: Enable-WOLWindowsNICSettings.ps1 in order to set Wake on Lan settings.
    try:
        # setf = "\"%s\\Enable-WOLWindowsNICSettings.ps1\"" % final.first_setup_path
        psxmlgen = subprocess.Popen(['powershell.exe',
                                     '-ExecutionPolicy',
                                     'Unrestricted',
                                     "C:\\%s" % WOL_SETTINGS_FILE], cwd=os.getcwd())
        result = psxmlgen.wait()
    except:
        pass


def have_internet():
    # checks if the computer is connected to the network. if not - lock the pc.
    condition = 0
    time.sleep(5)
    while final.end_gui is False:
        conn = httplib.HTTPConnection("www.google.com", timeout=5)
        try:
            conn.request("HEAD", "/")
            conn.close()
            if condition == 1:
                client.command_response("unlock_screen")
                condition = 0
        except:
            conn.close()
            if condition == 0:
                client.command_response("lock_screen")
                condition = 1
        time.sleep(3)


def main():
    create_start()
    add_to_startup()
    set_uac_message("0")
    set_taskmgr("1")
    define_wol_settings()
    hide_folder()
    global client
    client = Client(MAX_BYTES)
    client.start()
    time.sleep(0.5)
    net_thread = threading.Thread(target=have_internet, args=())
    net_thread.start()


if __name__ == '__main__':
    main()
