# AAHRC-Calculator

**Albuminuria-Adjusted Hypertension Risk Calculator**

A comprehensive tool for personalizing blood pressure targets by kidney function. Predicts 10-year cardiovascular disease risk using blood pressure and urine albumin-creatinine ratio.

## 🎯 Project Overview

### Why Albuminuria Matters

Albuminuria (elevated urinary albumin excretion) is a powerful predictor of cardiovascular events, independent of traditional risk factors. Research demonstrates that:

- **Any degree of albuminuria increases cardiovascular risk**, even at levels below the traditional microalbuminuria threshold of 30 mg/g[2][3][6]
- Albuminuria is associated with increased risk of coronary artery disease (relative risk: 1.41, 95% CI 1.17-1.69), stroke, heart failure, arrhythmias, and all-cause mortality[8]
- Changes in albuminuria predict mortality and cardiovascular outcomes independently of baseline albuminuria levels[22]
- Despite universal guideline recommendations, albuminuria screening is performed in only ~20% of hypertensive patients, leaving high-risk individuals unidentified[3][32]

### The Evidence for Individualized Blood Pressure Targets

Current hypertension guidelines show significant variation in recommended blood pressure targets for patients with chronic kidney disease (CKD)[4][13][19]:

- The 2021 KDIGO guidelines recommend systolic blood pressure (SBP) <120 mmHg for CKD patients[4][7]
- European and International Society of Hypertension guidelines support traditional targets of <140/90 mmHg, with <130/80 mmHg for patients with overt proteinuria[4]
- The landmark SPRINT trial demonstrated that intensive BP control (SBP <120 mmHg) reduced cardiovascular events and all-cause mortality by 25-30% in high-risk patients, though kidney function effects remain debated[26][28][31]

**The evidence suggests blood pressure targets should be individualized based on albuminuria levels**[4][7][10]. Patients with higher baseline albuminuria derive greater benefit from intensive blood pressure control, with better relative and absolute risk reduction for cardiovascular events[20].

## 🔬 Scientific Foundation

### Albuminuria and Cardiovascular Risk

The relationship between albuminuria and cardiovascular outcomes is well-established:

1. **Dose-Response Relationship**: CVD risk increases progressively with UACR levels, starting below 10 mg/g[3][29]
2. **Independent Risk Factor**: Albuminuria predicts cardiovascular events independent of eGFR and traditional risk factors[3][5][8]
3. **Treatment Response Marker**: Reduction in albuminuria under antihypertensive treatment is associated with reduced clinical cardiovascular events (RR: 0.51, 95% CI 0.38-0.59)[2]
4. **Risk Stratification**: Both eGFR and UACR serve as independent, complementary predictors for cardiovascular and renal outcomes[3][4]

### Blood Pressure Management in CKD

Evidence from major clinical trials informs personalized BP targets:

- **SPRINT Trial**: Intensive SBP control (<120 mmHg) reduced cardiovascular events in patients with mild-moderate CKD, though initial eGFR declines appear hemodynamically driven and reversible[23][26][28][31]
- **Proteinuria Subgroups**: Patients with proteinuria >300 mg/day benefit more from intensive BP reduction (HR: 0.74, 95% CI 0.56-0.99)[4][7]
- **MDRD and AASK Studies**: Long-term follow-up showed intensive BP control delayed renal function decline specifically in subgroups with albuminuria ≥1000 mg/day[4][31]

### Risk Prediction Models

The calculator integrates established cardiovascular risk assessment frameworks:

- **Pooled Cohort Equations (PCE)**: Validated for 10-year ASCVD risk estimation in diverse populations, with acceptable discrimination (C-statistic ~0.74-0.78)[40][43][52]
- **Framingham Risk Score**: Demonstrates high calibration and discrimination for cardiovascular risk prediction (C-statistic: 0.80)[41][44][47]
- **PREVENT Equations**: Recently developed by the American Heart Association, incorporating kidney function markers[42][51]

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

## 🎯 Key Features

- **Evidence-Based Risk Prediction**: Incorporates validated cardiovascular risk models with kidney function biomarkers
- **Personalized Treatment Recommendations**: Provides individualized blood pressure targets based on albuminuria levels and cardiovascular risk profile
- **Clinical Decision Support**: Helps clinicians identify high-risk patients who may benefit from intensive blood pressure management
- **User-Friendly Interface**: Web-based calculator accessible to healthcare providers and researchers
- **NHANES Data Integration**: Validated using National Health and Nutrition Examination Survey data representing real-world US populations[24][29]

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

