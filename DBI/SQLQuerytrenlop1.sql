	--cau 1--
SELECT empSSN, empName, depNum
FROM [dbo].[tblEmployee]
WHERE depNum = (SELECT depNum FROM [dbo].[tblDepartment] WHERE depName = N'Phòng Nghiên cứu và phát triển')
-- cau 1--
SELECT tblEmployee.empSSN, tblEmployee.empName, tblDepartment.depNum
FROM [dbo].[tblDepartment], [dbo].[tblEmployee]
WHERE tblEmployee.depNum = tblDepartment.depNum 
AND tblDepartment.depName like N'Phòng Nghiên cứu và phát triển'


-- cau1--  phong ban la nghien cuu va phat trien
select empName,empSSN, depNum
from  tblEmployee
where depNum = (
select depNum 
from tblDepartment 
where depName = N'Phòng Nghiên Cứu Và Phát Triển'
)

-- cau 1---
select empName, empSSN, tblEmployee.depNum
from tblEmployee,tblDepartment
where tblEmployee.depNum = tblDepartment.depNum and tblDepartment.depName like N'Phòng Nghiên Cứu Và Phát Triển'

-- cau 2--
-- khi nào có 2 khóa giống nhau thì nên làm như thế này -- 
select tblProject.proNum, tblProject.proName , tblDepartment.depName
from tblDepartment,tblProject
where tblProject.depNum = tblDepartment.depNum and tblDepartment.depName like N'Phòng Nghiên cứu và phát triển'


-- 3.	Cho biết dự án có tên ProjectB hiện đang được quản lý bởi phòng ban nào. Thông tin yêu cầu: mã số dụ án, tên dự án, tên phòng ban quản lý
select tblProject.proNum , tblProject.proName, tblDepartment.depName
from  tblProject,tblDepartment
where tblProject.proNum = tblDepartment.depNum and tblProject.proName like 'ProjectB'

select proName,proNum, tblDepartment.depName
from tblProject,tblDepartment
where tblDepartment.depNum = tblProject.depNum and tblProject.proName like 'ProjectB'

 --4	Cho biết những nhân viên nào đang bị giám sát bởi nhân viên có tên Mai Duy An. Thông tin yêu cầu: mã số nhân viên, họ tên nhân viên
 -- nó sẽ liên thông qua ba thực thể , tực thể trung gian --- 
SELECT tblEmployee.empSSN, tblEmployee.empName
FROM tblEmployee  
JOIN tblEmployee supervisor ON tblEmployee.supervisorSSN = supervisor.empSSN
WHERE supervisor.empName LIKE N'Mai Duy An'


-- cau 4 lam lai--
select  tblEmployee.empSSN, tblEmployee.empName
from tblEmployee  
join tblEmployee supersivor on tblEmployee.supervisorSSN = supersivor.empSSN
where supersivor.empName like N'Mai Duy An'

select tblEmployee.empSSN, tblEmployee.empName
from  tblEmployee
join tblEmployee supervisor on tblEmployee.supervisorSSN = supervisor.empSSN
where supervisor.empName like N'Mai Duy An'



select * 
from tblEmployee

--5-Cho biết ai hiện đang giám sát những nhân viên có tên Mai Duy An. Thông tin yêu cầu: mã số nhân viên, họ tên nhân viên giám sát.
SELECT supervisor.empSSN, supervisor.empName
FROM tblEmployee e
JOIN tblEmployee supervisor ON e.supervisorSSN = supervisor.empSSN
WHERE e.empName LIKE N'Mai Duy An'
 -- câu 5 ngược lại câu 4 --
select super.empName, super.empSSN
from tblEmployee 
join tblEmployee super on tblEmployee.supervisorSSN = super.empSSN
where  tblEmployee.empName like N'Mai Duy An'

-- câu 6---
select tblProject.proNum, tblLocation.locName, tblProject.proName
from tblProject, tblLocation
where tblProject.locNum = tblLocation.locNum and tblProject.proName like 'ProjectAA'

