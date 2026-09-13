WITH Qualified AS (
    SELECT 
        id,
        visit_date,
        people,
        id - ROW_NUMBER() OVER (ORDER BY id) AS island_id
    FROM Stadium
    WHERE people >= 100
),
GroupCounts AS (
    SELECT 
        id,
        visit_date,
        people,
        COUNT(*) OVER (PARTITION BY island_id) AS cnt
    FROM Qualified
)
SELECT 
    id,
    visit_date,
    people
FROM GroupCounts
WHERE cnt >= 3
ORDER BY visit_date;