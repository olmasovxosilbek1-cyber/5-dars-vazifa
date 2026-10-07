def foydalanuvchi_nomini_ol(foydalanuvchi):
    try:
        return foydalanuvchi["username"]
    except KeyError:
        return"username topilmadi"

print(foydalanuvchi_nomini_ol({"username":"eshmat"}))
print(foydalanuvchi_nomini_ol({"name":"eshmat"}))