(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:/opt/msjarvis-rebuild$ python3 << 'EOF'
import csv

print("=== ROUTED — ALL RESULTS FOR ANNOTATION ===\n")
with open('/tmp/annotation_routed_v2.csv') as f:
    rows = list(csv.DictReader(f))

current_qid = None
for r in rows:
    qid = r['query_id']
    if qid != current_qid:
        current_qid = qid
        print(f"\n{'─'*70}")
        print(f"Q{qid} [{r['category']}]: {r['query']}")
        print(f"{'─'*70}")
    dist = r.get('distance','')
    print(f"  Rank {r['rank']} (dist={dist}): {r['document_preview'][:120]}")

print("\n\n=== UNROUTED — ALL RESULTS FOR ANNOTATION ===\n")
with open('/tmp/annotation_unrouted_v2.csv') as f:
    rows = list(csv.DictReader(f))

current_qid = None
for r in rows:
    qid = r['query_id']
    if qid != current_qid:
        current_qid = qid
EOF print(f"  Rank {r['rank']} (dist={dist}): {r['document_preview'][:120]}")
=== ROUTED — ALL RESULTS FOR ANNOTATION ===


──────────────────────────────────────────────────────────────────────
Q1 [emergency]: Where can I get emergency food assistance in Oak Hill?
──────────────────────────────────────────────────────────────────────
  Rank 1 (dist=0.4935): faith communities, mutual aid, youth orgs,
  local government, economic development, health/food access, cultural preser
  Rank 2 (dist=0.5188): Oak Hill Volunteer Fire Department | fire department | 582 Virginia Street Oak Hill WV 25901 Oak Hill WV | phone: 304-46
  Rank 3 (dist=0.5386): Practical Living Words Ministry Inc. | school | 1880 Summerlee Road Oak Hill WV | phone:  | county: 54019 | state: WV
  Rank 4 (dist=0.5407): ount Hope area)
- WV Department of Human Services community liaisons

## Issue Intake
Submit concerns at: docs/governanc
  Rank 5 (dist=0.5464): Oak Hill Public Library | library | 611 Main Street Oak Hill WV | phone: 304 469 9890 | county: ? | state: WV

──────────────────────────────────────────────────────────────────────
Q2 [emergency]: Is there a food pantry near Fayetteville WV?
──────────────────────────────────────────────────────────────────────
  Rank 1 (dist=0.4826): faith communities, mutual aid, youth orgs,
  local government, economic development, health/food access, cultural preser
  Rank 2 (dist=0.5621): Fayette Nursing and Rehabilitation Center - AMFM Nursing & Rehab Centers | nursing home | 100 Hresan Boulevard Fayettevi
  Rank 3 (dist=0.5663): Hilltop Center | nursing home | P.O. Box 125 WV | phone: 469-2966 | county: Fayette | state: WV
  Rank 4 (dist=0.5735): Hilltop Center - Genesis Healthcare | nursing home | 152 Saddle Shop Road Hilltop WV 25855 | phone: 304-469-2966 | beds:
  Rank 5 (dist=0.5775): Fayette Nursing and Rehabilitation Center, Inc. | nursing home | 100 Hresan Boulevard WV | phone: 574-0770 | county: Fay

──────────────────────────────────────────────────────────────────────
Q3 [emergency]: How do I apply for SNAP in Fayette County?
──────────────────────────────────────────────────────────────────────
  Rank 1 (dist=0.5318): Divide Elementary School | school | 334 Propps Ridge Lookout WV 25868 nan WV | phone: 304-574-1443 | county: Fayette | s
  Rank 2 (dist=0.5337): Hilltop Center | nursing home | P.O. Box 125 WV | phone: 469-2966 | county: Fayette | state: WV
  Rank 3 (dist=0.5476): Valley PK-8 School | school | 55 Greyhound Lane Smithers WV | phone: nan | county: Fayette | state: WV
  Rank 4 (dist=0.5480): Boomer Christian Academy | school | 34 Christian School Drive Boomer WV | phone: nan | county: Fayette | state: WV
  Rank 5 (dist=0.5689): Sharples Volunteer Fire Department | fire department | 25 Signature Circle Sharples WV 25183 Sharples WV | phone: 304-36

──────────────────────────────────────────────────────────────────────
Q4 [emergency]: My family needs food help this week in Mount Hope
──────────────────────────────────────────────────────────────────────
  Rank 1 (dist=0.4724): faith communities, mutual aid, youth orgs,
  local government, economic development, health/food access, cultural preser
  Rank 2 (dist=0.5389): Mount Hope Volunteer Fire Department | fire department | 644 Main Street Mount Hope WV 25880 Mount Hope WV | phone: 304-
  Rank 3 (dist=0.5754): Mt Hope Public Library | library | 500 Main Street Mt. Hope WV | phone: 304 877 3260 | county: ? | state: WV
  Rank 4 (dist=0.5911): Wishing Well Health Center | nursing home | 1539 Country Club Road WV | phone: 366-9100 | county: Marion | state: WV
  Rank 5 (dist=0.5924): Feed My Sheep | school | 260 North High Street Philippi WV | phone: nan | county: Barbour | state: WV

──────────────────────────────────────────────────────────────────────
Q5 [emergency]: What food banks are open in Fayette County?
──────────────────────────────────────────────────────────────────────
  Rank 1 (dist=0.5139): Green bank Public Library | library | P.O. Box 1, Rt 28 Green Bank WV | phone: 304 456 4507 | county: ? | state: WV
  Rank 2 (dist=0.5173): faith communities, mutual aid, youth orgs,
  local government, economic development, health/food access, cultural preser
  Rank 3 (dist=0.5527): Ansted Center | nursing home | P.O. Drawer 400 WV | phone: 658-5271 | county: Fayette | state: WV
  Rank 4 (dist=0.5730): Montgomery General Elderly Care | nursing home | P.O. Box 1010 WV | phone: 442-2469 | county: Fayette | state: WV
  Rank 5 (dist=0.5734): Hilltop Center | nursing home | P.O. Box 125 WV | phone: 469-2966 | county: Fayette | state: WV

──────────────────────────────────────────────────────────────────────
Q6 [utility]: How do I apply for LIEAP in West Virginia?
──────────────────────────────────────────────────────────────────────
  Rank 1 (dist=0.4653): by applicable law and policy). - Residency: Primary residence address in West Virginia. - Identity verification: KYC and
  Rank 2 (dist=0.5040): Geographic Scope - Phase 1 deployment is limited to Users and Merchants whose primary residence or operations are locate
  Rank 3 (dist=0.5046): with employers, landlords, or community organizations, and accessible only by Ms. Jarvis for system enforcement purposes
  Rank 4 (dist=0.5151): West Virginia State University | higher education | 5000 Fairlawn Avenue Institute WV 25112 WV | phone: (304) 766-3000 |
  Rank 5 (dist=0.5182): legal prerequisites to MountainShares operating at Phase 2 scale; governed by Section 7A - **Annual Regulatory Complianc

──────────────────────────────────────────────────────────────────────
Q7 [utility]: My power is about to be shut off in Fayette County
──────────────────────────────────────────────────────────────────────
  Rank 1 (dist=0.5760): Fayette County E-911 | 911 emergency center | 1047 Nick Rahall Greenway Fayetteville WV 25840 WV | phone: 304-574-3590 |
  Rank 2 (dist=0.6041): Fayetteville Public Library | library | 200 W Maple Avenue Fayetteville WV | phone: 304 574 0070 | county: ? | state: WV
  Rank 3 (dist=0.6122): Fayetteville Fire Department | fire department | 177 Lively Street Fayetteville WV 25840 Fayetteville WV | phone: 304-57
  Rank 4 (dist=0.6190): Fayette Nursing and Rehabilitation Center, Inc. | nursing home | 100 Hresan Boulevard WV | phone: 574-0770 | county: Fay
  Rank 5 (dist=0.6217): Fayette County Sheriffs Office - Danese Detachment | police department | 6411 Meadow Bridge Road Danese WV 25831 WV | ph

