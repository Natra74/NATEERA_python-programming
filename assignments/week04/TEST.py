#รับข้อมูล "ชื่อจริง เป็นภาษาอังกฤษ"จากผู้ใช้
#นับจำนวนสระในข้อความดังกล่าว

#ตัวอย่างหน้าจอโปรแกรม
#what is your name : Nateera
#You have 4 vowels in your text.

ืname = input("what is you name : ")
letters = list(name)
counter = 0

for char in letters :
    if char == 'a' or char == 'A' :
        counter + 1
    
    elif char == 'e' or char == 'E' :
        counter + 1

     elif char == 'i' or char == 'I' :
        counter + 1

     elif char == 'o' or char == 'O' :
        counter + 1

     elif char == 'u' or char == 'U' :
        counter + 1

print("You have",counter,"vowel in you text.")