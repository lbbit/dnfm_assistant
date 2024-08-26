import time
import random
import argparse
import game_controls

def select_action_with_probability(action_weights):
    actions = [
        game_controls.move_up,
        game_controls.move_down,
        game_controls.move_left,
        game_controls.move_right,
        game_controls.attack,
        game_controls.skill1,
        game_controls.skill2,
        game_controls.skill3_0,
        game_controls.skill4,
        #game_controls.skill5,
        #game_controls.skill6,
        game_controls.skill7,
        game_controls.skill8
    ]
    # 创建一个包含动作和其对应权重的列表
    weighted_actions = [(action, action_weights.get(action.__name__, 1)) for action in actions]
    # 解包动作和权重为两个独立的列表
    choices, weights = zip(*weighted_actions)
    # 使用random.choices根据权重选择一个动作
    choice = random.choices(choices, weights=weights, k=1)[0]
    return choice

def main(loop_count=1, do_mission=False, action_weights=None):
    if action_weights is None:
        action_weights = {
            #'move_up': 4,
            #'move_down': 4,
            #'move_left': 2,
            #'move_right': 2,
            'attack': 1,
            'skill1': 4,
            'skill2': 5,
            'skill3_0': 3,
            'skill4': 3,
            'skill5': 4,
            'skill6': 3,
            'skill7': 3,
            'skill8': 2
        }

    for i in range(loop_count):
        print(f"Loop {i+1}/{loop_count}: Starting game process.")

        # Step 1: Start game
        print(f"Loop {i+1}/{loop_count}: Starting game.")
        game_controls.start_game(100)
        sleep_time = 11
        print(f"Loop {i+1}/{loop_count}: Sleeping for {sleep_time} seconds before battle.")
        time.sleep(sleep_time)

        # Step 2: Battle phase for 3 minutes
        print(f"Loop {i+1}/{loop_count}: Entering battle phase.")
        battle_start_time = time.time()
        battle_duration = 100  # 3 minutes
        while time.time() < battle_start_time + battle_duration:
            remaining_time = int((battle_start_time + battle_duration) - time.time())
            #print(f"Loop {i+1}/{loop_count}: Battle phase, {remaining_time} seconds remaining.")
            action = select_action_with_probability(action_weights)
            action_name = action.__name__.replace('game_controls.', '')
            print(f"Loop {i+1}/{loop_count}: Performing action: {action_name}, {remaining_time} seconds remaining.")
            action(40)
            #sleep_time = 0.01
            #print(f"Loop {i+1}/{loop_count}: Sleeping for {sleep_time:.2f} seconds.")
            #time.sleep(sleep_time)

        sleep_time = 5
        print(f"Loop {i+1}/{loop_count}: Battle phase ended. Sleeping for {sleep_time} seconds, next page.")
        time.sleep(sleep_time)
        game_controls.next_page_paiwei(100)
        time.sleep(1)

        # Step 3: End game to lobby
        print(f"Loop {i+1}/{loop_count}: Ending game and returning to lobby.")
        sleep_time = 5 + 20 # 20秒自动返回，按钮在不同情况会变
        #game_controls.return_start(100)
        print(f"Loop {i+1}/{loop_count}: Sleeping for {sleep_time} seconds before next loop.")
        time.sleep(sleep_time)

    if do_mission:
        # Mission claiming process
        print(f"Loop {i+1}/{loop_count}: Claiming missions.")
        game_controls.claim_mission_paiwei(100)
        time.sleep(1)
        game_controls.claim_button_paiwei(100)
        sleep_time = 3
        print(f"Loop {i+1}/{loop_count}: Sleeping for {sleep_time} seconds after claiming missions.")
        time.sleep(sleep_time)
        game_controls.return_button_paiwei(100)
        game_controls.return_button_paiwei(100)
        print(f"Loop {i+1}/{loop_count}: Missions claimed and returned to main menu.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Automate game operations.")
    parser.add_argument("--loop_count", type=int, default=1, help="Number of times to loop the main process.")
    parser.add_argument("--do_mission", action="store_true", help="Whether to perform the mission claiming process.")
    args = parser.parse_args()

    main(args.loop_count, args.do_mission)
