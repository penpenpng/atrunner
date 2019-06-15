# AtRunner
与えられたソースコードが[AtCoder](https://atcoder.jp/)のサンプルケースをパスするかをチェックするツールです。自分用。
Python 3.7 以降が必要です。

## 使い方
後述の方法でインストールしたのち、以下の手順に従います。

1. `attemp [contestID] [language]`を実行し、作業ディレクトリを作成します。
    * `contestID`は例えば`abc123`, `arc099`のような文字列です。
2. 作業ディレクトリで`atrunner [source_code]`を実行します。
3. ソースコードの内容によって、例えば以下のような結果を得ることができます:

```
> atrunner abc128_a.c

* [AC] Test #1
* [AC] Test #2
* [WA] Test #3
| input:
|  32 21
|  
| expected output:
|  58
|  
| but got:
|  -1
|  

Passed cases: 2/3
```

その他、細かい使い方については`atrunner -h`を参照してください。

## インストール
あなたが Windows を使っていて、C (gcc), C++ (g++), Python しか書かないならば端末で以下を実行すれば十分です:

```
pip install git+https://github.com/penpenpng/atrunner
```

もし以上の場合に当てはまらないならば、次節を参考に、パッケージディレクトリ以下の`settings.json`を編集してください。

### 設定ファイルの作成
以下を参考にして作成してください。

```js
{
  "command": {
    // フォーマットは以下の通り
    "[拡張子]": {
      "compile": "コンパイルのために実行するコマンド (ファイル名の代わりに`{}`を使用可能)",
      "bin": "生成される実行可能ファイルの名前",
      "run": "実行のためのコマンド"
    },
    // 以下はサンプル
    "c": {
      "compile": "gcc {}",
      "bin": "a.exe",
      "run": "a.exe"
    },
    "cpp": {
      "compile": "g++ {}",
      "bin": "a.exe",
      "run": "a.exe"
    },
    "py": {
      // コンパイルが不要な言語では compile, bin を省略する
      "run": "python {}"
    }
  }
}
```

## アンインストール
端末で以下を実行してください:
```
pip uninstall atrunner
```

## TODO
* ログインが必要なコンテストへの対応。
* `attemp`のユーザ設定機能の追加。
* 一部の特殊な URL で開催されているコンテストへの対応。
* 出力例が唯一解でない場合に警告する。
