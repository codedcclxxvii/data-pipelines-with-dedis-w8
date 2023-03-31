# Data Pipelines with Redis

## Background Information
As a telecommunications data engineer, you have been tasked with building a pipeline that can efficiently extract, transform, and load data from CSV files into a Postgres database. The data to be extracted is related to customer call logs, which contain information about the duration, cost, and destination of customer calls. The extracted data needs to be transformed to ensure it is in the correct format and structure for storage in the database. The pipeline should also cache data using Redis to speed up the data extraction and transformation.
Guidelines

## You can follow the steps below:
<ul><li>
Start by creating a new Python file and importing the necessary libraries (pandas,
psycopg2, and redis).</li>
<li>
 Create a Redis client object and connect it to the Redis Labs cloud instance.</li>
 <li>
Create an extract function that reads the CSV files using pandas and caches the data in
Redis.</li>
<li>
Create a transform function that cleans, structures, and formats the extracted data.
</li>
<li>
Create a load function that connects to the Postgres database using psycopg2 and loads
the transformed data into the database.</li>
<li>
Combine the extract, transform, and load functions into a single data pipeline that
extracts data from a CSV file, transforms it and loads it into a Postgres database.</li>
<li>Test the pipeline with a sample dataset to ensure it works correctly.</li></ul>

## Sample CSV Files

We’ve provided a sample CSV file (customer_call_logs.csv) that you can use for this data
pipeline. Files for this project can be downloaded from here (link). 

## Deliverables
We will be expected to deliver a GitHub repository with the following:
<ul><li> A python file for the data pipeline - in this repo</li>
<li>Documentation of the pipeline.
Highlight at least 3 best practices used during the implementation.
Recommendations for deployment and running the pipeline with a cloud-based
provider.</li>

## Documentation of the Pipeline
### Overview
This data pipeline extracts customer call log data from a CSV file, transforms it to the appropriate format and structure, and loads it into a Postgres database. The pipeline also caches data using Redis to speed up the extraction and transformation processes.

### Pipeline Steps
<ul><li>Extract: Reads the customer call log data from a CSV file using pandas and caches the data in Redis.</li>
<li>Transform: Cleans, structures, and formats the extracted data to ensure it is in the correct format and structure for storage in the Postgres database.</li>
<li>Load: Connects to the Postgres database using psycopg2 and loads the transformed data into the database.</li></ul>

### Best Practices Used

<ul><li>Separation of Concerns: The pipeline has been separated into distinct extract, transform, and load functions, each with its own responsibility. This makes the pipeline more modular and easier to test and maintain.</li><li>
Use of Libraries: The pipeline utilizes well-established libraries such as pandas, psycopg2, and redis, which are widely used and maintained. This reduces the amount of custom code that needs to be written, simplifies the development process, and reduces the likelihood of errors.</li><li>
Error Handling: The pipeline uses error handling techniques such as checking for missing or duplicate data and handling connection errors. This ensures that the pipeline is resilient to errors and can handle unexpected issues that may arise during execution.</li></ul>

### Recommendations for Deployment and Running the Pipeline with a Cloud-Based Provider
When deploying this pipeline on a cloud-based provider, there are a few things to keep in mind:
<ul><li>
Security: Ensure that appropriate security measures are in place to protect sensitive data. This includes secure connections to Redis and Postgres databases and proper access control mechanisms.</li><li>
Scalability: Consider the scalability requirements of the pipeline and the cloud-based provider's ability to handle increased traffic or data volumes. This may require the use of load balancers, caching mechanisms, and auto-scaling.</li><li>
Monitoring: Implement proper monitoring and logging mechanisms to ensure that any issues with the pipeline are quickly identified and resolved. This includes tracking metrics such as data volume, processing times, and error rates.</li></ul>
