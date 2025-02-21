
## install python 3.8, 3.10 or 3.11 

## create venv 
    python -m venv snowpark-venv
    source snowpark-venv/bin/activate
## install snowflake python 
    pip install snowflake-snowpark-python
![image](https://github.com/user-attachments/assets/b884b798-3701-4a2c-9f21-d455b1dd3be5)

## iN VScode > 
    import os
    import snowflake.snowpark.functions
    from snowflake.snowpark import Session
    from snowflake.snowpark.functions import col
![image](https://github.com/user-attachments/assets/1aab545a-61fa-4025-9c94-701e63e4f533)


## Test connection to Snowflake from VScode 

## Error is occurred 
------------------------------------------
    >>> test_session = Session.builder.configs(connection_parameters).create()
    
            Traceback (most recent call last):
              File "/home/wiks/Documents/Wikx_personal/2025/RnD_2025/Snowflake_DE/snowpark_DE/snowpark-venv/lib/python3.11/site-packages/snowflake/connector/vendored/urllib3/connection.py", line 174, in 
             _new_conn
                conn = connection.create_connection(
                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
              File "/home/wiks/Documents/Wikx_personal/2025/RnD_2025/Snowflake_DE/snowpark_DE/snowpark-venv/lib/python3.11/site-packages/snowflake/connector/vendored/urllib3/util/connection.py", line 
                 79, in create_connection
                for res in socket.getaddrinfo(host, port, family, socket.SOCK_STREAM):
                           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
              File "/usr/lib/python3.11/socket.py", line 974, in getaddrinfo
                for res in _socket.getaddrinfo(host, port, family, type, proto, flags):
                           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
            socket.gaierror: [Errno -3] Temporary failure in name resolution
            
            During handling of the above exception, another exception occurred:
            
            Traceback (most recent call last):
              File "/home/wiks/Documents/Wikx_personal/2025/RnD_2025/Snowflake_DE/snowpark_DE/snowpark-venv/lib/python3.11/site-packages/snowflake/connector/vendored/urllib3/connectionpool.py", line 
             715, in urlopen
                httplib_response = self._make_request(
                                   ^^^^^^^^^^^^^^^^^^^
              File "/home/wiks/Documents/Wikx_personal/2025/RnD_2025/Snowflake_DE/snowpark_DE/snowpark-venv/lib/python3.11/site-packages/snowflake/connector/vendored/urllib3/connectionpool.py", line 404, in _make_request
                self._validate_conn(conn)
              File "/home/wiks/Documents/Wikx_personal/2025/RnD_2025/Snowflake_DE/snowpark_DE/snowpark-venv/lib/python3.11/site-packages/snowflake/connector/vendored/urllib3/connectionpool.py", line 1058, in _validate_conn
                conn.connect()
              File "/home/wiks/Documents/Wikx_personal/2025/RnD_2025/Snowflake_DE/snowpark_DE/snowpark-venv/lib/python3.11/site-packages/snowflake/connector/vendored/urllib3/connection.py", line 363, in connect
                self.sock = conn = self._new_conn()
                                   ^^^^^^^^^^^^^^^^
              File "/home/wiks/Documents/Wikx_personal/2025/RnD_2025/Snowflake_DE/snowpark_DE/snowpark-venv/lib/python3.11/site-packages/snowflake/connector/vendored/urllib3/connection.py", line 186, in _new_conn
                raise NewConnectionError(
            snowflake.connector.vendored.urllib3.exceptions.NewConnectionError: <snowflake.connector.vendored.urllib3.connection.HTTPSConnection object at 0x7fdeca59d350>: Failed to establish a new connection: [Errno -3] Temporary failure in name resolution
            
            During handling of the above exception, another exception occurred:
            
            Traceback (most recent call last):
              File "/home/wiks/Documents/Wikx_personal/2025/RnD_2025/Snowflake_DE/snowpark_DE/snowpark-venv/lib/python3.11/site-packages/snowflake/connector/vendored/requests/adapters.py", line 486, in send
                resp = conn.urlopen(
                       ^^^^^^^^^^^^^
              File "/home/wiks/Documents/Wikx_personal/2025/RnD_2025/Snowflake_DE/snowpark_DE/snowpark-venv/lib/python3.11/site-packages/snowflake/connector/vendored/urllib3/connectionpool.py", line 827, in urlopen
                return self.urlopen(
                       ^^^^^^^^^^^^^
              File "/home/wiks/Documents/Wikx_personal/2025/RnD_2025/Snowflake_DE/snowpark_DE/snowpark-venv/lib/python3.11/site-packages/snowflake/connector/vendored/urllib3/connectionpool.py", line 799, in urlopen
                retries = retries.increment(
                          ^^^^^^^^^^^^^^^^^^
              File "/home/wiks/Documents/Wikx_personal/2025/RnD_2025/Snowflake_DE/snowpark_DE/snowpark-venv/lib/python3.11/site-packages/snowflake/connector/vendored/urllib3/util/retry.py", line 592, in increment
                raise MaxRetryError(_pool, url, error or ResponseError(cause))
            snowflake.connector.vendored.urllib3.exceptions.MaxRetryError: HTTPSConnectionPool(host='https', port=443): Max retries exceeded with url: //wbnepdb-vx98979.snowflakecomputing.com.snowflakecomputing.com:443/session/v1/login-request?request_id=c7840b0d-c81f-4d94-a04a-d687b26ea479&databaseName=DEMO_DB&schemaName=PUBLIC&warehouse=COMPUTE_WH&roleName=ACCOUNTADMIN (Caused by NewConnectionError('<snowflake.connector.vendored.urllib3.connection.HTTPSConnection object at 0x7fdeca59d350>: Failed to establish a new connection: [Errno -3] Temporary failure in name resolution'))
            
            During handling of the above exception, another exception occurred:
            
            Traceback (most recent call last):
              File "/home/wiks/Documents/Wikx_personal/2025/RnD_2025/Snowflake_DE/snowpark_DE/snowpark-venv/lib/python3.11/site-packages/snowflake/connector/network.py", line 1081, in _request_exec
                raw_ret = session.request(
                          ^^^^^^^^^^^^^^^^
              File "/home/wiks/Documents/Wikx_personal/2025/RnD_2025/Snowflake_DE/snowpark_DE/snowpark-venv/lib/python3.11/site-packages/snowflake/connector/vendored/requests/sessions.py", line 589, in 
               request
                resp = self.send(prep, **send_kwargs)
                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
              File "/home/wiks/Documents/Wikx_personal/2025/RnD_2025/Snowflake_DE/snowpark_DE/snowpark-venv/lib/python3.11/site-packages/snowflake/connector/vendored/requests/sessions.py", line 703, in 
                 send
                r = adapter.send(request, **kwargs)
                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
              File "/home/wiks/Documents/Wikx_personal/2025/RnD_2025/Snowflake_DE/snowpark_DE/snowpark-venv/lib/python3.11/site-packages/snowflake/connector/vendored/requests/adapters.py", line 519, in 
               send
                raise ConnectionError(e, request=request)
            snowflake.connector.vendored.requests.exceptions.ConnectionError: HTTPSConnectionPool(host='https', port=443): Max retries exceeded with url: //wbnepdb- 
                vx98979.snowflakecomputing.com.snowflakecomputing.com:443/session/v1/login-request?request_id=c7840b0d-c81f-4d94-a04a- 
            d687b26ea479&databaseName=DEMO_DB&schemaName=PUBLIC&warehouse=COMPUTE_WH&roleName=ACCOUNTADMIN (Caused by NewConnectionError('<snowflake.connector.vendored.urllib3.connection.HTTPSConnection 
                 object at 0x7fdeca59d350>: Failed to establish a new connection: [Errno -3] Temporary failure in name resolution'))
            
            During handling of the above exception, another exception occurred:
            
            Traceback (most recent call last):
              File "/home/wiks/Documents/Wikx_personal/2025/RnD_2025/Snowflake_DE/snowpark_DE/snowpark-venv/lib/python3.11/site-packages/snowflake/connector/connection.py", line 1432, in _authenticate
                auth.authenticate(
              File "/home/wiks/Documents/Wikx_personal/2025/RnD_2025/Snowflake_DE/snowpark_DE/snowpark-venv/lib/python3.11/site-packages/snowflake/connector/auth/_auth.py", line 265, in authenticate
                ret = self._rest._post_request(
                      ^^^^^^^^^^^^^^^^^^^^^^^^^
              File "/home/wiks/Documents/Wikx_personal/2025/RnD_2025/Snowflake_DE/snowpark_DE/snowpark-venv/lib/python3.11/site-packages/snowflake/connector/network.py", line 749, in _post_request
                ret = self.fetch(
                      ^^^^^^^^^^^
              File "/home/wiks/Documents/Wikx_personal/2025/RnD_2025/Snowflake_DE/snowpark_DE/snowpark-venv/lib/python3.11/site-packages/snowflake/connector/network.py", line 864, in fetch
                ret = self._request_exec_wrapper(
                      ^^^^^^^^^^^^^^^^^^^^^^^^^^^
              File "/home/wiks/Documents/Wikx_personal/2025/RnD_2025/Snowflake_DE/snowpark_DE/snowpark-venv/lib/python3.11/site-packages/snowflake/connector/network.py", line 992, in                     
              _request_exec_wrapper
                raise e
              File "/home/wiks/Documents/Wikx_personal/2025/RnD_2025/Snowflake_DE/snowpark_DE/snowpark-venv/lib/python3.11/site-packages/snowflake/connector/network.py", line 914, in 
                _request_exec_wrapper
                return_object = self._request_exec(
                                ^^^^^^^^^^^^^^^^^^^
              File "/home/wiks/Documents/Wikx_personal/2025/RnD_2025/Snowflake_DE/snowpark_DE/snowpark-venv/lib/python3.11/site-packages/snowflake/connector/network.py", line 1179, in _request_exec
                raise OperationalError(
            snowflake.connector.errors.OperationalError: 251011: ConnectionTimeout occurred during login. Will be handled by authenticator
            
            The above exception was the direct cause of the following exception:
            
            Traceback (most recent call last):
              File "<stdin>", line 1, in <module>
              File "/home/wiks/Documents/Wikx_personal/2025/RnD_2025/Snowflake_DE/snowpark_DE/snowpark-venv/lib/python3.11/site-packages/snowflake/snowpark/session.py", line 490, in create
                session = self._create_internal(self._options.get("connection"))
                          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
              File "/home/wiks/Documents/Wikx_personal/2025/RnD_2025/Snowflake_DE/snowpark_DE/snowpark-venv/lib/python3.11/site-packages/snowflake/snowpark/session.py", line 532, in _create_internal
                ServerConnection({}, conn) if conn else ServerConnection(self._options),
                                                        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
              File "/home/wiks/Documents/Wikx_personal/2025/RnD_2025/Snowflake_DE/snowpark_DE/snowpark-venv/lib/python3.11/site-packages/snowflake/snowpark/_internal/server_connection.py", line 167, in                 __init__
                self._conn = conn if conn else connect(**self._lower_case_parameters)
                                               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
              File "/home/wiks/Documents/Wikx_personal/2025/RnD_2025/Snowflake_DE/snowpark_DE/snowpark-venv/lib/python3.11/site-packages/snowflake/connector/__init__.py", line 55, in Connect
                return SnowflakeConnection(**kwargs)
                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
              File "/home/wiks/Documents/Wikx_personal/2025/RnD_2025/Snowflake_DE/snowpark_DE/snowpark-venv/lib/python3.11/site-packages/snowflake/connector/connection.py", line 467, in __init__
                self.connect(**kwargs)
              File "/home/wiks/Documents/Wikx_personal/2025/RnD_2025/Snowflake_DE/snowpark_DE/snowpark-venv/lib/python3.11/site-packages/snowflake/connector/connection.py", line 786, in connect
                self.__open_connection()
              File "/home/wiks/Documents/Wikx_personal/2025/RnD_2025/Snowflake_DE/snowpark_DE/snowpark-venv/lib/python3.11/site-packages/snowflake/connector/connection.py", line 1116, in                                 __open_connection
                self.authenticate_with_retry(self.auth_class)
              File "/home/wiks/Documents/Wikx_personal/2025/RnD_2025/Snowflake_DE/snowpark_DE/snowpark-venv/lib/python3.11/site-packages/snowflake/connector/connection.py", line 1404, in                                     authenticate_with_retry
                self._authenticate(auth_instance)
              File "/home/wiks/Documents/Wikx_personal/2025/RnD_2025/Snowflake_DE/snowpark_DE/snowpark-venv/lib/python3.11/site-packages/snowflake/connector/connection.py", line 1478, in _authenticate
                raise auth_op from e
              File "/home/wiks/Documents/Wikx_personal/2025/RnD_2025/Snowflake_DE/snowpark_DE/snowpark-venv/lib/python3.11/site-packages/snowflake/connector/connection.py", line 1453, in _authenticate
                auth_instance.handle_timeout(
              File "/home/wiks/Documents/Wikx_personal/2025/RnD_2025/Snowflake_DE/snowpark_DE/snowpark-venv/lib/python3.11/site-packages/snowflake/connector/auth/by_plugin.py", line 213, in                             handle_timeout
                raise error
            snowflake.connector.errors.OperationalError: 250001: Could not connect to Snowflake backend after 2 attempt(s).Aborting
            >>> 
            KeyboardInterrupt


  ##---------------------------------------------------
  # Solution > 
  ## Worked solution was > Get the correct account name from the below query  
  Note: The Snowflake web portal gives the account name, but it did not work for me. The only worked account name got from the below query 
  
  ![image](https://github.com/user-attachments/assets/3a715482-6115-4452-9689-76cb22009edd)

# We can check if there is a network connection issue from the two commands 
       nslookup vx98979.ap-south-1.aws.snowflakecomputing.com
       curl -v https://vx98979.ap-south-1.aws.snowflakecomputing.com:443/session/v1/login-request

 ![image](https://github.com/user-attachments/assets/467adc41-c66d-42af-a86c-a1dd713455d9)

##-----------------------------------------------------
   
