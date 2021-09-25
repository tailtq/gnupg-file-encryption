import gnupg

gpg = gnupg.GPG(gnupghome='/home/tai/.gnupg2')

file_data = open("test.asc", "rb").read()

input_data: gnupg.ImportResult
input_data = gpg.import_keys(file_data, )
gpg.trust_keys(input_data.fingerprints, "TRUST_ULTIMATE")
print(gpg.list_keys())

