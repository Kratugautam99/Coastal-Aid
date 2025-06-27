# Coastal-Aid 🌊🛰️

> Empowering beachgoers with real-time recreational suitability insights via a mobile app.

---
## 📖 Table of Contents

- [ℹ️ About](#-about)  
- [🎯 Problem Statement](#-problem-statement)  
- [✨ Features](#-features)  
- [🗂️ Structure](#-structure)  
- [⚙️ Installation](#-installation)  
- [🚀 Usage](#-usage)  
- [🤝 Contributing](#-contributing)  
- [📄 License](#-license)  

---
<a id="-about"></a>
## ℹ️ About

**Coastal-Aid** is Team Coastal Aid’s entry for Eurekathon 2024 (the internal hackathon for Smart India Hackathon 2024). We’ve built a cross-platform mobile application that aggregates environmental, safety, and amenity data to rate beaches on their recreational suitability. Whether you’re planning a family outing, water sports adventure, or sunset stroll, Coastal-Aid helps you pick the perfect shoreline.  

- **BeachDatasetFinal.csv**  
  • 10,000+ beach records with features like water quality, tide timings, UV index, lifeguard count, nearby amenities, and GPS coordinates.  
  • Ready to feed directly into machine learning models.  

- **Smart India Hackathon.7z**  
  • Original CSVs, GeoTIFFs, sensor logs, and scraped safety reports compressed for archival.  
  • Extract with `7z x "Smart India Hackathon.7z"` to regenerate raw inputs.

---
## 🎯 Problem Statement

**SIH 1656**: Development of a mobile application to provide recreational suitability information of beach locations .  

---
## ✨ Features

- 🌦️ **Environmental Metrics**  
  • Real-time weather & UV index  
  • Tide timings & water quality  
- 🦺 **Safety Indicators**  
  • Lifeguard availability  
  • Rip-current warnings  
- 📍 **Amenities & Accessibility**  
  • Nearby parking, restrooms, eateries  
  • Public-transport links & walking trails  
- 📊 **Beach Rating Score**  
  • Composite index from weighted factors  
  • Historical trends & favorite-beach bookmarking

---
<a id="-structure"></a>
## 🗂️ Structure

```text
# Eurekathon – Smart India Hackathon 2024 (Problem Statement 1656) 🚀

> Internal hackathon submission by Team Coastal Aid: building end-to-end pipelines to score beach recreational suitability.

```

---
<a id="-installation"></a>
## ⚙️ Installation

1. Clone the repo  
   ```bash
   git clone https://github.com/Kratugautam99/Coastal-Aid.git
   cd Coastal-Aid
   ```
2. **Backend**  
   ```bash
   cd backend
   pip install -r requirements.txt  # or npm install
   uvicorn src.main:app --reload    # or node src/server.js
   ```
3. **Mobile App**  
   ```bash
   cd mobile
   flutter pub get                  # or npm install
   flutter run                      # or npm start
   ```

---
## 🚀 Usage


Open **SmartIndiaHackathonMLModelFinal.ipynb** to explore:

1. **Data Ingestion & Cleaning**  
2. **Exploratory Data Analysis** (visualizing correlations and feature distributions)  
3. **Feature Engineering** (rolling statistics for tides, one-hot encoding of amenities)  
4. **Model Training** (Random Forest, XGBoost, and a simple neural network)  
5. **Evaluation** (mean absolute error, R², feature‐importance plots)  
6. **Inference Demo** (sample beach-score predictions)

---
## 🤝 Contributing

We welcome enhancements! Please:

1. Fork this repository  
2. Create a branch (`git checkout -b feature/my-addition`)  
3. Commit your changes (`git commit -m "Add my feature"`)  
4. Push to your fork (`git push origin feature/my-addition`)  
5. Open a pull request detailing your improvements

---
## 📄 License

Distributed under the MIT License. See [LICENSE](LICENSE) for details.  

---
