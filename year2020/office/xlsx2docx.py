from openpyxl import load_workbook
from docx import Document

word = Document('./demo_tmpl/d_mod.docx')
table1 = word.add_table(10, 7)
# word.save('./demo_tmpl/d_mod.docx')


excel = load_workbook('./demo_tmpl/e_mod.xlsx')
ws = excel.active
sheet = excel.get_sheet_by_name('Sheet1')

for i in range(0, 10):
    table1.cell(i, 0).text = str(ws.cell(row=(i + 1), column=1).value)
    table1.cell(i, 1).text = str(ws.cell(row=(i + 1), column=2).value)
    table1.cell(i, 2).text = str(ws.cell(row=(i + 1), column=3).value)
    table1.cell(i, 3).text = str(ws.cell(row=(i + 1), column=4).value)
    table1.cell(i, 4).text = str(ws.cell(row=(i + 1), column=5).value)
    table1.cell(i, 5).text = str(ws.cell(row=(i + 1), column=6).value)
    table1.cell(i, 6).text = str(ws.cell(row=(i + 1), column=7).value)
word.save('./xx_d_mod.docx')

tmpl = Document('./xx_d_mod.docx')
paras = tmpl.paragraphs

for para in paras:
    print(para.text)
    para.text = para.text.replace('{a}', str(ws.cell(row=1, column=2).value))
    para.text = para.text.replace('{b}', str(ws.cell(row=1, column=3).value))
    print(para.text)

for row in range(4, 10):
    pa1 = paras[0]
    pa2 = paras[1]
    pa1.text = pa1.text.replace('{a}', str(ws.cell(row=row, column=2).value))
    pa2.text = pa2.text.replace('{b}', str(ws.cell(row=row, column=4).value))
    tmpl.add_paragraph(pa1.text, pa1.style)
    tmpl.add_paragraph(pa2.text, pa2.style)

tmpl.save('xx_tmpl.docx')
