Project Overview
WriteAble is a modular Python‑based document analysis tool designed to evaluate grammar, readability, and accessibility while providing educational explanations and rewrite suggestions. The system is built using a clean, isolated module structure to support team development, maintainability, and clarity.

1. File Structure
Code
/writeable
    extraction.py
    grammar.py
    readability.py
    accessibility.py
    explanations.py
    pipeline.py
    ui.py

Global Coding Rules
•	Use module prefixes to avoid naming collisions.
•	Use simple docstrings — one sentence per function.
•	All modules return the same issue dictionary format.
•	Keep code simple — use libraries where possible.
•	No cross‑editing — each developer edits only their assigned module.
•	Python 3.11 .....TBA
•	Follow accessibility standards (WCAG 2.1 AA, ADA Section 508).

3. Required Header in Every File
Code
# Module: [Module Name]
# Person: [Name Here]
# Date Started: Jan __, 2026
# Python Version: 3.11
# Description: [Brief description of module purpose]

4. Accessibility Compliance Summary 
4.1 Standards
•	WCAG 2.1 AA https://www.w3.org/WAI/WCAG22/quickref/?showtechniques=141#distinguishable

•	ADA Section 508 https://www.ada.gov/resources/2024-03-08-web-rule/

•	Federal ICT Standards https://www.section508.gov/manage/playbooks/technology-accessibility-playbook/

•	Plain Language Act https://www.dni.gov/index.php/plain-language-act
4.2 Color Palette (WCAG‑Verified) 
Purpose	Color	Hex
Background	Soft Off‑White	#F7F7F7
Primary Text	Near‑Black	#1A1A1A
Primary Accent	Deep Blue	#1E4D8B
Secondary Accent	Teal	#0E7C86
Error	Dark Red	#8B1E1E
Success	Deep Green	#1E8B4D
Panels	White	#FFFFFF
Borders	Light Gray	#D9D9D9
All colors meet 4.5:1 contrast ratio minimum.
Other palettes available https://venngage.com/tools/accessible-color-palette-generator

4.3 Typography
•	Font: Segoe UI, Arial, Helvetica, sans‑serif
•	Body text: 16px minimum
•	Headers: 20–32px
•	Line spacing: 1.4–1.6
4.4 Keyboard & ARIA
•	Full keyboard navigation
•	Visible focus indicators
•	ARIA labels for icon buttons
•	Semantic HTML required
5. Module Reference Documents
Each module below includes:
•	Description
•	Class name
•	File name
•	Prefix
•	Variables
•	Constants
•	Functions
•	Dependencies
•	Test cases
•	Documentation rules


MODULE A — Document Upload & Text Extraction

Description / Purpose
Handles file upload, validation, and text extraction from TXT, DOCX, and PDF files. Must run before all other modules.
Class Name
Extractor
File Name
extraction.py
Prefix
ext_
Variables
   ext_file
•	ext_text
•	ext_type
•	ext_issues
•	ext_message
Constants
•	EXT_SUPPORTED_TYPES = [".txt", ".docx", ".pdf"]
•	EXT_MAX_FILE_SIZE_MB = 10
Functions
Function	Input	Output	Description
ext_upload_file(file_path)	file path	file object	Loads file into memory
ext_extract_text()	none	string	Extracts text based on file type
ext_read_txt()	file	string	Reads plain text
ext_read_docx()	file	string	Extracts DOCX text
ext_read_pdf()	file	string	Extracts PDF text
Dependencies
None — must run first.
Test Cases
1.	Upload valid TXT file → PASS: text extracted
2.	Upload unsupported file → FAIL: error returned
3.	Upload oversized file → FAIL: size warning



MODULE B — Grammar & Spelling Checker
Description / Purpose
Detects grammar and spelling issues using NLP libraries.
Class Name
GramChecker
File Name
grammar.py
Prefix
gram_
Variables
•	gram_text
•	gram_tool
•	gram_matches
•	gram_issue
•	gram_issues
•	gram_message
Constants
•	GRAM_LANGUAGE = "en-US"
•	GRAM_MAX_SENTENCE_LENGTH = 120
•	GRAM_TOOL_CONFIG = {}
Functions
Function	Input	Output
gram_check(text)	string	dict of issues
gram_find_errors(text)	string	list of matches
gram_format_issue(match)	match object	issue dict
Dependencies
Runs after Extraction.
Test Cases
1.	Detect misspelled word → PASS
2.	Detect long sentence → PASS
3.	Empty text → return empty list




