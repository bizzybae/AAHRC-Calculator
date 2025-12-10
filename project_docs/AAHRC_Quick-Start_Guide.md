# AAHRC Project: Quick-Start Implementation Guide

## Executive Summary
This comprehensive investigation algorithm provides a complete step-by-step roadmap for developing the **Albuminuria-Adjusted Hypertension Risk Calculator (AAHRC)** from conception to publication in **24 weeks (6 months)**.

**Key Metrics:**
- 46 main tasks, 433 subtasks
- 112 deliverables tracked
- 210-270 total hours (35-45 hrs/week)
- 4 sequential phases
- $0-500 budget (all free/open-source tools)

---

## Phase 1: SETUP & DATA ACQUISITION (Weeks 1-4)

### Week 1: Environment & Literature
**Goal:** Set up development environment and complete rapid literature review

**Day 1-2: Environment Setup** (2-3 hours)
```
1. Create GitHub repo: github.com/[YOUR-USERNAME]/AAHRC-Calculator
2. Install Python 3.10+, create virtual environment
3. Install packages: pandas, numpy, scikit-learn, lifelines, matplotlib, seaborn
4. Create folder structure: /data, /analysis, /models, /notebooks, /results, /app
5. Create .gitignore and initial README.md
```

**Day 3-5: Literature Review** (4-5 hours)
- Review 5-7 key papers on BP-albuminuria relationship
- Extract baseline risk estimates from literature
- Document prevalence data (e.g., 40% hypertensive, 20% have albuminuria)
- Create reference spreadsheet for model calibration

**Deliverables by End of Week 1:**
- ✓ GitHub repo with README.md
- ✓ Python environment installed & tested
- ✓ Literature_Summary.xlsx with key statistics

---

### Week 2: Data Download & Exploration
**Goal:** Acquire NHANES data and perform initial exploratory data analysis

**Day 1-2: Data Download** (3-4 hours)
```
1. Go to wwwn.cdc.gov/nchs/nhanes/
2. Download 2017-2020 cycle (most recent):
   - ALB_CR_H.XPT (albuminuria)
   - BPX_H.XPT (blood pressure)
   - DEMO_H.XPT (demographics)
3. Convert SAS format to CSV using Python:
   import pyreadstat
   df, meta = pyreadstat.read_xport("ALB_CR_H.XPT")
4. Merge datasets on SEQN (sequence number)
```

**Day 3-5: Exploratory Data Analysis** (4-5 hours)
- Load data into Jupyter notebook
- Check sample size: expect ~14,919 records
- Generate descriptive statistics table
- Create histograms for SBP, DBP, uACR distributions
- Document missing data patterns
- Identify outliers (SBP <70 or >280, etc.)

**Key Statistics Expected:**
- n = 14,919 adults
- Mean age: ~50 years
- Mean SBP: ~125 mmHg
- Median uACR: ~8 mg/g (highly right-skewed)
- ~20-25% have elevated uACR (≥30 mg/g)

**Deliverables by End of Week 2:**
- ✓ nhanes_raw.csv (merged dataset)
- ✓ EDA_Report.html (interactive summary)
- ✓ Missing_Data_Analysis.csv

---

### Week 3: Data Cleaning & AABPI Categories
**Goal:** Clean data and create 2×2 classification system

**Day 1-2: Data Cleaning** (3-4 hours)
```python
# Create average BP (from 3 readings)
df['SBP_avg'] = (df['SBPX1'] + df['SBPX2'] + df['SBPX3']) / 3

# Exclude outliers and missing data
df_clean = df[
    (df['SBP_avg'] >= 70) & (df['SBP_avg'] <= 280) &
    (df['Age'] >= 18) &
    (df['uACR'].notna())
].copy()

# Expected final n ≈ 12,000-13,000 after exclusions
```

**Day 3-5: Create AABPI Categories** (2-3 hours)
```python
def assign_aabpi_category(sbp, uacr):
    if sbp < 130 and uacr < 30:
        return 1  # Normotension
    elif sbp >= 130 and uacr < 30:
        return 2  # Isolated BP elevation
    elif sbp < 130 and uacr >= 30:
        return 3  # Occult hypertension
    else:
        return 4  # True HTN + HMOD

df_clean['AABPI_Category'] = df_clean.apply(
    lambda row: assign_aabpi_category(row['SBP_avg'], row['uACR']),
    axis=1
)

# Expected distribution (approximate):
# Category 1: 50-60% (normal)
# Category 2: 15-25% (elevated BP only)
# Category 3: 8-12% (occult HTN - key finding!)
# Category 4: 15-20% (true HTN)
```

