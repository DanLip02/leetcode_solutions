def exchange(amount, bills):
    bills = dict(sorted(bills.items(), reverse=True))  # сортировка по номиналу
    result = {}

    for denom in list(bills.keys()):  # итерация по номиналам
        if amount <= 0:
            break

        count = min(amount // denom, bills[denom])
        if count > 0:
            result[denom] = count
            amount -= denom * count
            bills[denom] -= count

        # если купюры кончились — вычеркиваем
        if bills[denom] == 0:
            bills.pop(denom)

    # если всё разменяли — успех, иначе None
    return result if amount == 0 else None


# 🔹 пример
bills = {5: 1, 3: 1, 1: 2 }
print(exchange(7, bills))