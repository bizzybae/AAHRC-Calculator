# AAHRC-Calculator

**Albuminuria-Adjusted Hypertension Risk Calculator**

A comprehensive tool for personalizing blood pressure targets by kidney function. Predicts 10-year cardiovascular disease risk using blood pressure and urine albumin-creatinine ratio.

## 🎯 Project Overview
## Why AAHRC-Calculator Matters

The **AAHRC-Calculator** addresses a crucial clinical gap in cardiovascular risk assessment. Traditional **blood pressure–only** approaches may **under-recognize patients at high risk** due to underlying kidney damage, particularly those with elevated **urine albumin-to-creatinine ratio (uACR)**. Incorporating uACR into risk stratification is scientifically supported, as albuminuria is a well-established and independent predictor of cardiovascular events.

As a **prototype and research-focused tool**, the AAHRC-Calculator provides value by enabling exploration of key hypotheses and population-level patterns. It allows users to visualize how cardiovascular risk shifts when patients are **reclassified by albuminuria levels**, helping identify individuals who may benefit from **more aggressive blood pressure management** or **kidney-protective interventions**. This makes it a useful starting point for research, quality improvement, or hypothesis generation in hypertension and chronic kidney disease care.

### Executive Summary
This project develops the **Albuminuria-Adjusted Hypertension Risk Calculator (AAHRC)**, a novel clinical decision support tool that personalizes blood pressure management based on kidney function. Just as BMI adjusts weight interpretation based on height, AAHRC adjusts blood pressure interpretation based on albuminuria.

### The Clinical Problem
- Only **4.1%** of hypertensive patients are screened for albuminuria
- **40%** of untreated hypertensive patients have undetected albuminuria
- Current guidelines provide one-size-fits-all BP targets
- Two patients with identical BP (145/90) but different uACR (10 vs 250 mg/g) receive the same diagnosis despite different cardiovascular risk

### The Solution
AAHRC creates 4 distinct phenotypes:
1. **Normal BP + Normal Albuminuria** → True normotension (lowest risk)
2. **Elevated BP + Normal Albuminuria** → Isolated BP elevation (intermediate risk)
3. **Normal BP + Elevated Albuminuria** → Occult hypertension (high risk, often missed)
4. **Elevated BP + Elevated Albuminuria** → True hypertension with organ damage (highest risk)

## 📊 Project Metrics

- **Timeline**: 24 weeks (6 months)
- **Budget**: $0-500 (all free/open-source tools)
- **Tasks**: 46 main tasks, 433 subtasks
- **Deliverables**: 112 tracked items
- **Time Investment**: 210-270 hours (35-45 hrs/week)

## 🗂️ Repository Structure

```
AAHRC-Calculator/
├── data/                    # NHANES and other public datasets
│   ├── raw/
│   ├── processed/
│   └── external/
├── notebooks/               # Jupyter notebooks for analysis
│   ├── 01_data_exploration.ipynb
│   ├── 02_model_development.ipynb
│   └── 03_validation.ipynb
├── src/                     # Source code
│   ├── data/               # Data processing scripts
│   ├── features/           # Feature engineering
│   ├── models/             # Model training and prediction
│   └── visualization/      # Plotting utilities
├── app/                     # Web calculator application
│   ├── static/             # CSS, JS, images
│   ├── templates/          # HTML templates
│   └── app.py              # Flask application
├── tests/                   # Unit and integration tests
├── docs/                    # Documentation
├── results/                 # Model outputs, figures, tables
└── requirements.txt         # Python dependencies
```

## 🚀 Quick Start

### Prerequisites
- Python 3.10+
- Git
- Virtual environment tool (venv, conda)

### Installation

