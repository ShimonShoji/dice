# ハンドチェッカーforサイコロポーカー
roll dices and check the hand of dice-poker
６面のサイコロを振って、サイコロポーカーの役をチェックします。

# 環境

* Raspberry Pi 3B+
* Ubuntu 20.04 LTS


# コードの使用方法

* セットアップ
```
$ cd ~/catkin_ws/src/
$ git clone git@github.com:ShimonShoji/dice.git
$ cd dice/scripts/
$ chmod +x roll.py
$ chmod +x hand.py
```

* roll.pyの実行
```
$ rosrun dice roll.py
```

* hand.pyの実行(別ウィンドウにて)
```
$ rosrun dice hand.py
```

# roll.pyとhand.pyの使い方
roll.pyを実行すると
```
press "e" to exit
press number-key(1~6) to send the number
press "r" to roll a dice:
```
と出てくるので指示に沿って、
"e"を入力すると通常のubuntuのコマンドプロンプトに戻り、
1から6の数字キーを入力するとその値がhand.pyに送られ、
"r"を入力すると6面のサイコロを振って、出た値がhand.pyに送られる。

hand.pyを実行したウィンドウには受け取った値（サイコロの出た目）が映し出され、
5個の値を受け取った時点でその手札を昇順にソートし、まとめて映し出され、
その手札の役と、最も影響力のあるカードの値が映し出される。


# ムカデロボ本体とその動作
[動画](https://youtu.be/00aMZ1T5Yws)

# Update
no update yet

# 製作者
* Shimon Shoji
* Chiba Institute of Technology

# 参考　

# ライセンス
" ムカデロボ用デバイスドライバー " is under [GNU General Public License v3.0](https://github.com/ShimonShoji/device_driver/blob/main/COPYING)
