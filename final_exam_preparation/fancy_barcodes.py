import re

pattern = r"[@{1}][#]+([A-Z]{1}[A-Za-z0-9]{4,}[A-Z]{1})[@{1}][#]+"

pattern_for_nums = r"(\d+)"
number_of_barcodes = int(input())

for barcodes in range(number_of_barcodes):
    barcode = input()

    is_valid = re.findall(pattern,barcode)
    if is_valid:
        group_barcode = re.findall(pattern_for_nums,barcode)
        if len(group_barcode) == 0:
            print(f"Product group: 00")
        else:
            print(f"Product group: {''.join(group_barcode)}")
    else:
        print("Invalid barcode")