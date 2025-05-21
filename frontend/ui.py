from typing import Tuple
from backend import process
import gradio as gr


def lsnr_generate_brochure(
    company_name: gr.Textbox, company_url: gr.Textbox
) -> Tuple[gr.Markdown, gr.Button]:
    brochure = process.generate_brochure(company_name, company_url)
    mkdn_output = gr.Markdown(value=brochure, show_copy_button=True)
    btn_download = gr.DownloadButton(
        label="Download Brochure",
        value=process.BROCHURE_PDF_FILE,
        icon="frontend/download.png",
        visible=True,
    )
    return mkdn_output, btn_download


def lsnr_clear_output() -> gr.Markdown:
    mkdn_output = gr.Markdown(value="", show_copy_button=False, min_height=100)
    btn_download = gr.DownloadButton(visible=False)
    return mkdn_output, btn_download


# ui component definition
mkdn_output = gr.Markdown(value="", min_height=100)
tbox_url = gr.Textbox(label="Website URL:")
tbox_cname = gr.Textbox(label="Company Name:")
btn_submit = gr.Button(value="Generate Brochure", icon="frontend/gears.png")
btn_download = gr.DownloadButton(
    label="Download Brochure", icon="frontend/download.png", visible=False
)
btn_clear = gr.ClearButton(
    components=[mkdn_output, tbox_url, tbox_cname],
    value="Clear Output",
    icon="frontend/clear.png",
)

with gr.Blocks() as demo:
    mkdn_output.render()
    with gr.Sidebar():
        tbox_cname.render()
        tbox_url.render()
        btn_submit.render()
        btn_clear.render()
        btn_download.render()

        # event handlers
        btn_submit.click(
            fn=lsnr_generate_brochure,
            inputs=[tbox_cname, tbox_url],
            outputs=[mkdn_output, btn_download],
        )
        btn_clear.click(
            fn=lsnr_clear_output,
            inputs=None,
            outputs=[mkdn_output, btn_download],
        )
