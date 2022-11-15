task1
SELECT nb.title, count(1) as count FROM notebooks_brand as nb
JOIN notebooks_notebook as nn ON nb.id = nn.brand_id 
GROUP BY nb.id ORDER BY count DESC
;

task2
SELECT diagonal as size, count(1) as count 
FROM (
    SELECT 
    	(round(diagonal * 2) / 2) AS diagonal 
    FROM notebooks_notebook
) as nn
GROUP BY nn.diagonal
ORDER BY size DESC;
