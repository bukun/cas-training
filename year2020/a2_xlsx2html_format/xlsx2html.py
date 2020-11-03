from openpyxl import load_workbook
wb = load_workbook('防灾减灾数据目录-中英文_20200629.xlsx')
print(wb.get_sheet_names())
str="""
<html>
    <head><meta charset="utf-8">
    <style>
    table{
    min-width:1000px;
    border: 1px seagreen solid;
    }

    table,th,td
    {
    border:1px solid green;
    }
    a{
    text-decoration: none;
    }
    a:link,a:visited,a:active{color:black}
    a:hover{color:green}
    </style>
        </head>
        <body>
        <div>
        <table>
"""
i=0
sheet = wb.get_sheet_by_name('中英文含摘要')



for row in sheet.rows:
    str=str+"""<tr>"""
    if i==0:
        str=str+"""<th>{id}</th>
        <th><a href="{url}" target="_blank">{title}</a></th>
        <th><a href="{url}" target="_blank">{intro}</a></th>
        """.format( id = i if i!=0 else '',
                   title = row[4].value,
                   intro = row[5].value,
                   url = row[1].value)
    else:
        str=str+"""<td>{id}</td>
        <td><a href="{url}" target="_blank">{title}</a></td>
        <td><a href="{url}" target="_blank">{intro}</a></td>
        """.format( id = i if i!=0 else '',
                   title = row[4].value,
                   intro = row[5].value,
                   url = row[1].value)
    str=str+"""</tr>"""
    i=i+1
str=str+"""</table> </div> </body></html>"""
fo = open("防灾减灾数据目录-中英文_20200629.html", "w")
fo.write(str)
fo.close()