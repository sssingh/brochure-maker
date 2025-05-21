"""Generic utility/helper functions"""

from spire.doc import Document, FileFormat
from spire.doc.common import *  # noqa: F403


def save_md_as_pdf(md_path: str, pdf_path: str):
    """Convert markdown formatted text into PDF doc and save as PDF file.

    Args:
        md_contents (str): markdown format text.
        file_name (str, optional): The PDF file name. Defaults to "report.pdf".
        title (str, optional): title of PDF doc. Defaults to "".
    """
    # pdf = MarkdownPdf()
    # pdf.meta["title"] = title
    # pdf.add_section(Section(md_contents, toc=True))
    # pdf.save(file_path)

    # Create a Document object
    document = Document()
    # Load a Markdown file
    document.LoadFromFile(md_path)
    # Save it as a pdf file
    document.SaveToFile(pdf_path, FileFormat.PDF)
    # Dispose resources
    document.Dispose()
