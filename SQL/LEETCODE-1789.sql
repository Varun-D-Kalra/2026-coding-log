-- Case 1: Employees in only 1 department
SELECT employee_id, department_id
FROM Employee
WHERE employee_id IN (
  SELECT employee_id
  FROM Employee
  GROUP BY employee_id
  HAVING COUNT(*) = 1
)

UNION ALL

-- Case 2: Employees in multiple departments, marked primary
SELECT employee_id, department_id
FROM Employee
WHERE primary_flag = 'Y'
  AND employee_id IN (
    SELECT employee_id
    FROM Employee
    GROUP BY employee_id
    HAVING COUNT(*) > 1
  )
