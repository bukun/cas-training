#!/usr/bin/env python
# coding: utf-8

# # 实例：用HTML作为排版工具
#
#
# ## 场景描述
#
# 有一组图片， 每张图片有一段描述文字（可放到 XLSX 中）， 以及长宽等属性，将图片及相关信息放到一起生成文档，以方便打印。
#
# 解决思路：相关信息生成 HTML ， 后面可用 Word 排版、输出。
#

# ## 解决方法

# **用Jinja2加载模板文件(html_base.html)：**

# In[8]:


from jinja2 import FileSystemLoader,Environment
env = Environment(loader=FileSystemLoader('templates'))
template = env.get_template('html_base.html')


# **openpyxl**模块是一个读写Excel文档的Python库
#
# 创建Workbook对象：用openpyxl模块的load_workbook函数进行读取excel文档
#

# In[9]:


import openpyxl
wb = openpyxl.load_workbook('imgs/img_contents.xlsx')


# 获取当前活跃的Worksheet

# In[10]:


sheet = wb.active


# 对sheet进行遍历获取相应的内容，并赋值给变量html_str

# In[112]:


html_str=''
for i in range(2, sheet.max_row + 1):
    img_title = sheet.cell(row=i, column=1).value
    img_misc = sheet.cell(row=i, column=2).value
    img_length = sheet.cell(row=i, column=3).value
    img_width = sheet.cell(row=i, column=4).value

    if img_title:
        pass
    else:
        continue

    html_content = '<div class="thumb"><img src="imgs/' + img_title + '"'+ ' width=' + str(img_width) + ' height=' + str(img_length) + '/> ' + img_misc + ' </div>'
    html_str += html_content


# 对模板进行渲染，将变量html_str赋值给html_base.html中的变量content

# In[27]:


template.render(content=html_str)


with open('xx_html.html', 'w') as fo:
    fo.write(template.render(content=html_str))




import requests
from bs4 import BeautifulSoup
import os
import docx
from docx import Document
from docx.shared import Inches


# 解析页面

# In[128]:


url = 'http://drr.ikcest.org/'
html = requests.get(url).content
soup = BeautifulSoup(html,'html.parser')
imgs_table = soup.find('table',{"class":"table"})
img=str(imgs_table.find('div',{"class":"col-sm-4"})).split('src="')[1].split('"')[0]
img_src='http://drr.ikcest.org'+img
img_title=imgs_table.find('div',{"class":"col-sm-8"}).text
img


# 保存图片至本地

# In[119]:


img_name = './imgs/tornado_1.jpg'

with open(img_name,'wb')as f:
    response = requests.get(img_src).content
    f.write(response)
    f.close()


# 创建document对象，并向文档中添加文字，图片

# In[120]:


document = Document()
document.add_paragraph(img_title)
document.add_picture(img_name)


# 保存文档

# In[121]:


document.save('xx_result.docx')


# 删除保存在本地的图片

# In[122]:


os.remove(img_name)


# 详细排版可了解python-doc进行进一步操作