──────────────────────────────────────────────────────────────────────
Q8 [utility]: Is there utility assistance for low income families near Oak Hill?
──────────────────────────────────────────────────────────────────────
  Rank 1 (dist=0.5027): faith communities, mutual aid, youth orgs,
  local government, economic development, health/food access, cultural preser
  Rank 2 (dist=0.5163): of profit distributions from Harmony for Hope. --- ## 5. Use of Program Revenues (Charitable Intent) Program revenues an
  Rank 3 (dist=0.5163): of profit distributions from Harmony for Hope. --- ## 5. Use of Program Revenues (Charitable Intent) Program revenues an
  Rank 4 (dist=0.5467): your community role. For all other programs — SNAP, Medicaid, WV WORKS, housing assistance — the system does not apply a
  Rank 5 (dist=0.5470): Sand Hill Library | library | Sand Hill Elementary, Rt 1 Box 87 Dallas WV | phone: 304 547 5041 | county: ? | state: WV

──────────────────────────────────────────────────────────────────────
Q9 [utility]: Who do I call for emergency heating help in Fayette County WV?
──────────────────────────────────────────────────────────────────────
  Rank 1 (dist=0.3994): Fayette County E-911 | 911 emergency center | 1047 Nick Rahall Greenway Fayetteville WV 25840 WV | phone: 304-574-3590 |
  Rank 2 (dist=0.4167): Summers County E-911 | 911 emergency center | 451 1st Avenue Suite 101 Hinton WV 25951 WV | phone: 304-466-5613 | county
  Rank 3 (dist=0.4328): White Sulphur Springs Volunteer Fire Department | fire department | 195 Bob White Lane White Sulphur Springs WV 24986 Wh
  Rank 4 (dist=0.4372): Hilltop Center | nursing home | P.O. Box 125 WV | phone: 469-2966 | county: Fayette | state: WV
  Rank 5 (dist=0.4390): Main Street Care | nursing home | 189 Summers Hospital Road Suite 300 Hinton WV 25951 | phone: 304-466-6090 | beds: 34.0

──────────────────────────────────────────────────────────────────────
Q10 [utility]: What programs help pay electric bills in southern West Virginia?
──────────────────────────────────────────────────────────────────────
  Rank 1 (dist=0.5168): fee revenue is allocated between treasury reserves, organizational operations, infrastructure, and community programs. -
  Rank 2 (dist=0.5168): fee revenue is allocated between treasury reserves, organizational operations, infrastructure, and community programs. -
  Rank 3 (dist=0.5567): legal prerequisites to MountainShares operating at Phase 2 scale; governed by Section 7A - **Annual Regulatory Complianc
  Rank 4 (dist=0.5600): 30% | Harmony for Hope, Inc. (H4H Operations) | Covers nonprofit administration, staffing, compliance, legal, and progra
  Rank 5 (dist=0.5738): faith communities, mutual aid, youth orgs,
  local government, economic development, health/food access, cultural preser

──────────────────────────────────────────────────────────────────────
Q11 [housing]: How do I apply for Section 8 in Fayette County?
──────────────────────────────────────────────────────────────────────
  Rank 1 (dist=0.4589): Divide Elementary School | school | 334 Propps Ridge Lookout WV 25868 nan WV | phone: 304-574-1443 | county: Fayette | s
  Rank 2 (dist=0.5271): Valley PK-8 School | school | 55 Greyhound Lane Smithers WV | phone: nan | county: Fayette | state: WV
  Rank 3 (dist=0.5391): Fayette County E-911 | 911 emergency center | 1047 Nick Rahall Greenway Fayetteville WV 25840 WV | phone: 304-574-3590 |
  Rank 4 (dist=0.5523): Wiley Ford Primary School | school | 71 Wiley Ford School Road Wiley Ford WV 26767 nan WV | phone: 304-738-0400 | county
  Rank 5 (dist=0.5553): Boomer Christian Academy | school | 34 Christian School Drive Boomer WV | phone: nan | county: Fayette | state: WV

──────────────────────────────────────────────────────────────────────
Q12 [housing]: Is there emergency housing assistance near Fayetteville?
──────────────────────────────────────────────────────────────────────
  Rank 1 (dist=0.4455): Fayette County E-911 | 911 emergency center | 1047 Nick Rahall Greenway Fayetteville WV 25840 WV | phone: 304-574-3590 |
  Rank 2 (dist=0.4572): Hilltop Center | nursing home | P.O. Box 125 WV | phone: 469-2966 | county: Fayette | state: WV
  Rank 3 (dist=0.4634): Fayette Nursing and Rehabilitation Center - AMFM Nursing & Rehab Centers | nursing home | 100 Hresan Boulevard Fayettevi
  Rank 4 (dist=0.4684): Ansted Center | nursing home | P.O. Drawer 400 WV | phone: 658-5271 | county: Fayette | state: WV
  Rank 5 (dist=0.4784): Fayette Nursing and Rehabilitation Center, Inc. | nursing home | 100 Hresan Boulevard WV | phone: 574-0770 | county: Fay

──────────────────────────────────────────────────────────────────────
Q13 [housing]: Who handles HUD housing vouchers in southern WV?
──────────────────────────────────────────────────────────────────────
  Rank 1 (dist=0.4544): - WV WORKS/TANF; - SNAP; - Medicaid, WV CHIP, or other medical assistance; - HUD or other housing assistance; or - State
  Rank 2 (dist=0.5173): (add new forms, e.g., community project investment elections), *subject to legal review* ✅ **Distribution confirmation t
  Rank 3 (dist=0.5267): may never be activated or may only apply to limited categories of MountainShares or Users. Internal buying‑power schedul
  Rank 4 (dist=0.5520): # Benefits‑Sensitive Accounts – Plain Language Notice *(Draft – For Discussion, Not Legal Advice)* This notice explains 
  Rank 5 (dist=0.5569): adjusts: - **Weekly:** County-level network snapshots added to the standard weekly report - **Monthly:** Per-county trea

──────────────────────────────────────────────────────────────────────
Q14 [housing]: Where can I get help with rent in Oak Hill West Virginia?
──────────────────────────────────────────────────────────────────────
  Rank 1 (dist=0.4474): Oak Hill Volunteer Fire Department | fire department | 582 Virginia Street Oak Hill WV 25901 Oak Hill WV | phone: 304-46
  Rank 2 (dist=0.4641): Oak Hill Public Library | library | 611 Main Street Oak Hill WV | phone: 304 469 9890 | county: ? | state: WV
  Rank 3 (dist=0.4772): West Virginia State Police Troop 6 - Oak Hill Detachment | police department | 3057 Main Street East Oak Hill WV 25901 W
  Rank 4 (dist=0.4800): Practical Living Words Ministry Inc. | school | 1880 Summerlee Road Oak Hill WV | phone:  | county: 54019 | state: WV
  Rank 5 (dist=0.4949): Oak Ridge Center - Genesis Healthcare | nursing home | 1000 Association Drive Charleston WV 25311 | phone: 304-347-4372 

