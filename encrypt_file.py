import gnupg
import os

gpg = gnupg.GPG(gnupghome="/home/tai/.gnupg2")

path = "/home/tai/Desktop/fun2.jpg"

with open(path, 'rb') as f:
    status = gpg.encrypt_file(f, recipients=gpg.list_keys()[0]["uids"], output=path + '.encrypted')

print(status.ok)
print(status.stderr)

