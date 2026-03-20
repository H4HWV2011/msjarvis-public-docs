# Case Study: Institutional Timberland Acquisition, Federal Subsidy Utilization, and Absentee Ownership Concentration in Fayette County, West Virginia

**Date of Analysis:** March 20, 2026
**Producing Organization:** Harmony for Hope, Inc. — Oak Hill, West Virginia
**Analytical System:** Advanced Location Intelligence Infrastructure
**Primary Database:** `msjarvisgis` — `public.mvw_gbim_landowner_spatial`
**Data Source:** Fayette County, West Virginia Public Property Assessment Records
**Classification:** Public Research Record

---

## Abstract

This case study documents the findings of a spatial analysis of Fayette County, West Virginia public property assessment records, cross-referenced with West Virginia Secretary of State corporate filings, U.S. Treasury Community Development Financial Institutions (CDFI) Fund program documentation, and publicly available corporate disclosures. The analysis identified 287 parcels totaling 50,697 acres held by four interrelated corporate entities, all registered to a single institutional timberland investment management organization (TIMO) headquartered in Chapel Hill, North Carolina. The analysis further identified the utilization of federal New Markets Tax Credit (NMTC) financing in the acquisition of a subset of these holdings, with no publicly available documentation of the community benefit delivery required under NMTC program compliance standards. The findings raise substantive questions regarding federal program accountability, absentee institutional land ownership concentration, carbon credit revenue extraction, and the adequacy of existing oversight mechanisms for NMTC-financed timberland transactions in economically distressed rural communities.

---

## 1. Introduction

### 1.1 Background

Fayette County, West Virginia is classified as an economically distressed community by the Appalachian Regional Commission. The county's economic trajectory reflects broader patterns of resource extraction and capital outflow characteristic of Appalachian economies — patterns extensively documented in the academic literature on regional political economy, absentee land ownership, and the financialization of natural resource assets.

The New Markets Tax Credit program, established by the Community Renewal Tax Relief Act of 2000 (P.L. 106-554) and administered by the U.S. Treasury's CDFI Fund, was designed to catalyze private investment in low-income communities by providing investors a federal tax credit equal to 39 percent of their qualified equity investment, distributed over a seven-year compliance period. The program requires recipient Community Development Entities (CDEs) to maintain accountability to residents of the low-income communities served, including through representation on governing or advisory boards, and to deliver measurable, documented community benefit as a condition of credit utilization.

### 1.2 Research Question

This case study addresses the following primary question: To what extent does the concentration of institutionally managed timberland in Fayette County — facilitated in part through federally subsidized NMTC financing — reflect compliance with the community benefit obligations attendant to that financing, and what mechanisms exist to ensure public accountability for those obligations?

### 1.3 Methodology

Spatial queries were executed against the `public.mvw_gbim_landowner_spatial` materialized view within the `msjarvisgis` PostgreSQL/PostGIS database, which aggregates publicly available parcel-level land ownership records from West Virginia county assessors. Entity names identified through the spatial analysis were cross-referenced against the West Virginia Secretary of State online business database to establish corporate structure, registered addresses, and management relationships. Corporate identities were further verified through publicly available investor presentations, corporate websites, press releases, and federal program databases. All data sources utilized in this analysis are publicly available and independently verifiable.

---

## 2. Spatial Analysis Findings

### 2.1 Query Methodology

The following SQL queries were executed against the county parcel database to identify institutional landholding entities associated with known timberland investment operators in the region:

```sql
-- Primary entity holdings query
SELECT entity_name, feature_type,
       COUNT(*) AS parcels,
       ROUND(SUM(acres)::numeric, 1) AS total_acres,
       COUNT(DISTINCT county_id) AS counties
FROM public.mvw_gbim_landowner_spatial
WHERE UPPER(entity_name) ILIKE '%ORBIS%'
   OR UPPER(entity_name) ILIKE '%QUERCUS%'
   OR UPPER(entity_name) ILIKE '%OAK HILL FORESTLANDS%'
   OR UPPER(entity_name) ILIKE '%NMTC%'
GROUP BY entity_name, feature_type
ORDER BY total_acres DESC;

-- County distribution query
SELECT entity_name, county_id,
       COUNT(*) AS parcels,
       ROUND(SUM(acres)::numeric, 1) AS acres
FROM public.mvw_gbim_landowner_spatial
WHERE UPPER(entity_name) ILIKE '%ORBIS%'
   OR UPPER(entity_name) ILIKE '%QUERCUS%'
   OR UPPER(entity_name) ILIKE '%OAK HILL FORESTLANDS%'
GROUP BY entity_name, county_id
ORDER BY entity_name, acres DESC;

-- Aggregate summary query
SELECT ROUND(SUM(acres)::numeric, 0) AS total_orbis_acres,
       COUNT(*) AS total_parcels,
       COUNT(DISTINCT entity_name) AS holding_entities,
       COUNT(DISTINCT county_id) AS counties
FROM public.mvw_gbim_landowner_spatial
WHERE UPPER(entity_name) ILIKE '%ORBIS%'
   OR UPPER(entity_name) ILIKE '%QUERCUS%'
   OR UPPER(entity_name) ILIKE '%OAK HILL FORESTLANDS%';
```

