from fastapi import FastAPI, HTTPException
from fastapi.responses import StreamingResponse
import pdfkit
import io

app = FastAPI()

@app.get("/generate_pdf")
def generate_pdf(url: str):
    try:
        # Use pdfkit to generate PDF from the given URL
        print("PDF URL", url)
        pdf_content = pdfkit.from_url(url, False)
        
        # Create a StreamingResponse to return the PDF as a response
        response = StreamingResponse(io.BytesIO(pdf_content), media_type="application/pdf")
        
        # Set the Content-Disposition header to suggest the filename when downloading
        response.headers["Content-Disposition"] = f"attachment; filename=generated_pdf.pdf"
        
        return response
    except Exception as e:
        # Handle exceptions, such as invalid URL or failure in PDF generation
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)