# Robosys2019_task2
Raspberry Piでのサーボ制御をROSを用いて行うプログラムである。
# 作成したプログラムについて
## 使用方法
~~~
$ roscore &
$ cd ~/ros_catkin_ws/
$ catkin_make
$ source devel/setup.bash
$ roscd mypkg/scripts/
$ chmod +x set.sh
$ rosrun mypkg count.py &
$ rosrun mypkg twice.py
~~~
終了するときは ctrl+c を押す
## 処理の流れ
* パブリッシャで、トピックとして設定した"count_up"にサーボモータの可動範囲である500~2500の値を100ずつ増加させたり減少させたりした値を書き込む
* その後サブスクライバで、トピックを購読してその値からサーボモータに指令値を送る

# 動画URL
https://youtu.be/C8O9HrlY7nM