**Deliverables by End of Week 3:**
- ✓ nhanes_cleaned.csv (final analytic dataset)
- ✓ AABPI_Category_Distribution.csv
- ✓ Data_Cleaning_Log.txt
- ✓ Category_Distribution_Plot.png (2×2 heatmap)

---

### Week 4: Descriptive Analysis & Data Requests
**Goal:** Create baseline characteristics table and submit external data requests

**Day 1-2: Descriptive Statistics** (3-4 hours)
```python
# Create Table 1: Baseline characteristics by category
table1 = df_clean.groupby('AABPI_Category').agg({
    'Age': ['mean', 'std'],
    'SBP_avg': ['mean', 'std'],
    'uACR': ['median', 'IQR'],
    'Female': 'mean',  # % female
    'Hypertension': 'mean',  # % with HTN dx
    'Diabetes': 'mean'  # % with DM dx
})

# Run statistical tests (ANOVA, Kruskal-Wallis)
from scipy.stats import f_oneway, kruskal
# Test if groups differ significantly
```

**Day 3-4: Submit External Data Requests** (1-2 hours each)
- SPRINT (NIH BioLINCC): ~30 minutes
- UK Biobank: ~2 hours (requires detailed proposal)
- Response times: 2-4 weeks for SPRINT, 4-8 weeks for UK Biobank

**Day 5: GitHub & Documentation** (1-2 hours)
- Commit all code with meaningful messages
- Update README.md with project overview
- Create CHANGELOG.md documenting weeks 1-4
- Set up GitHub Issues for tracking next phases

**Deliverables by End of Week 4:**
- ✓ Table1_BaselineCharacteristics.csv
- ✓ Statistical_Tests.txt (p-values, effect sizes)
- ✓ Data request confirmations (SPRINT, UK Biobank)
- ✓ GitHub repository updated

---

## Phase 2: STATISTICAL MODELING (Weeks 5-12)

### Weeks 5-6: Formula Development
**Goal:** Develop three AABPI formulas and compare performance

**Formula 1: Categorical (Simplest)**
```
AABPI_Category: 1, 2, 3, or 4
(Already created in Phase 1)
Performance: Baseline for comparison
```

**Formula 2: Ratio Method** (Week 5)
```python
# AABPI = SBP / (1 + uACR/100)
# Analogous to BMI = weight / height²
df['AABPI_Ratio'] = df['SBP_avg'] / (1 + df['uACR']/100)

# Lower ratio = better (less risk)
# High SBP + high uACR = low ratio
# Calculate C-statistic using logistic regression
```

**Formula 3: Regression-Based** (Week 6)
```python
# AABPI_Score = β0 + β1*SBP + β2*log(uACR) + β3*age + 
#               β4*female + β5*SBP*log(uACR)
from sklearn.linear_model import LogisticRegression

# Create interaction term
df['BP_uACR_interaction'] = df['SBP_avg'] * np.log(df['uACR'] + 0.1)

# Fit model on 80% training set
X = df[['SBP_avg', 'log_uACR', 'Age', 'Female', 'BP_uACR_interaction']]
y = df['CVD_Outcome']  # Simulated for now
model = LogisticRegression()
model.fit(X, y)
```

**Deliverables (End of Week 6):**
- ✓ Formula_Comparison_Table.csv (C-stats, sensitivity, specificity)
- ✓ ROC_Curves.png (3 formulas compared)
- ✓ Model_Coefficients.csv
- ✓ Visualization: SBP vs uACR risk surface

---

### Weeks 7-8: External Validation (If Data Available)
**Goal:** Validate models on SPRINT cohort (if data received)

```python
# Load SPRINT data (when available)
sprint_df = pd.read_csv('SPRINT_data.csv')

# Apply trained AABPI models to SPRINT
sprint_df['AABPI_Category'] = sprint_df.apply(assign_aabpi_category, axis=1)

# Calculate performance metrics on independent cohort
from sklearn.metrics import roc_auc_score, calibration_curve

c_stat_sprint = roc_auc_score(sprint_df['MACE'], sprint_df['AABPI_Score'])
# Expected: Similar C-stat to NHANES (within 0.02)

# Create Kaplan-Meier curves by category
from lifelines import KaplanMeierFitter
kmf = KaplanMeierFitter()
for cat in [1,2,3,4]:
    kmf.fit(sprint_df[sprint_df['AABPI_Category']==cat]['Followup_Years'],
            sprint_df[sprint_df['AABPI_Category']==cat]['MACE'])
    kmf.plot_survival_function(label=f'Category {cat}')
```

