-- ===== 形而上学データベース分析SQL =====
-- 従来の哲学では不可能だった定量的・体系的分析を実現

-- 【パターン1】神の「万能カード」問題の解決
-- 従来：「存在の根拠は神である」で議論終了
-- SQL革命：神に依存しない根本概念を定量的に特定・分析可能

-- 1-1. 神に依存しない根本概念を全て特定
WITH god_created_concepts AS (
    SELECT DISTINCT target_table, target_id
    FROM concept_relations cr
    JOIN divine_concepts dc ON cr.source_table = 'divine_concepts' 
        AND cr.source_id = dc.id
    WHERE cr.relation_type IN ('creates', 'generates', 'causes')
),
independent_concepts AS (
    SELECT 'existence_concepts' as table_name, id, name, cultural_context, abstraction_level
    FROM existence_concepts 
    WHERE id NOT IN (
        SELECT target_id FROM god_created_concepts 
        WHERE target_table = 'existence_concepts'
    )
    
    UNION ALL
    
    SELECT 'nothingness_concepts' as table_name, id, name, cultural_context, paradox_level as abstraction_level
    FROM nothingness_concepts 
    WHERE id NOT IN (
        SELECT target_id FROM god_created_concepts 
        WHERE target_table = 'nothingness_concepts'
    )
    
    UNION ALL
    
    SELECT 'dao_concepts' as table_name, id, name, cultural_context, 
           CASE knowability 
               WHEN 'experiential_only' THEN 10
               WHEN 'partially_knowable' THEN 7
               WHEN 'knowable' THEN 5
               ELSE 0
           END as abstraction_level
    FROM dao_concepts 
    WHERE id NOT IN (
        SELECT target_id FROM god_created_concepts 
        WHERE target_table = 'dao_concepts'
    )
)
SELECT 
    table_name as 概念分類,
    name as 概念名,
    cultural_context as 文化的背景,
    abstraction_level as 抽象度,
    COUNT(*) OVER (PARTITION BY cultural_context) as 同文化圏内の自立概念数
FROM independent_concepts
ORDER BY abstraction_level DESC, cultural_context;

-- 1-2. 神への依存度分析：どの概念が最も「神の説明」に頼っているか
SELECT 
    target_table as 概念領域,
    COUNT(*) as 神依存概念数,
    AVG(cr.strength) as 平均依存強度,
    GROUP_CONCAT(DISTINCT cr.cultural_specificity) as 依存文化圏
FROM concept_relations cr
JOIN divine_concepts dc ON cr.source_table = 'divine_concepts' AND cr.source_id = dc.id
WHERE cr.relation_type IN ('creates', 'generates', 'causes', 'sustains')
GROUP BY target_table
ORDER BY 神依存概念数 DESC, 平均依存強度 DESC;

-- ===================================================================

-- 【パターン2】文化間概念の定量的比較分析
-- 従来：「東洋と西洋は違う」という曖昧な議論
-- SQL革命：具体的な違いを数値化し、共通点・相違点を客観的に分析

-- 2-1. 存在vs無の文化的解釈の定量比較
WITH cultural_existence_analysis AS (
    SELECT 
        'western' as culture_group,
        'existence' as concept_type,
        AVG(abstraction_level) as avg_abstraction,
        COUNT(*) as concept_count,
        AVG(CAST(temporal_aspect AS FLOAT)) as temporality_ratio,
        AVG(CAST(spatial_aspect AS FLOAT)) as spatiality_ratio
    FROM existence_concepts 
    WHERE cultural_context LIKE 'western%'
    
    UNION ALL
    
    SELECT 
        'eastern' as culture_group,
        'existence' as concept_type,
        AVG(abstraction_level) as avg_abstraction,
        COUNT(*) as concept_count,
        AVG(CAST(temporal_aspect AS FLOAT)) as temporality_ratio,
        AVG(CAST(spatial_aspect AS FLOAT)) as spatiality_ratio
    FROM existence_concepts 
    WHERE cultural_context IN ('buddhist', 'daoist', 'hindu')
    
    UNION ALL
    
    SELECT 
        'western' as culture_group,
        'nothingness' as concept_type,
        AVG(paradox_level) as avg_abstraction,
        COUNT(*) as concept_count,
        0.5 as temporality_ratio,  -- 無の時間性は中程度と仮定
        0.0 as spatiality_ratio    -- 無は空間を持たない
    FROM nothingness_concepts 
    WHERE cultural_context LIKE 'western%'
    
    UNION ALL
    
    SELECT 
        'eastern' as culture_group,
        'nothingness' as concept_type,
        AVG(paradox_level) as avg_abstraction,
        COUNT(*) as concept_count,
        0.8 as temporality_ratio,  -- 東洋の無は時間的側面が強い
        0.3 as spatiality_ratio    -- 仏教の空は空間との関わりあり
    FROM nothingness_concepts 
    WHERE cultural_context IN ('buddhist', 'daoist')
)
SELECT 
    culture_group as 文化圏,
    concept_type as 概念タイプ,
    ROUND(avg_abstraction, 2) as 平均抽象度,
    concept_count as 概念数,
    ROUND(temporality_ratio, 2) as 時間性比率,
    ROUND(spatiality_ratio, 2) as 空間性比率,
    ROUND(avg_abstraction * concept_count, 2) as 概念総合力
