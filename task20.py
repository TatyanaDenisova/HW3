# *Задача 20: * В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность.
# В случае с английским алфавитом очки распределяются так:A, E, I, O, U, L, N, S, T, R – 1 очко;
# D, G – 2 очка; B, C, M, P – 3 очка; F, H, V, W, Y – 4 очка; K – 5 очков; J, X – 8 очков; Q, Z – 10 очков.
# А русские буквы оцениваются так: А, В, Е, И, Н, О, Р, С, Т – 1 очко; Д, К, Л, М, П, У – 2 очка;
# Б, Г, Ё, Ь, Я – 3 очка; Й, Ы – 4 очка; Ж, З, Х, Ц, Ч – 5 очков; Ш, Э, Ю – 8 очков; Ф, Щ, Ъ – 10 очков.
# Напишите программу, которая вычисляет стоимость введенного пользователем слова. Будем считать,
# что на вход подается только одно слово, которое содержит либо только английские, либо только русские буквы.
# *Пример:*
# ноутбук
#     12

# text = str(input("Введите слово:   ").upper())
# dic_en = {1: "AEIOULNSTR", 2: "DG", 3: "BCMP",
#        4: "FHVWY", 5: "K", 8: "JX", 10: "QZ"}
# dic_ru = {1: "АВЕИНОРСТ", 2: "ДКЛМПУ", 3: "БГЁЬЯ",
#        4: "ЙЫ", 5: "ЖЗХЦЧ", 8: "ШЭЮ", 10: "ФЩЪ"}
# for letter in text:
#     if letter in dic_en.items():
#         print(sum([key for letter in text for key, elem in dic_en.items() if letter in elem]))
#     else:
#         print(sum([key for letter in text for key, elem in dic_ru.items() if letter in elem]))

text = str(input("Введите слово:   ").upper())
dic = {1: "AEIOULNSTRАВЕИНОРСТ", 2: "DGДКЛМПУ", 3: "BCMPБГЁЬЯ",
    4: "FHVWYЙЫ", 5: "KЖЗХЦЧ", 8: "JXШЭЮ", 10: "QZФЩЪ"}
count = 0
for letter in text:
	    for key, elem in dic.items():
	        if letter in elem:
	            count = count + key
print(count)