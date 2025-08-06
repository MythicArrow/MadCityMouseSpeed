import ctypes
import pyautogui


def change_speed(speed):
    #   1 - slow
    #   10 - standard
    #   20 - fast
    set_mouse_speed = 113   # 0x0071 for SPI_SETMOUSESPEED
    ctypes.windll.user32.SystemParametersInfoA(set_mouse_speed, 0, speed, 0)


def get_current_speed():
    get_mouse_speed = 112   # 0x0070 for SPI_GETMOUSESPEED
    speed = ctypes.c_int()
    ctypes.windll.user32.SystemParametersInfoA(get_mouse_speed, 0, ctypes.byref(speed), 0)

    return speed.value


def proper_close():
    change_speed(standard_speed)

standard_speed = get_current_speed()

if __name__ == "__main__":
    print("Current mouse speed:", standard_speed)
    if pyautogui.press("1","2","3","4","5","6","7"):
        change_speed(20)  # Set to fast speed
    if pyautogui.press("1","2","3","4","5","6","7"):
        change_speed(10) # Set to standard speed
    if pyautogui.press("q"):
        proper_close()
    
        