──────────────────────────────────────────────────────────────────────
Q15 [housing]: What homeless shelters are in Fayette County?
──────────────────────────────────────────────────────────────────────
  Rank 1 (dist=0.4668): Hilltop Center | nursing home | P.O. Box 125 WV | phone: 469-2966 | county: Fayette | state: WV
  Rank 2 (dist=0.4998): Fayette Nursing and Rehabilitation Center, Inc. | nursing home | 100 Hresan Boulevard WV | phone: 574-0770 | county: Fay
  Rank 3 (dist=0.5042): Fayette Nursing and Rehabilitation Center - AMFM Nursing & Rehab Centers | nursing home | 100 Hresan Boulevard Fayettevi
  Rank 4 (dist=0.5088): Hilltop Center - Genesis Healthcare | nursing home | 152 Saddle Shop Road Hilltop WV 25855 | phone: 304-469-2966 | beds:
  Rank 5 (dist=0.5163): Ansted Center | nursing home | P.O. Drawer 400 WV | phone: 658-5271 | county: Fayette | state: WV

──────────────────────────────────────────────────────────────────────
Q16 [health]: How do I apply for Medicaid in Fayette County?
──────────────────────────────────────────────────────────────────────
  Rank 1 (dist=0.4200): Montgomery General Elderly Care | nursing home | P.O. Box 1010 WV | phone: 442-2469 | county: Fayette | state: WV
  Rank 2 (dist=0.4863): Hilltop Center | nursing home | P.O. Box 125 WV | phone: 469-2966 | county: Fayette | state: WV
  Rank 3 (dist=0.4898): Fayette Nursing and Rehabilitation Center, Inc. | nursing home | 100 Hresan Boulevard WV | phone: 574-0770 | county: Fay
  Rank 4 (dist=0.4911): Montgomery General Elderly Care | nursing home | 335 Sixth Avenue Montgomery WV 25136 | phone: 304-442-2469 | beds: 60.0
  Rank 5 (dist=0.5043): Montgomery General Hospital, D/P | nursing home | Washington St. & 6th Ave. WV | phone: 442-5151 | county: Fayette | sta

──────────────────────────────────────────────────────────────────────
Q17 [health]: Where is the nearest DHHR office to Oak Hill WV?
──────────────────────────────────────────────────────────────────────
  Rank 1 (dist=0.3973): Oak Hill Public Library | library | 611 Main Street Oak Hill WV | phone: 304 469 9890 | county: ? | state: WV
  Rank 2 (dist=0.3998): Oak Hill Volunteer Fire Department | fire department | 582 Virginia Street Oak Hill WV 25901 Oak Hill WV | phone: 304-46
  Rank 3 (dist=0.4529): Practical Living Words Ministry Inc. | school | 1880 Summerlee Road Oak Hill WV | phone:  | county: 54019 | state: WV
  Rank 4 (dist=0.4626): Oak Hill Parole Office | parole facility | 1307 Main Street East Oak Hill WV | county: Fayette | state: WV
  Rank 5 (dist=0.4629): Fayette Co. Public Library | library | 531 Summit Street Oak Hill WV | phone: 304 465 0121 | county: ? | state: WV

──────────────────────────────────────────────────────────────────────
Q18 [health]: What free clinics are available in Fayette County?
──────────────────────────────────────────────────────────────────────
  Rank 1 (dist=0.4387): Fayetteville Clinic | health | Fayetteville WV 25840 | Free health clinic
  Rank 2 (dist=0.4883): Montgomery General Elderly Care | nursing home | P.O. Box 1010 WV | phone: 442-2469 | county: Fayette | state: WV
  Rank 3 (dist=0.4945): Hilltop Center | nursing home | P.O. Box 125 WV | phone: 469-2966 | county: Fayette | state: WV
  Rank 4 (dist=0.5004): Fayette Nursing and Rehabilitation Center, Inc. | nursing home | 100 Hresan Boulevard WV | phone: 574-0770 | county: Fay
  Rank 5 (dist=0.5120): Montgomery General Hospital, D/P | nursing home | Washington St. & 6th Ave. WV | phone: 442-5151 | county: Fayette | sta

──────────────────────────────────────────────────────────────────────
Q19 [health]: How do I get health insurance if I cannot afford it in WV?
──────────────────────────────────────────────────────────────────────
  Rank 1 (dist=0.5338): West Virginia School of Osteopathic Medicine | higher education | 400 North Lee Street Lewisburg WV 24901 WV | phone: (8
  Rank 2 (dist=0.5345): - WV WORKS/TANF; - SNAP; - Medicaid, WV CHIP, or other medical assistance; - HUD or other housing assistance; or - State
  Rank 3 (dist=0.5365): WV University Hospital, D/P | nursing home | Medical Center Drive WV | phone: 598-4704 | county: Monongalia | state: WV
  Rank 4 (dist=0.5432): Care Haven Center - Genesis Healthcare | nursing home | 2720 Charles Town Road Martinsburg WV 25405 | phone: 304-263-093
  Rank 5 (dist=0.5526): Care Haven Center | nursing home | 2720 Charles Town Road WV | phone: 263-0933 | county: Berkeley | state: WV

──────────────────────────────────────────────────────────────────────
Q20 [health]: Who helps with Medicare enrollment in southern West Virginia?
──────────────────────────────────────────────────────────────────────
  Rank 1 (dist=0.5246): when making decisions about your benefits.* --- *Version 2.0 — Rewritten March 2026* *Authors: Carrie Kidd (Mamma Kidd),
  Rank 2 (dist=0.5266): faith communities, mutual aid, youth orgs,
  local government, economic development, health/food access, cultural preser
  Rank 3 (dist=0.5438): ount Hope area)
- WV Department of Human Services community liaisons

## Issue Intake
Submit concerns at: docs/governanc
  Rank 4 (dist=0.5468): Valley Center - Genesis Healthcare | nursing home | 1000 Lincoln Drive South Charleston WV 25309 | phone: 304-768-4400 |
  Rank 5 (dist=0.5470): - WV WORKS/TANF; - SNAP; - Medicaid, WV CHIP, or other medical assistance; - HUD or other housing assistance; or - State

──────────────────────────────────────────────────────────────────────
Q21 [childcare]: Is there childcare assistance available in Fayette County?
──────────────────────────────────────────────────────────────────────
  Rank 1 (dist=0.4192): Hilltop Center | nursing home | P.O. Box 125 WV | phone: 469-2966 | county: Fayette | state: WV
  Rank 2 (dist=0.4252): Ansted Center | nursing home | P.O. Drawer 400 WV | phone: 658-5271 | county: Fayette | state: WV
  Rank 3 (dist=0.4320): Divide Elementary School | school | 334 Propps Ridge Lookout WV 25868 nan WV | phone: 304-574-1443 | county: Fayette | s
  Rank 4 (dist=0.4387): Fayette Nursing and Rehabilitation Center, Inc. | nursing home | 100 Hresan Boulevard WV | phone: 574-0770 | county: Fay
  Rank 5 (dist=0.4500): Montgomery General Elderly Care | nursing home | P.O. Box 1010 WV | phone: 442-2469 | county: Fayette | state: WV

──────────────────────────────────────────────────────────────────────
Q22 [childcare]: How do I apply for the WV childcare subsidy program?
──────────────────────────────────────────────────────────────────────
  Rank 1 (dist=0.4881): - WV WORKS/TANF; - SNAP; - Medicaid, WV CHIP, or other medical assistance; - HUD or other housing assistance; or - State
  Rank 2 (dist=0.5167): Applied Behavior Learning Center | school | 325 6th Avenue South Charleston WV | phone: nan | county: Kanawha | state: W
  Rank 3 (dist=0.5350): Mother Goose Land Day Care | school | 401 West Virginia Avenue Nutter Fort WV | phone:  | county: 54033 | state: WV
  Rank 4 (dist=0.5457): Divide Elementary School | school | 334 Propps Ridge Lookout WV 25868 nan WV | phone: 304-574-1443 | county: Fayette | s
  Rank 5 (dist=0.5538): The Light of the Child Montessori School | school | 112 North King Street Shepherdstown WV | phone:  | county: 54037 | s

