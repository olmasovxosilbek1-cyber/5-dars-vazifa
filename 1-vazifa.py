def xavfsiz_bolish(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return("0 ga bolish mumkun emas")

print(xavfsiz_bolish(12,3))
print(xavfsiz_bolish(12,0))