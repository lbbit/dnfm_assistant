import subprocess
import os
CHANGE_W_H = False # 某些手机横屏是长宽会互换
# 设定屏幕分辨率，此值为华为P60
SCREEN_WIDTH = 1220
SCREEN_HEIGHT = 2700

COMMON_SCREEN_WIDTH = 1220
COMMON_SCREEN_HEIGHT = 2700
WIN_ADB_EXE_PATH = "bin\\adb.exe"
UNIX_ADB_EXE_PATH = "adb"
def update_screen_resolution(change_w_h = False):
    ADB_EXE_PATH = UNIX_ADB_EXE_PATH
    if os.name == 'nt':
        print('Windows系统')
        ADB_EXE_PATH = WIN_ADB_EXE_PATH

    global CHANGE_W_H
    CHANGE_W_H = change_w_h
    global COMMON_SCREEN_WIDTH, COMMON_SCREEN_HEIGHT
    exec_success = False
    try:
        # 执行adb命令获取屏幕分辨率
        result = subprocess.run(f"{ADB_EXE_PATH} shell wm size", shell=True, capture_output=True, text=True)
        if result.stdout:
            # 输出通常是"Physical size: 1080x1920"
            output = result.stdout.strip()
            dimensions = output.split()[-1]  # 获取"1080x1920"
            width, height = dimensions.split('x')  # 分离宽度和高度
            if CHANGE_W_H: # x y互换
                COMMON_SCREEN_WIDTH, COMMON_SCREEN_HEIGHT = int(height),int(width)
            else:
                COMMON_SCREEN_WIDTH = int(width)
                COMMON_SCREEN_HEIGHT = int(height)
            print(f"Screen resolution updated to: {COMMON_SCREEN_WIDTH}x{COMMON_SCREEN_HEIGHT}")
            exec_success = True
        else:
            print("Failed to get screen resolution")
    except Exception as e:
        print(f"Failed to update screen resolution due to an error: {e}")
    return exec_success, COMMON_SCREEN_WIDTH, COMMON_SCREEN_HEIGHT
def get_coords(x_ratio, y_ratio):
    """根据比例计算绝对坐标"""
    return int(x_ratio * COMMON_SCREEN_HEIGHT), int(y_ratio * COMMON_SCREEN_WIDTH)

def adb_tap(x_ratio, y_ratio, duration=100):
    ADB_EXE_PATH = UNIX_ADB_EXE_PATH
    if os.name == 'nt':
        #print('Windows系统')
        ADB_EXE_PATH = WIN_ADB_EXE_PATH
    if CHANGE_W_H:
        x_ratio, y_ratio = y_ratio, x_ratio
    #print(f"adb_tap: x:{x_ratio} y:{y_ratio}")
    x, y = get_coords(x_ratio, y_ratio)
    #cmd = f"{ADB_EXE_PATH} shell input swipe {x} {y} {x} {y} {duration}"
    cmd = f"{ADB_EXE_PATH} shell input tap {x} {y}"
    #print(cmd)
    subprocess.run(cmd, shell=True)

# 休闲模式开始按钮
def start_game_xiuxian(duration=100):
    adb_tap(741.0 / 1560, 405.0 / 720, duration)
def start_game(duration=100):
    adb_tap(2284.0 / SCREEN_HEIGHT, 1100.0 / SCREEN_WIDTH, duration)

def move_up(duration=100):
    adb_tap(456.0 / SCREEN_HEIGHT, 763.0 / SCREEN_WIDTH, duration)

def move_down(duration=100):
    adb_tap(480.0 / SCREEN_HEIGHT, 993.0 / SCREEN_WIDTH, duration)

def move_left(duration=100):
    adb_tap(370.0 / SCREEN_HEIGHT, 895.0 / SCREEN_WIDTH, duration)

def move_right(duration=100):
    adb_tap(584.0 / SCREEN_HEIGHT, 901.0 / SCREEN_WIDTH, duration)

def attack(duration=100):
    adb_tap(2330.0 / SCREEN_HEIGHT, 1049.0 / SCREEN_WIDTH, duration)

def skill1(duration=100):
    adb_tap(2023.0 / SCREEN_HEIGHT, 1089.0 / SCREEN_WIDTH, duration)

def skill2(duration=100):
    adb_tap(2049.0 / SCREEN_HEIGHT, 929.0 / SCREEN_WIDTH, duration)

def skill3(duration=100):
    adb_tap(2181.0 / SCREEN_HEIGHT, 979.0 / SCREEN_WIDTH, duration)

