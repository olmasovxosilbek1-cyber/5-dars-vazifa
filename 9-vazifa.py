def ortacha(ballar):
    if not ballar:
        return"ballar yoq"
    return sum(ballar)/len(ballar)

assert ortacha([60,80])== 70.0
assert ortacha({})=="ballar yoq"

print(ortacha([60,80]))
print(ortacha([]))