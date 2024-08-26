import time
import argparse
import game_controls


def main(loop_count=1, do_mission=False, action_weights=None):
    print(f"tangguo: start, loop_count: {loop_count} min")

    # 计算结束时间
    total_time = 60 * loop_count
    time_end = time.time() + total_time
    last_print_time = time.time()  # 初始化最后一次打印时间

    # 循环loop_count分钟持续运行
    while time.time() <= time_end:
        # 执行游戏控制操作
        for i in range(20):
            game_controls.tangguo_down()
        game_controls.tangguo_tryagain()

        # 检查是否已经过去5秒钟
        current_time = time.time()
        if current_time - last_print_time >= 5:
            elapsed_time = current_time - (time_end - total_time)
            remaining_time = time_end - current_time
            print(f"Elapsed Time: {elapsed_time:.2f} seconds, Remaining Time: {remaining_time:.2f} seconds")
            last_print_time = current_time  # 更新最后一次打印时间

    print("tangguo Loop completed.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Automate game operations.")
    parser.add_argument("--loop_count", type=int, default=1, help="Number of times to loop the main process.")
    parser.add_argument("--do_mission", action="store_true", help="Whether to perform the mission claiming process.")
    args = parser.parse_args()

    main(args.loop_count, args.do_mission)
