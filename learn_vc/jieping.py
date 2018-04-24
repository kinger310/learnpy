# encoding: utf-8
import re
import pickle

import numpy as np
import win32gui
import win32clipboard as clip
import pyscreenshot as ps
from PIL import Image


class WindowMgr:
    """Encapsulates some calls to the winapi for window management"""

    def __init__(self):
        """Constructor"""
        self._handle = None

    def isfind(self):
        return bool(self._handle)

    def find_window(self, class_name, window_name=None):
        """find a window by its class_name"""
        self._handle = win32gui.FindWindow(class_name, window_name)

    def _window_enum_callback(self, hwnd, wildcard):
        """Pass to win32gui.EnumWindows() to check all the opened windows"""
        if re.match(wildcard, str(win32gui.GetWindowText(hwnd))) is not None:
            self._handle = hwnd

    def find_window_wildcard(self, wildcard):
        """find a window whose title matches the wildcard regex"""
        self._handle = None
        win32gui.EnumWindows(self._window_enum_callback, wildcard)

    def set_foreground(self):
        """put the window in the foreground"""
        win32gui.SetForegroundWindow(self._handle)


def crop_images():
    image = Image.open('C:\PycharmProjects\ppdai3\learn_vc\screenshot.png')
    image = image.convert("L")
    # image.show()
    X, y = image.size
    x = X / 6
    images = []
    for i in range(6):
        tmp_im = image.crop((i * x, 0, (i + 1) * x, y))
        tmp = np.array(tmp_im).reshape(1, -1)  # / 255 貌似除不除都行。。
        images.append(tmp)
    return images


def screenshot():
    w = WindowMgr()
    w.find_window_wildcard(".*宁盾令牌.*")
    if w.isfind():
        w.set_foreground()
    else:
        raise Exception('请打开宁盾令牌！')
    w.set_foreground()
    im = ps.grab(bbox=(861, 482, 1059, 537))  # X1,Y1,X2,Y2
    # im.show()
    im.save('C:\PycharmProjects\ppdai3\learn_vc\screenshot.png')


def main():
    screenshot()
    images = crop_images()
    with open(r'C:\PycharmProjects\ppdai3\learn_vc\model.pkl', 'rb') as file:
        model = pickle.load(file)
    chars = "".join([str(model.predict(im)[0]) for im in images])
    # print(chars)
    clip.OpenClipboard()
    clip.EmptyClipboard()
    clip.SetClipboardText(chars)
    clip.CloseClipboard()

if __name__ == "__main__":
    main()
