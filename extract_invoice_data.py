from pydantic import BaseModel, Field
from agentic_doc.parse import parse
from typing import Optional
from datetime import date
import json
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Define the fields you want to extract
class InvoiceFields(BaseModel):
    bill_to_name: str = Field(description="The full name of the person or entity being billed.")
    bill_to_address: str = Field(description="The address of the billed entity.")
    invoice_number: str = Field(description="The invoice number.")
    customer_number: str = Field(description="The customer number associated with the invoice.")
    invoice_date: date = Field(description="The date when the invoice was issued.")
    invoice_period_start: date = Field(description="Start date of the invoice billing period.")
    invoice_period_end: date = Field(description="End date of the invoice billing period.")
    gross_amount: float = Field(description="The total gross amount including VAT.")
    net_amount: float = Field(description="The total amount excluding VAT.")
    vat_amount: float = Field(description="The VAT amount charged.")
    iban: Optional[str] = Field(description="The IBAN number for payment.", default=None)
    bic: Optional[str] = Field(description="The BIC code for payment.", default=None)
    company_issuing_invoice: str = Field(description="The name of the company that issued the invoice.")

def date_serializer(obj):
    """Custom serializer for date objects"""
    if isinstance(obj, date):
        return obj.isoformat()
    raise TypeError(f"Object of type {type(obj)} is not JSON serializable")

def extract_invoice_data():
    """Extract invoice data and return it in various formats"""
    
    # Parse the invoice
    results = parse(r"sample_pdfs\sample-invoice.pdf", extraction_model=InvoiceFields, result_save_dir=r"output")
    
    # Method 1: Get as dictionary
    extraction_dict = results[0].extraction.model_dump()
    
    # Method 2: Get as JSON string
    extraction_json = json.dumps(extraction_dict, indent=2, default=date_serializer)
    
    # Method 3: Access individual fields
    fields = results[0].extraction
    
    print("=== EXTRACTION DATA ===")
    print("\n1. As Dictionary:")
    print(json.dumps(extraction_dict, indent=2, default=str))
    
    print("\n2. As JSON:")
    print(extraction_json)
    
    print("\n3. Individual Fields:")
    print(f"Bill to Name: {fields.bill_to_name}")
    print(f"Bill to Address: {fields.bill_to_address}")
    print(f"Invoice Number: {fields.invoice_number}")
    print(f"Customer Number: {fields.customer_number}")
    print(f"Invoice Date: {fields.invoice_date}")
    print(f"Period Start: {fields.invoice_period_start}")
    print(f"Period End: {fields.invoice_period_end}")
    print(f"Gross Amount: {fields.gross_amount}")
    print(f"Net Amount: {fields.net_amount}")
    print(f"VAT Amount: {fields.vat_amount}")
    print(f"IBAN: {fields.iban}")
    print(f"BIC: {fields.bic}")
    print(f"Company: {fields.company_issuing_invoice}")
    
    # Save to file
    with open('output/invoice_extraction.json', 'w') as f:
        json.dump(extraction_dict, f, indent=2, default=date_serializer)
    
    print("\n4. Data saved to 'output/invoice_extraction.json'")
    
    return extraction_dict

if __name__ == "__main__":
    extract_invoice_data() 