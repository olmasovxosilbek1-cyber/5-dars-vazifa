def ballni_tekshir(ball):
    if ball <0 or ball>100:
        raise ValueError("ball 0 dan 100 gacha bolishi kerak")
    return ball

print(ballni_tekshir(85))
print(ballni_tekshir(120))
