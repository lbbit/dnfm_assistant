import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QLabel, QSpinBox, QComboBox, QTextEdit, QCheckBox
from PyQt5.QtWidgets import QSystemTrayIcon, QMenu, QAction
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtGui import QFont
from PyQt5.QtGui import QIcon
import game_controls
import daluandou
import jidou
import paiwei
import tangguo
import time
import os

class Worker(QThread):
    log_signal = pyqtSignal(str)
    finish_signal = pyqtSignal()
    def __init__(self, mode, loop_count, do_mission):
        super(Worker, self).__init__()
        self.mode = mode
        self.loop_count = loop_count
        self.do_mission = do_mission
        self.running = True

    def run(self):
        self.log_signal.emit(f"自动化任务开始, {self.mode}, {self.loop_count}, {self.do_mission}...")
        if self.mode == "paiwei":
            paiwei.main(self.loop_count, self.do_mission)
        elif self.mode == "daluandou":
            daluandou.main(self.loop_count, self.do_mission)
        elif self.mode == "jidou":
            jidou.main(self.loop_count, self.do_mission)
        elif self.mode == "tangguo":
            tangguo.main(self.loop_count, self.do_mission)
        elif self.mode == "all_loop": # 从决斗界面开始三种循环执行
            all_loop = 0
            while all_loop != self.loop_count:
                # 排位
                print(f"all_loop {all_loop}/{self.loop_count} paiwei start")
                game_controls.juedou_select_paiwei()
                time.sleep(4)
                paiwei.main(1, self.do_mission)
                time.sleep(4)
                game_controls.common_return()
                print(f"all_loop {all_loop}/{self.loop_count} paiwei end")
                time.sleep(4)
                # 激斗
                print(f"all_loop {all_loop}/{self.loop_count} jidou start")
                game_controls.juedou_select_jidou()
                time.sleep(7)
                jidou.main(1, self.do_mission)
                time.sleep(4)
                game_controls.common_return()
                print(f"all_loop {all_loop}/{self.loop_count} jidou end")
                time.sleep(7)
                # 大乱斗
                print(f"all_loop {all_loop}/{self.loop_count} daluandou start")
                game_controls.juedou_select_daluandou()
                time.sleep(4)
                daluandou.main(1, self.do_mission)
                time.sleep(4)
                game_controls.common_return()
                print(f"all_loop {all_loop}/{self.loop_count} daluandou end")
                time.sleep(4)
                all_loop += 1
        self.log_signal.emit("自动化任务完成。")
        self.stop()
        self.finish_signal.emit()

    def stop(self):
        self.running = False

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # 设置窗口图标
        if hasattr(sys, '_MEIPASS'):
            self.icon_path = os.path.join(sys._MEIPASS, 'dnf.png')
        else:
            self.icon_path = 'dnf.png'
        self.setWindowIcon(QIcon(self.icon_path))
        self.initUI()
        self.worker = None
        self.createTrayIcon()


    def createTrayIcon(self):
        self.trayIcon = QSystemTrayIcon(QIcon(self.icon_path), self)
        self.trayIcon.setToolTip("DNF手游PK助手--lbb")

        showAction = QAction("Show", self)
        showAction.triggered.connect(self.showWindow)
        quitAction = QAction("Quit", self)
        quitAction.triggered.connect(self.quitApplication)

        trayMenu = QMenu()
        trayMenu.addAction(showAction)
        trayMenu.addAction(quitAction)

        self.trayIcon.setContextMenu(trayMenu)
        self.trayIcon.activated.connect(self.onTrayIconActivated)

        self.trayIcon.show()

    def onTrayIconActivated(self, reason):
        if reason == QSystemTrayIcon.DoubleClick:
            self.showWindow()
    def closeEvent(self, event):
        event.ignore()
        self.hide()
        self.trayIcon.showMessage(
            "提示",
            "程序已最小化到系统托盘。",
            QSystemTrayIcon.Information,
            1000
        )

    def showWindow(self):
        self.showNormal()
        self.activateWindow()

    def quitApplication(self):
        self.trayIcon.hide()
        QApplication.quit()
    def initUI(self):
        self.setWindowTitle("DNF手游PK助手--lbb")
        layout = QVBoxLayout()

        # Input for loop count
        self.loop_count_input_lbl = QLabel("自动执行轮数:", self)
        layout.addWidget(self.loop_count_input_lbl)
        self.loop_count_input = QSpinBox(self)
        # 设置范围
        self.loop_count_input.setMinimum(1)  # 最小值
        self.loop_count_input.setMaximum(9999)  # 最大值
        # 设置默认值
        self.loop_count_input.setValue(1)
        layout.addWidget(self.loop_count_input)

        # Checkbox for mission
        self.do_mission_input = QCheckBox("自动领取任务奖励", self)
        layout.addWidget(self.do_mission_input)

        # Checkbox for exchange w h
        self.exchange_w_h = QCheckBox("分辨率长度和宽度颠倒", self)
        layout.addWidget(self.exchange_w_h)
        self.exchange_w_h.setEnabled(False);

        # Dropdown for mode selection
        self.mode_input = QComboBox(self)
        self.mode_input.addItem("排位(从排位界面启动)", "paiwei")
        self.mode_input.addItem("大乱斗(从休闲模式界面启动)", "daluandou")
        self.mode_input.addItem("激斗(从激斗界面启动)", "jidou")
        self.mode_input.addItem("糖果(从糖果游戏中启动)", "tangguo")
        #self.mode_input.addItem("所有循环(从对决界面启动)", "all_loop")
        layout.addWidget(self.mode_input)

        # Start/Stop button
        self.start_stop_btn = QPushButton("开始", self)
        self.start_stop_btn.clicked.connect(self.start_or_stop)
        layout.addWidget(self.start_stop_btn)

        # TextEdit for logs
        self.log_output = QTextEdit(self)
        self.log_output.setReadOnly(True)
        layout.addWidget(self.log_output)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)
        self.resize(400, 300)

    def start_or_stop(self):
        if self.worker is None or not self.worker.isRunning():
            ex_w_h = self.exchange_w_h.isChecked()
            ret, w, h = game_controls.update_screen_resolution(ex_w_h)
            if ret == False:
                self.update_log("无法获取屏幕分辨率，请检查是否已连接手机并打开USB调试，"
                                "如果是macos或linux系统需要安装adb工具。")
                return
            self.update_log(f"获取屏幕分辨率成功，分辨率为：{w}x{h}")
            loop_count = int(self.loop_count_input.text())
            if loop_count <= 0:
                loop_count = 1
            do_mission = self.do_mission_input.isChecked()
            mode = self.mode_input.currentData()
            self.worker = Worker(mode, loop_count, do_mission)
            self.worker.log_signal.connect(self.update_log)
            self.worker.finish_signal.connect(self.work_finished_slot)
            self.worker.start()
            self.update_log(f"开始自动进行：{self.mode_input.currentText()}，"
                            f"执行轮数：{loop_count}, 自动领取任务奖励：{do_mission}")
            self.start_stop_btn.setText("停止")
        else:
            self.update_log(f"手动停止执行...")
            self.worker.stop()
            self.worker.terminate()
            self.worker.wait()
            self.start_stop_btn.setText("开始")

    def update_log(self, message):
        self.log_output.append(message)
    def work_finished_slot(self):
        print("任务完成。。。")
        if self.worker is not None:
            self.worker.stop()
            self.worker.terminate()
            self.worker.wait()
        self.start_stop_btn.setText("开始")


if __name__ == "__main__":
    #'''
    print("正在启动程序界面，请等待，程序运行期间请勿关闭此窗口...")
    app = QApplication(sys.argv)
    font = QFont('Arial', 13)  # 选择字体和大小
    font.setBold(True)
    app.setFont(font)
    win = MainWindow()
    win.show()
    print("窗口启动成功...")
    sys.exit(app.exec_())
    #'''
