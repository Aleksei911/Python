import csv

with open('example.csv', encoding='UTF-8') as csv_file:
    exampleReader = csv.reader(csv_file, delimiter=';')
    for row in exampleReader:
        string = 'Строка #' + str(exampleReader.line_num) + ' '
        for value in row:
            string += value + ' '
        print(string)


####################################################################


exampleFile = open('output.csv', 'w', encoding='UTF-8', newline='')
exampleWriter = csv.writer(exampleFile, delimiter=';')
exampleData = [['05.04.2015 13:34;Яблоки;73'],
               ['05.04.2015 3:41;Вишни;85'],
               ['05.04.2015 12:46;Груши;14']]
for row in exampleData:
    exampleWriter.writerow(row)
exampleFile.close()