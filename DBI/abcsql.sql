DECLARE @empName Nvarchar(20), @empSalary DECIMAL
SET @empName = N'Mai Duy An'
SET @empSalary = 1000
PRINT @empName + '''s salary is ' + cast(@empSalary AS Varchar)
print @empName + '''s salary is ' + convert(varchar, @empSalary)
--
declare @workhours decimal, @bonus decimal
select @workhours = Sum(workhours)
from tblWorksOn
where empSSN=30121050027
group by empSSN

if (@workhours >300)
	set @bonus = 1000
else
	set @bonus = 500
print @bonus
--
DECLARE	@depNum DECIMAL, @str NVARCHAR(30)
set @depNum = 1
set @str = 
	Case @depNum
		when 1 then N'Phong ban so 1'
		when 2 then N'Phong ban so 2'
		else N' Ma phong ban khac 1,2'
	End
print @str
--
Create procedure INDSPB @mapb int
as 
begin
	select * from tblEmployee
	where depnum = @mapb
end
exec INDSPB 2
--
create function countdep
(@mapb int)
returns int
as 
begin
	declare @sl int
	select @sl = count(empssn)
	from tblEmployee
	where depnum=@mapb
	return @sl
end
 
select dbo.countdep(1)
--
