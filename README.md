# 📊 MEF Dataset Downloader & Extractor

This project automates the download and processing of public finance datasets from the [Peruvian Ministry of Economy and Finance (MEF)](https://datosabiertos.mef.gob.pe/), specifically using the `datastorefiles` service.

It supports downloading both `.csv` and `.zip` files, extracting zipped files, and organizing them into a clean folder structure for further processing.

---

## 📁 Project Structure

```
project-root/
│
├── data/
│   ├── bronze/      # Raw downloaded files (CSV and extracted ZIPs)
│   └── silver/      # (Planned) Cleaned/processed datasets
│
├── downloader.py    # Main script to download and extract data
├── .gitignore       # Ignores raw data files
└── README.md        # Project documentation
```

---

## ✨ Features

* ⏱️ Decorator to time each download
* 🌐 Downloads `.csv` and `.zip` files directly from MEF OpenData Portal
* 📦 Automatically extracts `.zip` files and renames them to match naming convention

---

## 🔧 Setup

### 1. Clone the repo

```bash
git clone https://github.com/Tooruogata/mef-opendata-analysis.git
cd mef-opendata-analysis
```

### 2. Set up the docker image:

```bash
docker build -t mef-opendata-analysis:latest -f .devcontainer/Dockerfile .
docker run -dit --name mef-opendata-analysis -v "$repopath:/workspace" -w /workspace mef-opendata-analysis:latest
```

## 📃 Git Ignore Strategy

`.gitignore` is set up to ignore large raw data files:

```gitignore
**/data/**/*.zip
**/data/**/*.csv
**/data/**/*.xlsx
**/data/**/*.xls
**/data/**/*.json
!**/data/**/*.md
```

This means:

* All `.zip`, `.csv`, `.xlsx`, `.xls`, and `.json` files under any `data/` folder are ignored.

---

## 📊 Example Dataset Config

```python
list_dataset = [
    ('SIAF', '2025-Ingreso-Diario', 'ingreso_2025', 'csv'),
    ('SIAF', '2025-Ingreso-Diario', 'ingreso_2025', 'zip'),
]
```

The script will download:

* `https://fs.datosabiertos.mef.gob.pe/datastorefiles/2025-Ingreso-Diario.csv`
* `https://fs.datosabiertos.mef.gob.pe/datastorefiles/2025-Ingreso-Diario.zip`

It will save them as:

* `data/bronze/SIAF_ingreso_2025.csv`
* `data/bronze/SIAF_fzip_ingreso_2025.csv` (extracted and renamed from ZIP)

---

## 🚀 Next Steps

* [ ] Move cleaned data to `silver/`
* [ ] Combine the processed datasets and generate summary analytics in the `gold/` layer