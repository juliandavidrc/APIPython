
# Query 1

select department, job, 
      (case when quarter = 1 then conteo else 0 end) Q1,
      (case when quarter = 2 then conteo else 0 end) Q2,
      (case when quarter = 3 then conteo else 0 end) Q3,
      (case when quarter = 4 then conteo else 0 end) Q4
from
(
SELECT COALESCE(d.department,'Undefined') as department, COALESCE(j.job,'Undefined') as Job, EXTRACT(QUARTER FROM to_date(e.field2,'YYYY-MM-DD')) as quarter,
count(*) conteo
FROM "public"."hired_employees" e
LEFT JOIN "public"."departments" d ON d.id = e.department_id
LEFT JOIN "public"."jobs" j ON j.id = e.job_id
WHERE DATE_PART('Year', to_date(e.field2,'YYYY-MM-DD')) = '2021'
group by 1,2,3
)r
order by department,job



# query 2
SELECT d.id,
       COALESCE(d.department, 'Undefined') department,
       count(*) hired
FROM public.hired_employees e
LEFT JOIN public.departments d ON d.id = e.department_id
GROUP BY 1,2
HAVING count(*) > (SELECT avg(hired)::float FROM
     (SELECT d.department,
             count(*) hired
      FROM public.hired_employees e
      LEFT JOIN public.departments d ON d.id = e.department_id
      WHERE DATE_PART('Year', to_date(e.field2, 'YYYY-MM-DD')) = '2021'
      GROUP BY 1
      )
      d)
ORDER BY 3 DESC;

# ATHENA
select department, job, 
      (case when quarter = 1 then conteo else 0 end) Q1,
      (case when quarter = 2 then conteo else 0 end) Q2,
      (case when quarter = 3 then conteo else 0 end) Q3,
      (case when quarter = 4 then conteo else 0 end) Q4
from
(
SELECT d.department, COALESCE(j.job,'Undefined') as Job, QUARTER(e.hired_date) as quarter,
count(*) conteo
FROM (
		SELECT 
			"id",
			"employee_name",
			from_iso8601_timestamp((CASE WHEN "hired_date" = '' THEN '1900-01-01T00:00:00Z' ELSE "hired_date" END)) as hired_date,
			coalesce("department_id",0) as department_id,
			coalesce("job_id",0) as job_id
		FROM "mydatabase"."hr") e
LEFT JOIN "mydatabase"."departments" d ON d.id = e.department_id
LEFT JOIN "mydatabase"."jobs" j ON j.id = e.job_id
WHERE YEAR(e.hired_date) = 2021
group by 1,2,3
)r
order by department, job


