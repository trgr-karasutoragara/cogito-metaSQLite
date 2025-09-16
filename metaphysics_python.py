#!/usr/bin/env python3
"""
形而上学概念データベースの操作スクリプト
SQLiteを使用して複雑な哲学概念とその関係性を管理する
"""

import sqlite3
import json
import datetime
from typing import List, Dict, Any, Optional, Tuple
from dataclasses import dataclass
from contextlib import contextmanager

@dataclass
class ConceptRelation:
    """概念間の関係を表すデータクラス"""
    source_table: str
    source_id: int
    target_table: str
    target_id: int
    relation_type: str
    strength: float = 0.5
    cultural_specificity: Optional[str] = None
    logical_necessity: str = 'unknown'
    temporal_stability: str = 'contextual'

class MetaphysicsDB:
    """形而上学概念データベースの操作クラス"""
    
    def __init__(self, db_path: str = "metaphysics.db"):
        self.db_path = db_path
        self.setup_database()
    
    @contextmanager
    def get_connection(self):
        """データベース接続のコンテキストマネージャー"""
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row  # 辞書ライクなアクセス
        try:
            yield conn
        finally:
            conn.close()
    
    def setup_database(self):
        """データベースとテーブルを作成"""
        with self.get_connection() as conn:
            cursor = conn.cursor()
            
            # 全テーブル作成SQL
            tables_sql = """
            -- 1. 存在概念テーブル
            CREATE TABLE IF NOT EXISTS existence_concepts (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                cultural_context TEXT,
                definition TEXT,
                abstraction_level INTEGER,
                temporal_aspect BOOLEAN,
                spatial_aspect BOOLEAN,
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP
            );

            -- 2. 無・空・虚無概念テーブル  
            CREATE TABLE IF NOT EXISTS nothingness_concepts (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                cultural_context TEXT,
                definition TEXT,
                type TEXT,
                relation_to_existence TEXT,
                paradox_level INTEGER
            );

            -- 3. 時間概念テーブル
            CREATE TABLE IF NOT EXISTS time_concepts (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                cultural_context TEXT,
                definition TEXT,
                linearity BOOLEAN,
                objectivity TEXT,
                measurement_unit TEXT,
                arrow_direction TEXT
            );

            -- 4. 空間概念テーブル
            CREATE TABLE IF NOT EXISTS space_concepts (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                cultural_context TEXT,
                definition TEXT,
                dimensionality INTEGER,
                curvature TEXT,
                absoluteness TEXT,
                boundaries BOOLEAN
            );

            -- 5. 意識・精神概念テーブル
            CREATE TABLE IF NOT EXISTS consciousness_concepts (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                cultural_context TEXT,
                definition TEXT,
                embodiment TEXT,
                unity BOOLEAN,
                privacy_level INTEGER,
                computational BOOLEAN
            );

            -- 6. 実体概念テーブル
            CREATE TABLE IF NOT EXISTS substance_concepts (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                cultural_context TEXT,
                definition TEXT,
                independence_level INTEGER,
                materiality TEXT,
                divisibility BOOLEAN,
                permanence_level INTEGER
            );

            -- 7. 普遍概念テーブル
            CREATE TABLE IF NOT EXISTS universal_concepts (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                cultural_context TEXT,
                definition TEXT,
                realism_level INTEGER,
                instantiation_type TEXT,
                scope TEXT
            );

            -- 8. 神・絶対者概念テーブル  
            CREATE TABLE IF NOT EXISTS divine_concepts (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                cultural_context TEXT,
                definition TEXT,
                transcendence_level INTEGER,
                immanence_level INTEGER,
                personality BOOLEAN,
                causality_role TEXT
            );

            -- 9. 善概念テーブル
            CREATE TABLE IF NOT EXISTS good_concepts (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                cultural_context TEXT,
                definition TEXT,
                objectivity TEXT,
                relation_to_being TEXT,
                measurement_scale TEXT,
                source TEXT
            );

            -- 10. 道（タオ）・根本原理テーブル
            CREATE TABLE IF NOT EXISTS dao_concepts (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                cultural_context TEXT,
                definition TEXT,
                expressability BOOLEAN,
                action_principle TEXT,
                universality_scope TEXT,
                knowability TEXT
            );

            -- リレーションシップテーブル
            CREATE TABLE IF NOT EXISTS concept_relations (
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

            -- 矛盾・パラドックステーブル
            CREATE TABLE IF NOT EXISTS contradictions (
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

            -- 文化的解釈バリエーションテーブル
            CREATE TABLE IF NOT EXISTS cultural_interpretations (
                id INTEGER PRIMARY KEY,
                base_concept_table TEXT NOT NULL,
                base_concept_id INTEGER NOT NULL,
                culture TEXT NOT NULL,
                interpretation TEXT,
                emphasis_points TEXT,
                unique_aspects TEXT,
                historical_evolution TEXT
            );
            """
            
            # SQLを分割して実行
            for statement in tables_sql.split(';'):
                if statement.strip():
                    cursor.execute(statement)
            
            conn.commit()
            print("✅ データベーステーブルを作成しました")

    def insert_sample_data(self):
        """サンプルデータを挿入"""
        with self.get_connection() as conn:
            cursor = conn.cursor()
            
            # テーブルごとに明示的にカラムを指定してサンプルデータを挿入
            
            # 存在概念
            cursor.executemany("""
                INSERT OR REPLACE INTO existence_concepts 
                (name, cultural_context, definition, abstraction_level, temporal_aspect, spatial_aspect)
                VALUES (?, ?, ?, ?, ?, ?)
            """, [
                ('存在', 'western', 'ハイデガーの根本概念、現存在の基盤', 10, True, True),
                ('有', 'buddhist', '一切法有、現象界の存在性', 9, True, True),
                ('実在', 'western', 'プラトンのイデア界の実体', 10, False, False),
                ('犬のタロー', 'universal', '具体的個体の存在例', 0, True, True),
                ('Being', 'western', 'ハイデガーのSein概念', 10, True, True),
            ])
            
            conn.commit()
            
            # 無・空・虚無概念
            cursor.executemany("""
                INSERT OR REPLACE INTO nothingness_concepts
                (name, cultural_context, definition, type, relation_to_existence, paradox_level)
                VALUES (?, ?, ?, ?, ?, ?)
            """, [
                ('無', 'daoist', '道教の根本概念、有を生み出す源', 'daoist_wu', '有を生成する', 8),
                ('空', 'buddhist', '縁起による実体の空性', 'buddhist_emptiness', '固定実体の否定', 9),
                ('虚無', 'western', '絶対的な無、存在の完全否定', 'absolute_void', '存在との対立', 7),
                ('Nothingness', 'western', 'サルトルの無概念', 'existential_negation', '意識による無化', 6),
            ])
            
            # 時間概念
            cursor.executemany("""
                INSERT OR REPLACE INTO time_concepts
                (name, cultural_context, definition, linearity, objectivity, measurement_unit, arrow_direction)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            """, [
                ('時間', 'western_newton', 'ニュートンの絶対時間', True, 'absolute', 'second', 'forward'),
                ('時空', 'western_einstein', 'アインシュタインの相対論的時空', True, 'relative', 'spacetime_interval', 'forward'),
                ('劫', 'buddhist', '仏教の宇宙論的時間単位', False, 'illusory', 'kalpa', 'none'),
                ('永遠の今', 'mystical', '時間を超越した瞬間', False, 'subjective', 'moment', 'none'),
            ])
            
            # 神・絶対者概念
            cursor.executemany("""
                INSERT OR REPLACE INTO divine_concepts
                (name, cultural_context, definition, transcendence_level, immanence_level, personality, causality_role)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            """, [
                ('神', 'western_christian', 'キリスト教の創造神', 10, 3, True, 'first_cause'),
                ('ブラフマン', 'hindu', 'ウパニシャッドの根本実在', 10, 10, False, 'sustaining_cause'),
                ('道', 'daoist', '老子の根本原理', 8, 10, False, 'no_cause'),
            ])
            
            # 道・根本原理概念
            cursor.executemany("""
                INSERT OR REPLACE INTO dao_concepts
                (name, cultural_context, definition, expressability, action_principle, universality_scope, knowability)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            """, [
                ('道', 'daoist', '老子の道徳経の根本概念', False, 'wu_wei', 'cosmic', 'experiential_only'),
                ('ダルマ', 'buddhist', '仏教の法・真理', True, 'dharma', 'universal', 'partially_knowable'),
                ('ロゴス', 'western_ancient', 'ヘラクレイトスの理性原理', True, 'logos', 'cosmic', 'knowable'),
            ])
            
            # 意識・精神概念
            cursor.executemany("""
                INSERT OR REPLACE INTO consciousness_concepts
                (name, cultural_context, definition, embodiment, unity, privacy_level, computational)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            """, [
                ('意識', 'western_modern', '現代哲学の心の問題', 'embodied', True, 8, False),
                ('心', 'buddhist', '仏教の心識論', 'both', False, 6, False),
                ('魂', 'western_ancient', 'プラトンの霊魂論', 'disembodied', True, 10, False),
            ])
            
            # 関係性データの挿入
            relations = [
                ConceptRelation('nothingness_concepts', 1, 'existence_concepts', 2, 'generates', 0.9, 'daoist', 'necessary', 'eternal'),
                ConceptRelation('existence_concepts', 2, 'nothingness_concepts', 2, 'is_empty_of', 0.8, 'buddhist', 'necessary', 'eternal'),
                ConceptRelation('divine_concepts', 1, 'existence_concepts', 1, 'creates', 0.7, 'western_christian', 'contingent', 'historical'),
                ConceptRelation('dao_concepts', 1, 'nothingness_concepts', 1, 'manifests_through', 0.9, 'daoist', 'necessary', 'eternal'),
                ConceptRelation('consciousness_concepts', 1, 'existence_concepts', 1, 'realizes', 0.6, 'western_modern', 'contingent', 'contextual'),
            ]
            
            for rel in relations:
                cursor.execute("""
                    INSERT INTO concept_relations 
                    (source_table, source_id, target_table, target_id, relation_type, 
                     strength, cultural_specificity, logical_necessity, temporal_stability)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
                """, (rel.source_table, rel.source_id, rel.target_table, rel.target_id, 
                      rel.relation_type, rel.strength, rel.cultural_specificity, 
                      rel.logical_necessity, rel.temporal_stability))
            
            conn.commit()
            print("✅ サンプルデータを挿入しました")

    def query_cross_cultural_concepts(self) -> List[Dict]:
        """文化横断的概念を検索"""
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT 
                    ec.name as existence_concept,
                    ec.cultural_context as existence_culture,
                    nc.name as nothingness_concept,
                    nc.cultural_context as nothingness_culture,
                    cr.relation_type,
                    cr.strength
                FROM concept_relations cr
                JOIN existence_concepts ec ON cr.source_table = 'existence_concepts' AND cr.source_id = ec.id
                JOIN nothingness_concepts nc ON cr.target_table = 'nothingness_concepts' AND cr.target_id = nc.id
                UNION
                SELECT 
                    nc.name as existence_concept,
                    nc.cultural_context as existence_culture,
                    ec.name as nothingness_concept,
                    ec.cultural_context as nothingness_culture,
                    cr.relation_type,
                    cr.strength
                FROM concept_relations cr
                JOIN nothingness_concepts nc ON cr.source_table = 'nothingness_concepts' AND cr.source_id = nc.id
                JOIN existence_concepts ec ON cr.target_table = 'existence_concepts' AND cr.target_id = ec.id
                ORDER BY strength DESC
            """)
            return [dict(row) for row in cursor.fetchall()]

    def find_god_independent_concepts(self) -> Dict[str, List[Dict]]:
        """神に依存しない根本概念を特定"""
        with self.get_connection() as conn:
            cursor = conn.cursor()
            
            # 各概念テーブルから神の創造に依存しない概念を抽出
            tables = ['existence_concepts', 'nothingness_concepts', 'dao_concepts', 'consciousness_concepts']
            results = {}
            
            for table in tables:
                cursor.execute(f"""
                    SELECT name, cultural_context, definition
                    FROM {table}
                    WHERE id NOT IN (
                        SELECT target_id 
                        FROM concept_relations 
                        WHERE target_table = ? 
                        AND source_table = 'divine_concepts' 
                        AND relation_type IN ('creates', 'generates', 'causes')
                    )
                """, (table,))
                results[table] = [dict(row) for row in cursor.fetchall()]
            
            return results

    def analyze_paradoxes(self) -> List[Dict]:
        """パラドックス・矛盾を分析"""
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT 
                    ec.name as existence_name,
                    ec.cultural_context as existence_culture,
                    nc.name as nothingness_name,
                    nc.cultural_context as nothingness_culture,
                    nc.paradox_level,
                    cr.relation_type,
                    cr.strength,
                    cr.logical_necessity
                FROM concept_relations cr
                JOIN existence_concepts ec ON (
                    (cr.source_table = 'existence_concepts' AND cr.source_id = ec.id) OR
                    (cr.target_table = 'existence_concepts' AND cr.target_id = ec.id)
                )
                JOIN nothingness_concepts nc ON (
                    (cr.source_table = 'nothingness_concepts' AND cr.source_id = nc.id) OR
                    (cr.target_table = 'nothingness_concepts' AND cr.target_id = nc.id)
                )
                WHERE nc.paradox_level >= 7
                ORDER BY nc.paradox_level DESC, cr.strength DESC
            """)
            return [dict(row) for row in cursor.fetchall()]

    def concept_network_analysis(self) -> Dict[str, Any]:
        """概念ネットワーク分析"""
        with self.get_connection() as conn:
            cursor = conn.cursor()
            
            # 最も関係性の多い概念
            cursor.execute("""
                SELECT 
                    source_table,
                    COUNT(*) as connection_count
                FROM concept_relations 
                GROUP BY source_table
                ORDER BY connection_count DESC
            """)
            hub_tables = [dict(row) for row in cursor.fetchall()]
            
            # 最も強い関係性
            cursor.execute("""
                SELECT 
                    source_table, target_table, relation_type, strength,
                    cultural_specificity, logical_necessity
                FROM concept_relations 
                ORDER BY strength DESC 
                LIMIT 10
            """)
            strongest_relations = [dict(row) for row in cursor.fetchall()]
            
            # 文化的特異性の分析
            cursor.execute("""
                SELECT 
                    cultural_specificity,
                    COUNT(*) as count,
                    AVG(strength) as avg_strength
                FROM concept_relations 
                WHERE cultural_specificity IS NOT NULL
                GROUP BY cultural_specificity
                ORDER BY count DESC
            """)
            cultural_analysis = [dict(row) for row in cursor.fetchall()]
            
            return {
                'hub_tables': hub_tables,
                'strongest_relations': strongest_relations,
                'cultural_analysis': cultural_analysis
            }

    def add_custom_concept(self, table_name: str, **kwargs):
        """カスタム概念を追加"""
        with self.get_connection() as conn:
            cursor = conn.cursor()
            
            # テーブル構造を取得
            cursor.execute(f"PRAGMA table_info({table_name})")
            table_info = cursor.fetchall()
            # id列とDEFAULT値のある列を除外
            columns = []
            for col in table_info:
                col_name = col[1]
                col_default = col[4]  # DEFAULT値
                if col_name != 'id' and col_default is None:
                    columns.append(col_name)
            
            # 提供されたキーワード引数から対応する値を取得
            values = []
            actual_columns = []
            for col in columns:
                if col in kwargs:
                    actual_columns.append(col)
                    values.append(kwargs[col])
            
            if not actual_columns:
                raise ValueError("有効なカラムデータが提供されていません")
            
            # データを挿入
            placeholders = ','.join(['?' for _ in actual_columns])
            cursor.execute(f"""
                INSERT INTO {table_name} ({','.join(actual_columns)})
                VALUES ({placeholders})
            """, values)
            
            conn.commit()
            return cursor.lastrowid

    def export_to_json(self, filename: str = "metaphysics_export.json"):
        """データベースをJSONでエクスポート"""
        data = {}
        
        with self.get_connection() as conn:
            cursor = conn.cursor()
            
            # 全テーブルのデータを取得
            tables = [
                'existence_concepts', 'nothingness_concepts', 'time_concepts',
                'space_concepts', 'consciousness_concepts', 'substance_concepts',
                'universal_concepts', 'divine_concepts', 'good_concepts',
                'dao_concepts', 'concept_relations', 'contradictions',
                'cultural_interpretations'
            ]
            
            for table in tables:
                cursor.execute(f"SELECT * FROM {table}")
                columns = [description[0] for description in cursor.description]
                rows = cursor.fetchall()
                data[table] = [dict(zip(columns, row)) for row in rows]
        
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2, default=str)
        
        print(f"✅ データを {filename} にエクスポートしました")

