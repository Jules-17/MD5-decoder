import hashlib

H = "4ddd4137b84ff2db7291b568289717f0"
SEL = "<1755.1.5f403625.BcWGgpKzUPRC8vscWn0wuA==@vps-7e2f5a72>"

with open("wordlist3.txt", encoding="latin-1") as f:

    for ligne in f:
        mot = ligne.strip()
        mot2 =  SEL + mot
        hashed = hashlib.md5(mot2.encode()).hexdigest()

        if hashed == H:
                print("Hashes match!")
                print("Mot:", mot)
                break

        #else:
    print("Hashes do not match.")


