import gnupg

gpg = gnupg.GPG(gnupghome='/home/tai/.gnupg')

input_data = gpg.gen_key_input(
    name_real="Tai Le",
    name_email="ltquoctaidn98@gmail.com",
    passphrase="123123",
    key_type="RSA",
    key_length=2048,
)
key = gpg.gen_key(input_data)
public_key = gpg.export_keys(str(key))
private_key = gpg.export_keys(str(key), True, passphrase="123123")

with open("public_key.asc", "w") as f:
    f.write(public_key)

with open("private_key.asc", "w") as f:
    f.write(private_key)

print(len(public_key))
