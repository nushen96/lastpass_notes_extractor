import os
import sys
import csv

# The csv file extracted from lastpass
csv_file_path = os.path.join(sys.path[0], 'lastpass_export.csv')
data = []
with open(csv_file_path) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for index,row in enumerate(csv_reader):
        row_dict = {}
        if row[0] == "http://sn":
            row_dict["title"] = row[-3]
            row_dict["content"] = row[4]
            data.append(row_dict)

for note in data:
    f = open(os.path.join(sys.path[0],'extracted_notes',f"{note['title']}.txt"), 'w')
    # Notes takes the first line as a title by default
    f.write(f"{note['title']}\n")
    f.write("----------------------------------------\n\n")
    f.writelines(note["content"])
    f.close()
print(f"{len(data)} notes succesfully extracted!")