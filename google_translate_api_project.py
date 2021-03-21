from google_trans_new import google_translator

file = open("first.txt", "r")
second_file = open("second.txt", "a")

myStr = ""
for line in file:
    myStr += line[:-1] + " "

myStr = myStr[:-1]

file.seek(0, 2)
file.seek(file.tell()-1, 0)
last_char = file.read()

myStr += last_char

translator = google_translator()
translate_text = translator.translate(myStr, lang_tgt='tr')
counter = 20

count_for_space = 0
for i in translate_text:
    if count_for_space == 15:
        second_file.write("\n")
        count_for_space = 0
    if i == " ":
        count_for_space += 1
    second_file.write(i)

file.close()
second_file.close()
