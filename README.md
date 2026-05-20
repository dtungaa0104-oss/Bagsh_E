# 🎓 БагшAI — Хичээлийн Хөтөлбөр Боловсруулагч

Монгол ЕБС-ийн 1–12-р ангийн бүх хичээлийн **хичээлийн хөтөлбөр** (lesson plan) автоматаар боловсруулдаг AI систем.

---

## ✨ Онцлог

- 🇲🇳 **Бүрэн монгол хэлтэй** интерфейс
- 📚 **1–12-р анги** — бүх хичээл, сэдвийг хамарсан
- 🧠 **Bloom-ийн таксономи** дагуу 3 түвшний зорилт (А–Б–В)
- 📋 **Discovery Learning + Cooperative Learning** арга зүй
- 🖨️ **A4 хэвлэх** бэлэн, мэргэжлийн форматтай
- ⚡ Хэдэн секундэд бэлэн хөтөлбөр гардаг

---

## 📁 Бүтэц

```
bagsh-ai/
├── app.py                  # Flask веб аппликейшн
├── requirements.txt        # Python хамаарлууд
├── data/
│   └── curriculum.json    # ЕБС-ийн хичээлийн агуулга
├── templates/
│   └── index.html         # Үндсэн HTML загвар
└── static/
    ├── css/style.css      # Дизайн
    └── js/main.js         # Интерактив логик
```

---

## 🚀 Суулгах ба ажиллуулах

### 1. Репозиторий хуулах
```bash
git clone https://github.com/YOUR_USERNAME/bagsh-ai.git
cd bagsh-ai
```

### 2. Virtual environment үүсгэх
```bash
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
```

### 3. Хамаарлуудыг суулгах
```bash
pip install -r requirements.txt
```

### 4. Ажиллуулах
```bash
python app.py
```

Браузерт: `http://localhost:5000` хаягаар нээнэ үү.

---

## 🌐 GitHub Pages / Render дээр байршуулах

### Render.com (үнэгүй)
1. `render.com` дээр бүртгэл үүсгэх
2. New → Web Service → GitHub repo холбох
3. Start command: `python app.py`
4. Environment: Python 3.11

### Railway.app
```bash
railway login
railway init
railway up
```

---

## 📊 Хамарсан хичээлүүд

| Анги | Хичээлүүд |
|------|-----------|
| 1–4 | Монгол хэл, Математик, Байгаль судлал, Хөгжим, Дүрслэх урлаг, Биеийн тамир |
| 5–8 | + Физик, Хими, Биологи, Газарзүй, Түүх, Англи хэл, Мэдээлэл зүй |
| 9–12 | + Алгебр, Геометр, Нийгмийн ухаан, Эдийн засаг, ЭЕШ бэлтгэл |

---

## 🔧 Хөгжүүлэх

### Шинэ хичээл нэмэх
`data/curriculum.json` файлд нэмнэ:
```json
"6": {
  "subjects": {
    "Шинэ хичээл": {
      "topics": ["Сэдэв 1", "Сэдэв 2"]
    }
  }
}
```

### AI интеграц нэмэх
`app.py`-д Anthropic API ашиглаж хөтөлбөрийг илүү ухаалаг болгох боломжтой:
```python
import anthropic
client = anthropic.Anthropic(api_key="...")
```

---

## 📚 Мэдээллийн эх сурвалж

- **Боловсролын яам** — www.mecs.gov.mn
- **Боловсролын үнэлгээний төв** — www.eec.mn  
- **Econtent** — www.econtent.mn
- **Монгол сурах бичиг** — 1–12-р ангийн үндэсний хөтөлбөр

---

## 📄 Лиценз

MIT License — чөлөөтэй ашиглах, өөрчлөх боломжтой.

---

*БагшAI — Монголын багш нарт зориулсан 🇲🇳*