def main():
    """メイン実行関数"""
    print("🏛️ 形而上学データベース初期化中...")
    
    # データベース初期化
    db = MetaphysicsDB()
    db.insert_sample_data()
    
    print("\n" + "="*50)
    print("📊 データベース分析結果")
    print("="*50)
    
    # 文化横断的概念分析
    print("\n🌍 文化横断的概念関係:")
    cross_cultural = db.query_cross_cultural_concepts()
    for relation in cross_cultural[:5]:  # 上位5件
        print(f"  {relation['existence_concept']} ({relation['existence_culture']}) "
              f"--[{relation['relation_type']}:{relation['strength']:.1f}]--> "
              f"{relation['nothingness_concept']} ({relation['nothingness_culture']})")
    
    # 神に依存しない概念
    print("\n⚖️ 神に依存しない根本概念:")
    god_independent = db.find_god_independent_concepts()
    for table, concepts in god_independent.items():
        if concepts:
            print(f"  {table}:")
            for concept in concepts[:3]:  # 上位3件
                print(f"    • {concept['name']} ({concept['cultural_context']})")
    
    # パラドックス分析
    print("\n🔄 高パラドックス概念:")
    paradoxes = db.analyze_paradoxes()
    for p in paradoxes[:3]:  # 上位3件
        print(f"  {p['existence_name']} ←→ {p['nothingness_name']} "
              f"(パラドックス度: {p['paradox_level']}, 強度: {p['strength']:.1f})")
    
    # ネットワーク分析
    print("\n🕸️ 概念ネットワーク分析:")
    network = db.concept_network_analysis()
    print("  最も接続の多いテーブル:")
    for hub in network['hub_tables'][:3]:
        print(f"    • {hub['source_table']}: {hub['connection_count']} connections")
    
    # JSONエクスポート
    db.export_to_json()
    
    print("\n✨ 分析完了！SQLiteデータベースとJSONエクスポートが準備できました。")
    print(f"📁 データベースファイル: {db.db_path}")
    
    # インタラクティブなサンプル
    print("\n" + "="*50)
    print("🔍 カスタム概念追加のサンプル")
    print("="*50)
    
    # カスタム概念を追加
    concept_id = db.add_custom_concept(
        'dao_concepts',
        name='直観',
        cultural_context='western_bergson', 
        definition='ベルクソンの直観哲学の根本概念',
        expressability=True,
        action_principle='intuitive_method',
        universality_scope='human',
        knowability='experiential_only'
    )
    print(f"✅ 新しい道概念 '直観' を追加しました (ID: {concept_id})")

if __name__ == "__main__":
    main()