def skill3_0(duration=100):
    adb_tap(2168.0 / SCREEN_HEIGHT, 762.0 / SCREEN_WIDTH, duration)

def skill4(duration=100):
    adb_tap(2387.0 / SCREEN_HEIGHT, 753.0 / SCREEN_WIDTH, duration)

def skill5(duration=100):
    adb_tap(1834.0 / SCREEN_HEIGHT, 1132.0 / SCREEN_WIDTH, duration)

def skill6(duration=100):
    adb_tap(1677.0 / SCREEN_HEIGHT, 1100.0 / SCREEN_WIDTH, duration)

def skill7(duration=100):
    adb_tap(2386.0 / SCREEN_HEIGHT, 508.0 / SCREEN_WIDTH, duration)

def skill8(duration=100):
    adb_tap(2443.0 / SCREEN_HEIGHT, 400.0 / SCREEN_WIDTH, duration)

# 激斗左边技能2
def skill9_jidou1(duration=100):
    adb_tap(222.0 / SCREEN_HEIGHT, 342.0 / SCREEN_WIDTH, duration)

# 激斗左边技能1
def skill9_jidou2(duration=100):
    adb_tap(131.0 / SCREEN_HEIGHT, 335.0 / SCREEN_WIDTH, duration)

def end_game_to_lobby(duration=100):
    adb_tap(1349.0 / SCREEN_HEIGHT, 1138.0 / SCREEN_WIDTH, duration)

def end_game_to_lobby_daluandou(duration=100):
    adb_tap(801.0 / 1560, 468.0 / 720, duration)

def claim_mission(duration=100):
    adb_tap(389.0 / SCREEN_HEIGHT, 1130.0 / SCREEN_WIDTH, duration)

def claim_mission_paiwei(duration=100):
    adb_tap(244.0 / 1560, 660.0 / 720, duration)

    # 大乱斗任务入口
def claim_mission_daluandou(duration=100):
    adb_tap(127.0 / 1560, 644.0 / 720, duration)

def jidou_claim_mission(duration=100):
    adb_tap(627.0 / 1560, 656.0 / 720, duration)

def claim_button(duration=100):
    adb_tap(2200.0 / SCREEN_HEIGHT, 1055.0 / SCREEN_WIDTH, duration)

def claim_button_paiwei(duration=100):
    adb_tap(1270.0 / 1560, 646.0 / 720, duration)

def claim_button_daluandou(duration=100):
    adb_tap(1237.0 / 1560, 640.0 / 720, duration)

def return_button(duration=100):
    adb_tap(2340.0 / SCREEN_HEIGHT, 125.0 / SCREEN_WIDTH, duration)

def return_button_paiwei(duration=100):
    adb_tap(1368.0 / 1560, 65.0 / 720, duration)
def return_button_daluandou(duration=100):
    adb_tap(1368.0 / 1560, 65.0 / 720, duration)

def next_page(duration=100):
    adb_tap(1302.0 / SCREEN_HEIGHT, 1056.0 / SCREEN_WIDTH, duration)

def next_page_paiwei(duration=100):
    adb_tap(764.0 / 1560, 661.0 / 720, duration)

def jidou_next_page(duration=100):
    adb_tap(771.0 / 1560, 640.0 / 720, duration)

def return_start(duration=100):
    adb_tap(1134.0 / SCREEN_HEIGHT, 1109.0 / SCREEN_WIDTH, duration)

# 大乱斗超过7次开始后
def daluandou_ensure_start(duration=100):
    adb_tap(860.0 / 1560, 469.0 / 720, duration)

# 左上角返回
def common_return(duration=100):
    adb_tap(94.0 / 1560, 31.0 / 720, duration)

def juedou_select_paiwei(duration=100): # 决斗页面选择排位
    adb_tap(326.0 / 1560, 284.0 / 720, duration)

def juedou_select_jidou(duration=100): # 决斗页面选择激斗
    adb_tap(930.0 / 1560, 362.0 / 720, duration)

def juedou_select_daluandou(duration=100): # 决斗页面选择大乱斗
    adb_tap(1266.0 / 1560, 370.0 / 720, duration)

# 糖果弹弹乐_下降一个糖果
def tangguo_down(duration=100):
    adb_tap(1321.0 / 1560, 622.0 / 720, duration)

# 糖果弹弹乐_再次挑战
def tangguo_tryagain(duration=100):
    adb_tap(885.0 / 1560, 547.0 / 720, duration)