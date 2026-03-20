# Case Study: Institutional Timberland Acquisition, Federal Subsidy Utilization, and Absentee Ownership Concentration in Fayette County, West Virginia

**Date of Analysis:** March 20, 2026
**Producing Organization:** Kidd's Technical Services, Inc. — Mount Hope, West Virginia
**Analytical System:** Advanced Location Intelligence Infrastructure
**Primary Database:** `msjarvisgis` — `public.mvw_gbim_landowner_spatial`
**Data Source:** Fayette County, West Virginia Public Property Assessment Records
**Classification:** Public Research Record

---

## Abstract

This case study documents the findings of a spatial analysis of Fayette County, West Virginia public property assessment records, cross-referenced with West Virginia Secretary of State corporate filings, U.S. Treasury Community Development Financial Institutions (CDFI) Fund program documentation, and publicly available corporate disclosures. The analysis identified 287 parcels totaling 50,697 acres held by four interrelated corporate entities, all registered to a single institutional timberland investment management organization (TIMO) headquartered in Chapel Hill, North Carolina. The analysis further identified the utilization of federal New Markets Tax Credit (NMTC) financing in the acquisition of a subset of these holdings, with no publicly available documentation of the community benefit delivery required under NMTC program compliance standards. The findings raise substantive questions regarding federal program accountability, absentee institutional land ownership concentration, carbon credit revenue extraction, and the adequacy of existing oversight mechanisms for NMTC-financed timberland transactions in economically distressed rural communities. Contextual analysis of the acquiring entity's ownership lineage — tracing through Oak Hill Advisors to the Bass family oil fortune and ultimately to T. Rowe Price — illuminates the full arc of capital extraction operating in Fayette County under federally subsidized instruments.

---

## 1. Introduction

### 1.1 Background

Fayette County, West Virginia is classified as an economically distressed community by the Appalachian Regional Commission. The county's economic trajectory reflects broader patterns of resource extraction and capital outflow characteristic of Appalachian economies — patterns extensively documented in the academic literature on regional political economy, absentee land ownership, and the financialization of natural resource assets. The WV Center on Budget and Policy documented as early as 2013 that absentee corporate and institutional entities held the majority of West Virginia's most productive timberland, with a single Chapel Hill, North Carolina investment firm — The Forestland Group — identified as the state's largest private landowner at that time, holding over 500,000 acres across 31 counties. ([WV Center on Budget and Policy — Land Ownership Study, December 2013](https://wvpolicy.org/wp-content/uploads/2018/5/land-study-paper-final3.pdf))

The New Markets Tax Credit program, established by the Community Renewal Tax Relief Act of 2000 (P.L. 106-554) and administered by the U.S. Treasury's CDFI Fund, was designed to catalyze private investment in low-income communities by providing investors a federal tax credit equal to 39 percent of their qualified equity investment, distributed over a seven-year compliance period. The program requires recipient Community Development Entities (CDEs) to maintain accountability to residents of the low-income communities served, including through representation on governing or advisory boards, and to deliver measurable, documented community benefit as a condition of credit utilization. ([U.S. Treasury CDFI Fund — NMTC Program Overview](https://www.cdfifund.gov/programs-training/programs/new-markets-tax-credit))

Appalachia's pattern of resource extraction — coal, timber, natural gas, and increasingly carbon sequestration value — has been sustained across successive economic eras by structural information asymmetries: communities possess neither the analytical tools nor the institutional capacity to identify, document, and challenge the mechanisms through which wealth is extracted from their geography. This case study represents a direct application of community-owned spatial intelligence to close that asymmetry.

### 1.2 Research Question

This case study addresses the following primary question: To what extent does the concentration of institutionally managed timberland in Fayette County — facilitated in part through federally subsidized NMTC financing — reflect compliance with the community benefit obligations attendant to that financing, and what mechanisms exist to ensure public accountability for those obligations?

Secondary questions examined include: What is the full ownership lineage of the entities currently holding or previously holding these assets? What revenue streams have been generated from these holdings beyond timber harvesting? What operational infrastructure supports the management of these holdings, and do any conflicts of interest exist within that infrastructure? What comparable NMTC timberland transactions provide a community benefit documentation standard against which this transaction may be evaluated?

### 1.3 Methodology

Spatial queries were executed against the `public.mvw_gbim_landowner_spatial` materialized view within the `msjarvisgis` PostgreSQL/PostGIS database, which aggregates publicly available parcel-level land ownership records from West Virginia county assessors. Entity names identified through the spatial analysis were cross-referenced against the West Virginia Secretary of State online business database to establish corporate structure, registered addresses, and management relationships. Corporate identities were further verified through publicly available investor presentations, corporate websites, press releases, federal program databases, and financial news sources. Capital lineage was traced through publicly available biographical records, investment firm histories, and corporate acquisition announcements. All data sources utilized in this analysis are publicly available and independently verifiable by any researcher or member of the public.

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

