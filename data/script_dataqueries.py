
# Below are some quick examples

# Assign column name by index
df.columns.values[1] = 'Courses_Fee'
print(df.columns)

# Rename column name by index
df.rename(columns={df.columns[2]: 'Courses_Duration'},inplace=True)
print(df.columns)

# Rename multiple columns
df.rename(columns={df.columns[1]: 'Fee', df.columns[2]: 'Duration'},inplace=True)
print(df.columns)


ddl_table_department = (
    "CREATE TABLE IF NOT EXISTS departments(id int, department varchar(100));")
    
query_departmments = ("select * from departments where department ilike '%s'")


@app.get("/query/dept")
def query_dept():  
    #load df dept
    data_dept = pd.read_csv(path_dept, header=None, names=['id', 'tdepartment'])    
    #load df jobs
    #data_jobs = pd.read_csv(path_jobs, header=None, names=['id', 'job'])    
    #load df hiredemployees
    #data_hiredemp = pd.read_csv(path_hiredemp, header=None, names=['id', 'name', 'datetime', 'department_id', 'job_id'])
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(ddl_table_department)
            for index, row in data_dept.iterrows():
                cursor.execute("INSERT INTO departments (id,department) values(?)", row.id, row.tdepartment)
            connection.commit()
            #cursor.close()
    return "Data Loaded"
	
	
i = 0
sqlLimit = 99999
for x in range(len(df)): #where df is your dataframe
    if i == sqlLimit or i == len(df):
        # sql execution
        if i == len(df):
            break
        else:
            i = 0
            sql = "" # or whatever to set it to what it was at the beginning of the loop
            # add formatted row to sql (with .iloc?)
    else:
        i += 1
        # add formatted row to sql (with .iloc?)
		
		
		
# Sirven		
		
i = 0
sqlLimit = 6
for x in range(len(df)): #where df is your dataframe    
    if i == sqlLimit or i == len(df):     
        print("0")
        print(sqlLimit/2)        
        # sql execution
        if i == len(df):            
            break
        else:
            i = 0            
            sql = "dml executed" # or whatever to set it to what it was at the beginning of the loop                        
            # add formatted row to sql (with .iloc?)
    else:
        i += 1
        # add formatted row to sql (with .iloc?)




i = 0
sqlLimit = 6
for x in range(len(df)): #where df is your dataframe    
    if i == sqlLimit or i == len(df):     
        # sql execution
        if i == len(df):            
            break
        else:
            i = 0            
            sql = "dml executed" # or whatever to set it to what it was at the beginning of the loop
            print(sql)            
            # add formatted row to sql (with .iloc?)
    else:
        i += 1
        # add formatted row to sql (with .iloc?)		
        
        
i = 0
sqlLimit = 6
for x in range(len(df)): #where df is your dataframe    
    if i == sqlLimit or i == len(df):     
        # sql execution
        if i == len(df):            
            break
        else:
            i = 0            
            sql = "dml executed" # or whatever to set it to what it was at the beginning of the loop
            print(sql)            
            print(i) 
            # add formatted row to sql (with .iloc?)
    else:
        i += 1
        # add formatted row to sql (with .iloc?)        
        
        
        
        
        


                
            #Load Deparment Hired Emp
            cursor.execute(ddl_table_hired_emp)
            cursor.execute(dml_delete_hired_emp) 
            cursor.execute("select count(*) from hired_employees")              
            for index, row in data_hiredemp.iloc[0:1000,].iterrows():
                cursor.execute(dml_insert_hired_emp, (row.id, row.name, row.datetime, row.department_id, row.job_id),)                 
                
                
                
                ddl_table_hired_emp = "CREATE TABLE IF NOT EXISTS hired_employees(id int, name varchar(200) NULL, field2 date, department_id int NULL, job_id int NULL);"
                
                cursor.execute(dml_insert_hired_emp, (row.id, row.name, row.field2, row.department_id, row.job_id),)                                          
                
                
                
SELECT * FROM "public"."hired_employees" 
where to_timestamp(field2,'YYYY-MM-DD hh24:mi:ss')::timestamp > '2021-09-18 14:37:49'                


SELECT d.department, j.job, to_date(e.field2,'YYYY-MM-DD') as HireDate,
count(*) 
FROM "public"."hired_employees" e
LEFT JOIN "public"."departments" d ON d.id = e.department_id
LEFT JOIN "public"."jobs" j ON j.id = e.job_id
--WHERE to_date(e.field2,'YYYY') = '2021'
GROUP BY 1,2,3
ORDER BY 4 desc, 3


