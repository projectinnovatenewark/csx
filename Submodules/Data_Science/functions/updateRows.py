from executeQuery import execute_query

users_query = """UPDATE users 
                 SET username = test1 
                 WHERE username = test0;"""
                 
execute_query(users_query)