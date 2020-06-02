#!/user/bin/python
# _*_ coding:utf-8 _*_
__author__ = "super.gyk"
from PyPDF2 import PdfFileReader, PdfFileWriter

"""
readFile = open('example.pdf', 'rb')

# 获取 PdfFileReader 对象
pdfFileReader = PdfFileReader(readFile)

# 获取 PDF 文件的文档信息
documentInfo = pdfFileReader.getDocumentInfo()
print('documentInfo = %s' % documentInfo)

# 获取页面布局
pageLayout = pdfFileReader.getPageLayout()
print('pageLayout = %s ' % pageLayout)

# 获取页模式
pageMode = pdfFileReader.getPageMode()
print('pageMode = %s' % pageMode)

# 从 PDF 文档根目录中检索 XMP 数据
xmpMetadata = pdfFileReader.getXmpMetadata()
print('xmpMetadata  = %s ' % xmpMetadata)

# 获取 pdf 文件页数
pageNum = pdfFileReader.getNumPages()
print('pageNum = %s' % pageNum)

for index in range(0, pageNum):
    # 返回指定页编号的 pageObject
    pageObj = pdfFileReader.getPage(index)
    # <class 'PyPDF2.pdf.PageObject'>
    print('index = %d , pageObj = %s' % (index, type(pageObj)))
    # 获取 pageObject 在 PDF 文档中处于的页码
    pageNumber = pdfFileReader.getPageNumber(pageObj)
    print('pageNumber = %s ' % pageNumber)
"""


# 写入文档
def add_blank_page():
    read_file = open('example.pdf', 'rb')
    out_file = 'example_copy.pdf'
    pdf_file_writer = PdfFileWriter()

    # 获取 PdfFileReader 对象
    pdf_file_reader = PdfFileReader(read_file)
    num_pages = pdf_file_reader.getNumPages()

    for i in range(0, num_pages):
        page_obj = pdf_file_reader.getPage(i)
        # 根据每页返回的 PageObject,写入到文件
        pdf_file_writer.addPage(page_obj)
        pdf_file_writer.write(open(out_file, 'wb'))

    # 在文件的最后一页写入一个空白页,保存至文件中
    pdf_file_writer.addBlankPage()
    pdf_file_writer.write(open(out_file, 'wb'))


# 分割文档
def split_pdf():
    read_file = open('example.pdf', 'rb')
    out_file = 'example_copy.pdf'
    pdf_file_writer = PdfFileWriter()

    # 获取 PdfFileReader 对象
    pdf_file_reader = PdfFileReader(read_file)
    # 文档总页数
    num_pages = pdf_file_reader.getNumPages()

    if num_pages > 5:
        # 从第五页之后的页面，输出到一个新的文件中，即分割文档
        for index in range(5, num_pages):
            page_obj = pdf_file_reader.getPage(index)
            pdf_file_writer.addPage(page_obj)
        # 添加完每页，再一起保存至文件中
        pdf_file_writer.write(open(out_file, 'wb'))


# 合并文件
def merge_pdf(in_file_list, out_file):
    """
    :param in_file_list: 要合并的文档列表
    :param out_file: 输出文件
    :return:
    """

    pdf_file_writer = PdfFileWriter()
    for in_file in in_file_list:
        # 依次循环打开要合并文件
        pdf_reader = PdfFileReader(open(in_file, 'rb'))
        num_pages = pdf_reader.getNumPages()
        for index in range(0, num_pages):
            page_obj = pdf_reader.getPage(index)
            pdf_file_writer.addPage(page_obj)

        # 最后,统一写入到输出文件中
        pdf_file_writer.write(open(out_file, 'wb'))


# 粗略读取PDF文件内容
def get_pdf_content(filename):
    pdf = PdfFileReader(open(filename, "rb"))
    num = pdf.getNumPages()
    content = ""
    for i in range(0, num):
        page_obj = pdf.getPage(i)

        extracted_text = page_obj.extractText()
        content += extracted_text + "\n"
        # return content.encode("ascii", "ignore")
    # print(content.encode("ascii", "ignore"))
    return content


get_pdf_content("example.pdf")

# 注：当我试图获取PDF文件的内容时，却获取到了null，这个玩意获取PDF内容还是不怎么可靠的