--7.Cho biết vị trí làm việc có tên Tp. HCM hiện đang là chỗ làm việc của những dự án nào. Thông tin yêu cầu: mã số, tên dự án-
select  tblProject.proName ,tblProject.proNum 
from  tblProject , tblLocation
where  tblProject.locNum = tblLocation.locNum or  tblLocation.locName = N'TP Hồ Chí Minh'


--8 cho biết những người phụ thuộc trên 18 tuổi , tên , ngày tháng , tên nhân viên phụ thuộc ---
select  empName, empBirthdate, depName
from tblEmployee, tblDependent
where tblEmployee.empSSN = tblDependent.empSSN and YEAR( GETDATE()) - YEAR(empBirthdate) >= 18

--9 cho biết những người phụ thuộc là nam giới --
select  empName, empSex , depName 
from tblEmployee, tblDependent
where tblEmployee.empSSN = tblDependent.empSSN and  empSex = 'M'


--10 cho biết những nơi làm việc của phòng ban có tên phòng nghiên cứu và phát triển, mã phòng ban tên phòng ban , nơi làm việc 
-- đơn giản nếu nó liên thông qua 3 thực thể thì ta cứ nối các PK ở where như bình thường ' 
select  dep.depName, dep.depNum, loc.locName
from tblDepLocation deplo , tblDepartment dep , tblLocation loc
where deplo.depNum = dep.depNum and loc.locNum = deplo.locNum
and dep.depName = N'Phòng Nghiên Cứu Và Phát Triển'


select dep.depName,dep.depNum, loc.locName
from tblDepartment dep inner join tblDepLocation del on dep.depNum = del.depNum inner join tblLocation loc on loc.locNum = del.locNum and dep.depName = N'Phòng Nghiên Cứu Và Phát Triển'

-- 11 Cho biết những dự án đang làm việc ở TPHCM

SELECT
  p.proNum,
  p.proName,
  d.depName
FROM
  tblProject p
  INNER JOIN tblDepLocation dl ON p.depNum = dl.depNum
  INNER JOIN tblLocation l ON dl.locNum = l.locNum
  INNER JOIN tblDepartment d ON p.depNum = d.depNum
WHERE
  l.locName = N'TP Hồ Chí Minh'



  -- cau 12 
  SELECT
  e.empName,
  d.depName,
  d.depRelationship
FROM
  tblEmployee e
  INNER JOIN tblDepartment dep ON e.depNum = dep.depNum
  INNER JOIN tblDependent d ON e.empSSN = d.empSSN
WHERE
  dep.depName = N'Phòng Nghiên cứu và phát triển'
  AND d.depSex like 'F'


  -- cau 13
  SELECT
  e.empName,
  d.depName,
  d.depRelationship
FROM
  tblEmployee e
  INNER JOIN tblDepartment dep ON e.depNum = dep.depNum
  INNER JOIN tblDependent d ON e.empSSN = d.empSSN
WHERE
  dep.depName = 'Phòng Nghiên cứu và phát triển'
  AND YEAR( GETDATE()) - YEAR() >= 18


  --- cau 15 --
  SELECT
  depRelationship AS Relationship,
  COUNT(*) AS DependentCount
FROM
  tblDependent
GROUP BY
  depRelationship

  -- cau 16 ---------------
  SELECT
  d.depNum,
  d.depName,
  COUNT(d.depName) AS DependentCount
FROM
  tblDepartment d
  INNER JOIN tblEmployee e ON d.depNum = e.depNum
  INNER JOIN tblDependent dp ON e.empSSN = dp.empSSN
GROUP BY
  d.depNum,
  d.depName


  --- cau 17 ---
 SELECT TOP 1
  d.depNum,
  d.depName,
  COUNT(dp.depName) AS DependentCount
FROM
  tblDepartment d
  INNER JOIN tblEmployee e ON d.depNum = e.depNum
  INNER JOIN tblDependent dp ON e.empSSN = dp.empSSN
GROUP BY
  d.depNum,
  d.depName
