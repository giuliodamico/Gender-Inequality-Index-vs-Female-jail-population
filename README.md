# Gender Inequality Index vs Female Jail Population

> **Visual Analytics — University Group Project**

A data visualization project exploring the relationship between gender inequality and female incarceration across European Union countries.

---

## Research Question

> *"How do changes in gender inequality relate to cross-country differences in female incarceration in Europe?"*

---

## Project Overview

This project investigates whether—and to what extent—a country's level of gender inequality is associated with the share or rate of female prisoners. The analysis focuses exclusively on **European Union member states**, with an additional grouping by macro-region:

- **Northern Europe**
- **Eastern Europe**
- **Central-Southern Europe**

The project combines quantitative data analysis (Python), interactive dashboards (Tableau / Power BI), a small original interactive feature (JavaScript), and a public-facing narrative page (WordPress).

---

## Data Sources

| Source | Description | Format |
|--------|-------------|--------|
| [EIGE Gender Equality Index](https://eige.europa.eu/gender-equality-index) | Gender equality scores and sub-domain indicators for EU countries | CSV / API |
| [Eurostat — Prison Statistics](https://ec.europa.eu/eurostat/web/crime/data/database) | Number of prisoners by sex, country, and year | CSV |
| Additional EU-level contextual variables (TBD) | e.g., GDP, unemployment by sex, education attainment | CSV |

> **Raw data must never be modified.** All transformations are performed programmatically and saved to `data/interim/` or `data/processed/`.

---

## Repository Structure

```
.
├── data/
│   ├── raw/          # Original, unmodified source files (read-only)
│   ├── interim/      # Intermediate files produced during cleaning/merging
│   └── processed/    # Final analysis-ready datasets
│
├── notebooks/        # Jupyter notebooks for exploration and communication
│   ├── 01_data_understanding.ipynb
│   ├── 02_cleaning_integration.ipynb
│   ├── 03_eda.ipynb
│   └── 04_visual_support.ipynb
│
├── src/              # Reusable Python modules
│   ├── data_cleaning.py
│   ├── integration.py
│   ├── eda.py
│   └── utils.py
│
├── visuals/          # Exported static charts, maps, and design assets
├── website/          # WordPress export / HTML prototypes
├── report/           # Final paper and supporting documents
│
├── docs/             # Project documentation
│   ├── dataset_inventory.md
│   ├── task_analysis.md
│   ├── design_decisions.md
│   ├── meeting_notes.md
│   └── project_timeline.md
│
├── .gitignore
├── requirements.txt
└── README.md
```

---

## Setup Instructions

### Prerequisites

- Python 3.10 or higher
- [pip](https://pip.pypa.io/) or [conda](https://docs.conda.io/)

### Install dependencies

```bash
# Clone the repository
git clone https://github.com/giuliodamico/Gender-Inequality-Index-vs-Female-jail-population.git
cd Gender-Inequality-Index-vs-Female-jail-population

# (Recommended) Create and activate a virtual environment
python -m venv .venv
source .venv/bin/activate        # Linux / macOS
# .venv\Scripts\activate         # Windows PowerShell

# Install Python dependencies
pip install -r requirements.txt
```

### Launch Jupyter

```bash
jupyter lab
```

---

## Workflow

### Branch Strategy

| Branch | Purpose |
|--------|---------|
| `main` | Stable, reviewed code only |
| `develop` | Integration branch for ongoing work |
| `feature/<short-description>` | Individual features or analysis tasks |
| `fix/<short-description>` | Bug fixes |

**Standard flow:**
1. Branch off `develop`: `git checkout -b feature/eda-prison-data`
2. Make small, focused commits.
3. Open a Pull Request into `develop` with a short description.
4. At least one other team member reviews before merging.
5. `develop` is merged into `main` at project milestones.

### Commit Message Conventions

Follow the [Conventional Commits](https://www.conventionalcommits.org/) style:

```
<type>(<scope>): <short summary>

Types: feat | fix | data | docs | style | refactor | test | chore
Examples:
  feat(eda): add scatter plot for GII vs incarceration rate
  data(raw): add Eurostat prison CSV 2015-2022
  docs(design): update design decisions after peer review
  fix(cleaning): handle missing values in EIGE 2020 dataset
```

### Data Management

- **`data/raw/`** — Place original downloaded files here. **Never edit these.**
- **`data/interim/`** — Intermediate outputs (merged, partially cleaned).
- **`data/processed/`** — Final, analysis-ready files used in notebooks and dashboards.
- Document every dataset in `docs/dataset_inventory.md` (source, date downloaded, license, columns).

### Design Choices

- Document every significant visualization decision in `docs/design_decisions.md`.
- Justify choice of chart types, color palettes, and aggregation methods.
- Include a section on **white-hat vs black-hat** design considerations.

---

## Reproducibility

- All data transformations are scripted in `src/` and demonstrated in `notebooks/`.
- Random seeds (if used) must be set explicitly and documented.
- The `requirements.txt` pins exact package versions.
- To reproduce the full analysis pipeline, run the notebooks in order (01 → 04).

---

## Team Roles

| Role | Responsibilities |
|------|-----------------|
| **Data Engineer** | Data collection, cleaning, integration (`src/`, `data/`) |
| **Analyst** | EDA, statistical summaries, insight generation (`notebooks/`) |
| **Visualization Designer** | Charts, dashboard layout, color/typography choices (`visuals/`) |
| **Web Developer** | JavaScript interactive feature, WordPress page (`website/`) |
| **Reporter** | Written report, design rationale, white-hat reflection (`report/`, `docs/`) |

> Roles may overlap; update this section as responsibilities evolve.

---

## Limitations and Bias

- **Data availability**: Not all EU countries report prison data consistently; missing values may bias cross-country comparisons.
- **Temporal alignment**: The EIGE index and Eurostat prison statistics may cover different reference years; merging requires careful temporal matching.
- **Ecological fallacy**: Relationships observed at the country level do not necessarily apply to individuals.
- **Selection of indicators**: The choice of which gender inequality sub-dimensions to include affects the conclusions; this choice is documented in `docs/design_decisions.md`.
- **Aggregation**: Grouping countries into Northern / Eastern / Central-Southern Europe is a simplification; results may vary with different groupings.
- **White-hat commitment**: All design choices aim to present data honestly. Manipulative techniques (misleading axes, cherry-picked time windows, etc.) are explicitly avoided and discussed in the report.

---

## License

This project is produced for academic purposes. Data sources retain their original licenses (see `docs/dataset_inventory.md`).
