from executeQuery import execute_query

users_query = "DELETE FROM users WHERE username = 'test0';"

execute_query(users_query)