MODULE C — Readability & Clarity Checker
Description / Purpose
Calculates readability scores and identifies long or dense sentences.
Class Name
ReadabilityChecker
File Name
readability.py
Prefix
read_
Variables
•	read_text
•	read_score_value
•	read_sentences
•	read_long_sentences
•	read_issue
•	read_issues
•	read_message
Constants
•	READ_LONG_SENTENCE_THRESHOLD = 25
•	READ_DENSITY_THRESHOLD = 0.6
Functions
Function	Input	Output
read_check(text)	string	dict
read_score(text)	string	float
read_find_long_sentences(text)	string	list
Dependencies
Runs after Grammar.
Test Cases
1.	Long sentence detected → PASS
2.	Readability score returned → PASS
3.	Empty text → empty issues



MODULE D — Accessibility Checker
Description / Purpose
Checks headings, inclusive language, and color contrast.
Class Name
AccessibilityChecker
File Name
accessibility.py
Prefix
acc_
Variables
•	acc_text
•	acc_headings
•	acc_alt_flags
•	acc_contrast
•	acc_issue
•	acc_issues
•	acc_message
Constants
•	ACC_MIN_CONTRAST_RATIO = 4.5
•	ACC_HEADING_LEVELS = [1,2,3,4,5,6]
•	ACC_ALT_TEXT_REQUIRED = True
Functions
Function	Input	Output
acc_check(text)	string	dict
acc_check_headings(text)	string	list
acc_check_alt_text(text)	string	list
acc_check_contrast(text)	string	list
Dependencies
Runs after Readability.
Test Cases
1.	Missing headings → PASS
2.	Non‑inclusive language → PASS
3.	Low contrast → PASS






MODULE E — Explanations + AI Rewrite
Description / Purpose
Adds educational explanations and optional rewrite suggestions.
Class Name
ExplanationEngine
File Name
explanations.py
Prefix
exp_
Variables
•	exp_issues
•	exp_explanations
•	exp_ai_response
•	exp_prompt
•	exp_message
Constants
•	EXP_API_TIMEOUT = 10
•	EXP_MAX_PROMPT_LENGTH = 512
•	EXP_DEFAULT_TONE = "educational"
Functions
Function	Input	Output
exp_add_explanations(issues)	list	list
exp_rewrite(text)	string	string
exp_generate_prompt(issue)	dict	string
Dependencies
Runs after Accessibility.
Test Cases
1.	Explanation added → PASS
2.	Rewrite returned → PASS
3.	API timeout → FAIL gracefully





MODULE F — Pipeline Manager
Description / Purpose
Controls module execution order and merges all issues.
Class Name
PipelineManager
File Name
pipeline.py
Prefix
pipe_
Variables
•	pipe_text
•	pipe_all_issues
•	pipe_extraction
•	pipe_grammar
•	pipe_readability
•	pipe_accessibility
•	pipe_explained
•	pipe_result
Constants
•	PIPE_MODULE_ORDER = ["EXTRACTION", "GRAMMAR", "READABILITY", "ACCESSIBILITY", "EXPLANATIONS"]
•	PIPE_OUTPUT_KEY = "issues"
Functions
Function	Input	Output
pipe_run(text)	string	dict
pipe_merge(issues_list)	list	dict
pipe_order(issues)	dict	dict
Dependencies
Imports Modules A–E.
Test Cases
1.	Full pipeline returns issues → PASS
2.	Missing module → FAIL gracefully
3.	Empty text → empty output








MODULE G — Streamlit UI
Description / Purpose
Provides user interface for uploading documents, viewing results, and interacting with rewrite suggestions.
Class Name
UIController
File Name
ui.py
Prefix
ui_
Variables
•	ui_text_input
•	ui_uploaded_file
•	ui_results
•	ui_display_block
•	ui_rewrite_text
Constants
•	UI_PAGE_TITLE = "WriteAble Document Analyzer"
•	UI_MAX_DISPLAY_LINES = 50
Functions
Function	Input	Output
ui_main()	none	UI
ui_display_results(results)	dict	UI
ui_upload_file()	file	string
Dependencies
Runs after Pipeline Manager.
Test Cases
1.	Upload file → PASS
2.	Display results → PASS
3.	Rewrite suggestion accepted → PASS
6. Pipeline Order (Required)
1.	Module A — Extraction
2.	Module B — Grammar
3.	Module C — Readability
4.	Module D — Accessibility
5.	Module E — Explanations
6.	Module F — Pipeline Manager
7.	Module G — UI
Pipeline Output Format
Code
{"issues": all_issues}