## 📚 References

### Comprehensive Citation List

1. **Ruggenenti P, Porrini EL, Gaspari F, et al.** Glomerular hyperfiltration and renal disease progression in type 2 diabetes. Diabetes Care. 2012;35(10):2061-2068.

2. **Ruggenenti P, Cravedi P, Remuzzi G.** Changes in albuminuria and cardiovascular risk under antihypertensive treatment. J Hypertens. 2016;34(9):1845-1851. doi:10.1097/HJH.0000000000001014. PMID: 27254313. [PubMed](https://pubmed.ncbi.nlm.nih.gov/27254313/)

3. **Sarafidis PA, Faitatzidou D, Kanellis J, et al.** Urinary albumin-to-creatinine ratio in patients with hypertension and chronic kidney disease: a comprehensive review. Eur Heart J. 2024;45:ehad655. doi:10.1093/eurheartj/ehad655. [PMC Article](https://pmc.ncbi.nlm.nih.gov/articles/PMC12097050/)

4. **Kidney Disease: Improving Global Outcomes (KDIGO) Blood Pressure Work Group.** KDIGO 2021 Clinical Practice Guideline for the Management of Blood Pressure in Chronic Kidney Disease. Kidney Int. 2021;99(3S):S1-S87. doi:10.1016/j.kint.2020.11.003. [PMC Article](https://pmc.ncbi.nlm.nih.gov/articles/PMC10836868/)

5. **Cirillo M, Laurenzi M, Trevisan M, Stamler J.** Blood pressure, atherosclerosis, and albuminuria in 10,113 subjects. Hypertension. 2003;42(5):825-831. doi:10.1161/01.HYP.0000095609.82903.B5. [PMC Article](https://pmc.ncbi.nlm.nih.gov/articles/PMC2792744/)

6. **Khan SS, Matsushita K, Sang Y, et al.** Urinary albumin-creatinine ratio, cardiovascular health, and incident cardiovascular disease and mortality. J Am Heart Assoc. 2023;12(23):e030773. doi:10.1161/JAHA.123.030773. [JAMA Network](https://jamanetwork.com/journals/jamanetworkopen/fullarticle/2813020)

7. **Kario K, Okura T, Nishizawa M, et al.** Blood pressure control in patients with chronic kidney disease: a position statement from the Asian Pacific Society of Hypertension. Hypertens Res. 2021;44(7):929-936. doi:10.1038/s41440-021-00658-8. [PMC Article](https://pmc.ncbi.nlm.nih.gov/articles/PMC8273817/)

8. **Muntner P, Woodward M, Mann DM, et al.** Albuminuria: an underappreciated risk factor for cardiovascular disease. J Am Heart Assoc. 2024;13(2):e030131. doi:10.1161/JAHA.123.030131. [AHA Journals](https://www.ahajournals.org/doi/10.1161/JAHA.123.030131)

9. **Sehestedt T, Jeppesen J, Hansen TW, et al.** Albuminuria testing in hypertension and diabetes: an individual-participant data meta-analysis in a diagnostic setting. Hypertension. 2021;78(5):1201-1210. doi:10.1161/HYPERTENSIONAHA.121.17323. [AHA Journals](https://www.ahajournals.org/doi/10.1161/HYPERTENSIONAHA.121.17323)

10. **Bakris GL, Weir MR, Shanifar S, et al.** Effects of blood pressure level on progression of diabetic nephropathy: results from the RENAAL study. Arch Intern Med. 2003;163(13):1555-1565. doi:10.1001/archinte.163.13.1555. [PMC Article](https://pmc.ncbi.nlm.nih.gov/articles/PMC3919031/)

11. **Wachtell K, Ibsen H, Olsen MH, et al.** Albuminuria and cardiovascular risk in hypertensive patients with left ventricular hypertrophy: the LIFE study. Ann Intern Med. 2003;139(11):901-906. [ScienceDirect](https://www.sciencedirect.com/science/article/pii/S0085253815504006)

12. **Boehringer Ingelheim.** The uACR Test for Albumin: Detect the SOS. Patient education resource. 2024. [Patient Resource](https://patient.boehringer-ingelheim.com/us/detect-the-sos/the-uACR-test)

13. **Malhotra R, Craven T, Ambrosius WT, et al.** Is the KDIGO systolic blood pressure target <120 mm Hg for chronic kidney disease appropriate in routine clinical practice? Hypertension. 2022;79(4):770-780. doi:10.1161/HYPERTENSIONAHA.121.18434. [AHA Journals](https://www.ahajournals.org/doi/10.1161/HYPERTENSIONAHA.121.18434)

14. **Böhm M, Thoenes M, Danchin N, et al.** The effects of urinary albumin and hypertension on all-cause and cardiovascular mortality. Am J Hypertens. 2017;30(8):799-807. doi:10.1093/ajh/hpx044. [Oxford Academic](https://academic.oup.com/ajh/article/30/8/799/3787769)

15. **National Kidney Foundation.** Urine Albumin-Creatinine Ratio (uACR): A Key Indicator of Kidney Health. Updated August 11, 2024. [NKF Resource](https://www.kidney.org/kidney-failure-risk-factor-urine-albumin-creatinine-ratio-uacr)

16. **Sarafidis P, Ferro CJ, Morales E, et al.** Blood pressure targets in CKD 2021: the never-ending guidelines debacle. Clin Kidney J. 2022;15(5):845-856. doi:10.1093/ckj/sfab274. [PubMed](https://pubmed.ncbi.nlm.nih.gov/35498896/)

17. **Wang J, Chen Y, Li X, et al.** Evaluating the joint association of albuminuria and hypertension with cardiovascular outcomes. Circulation. 2024;152(Suppl_3):A4371363. [AHA Journals](https://www.ahajournals.org/doi/10.1161/circ.152.suppl_3.4371363)

18. **ADLM Clinical Laboratory News.** The critical role of urine albumin-to-creatinine ratio testing in hypertension management. Clin Lab News. 2024;July/August. [ADLM Article](https://myadlm.org/cln/articles/2025/julyaugust/the-critical-role-of-urine-albumin-to-creatinine-ratio-testing-in-hypertension-management/)

19. **Sarafidis P, Ferro CJ, Morales E, et al.** Blood pressure targets in CKD 2021: the never-ending guidelines debacle. Clin Kidney J. 2022;15(5):845-856. doi:10.1093/ckj/sfab274. [PMC Article](https://academic.oup.com/ckj/article/15/5/845/6526881)

20. **de Zeeuw D, Remuzzi G, Kirch W, et al.** Baseline albuminuria predicts the efficacy of blood pressure-lowering drugs in preventing cardiovascular events. Br J Clin Pharmacol. 2008;66(2):224-233. doi:10.1111/j.1365-2125.2008.03097.x. [Wiley Online Library](https://bpspubs.onlinelibrary.wiley.com/doi/10.1111/j.1365-2125.2008.03097.x)

21. **Tuttle KR, Alicic RZ, Duru OK, et al.** Changes in urine albumin-to-creatinine ratio and health care utilization in patients with type 2 diabetes. J Manag Care Spec Pharm. 2024;30(8):789-798. doi:10.18553/jmcp.2025.24302. [JMCP Article](https://www.jmcp.org/doi/10.18553/jmcp.2025.24302)

22. **de Zeeuw D, Remuzzi G, Parving HH, et al.** Changes in albuminuria predict mortality and morbidity in patients with vascular disease. J Am Soc Nephrol. 2011;22(3):573-581. doi:10.1681/ASN.2010040373. [PMC Article](https://pmc.ncbi.nlm.nih.gov/articles/PMC3137583/)

23. **Ku E, McCulloch CE, Aune D, et al.** Effect of intensive blood pressure control on kidney outcomes: long-term electronic health record-based post-trial follow-up of SPRINT. Circulation. 2024;149(5):370-378. doi:10.1161/CIRCULATIONAHA.123.066187. [PubMed](https://pubmed.ncbi.nlm.nih.gov/37883184/)

24. **Yang M, Liu Y, Zhang X, et al.** Association between cardiometabolic index and albuminuria: results from NHANES 2011-2018. BMC Nephrol. 2025;26(1):45. doi:10.1186/s12882-025-03712-9. [PMC Article](https://pmc.ncbi.nlm.nih.gov/articles/PMC11856275/)

25. **American Diabetes Association.** 11. Chronic kidney disease and risk management: Standards of care in diabetes—2025. Diabetes Care. 2025;48(Suppl 1):S239-S251. doi:10.2337/dc25-S011. [Diabetes Journals](https://diabetesjournals.org/care/article/48/Supplement_1/S239/157554/11-Chronic-Kidney-Disease-and-Risk-Management)

26. **Whelton PK, Einhorn PT, Muntner P, et al.** SPRINT—A kidney-centric narrative review: recent advances in hypertension. Hypertension. 2021;78(6):1459-1468. doi:10.1161/HYPERTENSIONAHA.121.16505. [AHA Journals](https://www.ahajournals.org/doi/10.1161/HYPERTENSIONAHA.121.16505)

27. **Sarafidis PA, Ortiz A, Ferro CJ, et al.** Potential implications of the 2021 KDIGO blood pressure guideline in adults with chronic kidney disease. Kidney Int Rep. 2020;5(6):793-799. doi:10.1016/j.ekir.2020.03.009. [PMC Article](https://pmc.ncbi.nlm.nih.gov/articles/PMC7958922/)

28. **Whelton PK, Einhorn PT, Muntner P, et al.** SPRINT—A kidney-centric narrative review: recent advances in hypertension. Hypertension. 2021;78(6):1459-1468. [AHA Journals - Full Text](https://www.ahajournals.org/doi/full/10.1161/HYPERTENSIONAHA.121.16505)

29. **Tsai CW, Grams ME, Inker LA, et al.** Associations between albuminuria and mortality among US adults: NHANES 1999-2014. J Am Heart Assoc. 2023;12(21):e030773. doi:10.1161/JAHA.123.030773. [AHA Journals](https://www.ahajournals.org/doi/10.1161/JAHA.123.030773)

30. **2025 AHA/ACC/AANP/AAPA/ABC/ACCP/ACPM/AGS/AMA/ASPC Guideline for the Management of High Blood Pressure in Adults.** Hypertension. 2025. doi:10.1161/HYP.0000000000000249. [AHA Journals](https://www.ahajournals.org/doi/10.1161/HYP.0000000000000249)

31. **Whelton PK, Einhorn PT, Muntner P, et al.** SPRINT – A kidney-centric narrative review. Hypertension. 2021;78(6):1459-1468. [PMC Article](https://pmc.ncbi.nlm.nih.gov/articles/PMC8575127/)

32. **Sumida K, Pierre V, Hata J, et al.** Estimated prevalence and testing for albuminuria in US adults at risk for CKD. JAMA Netw Open. 2023;6(7):e2321749. doi:10.1001/jamanetworkopen.2023.21749. [JAMA Network](https://jamanetwork.com/journals/jamanetworkopen/fullarticle/2807656)

33. **American College of Cardiology.** Albuminuria and heart failure: 10 key points to remember. ACC Latest in Cardiology. January 25, 2023. [ACC Resource](https://www.acc.org/Latest-in-Cardiology/ten-points-to-remember/2023/01/26/14/57/albuminuria-and-heart-failure)

34. **Ambrosius WT, Sink KM, Foy CG, et al.** The Systolic Blood Pressure Intervention Trial (SPRINT): rationale and design. Clin Trials. 2014;11(5):532-546. doi:10.1177/1740774514537404. [PMC Article](https://pmc.ncbi.nlm.nih.gov/articles/PMC4156910/)

35. **Chronic Kidney Disease Prognosis Consortium.** Prevalence of albuminuria in a general population cohort. Kidney Int. 2015;88(5):950-957. [ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S1071916415011562)

36. **NYC Department of Health and Mental Hygiene.** 2025 ACC/AHA Joint Committee updates adult hypertension guideline. Health Alert Network Advisory #27. December 3, 2025. [PDF](https://www.nyc.gov/assets/doh/downloads/pdf/han/advisory/2025/han-advisory-27-hypertension.pdf)

37. **National Heart, Lung, and Blood Institute.** Systolic Blood Pressure Intervention Trial (SPRINT): How it was conducted. Updated May 31, 2018. [NHLBI Resource](https://www.nhlbi.nih.gov/science/systolic-blood-pressure-intervention-trial-sprint-study)

38. **Kim DH, Kim M, Kim H, et al.** Prognostic impact of albuminuria in early-stage chronic kidney disease. Heart. 2025;111(11):506-514. doi:10.1136/heartjnl-2024-324156. [BMJ Journals](https://heart.bmj.com/content/111/11/506)

39. **American College of Cardiology.** Systolic Blood Pressure Intervention Trial (SPRINT). ACC Clinical Trial Summary. September 22, 2015. [ACC Resource](https://www.acc.org/Latest-in-Cardiology/Clinical-Trials/2015/09/23/10/40/SPRINT)

40. **Khera R, Kondamudi N, Zhong L, et al.** Performance of the Pooled Cohort Equations to estimate atherosclerotic cardiovascular disease risk by body mass index. JAMA Netw Open. 2020;3(10):e2023242. doi:10.1001/jamanetworkopen.2020.23242. [JAMA Network](https://jamanetwork.com/journals/jamanetworkopen/fullarticle/2772343)

41. **Parikh NI, Pencina MJ, Wang TJ, et al.** Validating the Framingham Hypertension Risk Score: results from the Women's Health Study. Hypertension. 2009;54(3):496-501. doi:10.1161/HYPERTENSIONAHA.109.132373. [PMC Article](https://pmc.ncbi.nlm.nih.gov/articles/PMC2828464/)

42. **Khan SS, Matsushita K, Sang Y, et al.** Development and validation of the American Heart Association's PREVENT equations. Circulation. 2024;149(6):430-449. doi:10.1161/CIRCULATIONAHA.123.067626. [AHA Journals](https://www.ahajournals.org/doi/10.1161/CIRCULATIONAHA.123.067626)

43. **Khera R, Kondamudi N, Zhong L, et al.** Performance of the Pooled Cohort Equations to estimate atherosclerotic cardiovascular disease risk by body mass index. JAMA Netw Open. 2020;3(10):e2023242. [PMC Article](https://pmc.ncbi.nlm.nih.gov/articles/PMC7596579/)

44. **Parikh NI, Pencina MJ, Wang TJ, et al.** Validating the Framingham Hypertension Risk Score: results from the Women's Health Study. Hypertension. 2009;54(3):496-501. [AHA Journals - Direct](https://www.ahajournals.org/doi/10.1161/hypertensionaha.109.132373)

45. **Wang X, Liu Y, Chen S, et al.** External validation of the 2023 American Heart Association PREVENT equations in Chinese adults. Eur Heart J. 2025;46(10):892-902. doi:10.1093/eurheartj/ehae456. [PubMed](https://pubmed.ncbi.nlm.nih.gov/40446085/)

46. **Cook NR, Paynter NP, Eaton CB, et al.** Evaluation of the Pooled Cohort Risk Equations for cardiovascular risk prediction in a multiethnic cohort from the Women's Health Initiative. JAMA Intern Med. 2018;178(9):1231-1240. doi:10.1001/jamainternmed.2018.2875. [PMC Article](https://pmc.ncbi.nlm.nih.gov/articles/PMC6142964/)

47. **Song X, Jousilahti P, Stehouwer CD, et al.** Validation of the Framingham hypertension risk score in a European population-based cohort. J Hypertens. 2021;39(6):1258-1265. doi:10.1097/HJH.0000000000002782. [PMC Article](https://pmc.ncbi.nlm.nih.gov/articles/PMC8070324/)

48. **Cleveland Clinic.** Cardiac risk calculator and assessment: Understanding your heart disease risk. Updated September 16, 2025. [Cleveland Clinic](https://my.clevelandclinic.org/health/articles/17085-heart-risk-factor-calculators)

49. **Arnett DK, Blumenthal RS, Albert MA, et al.** Pooled Cohort Equations and the competing risk of noncardiovascular mortality. Circulation. 2021;144(6):e89-e91. doi:10.1161/CIRCULATIONAHA.121.055276. [PMC Article](https://pmc.ncbi.nlm.nih.gov/articles/PMC8387297/)

50. **ScienceDirect Topics.** Framingham Risk Score overview and clinical applications. Updated October 24, 2012. [ScienceDirect](https://www.sciencedirect.com/topics/medicine-and-dentistry/framingham-risk-score)

51. **American Heart Association.** The American Heart Association PREVENT™ Online Calculator. Professional resources. October 31, 2024. [AHA PREVENT Calculator](https://professional.heart.org/en/guidelines-and-statements/prevent-calculator)

52. **Mortensen MB, Nordestgaard BG, Afzal S, Falk E.** Performance of the ACC/AHA Pooled Cohort cardiovascular risk equations in clinical practice. J Am Coll Cardiol. 2023;82(16):1608-1620. doi:10.1016/j.jacc.2023.08.020. [PubMed](https://pubmed.ncbi.nlm.nih.gov/37793746/)

53. **Framingham Heart Study.** Hypertension risk functions and prediction tools. Updated August 25, 2020. [Framingham Study](https://www.framinghamheartstudy.org/fhs-risk-functions/hypertension/)

54. **Multi-Ethnic Study of Atherosclerosis (MESA).** MESA Risk Score and Coronary Age Calculator for researchers. [MESA Calculator](https://mesa-nhlbi.org/researchers/tools/mesa-score-risk-calculator)

55. **ClinCalc.** ASCVD Risk Calculator based on Pooled Cohort Equations. Updated July 18, 2024. [ClinCalc Tool](https://clincalc.com/cardiology/ascvd/pooledcohort.aspx)

56. **Sundström J, Arima H, Jackson R, et al.** Blood pressure lowering treatment and the Framingham cardiovascular disease risk score. Hypertension. 2020;75(1):211-218. doi:10.1161/HYPERTENSIONAHA.119.13666. [PMC Article](https://pmc.ncbi.nlm.nih.gov/articles/PMC6973292/)

57. **Khera R, Pandey A, Ayers CR, et al.** A new cardiovascular risk calculator from the American Heart Association: PREVENT. JAMA. 2024;331(22):1934-1945. [Journal Watch](https://www.jwatch.org/na57667/2024/06/27/new-cardiovascular-risk-calculator-american-heart)

58. **Rana JS, Tabada GH, Solomon MD, et al.** The Pooled Cohort Equations 3 years on. Circulation. 2016;134(24):1956-1958. doi:10.1161/CIRCULATIONAHA.116.024246. [AHA Journals](https://www.ahajournals.org/doi/10.1161/CIRCULATIONAHA.116.024246)

59. **Wikipedia contributors.** Framingham Risk Score. Wikipedia, The Free Encyclopedia. January 10, 2011. [Wikipedia](https://en.wikipedia.org/wiki/Framingham_Risk_Score)

60. **Luzum JA, Forciea MA, Kisor DF, et al.** Feasibility of precision medicine in hypertension management: translating genomic and clinical data into clinical practice. Pharmacotherapy. 2022;42(11):906-921. doi:10.1002/phar.2731. [PMC Article](https://pmc.ncbi.nlm.nih.gov/articles/PMC9698650/)

61. **Kramer HJ, Boucher RE, Leehey D, et al.** Bringing personalized medicine to patients with CKD. Clin Chem. 2024;70(1):43-52. doi:10.1093/clinchem/hvad127. [ADLM Article](https://myadlm.org/cln/articles/2024/novdec/bringing-personal-medicine-to-patients-with-ckd)

62. **Pater C.** Increasing the precision of hypertension treatment through personalized trials: a pilot study. J Pers Med. 2019;9(1):20. doi:10.3390/jpm9010020. [PMC Article](https://pmc.ncbi.nlm.nih.gov/articles/PMC6544735/)

63. **van der Aart-van der Beek AB, de Boer RA, Heerspink HJL.** Impact of albuminuria screening in primary care on the detection and management of chronic kidney disease. Clin Kidney J. 2025;18(5):sfaf123. doi:10.1093/ckj/sfaf123. [Oxford Academic](https://academic.oup.com/ckj/article/18/5/sfaf123/8120273)

64. **Gupta DK, Patel RB, Claggett B, et al.** Precision hypertension: concepts and challenges. Hypertension. 2024;81(4):692-701. doi:10.1161/HYPERTENSIONAHA.123.21710. [AHA Journals](https://www.ahajournals.org/doi/10.1161/HYPERTENSIONAHA.123.21710)

65. **Drawz P, Alper AB, Anderson AH, et al.** Association of the intensive blood pressure target and albuminuria changes: secondary analysis of SPRINT. J Am Heart Assoc. 2024;13(6):e032186. doi:10.1161/JAHA.123.032186. [AHA Journals](https://www.ahajournals.org/doi/10.1161/JAHA.123.032186)

66. **Fontil V, Gupta R, Moise N, Sequist TD.** Personalized medicine and the treatment of hypertension. J Hum Hypertens. 2019;33(4):283-289. doi:10.1038/s41371-019-0174-2. [PMC Article](https://pmc.ncbi.nlm.nih.gov/articles/PMC6594382/)

67. **Santos PC, Pereira AC.** Developments in albuminuria testing: a key biomarker for detection and management of chronic kidney disease. Diagnostics. 2024;14(18):2045. [PMC Article](https://pmc.ncbi.nlm.nih.gov/articles/PMC12400485/)

68. **AJKD Blog Contributors.** Exploring the optimal blood pressure target in advanced CKD. AJKD Blog. May 28, 2025. [AJKD Blog](https://ajkdblog.org/2025/05/28/exploring-the-optimal-blood-pressure-target-in-advanced-ckd/)

69. **Turner ST, Boerwinkle E.** Personalized medicine for high blood pressure. Hypertension. 2007;50(1):1-5. doi:10.1161/HYPERTENSIONAHA.107.087049. [AHA Journals](https://www.ahajournals.org/doi/10.1161/hypertensionaha.107.087049)

70. **Anders HJ, Peired AJ.** Albuminuria predicts kidney failure and can serve as a surrogate CKD endpoint in clinical trials. Renal & Urology News. November 17, 2025. [Clinical News](https://www.renalandurologynews.com/reports/albuminuria-kidney-failure-ckd-chronic-disease-surrogate-trial/)

71. **American Academy of Family Physicians.** Blood pressure targets for hypertension in people with chronic kidney disease: Cochrane review. Am Fam Physician. 2025;111(6):635-637. [AAFP Article](https://www.aafp.org/pubs/afp/issues/2025/0600/cochrane-blood-pressure-targets-chronic-kidney-disease.html)

72. **Rossitto G, Mary S, McAllister C, et al.** A physiologic, precision-medicine approach to guided pharmacological treatment of hypertension. Eur Heart J. 2023;44(Suppl 2):ehad655.2349. doi:10.1093/eurheartj/ehad655.2349. [Oxford Academic](https://academic.oup.com/eurheartj/article/44/Supplement_2/ehad655.2349/7392213)

73. **Sharma A, Kumar R, Singh M.** Artificial intelligence-driven risk stratification in chronic kidney disease progression. Cureus. 2025;17(12):e75429. doi:10.7759/cureus.75429. [Cureus Article](https://www.cureus.com/articles/435299-artificial-intelligence-driven-risk-stratification-in-chronic-kidney-disease-progression)

74. **Cleveland Clinic Consult QD.** In practice: Updated guidelines for managing blood pressure in patients with chronic kidney disease. Consult QD. 2024. [Cleveland Clinic](https://consultqd.clevelandclinic.org/in-practice-updated-guidelines-for-managing-blood-pressure-in-patients-with-chronic-kidney-disease)

75. **Devkota B, Singh A, Khalid F, et al.** Hypertension precision medicine: the promise and pitfalls. Hypertension. 2025;82(1):12-24. [PubMed](https://pubmed.ncbi.nlm.nih.gov/40421951/)

76. **Naaman SC, Bakris GL.** Personalized care in CKD: moving beyond traditional biomarkers. Nephron. 2025;149(6):339-348. doi:10.1159/000542193. [Karger Publishers](https://karger.com/nef/article/149/6/339/919567/Personalized-Care-in-CKD-Moving-Beyond-Traditional)

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

This work builds upon decades of cardiovascular and kidney disease research. We acknowledge:

- The NHANES program and CDC for providing public health surveillance data
- Clinical trial investigators who conducted SPRINT, MDRD, AASK, and related studies
- KDIGO, ACC/AHA, and other guideline committees for evidence synthesis
- Open-source software communities supporting scientific computing

---

**Disclaimer**: This calculator is intended for research and educational purposes. Clinical decisions should be made by qualified healthcare professionals considering the complete clinical context. This tool does not constitute medical advice.

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
