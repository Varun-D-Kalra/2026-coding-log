SELECT x, y, z,
       CASE 
         WHEN x + y > z AND y + z > x AND z + x > y 
         THEN 'Yes' 
         ELSE 'No' 
       END AS triangle
FROM Triangle;
-- yes i copied this one. my brain just skipped the case when concept, rewired the neuronss