**Deliverables (End of Week 8):**
- ✓ External_Validation_Results.csv
- ✓ Calibration_Plot.png
- ✓ KM_Curves_by_Category.png
- ✓ Model_Validation_Report.md

---

### Weeks 9-10: Subgroup & Sensitivity Analyses
**Goal:** Test model performance across population subgroups

```python
# Subgroup 1: Age <60 vs ≥60
for age_group in ['<60', '≥60']:
    subset = df[df['Age_Group'] == age_group]
    c_stat = roc_auc_score(subset['CVD_Outcome'], subset['AABPI_Score'])
    print(f"C-stat {age_group}: {c_stat:.3f}")

# Subgroup 2: Male vs Female
# Subgroup 3: With/without diabetes

# Sensitivity analyses:
# A. Exclude medicated patients
# B. Restrict to multiple uACR measurements
# C. Test different uACR thresholds (25, 35 mg/g)
```

**Deliverables (End of Week 10):**
- ✓ Subgroup_Analysis_Table.csv
- ✓ Forest_Plot_HRs_by_Subgroup.png
- ✓ Sensitivity_Analysis_Results.csv

---

### Weeks 11-12: Final Model Selection & Report
**Goal:** Select best AABPI formula and write comprehensive modeling report

**Model Selection Criteria:**
1. Discrimination (C-statistic): Target ≥0.65
2. Calibration: Expected vs observed risk aligned
3. Simplicity: Easy to implement (favors categorical/ratio)
4. Clinical utility: Identifies important reclassifications

**Expected Winner:** Categorical (Formula 1) + optional regression for refinement

```python
# Save final model
import pickle
with open('models/aabpi_final.pkl', 'wb') as f:
    pickle.dump(final_model, f)

# Document all coefficients, thresholds, performance metrics
```

**10-15 Page Modeling Report Should Include:**
- Model development methodology
- All three formulas with equations
- Comparative performance table
- Calibration plots
- Subgroup results
- Sensitivity analyses
- Reclassification analysis (30-40% Category 3 patients)
- Limitations and next steps

**Deliverables (End of Week 12):**
- ✓ AABPI_Final_Model.pkl
- ✓ Model_Coefficients_Final.csv
- ✓ Comprehensive_Modeling_Report.pdf (15+ pages)
- ✓ GitHub commit with all analysis code

---

## Phase 3: WEB CALCULATOR DEVELOPMENT (Weeks 13-16)

### Week 13-14: Build & Deploy Web App
**Goal:** Create interactive calculator and deploy to cloud

**Backend Development (Flask)** - 5-6 hours
```python
# app.py
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

def calculate_aabpi(age, sbp, uacr, sex, egfr=None):
    """Calculate AABPI category and risk"""
    if sbp < 130 and uacr < 30:
        category = 1
        risk_pct = 5  # Low risk
    elif sbp >= 130 and uacr < 30:
        category = 2
        risk_pct = 10  # Intermediate
    elif sbp < 130 and uacr >= 30:
        category = 3
        risk_pct = 20  # High
    else:
        category = 4
        risk_pct = 35  # Very high
    
    return {
        'category': category,
        'risk_percent': risk_pct,
        'bp_target': '120-130 mmHg' if category <= 2 else '<120 mmHg',
        'recommendation': 'Consider ACEi/ARB and SGLT2i'
    }

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.json
    result = calculate_aabpi(
        data['age'], data['sbp'], data['uacr'], 
        data['sex'], data.get('egfr')
    )
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
```

