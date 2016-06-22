import xlsxwriter


def write_document(filepath, results):
    workbook = xlsxwriter.Workbook(filepath)
    worksheet = workbook.add_worksheet()

    c = 0
    r = 0

    for result in results:
        c = 0
        for column in result:
            worksheet.write(r, c, column)
            c += 1
        r += 1

    workbook.close()