FROM cultural_existence_analysis
ORDER BY culture_group, avg_abstraction DESC;

-- 2-2. 文化間の概念関係性パターン分析
SELECT 
    cr.cultural_specificity as 文化特有性,
    cr.relation_type as 関係タイプ,
    COUNT(*) as 関係数,
    ROUND(AVG(cr.strength), 3) as 平均関係強度,
    ROUND(MIN(cr.strength), 3) as 最小強度,
    ROUND(MAX(cr.strength), 3) as 最大強度,
    cr.logical_necessity as 論理的必然性,
    GROUP_CONCAT(DISTINCT cr.temporal_stability) as 時間的安定性パターン
FROM concept_relations cr
WHERE cr.cultural_specificity IS NOT NULL
GROUP BY cr.cultural_specificity, cr.relation_type, cr.logical_necessity
HAVING COUNT(*) > 0
ORDER BY 平均関係強度 DESC, 関係数 DESC;

-- ===================================================================

-- 【パターン3】概念ネットワークの隠れた構造分析
-- 従来：概念間の関係を個別に議論、全体像が見えない
-- SQL革命：概念のネットワーク構造を定量分析、隠れたパターンを発見

-- 3-1. 最も重要な「ハブ概念」の特定（PageRank的分析）
WITH concept_connections AS (
    -- 各概念の接続数を計算（送信・受信両方向）
    SELECT 
        source_table as table_name,
        source_id as concept_id,
        COUNT(*) as outbound_connections,
        AVG(strength) as avg_outbound_strength
    FROM concept_relations
    GROUP BY source_table, source_id
    
    UNION ALL
    
    SELECT 
        target_table as table_name,
        target_id as concept_id,
        COUNT(*) as inbound_connections,
        AVG(strength) as avg_inbound_strength
    FROM concept_relations
    GROUP BY target_table, target_id
),
hub_analysis AS (
    SELECT 
        table_name,
        concept_id,
        SUM(outbound_connections) as total_connections,
        AVG(avg_outbound_strength) as connection_strength,
        -- ハブ重要度 = 接続数 × 平均強度
        SUM(outbound_connections) * AVG(avg_outbound_strength) as hub_importance
    FROM concept_connections
    GROUP BY table_name, concept_id
)
SELECT 
    ha.table_name as 概念分野,
    CASE ha.table_name
        WHEN 'existence_concepts' THEN ec.name
        WHEN 'nothingness_concepts' THEN nc.name
        WHEN 'dao_concepts' THEN dc.name
        WHEN 'divine_concepts' THEN dv.name
        WHEN 'consciousness_concepts' THEN cc.name
        ELSE 'Unknown'
    END as 概念名,
    ha.total_connections as 総接続数,
    ROUND(ha.connection_strength, 3) as 平均接続強度,
    ROUND(ha.hub_importance, 3) as ハブ重要度,
    CASE ha.table_name
        WHEN 'existence_concepts' THEN ec.cultural_context
        WHEN 'nothingness_concepts' THEN nc.cultural_context
        WHEN 'dao_concepts' THEN dc.cultural_context
        WHEN 'divine_concepts' THEN dv.cultural_context
        WHEN 'consciousness_concepts' THEN cc.cultural_context
        ELSE 'Unknown'
    END as 文化的背景
FROM hub_analysis ha
LEFT JOIN existence_concepts ec ON ha.table_name = 'existence_concepts' AND ha.concept_id = ec.id
LEFT JOIN nothingness_concepts nc ON ha.table_name = 'nothingness_concepts' AND ha.concept_id = nc.id
LEFT JOIN dao_concepts dc ON ha.table_name = 'dao_concepts' AND ha.concept_id = dc.id
LEFT JOIN divine_concepts dv ON ha.table_name = 'divine_concepts' AND ha.concept_id = dv.id
LEFT JOIN consciousness_concepts cc ON ha.table_name = 'consciousness_concepts' AND ha.concept_id = cc.id
WHERE ha.total_connections > 0
ORDER BY ha.hub_importance DESC;