**Frontend Development (HTML/CSS/JavaScript)** - 5-6 hours
```html
<!-- templates/index.html -->
<form id="calculator-form">
  <input type="number" id="age" placeholder="Age (years)" min="18" max="100">
  <input type="number" id="sbp" placeholder="Systolic BP (mmHg)" min="70" max="280">
  <input type="number" id="uacr" placeholder="uACR (mg/g)" min="0" max="10000">
  <select id="sex">
    <option>Male</option>
    <option>Female</option>
  </select>
  <button type="submit">Calculate Risk</button>
</form>

<div id="results" style="display:none;">
  <h2>Your Results</h2>
  <div id="traffic-light"></div>
  <p>10-Year CVD Risk: <span id="risk-percent"></span>%</p>
  <p>Recommended BP Target: <span id="bp-target"></span></p>
  <p>Recommendation: <span id="recommendation"></span></p>
  <button onclick="printResults()">Print Results</button>
</div>

<script>
document.getElementById('calculator-form').addEventListener('submit', async (e) => {
  e.preventDefault();
  const data = {
    age: parseInt(document.getElementById('age').value),
    sbp: parseInt(document.getElementById('sbp').value),
    uacr: parseFloat(document.getElementById('uacr').value),
    sex: document.getElementById('sex').value
  };
  
  const response = await fetch('/calculate', {
    method: 'POST',
    headers: {'Content-Type': 'application/json'},
    body: JSON.stringify(data)
  });
  
  const result = await response.json();
  document.getElementById('risk-percent').textContent = result.risk_percent;
  document.getElementById('bp-target').textContent = result.bp_target;
  document.getElementById('results').style.display = 'block';
});
</script>
```

**Deployment (Week 14)**
```bash
# Create Procfile for Heroku
# Push to GitHub
# Deploy: heroku create aahrc-calculator && git push heroku main
# Verify: Visit https://aahrc-calculator.herokuapp.com
```

### Week 15: Testing & Refinement
**Goal:** QA testing and user experience improvements

**Test Cases to Run:**
- [ ] Form submission with valid inputs
- [ ] Form validation (reject age <18, SBP >280)
- [ ] Results calculation accuracy
- [ ] Mobile responsiveness (iPhone, Android)
- [ ] Browser compatibility (Chrome, Firefox, Safari)
- [ ] Print/PDF generation
- [ ] Accessibility (screen readers)

### Week 16: Documentation & Final Polish
**Goal:** Complete documentation and prepare for promotion

**Deliverables (End of Week 16):**
- ✓ Live calculator at unique URL (Heroku, Railway, etc.)
- ✓ QA Testing Report (all tests passed)
- ✓ Demo video (3-5 min YouTube)
- ✓ User guide (1-page PDF)
- ✓ API documentation
- ✓ GitHub repository with complete code

---

## Phase 4: VALIDATION & PUBLICATION (Weeks 17-24)

### Weeks 17-18: Manuscript Writing
**Goal:** Write Methods and Results sections

**Methods Section (3-4 pages):**
- Study design (retrospective cohort)
- Data sources (NHANES 2017-2020, SPRINT if available)
- Variable definitions (BP measurement, uACR)
- AABPI formula (equations and categories)
- Statistical methods (logistic regression, C-stat)
- Data analysis steps

**Results Section (3-4 pages):**
- Table 1: Baseline characteristics by AABPI category
- Category distribution: ~50% Cat 1, 15% Cat 2, 10% Cat 3, 25% Cat 4
- Model performance: C-statistic ≥0.65
- Subgroup results (age, sex, diabetes)
- Reclassification analysis: ~35% of normotensive have albuminuria

**Figures:**
- Figure 1: 2×2 distribution heatmap
- Figure 2: ROC curves (3 formulas)
- Figure 3: Kaplan-Meier curves (4 categories)
- Figure 4: Risk surface (SBP vs uACR vs risk)

---

### Weeks 19-20: Write Introduction, Discussion & Submit
**Goal:** Complete manuscript and submit to journal

**Introduction (2-3 pages):**
- Hypertension affects 1 in 3 Americans
- Current BP-only definitions miss kidney damage
- BMI analogy: weight alone inadequate, similar for BP
- Albuminuria: independent risk factor
- Personalized medicine in hypertension
- Study aims: develop and validate AABPI

**Discussion (3-4 pages):**
- Main findings: AABPI improves risk stratification
- Comparison to PREVENT, ASCVD risk calculator
- Clinical implications: identify occult HTN
- Strengths: novel concept, free tool, public data
- Limitations: cross-sectional, retrospective, NHANES sampling
- Future directions: prospective validation, EHR integration

**Target Journals (in order of preference):**
1. **JAMA Network Open** - High impact, open access, accepts QI/methods
2. **Hypertension** - AHA official journal, strong for HTN research
3. **American Journal of Hypertension**
4. **BMJ Quality & Safety** - If emphasizing QI aspect

**Submission Package:**
- Formatted manuscript (per journal guidelines)
- Cover letter (1 page)
- Highlights (3-4 bullet points)
- Supplementary materials
- Conflict of interest declaration
- Author contributions

---

### Weeks 21-22: Conference Abstracts
**Goal:** Submit to major conferences

