# chatbotAIML
pythonでAIMLを動作させます。
日本語対応のため、janomeの形態素解析を用いて単語の間に空白をいれました。
実行方法は以下の通り
```
python main.py
```
作成したAIMLファイルは以下のディレクトリに入れることで読み込まれます。
```
chatbotAIML/aiml/wolf/
```

# converter.py
SUNABAなどで作成したファイルを、上記のpythonプログラムで動作するよう、単語の間に空白をいれます。
実行方法は以下の通り
```
python converter.py [変換対象ファイル名] [出力ファイル名]
```
aaa