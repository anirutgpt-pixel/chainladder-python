# ตรวจ CSV กับ `5_Friedland.pdf`

`y` หมายถึงพบชุดข้อมูล/ตัวอย่างที่สอดคล้องกันใน PDF; `n` หมายถึงไม่พบชุดข้อมูลนั้นใน PDF ตัวเลขใน PDF บางตารางแสดงเป็นหน่วย `$000` หรือปัดเศษ จึงพิจารณาร่วมกับชื่อชุดข้อมูลและหัวตาราง ไม่ได้เทียบข้อความดิบแบบ byte-to-byte

| csv | 5_Friedland | ck_result |
|---|---|:---:|
| `friedland_auto_bi_insurer.csv` | Auto BI Insurer — ตัวอย่างการประเมินสินไหม | y |
| `friedland_auto_freq_sev.csv` | Chapter 11 — Frequency-Severity (Auto / XYZ Auto BI) | y |
| `friedland_auto_salsub.csv` | Chapter 14 — Recoveries: Salvage and Subrogation | y |
| `friedland_autoprop.csv` | ALAE / Auto Property Damage example data | y |
| `friedland_berq_sher_auto.csv` | Berq-Sher Auto BI Insurer | y |
| `friedland_dc_insurer.csv` | DC Insurer — development example | y |
| `friedland_gl_insurer.csv` | GL Insurer — Frequency-Severity Approach 3 | y |
| `friedland_gl_self_insurer.csv` | GL Self-Insurer — step-by-step example | y |
| `friedland_med_mal.csv` | Berq-Sher Med Mal Insurer | y |
| `friedland_qs.csv` | Chapter 14 — Quota Share Reinsurance | y |
| `friedland_us_auto.csv` | U.S. Auto — Steady-State / Changing Product Mix | y |
| `friedland_us_industry_auto.csv` | U.S. Industry Auto | y |
| `friedland_us_industry_auto_case.csv` | U.S. Industry Auto — case outstanding / paid claims | y |
| `friedland_uspp.csv` | U.S. PP Auto scenarios | y |
| `friedland_uspp_auto_increasing_case.csv` | U.S. PP Auto — Increasing Case Outstanding Strength | y |
| `friedland_uspp_auto_increasing_claim.csv` | U.S. PP Auto — Increasing Claim Ratios | y |
| `friedland_uspp_auto_steady_state.csv` | U.S. PP Auto — Steady-State | y |
| `friedland_uspp_increasing_claim_case.csv` | U.S. PP Auto — Increasing Claim Ratios and Case Outstanding Strength | y |
| `friedland_wc_self_insurer.csv` | WC Self-Insurer — Frequency-Severity Approach 2 | y |
| `friedland_xol.csv` | Chapter 14 — Excess-of-Loss Reinsurance | y |
| `friedland_xyz_auto_bi.csv` | XYZ Insurer — Auto BI development exhibits | y |
| `quarterly.csv` | ไม่พบชุดข้อมูล Quarterly ใน PDF | n |

ตรวจเฉพาะ CSV; ไม่รวมไฟล์ JSON ที่อยู่ในรายการต้นทาง
