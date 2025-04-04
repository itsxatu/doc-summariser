# 🧠 PDF Summarizer using Langchain + Ollama

This is a simple yet powerful Python script that uses AI (via Ollama's `gemma:2b` model) to extract and summarize text from any PDF file. Perfect for quickly digesting long academic papers, reports, or e-books.

---

## 📌 Features

- 🔍 **PDF Text Extraction** – Reads and extracts all text from the PDF.
- ✂️ **Text Chunking** – Splits long documents into manageable parts for accurate summarization.
- 🤖 **AI Summarization** – Uses `Langchain` with Ollama’s `gemma:2b` model.
- 📂 **Automatic Saving** – Saves the summary as a `.txt` file in the same folder as your PDF.
- 👡 **Interactive File Picker** – Choose your PDF file without typing the path manually (if you don't pass it in terminal).
- 📊 **Progress Bar** – Shows real-time progress while processing.

---

## 🛠️ Requirements

Make sure you have Python 3.8+ installed.

### 🧪 Install Dependencies

```bash
pip install langchain PyPDF2 python-dotenv tqdm
```

### 🦙 Install & Run Ollama

Make sure you have [Ollama](https://ollama.com/) installed and running locally.

Then pull the `gemma:2b` model:

```bash
ollama pull gemma:2b
```

---

## 🚀 How to Use

### 📁 Option 1: Run with file path

```bash
python summariser.py "path/to/your/file.pdf"
```

### 👡 Option 2: Run without arguments (GUI file picker)

```bash
python summariser.py
```

You’ll be prompted to select a PDF file from your system.

---

## 📝 Output

- The summary is printed in the terminal.
- A `.txt` file is saved alongside your PDF file:
  ```
  yourfilename_summary_2025-04-04_15-30.txt
  ```

---

## 📂 File Structure

```
.
├── summariser.py
├── README.md
└── .env (optional for future use)
```

---

## 🙌 Credits

Built with ❤️ using:
- [Langchain](https://www.langchain.com/)
- [Ollama](https://ollama.com/)
- [Gemma:2B Model](https://ollama.com/library/gemma)
- [PyPDF2](https://pypi.org/project/PyPDF2/)
- [TQDM](https://tqdm.github.io/)

---

## 📃 License

This project is open source and available under the [MIT License](LICENSE).

