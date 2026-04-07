# Design Decisions

This document records significant choices made during the visual design and analytical process, including the rationale behind each decision.

> **Principle:** Every chart and interaction design choice should be justifiable in terms of what it helps the audience understand, and should be scrutinized for potential white-hat / black-hat implications.

---

## Template for Entries

**Decision:** _Short description of the choice made._  
**Alternatives considered:** _What else was considered?_  
**Rationale:** _Why was this option chosen?_  
**White-hat check:** _Does this choice present the data fairly? Any risk of misleading the audience?_  
**Date / Author:** TBD

---

## Decisions Log

### VD-01 — Geographic unit of analysis

**Decision:** Analyze at the country level (EU-27).  
**Alternatives considered:** Regional (NUTS-2), sub-national.  
**Rationale:** Both the EIGE Gender Equality Index and Eurostat prison statistics are available at the country level. Sub-national breakdowns are not consistently available across all EU member states.  
**White-hat check:** Country-level aggregation may obscure within-country variation. This limitation is explicitly acknowledged in the report.  
**Date / Author:** TBD

---

### VD-02 — Choice of primary indicator for incarceration

**Decision:** TBD (e.g., female share of total prison population vs. female incarceration rate per 100,000 population)  
**Alternatives considered:** Absolute count, share of total, rate per 100,000.  
**Rationale:** TBD  
**White-hat check:** TBD  
**Date / Author:** TBD

---

### VD-03 — Color palette for choropleth maps

**Decision:** TBD  
**Alternatives considered:** Sequential, diverging, qualitative palettes.  
**Rationale:** TBD  
**White-hat check:** Ensure color scale is perceptually uniform and accessible to color-blind users (use colorblind-safe palettes).  
**Date / Author:** TBD

---

### VD-04 — Handling of missing data in visualizations

**Decision:** TBD  
**Alternatives considered:** Imputation, exclusion, explicit "no data" encoding.  
**Rationale:** TBD  
**White-hat check:** TBD  
**Date / Author:** TBD

---

## White-Hat vs Black-Hat Reflection

_To be completed as part of the final report. Document any temptations to use manipulative techniques and how they were avoided._

| Potential manipulation | Why avoided |
|------------------------|-------------|
| Truncated Y-axis to exaggerate differences | Axes start at zero (or are clearly annotated when not) |
| Cherry-picked time window | Full available time range is shown; any restriction is justified |
| Misleading color scale | Perceptually uniform palettes used; scale annotated clearly |
| Unlabeled outliers | All outlier countries are labeled and discussed in the text |

---

_Add new entries to the Decisions Log as choices are made throughout the project._