HAVING
  COUNT(dp.depName) = (
    SELECT MIN(DependentCount)
    FROM (
      SELECT COUNT(depName) AS DependentCount
      FROM tblDependent
      GROUP BY empSSN
    ) AS DependentCounts
  )
  --- cau 18 --- 
 SELECT TOP 1
  d.depNum,
  d.depName,
  COUNT(dp.depName) AS DependentCount
FROM
  tblDepartment d
  INNER JOIN tblEmployee e ON d.depNum = e.depNum
  INNER JOIN tblDependent dp ON e.empSSN = dp.empSSN
GROUP BY
  d.depNum,
  d.depName
ORDER BY
  DependentCount DESC
  --- cau 19 ---- 
  SELECT
  e.empSSN AS EmployeeID,
  e.empName AS EmployeeName,
  d.depName AS DepartmentName,
  SUM(w.workHours) AS TotalWorkHours
FROM
  tblEmployee e
  INNER JOIN tblDepartment d ON e.depNum = d.depNum
  LEFT JOIN tblWorksOn w ON e.empSSN = w.empSSN
GROUP BY
  e.empSSN,
  e.empName,
  d.depName
  --- cau 20 --- 
  SELECT
  d.depNum AS DepartmentID,
  d.depName AS DepartmentName,
  SUM(w.workHours) AS TotalWorkHours
FROM
  tblDepartment d
  LEFT JOIN tblEmployee e ON d.depNum = e.depNum
  LEFT JOIN tblWorksOn w ON e.empSSN = w.empSSN
GROUP BY
  d.depNum,
  d.depName
  -- cau 21 --- 
  SELECT
  e.empSSN AS EmployeeID,
  e.empName AS EmployeeName,
  SUM(w.workHours) AS TotalWorkHours
FROM
  tblEmployee e
  LEFT JOIN tblWorksOn w ON e.empSSN = w.empSSN
GROUP BY
  e.empSSN,
  e.empName
HAVING
  SUM(w.workHours) = (
    SELECT MIN(TotalWorkHours)
    FROM (
      SELECT SUM(workHours) AS TotalWorkHours
      FROM tblWorksOn
      GROUP BY empSSN
    ) AS MinWorkHours
  )
  -- cau 22 --
  SELECT
  e.empSSN AS EmployeeID,
  e.empName AS EmployeeName,
  SUM(w.workHours) AS TotalWorkHours
FROM
  tblEmployee e
  LEFT JOIN tblWorksOn w ON e.empSSN = w.empSSN
GROUP BY
  e.empSSN,
  e.empName
HAVING
  SUM(w.workHours) = (
    SELECT MAX(TotalWorkHours)
    FROM (
      SELECT SUM(workHours) AS TotalWorkHours
      FROM tblWorksOn
      GROUP BY empSSN
    ) AS MaxWorkHours
  )

  --- cau 23 ---
 SELECT
  e.empSSN AS EmployeeID,
  e.empName AS EmployeeName,
  d.depName AS DepartmentName
FROM
  tblEmployee e
  INNER JOIN tblDepartment d ON e.depNum = d.depNum
WHERE
  e.empSSN IN (
    SELECT
      empSSN
    FROM
      tblWorksOn
    GROUP BY
      empSSN
    HAVING
      MIN(distinct proNum)
  )

  --cau 24---
  SELECT
  e.empSSN AS EmployeeID,
  e.empName AS EmployeeName,
  d.depName AS DepartmentName
FROM
  tblEmployee e
  INNER JOIN tblDepartment d ON e.depNum = d.depNum
WHERE
  e.empSSN IN (
    SELECT
      empSSN
    FROM
      tblWorksOn
    GROUP BY
      empSSN
    HAVING
      COUNT(DISTINCT proNum) > 1
  )

  -- cau 25---
  SELECT
  e.empSSN AS EmployeeID,
  e.empName AS EmployeeName,
  d.depName AS DepartmentName
FROM
  tblEmployee e
  INNER JOIN tblDepartment d ON e.depNum = d.depNum
