# garlic-diary-keeper

にんにく日記をTwitterに呟くBot

Twitter：https://twitter.com/garlic_diary

## 環境構築

### 実行環境

|環境|バージョン|
|---|---|
|python|3.7.2|
|pip|22.0.3|

```
$ pip install -r requirements.txt
```

### 環境変数

以下の環境変数をすべてセットする。

Key 一覧：https://drive.google.com/file/d/18vC2pyuCw_srKAKiEbNMrlvyWINouokWnNn_VD8uyq8/view

|KEY|VALUE|
|---|---|
|TWITTER_API_KEY| Twitter API キー |
|TWITTER_API_KEY_SECRET| Twitter API シークレット|
|TWITTER_ACCESS_TOKEN| Twitter アクセストークン |
|TWITTER_ACCESS_TOKEN_SECRET| Twitter アクセストークンシークレット |
|GROWTH_START_DATE| 栽培開始日 |

## 実行

```
$ python src/garlic_diary_keeper/main.py
```
