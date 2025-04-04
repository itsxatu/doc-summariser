import os
import sys
import tkinter as tk
from tkinter import filedialog
from langchain_community.llms import Ollama
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from PyPDF2 import PdfReader
from tqdm import tqdm
from dotenv import load_dotenv
from datetime import datetime
import textwrap

load_dotenv()

CHUNK_SIZE = 2000

def extract_text_from_pdf(file_path):
    try:
        reader = PdfReader(file_path)
        text = ""
        print(f"📖 Extracting text from {file_path}...")
        for page in tqdm(reader.pages, desc="Reading PDF pages"):
            text += page.extract_text() or ""
        return text.strip()
    except Exception as e:
        print(f"❌ Error reading PDF: {e}")
        sys.exit(1)

def split_text(text, chunk_size=CHUNK_SIZE):
    return textwrap.wrap(text, chunk_size)

def summarize_chunk(chunk, llm, chain):
    return chain.run(chunk)

def summarize_text_with_ollama(text):
    try:
        llm = Ollama(model="gemma:2b", temperature=0.6)

        prompt_template = PromptTemplate(
            input_variables=["text"],
            template=(
                "You're an expert summarizer. Summarize the following text clearly, preserving key points and important details:\n\n"
                "{text}\n\nSummary:"
            )
        )

        chain = LLMChain(llm=llm, prompt=prompt_template)
        chunks = split_text(text)

        print(f"\n🧠 Summarizing in {len(chunks)} chunk(s)...")
        summary_parts = []
        for i, chunk in enumerate(chunks, 1):
            print(f"🔹 Summarizing chunk {i}/{len(chunks)}...")
            summary = summarize_chunk(chunk, llm, chain)
            summary_parts.append(summary.strip())

        final_summary = "\n\n".join(summary_parts)
        return final_summary

    except Exception as e:
        print(f"❌ Error generating summary: {e}")
        sys.exit(1)

def select_pdf_file():
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(
        title="Select a PDF file",
        filetypes=[("PDF Files", "*.pdf")]
    )
    return file_path

def save_summary(summary, original_path):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    base_name = os.path.splitext(os.path.basename(original_path))[0]
    save_path = os.path.join(os.path.dirname(original_path), f"{base_name}_summary_{timestamp}.txt")

    with open(save_path, "w", encoding="utf-8") as f:
        f.write(summary)
    print(f"\n✅ Summary saved at: {save_path}")

def main():
    if len(sys.argv) > 1:
        pdf_path = sys.argv[1]
    else:
        print("📂 No file path provided. Opening file dialog...")
        pdf_path = select_pdf_file()

    if not pdf_path or not os.path.isfile(pdf_path):
        print("❌ No valid file selected.")
        sys.exit(1)

    text = extract_text_from_pdf(pdf_path)
    summary = summarize_text_with_ollama(text)

    print("\n📝 Final Summary:")
    print("=" * 60)
    print(summary)
    print("=" * 60)

    save_summary(summary, pdf_path)

if __name__ == "__main__":
    main()