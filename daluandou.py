import time
import random
import argparse
import game_controls
import threading


def execute_action(action, act_time, delay):
    action(act_time)
    time.sleep(delay)
def select_and_execute_actions(action_weights):
    move_actions = [
        game_controls.move_up,
        game_controls.move_down,
        game_controls.move_left,
        game_controls.move_right
    ]
    attack_actions = [
        game_controls.attack,
        game_controls.skill1,
        game_controls.skill2,
        game_controls.skill3,
        game_controls.skill4
    ]

    move_choice = \
    random.choices(move_actions, weights=[action_weights.get(action.__name__, 1) for action in move_actions], k=1)[0]
    attack_choice = \
    random.choices(attack_actions, weights=[action_weights.get(action.__name__, 1) for action in attack_actions], k=1)[
        0]

    move_thread = threading.Thread(target=execute_action, args=(move_choice, 800, random.uniform(0.05, 0.2)))
    attack_thread = threading.Thread(target=execute_action, args=(attack_choice, 200, random.uniform(0.05, 0.2)))

    move_thread.start()
    attack_thread.start()

    move_thread.join()
    attack_thread.join()
def select_action_with_probability(action_weights):
    actions = [
        game_controls.move_up,
        game_controls.move_down,
        game_controls.move_left,
        game_controls.move_right,
        game_controls.attack,
        game_controls.skill1,
        game_controls.skill2,
        game_controls.skill3,
        game_controls.skill4
    ]
    # 创建一个包含动作和其对应权重的列表
    weighted_actions = [(action, action_weights.get(action.__name__, 1)) for action in actions]
    # 解包动作和权重为两个独立的列表
    choices, weights = zip(*weighted_actions)
    # 使用random.choices根据权重选择一个动作
    choice = random.choices(choices, weights=weights, k=1)[0]
    return choice

def select_and_execute_actions_nothread(action_weights):
    action = select_action_with_probability(action_weights)
    action(40)

def main(loop_count=1, do_mission=False, action_weights=None):
    if action_weights is None:
        action_weights = {
            'move_up': 3,
            'move_down': 3,
            'move_left': 2,
            'move_right': 2,
            'attack': 10,
            'skill1': 4,
            'skill2': 4,
            'skill3': 4,
            'skill4': 4
        }

    for i in range(loop_count):
        print(f"Loop {i+1}/{loop_count}: Starting game process.")

        # Step 1: Start game
        print(f"Loop {i+1}/{loop_count}: Starting game.")
        # 休闲界面 开始决斗 按钮
        game_controls.start_game_xiuxian(100)
        time.sleep(1)

        if do_mission:
            # Mission claiming process
            print(f"Loop {i + 1}/{loop_count}: Claiming missions.")
            game_controls.claim_mission_daluandou(100)
            time.sleep(1)
            game_controls.claim_button_daluandou(100)
            sleep_time = 3
            print(f"Loop {i + 1}/{loop_count}: Sleeping for {sleep_time} seconds after claiming missions.")
            time.sleep(sleep_time)
            game_controls.return_button_daluandou(100)
            game_controls.return_button_daluandou(100)
            print(f"Loop {i + 1}/{loop_count}: Missions claimed and returned to main menu.")

        game_controls.start_game(100)
        time.sleep(1)
        game_controls.daluandou_ensure_start(100)
        sleep_time = 13
        print(f"Loop {i+1}/{loop_count}: Sleeping for {sleep_time} seconds before battle.")
        time.sleep(sleep_time)

        # Step 2: Battle phase for 3 minutes
        print(f"Loop {i+1}/{loop_count}: Entering battle phase.")
        battle_start_time = time.time()
        battle_duration = 180  # 3分钟
        while time.time() < battle_start_time + battle_duration:
            remaining_time = int((battle_start_time + battle_duration) - time.time())
            print(f"Loop {i+1}/{loop_count}: Battle phase, {remaining_time} seconds remaining.")
            select_and_execute_actions_nothread(action_weights)

        print(f"Loop {i+1}/{loop_count}: Battle phase ended.")

        sleep_time = 20
        print(f"Loop {i+1}/{loop_count}: Battle phase ended. Sleeping for {sleep_time} seconds.")
        time.sleep(sleep_time)

        # Step 3: End game to lobby
        print(f"Loop {i+1}/{loop_count}: Ending game and returning to lobby.")
        game_controls.end_game_to_lobby_daluandou(100)
        time.sleep(1)
        game_controls.end_game_to_lobby_daluandou(100)
        sleep_time = 5
        print(f"Loop {i+1}/{loop_count}: Sleeping for {sleep_time} seconds before next loop.")
        time.sleep(sleep_time)



