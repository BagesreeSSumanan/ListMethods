# 1.Iterate both lists simultaneously use zip method.
list1 = [10, 20, 30, 40]
list2 = [50, 60, 70, 80]
for a, b in zip(list1, list2):
    print(a, b)

# 2.Replace list’s item Python with .Net in the following list
languages = ['Java', 'Python', 'JavaScript']
languages[1] = ".Net"
print(languages)