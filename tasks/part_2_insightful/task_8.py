names = input().split()
vowels = "АУЕЫОЭЯИЮауеыоэяию"
max_vowels = -1
count_vowels = 0
empty_list = []
for name in names:
    for letter in name:
        if letter in vowels:
            count_vowels += 1
    
    print(name)
print(empty_list)
# Счетчик_макс_гласных

# Список_для_хранения_имен_с_максимальным_кол-вом_гласных
# Счетчик
# Сначала посчитаем количество гласных в имени
# Сравнить количество гласных с максимальным


# nums = [10, 6, 56, 23, 7, 2]
# mx_num = -1
#
# for n in nums:
#     if n > mx_num:
#         mx_num = n
# print(mx_num)
# print(max(nums))
