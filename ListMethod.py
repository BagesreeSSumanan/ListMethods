# 1.Iterate both lists simultaneously use zip method.
list1 = [10, 20, 30, 40]
list2 = [50, 60, 70, 80]
for a, b in zip(list1, list2):
    print(a, b)

# 2.Replace list’s item Python with .Net in the following list
languages = ['Java', 'Python', 'JavaScript']
index = languages.index("Python")
languages[index] = ".Net"
print(languages)

# 3.Remove all occurrences of a specific item from a list.
languages = ['Java', 'Python', 'JavaScript','Python']
languages = [lang for lang in languages if lang != "Python"]
print(languages)

# 4.Given a nested list ['a', ['bb', 'cc'], 'd']Insert item ‘dd’ to the second sublist’s first position so that resulting list will be['a', [‘dd’,'bb', 'cc'], 'd']
nested_list = ['a', ['bb', 'cc'], 'd']
nested_list[1].insert(0, 'dd')
print(nested_list)

# 5.Iterate through the following nested list using for loop and and print the elements
L = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]
for item in L:
    for value in item:
        print(value)


# 6.Given a list [10,23,40,[9,3,4],6,7].Print the first 2 elements of sublist at position 3
Newlist = [10,23,40,[9,3,4],6,7]
Newlist = Newlist[3][:2]
Newlist=Newlist[:2]
print(Newlist)

#7.There are 5 students in this class whose names and grades are assembled to build the following list, list the name and grade 
Input = [['rishav', 10], ['akash', 50], ['ram', 80], ['gaurav', 85],['Akhil', 58]]
for student in Input:
    print("Name:", student[0], "Grade:", student[1])