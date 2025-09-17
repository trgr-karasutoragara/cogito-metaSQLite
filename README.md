**To the GitHub community:**

This project provides a system that supplements the inconvenience of thinking about metaphysical ontology and related concepts in natural language by using SQL.
Since it deals with philosophical terminology, it is published in **my native language**.
AI systems can understand and explain it, so please feel free to try using AI translation.
This project is released under the **MIT License**, which guarantees your freedom to translate, modify, and use it within the scope of the license.

<br>


# cogito-metaSQLite
形而上学存在論など高度に抽象的なことを直感的に操作するフレームワーク案

<br>

## これは何？
哲学者・研究者・学生・大学院生さんなどが、ハイデガーのように高度に抽象的に考えられるのに、言葉（英語や日本語など自然言語）の制約で苦労する問題への提案です。

ラッセルやヴィトゲンシュタインのコンセプトを踏襲しつつ、PythonとSQL（高次元のデータも柔軟に操作できる）を研究に使うことで、数式や論理式を使わなくても、自然言語の制約から自由になれます。

SQL自体も配布していますが、サンプルなので、内容は専門家がデザインなさって下さい。

<br>


### 自然言語の構造問題例

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

<br>

## 配布ファイルの同一性検証用のSHA256ハッシュ値
| SHA256ハッシュ値 | ファイル名 |
|----------|----------|
| fd95abe097eef0383e8f1dac5b36799bd02c4366ce8aa1bc0e6c8c75789563fd | [metaphysics.db](https://github.com/trgr-karasutoragara/cogito-metaSQLite/blob/main/metaphysics.db) |
| d222ca8321a1866bddc45866f3861253aefac80b19132756546512328352415a | [metaphysics_python.py](https://github.com/trgr-karasutoragara/cogito-metaSQLite/blob/main/metaphysics_python.py) |
| 87edf725b0842fb0df2f134a28345dc4d3aa6931dc89ca6212c3edeb4a807bd1 | [metaphysics_export.json](https://github.com/trgr-karasutoragara/cogito-metaSQLite/blob/main/metaphysics_export.json) |
| 865b8bdfd8d2580331f6bf5f85e246bf28d56c38b1261a5457cd4e9a5b40854f | [metaphysics_sample_queries.sql](https://github.com/trgr-karasutoragara/cogito-metaSQLite/blob/main/metaphysics_sample_queries.sql) |

<br>

## クイックスタート
1. [metaphysics_python.py](https://github.com/trgr-karasutoragara/cogito-metaSQLite/blob/main/metaphysics_python.py) をダウンロードする
2. `Python3 metaphysics_python.py`と実行する
3. [metaphysics.db](https://github.com/trgr-karasutoragara/cogito-metaSQLite/blob/main/metaphysics.db) と[metaphysics_export.json](https://github.com/trgr-karasutoragara/cogito-metaSQLite/blob/main/metaphysics_export.json)が生成される（セットアップされる）
4. [metaphysics.db](https://github.com/trgr-karasutoragara/cogito-metaSQLite/blob/main/metaphysics.db) をSQL文で操作

<br>

## .schema
```
sqlite> .schema
CREATE TABLE existence_concepts (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                cultural_context TEXT,
                definition TEXT,
                abstraction_level INTEGER,
                temporal_aspect BOOLEAN,
                spatial_aspect BOOLEAN,
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP
            );
CREATE TABLE nothingness_concepts (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                cultural_context TEXT,
                definition TEXT,
                type TEXT,
                relation_to_existence TEXT,
                paradox_level INTEGER
            );
CREATE TABLE time_concepts (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                cultural_context TEXT,
                definition TEXT,
                linearity BOOLEAN,
                objectivity TEXT,
                measurement_unit TEXT,
                arrow_direction TEXT
            );
CREATE TABLE space_concepts (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                cultural_context TEXT,
                definition TEXT,
                dimensionality INTEGER,
                curvature TEXT,
                absoluteness TEXT,
                boundaries BOOLEAN
            );
CREATE TABLE consciousness_concepts (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                cultural_context TEXT,
                definition TEXT,
                embodiment TEXT,
                unity BOOLEAN,
                privacy_level INTEGER,
                computational BOOLEAN
            );
CREATE TABLE substance_concepts (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                cultural_context TEXT,
                definition TEXT,
                independence_level INTEGER,
                materiality TEXT,
                divisibility BOOLEAN,
                permanence_level INTEGER
            );
CREATE TABLE universal_concepts (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                cultural_context TEXT,
                definition TEXT,
                realism_level INTEGER,
                instantiation_type TEXT,
                scope TEXT
            );
CREATE TABLE divine_concepts (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                cultural_context TEXT,
                definition TEXT,
                transcendence_level INTEGER,
                immanence_level INTEGER,
                personality BOOLEAN,
                causality_role TEXT
            );
CREATE TABLE good_concepts (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                cultural_context TEXT,
                definition TEXT,
                objectivity TEXT,
                relation_to_being TEXT,
                measurement_scale TEXT,
                source TEXT
            );
CREATE TABLE dao_concepts (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                cultural_context TEXT,
                definition TEXT,
                expressability BOOLEAN,
                action_principle TEXT,
                universality_scope TEXT,
                knowability TEXT
            );
CREATE TABLE concept_relations (
                id INTEGER PRIMARY KEY,
                source_table TEXT NOT NULL,
                source_id INTEGER NOT NULL,
                target_table TEXT NOT NULL,
                target_id INTEGER NOT NULL,
                relation_type TEXT NOT NULL,
                strength REAL DEFAULT 0.5,
                cultural_specificity TEXT,
                logical_necessity TEXT,
                temporal_stability TEXT,
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP
            );
CREATE TABLE contradictions (
                id INTEGER PRIMARY KEY,
                concept1_table TEXT NOT NULL,
                concept1_id INTEGER NOT NULL,
                concept2_table TEXT NOT NULL,
                concept2_id INTEGER NOT NULL,
                contradiction_type TEXT,
                resolution_attempts TEXT,
                unresolved BOOLEAN DEFAULT TRUE,
                philosopher_comments TEXT
            );
CREATE TABLE cultural_interpretations (
                id INTEGER PRIMARY KEY,
                base_concept_table TEXT NOT NULL,
                base_concept_id INTEGER NOT NULL,
                culture TEXT NOT NULL,
                interpretation TEXT,
                emphasis_points TEXT,
                unique_aspects TEXT,
                historical_evolution TEXT
            );
sqlite> 
```


<br>

## SQLの動作例
```
sqlite3 metaphysics.db

# 任意のクエリをコピペして実行
.mode column
.headers on
# ←ここに metaphysics_sample_queries.sql からコピペ

```

### 1
```
ORDER BY 神依存概念数 DESC, 平均依存強度 DESC;es', 'causes', 'sustains')urce_id = dc.id
概念分類                  概念名          文化的背景            抽象度  同文化圏内の自立概念数
--------------------  -----------  ---------------  ---  -----------
dao_concepts          道            daoist           10   2          
existence_concepts    実在           western          10   4          
existence_concepts    Being        western          10   4          
dao_concepts          直観           western_bergson  10   1          
existence_concepts    有            buddhist         9    3          
nothingness_concepts  空            buddhist         9    3          
nothingness_concepts  無            daoist           8    2          
dao_concepts          ダルマ          buddhist         7    3          
nothingness_concepts  虚無           western          7    4          
nothingness_concepts  Nothingness  western          6    4          
dao_concepts          ロゴス          western_ancient  5    1          
existence_concepts    犬のタロー        universal        0    1          
概念領域                神依存概念数  平均依存強度  依存文化圏            
------------------  ------  ------  -----------------
existence_concepts  1       0.7     western_christian
sqlite> 
```

<br>

### 2
```
ORDER BY 平均関係強度 DESC, 関係数 DESC;ation_type, cr.logical_necessity
文化圏      概念タイプ        平均抽象度  概念数  時間性比率  空間性比率  概念総合力
-------  -----------  -----  ---  -----  -----  -----
eastern  existence    9.0    1    1.0    1.0    9.0  
eastern  nothingness  8.5    2    0.8    0.3    17.0 
western  existence    10.0   3    0.67   0.67   30.0 
western  nothingness  6.5    2    0.5    0.0    13.0 
文化特有性              関係タイプ              関係数  平均関係強度  最小強度  最大強度  論理的必然性      時間的安定性パターン
-----------------  -----------------  ---  ------  ----  ----  ----------  ----------
daoist             generates          1    0.9     0.9   0.9   necessary   eternal   
daoist             manifests_through  1    0.9     0.9   0.9   necessary   eternal   
buddhist           is_empty_of        1    0.8     0.8   0.8   necessary   eternal   
western_christian  creates            1    0.7     0.7   0.7   contingent  historical
western_modern     realizes           1    0.6     0.6   0.6   contingent  contextual
sqlite> 
```

<br>

### 3

```
LIMIT 15;総合安定性スコア DESC, 関係強度 DESC度がある関係のみd AND cr.target_table = 'd
概念分野                    概念名  総接続数  平均接続強度  ハブ重要度  文化的背景            
----------------------  ---  ----  ------  -----  -----------------
nothingness_concepts    無    2     0.9     1.8    daoist           
existence_concepts      有    2     0.85    1.7    buddhist         
existence_concepts      存在   2     0.65    1.3    western          
dao_concepts            道    1     0.9     0.9    daoist           
nothingness_concepts    空    1     0.8     0.8    buddhist         
divine_concepts         神    1     0.7     0.7    western_christian
consciousness_concepts  意識   1     0.6     0.6    western_modern   
無概念名  無文化     パラドックス度  関係タイプ      関係強度  論理的必然性     相互作用概念  相互作用文化    パラドックス影響度  パラドックス分類 
----  ------  -------  ---------  ----  ---------  ------  --------  ---------  ---------
無     daoist  8        generates  0.9   necessary  有       buddhist  7.2        文化間パラドックス
起点概念                    関係                 終点概念                    関係強度  論理的必然性      時間的安定性      文化特有性              総合安定性スコア
----------------------  -----------------  ----------------------  ----  ----------  ----------  -----------------  --------
nothingness_concepts.無  generates          existence_concepts.有    0.9   necessary   eternal     daoist             0.9     
dao_concepts.道          manifests_through  nothingness_concepts.無  0.9   necessary   eternal     daoist             0.9     
existence_concepts.有    is_empty_of        nothingness_concepts.空  0.8   necessary   eternal     buddhist           0.8     
                        creates            existence_concepts.存在   0.7   contingent  historical  western_christian  0.392   
                        realizes           existence_concepts.存在   0.6   contingent  contextual  western_modern     0.252   
sqlite> 
```

<br>

# License
[MIT License](https://github.com/trgr-karasutoragara/cogito-metaSQLite/edit/main/README.md)

<br>

# Repository Policy
I develop prototypes with a focus on ethics.
There are no plans for maintenance or support.
The project is released under the MIT License, so feel free to modify it within the scope of the license.
Instead of providing support, I create new prototypes to solve emerging problems.

<br>

# Author Declaration
I am an unaffiliated volunteer individual, and there is no conflict of interest in this project.





