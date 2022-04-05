import pyautogui as pag, time
import threading
from pynput.keyboard import Listener, KeyCode


delay = 1
start_stop_key = KeyCode(char='s')
exit_key = KeyCode(char='e')


class sendTxt(threading.Thread):
    def __init__(self,delay):
        super(sendTxt, self).__init__()
        self.delay = delay
        self.txt = "starway_to_heaven.txt"
        self.song = open(f"{self.txt}", "r")
        self.lines = self.song.readlines()
        self.running = False
        self.program_running = True

    def start_txting(self):
        self.runnnig = True

    def stop_txting(self):
        self.runnnig = False
    
    def exit(self):
        self.stop_txting()
        self.program_running = False

    def run(self):
        while self.program_running:
            while self.running:
                for self.line in self.lines: 
                    pag.typewrite(self.line)
                    pag.press("enter")
                    time.sleep(1)

time.sleep(2)
send_thread = sendTxt(delay)
send_thread.start()


def on_press(key):
    if key == start_stop_key:
        if send_thread.running:
            send_thread.stop_txting()
        else:
           send_thread.start_txting()
    elif key == exit_key:
        send_thread.exit()
        listener.stop()


with Listener(on_press=on_press) as listener:
    listener.join()

print("done")