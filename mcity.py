import ctypes
import keyboard
import time

def change_speed(speed):
    set_mouse_speed = 113  # SPI_SETMOUSESPEED
    ctypes.windll.user32.SystemParametersInfoA(set_mouse_speed, 0, speed, 0)

def get_current_speed():
    get_mouse_speed = 112  # SPI_GETMOUSESPEED
    speed = ctypes.c_int()
    ctypes.windll.user32.SystemParametersInfoA(get_mouse_speed, 0, ctypes.byref(speed), 0)
    return speed.value

def proper_close():
    change_speed(standard_speed)
    print("Mouse speed restored to original:", standard_speed)

standard_speed = get_current_speed()
current_speed = standard_speed
active_key = None  # Track which number key is currently toggling the speed

# Keys that trigger toggle
toggle_keys = ["1", "2", "3", "4", "5", "6", "7"]
toggle_speed = int(input("Write the toggle speed: "))  # Speed to switch to when toggled

print("Original mouse speed:", standard_speed)
print("Press any key 1–7 to toggle fast speed")
print("Press the same key again to restore speed")
print("Press 'q' to quit and restore original speed")

try:
    while True:
        for key in toggle_keys:
            if keyboard.is_pressed(key):
                if active_key == key:
                    change_speed(standard_speed)
                    active_key = None
                    print(f"Key {key} pressed again — restored to original speed: {standard_speed}")
                else:
                    change_speed(toggle_speed)
                    active_key = key
                    print(f"Key {key} pressed — set speed to: {toggle_speed}")
                time.sleep(0.24)  # debounce to prevent multiple triggers

        if keyboard.is_pressed("q"):
            proper_close()
            break

except KeyboardInterrupt:
    proper_close()
    print("Program terminated by user.")

        
