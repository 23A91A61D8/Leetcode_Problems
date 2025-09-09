-- Last updated: 09/09/2025, 14:17:45
SELECT *
FROM Users
WHERE 
    mail REGEXP '^[a-zA-Z][a-zA-Z0-9._-]*@leetcode\\.com$'
    AND BINARY RIGHT(mail, 13) = '@leetcode.com';
