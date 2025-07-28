
/*
========================================================================================================================================
                                                           Sub Queries
=========================================================================================================================================
*/

-- Retrieve the first name, last name, and the total number of people in the table for each record.
select first_name, last_name, (select count(*) from [dbo].[people-100])as total_people from [dbo].[people-100] group by  first_name, last_name


--Find all individuals whose date of birth is later than the average birth date in the table.
SELECT First_Name, Last_Name, Date_of_birth
FROM [dbo].[people-100]
WHERE year(Date_of_birth)> (SELECT AVG(year(Date_of_birth)) FROM [dbo].[people-100]);


-- Retrieve the first name, last name, and job title of individuals who have the same job title as someone with the email domain 'example.com'.
select first_name, last_name, job_title, email from [dbo].[people-100] p1 where exists (
select 1 from [dbo].[people-100] p2
where p2.job_title = p1.job_title and p1.email like '%example.com'
)

-- Find individuals whose phone number starts with '001-' and whose job title is among those held by females.

-- Calculate the number of people per job title and list only those job titles with more than 2 people.

-- For each person, display their first name, last name, and the number of people with the same sex

-- Display the first name, last name, and the earliest birth date for each job title.

-- Find all individuals whose job title is not among the job titles of people born before 1950.

--Retrieve individuals who share the same last name as at least one other person in the table.

--Retrieve the first name, last name, and date of birth of the second oldest person using a single subquery (avoiding nested subqueries).