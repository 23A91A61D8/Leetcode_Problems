-- Last updated: 09/09/2025, 14:17:38
SELECT 
    u.name,
    SUM(amount) AS balance
FROM 
    Users u
JOIN 
    Transactions t ON u.account = t.account
GROUP BY 
    u.name
    HAVING
    balance > 10000

 