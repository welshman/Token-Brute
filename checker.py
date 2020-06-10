import requests
with open("tokens.txt") as f:
    for line in f:
        token = line.strip("\n")
        headers = {'contentType': 'application/json', 'userAgent': 'userAgent', 'authorization': 'token', 'body': ''}
        url = "https://discordapp.com/api/v6/users/@me"
        r = requests.get(url, headers=headers)
        if r.status_code == 200:
            print("Valid.".format(line.strip("\n")))
            save = open("valid.txt", "a")
            save.write(line)
        else:
            print("Invalid")