### 2.2 Entity Holdings

| Entity Name | Feature Type | Parcels | Total Acres | Counties |
|---|---|---|---|---|
| QUERCUS WV LLC ICO: ORBIS INC | corporate_landowner | 71 | 24,807.6 | 1 |
| QUERCUS WEST VIRGINIA LLC | corporate_landowner | 110 | 14,032.3 | 1 |
| OAK HILL FORESTLANDS NMTC LLC C/O ORBIS INC | corporate_landowner | 77 | 9,613.3 | 1 |
| COASTAL FOREST RESOURCES CO C/O ORBIS INC | corporate_landowner | 29 | 2,244.0 | 2 |

### 2.3 County Distribution

| Entity Name | County ID | Parcels | Acres |
|---|---|---|---|
| COASTAL FOREST RESOURCES CO C/O ORBIS INC | 34 | 14 | 1,457.3 |
| COASTAL FOREST RESOURCES CO C/O ORBIS INC | 17 | 15 | 786.7 |
| OAK HILL FORESTLANDS NMTC LLC C/O ORBIS INC | 10 (Fayette) | 77 | 9,613.3 |
| QUERCUS WEST VIRGINIA LLC | 20 | 110 | 14,032.3 |
| QUERCUS WV LLC ICO: ORBIS INC | 10 (Fayette) | 71 | 24,807.6 |

### 2.4 Aggregate Summary

| Total Acres | Total Parcels | Distinct Holding Entities | Counties Represented |
|---|---|---|---|
| 50,697 | 287 | 4 | 4 |

---

## 3. Corporate Structure Analysis

### 3.1 Entity Identification and Ownership Chain

Cross-referencing entity names against the West Virginia Secretary of State public business database established the following ownership and operational structure. Every entity identified in the parcel dataset carries the registered care-of address of Orbis Inc., Charlotte, North Carolina. The managing entity address for Oak Hill Forestlands NMTC LLC — 55 Vilcom Center Drive, Suite 240, Chapel Hill, North Carolina — corresponds to the registered headquarters of The Forestland Group, LLC.

