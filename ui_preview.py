"""
WriteAble UI Preview (Standalone Version)
-----------------------------------------
Streamlit Cloud Ready Version
"""

import streamlit as st
import os

UI_PAGE_TITLE = "WriteAble Document Analyzer"


class UIController:
    def __init__(self):
        self.ui_text_input = ""
        self.ui_uploaded_file = None
        self.ui_results = None

    def ui_main(self):
        st.set_page_config(page_title=UI_PAGE_TITLE, layout="wide")

        self._ui_header()

        st.markdown(
            "<div style='font-size:18px; margin-bottom:20px;'>"
            "Upload a document or paste text below to analyze it."
            "</div>",
            unsafe_allow_html=True
        )

        col1, col2 = st.columns(2)

        with col1:
            self.ui_uploaded_file = self.ui_upload_file()

        with col2:
            self.ui_text_input = st.text_area(
                "Or paste text:",
                height=250,
                placeholder="Paste text here..."
            )

        st.markdown("---")

        if st.button("Analyze", use_container_width=True):
            self.ui_results = {
                "grammar": ["Missing comma in sentence 2", "Possible run-on sentence"],
                "clarity": [],
                "tone": ["Sentence 4 may sound overly formal"]
            }

        if self.ui_results:
            self.ui_display_results(self.ui_results)

    def _ui_header(self):
        col_logo, col_title = st.columns([1, 4])

        with col_logo:
            logo_path = os.path.join(os.path.dirname(__file__), "WriteAble.png")
            if os.path.exists(logo_path):
                st.image(logo_path, width=140)

        with col_title:
            st.markdown(
                f"<h1 style='margin-top:10px;'>{UI_PAGE_TITLE}</h1>",
                unsafe_allow_html=True
            )

    def ui_upload_file(self):
        uploaded = st.file_uploader(
            "Upload a document",
            type=["txt", "md", "pdf", "docx"]
        )

        if not uploaded:
            return None

        try:
            if uploaded.type in ["text/plain", "text/markdown"]:
                return uploaded.read().decode("utf-8", errors="ignore")

            if uploaded.type == "application/pdf":
                return "PDF uploaded (preview mode)."

            if uploaded.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
                return "DOCX uploaded (preview mode)."

        except Exception:
            st.error("Unable to read file.")
            return None

        return None

    def ui_display_results(self, results: dict):
        st.subheader("Analysis Results")
        st.markdown("Review the findings from your document analysis below.")

        for section, issues in results.items():
            with st.expander(section.capitalize()):
                if not issues:
                    st.info("No issues found.")
                else:
                    for issue in issues:
                        st.write(f"- {issue}")


if __name__ == "__main__":
    ui = UIController()
    ui.ui_main()
