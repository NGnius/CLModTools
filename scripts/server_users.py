import json, re, sys
#sys.path.append('../libs/')
sys.path.append('libs/')
import get_users


def get_input(prompt, options={"y", "n", ""}):
    '''covenience function for nagging users for an input'''
    response = input(prompt)
    while response not in options:
        response = input(prompt)
    return response

# retrieve current (old) users
old_users=dict()
try:
    with open("server_users.JSON", "r") as server_users_file:
        old_users = json.load(server_users_file)
except FileNotFoundError:
    pass

# retrieve new users from output log
new_users = get_users.get_from_log(input("Where is your output log stored?"))

# process new players
new_players = set()
for user in new_users:
    if user not in old_users:
        new_players.add(user)
        old_users[user] = new_users[user]

print("There are currently", len(old_users), "players who've logged onto your server!")

should_do = get_input("Display user list? [y/n]")

# display user list
if should_do in {"y", ""}:
    print("User list")
    for user in old_users:
        if user in new_players:
            print("\t", user, "ID:"+old_users[user], "*")
        else:
            print("\t", user, "ID:"+old_users[user])
    print("End of users")
    print("New users have a * beside them")

should_do = get_input("Display new users list? [y/n]")

# display new players list
if should_do in {"y", ""}:
    print("New users list")
    for user in new_players:
        print("\t", user, "ID:"+old_users[user])
    print("End of new users")

# save users so they can be compared with the players from next run
with open("server_users.JSON", "w") as server_users_file:
    json.dump(old_users, server_users_file)
