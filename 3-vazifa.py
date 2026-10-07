def elementni_ol(royxat, indeks):
    try:
        return royxat[indeks]
    except IndexError:
        return "bunday index yoq"
print(elementni_ol([10,20,30],1))
print(elementni_ol([10,20,30],5))