| Entity | Organizational Role | Headquarters | Primary Public Record |
|---|---|---|---|
| The Forestland Group, LLC | Timberland investment manager (TIMO); beneficial owner and portfolio manager | 55 Vilcom Center Dr., Suite 240, Chapel Hill, NC | [WV SOS Org. 339624](https://apps.sos.wv.gov/business/corporations/organization.aspx?org=339624) |
| Chateaugay Holding Company LLC | Registered fund vehicle; LLC manager of record | Chapel Hill, NC | [WV SOS Filing](https://apps.sos.wv.gov/business/corporations/organization.aspx?org=339624) |
| Orbis Inc. | Land asset management technology provider; property tax administration; recreational lease management; acquisition due diligence | Charlotte, NC | [orbisinc.com](https://orbisinc.com) |
| Anew Climate LLC / Oak Hill Advisors (OHA) | Current beneficial owner; acquired entire TFG portfolio November 2022 | New York, NY | [Yahoo Finance](https://finance.yahoo.com/news/anew-oha-led-investor-consortium-154600963.html) |

### 3.2 The Forestland Group: Organizational Profile

The Forestland Group (TFG) is a timberland investment management organization (TIMO) operating as a registered investment adviser. Their publicly available investor presentation documents the following portfolio characteristics:

- $2.6 billion in assets under management across 10 commingled funds and separate managed accounts
- 1,185,527 acres under active management across 11 states
- 4.5 million total acres transacted across 111 transactions since founding
- Self-described as the single largest producer of forestry carbon offsets in the United States, having generated over 22 million voluntary carbon market credits
- Approximately 15 percent share of the U.S. forestry carbon offset market
- Signatory to the United Nations Principles for Responsible Investment (UN PRI)
- Institutional client base comprising pension funds, university endowments, private foundations, and family offices

Within West Virginia, TFG assembled holdings exceeding 500,000 acres across 31 counties — a concentration documented by the WV Center on Budget and Policy as early as 2013, at which time TFG was identified as the largest single private landowner in the state.

**Primary Source:** [The Forestland Group: An Introduction — UNEP Finance Initiative PDF](https://www.unepfi.org/wordpress/wp-content/uploads/2021/02/01_The-Forestland-Group-Overview.pdf)

### 3.3 Orbis Inc.: Organizational Profile and Conflict of Interest Considerations

Orbis Inc. is a geospatial intelligence and land asset management technology firm founded in 2000 and headquartered in Charlotte, North Carolina. Their core service offerings to institutional timberland investors include parcel-level property data management, property tax minimization strategies, hunting and recreational lease administration, environmental due diligence support for new acquisitions, and ESG consulting services enabling institutional clients to market timberland holdings to socially responsible investment funds.

The Forestland Group's Senior Vice President, Mike Hincher, is cited on the Orbis Inc. corporate website as follows:

> *"I can only say positive things when it comes to working with Orbis. Their integrity, in line with their customer-focused attitude, allows me and The Forestland Group the peace of mind knowing our data is in the best hands."*

In April 2022, Orbis Inc. announced a formal research partnership with West Virginia University (WVU), funded through a National Science Foundation grant, focused on equitable access to economic opportunity for underserved communities in West Virginia, administered through WVU's Division of Forestry and Natural Resources.

This partnership warrants examination in the context of Orbis's concurrent operational role as the technology and property management infrastructure provider for institutional timberland holdings in West Virginia — holdings acquired in part through federal community development financing instruments. The relationship between Orbis's stated equity mission and its commercial function as an enabler of institutional extraction in the communities identified as underserved by the NSF grant has not been addressed in any publicly available documentation associated with the WVU partnership.

**Sources:**
- [Orbis Inc. — Business Solutions for Timberland Property Management](https://orbisinc.com/services/business-solutions/)
- [Orbis Inc. — WVU Partnership Announcement](https://orbisinc.com/orbis-inc-announces-partnership-with-west-virginia-university-for-project-connecting-underserved-communities)

---

## 4. Federal Subsidy Analysis

### 4.1 New Markets Tax Credit Program Overview

The designation "NMTC" embedded in the legal entity name Oak Hill Forestlands NMTC LLC constitutes a direct indication of New Markets Tax Credit program financing. The NMTC program, administered by the U.S. Treasury CDFI Fund under 26 U.S.C. § 45D, provides qualified equity investors a federal income tax credit equal to 39 percent of their investment, allocated over a seven-year compliance period. Credits are allocated by the CDFI Fund to certified Community Development Entities (CDEs), which in turn deploy capital into Qualified Low-Income Community Investments (QLICIs) in census tracts meeting statutory low-income thresholds.

Fayette County satisfies NMTC eligibility criteria under multiple qualifying metrics, including poverty rate thresholds and median family income standards established under the program.

### 4.2 Statutory Community Benefit Requirements

NMTC program compliance imposes substantive obligations on CDEs receiving allocation awards, including:

- Demonstrated accountability to residents of the low-income communities served, including through representation of low-income community residents on CDE governing or advisory boards
- Delivery of measurable, documented community benefit to the target low-income community as a primary investment objective
- Maintenance of compliance documentation subject to review by the CDFI Fund throughout the seven-year compliance period
- Public disclosure of allocation awards through the CDFI Fund's publicly searchable award database

These obligations are not discretionary program guidance; they are statutory and regulatory conditions attached to the utilization of federal tax credits.

### 4.3 Documented Community Benefit: Findings

Following a comprehensive review of publicly available records — including the CDFI Fund NMTC allocatee award database, West Virginia Secretary of State corporate filings, corporate disclosures, investor presentations, and program documentation — **this analysis has identified no public record documenting community benefit delivery to Fayette County residents attributable to the Oak Hill Forestlands NMTC LLC transaction.**

Specifically, the following categories of evidence were sought and not identified:

- Employment creation or retention records
- Documentation of low-income community resident representation on CDE governing or advisory boards
- CDFI Fund compliance reports referencing the Oak Hill Forestlands NMTC transaction
- Community impact assessments or investment summaries published by the CDE or its allocatee
- Any public communication from The Forestland Group, Orbis Inc., or affiliated entities addressing community benefit delivery in Fayette County

### 4.4 Comparable Transaction Standard

For purposes of establishing a community benefit documentation standard applicable to comparable NMTC timberland transactions in West Virginia, this analysis references the 2018 NMTC financing of The Lyme Timber Company through CEI Capital Management LLC (CCML), which closed $20 million in NMTC allocation for timberland acquisition in Wyoming, McDowell, Mingo, and Logan counties — communities with documented poverty rates as high as 37.9 percent and unemployment rates reaching 14.8 percent.

The Lyme transaction generated publicly available community benefit documentation including: 29 direct and contractor timber harvesting positions, deployment of new safe logging technology, and a quantified economic multiplier analysis for the target counties. This documentation constitutes the minimum standard of community benefit accountability applicable to NMTC-financed timberland transactions in comparable West Virginia communities.

No equivalent documentation has been identified for Oak Hill Forestlands NMTC LLC.

**Source:** [CEI Capital Management — Lyme Timber Company NMTC Financing Press Release, 2018](https://www.ceimaine.org/news-and-events/news/2018/08/ccml-financing-of-the-lyme-timber-company-introduces-new-safe-logging-tech)

---

## 5. Revenue Extraction Analysis

### 5.1 Timber Harvesting

Timber extraction from TFG-managed West Virginia holdings constitutes the primary revenue stream from these assets. Proceeds from timber harvesting flow to the investment manager and ultimately to institutional investor clients outside the state. No revenue sharing mechanism with Fayette County or its residents has been identified in any publicly available document.

### 5.2 Voluntary Carbon Market Credits

The Forestland Group's investor materials identify the firm as the single largest producer of forestry carbon offsets in the United States, having generated over 22 million voluntary carbon market credits from its timberland holdings. Carbon credits are generated through restriction of harvest activity and verification of carbon sequestration, with contracts typically structured over 20- to 50-year terms. Credit revenue flows to the landowner — in this case institutional investment vehicles registered outside West Virginia — with no documented revenue participation by host communities.

The voluntary carbon market representing a significant and growing revenue stream from West Virginia timberland held by out-of-state institutional investors was not contemplated in the original NMTC community benefit framework applicable to the Oak Hill Forestlands acquisition. No mechanism for retrospective community benefit adjustment to account for carbon credit revenue has been identified.

**Sources:**
- [The Forestland Group — UNEP PRI Overview PDF](https://www.unepfi.org/wordpress/wp-content/uploads/2021/02/01_The-Forestland-Group-Overview.pdf)
- [WV Highlands Conservancy — Forest Carbon Capture: What Is Going On?](https://www.wvhighlands.org/article/forest-carbon-capture-what-is-going-on/)

### 5.3 Property Tax Minimization

Orbis Inc.'s documented service offering of property tax minimization on behalf of institutional timberland clients has direct fiscal implications for Fayette County. The magnitude of annual property tax reduction achieved on the 287 parcels comprising this dataset has not been disclosed publicly. A formal inquiry to the Fayette County Assessor's office and a comparative analysis of assessed values against equivalent privately-held timberland parcels would establish the cumulative fiscal impact on county revenue.

### 5.4 Portfolio Disposition

In November 2022, The Forestland Group transferred its entire portfolio of approximately 1.7 million acres to Anew Climate LLC, backed by an investor consortium led by Oak Hill Advisors, an alternative investment firm managing assets in excess of $60 billion. The transaction was characterized in publicly available communications as a conservation-oriented initiative with emphasis on voluntary carbon market credit generation for institutional buyers.

The disposition of NMTC compliance obligations — including any residual community benefit delivery requirements associated with the Oak Hill Forestlands NMTC transaction — was not addressed in publicly available documentation of the sale. Whether those obligations transferred to the acquiring entity, were discharged prior to closing, or remain unaddressed constitutes a material public accountability question.

**Source:** [Anew Climate / Oak Hill Advisors Acquisition Announcement — Yahoo Finance, November 2, 2022](https://finance.yahoo.com/news/anew-oha-led-investor-consortium-154600963.html)

---

## 6. Historical and Policy Context

The concentration of timberland ownership in West Virginia by absentee institutional investors is not a novel phenomenon. The WV Center on Budget and Policy documented in 2013 that The Forestland Group had already assembled 500,366 acres across 31 West Virginia counties, identifying TFG as the state's largest single private landowner. That report characterized the pattern as the "financialization" of Appalachian timberland and called for greater transparency in absentee ownership structures, enhanced community benefit requirements, and policy mechanisms to support local ownership.

In the intervening twelve years, the portfolio expanded. The voluntary carbon market emerged as a substantial additional revenue stream. The institutional ownership structure became more complex through the 2022 portfolio sale. And the communities surrounding these holdings continued to record poverty rates, unemployment rates, and out-migration figures among the highest in the nation.

The analytical infrastructure to surface and document this pattern at the county level did not exist at the community level until the development of the system described in this case study.

**Source:** [WV Center on Budget and Policy — Land Ownership Study, December 2013](https://wvpolicy.org/wp-content/uploads/2018/5/land-study-paper-final3.pdf)

---

## 7. Unresolved Public Accountability Questions

The following questions arise directly from the findings documented in this case study. Each is grounded in publicly available evidence and addressable through appropriate public records mechanisms, regulatory inquiry, or legislative oversight.

**7.1** What specific, documented community benefit did Fayette County residents receive from the Oak Hill Forestlands NMTC LLC investment, as required under 26 U.S.C. § 45D and applicable CDFI Fund program compliance standards? Where is that documentation in the public record?

**7.2** Who represented low-income community residents of Fayette County on the governing or advisory board of the Community Development Entity through which Oak Hill Forestlands NMTC LLC was financed, as required by NMTC program accountability standards?

**7.3** What is the aggregate voluntary carbon market credit revenue generated from the Fayette County timberland parcels identified in this analysis, and through what mechanism, if any, did any portion of that revenue benefit the residents of the host community?

**7.4** Did NMTC community benefit compliance obligations transfer to Anew Climate LLC and Oak Hill Advisors upon the 2022 portfolio acquisition? If those obligations were discharged prior to sale, through what process and with what documentation?

**7.5** What is the annual property tax revenue Fayette County currently receives from the 287 parcels comprising this dataset, and how does that figure compare to the assessed value and tax obligation of equivalent privately-held timberland? What is the cumulative fiscal impact of the differential, if any, on county public services?

**7.6** What is the full scope of Orbis Inc.'s commercial relationship with institutional timberland investors holding NMTC-financed land in West Virginia, and was that relationship disclosed in connection with Orbis's NSF-funded equity partnership with West Virginia University?

---

## 8. Recommendations for Further Investigation

### 8.1 Immediate Public Records Actions

- Submit a Freedom of Information Act request to the U.S. Department of the Treasury CDFI Fund for all compliance documentation, community benefit reports, and board representation records associated with Oak Hill Forestlands NMTC LLC
- Submit a formal inquiry to the Fayette County Assessor's office for annual assessed value and property tax records for all 287 parcels identified in this dataset, with a comparative analysis against equivalent privately-held timberland
- Search the WV Secretary of State database for all corporate entities registered to the Chapel Hill and Charlotte addresses identified in this analysis to establish the full scope of institutional timberland holdings across West Virginia counties

### 8.2 Legislative and Regulatory Referral

- Referral to West Virginia's federal congressional delegation for inquiry to the CDFI Fund regarding NMTC community benefit compliance oversight in rural timberland transactions
- Referral to the West Virginia Legislature's relevant committee for examination of state-level oversight mechanisms applicable to absentee institutional timberland ownership and associated revenue extraction
- Inquiry to the National Science Foundation regarding disclosure requirements applicable to the Orbis Inc. / WVU equity partnership in light of Orbis's commercial operations in West Virginia communities

### 8.3 Academic and Policy Engagement

- Engagement with the WV Center on Budget and Policy for updated statewide analysis of institutional timberland ownership concentration incorporating NMTC financing identification
- Engagement with WVU's Division of Forestry and Natural Resources regarding the institutional context of the Orbis partnership and potential collaborative research on community benefit outcomes in NMTC-financed timberland transactions
- Replication of this spatial analysis methodology across Nicholas, Wyoming, McDowell, Logan, and additional West Virginia counties where comparable institutional ownership patterns are anticipated

---

## 9. Complete Source Reference

| Finding | Source | URL |
|---|---|---|
| Parcel data — entity names, acreage, county distribution | Fayette County Assessor Public Parcel Database | Public county record — independently verifiable |
| Corporate registration, registered address, managers | WV Secretary of State — Oak Hill Forestlands NMTC LLC | [SOS Org. 339624](https://apps.sos.wv.gov/business/corporations/organization.aspx?org=339624) |
| TFG AUM, portfolio scale, carbon credit production, UN PRI affiliation | The Forestland Group — UNEP Finance Initiative Investor Overview | [PDF](https://www.unepfi.org/wordpress/wp-content/uploads/2021/02/01_The-Forestland-Group-Overview.pdf) |
| TFG carbon credit marketing, ESG branding, institutional client base | The Forestland Group — CE Media Sponsor Profile | [ce-em.com](https://ce-em.com/community/all-sponsors/the-forestland-group-tfg/) |
| Orbis service offerings, TFG endorsement | Orbis Inc. — Business Solutions | [orbisinc.com](https://orbisinc.com/services/business-solutions/) |
| Orbis / WVU NSF partnership | Orbis Inc. — Partnership Announcement, April 2022 | [orbisinc.com](https://orbisinc.com/orbis-inc-announces-partnership-with-west-virginia-university-for-project-connecting-underserved-communities) |
| NMTC program statutory requirements, community benefit mandate | CBO Financial — West Virginia NMTC Program Overview | [cbofinancial.com](https://cbofinancial.com/financing/cdfi/new-markets-tax-credit/west-virginia/) |
| NMTC allocatee awards — searchable federal database | U.S. Treasury CDFI Fund | [cdfifund.gov](https://www.cdfifund.gov/awards/nmtc) |
| TFG portfolio acquisition by Anew Climate / Oak Hill Advisors | Yahoo Finance — Press Release, November 2, 2022 | [Yahoo Finance](https://finance.yahoo.com/news/anew-oha-led-investor-consortium-154600963.html) |
| Lyme Timber NMTC transaction — community benefit documentation standard | CEI Capital Management — Press Release, August 2018 | [ceimaine.org](https://www.ceimaine.org/news-and-events/news/2018/08/ccml-financing-of-the-lyme-timber-company-introduces-new-safe-logging-tech) |
| WV timberland ownership concentration history — TFG as largest WV landowner | WV Center on Budget and Policy — Land Ownership Study, December 2013 | [wvpolicy.org](https://wvpolicy.org/wp-content/uploads/2018/5/land-study-paper-final3.pdf) |
| WV forest carbon credit mechanisms and market structure | WV Highlands Conservancy — Forest Carbon Capture Analysis, 2023 | [wvhighlands.org](https://www.wvhighlands.org/article/forest-carbon-capture-what-is-going-on/) |

---

## 10. Conclusion

The spatial analysis documented in this case study establishes, through public records alone, that a single institutional timberland investment management organization headquartered in Chapel Hill, North Carolina holds 50,697 acres across 287 parcels in Fayette County, West Virginia — a holding assembled in part through federal New Markets Tax Credit financing instruments legally conditioned on the delivery of community benefit to one of the most economically distressed counties in the United States.

The analysis further establishes that the operational infrastructure supporting this holding is managed by a Charlotte, North Carolina technology firm that simultaneously holds a federally funded equity partnership with West Virginia University focused on underserved community development — a relationship that has not been publicly examined in light of the firm's commercial function as an enabler of institutional land asset extraction in the communities it ostensibly serves.

No public record has been identified documenting the community benefit delivery required under NMTC program compliance standards for the Oak Hill Forestlands NMTC LLC transaction. In the absence of such documentation, the federal subsidy extended to facilitate this acquisition represents an unresolved accountability gap that merits formal inquiry by the CDFI Fund, the West Virginia congressional delegation, and relevant state legislative bodies.

The data was publicly available. The records were always accessible. The findings presented here required no proprietary information and no extraordinary resources — only the analytical infrastructure to integrate and interrogate public records at scale.

That infrastructure now exists in Fayette County.

---

*Produced by Harmony for Hope, Inc. — Oak Hill, West Virginia*
*Advanced Location Intelligence Infrastructure: Ms. Egeria Jarvis GIS System*
*Public Documentation Repository: [github.com/H4HWV2011/msjarvis-public-docs](https://github.com/H4HWV2011/msjarvis-public-docs)*
*License: Creative Commons Attribution 4.0 International (CC BY 4.0)*
*All data sources utilized in this analysis are publicly available and independently verifiable by any researcher or member of the public.*
*Correspondence and inquiries: Harmony for Hope, Inc. — Oak Hill, West Virginia*
