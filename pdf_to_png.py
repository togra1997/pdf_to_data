from pathlib import Path

import fitz


def pdf_2_png(filepath: Path):
    """
    PDFをpngに変換
    """

    pdf = fitz.open(filepath)
    for i, page in enumerate(pdf):
        pix = page.get_pixmap(dpi=600)
        pix.save(Path("./page/test.png"))


if __name__ == "__main__":
    path = Path("./モビリタ_20240821/小田切.pdf")
    pdf_2_png(path)
