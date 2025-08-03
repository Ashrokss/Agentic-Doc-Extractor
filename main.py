from agentic_doc.parse import parse
from dotenv import load_dotenv
load_dotenv()

# Parse a local file
result = parse(r"sample_pdfs\SampleHealthReport.pdf",
               result_save_dir=r"output")

# Get the extracted data as markdown
print("Extracted Markdown:")
print(result[0].markdown)

# Get the extracted data as structured chunks of content in a JSON schema
print("Extracted Chunks:")
print(result[0].chunks)
