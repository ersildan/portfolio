SELECT 
    emp.name AS Employee
FROM Employee emp
INNER JOIN Employee manager ON emp.managerId = manager.id
AND emp.salary > manager.salary;
