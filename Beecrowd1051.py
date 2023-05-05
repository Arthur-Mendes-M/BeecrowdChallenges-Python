renda = float(input())

if renda <= 2000.00:
    print("Isento")
else:
    if renda <= 3000.00:
        imposto = (renda - 2000.00) * 0.08
    elif renda <= 4500.00:
        imposto = 1000.00 * 0.08 + (renda - 3000.00) * 0.18
    else:
        imposto = 1000.00 * 0.08 + 1500.00 * 0.18 + (renda - 4500.00) * 0.28

    print("R$ {:.2f}".format(imposto))