```bash
# Clone the repository
git clone https://github.com/bizzybae/AAHRC-Calculator.git
cd AAHRC-Calculator

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Week 1: Get Started

1. **Download NHANES Data**
   ```bash
   # Navigate to CDC NHANES website
   # Download 2017-2020 cycle:
   # - ALB_CR_H.XPT (albuminuria)
   # - BPX_H.XPT (blood pressure)
   # - DEMO_H.XPT (demographics)
   ```

2. **Run Initial Analysis**
   ```bash
   jupyter notebook notebooks/01_data_exploration.ipynb
   ```

## 📈 Development Phases

### Phase 1: Setup & Data Acquisition (Weeks 1-4)
- ✓ GitHub repository setup
- ✓ Python environment configuration
- □ NHANES data download and processing
- □ Exploratory data analysis
- □ Literature review completion

### Phase 2: Statistical Modeling (Weeks 5-12)
- □ Develop 3 AABPI formulas (categorical, ratio, regression-based)
- □ Cox proportional hazards models
- □ Model comparison and selection
- □ External validation
- □ Subgroup analyses

### Phase 3: Web Calculator Development (Weeks 13-16)
- □ Flask backend development
- □ Frontend UI/UX design
- □ Risk visualization tools
- □ Deployment to cloud platform
- □ User testing and QA

### Phase 4: Validation & Publication (Weeks 17-24)
- □ Manuscript writing
- □ Conference abstract submission
- □ Documentation completion
- □ Community outreach
- □ Phase 2 planning (prospective validation)

## 🔬 Scientific Background

### Supporting Evidence
- **PREVENT equations (2024)**: Already include uACR as optional predictor
- **SPRINT trial**: Albuminuria modifies BP treatment benefit
- **NHANES data**: Continuous BP-albuminuria-CVD relationship (30,000+ participants)
- **ESC/AHA guidelines**: Different BP targets recommended by albuminuria status

### Key Findings from Literature
- Each 5 mg/g increase in uACR → 1.31× increase in hypertension prevalence
- Each doubling of uACR → 11% increase in cardiovascular events
- 53.5% of patients with severe albuminuria not on guideline-recommended therapy
- Ratio of undetected to detected albuminuria in hypertension: **19.5:1**

## 📊 Publicly Available Datasets

### Primary Dataset: NHANES
- **Size**: 30,000+ participants
- **Variables**: BP, uACR, demographics, outcomes
- **Access**: Free, no authentication required
- **Download**: [CDC NHANES](https://wwwn.cdc.gov/nchs/nhanes/)

### Validation Datasets
1. **SPRINT**: 9,361 participants, hard CVD outcomes (requires application)
2. **UK Biobank**: 456,000+ with uACR, 10-year follow-up
3. **ACCORD-BP**: Diabetes subgroup, albuminuria-rich cohort
4. **CKD-PC**: Meta-analysis dataset, 2+ million participants

## 🛠️ Technology Stack

- **Language**: Python 3.10+
- **Data Analysis**: pandas, numpy, scipy
- **Machine Learning**: scikit-learn, lifelines (survival analysis)
- **Visualization**: matplotlib, seaborn, plotly
- **Web Framework**: Flask
- **Frontend**: HTML/CSS/JavaScript, Bootstrap
- **Deployment**: Heroku/Render (free tier)
- **Version Control**: Git/GitHub

## 📝 Documentation

Detailed documentation available in `/docs` directory:
- [Quick-Start Guide](docs/AAHRC_Quick-Start_Guide.md)
- [Comprehensive Algorithm](docs/AAHRC_Comprehensive_Algorithm.csv)
- [Week 1 Task Checklist](docs/AAHRC_Week1_Task_Checklist.csv)
- [Project Status Tracker](docs/AAHRC_Project_Status_Tracker.csv)

## 🤝 Contributing

Contributions welcome! Please:
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📧 Contact

**Project Lead**: Quddarat Mushtaq, MD
- GitHub: [@bizzybae](https://github.com/bizzybae)
- Email: QuddaratMushtaq@gmail.com

## 🙏 Acknowledgments

- CDC NHANES for public data access
- NHLBI BioLINCC for SPRINT/ACCORD data
- AHA/ACC for PREVENT equations framework
- Open-source community for tools and libraries

## 📚 Citation

If you use this tool in your research, please cite:

```bibtex
@software{aahrc2025,
  author = {Quddarat Mushtaq, MD},
  title = {AAHRC-Calculator: Albuminuria-Adjusted Hypertension Risk Calculator},
  year = {2025},
  url = {https://github.com/bizzybae/AAHRC-Calculator}
}
```

## 🎯 Project Milestones

| Milestone | Target Date / Phase | Description / Deliverables |
|---|---|---|
| **Phase 0 — Repository Setup & Infrastructure** | ● Done | Repository created; Python environment configured; basic folder structure established. |
| **Phase 1 — Data Acquisition & Preliminary Analysis** | Weeks 1–4 (initial plan) | Download and process primary dataset (e.g. NHANES), perform exploratory data analysis, compile literature review, assess data quality. |
| **Phase 1b — Data Quality & Pre-processing Review** | Month 2 | Define data-quality standards, implement data cleaning pipelines, document exclusion criteria, run sanity checks on processed data. |
| **Phase 2 — Statistical Modeling & Internal Validation** | Weeks 5–12 (expanded) | Develop candidate risk-prediction formulas (categorical, ratio-based, regression-based), fit survival/Cox models (or appropriate models), perform internal validation (e.g. cross-validation, bootstrapping), compare model performance. |
| **Phase 2b — Sensitivity Analyses & Subgroup Exploration** | Month 4 | Conduct subgroup analyses (e.g. by age, sex, baseline uACR categories), test robustness to alternative model specifications, examine effect of measurement variability (e.g. BP, uACR). |
| **Phase 2c — Calibration & Risk-Recalibration** | Month 5 | Assess calibration (e.g. calibration plots, calibration-in-the-large), adjust model if needed, document calibration performance. |
| **Phase 3 — External Validation** | Month 6–8 | Identify and import external datasets (e.g. other cohort(s) with BP + uACR + outcomes), apply model, assess discrimination & calibration on external data, document performance. |
| **Phase 4 — Web Calculator Development & Deployment** | Weeks 13–16 (initial plan) → Revised: Month 7–9 | Build and polish frontend & backend (e.g. Flask), integrate risk-prediction model, build UI/UX for users, add risk visualization tools, perform user testing & QA, deploy to cloud or hosting platform. |
| **Phase 5 — Documentation & User Guide Release** | Month 9 | Write comprehensive documentation: quick-start guide, algorithmic description, user instructions, data & versioning notes; release user-friendly documentation site; add usage examples. |
| **Phase 6 — Publication & Dissemination** | Month 10–12 | Prepare manuscript describing development, validation, limitations; submit to peer-reviewed journal or preprint server; draft conference abstract/ poster; outreach to clinical/research community. |
| **Phase 7 — Prospective / Longitudinal Validation Planning** | After successful external validation & publication | Design prospective validation study or registry-based study; draft protocol; seek collaborators; pre-register analysis plan. |
| **Phase 8 — Maintenance, Versioning & Community Engagement** | Ongoing | Version releases, issue/bug tracking, community feedback integration, periodic re-validation as new data emerge, update dependencies, ensure documentation remains current. |
| **Phase 9 — Feature Expansion & Extensions** | Longer-term / Future | Explore inclusion of additional predictors (e.g. comorbidities, lab values), adapt to different populations, support alternative endpoints (CKD progression, renal outcomes), build API or package for easy integration. |

---

**Status**: 🚧 Active Development  
**Last Updated**: December 9, 2025  
**Version**: 0.2.0 (Setup)
