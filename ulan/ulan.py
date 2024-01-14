def fibonacci_numbers(num, memo={}):
    # Базовые случаи: для num <= 0 возвращаем 0, для num == 1 возвращаем 1
    if num <= 0:
        return 0
    elif num == 1:
        return 1

    # Проверяем, было ли уже вычислено значение для текущего num
    if num in memo:
        return memo[num]
    else:
        # Если значение не было вычислено, рекурсивно вызываем функцию для двух предыдущих чисел
        result = fibonacci_numbers(num - 1, memo) + fibonacci_numbers(num - 2, memo)

        # Сохраняем результат в memo для последующего использования
        memo[num] = result

        # Возвращаем результат
        return result

# Пример использования
result = fibonacci_numbers(100)
print(result)