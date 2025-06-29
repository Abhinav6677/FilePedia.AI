# FilePedia 2.0

A Streamlit-based document processing and Q&A application that allows users to upload PDF files and interact with them through various features.

## Features

- **Document Upload**: Upload PDF files for processing
- **Document Summary**: Generate summaries of uploaded documents
- **Q&A System**: Ask questions about the document content
- **Challenge Mode**: Interactive challenges based on document content

## Installation

1. Clone the repository:
```bash
git clone <your-repository-url>
cd FilePedia-2.0
```

2. Install dependencies:
```bash
pip install -r requirement.txt
```

3. Run the application:
```bash
streamlit run filepedia.py
```

## Project Structure

```
FilePedia 2.0/
├── app/
│   ├── challenge.py    # Challenge mode functionality
│   ├── qa.py          # Q&A system
│   ├── summary.py     # Document summarization
│   └── utils.py       # Utility functions
├── filepedia.py       # Main Streamlit application
├── requirement.txt    # Python dependencies
└── README.md         # This file
```

## Usage

1. Open the application in your browser (usually at http://localhost:8501)
2. Upload a PDF document
3. Choose from the available features:
   - Generate a summary
   - Ask questions about the document
   - Try the challenge mode

## Requirements

- Python 3.8+
- Streamlit
- PyMuPDF
- Other dependencies listed in `requirement.txt`

## License

[Add your license information here] 