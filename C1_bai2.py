def Neper(n):
    if n < 0:
        return "Số n phải lớn hơn hoặc bằng 0"
    else:
        e_sum = 0
        factorial = 1
        for k in range(n + 1):
            e_sum += 1 / factorial
            factorial *= (k + 1)
        return e_sum

# Ví dụ sử dụng phương thức Neper
n = int(input("Nhập vào số nguyên n: "))
print("Tổng của các số hạng là:", Neper(n))
