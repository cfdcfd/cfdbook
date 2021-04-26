import tkinter as tk

import time
import argparse
import winsound
import logging

# todo log 打印到不同日志文件

import os

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Hello World\n(click me)"
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack(side="top")

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="bottom")

    def say_hi(self):
        input('what did you do during last period?')
        print("hi there, everyone!")

def mkdir(path):
	folder = os.path.exists(path)
	if not folder:
		os.makedirs(path)

first_class = ["事务","学习","编码","总结"]

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

log_show = logging.StreamHandler()
log_show.setLevel(logging.DEBUG)
mkdir('./tomato_record')
log_file = logging.FileHandler('./tomato_record/timer.log',encoding='utf8')
log_file.setLevel(logging.INFO)

logger.addHandler(log_show)
logger.addHandler(log_file)

# 增加日志功能
parser = argparse.ArgumentParser(description='Timer Config')
parser.add_argument('-m', type=int, default=25, help='timeing minutes')
args = parser.parse_args()

TIMER_MINITES = args.m

start = time.time()
start_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(start))
planed_task = input('what do you want to do during this period?')
difficult = input('difficult point? 5:very hard 1:very easy')
delta_seconds = time.time() - start
logger.debug('{} s used to write theme'.format(round(delta_seconds,2)))
left_time = TIMER_MINITES - delta_seconds//60
logger.debug('{} minutes left'.format(left_time))
is_interrupted = 0
actual_task = ''

try:
    while True:
        end = time.time()
        delta_seconds = end -start
        # print(start,end,delta_seconds)
        current_left_minutes = TIMER_MINITES - delta_seconds//60
        if current_left_minutes < left_time:
            left_time = current_left_minutes
            winsound.PlaySound('SystemAsterisk', winsound.SND_ALIAS)
            logger.debug('{} minutes left'.format(left_time)) 
        if delta_seconds >= TIMER_MINITES*60:
            end_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(end))
            winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS)
            winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS)
            root = tk.Tk()
            root.wm_attributes('-topmost',1)
            w, h = root.maxsize()
            root.geometry("{}x{}".format(w, h))
            app = Application(master=root)
            app.mainloop()
            actual_task = input('what did you do during last period?')
            pleasant = input('happy? 5:verry satisfy 1:verry unhappy')
            break

        time.sleep(10)
except KeyboardInterrupt:
    is_interrupted = 1
    interrupt_reason = 'interrupt reason:'+input('why interrupt the period?')
    pleasant = input('happy? 5:verry satisfy 1:verry unhappy')
    actual_end_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    delta_seconds = time.time() -start
    actual_minutes = round(delta_seconds // 60)
    actual_seconds = round(delta_seconds % 60)
    logger.debug('{} m {} s interrupted'.format(actual_minutes, round(actual_seconds,2)))
    logger.info('{},{}:{},{},{},{},{},{},{},{}'.format(TIMER_MINITES, actual_minutes, actual_seconds,start_time, actual_end_time, is_interrupted, planed_task, interrupt_reason,difficult,pleasant))
    raise SystemExit

actual_end_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
delta_seconds = time.time() -start
actual_minutes = round(delta_seconds // 60)
actual_seconds = round(delta_seconds % 60)
logger.debug('{} m {} s'.format(actual_minutes, round(actual_seconds,2)))
logger.info('{},{}:{},{},{},{},{},{},{},{}'.format(TIMER_MINITES, actual_minutes, actual_seconds, start_time, actual_end_time, is_interrupted, planed_task, actual_task,difficult,pleasant))
