import re
"""
При помощи регулярки пробегаемся по тексту и находим email адреса. затем выводим их в терминал
"""

text = """Иван Иванович!
Нужен ответ на письмо от ivanoff@ivan-chai.ru.
Не забудьте поставить в копию
sergeo-lupin@mail.ru- это важно.
"""

pattern = r"[\w\-]+@[\w\-]+\.[\w]{2,3}"
result = re.findall(pattern, text)

for email in result:
    print(email)

