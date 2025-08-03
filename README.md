# 🤖 Agentic Document Extraction

> **Intelligent PDF parsing and data extraction powered by AI**

Extract structured data from PDF documents using advanced AI vision and natural language processing. This project leverages the `agentic-doc` library to intelligently parse documents and extract meaningful information in both markdown and structured JSON formats.

## ✨ Features

- **🔍 Intelligent Document Parsing**: Automatically analyzes PDF documents using AI vision
- **📊 Structured Data Extraction**: Converts unstructured PDF content into organized, searchable data
- **🎯 Multiple Output Formats**: Get results in both markdown and structured JSON
- **⚡ Batch Processing**: Handle multiple documents efficiently
- **🔧 Configurable**: Customize parsing parameters and output directories
- **📝 Jupyter Notebook Support**: Interactive development and testing

## 🚀 Quick Start

### Prerequisites

- Python 3.12 or higher
- Valid Vision Agent API key

### Installation

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd agentic-doc-extraction
   ```

2. **Install dependencies**
   ```bash
   pip install -e .
   ```
   or using uv (recommended):
   ```bash
   uv sync
   ```

3. **Set up your API key**
   
   Create a `.env` file in the project root:
   ```env
   VISION_AGENT_API_KEY=your_api_key_here
   ```

### Basic Usage

```python
from agentic_doc.parse import parse
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Parse a PDF document
result = parse(
    "path/to/your/document.pdf",
    result_save_dir="output"
)

# Access extracted data
print("Markdown format:")
print(result[0].markdown)

print("Structured JSON:")
print(result[0].chunks)
```

## 📁 Project Structure

```
agentic-doc-extraction/
├── main.py                 # Main execution script
├── .env                    # Environment variables (create this file)
├── doc-extraction.ipynb   # Jupyter notebook for interactive use
├── sample_pdfs/           # Sample PDF documents for testing
│   └── SampleHealthReport.pdf
├── output/                # Extracted data output directory
│   ├── extracted_data.json
│   └── SampleHealthReport_20250803_141003.json
├── pyproject.toml         # Project dependencies and metadata
└── README.md             # This file
```

## 🔧 Configuration

The project uses environment variables for configuration. Create a `.env` file in the project root:

```env
VISION_AGENT_API_KEY=your_api_key_here
```

### Available Environment Variables

- **VISION_AGENT_API_KEY**: Your Vision Agent API key (required)
- **ENDPOINT_HOST**: API endpoint URL (optional, defaults to Landing AI)
- **BATCH_SIZE**: Number of documents to process in parallel (optional)
- **MAX_WORKERS**: Maximum concurrent workers (optional)
- **MAX_RETRIES**: Maximum retry attempts for failed requests (optional)
- **PDF_TO_IMAGE_DPI**: DPI for PDF to image conversion (optional)
- **SPLIT_SIZE**: Document splitting size for processing (optional)

## 📊 Output Formats

### Markdown Output
The extracted content is available in clean markdown format, preserving the document structure and formatting.

### Structured JSON
Get organized, structured data with metadata including:
- Text content with positioning information
- Document sections and hierarchy
- Confidence scores
- Page and location data

## 🧪 Interactive Development

Use the included Jupyter notebook for interactive development and testing:

```bash
jupyter notebook doc-extraction.ipynb
```

The notebook provides:
- Step-by-step document parsing examples
- Interactive data exploration
- Real-time result visualization

## 📋 Example Output

### Sample Health Report Extraction

The project includes a sample health report that demonstrates the extraction capabilities:

**Extracted Data:**
- Patient demographics (name, DOB, address, contact info)
- Medical history and allergies
- Current medications with dosage information
- Provider information


## 🔗 Dependencies

- **agentic-doc**: Core document parsing library
- **python-dotenv**: Environment variable management
- **ipykernel**: Jupyter notebook support


## 🎯 Use Cases

This tool is particularly useful for:

- **Healthcare**: Extracting patient data from medical reports
- **Legal**: Parsing contracts and legal documents
- **Finance**: Processing invoices and financial statements
- **Research**: Extracting data from academic papers
- **Business**: Converting forms and applications to structured data

---