-- 3-2. パラドックス・矛盾の構造分析（従来の哲学では避けられた問題を正面から分析）
WITH paradox_network AS (
    SELECT 
        nc.name as 無概念名,
        nc.cultural_context as 無文化,
        nc.paradox_level as パラドックス度,
        cr.relation_type as 関係タイプ,
        cr.strength as 関係強度,
        cr.logical_necessity as 論理的必然性,
        CASE cr.target_table
            WHEN 'existence_concepts' THEN ec.name
            WHEN 'divine_concepts' THEN dc.name
            ELSE '他概念'
        END as 相互作用概念,
        CASE cr.target_table
            WHEN 'existence_concepts' THEN ec.cultural_context
            WHEN 'divine_concepts' THEN dc.name
            ELSE '不明'
        END as 相互作用文化
    FROM nothingness_concepts nc
    JOIN concept_relations cr ON nc.id = cr.source_id AND cr.source_table = 'nothingness_concepts'
    LEFT JOIN existence_concepts ec ON cr.target_table = 'existence_concepts' AND cr.target_id = ec.id
    LEFT JOIN divine_concepts dc ON cr.target_table = 'divine_concepts' AND cr.target_id = dc.id
    WHERE nc.paradox_level >= 7  -- 高パラドックス概念のみ
)
SELECT 
    無概念名,
    無文化,
    パラドックス度,
    関係タイプ,
    ROUND(関係強度, 3) as 関係強度,
    論理的必然性,
    相互作用概念,
    相互作用文化,
    -- パラドックス強度 = パラドックス度 × 関係強度
    ROUND(パラドックス度 * 関係強度, 3) as パラドックス影響度,
    CASE 
        WHEN 無文化 = 相互作用文化 THEN '文化内パラドックス'
        WHEN 無文化 != 相互作用文化 THEN '文化間パラドックス'
        ELSE '分類不能'
    END as パラドックス分類
FROM paradox_network
ORDER BY パラドックス影響度 DESC;

-- ===================================================================

-- 【ボーナス】従来の哲学史では見えなかった発見的クエリ
-- 「最も論理的に安定した概念関係」の特定

SELECT 
    cr.source_table || '.' || 
    COALESCE(
        (SELECT name FROM existence_concepts WHERE id = cr.source_id AND cr.source_table = 'existence_concepts'),
        (SELECT name FROM nothingness_concepts WHERE id = cr.source_id AND cr.source_table = 'nothingness_concepts'),
        (SELECT name FROM dao_concepts WHERE id = cr.source_id AND cr.source_table = 'dao_concepts')
    ) as 起点概念,
    
    cr.relation_type as 関係,
    
    cr.target_table || '.' ||
    COALESCE(
        (SELECT name FROM existence_concepts WHERE id = cr.target_id AND cr.target_table = 'existence_concepts'),
        (SELECT name FROM nothingness_concepts WHERE id = cr.target_id AND cr.target_table = 'nothingness_concepts'),
        (SELECT name FROM dao_concepts WHERE id = cr.target_id AND cr.target_table = 'dao_concepts')
    ) as 終点概念,
    
    ROUND(cr.strength, 3) as 関係強度,
    cr.logical_necessity as 論理的必然性,
    cr.temporal_stability as 時間的安定性,
    cr.cultural_specificity as 文化特有性,
    
    -- 安定性スコア = 強度 × 必然性重み × 安定性重み
    ROUND(cr.strength * 
        CASE cr.logical_necessity
            WHEN 'necessary' THEN 1.0
            WHEN 'contingent' THEN 0.7
            WHEN 'impossible' THEN 0.0
            ELSE 0.5
        END *
        CASE cr.temporal_stability
            WHEN 'eternal' THEN 1.0
            WHEN 'historical' THEN 0.8
            WHEN 'contextual' THEN 0.6
            WHEN 'fluid' THEN 0.4
            ELSE 0.5
        END, 4) as 総合安定性スコア

FROM concept_relations cr
WHERE cr.strength >= 0.5  -- ある程度の関係強度がある関係のみ
ORDER BY 総合安定性スコア DESC, 関係強度 DESC
LIMIT 15;