WHERE
  e.empSSN IN (
    SELECT
      empSSN
    FROM
      tblWorksOn
    GROUP BY
      empSSN
    HAVING
      COUNT(DISTINCT proNum) >= 2
  )

-- cau26---
SELECT
  p.proNum AS ProjectID,
  p.proName AS ProjectName,
  COUNT(DISTINCT w.empSSN) AS MemberCount
FROM
  tblProject p
  LEFT JOIN tblWorksOn w ON p.proNum = w.proNum
GROUP BY
  p.proNum,
  p.proName
  ---cau27--
  SELECT
  p.proNum AS ProjectID,
  p.proName AS ProjectName,
  SUM(w.workHours) AS TotalWorkHours
FROM
  tblProject p
  LEFT JOIN tblWorksOn w ON p.proNum = w.proNum
GROUP BY
  p.proNum,
  p.proName
  -- cau28---
  SELECT
  p.proNum AS ProjectID,
  p.proName AS ProjectName,
  COUNT(DISTINCT w.empSSN) AS MemberCount
FROM
  tblProject p
  LEFT JOIN tblWorksOn w ON p.proNum = w.proNum
GROUP BY
  p.proNum,
  p.proName
HAVING
  COUNT(DISTINCT w.empSSN) = (
    SELECT
      MIN(MemberCount)
    FROM
      (
        SELECT
          p.proNum,
          COUNT(DISTINCT w.empSSN) AS MemberCount
        FROM
          tblProject p
          LEFT JOIN tblWorksOn w ON p.proNum = w.proNum
        GROUP BY
          p.proNum
      ) AS MinMemberCountTable
  )

  --- cau 29-- -
  SELECT
  p.proNum AS ProjectID,
  p.proName AS ProjectName,
  COUNT(DISTINCT w.empSSN) AS MemberCount
FROM
  tblProject p
  LEFT JOIN tblWorksOn w ON p.proNum = w.proNum
GROUP BY
  p.proNum,
  p.proName
HAVING
  COUNT(DISTINCT w.empSSN) = (
    SELECT
      MAX(MemberCount)
    FROM
      (
        SELECT
          p.proNum,
          COUNT(DISTINCT w.empSSN) AS MemberCount
        FROM
          tblProject p
          LEFT JOIN tblWorksOn w ON p.proNum = w.proNum
        GROUP BY
          p.proNum
      ) AS MaxMemberCountTable
  )
  --cau30--
  SELECT
  p.proNum AS ProjectID,
  p.proName AS ProjectName,
  SUM(w.workHours) AS TotalWorkHours
FROM
  tblProject p
  INNER JOIN tblWorksOn w ON p.proNum = w.proNum
GROUP BY
  p.proNum,
  p.proName
HAVING
  SUM(w.workHours) = (
    SELECT
      MIN(TotalWorkHours)
    FROM
      (
        SELECT
          p.proNum,
          SUM(w.workHours) AS TotalWorkHours
        FROM
          tblProject p
          INNER JOIN tblWorksOn w ON p.proNum = w.proNum
        GROUP BY
          p.proNum
      ) AS MinTotalWorkHoursTable
  )


  -- cau 31 --
  SELECT
  p.proNum AS ProjectID,
  p.proName AS ProjectName,
  SUM(w.workHours) AS TotalWorkHours
FROM
  tblProject p
  INNER JOIN tblWorksOn w ON p.proNum = w.proNum
GROUP BY
  p.proNum,
  p.proName
HAVING
  SUM(w.workHours) = (
    SELECT
      MAX(TotalWorkHours)
    FROM
      (
        SELECT
          p.proNum,
          SUM(w.workHours) AS TotalWorkHours
        FROM
          tblProject p
          INNER JOIN tblWorksOn w ON p.proNum = w.proNum
        GROUP BY
          p.proNum
      ) AS MaxTotalWorkHoursTable
  )
-- cau 32---
SELECT
  l.locName AS Workplace,
  COUNT(DISTINCT d.depNum) AS DepartmentCount
