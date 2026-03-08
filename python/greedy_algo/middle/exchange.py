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

def coin_change_bt(coins_dict, amount):
    coins = sorted(coins_dict.items())  # сортируем по номиналу
    min_coins = [float('inf')]  # используем список для замыкания

    def backtrack(idx, remaining, count):
        if remaining == 0:
            min_coins[0] = min(min_coins[0], count)
            return
        if idx == len(coins) or remaining < 0:
            return

        coin, max_count = coins[idx]
        # пробуем использовать 0..max_count монет текущего номинала
        for k in range(0, max_count + 1):
            if remaining - coin * k >= 0:
                backtrack(idx + 1, remaining - coin * k, count + k)

    backtrack(0, amount, 0)
    return min_coins[0] if min_coins[0] != float('inf') else -1