# Dataset Inventory

This document tracks every dataset used in the project. Update this file whenever a new file is added to `data/raw/`.

---

## Template

| Field                                | Value |
| ------------------------------------ | ----- |
| **Dataset name**               |       |
| **Source / URL**               |       |
| **Date downloaded**            |       |
| **Time period covered**        |       |
| **Geographic coverage**        |       |
| **License**                    |       |
| **File name in `data/raw/`** |       |
| **Key columns**                |       |
| **Known limitations**          |       |

---

## Datasets

### 1. UN Prisons & Prisoners

| Field                                | Value                                         |
| ------------------------------------ | --------------------------------------------- |
| **Dataset name**               | UN Prisons & Prisoners                        |
| **Source / URL**               | https://data.unodc.org/datareport/prison-held |
| **Date downloaded**            | 07/04/2026                                    |
| **Time period covered**        | 1998-2024                                     |
| **Geographic coverage**        | World                                         |
| **License**                    | TBD                                           |
| **File name in `data/raw/`** | data_cts_prisons_and_prisoners.xlsx           |
| **Key columns**                | TBD                                           |
| **Known limitations**          | TBD                                           |

---

### 2. Eurostat — Prison Statistics

| Field                                | Value                                                                                       |
| ------------------------------------ | ------------------------------------------------------------------------------------------- |
| **Dataset name**               | Eurostat Prison Statistics                                                                  |
| **Source / URL**               | https://ec.europa.eu/eurostat/databrowser/view/crim_pris_age__custom_20872132/default/table |
| **Date downloaded**            | 07/04/2026                                                                                  |
| **Time period covered**        | 2014-2023                                                                                   |
| **Geographic coverage**        | EU-27 member states                                                                         |
| **License**                    | Eurostat standard re-use policy                                                             |
| **File name in `data/raw/`** | crim_pris_age__custom_20872132.csv                                                          |
| **Key columns**                | Country, Year, Total prisoners, Female prisoners, Female share (%)                          |
| **Known limitations**          | Not all countries report every year; definitions of "prisoner" may vary                     |

---

### 3. Human Development Reports - EU Gender Inequality Index

| Field                                | Value                                                        |
| ------------------------------------ | ------------------------------------------------------------ |
| **Dataset name**               | EU Gender Inequality Index                                   |
| **Source / URL**               | https://hdr.undp.org/data-center/documentation-and-downloads |
| **Date downloaded**            | 07/04/2026                                                   |
| **Time period covered**        | 1998-2023                                                    |
| **Geographic coverage**        | Europe And Cerntral Asia                                     |
| **License**                    | -                                                            |
| **File name in `data/raw/`** | hdr-data.xlsx                                                |
| **Key columns**                | year; value                                                  |
| **Known limitations**          | TBD                                                          |

---

### 4. EUROSTAT - Prison statistics

| Field                                | Value                                                                                            |
| ------------------------------------ | ------------------------------------------------------------------------------------------------ |
| **Dataset name**               | Prison Statistics                                                                                |
| **Source / URL**               | https://ec.europa.eu/eurostat/statistics-explained/index.php?title=Prison_statistics#Data_source |
| **Date downloaded**            | 07/04/2026                                                                                       |
| **Time period covered**        | 1993-2023                                                                                        |
| **Geographic coverage**        | EU                                                                                               |
| **License**                    |                                                                                                  |
| **File name in `data/raw/`** | 2025_prison_statistics_2.xlsx                                                                    |
| **Key columns**                |                                                                                                  |
| **Known limitations**          | Missing Value for some years in different perspective                                            |
