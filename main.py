from pyhanko.pdf_utils.incremental_writer import IncrementalPdfFileWriter
from pyhanko.pdf_utils.images import PdfImage
from pyhanko.pdf_utils.layout import BoxConstraints
from pyhanko.stamp import StaticStampStyle


def add_signature():
    # 打开源文件和输出文件
    with open("doc.pdf", "rb") as doc, open("doc1.pdf", "wb") as output:
        # 创建一个writer对象，一次性写入的话可能不必用这个类
        w = IncrementalPdfFileWriter(doc)
        # 从路径读取一张图片，也可以直接用Image对象，具体看源码
        signature = PdfImage("signature.png")
        # 适用于将图片单独渲染的签章样式
        stampStyle = StaticStampStyle(background=signature, border_width=0)
        # 必须且只能指定宽、高、比率中的两个值
        sizeBox = BoxConstraints(height=50, width=150)
        # 创建签章 - 构造函数要求，必须要写命名参数 text_params
        stamp = stampStyle.create_stamp(w, sizeBox, text_params=None)
        # 将签章写入指定页的指定位置
        stamp.apply(0, 0, 0)
        w.write(output)


if __name__ == "__main__":
    add_signature()
