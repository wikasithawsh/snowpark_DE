import os
import snowflake.snowpark.functions
from snowflake.snowpark import Session
from snowflake.snowpark.functions import col

connection_parameters = {"account":"AV52212.ap-south-1.aws",
"user":"HESHANWSH",
"password": "wikasithaASD@2025",
"role":"ACCOUNTADMIN",
"warehouse":"COMPUTE_WH",
"database":"DEMO_DB",
"schema":"PUBLIC"
}

test_session = Session.builder.configs(connection_parameters).create()
session.

print(test_session.sql("select current_warehouse(), current_database(), current_schema()").collect())

session = Session.builder.configs(connection_parameters).create()


