from drcrypt.hash import MD5
from drcrypt import compare_hash

H = "4ddd4137b84ff2db7291b568289717f0"
SEL = "<1755.1.5f403625.BcWGgpKzUPRC8vscWn0wuA==@vps-7e2f5a72>"

with open("wordlist2.txt", encoding="utf-8") as f:

    for ligne in f:
            mot = ligne.strip()
            data = SEL + mot

            md5_hash = MD5()
            md5_hash.update(data.encode("utf-8"))
            md5_hash.finalize()
            hashed = md5_hash.hexdigest()
            result = compare_hash(MD5(), data, hashed)

            if hashed == H:
                print("Hashes match! The data matches the target hash.")
                print("Mot:", mot)
                break

            else:
                print("Hashes do not match. The data does not match the target hash.")

#lire wl
#selectionner B
#ajouter B a SEL
#Calculer H (SEL + B)
#Comparer les hash avec le hash par défault




