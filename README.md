# AtRunner
与えられたソースコードが[AtCoder](https://atcoder.jp/)のサンプルケースをパスするかをチェックするツールです。
Python 3.7 以降が必要です。

## 使い方
後述の方法でインストールしたのち、以下の手順に従います。

1. 適当な言語でソースコードを作成し、`ProblemID.*`という名前で保存します。
    * `ProblemID`は問題ページ URL の末尾の文字列です。
    * 例えば、[abc128 A - Apple Pie](https://atcoder.jp/contests/abc128/tasks/abc128_a)をC言語で解く場合、`abc128_a.c` という名前でソースコードを保存してください。
2. ソースコードを保存したディレクトリで`atrunner [source_code]`を実行します。
    * 上記の例の場合、`atrunner abc128_a.c`を実行します。
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

もし以上の場合に当てはまらないならば、以下のいずれかの方法で設定ファイルを変更する必要があります。

1. 設定ファイルを作成し、`atrunner`の実行時に`--settings`オプションで設定ファイルへのパスを渡す
2. このリポジトリをクローンして`settings.json`を編集し、ローカルリポジトリのルートで`pip install -e .`を実行する。

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

## 制約
* ログインが必要なコンテストに対応していません。
* 一部の特殊な URL で開催されているコンテストに対応していません。
