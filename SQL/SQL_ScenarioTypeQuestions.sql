-- QUESTIONS 1

CREATE TABLE Orders (
    OrderID INT,
    CustomerID INT,
    OrderDate DATE,
    Amount INT
);

INSERT INTO Orders VALUES
(1,101,'2024-01-10',500),
(2,101,'2024-01-15',700),
(3,102,'2024-02-01',300),
(4,101,'2024-03-10',400),
(5,103,'2024-01-20',900);

/*  ==== EXPECTED OUTPUT =======

OrderID | CustomerID | OrderDate  | Amount | PurchaseType
----------------------------------------------------------
1       | 101        | 2024-01-10 | 500    | FirstPurchase
2       | 101        | 2024-01-15 | 700    | RepeatPurchase
4       | 101        | 2024-03-10 | 400    | RepeatPurchase
3       | 102        | 2024-02-01 | 300    | FirstPurchase
5       | 103        | 2024-01-20 | 900    | FirstPurchase

*/

with CTE as (
select orderID, customerID, OrderDate, Amount, Dense_rank() over (order by customerID) as customer_rank from Orders
)
select *, case 
when customer_rank =  lag(customer_rank) over (order by customerID) then 'RepeatPurchase'
else 'FirstPurchase'
end 
from CTE

-- ==========================================================================================
--  QUESTION 2
CREATE TABLE DailySales (
    SaleDate DATE,
    Amount INT
);

INSERT INTO DailySales VALUES
('2024-01-01',100),
('2024-01-02',150),
('2024-01-10',200),
('2024-02-01',300),
('2024-02-05',100);

/* ==== EXPECTED OUTPUT ======= PART 1
SaleDate	Amount	    LastAmountTotal
-----------------------------------------
2024-01-01	  100	        100
2024-01-02	  150	        250
2024-01-10	  200	        350
2024-02-01	  300	        500
2024-02-05	  100	        400
*/

/* ==== EXPECTED OUTPUT ======= PART 2
SaleDate   | Amount | MonthlyRunningTotal
-----------------------------------------
2024-01-01 | 100    | 100
2024-01-02 | 150    | 250
2024-01-10 | 200    | 450
2024-02-01 | 300    | 300
2024-02-05 | 100    | 400
*/

select * from DailySales

-- part 1
with CTE as (
select *, Lag(amount,1,0) over (order by SaleDate) as temp_sales from DailySales
)
select SaleDate,Amount, (amount+temp_sales) as LastAmountTotal from CTE;

-- part2 

select *, sum(amount) over (partition by month(saleDate) order by SaleDate) as temp_sales from DailySales

-- ==========================================================================================
-- QUESTION 3
-- Find the longest consecutive login streak

CREATE TABLE UserLogins (
    UserID INT,
    LoginDate DATE
);

INSERT INTO UserLogins VALUES
(1,'2024-01-01'),
(1,'2024-01-02'),
(1,'2024-01-04'),
(2,'2024-02-10'),
(2,'2024-02-11'),
(2,'2024-02-12');

select * from UserLogins


/* ==== EXPECTED OUTPUT ======= 
UserID | MaxConsecutiveDays
---------------------------
1      | 2
2      | 3
*/

with CTE as (
select userID, LoginDate, dateadd(day, -row_number() over(partition by userID order by LoginDate),Logindate) as grp
from UserLogins
)
select userID, max(cnt) as MaxConsecutiveDays from (
select UserID, grp, count(*) as cnt from CTE group by userID, grp
) X group by UserID

-- ==========================================================================================
-- QUESTION 4
--latest price per product
CREATE TABLE ProductPrice (
    ProductID INT,
    Price INT,
    PriceDate DATE
);

INSERT INTO ProductPrice VALUES
(1,100,'2024-01-01'),
(1,120,'2024-02-01'),
(2,200,'2024-01-10'),
(2,180,'2024-03-01');

/* ==== EXPECTED OUTPUT ======= 
ProductID | Price | PriceDate
-----------------------------
1         | 120   | 2024-02-01
2         | 180   | 2024-03-01
*/


select b.* from Productprice b Left join ProductPrice a on b.PriceDate<a.Pricedate and b.ProductId = a.productID
where a.ProductId is null

-- ==========================================================================================
-- QUESTION 5
--Count how many employees share the same last name
CREATE TABLE Employees (
    EmpID INT,
    FullName VARCHAR(100)
);

INSERT INTO Employees VALUES
(1,'Amit Sharma'),
(2,'Amit Verma'),
(3,'Neha Sharma'),
(4,'Rohit Singh');

select * from Employees
/* ==== EXPECTED OUTPUT ======= 
EmpID | FullName      | LastName | LastNameCount
------------------------------------------------
1     | Amit Sharma   | Sharma   | 2
3     | Neha Sharma   | Sharma   | 2
2     | Amit Verma    | Verma    | 1
4     | Rohit Singh   | Singh    | 1
*/

select * from Employees;