──────────────────────────────────────────────────────────────────────
Q23 [childcare]: Where can I find affordable daycare near Oak Hill?
──────────────────────────────────────────────────────────────────────
  Rank 1 (dist=0.4847): Sand Hill Library | library | Sand Hill Elementary, Rt 1 Box 87 Dallas WV | phone: 304 547 5041 | county: ? | state: WV
  Rank 2 (dist=0.5074): Brightwood Center | nursing home | 840 Lee Road WV | phone: 527-1100 | county: Brooke | state: WV
  Rank 3 (dist=0.5114): Oak Ridge Center | nursing home | 1000 Association Drive WV | phone: 347-4372 | county: Kanawha | state: WV
  Rank 4 (dist=0.5121): Oak Hill Public Library | library | 611 Main Street Oak Hill WV | phone: 304 469 9890 | county: ? | state: WV
  Rank 5 (dist=0.5257): Practical Living Words Ministry Inc. | school | 1880 Summerlee Road Oak Hill WV | phone:  | county: 54019 | state: WV

──────────────────────────────────────────────────────────────────────
Q24 [childcare]: What programs help pay for childcare in southern WV?
──────────────────────────────────────────────────────────────────────
  Rank 1 (dist=0.4901): - WV WORKS/TANF; - SNAP; - Medicaid, WV CHIP, or other medical assistance; - HUD or other housing assistance; or - State
  Rank 2 (dist=0.5207): Mother Goose Land Day Care | school | 401 West Virginia Avenue Nutter Fort WV | phone:  | county: 54033 | state: WV
  Rank 3 (dist=0.5253): faith communities, mutual aid, youth orgs,
  local government, economic development, health/food access, cultural preser
  Rank 4 (dist=0.5495): Applied Behavior Learning Center | school | 325 6th Avenue South Charleston WV | phone: nan | county: Kanawha | state: W
  Rank 5 (dist=0.5601): Education Dept | library | 1001 Centre Way Charleston WV | phone: 304 558 1336 | county: ? | state: WV

──────────────────────────────────────────────────────────────────────
Q25 [childcare]: I need help paying for preschool in Fayette County
──────────────────────────────────────────────────────────────────────
  Rank 1 (dist=0.4895): Divide Elementary School | school | 334 Propps Ridge Lookout WV 25868 nan WV | phone: 304-574-1443 | county: Fayette | s
  Rank 2 (dist=0.5175): Gauley Bridge Elementary School | school | 140 Walnut Street Gauley Bridge WV 25085 nan WV | phone: 304-632-2661 | count
  Rank 3 (dist=0.5308): Mount Hope Elementary School | school | 408 Lincoln Street Mount Hope WV 25880 nan WV | phone: 304-877-2891 | county: Fa
  Rank 4 (dist=0.5329): Watson Elementary School | school | 1579 Mary Lou Retton Drive Fairmont WV 26554 nan WV | phone: 304-367-2156 | county: 
  Rank 5 (dist=0.5372): West Fairmont Middle School | school | 110 Tenth Street Fairmont WV 26554 nan WV | phone: 304-366-5631 | county: Marion 

──────────────────────────────────────────────────────────────────────
Q26 [ssi]: How do I apply for SSI in West Virginia?
──────────────────────────────────────────────────────────────────────
  Rank 1 (dist=0.5226): WEST VIRGINIA STATE POLICE TROOP 4 - SAINT MARYS DETACHMENT | law enforcement | 1313 SECOND STREET SAINT MARYS WV | phon
  Rank 2 (dist=0.5229): Geographic Scope - Phase 1 deployment is limited to Users and Merchants whose primary residence or operations are locate
  Rank 3 (dist=0.5249): West Virginia State Police Troop 4 - Saint Marys Detachment | police department | 1313 Second Street Saint Marys WV 2617
  Rank 4 (dist=0.5250): WEST VIRGINIA STATE POLICE TROOP 4 - SOUTH CHARLESTON DETACHMENT | law enforcement | 711 JEFFERSON ROAD SOUTH CHARLESTON
  Rank 5 (dist=0.5344): West Virginia State Police Troop 4 - South Charleston Detachment | police department | 711 Jefferson Road South Charlest

──────────────────────────────────────────────────────────────────────
Q27 [ssi]: Where is the Social Security office nearest to Oak Hill WV?
──────────────────────────────────────────────────────────────────────
  Rank 1 (dist=0.4121): Oak Hill Volunteer Fire Department | fire department | 582 Virginia Street Oak Hill WV 25901 Oak Hill WV | phone: 304-46
  Rank 2 (dist=0.4322): Oak Hill Parole Office | parole facility | 1307 Main Street East Oak Hill WV | county: Fayette | state: WV
  Rank 3 (dist=0.4337): SS Peter & Paul Catholic School | school | 123 Elmore Street Oak Hill WV | phone:  | county: 54019 | state: WV
  Rank 4 (dist=0.4369): Oak Hill Public Library | library | 611 Main Street Oak Hill WV | phone: 304 469 9890 | county: ? | state: WV
  Rank 5 (dist=0.4437): Hidden Valley Center- Genesis Healthcare | nursing home | 422  23rd Street Oak Hill WV 25901 | phone: 304-465-1903 | bed

──────────────────────────────────────────────────────────────────────
Q28 [ssi]: What disability assistance programs are in Fayette County?
──────────────────────────────────────────────────────────────────────
  Rank 1 (dist=0.4591): Fayette Nursing and Rehabilitation Center, Inc. | nursing home | 100 Hresan Boulevard WV | phone: 574-0770 | county: Fay
  Rank 2 (dist=0.4652): Hilltop Center | nursing home | P.O. Box 125 WV | phone: 469-2966 | county: Fayette | state: WV
  Rank 3 (dist=0.4681): Montgomery General Elderly Care | nursing home | P.O. Box 1010 WV | phone: 442-2469 | county: Fayette | state: WV
  Rank 4 (dist=0.4728): Fayette Nursing and Rehabilitation Center - AMFM Nursing & Rehab Centers | nursing home | 100 Hresan Boulevard Fayettevi
  Rank 5 (dist=0.4944): SunBridge Care & Rehab for Dunbar | nursing home | 501 Caldwell Lane WV | phone: 744-4761 | county: Kanawha | state: WV

──────────────────────────────────────────────────────────────────────
Q29 [ssi]: I was denied SSI who can help me appeal in WV?
──────────────────────────────────────────────────────────────────────
  Rank 1 (dist=0.5917): Arthur B. Hodges Center | nursing home | 300 Baker Lane Charleston WV 25302 | phone: 304-346-2323 | beds: 20.0 | county:
  Rank 2 (dist=0.6134): West Virginia State University | higher education | 5000 Fairlawn Avenue Institute WV 25112 WV | phone: (304) 766-3000 |
  Rank 3 (dist=0.6195): West Virginia Division of Protective Services - Capitol Police | police department | 1900 Kanawha Boulevard East State C
  Rank 4 (dist=0.6263): DIVISION OF PROTECTIVE SERVICES | law enforcement | 1900 KANAWHA BOULEVARD EAST CHARLESTON WV | phone: 304-558-9911 | co
  Rank 5 (dist=0.6273): Guardian Elder Care (Peterson Rehab. Hosp. D/P) | nursing home | Homestead Avenue WV | phone: 234-0500 | county: Ohio | 

