import json, re, traceback

def get_input(prompt, options={"y", "n", ""}):
    response = input(prompt)
    while response not in options:
        response = input(prompt)
    return response

server_users=dict()

try:
    with open("server_users.JSON", "r") as server_users_file:
        server_users = json.load(server_users_file)
except FileNotFoundError:
    pass

with open(input("Where is your output log stored?"), "r") as output_log:
    contents = output_log.read()
    users = re.findall(r"user verified: (\S+) (\S+)", contents)

#process new players
new_users = set()
for user in users:
    if user[0] not in server_users:
        new_users.add(user[0])
        server_users[user[0]] = user[1]

should_do = get_input("Display user list? [y/n]")

# display user list
if should_do in {"y", ""}:
    print("User list")
    for user in server_users:
        if user in new_users:
            print("\t", user, "ID:"+server_users[user], "*")
        else:
            print("\t", user, "ID:"+server_users[user])
    print("New users have a * beside them")

should_do = get_input("Display new users list? [y/n]")
if should_do in {"y", ""}:
    print("New users list")
    for user in new_users:
        print("\t", user, "ID:"+server_users[user])

with open("server_users.JSON", "w") as server_users_file:
    json.dump(server_users, server_users_file)
