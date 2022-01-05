from os import times
from pynput import keyboard
import time
import datetime

timer = 0
times = 0

print("""반드시 음소거가 해제된 상태로 프로그램을 켜주세요.
지정한 단축키로 음소거 상태를 변경했을 때만 시간이 카운트됩니다.""")

n = input("음소거 상태 변경 단축키를 입력하고 엔터를 누르십시오. >> ")

print("지금부터 카운트 시작합니다.")

def on_press(key):
    pass
    # try:
    #     print(type(key.char))
    # except AttributeError:
    #     print('special key pressed: {0}'.format(
    #         key))
            
def on_release(key):
    global timer,begin,end,times,n
    # print('Key released: {0}'.format(key))
    try :
        if key.char == n:
            if timer == 0 :
                # 타이머 시작
                begin = time.time()
                timer = 1
            else :
                # 타이머 끄기
                timer = 0
                end = time.time()
                if times == 0 :
                    times = round(end - begin, 2)
                else :
                    times = round(end - begin + times, 2)
                now = datetime.datetime.now()
                now = str(now)[:19]
                print(now + " : " + str(times) + "초 마이크 사용")
    except AttributeError:
        pass


# Collect events until released
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()