──────────────────────────────────────────────────────────────────────
Q30 [ssi]: What income help is available for disabled adults in Fayette County?
──────────────────────────────────────────────────────────────────────
  Rank 1 (dist=0.5208): faith communities, mutual aid, youth orgs,
  local government, economic development, health/food access, cultural preser
  Rank 2 (dist=0.5249): V60.6 (Z59.3) Problem Related to Living in a Residential Institution
This category should be used when a problem (or pro
  Rank 3 (dist=0.5394): Hilltop Center | nursing home | P.O. Box 125 WV | phone: 469-2966 | county: Fayette | state: WV
  Rank 4 (dist=0.5403): to your community and a way to access community resources in return. Here is what that means for your benefits: ### Your
  Rank 5 (dist=0.5456): Montgomery General Elderly Care | nursing home | P.O. Box 1010 WV | phone: 442-2469 | county: Fayette | state: WV


=== UNROUTED — ALL RESULTS FOR ANNOTATION ===


──────────────────────────────────────────────────────────────────────
Q1 [emergency]: Where can I get emergency food assistance in Oak Hill?
──────────────────────────────────────────────────────────────────────
  Rank 1 (dist=0.4635): Fire Department: Oak Hill Volunteer Fire Department, 582 Virginia Street Oak Hill WV 25901, Oak Hill, WV
  Rank 2 (dist=0.4934): rural_health Elk Garden Clinic health_rural_facilities lat:39.365643 lon:-79.174744 West Virginia WV
  Rank 3 (dist=0.4934): rural_health Elk Garden Clinic health_rural_facilities lat:39.365643 lon:-79.174744 West Virginia WV
  Rank 4 (dist=0.4934): rural_health Elk Garden Clinic health_rural_facilities lat:39.365643 lon:-79.174744 West Virginia WV
  Rank 5 (dist=0.4934): rural_health Elk Garden Clinic health_rural_facilities lat:39.365643 lon:-79.174744 West Virginia WV

──────────────────────────────────────────────────────────────────────
Q2 [emergency]: Is there a food pantry near Fayetteville WV?
──────────────────────────────────────────────────────────────────────
  Rank 1 (dist=0.4059): Mountaineer Food Bank hosting pantry in Fayette County on April 28. The organization will host a pantry at the Old Mount
  Rank 2 (dist=0.4296): Southern Appalachian Labor School hosting food pantry in Beards Fork on May 4. The Southern Appalachian Labor School wil
  Rank 3 (dist=0.4311): West Virginia Pepperoni Roll Museum to open this spring in Fayetteville
  Rank 4 (dist=0.4311): West Virginia Pepperoni Roll Museum to open this spring in Fayetteville
  Rank 5 (dist=0.4762): Library: Fayetteville Public Library, 200 W Maple Avenue, Fayetteville, WV

──────────────────────────────────────────────────────────────────────
Q3 [emergency]: How do I apply for SNAP in Fayette County?
──────────────────────────────────────────────────────────────────────
  Rank 1 (dist=0.5318): Divide Elementary School | school | 334 Propps Ridge Lookout WV 25868 nan WV | phone: 304-574-1443 | county: Fayette | s
  Rank 2 (dist=0.5337): Hilltop Center | nursing home | P.O. Box 125 WV | phone: 469-2966 | county: Fayette | state: WV
  Rank 3 (dist=0.5434): Law Enforcement: MINERAL COUNTY BAILIFFS OFFICE, 150 ARMSTRONG STREET, KEYSER, MINERAL County, WV
  Rank 4 (dist=0.5476): Valley PK-8 School | school | 55 Greyhound Lane Smithers WV | phone: nan | county: Fayette | state: WV
  Rank 5 (dist=0.5480): Boomer Christian Academy | school | 34 Christian School Drive Boomer WV | phone: nan | county: Fayette | state: WV

──────────────────────────────────────────────────────────────────────
Q4 [emergency]: My family needs food help this week in Mount Hope
──────────────────────────────────────────────────────────────────────
  Rank 1 (dist=0.4724): faith communities, mutual aid, youth orgs,
  local government, economic development, health/food access, cultural preser
  Rank 2 (dist=0.5130): Mountaineer Food Bank hosting pantry in Fayette County on April 28. The organization will host a pantry at the Old Mount
  Rank 3 (dist=0.5366): Additional Resources 
 
Find Help 
 
 
 
 
 
 https://www.findhelp.org/ 
 
Healthy Grandfamilies  
 
 
 
https://healthy
  Rank 4 (dist=0.5385): Fire Department: Mount Hope Volunteer Fire Department, 644 Main Street Mount Hope WV 25880, Mount Hope, WV
  Rank 5 (dist=0.5389): Mount Hope Volunteer Fire Department | fire department | 644 Main Street Mount Hope WV 25880 Mount Hope WV | phone: 304-

──────────────────────────────────────────────────────────────────────
Q5 [emergency]: What food banks are open in Fayette County?
──────────────────────────────────────────────────────────────────────
  Rank 1 (dist=0.4359): Mountaineer Food Bank hosting pantry in Fayette County on April 28. The organization will host a pantry at the Old Mount
  Rank 2 (dist=0.4714): Southern Appalachian Labor School hosting food pantry in Beards Fork on May 4. The Southern Appalachian Labor School wil
  Rank 3 (dist=0.4882): Mountaineer Food Bank stopping in Mercer and Monroe County this week. On Tuesday, May 5, the pantry will be in Mercer Co
  Rank 4 (dist=0.5118): rural_health Fayette Clinic PLLC health_rural_facilities lat:37.976612 lon:-81.097223 West Virginia WV
  Rank 5 (dist=0.5139): Green bank Public Library | library | P.O. Box 1, Rt 28 Green Bank WV | phone: 304 456 4507 | county: ? | state: WV

──────────────────────────────────────────────────────────────────────
Q6 [utility]: How do I apply for LIEAP in West Virginia?
──────────────────────────────────────────────────────────────────────
  Rank 1 (dist=0.4653): by applicable law and policy). - Residency: Primary residence address in West Virginia. - Identity verification: KYC and
  Rank 2 (dist=0.4667): WV opens application period for some Rural Health Transformation funds. The West Virginia Department of Health has start
  Rank 3 (dist=0.4814): rural_health S.K. Shammaa, M.D., Inc. health_rural_facilities lat:37.673593 lon:-80.890884 West Virginia WV
  Rank 4 (dist=0.4814): rural_health S.K. Shammaa, M.D., Inc. health_rural_facilities lat:37.673593 lon:-80.890884 West Virginia WV
  Rank 5 (dist=0.4814): rural_health S.K. Shammaa, M.D., Inc. health_rural_facilities lat:37.673593 lon:-80.890884 West Virginia WV

──────────────────────────────────────────────────────────────────────
Q7 [utility]: My power is about to be shut off in Fayette County
──────────────────────────────────────────────────────────────────────
  Rank 1 (dist=0.5760): Fayette County E-911 | 911 emergency center | 1047 Nick Rahall Greenway Fayetteville WV 25840 WV | phone: 304-574-3590 |
  Rank 2 (dist=0.6041): Fayetteville Public Library | library | 200 W Maple Avenue Fayetteville WV | phone: 304 574 0070 | county: ? | state: WV
  Rank 3 (dist=0.6122): Fayetteville Fire Department | fire department | 177 Lively Street Fayetteville WV 25840 Fayetteville WV | phone: 304-57
  Rank 4 (dist=0.6141): Fayette County Sheriff’s Office is investigating a death. The Fayette County Sheriff's Office is investigating a death i
  Rank 5 (dist=0.6190): Fayette Nursing and Rehabilitation Center, Inc. | nursing home | 100 Hresan Boulevard WV | phone: 574-0770 | county: Fay

