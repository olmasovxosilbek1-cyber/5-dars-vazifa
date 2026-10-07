def narxlarni_ol(narx_matnlari):
    natija = []

    for matn in narx_matnlari:
        try:
            natija.append(int(matn))
        except ValueError:
            print(f"notogri narx: {matn}")

            return natija
print(narxlarni_ol(["12000","x","5000"]))
print(narxlarni_ol([]))