**Data source:** Fayette County, West Virginia Public Property Assessment Records, accessed via `msjarvisgis` spatial database, March 20, 2026. All parcel records are publicly available through the Fayette County Assessor's office and independently verifiable.

---

## 3. Corporate Structure Analysis

### 3.1 Entity Identification and Ownership Chain

Cross-referencing entity names against the West Virginia Secretary of State public business database established the following ownership and operational structure. Every entity identified in the parcel dataset carries the registered care-of address of Orbis Inc., Charlotte, North Carolina. The managing entity address for Oak Hill Forestlands NMTC LLC — 55 Vilcom Center Drive, Suite 240, Chapel Hill, North Carolina — corresponds to the registered headquarters of The Forestland Group, LLC. ([WV Secretary of State — Oak Hill Forestlands NMTC LLC, Org. 339624](https://apps.sos.wv.gov/business/corporations/organization.aspx?org=339624))

| Entity | Organizational Role | Headquarters | Primary Public Record |
|---|---|---|---|
| The Forestland Group, LLC | Timberland investment manager (TIMO); beneficial owner and portfolio manager | 55 Vilcom Center Dr., Suite 240, Chapel Hill, NC | [WV SOS Org. 339624](https://apps.sos.wv.gov/business/corporations/organization.aspx?org=339624) |
| Chateaugay Holding Company LLC | Registered fund vehicle; LLC manager of record | Chapel Hill, NC | [WV SOS Filing](https://apps.sos.wv.gov/business/corporations/organization.aspx?org=339624) |
| Orbis Inc. | Land asset management technology provider; property tax administration; recreational lease management; acquisition due diligence | Charlotte, NC | [orbisinc.com](https://orbisinc.com) |
| Anew Climate LLC / Oak Hill Advisors (OHA) | Current beneficial owner; acquired entire TFG portfolio November 2022 | New York, NY | [Yahoo Finance — Acquisition Announcement, November 2, 2022](https://finance.yahoo.com/news/anew-oha-led-investor-consortium-154600963.html) |

### 3.2 The Forestland Group: Organizational Profile

The Forestland Group (TFG) is a timberland investment management organization (TIMO) operating as a registered investment adviser headquartered in Chapel Hill, North Carolina. Their publicly available investor presentation, hosted on the United Nations Environment Programme Finance Initiative platform, documents the following portfolio characteristics:

- $2.6 billion in assets under management across 10 commingled funds and separate managed accounts
- 1,185,527 acres under active management across 11 states
- 4.5 million total acres transacted across 111 transactions since founding
- Self-described as the single largest producer of forestry carbon offsets in the United States, having generated over 22 million voluntary carbon market credits
- Approximately 15 percent share of the U.S. forestry carbon offset market
- Signatory to the United Nations Principles for Responsible Investment (UN PRI)
- Institutional client base comprising pension funds, university endowments, private foundations, and family offices

Within West Virginia, TFG assembled holdings exceeding 500,000 acres across 31 counties — a concentration documented by the WV Center on Budget and Policy as early as 2013, at which time TFG was identified as the largest single private landowner in the state. ([WV Center on Budget and Policy — Land Ownership Study, December 2013](https://wvpolicy.org/wp-content/uploads/2018/5/land-study-paper-final3.pdf))

**Primary Source:** [The Forestland Group: An Introduction — UNEP Finance Initiative Investor Overview PDF](https://www.unepfi.org/wordpress/wp-content/uploads/2021/02/01_The-Forestland-Group-Overview.pdf)

**Secondary Source:** [The Forestland Group — CE Media Institutional Sponsor Profile](https://ce-em.com/community/all-sponsors/the-forestland-group-tfg/)

### 3.3 Orbis Inc.: Organizational Profile and Conflict of Interest Considerations

Orbis Inc. is a geospatial intelligence and land asset management technology firm founded in 2000 and headquartered in Charlotte, North Carolina. Their core service offerings to institutional timberland investors — as documented on their corporate website — include parcel-level property data management, property tax minimization strategies, hunting and recreational lease administration, environmental due diligence support for new timberland acquisitions, and ESG consulting services enabling institutional clients to market timberland holdings to socially responsible investment funds. ([Orbis Inc. — Business Solutions for Timberland Property Management](https://orbisinc.com/services/business-solutions/))

The Forestland Group's Senior Vice President, Mike Hincher, is cited directly on the Orbis Inc. corporate website endorsing the firm's services:

> *"I can only say positive things when it comes to working with Orbis. Their integrity, in line with their customer-focused attitude, allows me and The Forestland Group the peace of mind knowing our data is in the best hands."*

([Orbis Inc. — Home](https://orbisinc.com))

In April 2022, Orbis Inc. announced a formal research partnership with West Virginia University (WVU), funded through a National Science Foundation grant, focused on equitable access to economic opportunity for underserved communities in West Virginia, administered through WVU's Division of Forestry and Natural Resources. ([Orbis Inc. — WVU Partnership Announcement, April 2022](https://orbisinc.com/orbis-inc-announces-partnership-with-west-virginia-university-for-project-connecting-underserved-communities))

This partnership warrants examination in the context of Orbis's concurrent operational role as the technology and property management infrastructure provider for institutional timberland holdings in West Virginia — holdings acquired in part through federal community development financing instruments targeting the same underserved communities identified in the NSF grant. The relationship between Orbis's stated equity mission and its commercial function as an operational enabler of institutional extraction in those communities has not been addressed in any publicly available documentation associated with the WVU partnership. This constitutes a material conflict of interest warranting formal disclosure review by the National Science Foundation and West Virginia University.

### 3.4 Oak Hill Advisors and Capital Lineage: Historical Background

The 2022 acquisition of The Forestland Group's entire portfolio by Anew Climate LLC — backed by an investor consortium led by Oak Hill Advisors — introduces a capital lineage with direct historical relevance to the pattern of resource extraction documented in this case study.

**Oak Hill Advisors (OHA)** is an alternative credit and investment management firm headquartered in New York. At the time of the Anew Climate / TFG transaction, OHA managed assets in excess of $53 billion. In October 2021 — one year prior to the Forestland Group acquisition — T. Rowe Price acquired Oak Hill Advisors for **$4.2 billion**, integrating OHA into T. Rowe Price's alternative investment platform. T. Rowe Price currently manages approximately $1.61 trillion in assets under management globally. ([T. Rowe Price — Oak Hill Advisors Acquisition Press Release, October 2021](https://www.prnewswire.com/news-releases/t-rowe-price-to-acquire-oak-hill-advisors-accelerating-expansion-into-alternative-investments-301409168.html)) ([Institutional Investor — T. Rowe Price to Acquire Oak Hill Advisors for $4.2 Billion](https://www.institutionalinvestor.com/article/2bsws3k22w3gomzxgcsn4/portfolio/t-rowe-price-to-acquire-oak-hill-advisors-for-4-2-billion))

The "Oak Hill" brand traces directly to **Robert M. Bass**, born March 19, 1948, Fort Worth, Texas, with an estimated personal net worth exceeding $5 billion. Robert Bass founded Oak Hill Capital Partners in 1986 as a family office investment vehicle, from which the Oak Hill brand subsequently expanded across multiple fund families including Oak Hill Advisors. ([Robert Bass — Wikipedia](https://en.wikipedia.org/wiki/Robert_Bass))

The Bass family fortune originates with **Sid W. Richardson**, a Texas wildcatter and one of the wealthiest Americans of the mid-20th century, who accumulated his fortune through West Texas oil and gas exploration. Richardson died without direct heirs in 1959 and left the majority of his estate to his nephew **Perry Bass**, Robert Bass's father. Perry Bass subsequently founded **Bass Brothers Enterprises** to manage and grow the inherited oil fortune. ([D Magazine — Sid Richardson: Fort Worth's Philanthropic Oil Baron, February 2025](https://www.dmagazine.com/publications/d-ceo/2025/january-february/sid-richardson-fort-worth-s-philanthropic-oil-baron/))

The four Bass brothers — Sid, Edward, Robert, and Lee, all educated at Yale University and Stanford University — transformed their inherited petroleum wealth into a diversified investment empire spanning real estate, private equity, alternative credit, and natural resource assets. ([Wikipedia — Robert Bass](https://en.wikipedia.org/wiki/Robert_Bass))

The complete capital lineage operating in Fayette County through the Anew Climate / Oak Hill Advisors acquisition is therefore:

| Historical Origin | Entity | Era | Capital Type |
|---|---|---|---|
| West Texas oil and gas wildcatting | Sid W. Richardson personal fortune | 1930s–1950s | Petroleum extraction |
| Inherited oil fortune, Fort Worth TX | Perry Bass / Bass Brothers Enterprises | 1959–1980s | Diversified investment |
| Family office expansion | Robert Bass / Oak Hill Capital Partners | 1986–present | Private equity / alternatives |
| Alternative credit management | Oak Hill Advisors (OHA) | 1990s–2021 | Credit / alternatives |
| Global investment management | T. Rowe Price (acquired OHA for $4.2B) | 2021–present | $1.61 trillion AUM |
| Conservation / carbon credit vehicle | Anew Climate LLC / OHA consortium | 2022–present | Timberland / carbon markets |
| Federal poverty relief financing | Oak Hill Forestlands NMTC LLC | Acquisition date–present | NMTC tax credits / Fayette County land |

The extractive economic model that has characterized Appalachian resource development for more than a century — petroleum, coal, timber — is thus represented in this transaction not as historical legacy but as active, present-tense capital deployment. Texas oil dynasty wealth, grown through petroleum extraction, now holds West Virginia timberland acquired through federal poverty relief instruments, generating carbon credit revenue for institutional investors, administered by a Charlotte technology firm with a federally funded university equity partnership.

---

## 4. Federal Subsidy Analysis

### 4.1 New Markets Tax Credit Program Overview

The designation "NMTC" embedded in the legal entity name Oak Hill Forestlands NMTC LLC constitutes a direct indicator of New Markets Tax Credit program financing. The NMTC program, administered by the U.S. Treasury CDFI Fund under 26 U.S.C. § 45D, provides qualified equity investors a federal income tax credit equal to 39 percent of their investment, allocated over a seven-year compliance period. Credits are allocated by the CDFI Fund to certified Community Development Entities (CDEs), which in turn deploy capital into Qualified Low-Income Community Investments (QLICIs) in census tracts meeting statutory low-income thresholds. ([U.S. Treasury CDFI Fund — NMTC Program](https://www.cdfifund.gov/programs-training/programs/new-markets-tax-credit)) ([CBO Financial — West Virginia NMTC Program Overview](https://cbofinancial.com/financing/cdfi/new-markets-tax-credit/west-virginia/))

Fayette County satisfies NMTC eligibility criteria under multiple qualifying metrics, including poverty rate thresholds and median family income standards established under the program and verifiable through the CDFI Fund's mapping tools and census data.

### 4.2 Statutory Community Benefit Requirements

NMTC program compliance imposes substantive obligations on CDEs receiving allocation awards, including:

- Demonstrated accountability to residents of the low-income communities served, including through representation of low-income community residents on CDE governing or advisory boards
- Delivery of measurable, documented community benefit to the target low-income community as a primary investment objective
- Maintenance of compliance documentation subject to review by the CDFI Fund throughout the seven-year compliance period
- Public disclosure of allocation awards through the CDFI Fund's publicly searchable award database at [cdfifund.gov/awards/nmtc](https://www.cdfifund.gov/awards/nmtc)

These obligations are not discretionary program guidance; they are statutory and regulatory conditions attached to the utilization of federal tax credits under 26 U.S.C. § 45D and implementing Treasury regulations.

### 4.3 Documented Community Benefit: Findings

Following a comprehensive review of publicly available records — including the CDFI Fund NMTC allocatee award database, West Virginia Secretary of State corporate filings, corporate disclosures, investor presentations, and program documentation — **this analysis has identified no public record documenting community benefit delivery to Fayette County residents attributable to the Oak Hill Forestlands NMTC LLC transaction.**

Specifically, the following categories of evidence were sought and not identified:

- Employment creation or retention records associated with the Oak Hill Forestlands NMTC LLC investment
- Documentation of low-income community resident representation on CDE governing or advisory boards
- CDFI Fund compliance reports referencing the Oak Hill Forestlands NMTC transaction by name or allocatee
- Community impact assessments or investment summaries published by the CDE or its allocatee
- Any public communication from The Forestland Group, Orbis Inc., Anew Climate LLC, Oak Hill Advisors, or affiliated entities addressing community benefit delivery in Fayette County

The absence of publicly available documentation does not constitute definitive evidence of non-compliance; CDFI Fund compliance records may exist in non-public form. However, the absence of any public record of community benefit delivery — in a transaction large enough to be embedded in the legal name of the holding entity — is itself a finding warranting formal inquiry to the CDFI Fund through Freedom of Information Act mechanisms.

### 4.4 Comparable Transaction Standard

For purposes of establishing a community benefit documentation standard applicable to comparable NMTC timberland transactions in West Virginia, this analysis references the 2018 NMTC financing of The Lyme Timber Company through CEI Capital Management LLC (CCML), which closed $20 million in NMTC allocation for timberland acquisition in Wyoming, McDowell, Mingo, and Logan counties — communities with documented poverty rates as high as 37.9 percent and unemployment rates reaching 14.8 percent.

The Lyme transaction generated publicly available community benefit documentation including: 29 direct and contractor timber harvesting positions, deployment of new safe logging technology certified for reduced-impact harvesting, and a quantified economic multiplier analysis for the target counties. This documentation — publicly available through CEI Capital Management's press release archive — constitutes the minimum evidentiary standard of community benefit accountability applicable to NMTC-financed timberland transactions in comparable West Virginia communities. ([CEI Capital Management — Lyme Timber Company NMTC Financing Press Release, August 2018](https://www.ceimaine.org/news-and-events/news/2018/08/ccml-financing-of-the-lyme-timber-company-introduces-new-safe-logging-tech))

No equivalent documentation has been identified for Oak Hill Forestlands NMTC LLC.

---

## 5. Revenue Extraction Analysis

### 5.1 Timber Harvesting

Timber extraction from TFG-managed West Virginia holdings constitutes the primary documented revenue stream from these assets. Proceeds from timber harvesting flow to the investment manager and ultimately to institutional investor clients outside the state. No revenue sharing mechanism with Fayette County or its residents has been identified in any publicly available document.

### 5.2 Voluntary Carbon Market Credits

The Forestland Group's investor materials — hosted on the UNEP Finance Initiative platform — identify the firm as the single largest producer of forestry carbon offsets in the United States, having generated over 22 million voluntary carbon market credits from its timberland holdings. ([The Forestland Group — UNEP Finance Initiative Overview PDF](https://www.unepfi.org/wordpress/wp-content/uploads/2021/02/01_The-Forestland-Group-Overview.pdf))

Carbon credits are generated through restriction of harvest activity and third-party verification of carbon sequestration value, with contracts typically structured over 20- to 50-year terms. Credit revenue flows to the landowner — in this case institutional investment vehicles registered outside West Virginia — with no documented revenue participation by host communities. ([WV Highlands Conservancy — Forest Carbon Capture: What Is Going On?, November 2023](https://www.wvhighlands.org/article/forest-carbon-capture-what-is-going-on/))

The voluntary carbon market — representing a significant and growing revenue stream from West Virginia timberland held by out-of-state institutional investors — was not a material commercial consideration at the time the NMTC community benefit framework applicable to the Oak Hill Forestlands acquisition was established. The emergence of carbon credit revenue as a primary asset value driver, subsequent to the NMTC financing of the original acquisition, creates a retrospective community benefit gap that existing program compliance mechanisms are not structured to address. No mechanism for retrospective community benefit adjustment to account for carbon credit revenue generated from NMTC-financed timberland has been identified in CDFI Fund program documentation.

### 5.3 Property Tax Minimization

Orbis Inc.'s documented service offering of property tax minimization on behalf of institutional timberland clients has direct and quantifiable fiscal implications for Fayette County. Orbis's own materials document over $1.2 million in client property taxes saved across their managed portfolio. The magnitude of annual property tax reduction achieved specifically on the 287 Fayette County parcels comprising this dataset has not been disclosed publicly. A formal inquiry to the Fayette County Assessor's office and a comparative analysis of assessed values against equivalent privately-held timberland parcels would establish the cumulative fiscal impact on county public service revenue. ([Orbis Inc. — Business Solutions](https://orbisinc.com/services/business-solutions/))

### 5.4 Recreational Lease Revenue

Orbis Inc.'s documented administration of hunting and recreational leases on behalf of institutional timberland clients constitutes an additional revenue stream extracted from land whose access was historically available to local residents. The monetization of recreational access — converting common resource access to fee-based lease income flowing to out-of-state investors — represents a qualitative community benefit reduction not captured in financial documentation. The aggregate value of recreational leases administered by Orbis on Fayette County parcels has not been publicly disclosed.

### 5.5 Portfolio Disposition and Capital Gains

In November 2022, The Forestland Group transferred its entire portfolio of approximately 1.7 million acres to Anew Climate LLC, backed by an investor consortium led by Oak Hill Advisors — at the time a subsidiary of T. Rowe Price following the $4.2 billion acquisition completed in 2021. The transaction was characterized in publicly available communications as a conservation-oriented initiative with emphasis on voluntary carbon market credit generation for institutional buyers. ([Yahoo Finance — Anew Climate / OHA Acquisition Press Release, November 2, 2022](https://finance.yahoo.com/news/anew-oha-led-investor-consortium-154600963.html)) ([T. Rowe Price / OHA Acquisition — Paul Weiss Client Alert, October 2021](https://www.paulweiss.com/insights/client-news/oak-hill-advisors-to-be-acquired-by-t-rowe-price-for-42-billion))

The capital gains realized through portfolio appreciation — accruing to TFG's institutional investor clients over the holding period — represent the terminal expression of the extraction model. Land acquired at a federally subsidized cost, managed with minimized local tax obligations, generating timber revenue, carbon credit revenue, and recreational lease income over the holding period, was ultimately sold at appreciated value with capital gains flowing entirely to out-of-state institutional accounts.

The disposition of NMTC compliance obligations — including any residual community benefit delivery requirements associated with the Oak Hill Forestlands NMTC transaction — was not addressed in publicly available documentation of the 2022 sale. Whether those obligations transferred to the acquiring entity, were discharged prior to closing, or remain unaddressed constitutes a material public accountability question requiring CDFI Fund clarification.

---

## 6. Historical and Policy Context

### 6.1 The Financialization of Appalachian Timberland

The concentration of timberland ownership in West Virginia by absentee institutional investors is not a novel phenomenon. The WV Center on Budget and Policy documented in December 2013 that The Forestland Group had already assembled 500,366 acres across 31 West Virginia counties, identifying TFG as the state's largest single private landowner. That report characterized the broader pattern as the "financialization" of Appalachian timberland — the systematic replacement of traditional absentee corporate timber operators with Wall Street investment vehicles managing land for institutional portfolio returns — and called for greater transparency in absentee ownership structures, enhanced community benefit requirements, and policy mechanisms to support local and community ownership. ([WV Center on Budget and Policy — Land Ownership Study, December 2013](https://wvpolicy.org/wp-content/uploads/2018/5/land-study-paper-final3.pdf))

In the twelve years following that report: the TFG portfolio expanded; the voluntary carbon market matured into a multi-billion-dollar asset class generating additional extraction revenue from the same land base; the institutional ownership structure became substantially more complex and more remote from the communities of origin through the 2022 portfolio sale to a T. Rowe Price subsidiary; and the communities surrounding these holdings continued to record poverty rates, unemployment rates, and population out-migration figures among the highest in the nation.

### 6.2 The Extractive Capital Continuum

The historical lineage of capital now holding West Virginia timberland through the Anew Climate / Oak Hill Advisors vehicle — tracing through the Bass family investment empire to the inherited fortune of Texas oil wildcatter Sid W. Richardson — places the current configuration of Fayette County land ownership in a continuum of extractive capital deployment that predates the NMTC program, the carbon credit market, and the TIMO asset class by several decades.

West Texas petroleum wealth, accumulated through mid-20th century oil exploration, was institutionalized through family office investment vehicles in the 1980s, diversified into alternative credit and timberland assets through the 1990s and 2000s, and is now deployed in Fayette County, West Virginia — one of the nation's most persistently distressed communities — through a federally subsidized acquisition instrument that was legally conditioned on delivering community benefit to the residents of that county.

The commodity of extraction has changed — from petroleum to timber to carbon sequestration value. The structural relationship between the capital and the community has not. ([Wikipedia — Robert Bass](https://en.wikipedia.org/wiki/Robert_Bass)) ([D Magazine — Sid Richardson: Fort Worth's Philanthropic Oil Baron, February 2025](https://www.dmagazine.com/publications/d-ceo/2025/january-february/sid-richardson-fort-worth-s-philanthropic-oil-baron/)) ([Institutional Investor — T. Rowe Price Acquires Oak Hill Advisors, October 2021](https://www.institutionalinvestor.com/article/2bsws3k22w3gomzxgcsn4/portfolio/t-rowe-price-to-acquire-oak-hill-advisors-for-4-2-billion))

### 6.3 The ESG Rebranding of Extraction

A distinctive feature of the current configuration is the application of environmental, social, and governance (ESG) branding to assets and transactions that, on substantive examination, reflect the same extractive economic relationships that have historically characterized Appalachian resource development.

The Forestland Group's UN PRI signatory status, Orbis Inc.'s NSF-funded equity partnership with WVU, and the characterization of the 2022 portfolio sale as a "groundbreaking conservation initiative" each represent the deployment of ESG and equity frameworks as reputational instruments — enabling institutional investors to market timberland holdings to socially responsible investment mandates while the underlying community benefit obligations of the federal financing instruments that facilitated the original acquisition remain publicly unaccounted for.

The analytical infrastructure developed for this case study surfaces that gap directly from public records, without resort to proprietary data or institutional access.

---

## 7. Unresolved Public Accountability Questions

The following questions arise directly from the findings documented in this case study. Each is grounded in publicly available evidence and addressable through appropriate public records mechanisms, regulatory inquiry, or legislative oversight.

**7.1** What specific, documented community benefit did Fayette County residents receive from the Oak Hill Forestlands NMTC LLC investment, as required under 26 U.S.C. § 45D and applicable CDFI Fund program compliance standards? Where is that documentation in the public record? ([CDFI Fund NMTC Awards Database](https://www.cdfifund.gov/awards/nmtc))

**7.2** Who represented low-income community residents of Fayette County on the governing or advisory board of the Community Development Entity through which Oak Hill Forestlands NMTC LLC was financed, as required by NMTC program accountability standards? ([CDFI Fund Program Requirements](https://www.cdfifund.gov/programs-training/programs/new-markets-tax-credit))

**7.3** What is the aggregate voluntary carbon market credit revenue generated from the Fayette County timberland parcels identified in this analysis since the date of the Oak Hill Forestlands NMTC acquisition, and through what mechanism, if any, did any portion of that revenue benefit the residents of the host community? ([TFG UNEP Overview PDF](https://www.unepfi.org/wordpress/wp-content/uploads/2021/02/01_The-Forestland-Group-Overview.pdf))

**7.4** Did NMTC community benefit compliance obligations transfer to Anew Climate LLC and Oak Hill Advisors upon the 2022 portfolio acquisition? If those obligations were discharged prior to sale, through what process and with what documentation, and where is that documentation in the public record? ([Yahoo Finance — Anew/OHA Acquisition](https://finance.yahoo.com/news/anew-oha-led-investor-consortium-154600963.html))

**7.5** What is the annual property tax revenue Fayette County currently receives from the 287 parcels comprising this dataset, and how does that figure compare to the assessed value and tax obligation of equivalent privately-held timberland in the same county? What is the cumulative fiscal impact of the differential on county public services since the date of original acquisition?

**7.6** What is the full scope of Orbis Inc.'s commercial relationship with institutional timberland investors holding NMTC-financed land in West Virginia, and was that relationship disclosed to the National Science Foundation and West Virginia University in connection with Orbis's NSF-funded equity partnership? ([Orbis Inc. — WVU Partnership](https://orbisinc.com/orbis-inc-announces-partnership-with-west-virginia-university-for-project-connecting-underserved-communities))

**7.7** Given that Oak Hill Advisors is now a subsidiary of T. Rowe Price — a global investment manager with $1.61 trillion in assets under management — does T. Rowe Price's fiduciary and institutional governance framework include any mechanism for reviewing NMTC community benefit compliance obligations inherited through portfolio acquisition? ([Paul Weiss — T. Rowe Price / OHA Acquisition](https://www.paulweiss.com/insights/client-news/oak-hill-advisors-to-be-acquired-by-t-rowe-price-for-42-billion))

---

## 8. Recommendations for Further Investigation

### 8.1 Immediate Public Records Actions

- Submit a Freedom of Information Act (FOIA) request to the U.S. Department of the Treasury CDFI Fund for all compliance documentation, community benefit reports, and board representation records associated with Oak Hill Forestlands NMTC LLC, including the identity of the CDE allocatee through which the NMTC financing was deployed ([CDFI Fund Contact](https://www.cdfifund.gov))
- Submit a formal inquiry to the Fayette County Assessor's office for annual assessed value and property tax records for all 287 parcels identified in this dataset, with a comparative analysis against equivalent privately-held timberland parcels in the same county
- Search the WV Secretary of State database for all corporate entities registered to 55 Vilcom Center Drive Chapel Hill NC and the Orbis Inc. Charlotte address to establish the full scope of institutional timberland holdings across all West Virginia counties ([WV SOS Business Search](https://apps.sos.wv.gov/business/corporations/))

### 8.2 Legislative and Regulatory Referral

- Referral to West Virginia's federal congressional delegation — Senator Capito, Senator Morrisey, and Congressman Miller — for formal inquiry to the CDFI Fund regarding NMTC community benefit compliance oversight in rural timberland transactions in West Virginia
- Referral to the West Virginia Legislature's Finance and Natural Resources committees for examination of state-level oversight mechanisms applicable to absentee institutional timberland ownership, property tax minimization practices, and carbon credit revenue extraction
- Inquiry to the National Science Foundation Office of Inspector General regarding conflict of interest disclosure requirements applicable to the Orbis Inc. / WVU equity partnership grant in light of Orbis's concurrent commercial operations in West Virginia communities

### 8.3 Academic and Policy Engagement

- Engagement with the WV Center on Budget and Policy for an updated statewide analysis of institutional timberland ownership concentration incorporating systematic NMTC financing identification across all 55 West Virginia counties
- Engagement with WVU's Division of Forestry and Natural Resources regarding the full institutional context of the Orbis partnership and the opportunity for collaborative research examining community benefit outcomes in NMTC-financed timberland transactions across Appalachia
- Replication of this spatial analysis methodology across Nicholas, Wyoming, McDowell, Logan, Mingo, and additional West Virginia counties where comparable institutional ownership patterns are anticipated based on the WV Center on Budget and Policy's 2013 statewide landowner documentation
- Engagement with the Appalachian Citizens' Law Center and Appalachian Mountain Advocates regarding legal mechanisms for community benefit enforcement under NMTC program compliance frameworks

---

## 9. Complete Source Reference

| Finding | Source | URL |
|---|---|---|
| Parcel data — entity names, acreage, county distribution | Fayette County Assessor Public Parcel Database | Public county record — independently verifiable through Fayette County Assessor's office |
| Corporate registration, registered address, managers | WV Secretary of State — Oak Hill Forestlands NMTC LLC | [SOS Org. 339624](https://apps.sos.wv.gov/business/corporations/organization.aspx?org=339624) |
| TFG AUM, portfolio scale, carbon credit production, UN PRI affiliation | The Forestland Group — UNEP Finance Initiative Investor Overview | [PDF](https://www.unepfi.org/wordpress/wp-content/uploads/2021/02/01_The-Forestland-Group-Overview.pdf) |
| TFG carbon credit marketing, ESG branding, institutional client base | The Forestland Group — CE Media Institutional Sponsor Profile | [ce-em.com](https://ce-em.com/community/all-sponsors/the-forestland-group-tfg/) |
| Orbis service offerings, TFG endorsement quote | Orbis Inc. — Business Solutions for Timberland Property Management | [orbisinc.com](https://orbisinc.com/services/business-solutions/) |
| Orbis / WVU NSF equity partnership | Orbis Inc. — Partnership Announcement, April 2022 | [orbisinc.com](https://orbisinc.com/orbis-inc-announces-partnership-with-west-virginia-university-for-project-connecting-underserved-communities) |
| NMTC program statutory requirements, community benefit mandate | CBO Financial — West Virginia NMTC Program Overview | [cbofinancial.com](https://cbofinancial.com/financing/cdfi/new-markets-tax-credit/west-virginia/) |
| NMTC program statute and administration | U.S. Treasury CDFI Fund — NMTC Program | [cdfifund.gov](https://www.cdfifund.gov/programs-training/programs/new-markets-tax-credit) |
| NMTC allocatee awards — searchable federal database | U.S. Treasury CDFI Fund | [cdfifund.gov/awards/nmtc](https://www.cdfifund.gov/awards/nmtc) |
| TFG portfolio acquisition by Anew Climate / Oak Hill Advisors | Yahoo Finance — Press Release, November 2, 2022 | [Yahoo Finance](https://finance.yahoo.com/news/anew-oha-led-investor-consortium-154600963.html) |
| T. Rowe Price acquisition of Oak Hill Advisors for $4.2 billion | Institutional Investor, October 2021 | [institutionalinvestor.com](https://www.institutionalinvestor.com/article/2bsws3k22w3gomzxgcsn4/portfolio/t-rowe-price-to-acquire-oak-hill-advisors-for-4-2-billion) |
| T. Rowe Price / OHA acquisition legal documentation | Paul Weiss Client Alert, October 2021 | [paulweiss.com](https://www.paulweiss.com/insights/client-news/oak-hill-advisors-to-be-acquired-by-t-rowe-price-for-42-billion) |
| Robert Bass biography, Oak Hill capital lineage | Wikipedia — Robert Bass | [wikipedia.org](https://en.wikipedia.org/wiki/Robert_Bass) |
| Sid W. Richardson — Bass family oil fortune origin | D Magazine — Sid Richardson: Fort Worth's Philanthropic Oil Baron, February 2025 | [dmagazine.com](https://www.dmagazine.com/publications/d-ceo/2025/january-february/sid-richardson-fort-worth-s-philanthropic-oil-baron/) |
| Lyme Timber NMTC transaction — community benefit documentation standard | CEI Capital Management — Press Release, August 2018 | [ceimaine.org](https://www.ceimaine.org/news-and-events/news/2018/08/ccml-financing-of-the-lyme-timber-company-introduces-new-safe-logging-tech) |
| WV timberland ownership concentration history — TFG as largest WV landowner | WV Center on Budget and Policy — Land Ownership Study, December 2013 | [wvpolicy.org](https://wvpolicy.org/wp-content/uploads/2018/5/land-study-paper-final3.pdf) |
| WV forest carbon credit mechanisms and market structure | WV Highlands Conservancy — Forest Carbon Capture Analysis, November 2023 | [wvhighlands.org](https://www.wvhighlands.org/article/forest-carbon-capture-what-is-going-on/) |

---

## 10. Conclusion

The spatial analysis documented in this case study establishes, through public records alone, that a single institutional timberland investment management organization headquartered in Chapel Hill, North Carolina holds 50,697 acres across 287 parcels in Fayette County, West Virginia — a holding assembled in part through federal New Markets Tax Credit financing instruments legally conditioned on the delivery of community benefit to one of the most economically distressed counties in the United States.

The analysis further establishes that the current beneficial ownership of this portfolio traces through Oak Hill Advisors — a subsidiary of T. Rowe Price, itself a $1.61 trillion global investment manager — to a capital lineage rooted in Texas petroleum extraction wealth originating with Sid W. Richardson and institutionalized through the Bass family investment empire. The commodity of extraction has evolved from petroleum to timber to carbon sequestration value. The structural relationship between absentee capital and Appalachian community has not.

The operational infrastructure supporting these holdings is managed by a Charlotte, North Carolina technology firm that simultaneously holds a federally funded equity partnership with West Virginia University focused on underserved community development — a relationship that has not been publicly examined in light of the firm's commercial function as the operational backbone of institutional land asset extraction in the communities that partnership ostensibly serves.

No public record has been identified documenting the community benefit delivery required under NMTC program compliance standards for the Oak Hill Forestlands NMTC LLC transaction. In the absence of such documentation, the federal subsidy extended to facilitate this acquisition represents an unresolved accountability gap that merits formal inquiry by the CDFI Fund, the West Virginia congressional delegation, the National Science Foundation, and relevant state legislative bodies.

The data was publicly available. The records were always accessible. The capital lineage was traceable through public sources. The findings presented here required no proprietary information, no institutional access, and no extraordinary resources — only the analytical infrastructure to integrate and interrogate public records at scale, and the community standing to ask the questions that infrastructure makes possible.

That infrastructure now exists in Fayette County.

---

*Produced by Kidd's Technical Services, Inc. — Mount Hope, West Virginia*
*Advanced Location Intelligence Infrastructure: Ms. Egeria Jarvis GIS System*
*Public Documentation Repository: [github.com/H4HWV2011/msjarvis-public-docs](https://github.com/H4HWV2011/msjarvis-public-docs)*
*License: Creative Commons Attribution 4.0 International (CC BY 4.0)*
*All data sources utilized in this analysis are publicly available and independently verifiable by any researcher or member of the public.*
*Date of publication: March 20, 2026*
*Correspondence and inquiries: Kidd's Technical Services, Inc. — Mount Hope, West Virginia*