──────────────────────────────────────────────────────────────────────
Q8 [utility]: Is there utility assistance for low income families near Oak Hill?
──────────────────────────────────────────────────────────────────────
  Rank 1 (dist=0.4676): Additional Resources 
 
Find Help 
 
 
 
 
 
 https://www.findhelp.org/ 
 
Healthy Grandfamilies  
 
 
 
https://healthy
  Rank 2 (dist=0.4870): Additional Resources Find Help https://www.findhelp.org/ Healthy Grandfamilies https://healthygrandfamilies.com/ Interna
  Rank 3 (dist=0.4887): 

- **Harmony for Hope operations and staff**, which provide organizational backbone for community programming and techn
  Rank 4 (dist=0.5027): faith communities, mutual aid, youth orgs,
  local government, economic development, health/food access, cultural preser
  Rank 5 (dist=0.5163): of profit distributions from Harmony for Hope. --- ## 5. Use of Program Revenues (Charitable Intent) Program revenues an

──────────────────────────────────────────────────────────────────────
Q9 [utility]: Who do I call for emergency heating help in Fayette County WV?
──────────────────────────────────────────────────────────────────────
  Rank 1 (dist=0.3994): Fayette County E-911 | 911 emergency center | 1047 Nick Rahall Greenway Fayetteville WV 25840 WV | phone: 304-574-3590 |
  Rank 2 (dist=0.4095): public_health FAYETTE COUNTY HEALTH DEPARTMENT public_health_depts_2009 lat:38.054048 lon:-81.103434 West Virginia WV
  Rank 3 (dist=0.4167): Summers County E-911 | 911 emergency center | 451 1st Avenue Suite 101 Hinton WV 25951 WV | phone: 304-466-5613 | county
  Rank 4 (dist=0.4328): White Sulphur Springs Volunteer Fire Department | fire department | 195 Bob White Lane White Sulphur Springs WV 24986 Wh
  Rank 5 (dist=0.4372): Hilltop Center | nursing home | P.O. Box 125 WV | phone: 469-2966 | county: Fayette | state: WV

──────────────────────────────────────────────────────────────────────
Q10 [utility]: What programs help pay electric bills in southern West Virginia?
──────────────────────────────────────────────────────────────────────
  Rank 1 (dist=0.5168): fee revenue is allocated between treasury reserves, organizational operations, infrastructure, and community programs. -
  Rank 2 (dist=0.5168): fee revenue is allocated between treasury reserves, organizational operations, infrastructure, and community programs. -
  Rank 3 (dist=0.5342): Additional Resources Find Help https://www.findhelp.org/ Healthy Grandfamilies https://healthygrandfamilies.com/ Interna
  Rank 4 (dist=0.5379): Additional Resources 
 
Find Help 
 
 
 
 
 
 https://www.findhelp.org/ 
 
Healthy Grandfamilies  
 
 
 
https://healthy
  Rank 5 (dist=0.5456): re implemented and respected in practice.

- **Program operations and partnerships**  
  - Managing relationships with l

──────────────────────────────────────────────────────────────────────
Q11 [housing]: How do I apply for Section 8 in Fayette County?
──────────────────────────────────────────────────────────────────────
  Rank 1 (dist=0.4589): Divide Elementary School | school | 334 Propps Ridge Lookout WV 25868 nan WV | phone: 304-574-1443 | county: Fayette | s
  Rank 2 (dist=0.5230): ARC Seeking Applicants for Leadership Development Program Focused on Multi-Sector Economic Development. <p>Public,&#160;
  Rank 3 (dist=0.5230): ARC Seeking Applicants for Leadership Development Program Focused on Multi-Sector Economic Development. <p>Public,&#160;
  Rank 4 (dist=0.5271): Valley PK-8 School | school | 55 Greyhound Lane Smithers WV | phone: nan | county: Fayette | state: WV
  Rank 5 (dist=0.5299): School: Wiley Ford Primary School, 71 Wiley Ford School Road Wiley Ford WV 26767, Mineral County, WV

──────────────────────────────────────────────────────────────────────
Q12 [housing]: Is there emergency housing assistance near Fayetteville?
──────────────────────────────────────────────────────────────────────
  Rank 1 (dist=0.4455): Fayette County E-911 | 911 emergency center | 1047 Nick Rahall Greenway Fayetteville WV 25840 WV | phone: 304-574-3590 |
  Rank 2 (dist=0.4572): Hilltop Center | nursing home | P.O. Box 125 WV | phone: 469-2966 | county: Fayette | state: WV
  Rank 3 (dist=0.4613): Nursing Home: Fayette Nursing and Rehabilitation Center, Inc., 100 Hresan Boulevard, Fayetteville, Fayette County, WV
  Rank 4 (dist=0.4634): Fayette Nursing and Rehabilitation Center - AMFM Nursing & Rehab Centers | nursing home | 100 Hresan Boulevard Fayettevi
  Rank 5 (dist=0.4684): Ansted Center | nursing home | P.O. Drawer 400 WV | phone: 658-5271 | county: Fayette | state: WV

──────────────────────────────────────────────────────────────────────
Q13 [housing]: Who handles HUD housing vouchers in southern WV?
──────────────────────────────────────────────────────────────────────
  Rank 1 (dist=0.4544): - WV WORKS/TANF; - SNAP; - Medicaid, WV CHIP, or other medical assistance; - HUD or other housing assistance; or - State
  Rank 2 (dist=0.4762): Emergency housing vouchers are ending early, leaving cities and renters scrambling. A New York City mom and domestic vio
  Rank 3 (dist=0.4959): The Change Initiative receives $380K grant to expand recovery housing in North Central West Virginia
  Rank 4 (dist=0.5173): (add new forms, e.g., community project investment elections), *subject to legal review* ✅ **Distribution confirmation t
  Rank 5 (dist=0.5250): WV youth aging out of foster care face waitlist for resources; Morrisey vetoes bill to address issue. Children’s Home So

──────────────────────────────────────────────────────────────────────
Q14 [housing]: Where can I get help with rent in Oak Hill West Virginia?
──────────────────────────────────────────────────────────────────────
  Rank 1 (dist=0.4474): Oak Hill Volunteer Fire Department | fire department | 582 Virginia Street Oak Hill WV 25901 Oak Hill WV | phone: 304-46
  Rank 2 (dist=0.4641): Oak Hill Public Library | library | 611 Main Street Oak Hill WV | phone: 304 469 9890 | county: ? | state: WV
  Rank 3 (dist=0.4737): Fire Department: Oak Hill Volunteer Fire Department, 582 Virginia Street Oak Hill WV 25901, Oak Hill, WV
  Rank 4 (dist=0.4772): West Virginia State Police Troop 6 - Oak Hill Detachment | police department | 3057 Main Street East Oak Hill WV 25901 W
  Rank 5 (dist=0.4800): Practical Living Words Ministry Inc. | school | 1880 Summerlee Road Oak Hill WV | phone:  | county: 54019 | state: WV

──────────────────────────────────────────────────────────────────────
Q15 [housing]: What homeless shelters are in Fayette County?
──────────────────────────────────────────────────────────────────────
  Rank 1 (dist=0.4005): [empty document]
  Rank 2 (dist=0.4668): Hilltop Center | nursing home | P.O. Box 125 WV | phone: 469-2966 | county: Fayette | state: WV
  Rank 3 (dist=0.4824): rural_health Fayette Clinic PLLC health_rural_facilities lat:37.976612 lon:-81.097223 West Virginia WV
  Rank 4 (dist=0.4888): 

