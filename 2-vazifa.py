def ballni_ol(matn):
    try:
        return int(matn)
    except ValueError:
        return "ball son bolishi kerak"
print(ballni_ol("85"))
print(ballni_ol("salom"))