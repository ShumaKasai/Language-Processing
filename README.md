# Language-Processing

数値解析学の課題用リポジトリ

## ダウンロード
```bash
$ git clone -b main https://github.com/ShumaKasai/Language-Processing.git
$ cd Language-Processing
```

## 必要なソフトウェア
- Python 3.7～3.10

## 使用方法
### problem1
`test.txt` に入力した英文の改行、空白、アルファベット小文字以外を空白に変換して `new_test.txt` に出力する
```bash
$ python problem1
```
### problem2
`test.txt` に入力した英文をアルファベット小文字だけの文字列にし、その数を数えて多い順に標準出力に出力する
```bash
$ python problem2
Counter({'e': 451, 't': 339, 'a': 300, 'h': 256, 'n': 234, 'd': 233, 'i': 198, 'r': 186, 'o': 167, 's': 131, 'g': 114, 'l': 94, 'f': 87, 'm': 65, 'w': 62, 'v': 59, 'u': 44, 'y': 42, 'b': 32, 'c': 31, 'p': 25, 'k': 16, 'x': 1})
```
### problem4
`test.txt` に入力した英文をアルファベット小文字だけの文字列にし、そこからランダムに100文字出力する
```bash
$ python problem4
nwwefhidtmthfrfolgmekeeihtntdiatagnoosgtyuaaetasntgsaghthhniteysdinphdenomdveboiewetftrelftesdahsvls
```

## ライセンス
- このソフトウェアパッケージは、3条項BSDライセンスの下、再頒布および使用が許可されます.

© 2022 Shuma Kasai