- **Harmony for Hope operations and staff**, which provide organizational backbone for community programming and techn
  Rank 5 (dist=0.4986): Nursing Home: Fayette Nursing and Rehabilitation Center, Inc., 100 Hresan Boulevard, Fayetteville, Fayette County, WV

──────────────────────────────────────────────────────────────────────
Q16 [health]: How do I apply for Medicaid in Fayette County?
──────────────────────────────────────────────────────────────────────
  Rank 1 (dist=0.4200): Montgomery General Elderly Care | nursing home | P.O. Box 1010 WV | phone: 442-2469 | county: Fayette | state: WV
  Rank 2 (dist=0.4603): public_health FAYETTE COUNTY HEALTH DEPARTMENT public_health_depts_2009 lat:38.054048 lon:-81.103434 West Virginia WV
  Rank 3 (dist=0.4791): rural_health Fayette Clinic PLLC health_rural_facilities lat:37.976612 lon:-81.097223 West Virginia WV
  Rank 4 (dist=0.4863): Hilltop Center | nursing home | P.O. Box 125 WV | phone: 469-2966 | county: Fayette | state: WV
  Rank 5 (dist=0.4865): Many states unsure how to implement new Medicaid work requirements, KFF survey finds. WASHINGTON — State officials say t

──────────────────────────────────────────────────────────────────────
Q17 [health]: Where is the nearest DHHR office to Oak Hill WV?
──────────────────────────────────────────────────────────────────────
  Rank 1 (dist=0.3710): Fire Department: Oak Hill Volunteer Fire Department, 582 Virginia Street Oak Hill WV 25901, Oak Hill, WV
  Rank 2 (dist=0.3873): Law Enforcement: Oak Hill Police Department, 691 Virginia Street Oak Hill WV 25901, Fayette County, WV
  Rank 3 (dist=0.3948): Law Enforcement: West Virginia State Police Troop 6 - Oak Hill Detachment, 3057 Main Street East Oak Hill WV 25901, Faye
  Rank 4 (dist=0.3962): Library: Oak Hill Public Library, 611 Main Street, Oak Hill, WV
  Rank 5 (dist=0.3973): Oak Hill Public Library | library | 611 Main Street Oak Hill WV | phone: 304 469 9890 | county: ? | state: WV

──────────────────────────────────────────────────────────────────────
Q18 [health]: What free clinics are available in Fayette County?
──────────────────────────────────────────────────────────────────────
  Rank 1 (dist=0.3688): rural_health Fayette Clinic PLLC health_rural_facilities lat:37.976612 lon:-81.097223 West Virginia WV
  Rank 2 (dist=0.4387): Fayetteville Clinic | health | Fayetteville WV 25840 | Free health clinic
  Rank 3 (dist=0.4600): rural_health Summers County App. Regiona. Hospital Clinic health_rural_facilities lat:37.671504 lon:-80.890026 West Virg
  Rank 4 (dist=0.4768): public_health FAYETTE COUNTY HEALTH DEPARTMENT public_health_depts_2009 lat:38.054048 lon:-81.103434 West Virginia WV
  Rank 5 (dist=0.4883): Montgomery General Elderly Care | nursing home | P.O. Box 1010 WV | phone: 442-2469 | county: Fayette | state: WV

──────────────────────────────────────────────────────────────────────
Q19 [health]: How do I get health insurance if I cannot afford it in WV?
──────────────────────────────────────────────────────────────────────
  Rank 1 (dist=0.4502): WV opens application period for some Rural Health Transformation funds. The West Virginia Department of Health has start
  Rank 2 (dist=0.4638): Medicaid work requirements, redeterminations will cause up to 75K to lose their health care in WV. Between 40,000 and 75
  Rank 3 (dist=0.5184): public_health MCDOWELL COUNTY HEALTH DEPARTMENT public_health_depts_2009 lat:37.378643 lon:-81.562447 West Virginia WV
  Rank 4 (dist=0.5244): rural_health Family Healthcare Associates, Inc. health_rural_facilities lat:37.743198 lon:-81.874845 West Virginia WV
  Rank 5 (dist=0.5244): rural_health Family Healthcare Associates, Inc. health_rural_facilities lat:37.743198 lon:-81.874845 West Virginia WV

──────────────────────────────────────────────────────────────────────
Q20 [health]: Who helps with Medicare enrollment in southern West Virginia?
──────────────────────────────────────────────────────────────────────
  Rank 1 (dist=0.4529): Hospice of Southern WV recognized for 5-star care. Hospice of Southern West Virginia has been recognized by the Centers 
  Rank 2 (dist=0.4739): Medicaid work requirements, redeterminations will cause up to 75K to lose their health care in WV. Between 40,000 and 75
  Rank 3 (dist=0.4782): rural_health Family Healthcare Associates, Inc. health_rural_facilities lat:37.743198 lon:-81.874845 West Virginia WV
  Rank 4 (dist=0.4782): rural_health Family Healthcare Associates, Inc. health_rural_facilities lat:37.743198 lon:-81.874845 West Virginia WV
  Rank 5 (dist=0.4953): Additional Resources 
 
Find Help 
 
 
 
 
 
 https://www.findhelp.org/ 
 
Healthy Grandfamilies  
 
 
 
https://healthy

──────────────────────────────────────────────────────────────────────
Q21 [childcare]: Is there childcare assistance available in Fayette County?
──────────────────────────────────────────────────────────────────────
  Rank 1 (dist=0.4192): Hilltop Center | nursing home | P.O. Box 125 WV | phone: 469-2966 | county: Fayette | state: WV
  Rank 2 (dist=0.4252): Ansted Center | nursing home | P.O. Drawer 400 WV | phone: 658-5271 | county: Fayette | state: WV
  Rank 3 (dist=0.4320): Divide Elementary School | school | 334 Propps Ridge Lookout WV 25868 nan WV | phone: 304-574-1443 | county: Fayette | s
  Rank 4 (dist=0.4387): Fayette Nursing and Rehabilitation Center, Inc. | nursing home | 100 Hresan Boulevard WV | phone: 574-0770 | county: Fay
  Rank 5 (dist=0.4500): Montgomery General Elderly Care | nursing home | P.O. Box 1010 WV | phone: 442-2469 | county: Fayette | state: WV

──────────────────────────────────────────────────────────────────────
Q22 [childcare]: How do I apply for the WV childcare subsidy program?
──────────────────────────────────────────────────────────────────────
  Rank 1 (dist=0.4810): WV opens application period for some Rural Health Transformation funds. The West Virginia Department of Health has start
  Rank 2 (dist=0.4881): - WV WORKS/TANF; - SNAP; - Medicaid, WV CHIP, or other medical assistance; - HUD or other housing assistance; or - State
  Rank 3 (dist=0.4964): WV youth aging out of foster care face waitlist for resources; Morrisey vetoes bill to address issue. Children’s Home So
  Rank 4 (dist=0.5011): School: Divide Elementary School, 334 Propps Ridge Lookout WV 25868, Fayette County, WV
  Rank 5 (dist=0.5159): 26,000 West Virginia kids lack childcare access. These Clay County parents want answers from their lawmakers.. <figure><

──────────────────────────────────────────────────────────────────────
Q23 [childcare]: Where can I find affordable daycare near Oak Hill?
──────────────────────────────────────────────────────────────────────
  Rank 1 (dist=0.4847): Sand Hill Library | library | Sand Hill Elementary, Rt 1 Box 87 Dallas WV | phone: 304 547 5041 | county: ? | state: WV
  Rank 2 (dist=0.4962): Library: Oak Hill Public Library, 611 Main Street, Oak Hill, WV
  Rank 3 (dist=0.4970): Nursing Home: Hidden Valley Center- Genesis Healthcare, 422  23rd Street Oak Hill WV 25901, Fayette County, WV
  Rank 4 (dist=0.5035): Nursing Home: River Oaks - Stonerise Healthcare, 100 Parkway Drive Clarksburg WV 26301, Harrison County, WV
  Rank 5 (dist=0.5049): Nursing Home: Hidden Valley Center, 422 - 23rd Street, Oak Hill, Fayette County, WV

