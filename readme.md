# Local RestApi / Python Load Data

## Endpoint to load batch 1 up to 1000 transactions (HTTP Post Request)

* Load hired employees data 
http://127.0.0.1:5000/load/hired_employees

* Load dimension data (departments & jobs)
http://127.0.0.1:5000/load/dims

## Endpoint Query Requirements (HTTP GET Request)

* Query1: Number of employees hired for each job and department in 2021 divided by quarter. The table must be ordered alphabetically by department and job.
http://127.0.0.1:5000/query/req1, endpoint JSON result [jsonqry1](results_querys_endpoint/qry1.json)

![Alt text](images/qr1.jpg)
![Alt text](images/qr2.jpg)
![Alt text](images/qr3.jpg)

* Query2: List of ids, name and number of employees hired of each department that hired more employees than the mean of employees hired in 2021 for all the departments, ordered by the number of employees hired (descending).
http://127.0.0.1:5000/query/req2, endpoint JSON result [jsonqry2](results_querys_endpoint/qry2.json)

![Alt text](images/qr2_2.jpg)

## AWS Solution Services

* AWS S3 
![Alt text](aws_solution/s3buckets.jpg)

* AWS GlueCrawlers
![Alt text](aws_solution/GlueCrawlers.JPG)

* AWS GlueDatabase
![Alt text](aws_solution/GlueDatabase.JPG)

* AWS GlueTables
![Alt text](aws_solution/GlueTables.JPG)

* AWS GlueTable Hired Employees
![Alt text](aws_solution/GlueTableHR.JPG)

* AWS Athena Service
![Alt text](aws_solution/AthenaService.JPG)

* AWS IAM_RoleGlue
![Alt text](aws_solution/IAM_RoleGlue.JPG)

* AWS Analysis Hired Employees by Dept, Quarter, 2021
![Alt text](aws_solution/hired_emp_bydept_by_q.jpg)

* AWS Analysis Hired Employees by Dept, Job, Quarter, 2021
![Alt text](aws_solution/hired_emp_bydept_job_by_q.jpg)

* AWS Horizontal Bar Chart by Dept, 2021, Drill Down
![Alt text](aws_solution/analysis2.jpg)

* AWS Horizontal Bar Chart by Dept, Quarter, 2021, Drill Down
![Alt text](aws_solution/analysis21.jpg)