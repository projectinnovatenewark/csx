"""
Actions you can perform on lists and dictionaries
"""

unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

# TODO: verify each user until theres no more unconfirmed users, then
# TODO: move verified users into confirmed users all by using a while loop

while unconfirmed_users:
    current_user = unconfirmed_users.pop()

    print("Verifying username " + current_user.title())
    confirmed_users.append(current_user)

##################################################################################################

# TODO: display all the confirmed users with a for loop
print('\nThe following users have been confirmed:')
for user in confirmed_users:
    print(user.title())
