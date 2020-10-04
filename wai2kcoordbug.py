import json

import pyautogui
import pygetwindow
import win32api

win = pygetwindow.getWindowsWithTitle("Android Emulator")[0]
top_pad = 30
left_pad = 10
bot_pad = 0
reg = [win.left + left_pad, win.top + top_pad, win.width, win.bottom - bot_pad]
coords = []


def rel_pos():
    x = pyautogui.position().x - win.left
    y = pyautogui.position().y - win.top
    return "x = {}, y = {}".format(x, y)


def rel_coords(region, coord):
    rel_coord = [coord[0] - region[0], coord[1] - region[1], coord[2], coord[3]]
    return rel_coord


def make_box():
    corner1 = pyautogui.position()
    a = win32api.GetKeyState(0x02)
    while a < 0:
        a = win32api.GetKeyState(0x02)
    corner2 = pyautogui.position()
    return corner1, corner2


def corners_to_box(point1, point2):
    l = min(point1[0], point2[0])
    t = min(point1[1], point2[1])
    w = abs(point1[0] - point2[0])
    h = abs(point1[1] - point2[1])
    b = (l, t, w, h)
    return b


def to_dict(points):
    coord = {
        "x": points[0],
        "y": points[1],
        "width": points[2],
        "height": points[3]
    }
    coords.append(coord)


while True:
    try:
        rmb = win32api.GetKeyState(0x02)
        print("\r" + str(rel_pos() + " "), end='', flush=True)
        if rmb < 0:
            p1, p2 = make_box()
            box = corners_to_box(p1, p2)
            to_dict(rel_coords(reg, box))
            print("\r" + str(rel_coords(reg, box)))
    except KeyboardInterrupt:
        break

print(coords)
with open("map.json", "w") as f:
    json.dump(coords, f, indent=4)
