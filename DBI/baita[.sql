/*select    --thông tin (cột cần hiển thị)
from        -- nguồn dữ liệu
where       -- điều kiện
group by    --hàm thống kê: count, min, max, sum , avg
having
order by*/
*1
select *
from tblDepartment
where depNum = 5
*3
select proNum, proName, depname
from tblProject E inner join tblDepartment D
on E.depNum = D.depNum
where E.depNum = 5
*4
select empName, empSSN
from tblEmployee
where supervisorSSN = (select empSSN from tblEmployee where empName = 'Mai Duy An')
*5
select empName, empSSN
from tblEmployee
where empSSN = (select supervisorSSN from tblEmployee where empName = 'Mai Duy An')
*exampl 
select depnum, count(empssn) as SL
from tblEmployee
group by depNum

select depnum, avg(empsalary) as AVG
from tblEmployee
group by depnum
having avg(empsalary) > 80000

*6 
select proname,locName
from tblLocation A inner join tblProject B
on A.locNum = B.locNum
where proname = 'ProjectA'
*14
select depsex, count(depsex) as SL
from tblDependent
group by depsex
*17

select top 1 with ties depNum, depname, count() as SL
from tblEmployee A inner join tblDepartment B inner join tblDependent C
group by mgrssn, depname
order by SL DESC