import win32api,win32con,win32gui
def get_windows_pos(name):
    name = name
    handle = win32gui.FindWindow(name,0)
    #get windows sentence
    if handle == 0:
        return None
    else:
        return win32gui.GetWindowRect(handle)

#x1,y1,x2,y2 =
get_windows_pos('Intermediate D3D Window')
#print(x1,y1,x2,y2)


