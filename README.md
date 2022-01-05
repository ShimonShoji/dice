# ハンドチェッカーforサイコロポーカー

サイコロを5回振って、サイコロポーカーの役をチェックします。

# 環境

* Raspberry Pi 3B+
* Ubuntu 20.04 LTS
* ROS1


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

# roll.pyとhand.pyの見かた、使い方

* ### roll.pyについて
roll.pyを実行すると
```
press "e" to exit
press number-key(1~6) to send the number
press "r" to roll a dice:
```
と表示されるので指示に沿って、

"e"を入力すると通常のubuntuのコマンドプロンプトに戻り、

1から6の数字を入力するとその値がhand.pyに送られ、

"r"を入力すると6面のサイコロを振って、出た目の値がhand.pyに送られる。

* ### hand.pyについて
hand.pyを実行したウィンドウにはrollから受け取った値（サイコロの出た目）が１つずつ表示されていく。

5個の値を受け取った時点でその手札を昇順にソートした数字列が表示され、

また、手札の役と最も影響力のあるカードの値が一緒に表示される。

#### 例.
```
[INFO] [1641358804.182578]: 1st: 4
[INFO] [1641358804.544479]: 2nd: 2
[INFO] [1641358804.864866]: 3rd: 3
[INFO] [1641358805.168686]: 4th: 1
[INFO] [1641358805.493031]: 5th: 5
[INFO] [1641358805.504032]: hand: 1, 2, 3, 4, 5
[INFO] [1641358805.512706]: 5 high STRAIGHT
```


# 実行した結果
[動画](https://youtu.be/00aMZ1T5Yws)

# Update
no update yet

# 製作者
* Shimon Shoji
* Chiba Institute of Technology

# ライセンス
" ハンドチェッカーforサイコロポーカー " is under [BSD 2-Clause "Simplified" License](https://github.com/ShimonShoji/dice/blob/main/COPYING)