FROM
  tblLocation l
  INNER JOIN tblDepLocation dl ON l.locNum = dl.locNum
  INNER JOIN tblDepartment d ON dl.depNum = d.depNum
GROUP BY
  l.locName

  --- cau33---
  SELECT
  d.depNum AS DepartmentID,
  d.depName AS DepartmentName,
  COUNT(dl.locNum) AS WorkplaceCount
FROM
  tblDepartment d
  LEFT JOIN tblDepLocation dl ON d.depNum = dl.depNum
GROUP BY
  d.depNum,
  d.depName

  -- cau 34---
  SELECT
  d.depNum AS DepartmentID,
  d.depName AS DepartmentName,
  COUNT(dl.locNum) AS WorkplaceCount
FROM
  tblDepartment d
  LEFT JOIN tblDepLocation dl ON d.depNum = dl.depNum
GROUP BY
  d.depNum,
  d.depName
HAVING
  COUNT(dl.locNum) = (
    SELECT
      MAX(WorkplaceCount)
    FROM
      (
        SELECT
          d.depNum,
          COUNT(dl.locNum) AS WorkplaceCount
        FROM
          tblDepartment d
          LEFT JOIN tblDepLocation dl ON d.depNum = dl.depNum
        GROUP BY
          d.depNum
      ) AS WorkplaceCountTable
  )
  --- cau35---
  SELECT TOP 1
  d.depNum AS DepartmentID,
  d.depName AS DepartmentName,
  COUNT(dl.locNum) AS WorkplaceCount
FROM
  tblDepartment d
  LEFT JOIN tblDepLocation dl ON d.depNum = dl.depNum
GROUP BY
  d.depNum,
  d.depName
ORDER BY
  WorkplaceCount ASC
  --- cau 36 ---
  SELECT TOP 1
  l.locName AS WorkplaceName,
  COUNT(d.depNum) AS DepartmentCount
FROM
  tblLocation l
  INNER JOIN tblDepLocation dl ON l.locNum = dl.locNum
  INNER JOIN tblDepartment d ON dl.depNum = d.depNum
GROUP BY
  l.locName
ORDER BY
  DepartmentCount DESC

  --cau37--
  SELECT TOP 1
  l.locName AS WorkplaceName,
  COUNT(d.depNum) AS DepartmentCount
FROM
  tblLocation l
  INNER JOIN tblDepLocation dl ON l.locNum = dl.locNum
  INNER JOIN tblDepartment d ON dl.depNum = d.depNum
GROUP BY
  l.locName
ORDER BY
  DepartmentCount ASC
  -- cau 38--
  SELECT TOP 1
  e.empSSN AS EmployeeID,
  e.empName AS EmployeeName,
  COUNT(d.depName) AS DependentsCount
FROM
  tblEmployee e
  LEFT JOIN tblDependent d ON e.empSSN = d.empSSN
GROUP BY
  e.empSSN, e.empName
ORDER BY
  DependentsCount DESC
  -- cau 39---
  SELECT TOP 1
  e.empSSN AS EmployeeID,
  e.empName AS EmployeeName,
  COUNT(d.depName) AS DependentsCount
FROM
  tblEmployee e
  LEFT JOIN tblDependent d ON e.empSSN = d.empSSN
GROUP BY
  e.empSSN, e.empName
ORDER BY
  DependentsCount ASC

-- cau 40---
SELECT
  e.empSSN AS EmployeeID,
  e.empName AS EmployeeName,
  d.depName AS DepartmentName
FROM
  tblEmployee e
  LEFT JOIN tblDependent d ON e.empSSN = d.empSSN
WHERE
  d.depName IS NULL
  -- cau 41--
  SELECT
  d.depNum AS DepartmentID,
  d.depName AS DepartmentName
FROM
  tblDepartment d
  LEFT JOIN tblEmployee e ON d.depNum = e.depNum