──────────────────────────────────────────────────────────────────────
Q24 [childcare]: What programs help pay for childcare in southern WV?
──────────────────────────────────────────────────────────────────────
  Rank 1 (dist=0.4546): WV youth aging out of foster care face waitlist for resources; Morrisey vetoes bill to address issue. Children’s Home So
  Rank 2 (dist=0.4569): Additional Resources Find Help https://www.findhelp.org/ Healthy Grandfamilies https://healthygrandfamilies.com/ Interna
  Rank 3 (dist=0.4678): Additional Resources 
 
Find Help 
 
 
 
 
 
 https://www.findhelp.org/ 
 
Healthy Grandfamilies  
 
 
 
https://healthy
  Rank 4 (dist=0.4754): 26,000 West Virginia kids lack childcare access. These Clay County parents want answers from their lawmakers.. <figure><
  Rank 5 (dist=0.4901): - WV WORKS/TANF; - SNAP; - Medicaid, WV CHIP, or other medical assistance; - HUD or other housing assistance; or - State

──────────────────────────────────────────────────────────────────────
Q25 [childcare]: I need help paying for preschool in Fayette County
──────────────────────────────────────────────────────────────────────
  Rank 1 (dist=0.4738): Kiddie Fair and Pre-K Registration kicks off on April 17 at Fayetteville Memorial Building as Universal Pre-K Registrati
  Rank 2 (dist=0.4895): Divide Elementary School | school | 334 Propps Ridge Lookout WV 25868 nan WV | phone: 304-574-1443 | county: Fayette | s
  Rank 3 (dist=0.5175): Gauley Bridge Elementary School | school | 140 Walnut Street Gauley Bridge WV 25085 nan WV | phone: 304-632-2661 | count
  Rank 4 (dist=0.5211): School: Mercer County Early Learning Center Bluefield, 3318 East Cumberland Road Bluefield WV 24701, Mercer County, WV
  Rank 5 (dist=0.5251): School: Doddridge County Preschool, 2945 Smithton Road West Union WV 26456, Doddridge County, WV

──────────────────────────────────────────────────────────────────────
Q26 [ssi]: How do I apply for SSI in West Virginia?
──────────────────────────────────────────────────────────────────────
  Rank 1 (dist=0.4936): n the State of West Virginia, unless expressly authorized in writing by Harmony for Hope.  
- Additional regions (for ex
  Rank 2 (dist=0.5152): Law Enforcement: West Virginia State Police Troop 4 - Saint Marys Detachment, 1313 Second Street Saint Marys WV 26170, P
  Rank 3 (dist=0.5169): LIST: Social Security offices in West Virginia, several other states temporarily closed. The agency notes the closures a
  Rank 4 (dist=0.5193): Law Enforcement: WEST VIRGINIA STATE POLICE TROOP 4 - SAINT MARYS DETACHMENT, 1313 SECOND STREET, SAINT MARYS, PLEASANTS
  Rank 5 (dist=0.5226): WEST VIRGINIA STATE POLICE TROOP 4 - SAINT MARYS DETACHMENT | law enforcement | 1313 SECOND STREET SAINT MARYS WV | phon

──────────────────────────────────────────────────────────────────────
Q27 [ssi]: Where is the Social Security office nearest to Oak Hill WV?
──────────────────────────────────────────────────────────────────────
  Rank 1 (dist=0.3972): Correctional: OAK HILL POLICE DEPARTMENT, 100 KELLY AVENUE, OAK HILL, FAYETTE County, WV
  Rank 2 (dist=0.3979): Fire Department: Oak Hill Volunteer Fire Department, 582 Virginia Street Oak Hill WV 25901, Oak Hill, WV
  Rank 3 (dist=0.4054): Nursing Home: Hidden Valley Center- Genesis Healthcare, 422  23rd Street Oak Hill WV 25901, Fayette County, WV
  Rank 4 (dist=0.4064): Parole Office: Oak Hill Parole Office, 1307 Main Street East, Oak Hill, Fayette County, WV
  Rank 5 (dist=0.4121): Oak Hill Volunteer Fire Department | fire department | 582 Virginia Street Oak Hill WV 25901 Oak Hill WV | phone: 304-46

──────────────────────────────────────────────────────────────────────
Q28 [ssi]: What disability assistance programs are in Fayette County?
──────────────────────────────────────────────────────────────────────
  Rank 1 (dist=0.4591): Fayette Nursing and Rehabilitation Center, Inc. | nursing home | 100 Hresan Boulevard WV | phone: 574-0770 | county: Fay
  Rank 2 (dist=0.4652): Hilltop Center | nursing home | P.O. Box 125 WV | phone: 469-2966 | county: Fayette | state: WV
  Rank 3 (dist=0.4669): Nursing Home: Fayette Nursing and Rehabilitation Center, Inc., 100 Hresan Boulevard, Fayetteville, Fayette County, WV
  Rank 4 (dist=0.4681): Montgomery General Elderly Care | nursing home | P.O. Box 1010 WV | phone: 442-2469 | county: Fayette | state: WV
  Rank 5 (dist=0.4728): Fayette Nursing and Rehabilitation Center - AMFM Nursing & Rehab Centers | nursing home | 100 Hresan Boulevard Fayettevi

──────────────────────────────────────────────────────────────────────
Q29 [ssi]: I was denied SSI who can help me appeal in WV?
──────────────────────────────────────────────────────────────────────
  Rank 1 (dist=0.5207): Court ruling limiting adult gender-affirming Medicaid coverage could have national impacts. A U.S. appeals court ruling 
  Rank 2 (dist=0.5361): WV state school board files appeal to Supreme Court over vaccine ruling. Attorneys for the West Virginia Board of Educat
  Rank 3 (dist=0.5745): Federal appeals court upholds WV school vaccine law. A federal appeals court on Wednesday ruled against a West Virginia 
  Rank 4 (dist=0.5917): Arthur B. Hodges Center | nursing home | 300 Baker Lane Charleston WV 25302 | phone: 304-346-2323 | beds: 20.0 | county:
  Rank 5 (dist=0.6038): WV Supreme Court considering child abuse case that involves mother’s use of Bible verses. The West Virginia Supreme Cour

──────────────────────────────────────────────────────────────────────
Q30 [ssi]: What income help is available for disabled adults in Fayette County?
──────────────────────────────────────────────────────────────────────
  Rank 1 (dist=0.4890): Raleigh County organizations receive more than $375,000 in state grant funding. Four local groups serving seniors, famil
  Rank 2 (dist=0.4954): Additional Resources 
 
Find Help 
 
 
 
 
 
 https://www.findhelp.org/ 
 
Healthy Grandfamilies  
 
 
 
https://healthy
  Rank 3 (dist=0.5147): Additional Resources Find Help https://www.findhelp.org/ Healthy Grandfamilies https://healthygrandfamilies.com/ Interna
  Rank 4 (dist=0.5183): Grant Program Seeks To Help Those In Recovery Find Jobs. Grants of up to $500,000 will be used to help Appalachians in r
  Rank 5 (dist=0.5194): 

- **Harmony for Hope operations and staff**, which provide organizational backbone for community programming and techn
(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:/opt/msjarvis-rebuild$ 

