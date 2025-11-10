f# 🌙 Yume – AI-Powered Script-to-Storyboard Generator

**Yume** is an AI-powered tool that transforms written scripts into **visual storyboards**. It automatically parses scenes, identifies characters, locations, and artifacts, and generates corresponding storyboard panels using **generative image models** — all while maintaining **visual consistency** across the story.

---

## 🚀 Features

* 🎬 **Script-to-Storyboard Conversion** – Upload or paste your screenplay, and Yume automatically breaks it into scenes and shots.
* 🧠 **Intelligent Parsing Engine** – Detects **characters**, **locations**, and **artifacts** from natural language text.
* 🧍‍♀️ **Memory for Consistency** – Remembers each character’s appearance, recurring settings, and props to ensure coherent visuals.
* 🎨 **Generative Storyboard Creation** – Uses cutting-edge **text-to-image diffusion models** to create cinematic storyboard panels.
* 🧩 **Editable Panels** – Regenerate or fine-tune any frame with simple prompts.
* 📚 **Scene Overview Dashboard** – Visual summary of all scenes, characters, and their interactions.

---

## 🛠️ How It Works

1. **Input your script**
   Paste or upload your screenplay in `.txt` or `.pdf` format.

2. **Scene Breakdown**
   Yume’s NLP engine identifies scene headers, transitions, and key elements.

3. **Entity Extraction**
   Automatically detects and stores character names, locations, and recurring objects.

4. **Visual Generation**
   Each scene is converted into storyboard panels using generative AI models (e.g., Stable Diffusion, DALL·E, or FLUX).

5. **Consistency Memory**
   Characters and environments are remembered — ensuring recurring elements look the same across scenes.

6. **Export & Share**
   Export storyboards as **PDFs**, **images**, or an **interactive web viewer**.

---

## 💡 Example

**Input:**

```
INT. HOTEL LOBBY – NIGHT  
RAM enters nervously, glancing around. Gopal struggles to carry a suitcase twice his size.  
MONA, elegant and confident, stands by the reception desk.  
```

**Yume Output:**

* Scene 01: Hotel Lobby (Night)
* Characters: Ram, Gopal, Mona
* Generated Panels:

  * Panel 1: Ram entering the lobby nervously
  * Panel 2: Gopal with oversized suitcase
  * Panel 3: Mona waiting at reception

---

## 🧰 Tech Stack

| Layer                | Technology                           |
| -------------------- | ------------------------------------ |
| Language Processing  | Python, spaCy, transformers          |
| Image Generation     | Stable Diffusion / DALL·E / FLUX     |
| Memory & Consistency | Vector embeddings (FAISS / ChromaDB) |
| Frontend (optional)  | Streamlit / React                    |
| Backend              | FastAPI                              |
| Storage              | SQLite / Supabase / Pinecone         |

---


## 🧪 Example Usage

```python
from yume import Yume

# Initialize Yume
yume = Yume()

# Load a script
yume.load_script("script.txt")

# Generate storyboard
yume.generate_storyboard(output_dir="storyboard_output")

# Export as PDF
yume.export("storyboard_output", format="pdf")
```

---

## 🔮 Roadmap

* [ ] Add dialogue-based emotion analysis for expressions
* [ ] Multi-style rendering (comic, cinematic, noir)
* [ ] Cloud-based collaboration mode
* [ ] Integration with screenwriting tools (Final Draft, Celtx, WriterDuet)

---

## 🤝 Contributing

Contributions are welcome!

---

## 🌌 Inspiration

Yume (夢) means *“dream”* in Japanese — this project aims to turn your **written dreams into visual stories**.

---
Data set: https://www.kaggle.com/code/burhanuddinlatsaheb/text-to-image-generation-stable-diffusion