SELECT d.department, j.job, EXTRACT(QUARTER FROM to_date(e.field2,'YYYY-MM-DD')) as QUARTER,
count(*) 
FROM "public"."hired_employees" e
LEFT JOIN "public"."departments" d ON d.id = e.department_id
LEFT JOIN "public"."jobs" j ON j.id = e.job_id
WHERE DATE_PART('Year', to_date(e.field2,'YYYY-MM-DD')) = '2021'
GROUP BY 1,2,3
ORDER BY 1,2



SELECT d.department, j.job, DATE_PART('Year', to_date(e.field2,'YYYY-MM-DD')) as QUARTER,
count(*) 
FROM "public"."hired_employees" e
LEFT JOIN "public"."departments" d ON d.id = e.department_id
LEFT JOIN "public"."jobs" j ON j.id = e.job_id
WHERE DATE_PART('Year', to_date(e.field2,'YYYY-MM-DD')) = '2021'
GROUP BY 1,2,3
ORDER BY 4 desc, 3


SELECT * FROM 
"public"."hired_employees" where department_id = 8 and job_id = 0



SELECT d.department, COALESCE(j.job,'Undefined') as Job, EXTRACT(QUARTER FROM to_date(e.field2,'YYYY-MM-DD')) as QUARTER,
SUM (CASE WHEN EXTRACT(QUARTER FROM to_date(e.field2,'YYYY-MM-DD')) = 1 )
count(*) 
FROM "public"."hired_employees" e
LEFT JOIN "public"."departments" d ON d.id = e.department_id
LEFT JOIN "public"."jobs" j ON j.id = e.job_id
WHERE DATE_PART('Year', to_date(e.field2,'YYYY-MM-DD')) = '2021'
GROUP BY 1,2,3
ORDER BY 1,2




select department, job, 
      (case when quarter = 1 then conteo else 0 end) Q1,
      (case when quarter = 2 then conteo else 0 end) Q2,
      (case when quarter = 3 then conteo else 0 end) Q3,
      (case when quarter = 4 then conteo else 0 end) Q4
from
(
SELECT d.department, COALESCE(j.job,'Undefined') as Job, EXTRACT(QUARTER FROM to_date(e.field2,'YYYY-MM-DD')) as quarter,
count(*) conteo
FROM "public"."hired_employees" e
LEFT JOIN "public"."departments" d ON d.id = e.department_id
LEFT JOIN "public"."jobs" j ON j.id = e.job_id
WHERE DATE_PART('Year', to_date(e.field2,'YYYY-MM-DD')) = '2021'
AND d.department = 'Accounting'
group by 1,2,3
)r


# Query 1

select department, job, 
      (case when quarter = 1 then conteo else 0 end) Q1,
      (case when quarter = 2 then conteo else 0 end) Q2,
      (case when quarter = 3 then conteo else 0 end) Q3,
      (case when quarter = 4 then conteo else 0 end) Q4
from
(
SELECT d.department, COALESCE(j.job,'Undefined') as Job, EXTRACT(QUARTER FROM to_date(e.field2,'YYYY-MM-DD')) as quarter,
count(*) conteo
FROM "public"."hired_employees" e
LEFT JOIN "public"."departments" d ON d.id = e.department_id
LEFT JOIN "public"."jobs" j ON j.id = e.job_id
WHERE DATE_PART('Year', to_date(e.field2,'YYYY-MM-DD')) = '2021'
AND d.department = 'Accounting'
group by 1,2,3
)r





select avg(conteo)::float from (
SELECT d.department, d.id, EXTRACT(QUARTER FROM to_date(e.field2,'YYYY-MM-DD')) as quarter,
count(*) conteo
FROM "public"."hired_employees" e
LEFT JOIN "public"."departments" d ON d.id = e.department_id
WHERE DATE_PART('Year', to_date(e.field2,'YYYY-MM-DD')) = '2021'
AND d.department = 'Accounting'
group by 1,2,3
)
d


SELECT id, department, conteo (
SELECT d.id, d.department, count(*) conteo
FROM "public"."hired_employees" e
LEFT JOIN "public"."departments" d ON d.id = e.department_id
) r
where r.conteo > 9.5


# query 2
SELECT d.id, COALESCE(d.department ,'Undefined') department , count(*) conteo
FROM "public"."hired_employees" e
LEFT JOIN "public"."departments" d ON d.id = e.department_id
group by 1,2
having count(*) > (select avg(conteo)::float from (
SELECT d.department, d.id, EXTRACT(QUARTER FROM to_date(e.field2,'YYYY-MM-DD')) as quarter,
count(*) conteo
FROM "public"."hired_employees" e
LEFT JOIN "public"."departments" d ON d.id = e.department_id
WHERE DATE_PART('Year', to_date(e.field2,'YYYY-MM-DD')) = '2021'
AND d.department = 'Accounting'
group by 1,2,3
)
d
)
order by 3 desc
