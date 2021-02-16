from pynput.mouse import Listener
import firefox_browser

# mouse = Controller()
# 
# # Read pointer position
# while True:
#     print('The current pointer position is {0}'.format(mouse.position))

def on_move(x, y):
    print('Pointer moved to {0}'.format((x, y)))
    # if x == 0 and y == 0:
    #     firefox_browser.firefox('https://www.google.com')

def on_click(x, y, button, pressed):
    print('{0} at {1}'.format(
        'Pressed' if pressed else 'Released',
        (x, y)))
    if not pressed:
        # stop listener
        return False

def on_scroll(x, y, dx, dy):
    print('Scrolled {0}'.format((x, y)))

# Collect events until released
with Listener(
        on_move=on_move,
        on_click=on_click,
        on_scroll=on_scroll) as listener:
    listener.join()
