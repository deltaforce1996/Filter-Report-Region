import csv
from tqdm import tqdm

path = 'D:\Filter-Report-Region\outputs'

with open('ข้อมูลยอดขาย.csv', 'r',  encoding='utf-8') as file:
    reader = csv.reader(file)
    subObj = {}

    for row in tqdm(reader, desc='Reading CSV file', total=2264, colour='green'):
        if row[3] not in subObj:
            subObj[row[3]] = []
        subObj[row[3]].append(row)

        header_group = subObj.keys()

for index, item in enumerate(header_group):
    if index != 0:
        file_name = f'{item}.csv'

        # print(file_name)
        # print(subObj['BPRegion'][0])
        # print(subObj[item])

        with open(f'{path}\{file_name}', 'w', newline='', encoding='utf-8') as csv_file:

            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(subObj['BPRegion'][0])

            for region in tqdm(enumerate(subObj[item]), desc=f'Writing CSV', total=len(subObj[item])):
                csv_writer.writerow(region)
