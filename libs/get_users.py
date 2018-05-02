import re

def get_from_log(log_dir):
    '''(path-like str) -> dict
    finds all server users from server's output log
    returns dict of username:id'''
    with open(log_dir, "r") as output_log:
        contents = output_log.read()
    users = re.findall(r"Creating AccountIdServerNode ([^,]+), ([^,]+), u(\S+)", contents)
    #process users
    server_users = dict()
    for user in users:
        if user[0] not in server_users:
            server_users[user[0]] = user[2]
    return server_users
