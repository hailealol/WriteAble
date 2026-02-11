"""
WriteAble UI Preview (Standalone Version)
-----------------------------------------
This file is a self-contained preview of the WriteAble interface.
It is NOT connected to the real PipelineManager or backend logic.

Purpose:
- Preview the professional UI layout
- Verify logo placement
- Test the two-column input layout
- Show how results will appear in expanders

How to run:
1. Place 'logo.png' in the same folder as this file
2. Run:  streamlit run ui_preview.py
"""

import streamlit as st

UI_PAGE_TITLE = "WriteAble Document Analyzer"

class UIController:
    """Standalone UI preview without pipeline dependency."""

    def __init__(self):
        self.ui_text_input = ""
        self.ui_uploaded_file = None
        self.ui_results = None

    def ui_main(self):
        st.set_page_config(page_title=UI_PAGE_TITLE, layout="wide")

        # --- Header with logo + title ---
        self._ui_header()

        st.markdown(
            "<div style='font-size:18px; margin-bottom:20px;'>"
            "Upload a document or paste text below to analyze it."
            "</div>",
            unsafe_allow_html=True
        )

        # --- Input Section ---
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

        # --- Analyze Button ---
        if st.button("Analyze", use_container_width=True):
            # Fake results for preview purposes
            self.ui_results = {
                "grammar": ["Missing comma in sentence 2", "Possible run-on sentence"],
                "clarity": [],
                "tone": ["Sentence 4 may sound overly formal"]
            }

        # --- Results Section ---
        if self.ui_results:
            self.ui_display_results(self.ui_results)

    # ---------------------------------------------------------
    # Header with Logo + Title
    # ---------------------------------------------------------
    def _ui_header(self):
        col_logo, col_title = st.columns([1, 4])

        with col_logo:
            st.image("logo.png", width=140)

        with col_title:
            st.markdown(
                f"<h1 style='margin-top:10px;'>{UI_PAGE_TITLE}</h1>",
                unsafe_allow_html=True
            )

    # ---------------------------------------------------------
    # File Upload
    # ---------------------------------------------------------
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
                return "PDF uploaded (text extraction not implemented yet)."

            if uploaded.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
                return "DOCX uploaded (text extraction not implemented yet)."

        except Exception:
            st.error("Unable to read file.")
            return None

        return None

    # ---------------------------------------------------------
    # Results Display
    # ---------------------------------------------------------
    def ui_display_results(self, results: dict):
        st.subheader("Analysis Results")
        st.markdown("Review the findings from your document analysis below.")

        for section, issues in results.items():
            with st.expander(section.capitalize(), expanded=False):
                if not issues:
                    st.info("No issues found.")
                else:
                    for issue in issues:
                        st.write(f"- {issue}")


# ---------------------------------------------------------
# Run the UI
# ---------------------------------------------------------
if __name__ == "__main__":
    ui = UIController()
    ui.ui_main()

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
                return "PDF uploaded (text extraction not implemented yet)."

            if uploaded.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
                return "DOCX uploaded (text extraction not implemented yet)."

        except Exception:
            st.error("Unable to read file.")
            return None

        return None

    # ---------------------------------------------------------
    # Results Display
    # ---------------------------------------------------------
    def ui_display_results(self, results: dict):
        st.subheader("Analysis Results")
        st.markdown("Review the findings from your document analysis below.")

        for section, issues in results.items():
            with st.expander(section.capitalize(), expanded=False):
                if not issues:
                    st.info("No issues found.")
                else:
                    for issue in issues:
                        st.write(f"- {issue}")


# ---------------------------------------------------------
# Run the UI
# ---------------------------------------------------------
if __name__ == "__main__":
    ui = UIController()
    ui.ui_main()
