-- 1004:Todoリスト
SELECT id, description, completion_flag
FROM Todo
WHERE completion_flag = False;