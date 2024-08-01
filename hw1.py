import csv

def copy_rows(input_file, output_file, row_numbers):
    with open(input_file, mode='r', newline='', encoding='utf-8') as infile:
        reader = csv.reader(infile)
        rows_to_copy = [row for i, row in enumerate(reader) if i in row_numbers]

    with open(output_file, mode='w', newline='', encoding='utf-8') as outfile:
        writer = csv.writer(outfile)
        writer.writerows(rows_to_copy)


def main():
    input_csv = input("Введите имя файлы откуда произвести копирование:")+".csv"
    output_csv = input("Введите название куда вставить скопированные данные")+".csv"
    input_rows = input("Введите номера строк через пробел:")
    rows = list(map(int, input_rows.split()))
    copy_rows(input_csv, output_csv, rows)

main()