WITH daily_totals AS (
    SELECT
        visited_on,
        SUM(amount) as daily_amount
    FROM Customer
    GROUP BY visited_on
),
window_data AS (
    SELECT
        visited_on,
        daily_amount,
        SUM(daily_amount) OVER (
            ORDER BY visited_on
            ROWS BETWEEN 6 PRECEDING AND CURRENT ROW
        ) as amount,
        ROUND(
            AVG(daily_amount) OVER (
                ORDER BY visited_on
                ROWS BETWEEN 6 PRECEDING AND CURRENT ROW
            ), 2
        ) as average_amount,
        COUNT(*) OVER (
            ORDER BY visited_on
            ROWS BETWEEN 6 PRECEDING AND CURRENT ROW
        ) as days_count
    FROM daily_totals
)
SELECT
    visited_on,
    amount,
    average_amount
FROM window_data
WHERE days_count = 7
ORDER BY visited_on;