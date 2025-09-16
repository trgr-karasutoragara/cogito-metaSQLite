**To the GitHub community:**

This project provides a system that supplements the inconvenience of thinking about metaphysical ontology and related concepts in natural language by using SQL.
Since it deals with philosophical terminology, it is published in **my native language**.
AI systems can understand and explain it, so please feel free to try using AI translation.
This project is released under the **MIT License**, which guarantees your freedom to translate, modify, and use it within the scope of the license.

<br>


# cogito-metaSQLite
形而上学存在論など高度に抽象的なことを直感的に操作するフレームワーク案

## これは何？
哲学者・研究者・学生・大学院生さんなどが、ハイデガーのように高度に抽象的に考えられるのに、言葉（英語や日本語など自然言語）の制約で苦労する問題への提案です。

ラッセルやヴィトゲンシュタインのコンセプトを踏襲しつつ、PythonとSQL（高次元のデータも柔軟に操作できる）を研究に使うことで、数式や論理式を使わなくても、自然言語の制約から自由になれます。

SQL自体も配布していますが、サンプルなので、内容は専門家がデザインなさって下さい。


``` 
蒸気機関の系譜 = [
    "蒸気機関",        # 個体・具体物
    "蒸気エンジン",    # 種類
    "熱機関",          # カテゴリ
    "動力機械",        # 上位分類
    "機械",            # 大分類
    "人工物",          # 自然/人工の区別
    "物体",            # 物理的実体
    "存在"             # 最上位概念
]

スマホの系譜 = [
    "スマホ",          # 個体・具体物
    "スマートフォン",  # 正式名称
    "携帯端末",        # 機能分類
    "通信機器",        # 用途分類
    "電子機器",        # 技術分類
    "人工物",          # 自然/人工の区別
    "物体",            # 物理的実体
    "存在"             # 最上位概念
]

テントウムシのハナちゃんの系譜 = [
    "テントウムシのハナちゃん",  # 個体
    "テントウムシ",            # 種（ナミテントウ等）
    "テントウムシ科",          # 科
    "甲虫目",                  # 目
    "昆虫綱",                  # 綱
    "節足動物門",              # 門
    "動物界",                  # 界
    "生物",                    # 生命体
    "存在"                     # 最上位概念
]

第三保育園の紅葉する楓の系譜 = [
    "第三保育園の紅葉する楓",  # 個体
    "楓",                     # 種
    "カエデ科",               # 科
    "ムクロジ目",             # 目
    "双子葉植物綱",           # 綱
    "被子植物門",             # 門
    "植物界",                 # 界
    "生物",                   # 生命体
    "存在"                    # 最上位概念
]
``` 

上記出典の私の記事: https://note.com/karasu_toragara/n/n9a233509e012






