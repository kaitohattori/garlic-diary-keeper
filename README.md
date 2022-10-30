# garlic-diary-keeper

にんにく日記をTwitterに呟くBot

Twitter：https://twitter.com/garlic_diary

## 使い方

### 環境変数

以下の環境変数をすべてセットする。

https://docs.google.com/document/d/18vC2pyuCw_srKAKiEbNMrlvyWINouokWnNn_VD8uyq8/view

|KEY|VALUE|
|---|---|
|TWITTER_API_KEY| API キー |
|TWITTER_API_KEY_SECRET| API シークレット|
|TWITTER_ACCESS_TOKEN| アクセストークン |
|TWITTER_ACCESS_TOKEN_SECRET| アクセストークンシークレット |

### 環境構築

|環境|バージョン|
|---|---|
|python|3.7.2|
|pip|22.0.3|

```
$ pip install -r requirements.txt
```

### 実行

```
$ python src/garlic_diary_keeper/main.py
```
