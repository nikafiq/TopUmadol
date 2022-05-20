from main import text
import csv

#splitting number, listing them
x = [int(s) for s in text.split() if s.isdigit()]

print(x)

#with open('test.csv', 'w', encoding='UTF-8') as f:
#    writer = csv.writer(f)
#    writer.writerow(s)

def text_splitter(member, fan_count):
    global member, fan_count

    def csv_input(member, fan_count):
