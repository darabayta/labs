n = int(input("Введите количество людей (n): "))

if n <= 0:
    print("Количество людей должно быть больше нуля.")
else:
        total_age = 0

            for i in range(n):
                    age = float(input(f"Введите возраст человека {i+1}: "))
                            total_age += age
                                
                                    average_age = total_age / n
                                        print(f"Средний возраст: {average_age:.2f}") # .2f оставляет 2 знака после запятой
