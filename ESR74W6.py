
# 1
s = input()  
s1, s2 = s.split()  
new_s = s2 + " " + s1  
print(new_s)



# 2

string = input() 
first_index = string.find('f')  
last_index = string.rfind('f')  

if first_index == -1:
    pass
elif first_index == last_index:
    
    print(first_index)
else:
    
    print(first_index, last_index)

# 3

string = input()  

first_index = string.find('f')  

if first_index == -1:  
    second_index = -2
elif first_index == len(string) - 1:  
    second_index = -1
else:
    second_index = string.find('f', first_index + 1)  

print(second_index)  

#Задача G4
def remove_between_h(string):
    # Найти первое вхождение буквы "h"
    first_h = string.index('h')
    # Найти последнее вхождение буквы "h"
    last_h = string.rindex('h')
    # Получить подстроку до первого вхождения "h"
    substring1 = string[:first_h]
    # Получить подстроку после последнего вхождения "h"
    substring2 = string[last_h + 1:]
    # Соединить подстроки
    result = substring1 + substring2
    
    return result

string = input("Введите строку: ")
result = remove_between_h(string)
print("Результат:", result)

