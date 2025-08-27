# Assistant Project 🎵🤖

This project is a simple Python-based assistant that can handle different tasks, including playing music, handling commands, and performing automated actions.  

---

## 📂 Project Structure
```
Assistant-Project/
│── main_1.py        # Core assistant logic / functions
│── main_2.py        # Secondary logic (helper/extended features)
│── music.json       # Music database with YouTube links
```

---

## ⚙️ Requirements
- Python 3.8+  
- Required libraries (install with pip):
```bash
pip install -r requirements.txt
```

*(You can create a `requirements.txt` later if needed.)*

---

## ▶️ Usage
Run the assistant with:
```bash
python main_1.py
```
or
```bash
python main_2.py
```

---

## 🎶 Music Integration
The assistant uses `music.json` to fetch songs. Example entries:
```json
{
    "darkside": "https://youtu.be/M-P4QBt-FWw?si=x47FhztLGM_S5moG",
    "alone": "https://youtu.be/1-xGerv5FOk?si=Fb3OaBGiyaVWscFt"
}
```
You can add your own songs by editing `music.json`.

---

## 🚀 Features
- Command-based assistant  
- Music playback (via YouTube links in `music.json`)  
- Extendable with new commands  

---

## 👨‍💻 Author
- **Sarthak Patoliya**  

---

## 📜 License
This project is for personal/educational use.
