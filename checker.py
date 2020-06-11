from random import choice
from requests import get, exceptions
from datetime import datetime
from colorama import Fore, Style, init
init()


class TokenChecker():
    def __init__(self, log=False):
        self.URL = "https://discordapp.com/api/v6/users/@me/library"
        self.token_list = []
        self.proxy_list = "https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/https.txt"
        self.timeout = 5

        self.status_codes = {200: 'Valid -', 401: 'Invalid -', 429: 'Too many requests !'}
        self.colors_codes = {200: Fore.GREEN, 401: Fore.RED, 429: Fore.YELLOW}

        self.valid_token = []
        self.invalid_token = []

        self.log_ = log

    def log(self, msg: str, color: Fore):
        if self.log_ is True:
            print(f'{color + Style.BRIGHT}{msg}', Fore.WHITE + Style.NORMAL)

    def addTokenList(self, token_list):
        self.token_list.extend(token_list)

    def addProxyList(self, proxy_list):
        self.proxy_list.extend(proxy_list)

    def setTimeout(self, timeout):
        self.timeout = timeout

    def checkWproxyList(self):

        if self.proxy_list == None:
            self.log("No proxies !", Fore.RED)
            return False

        for token in self.token_list:
            try:
                status = get(self.URL, {'https://':choice(self.proxy_list)}, headers={'Content-Type': 'application/json', 'authorization': token}, timeout=self.timeout).status_code

                if status in self.status_codes:
                    self.log(f'{self.status_codes[status]} {token}', self.colors_codes[status])

                    if status == 200:
                        valid_token.append(token)

                else:
                    self.log('Unknown error. ' + str(status), Fore.RED)

            except exceptions.ConnectionError:
                self.log('Connection error.', Fore.LIGHTRED_EX)


if __name__ == '__main__':

    VALID_TOKEN_FILE = r"valid.txt"
    TOKEN_FILE = r"tokens.txt"


    def remove_shit(foo : list):
        return list(filter(None, list(map(lambda x: str.replace(x, "\n", ""), foo))))

    valid_token = open(VALID_TOKEN_FILE, 'a')

    with open(TOKEN_FILE, 'r') as f:
        token_file = remove_shit(f.readlines())

    checker = TokenChecker(log=True)
    checker.addTokenList(token_file)
    checker.checkWproxyList()

    for token in checker.valid_token: valid_token.write(token + '\n')