**Priority Conferences:**
1. **American Heart Association Scientific Sessions** (Abstract deadline: August)
2. **ASN Kidney Week** (Abstract deadline: June)
3. **ACC/AHA Annual Meeting** (Abstract deadline: December)

**Abstract Format (250-300 words):**
- Background: BP-only definitions inadequate
- Methods: NHANES cohort, AABPI development
- Results: 4-category classification, 35% reclassification
- Conclusions: AABPI improves risk stratification

**Submit via conference websites with tracking confirmation**

---

### Weeks 23-24: Final Documentation & Next Steps
**Goal:** Complete project and prepare for future phases

**Create Comprehensive Final Report (20-30 pages):**
- Executive summary
- Project background and rationale
- Methodology (4 phases)
- Key findings (tables, figures)
- Web calculator description
- Lessons learned
- Recommendations for Phase 2
- Full appendices

**Plan Phase 2 (Prospective Validation):**
- Multi-site prospective study
- 1,000-2,000 patients with prospective MACE outcomes
- EHR integration (Epic, Cerner)
- Timeline: 12-18 months
- Budget: $50,000-100,000

**Public Dissemination:**
- GitHub repository public (all code, analysis)
- Preprint on medRxiv (if journal review delayed)
- Social media announcement
- Press release (when published)
- Reach out to EHR vendors about integration

---

## Success Metrics Checklist

### End of Week 4 ✓
- [ ] NHANES data merged (14,919 records)
- [ ] Data cleaned and validated
- [ ] AABPI categories created (all 4 groups >100 patients)
- [ ] GitHub repository ready

### End of Week 12 ✓
- [ ] Three formulas developed and compared
- [ ] C-statistic ≥0.65 for best model
- [ ] External validation complete (if SPRINT available)
- [ ] Reclassification analysis documented

### End of Week 16 ✓
- [ ] Web calculator live and publicly accessible
- [ ] All QA tests passed
- [ ] Demo video created
- [ ] Full documentation complete

### End of Week 24 ✓
- [ ] Manuscript submitted to journal
- [ ] Conference abstracts submitted
- [ ] GitHub repository public and complete
- [ ] Project deliverables documented

---

## Resource Requirements

### Free Tools (Total Cost: $0-50)
- Python 3.10+ (free)
- Git & GitHub (free)
- Flask web framework (free)
- Jupyter Notebooks (free)
- VS Code editor (free)

### Free Data Sources
- NHANES (CDC): 14,919 records
- SPRINT (NIH): 9,361 records + hard outcomes
- UK Biobank (if approved): 456,000+ records

### Free Cloud Hosting
- Heroku: Free tier (sufficient)
- Railway.app: Free credits
- GitHub Pages: Static hosting

### Optional (Not Required)
- Journal open-access fee: $0-3,000
- Conference registration: $500-1,500
- Custom domain: $12-15/year

**Total Budget: $0-500 (within PBLI allocation)**

---

## Risk Mitigation

| Risk | Probability | Impact | Mitigation |
|------|------------|--------|-----------|
| Data delays | Medium | High | Proceed with NHANES; add later |
| Poor performance | Low | High | Add variables; test interactions |
| Deployment fails | Low | Medium | Multiple hosting platforms |
| Manuscript rejected | Medium | Medium | Plan revision; use lower-tier journal |
| Time constraints | High | Medium | Prioritize Phase 1-2; extend timeline |

---

## Quick Reference: GitHub Commands

```bash
# Initial setup
git init
git add .
git commit -m "Initial commit: Phase 1 complete"
git push origin main

# Weekly commits
git add analysis/
git commit -m "Week X: [Task description]"
git push origin main

# Create release (at project end)
git tag -a v1.0 -m "AAHRC v1.0 - Initial release"
git push origin v1.0
```

---

## Next Steps: Right Now

**Today:**
1. Create GitHub repository
2. Fork this algorithm document
3. Set up Python environment
4. Download NHANES data (wwwn.cdc.gov/nchs/nhanes/)

**Week 1:**
1. Complete environment setup
2. Perform rapid literature review
3. Start EDA on NHANES data

**Week 2:**
1. Complete data cleaning
2. Create AABPI categories
3. Generate Table 1

**Week 4:**
1. Submit SPRINT data request
2. Commit code to GitHub
3. Plan Phase 2 kickoff

---

**Good luck! This is an ambitious but achievable project. The detailed algorithm provides a complete roadmap to take your hypertension innovation from concept to published science in 6 months.**

*For questions or issues, refer to the comprehensive CSV files created alongside this guide.*
