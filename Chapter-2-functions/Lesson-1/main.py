def is_palindrome(arr):
    # حساب عدد العناصر في المصفوفة
    n = len(arr)
    
    # مقارنة العناصر من البداية والنهاية
    for i in range(n // 2):
        if arr[i] != arr[n - i - 1]:
            return False
    
    return True

# الحصول على المصفوفة من المستخدم

input_str = input("Enter list of numbers seperated by comma:")
arr = [int(num) for num in input_str.split(',')]
    
if is_palindrome(arr):
    print("Yes")
else:
    print("No")