WHERE
  e.empSSN IS NULL

  -- cau 42---
	  SELECT
	  e.empSSN AS EmployeeID,
	  e.empName AS EmployeeName,
	  d.depName AS DepartmentName
	FROM
	  tblEmployee e
	  INNER JOIN tblDepartment d ON e.depNum = d.depNum
	  LEFT JOIN tblWorksOn w ON e.empSSN = w.empSSN
	WHERE
	  w.proNum IS NULL
  -- cau 43---
  SELECT
  d.depNum AS DepartmentID,
  d.depName AS DepartmentName
FROM
  tblDepartment d
  LEFT JOIN tblEmployee e ON d.depNum = e.depNum
WHERE
  e.empSSN IS NULL

  -- cau 44--
select  depNum, depName
from  tblDepartment
where depnum not in  (select  A.depNum
						from  (tblProject B inner join tblDepartment A on B.depNum=A.depNum) inner join  tblEmployee C on C.depnum = A.depnum)

 -- cau 45 --
 select D.depNum, D.depName, Count(P.depNum) As SLP  from tblDepartment D Join tblProject P
 On  D.DepNum = P.Depnum 
 Group By D.depNum, D.depName

 -- cau 46---
 With t AS
 (select D.depNum, D.depName, Count(P.depNum) As SLP  from tblDepartment D Join tblProject P
 On  D.DepNum = P.Depnum 
 Group By D.depNum, D.depName)
 select * from t
 Where t.SLP = (Select Min(SLP) From t)
 -- cau 47--
 With t AS
 (select D.depNum, D.depName, Count(P.depNum) As SLP  from tblDepartment D Join tblProject P
 On  D.DepNum = P.Depnum 
 Group By D.depNum, D.depName)
 select * from t
 Where t.SLP = (Select MAX(SLP) From t)
 -- cau48--
 select D.depnum, D.depname, P.proname, count(empSSN) as snv From tblDepartment D
 join tblProject P
 on D.depnum = P.depNum
 join tblEmployee E
 on  D.depNum= E.depNum
 Group by D.depnum, D.depname, P.proname
 having count(empSSN) >=5

  


 
 
 -- cau 50 ---





	
select *
from tblDependent

-- ko co cai gi lien ket thi sẽ thành tích decat --> nó chỉ nối liên tục 
-- bai moi--- 2 bang lien quan voi nhau  
select empSSN, empName , E.depNum, depName
from tblEmployee E , tblDepartment D
where E.depNum  = D.depNum -- liên kết chung , chống tích decat 
-- vidu2--
--- 3 bảng này liên quan với nhau --- 
select e.empSSN , empName, proName
from tblEmployee e, tblProject p , tblWorksOn w
where e.empSSN = w.empSSN and w.proNum  = p.proNum 
-- cách dùng chuyên nghiệp , đẩy lên from cho 3 cái liên quan với nhau --- 
select empSSN, empName , d.depNum, depName
from tblEmployee e inner join tblDepartment d on e.depNum = d.depNum
--- cách chuyên nghiệp 3 bảng liên quan với nhau , nhớ nối theo thứ tự của bảng ERD
select e.empSSN , empName, proName
from tblEmployee e inner join tblWorksOn w on e.empSSN = w.empSSN inner join tblProject p on w.proNum = p.proNum

-- left/right outer join---
-- ví dụ tiền phòng và dịch vụ trong khách sạn , ở mà ko dùng dịch vụ hoặc dùng dịch vụ hoặc ko ở thì phải dùng right/left outer join


 
-- diden ten nhung nguoi  không có những dự án nào 

select *
from tblEmployee 
where  empSSN not in (select empSSN  from [dbo].[tblWorksOn])
 

 select * 
 from tblWorksOn

select *
from tblDepartment
--14.Cho biết số lượng người phụ thuộc theo giới tính. Thông tin yêu cầu: giới tính, số lượng người phụ thuộc

select  depSex , count(depName) as 'soluongnguoiphuthuoc'
from tblDependent
GROUP BY depSex

--17 Cho biết phòng ban nào có số lượng người phụ thuộc là ít nhất. Thông tin yêu cầu: mã phòng ban, tên phòng ban, số lượng người phụ thuộc
-- sắp xếp và lấy top của nó -- 





 
