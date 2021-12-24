# Author: Daniel Hall

import bcrypt
import threading
from functools import cache
import itertools


@cache
def Openfiles(passwords, user_hash):
    temp_dict = {}
    temp_list = []

    for word in user_hash:
        total = word.split()

        username = total[0]

        hashh = total[1].lstrip("b'").strip("'").encode('utf-8')

        temp_dict[username] = hashh

    for code in passwords:
        code = code.rstrip("\n")
        code = code.encode('utf-8')

        temp_list.append(code)

    return temp_list, temp_dict


def Hashchecker1(passwords, hashes):
    for password in passwords:
        for hashe in hashes.keys() and hashes.items():

            if bcrypt.checkpw(password, hashe[1]):
                with open("correct_passwords.txt", 'a') as a:
                    print(f"{hashe[0]} matches password {password}")
                    a.write(f"{hashe[0]} matches password {password}")
                    a.close()

            else:
                print("Username: ", hashe[0])  # username
                print("Hash: ", hashe[1])  # hash
                print("Password: ", password, "\n")


def Hashchecker2(passwords, hashes):
    for password in passwords:
        for hashe in hashes.keys() and hashes.items():

            if bcrypt.checkpw(password, hashe[1]):
                with open("correct_passwords.txt", 'a') as a:
                    print(f"{hashe[0]} matches password {password}")
                    a.write(f"{hashe[0]} matches password {password}")
                    a.close()

            else:
                print("Username: ", hashe[0])  # username
                print("Hash: ", hashe[1])  # hash
                print("Password: ", password, "\n")


def main1():
    with open("passwordlist.txt", 'rt') as passwords:
        with open("username_passwordhash.txt", 'rt') as user_hash:
            exports = Openfiles(passwords, user_hash)

            n = len(exports[1]) // 2
            i = iter(exports[1].items())

            half1 = dict(itertools.islice(i, n))
            half2 = dict(i) # Not Used

            # print(exports[0])  # Passwords
            # print(exports[1])  # Hashes and usernames
            Hashchecker1(exports[0], half1)


def main2():
    with open("passwordlist.txt", 'rt') as passwords:
        with open("username_passwordhash.txt", 'rt') as user_hash:
            exports = Openfiles(passwords, user_hash)

            n = len(exports[1]) // 2
            i = iter(exports[1].items())

            half1 = dict(itertools.islice(i, n)) # Not Used
            half2 = dict(i)

            # print(exports[0])  # Passwords
            # print(exports[1])  # Hashes and usernames
            Hashchecker1(exports[0], half2)


t1 = threading.Thread(target=main1)
t2 = threading.Thread(target=main2)

t1.start()
t2.start()