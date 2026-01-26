# Module: UI
# Person: Julie Phillips
# Date Started: Jan 25 2026
# Python Version: 3.11
# Description: Provides Streamlit interface for document analysis.

import streamlit as st
from pipeline import PipelineManager

UI_PAGE_TITLE = "WriteAble Document Analyzer"
UI_MAX_DISPLAY_LINES = 50

class UIController:
    """Controls the Streamlit user interface."""

    def __init__(self):
        self.ui_text_input = ""
        self.ui_uploaded_file = None
        self.ui_results = None
        self.ui_display_block = None
        self.ui_rewrite_text = ""

    def ui_main(self):
        """Renders the main UI layout."""
        st.set_page_config(page_title=UI_PAGE_TITLE, layout="wide")
        st.title(UI_PAGE_TITLE)

        st.markdown("Upload a document or paste text below to analyze it.")

        col1, col2 = st.columns(2)

        with col1:
            self.ui_uploaded_file = self.ui_upload_file()

        with col2:
            self.ui_text_input = st.text_area(
                "Or paste text:",
                height=250,
                placeholder="Paste text here..."
            )

        if st.button("Analyze"):
            self._ui_run_pipeline()

        if self.ui_results:
            self.ui_display_results(self.ui_results)

    def ui_upload_file(self):
        """Handles file upload and returns text."""
        uploaded = st.file_uploader(
            "Upload a document",
            type=["txt", "md", "pdf", "docx"]
        )

        if not uploaded:
            return None

        try:
            # Basic text formats
            if uploaded.type in ["text/plain", "text/markdown"]:
                return uploaded.read().decode("utf-8", errors="ignore")

            # PDF fallback
            if uploaded.type == "application/pdf":
                return "PDF uploaded (text extraction not implemented yet)."

            # DOCX fallback
            if uploaded.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
                return "DOCX uploaded (text extraction not implemented yet)."

        except Exception:
            st.error("Unable to read file.")
            return None

        return None

    def ui_display_results(self, results: dict):
        """Displays analysis results."""
        st.subheader("Analysis Results")

        for section, issues in results.items():
            with st.expander(section.capitalize(), expanded=False):
                if not issues:
                    st.info("No issues found.")
                else:
                    for issue in issues:
                        st.write(issue)

    def _ui_run_pipeline(self):
        """Runs the pipeline and stores results."""
        text = self.ui_uploaded_file or self.ui_text_input

        if not text:
            st.error("Please upload a file or enter text.")
            return

        pipeline = PipelineManager()
        self.ui_results = pipeline.run(text)
