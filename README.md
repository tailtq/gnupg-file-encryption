# GnuPG (GPG)

> GnuPG uses public-key cryptography so that users may communicate securely. In a public-key system, each user has a pair of keys consisting of a private key and a public key. A user's private key is kept secret; it need never be revealed. The public key may be given to anyone with whom the user wants to communicate.

### Generate Input Parameters:

- User ID (name/email address): associate the key being created with a real person.

    (Ex: David Steele [dsteele@gmail.com](mailto:dsteele@gmail.com))

    - Name-Real
    - Name-Email
- Passphrase: protect the primary and subordinate private keys
- Signature
- Expire-Date
- ...

### Exporting Keys Parameters:

- Armor: Creating ASCII instead of binary file
- Passphrase

### Encryption and Decryption

Data intended for some particular recipients is encrypted with the public keys of those recipients. Each recipient can decrypt the encrypted data using the corresponding private key.

- sign??
- always_trust: (true ⇒ Skip key validation)
- passphrase: use when accessing the keyrings

---

**Note:** GnuPG works on the basis of a “home directory” which is used to store public and private keyring files

...
