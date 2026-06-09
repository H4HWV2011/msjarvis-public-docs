(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:/opt/msjarvis-rebuild$ # 1. Targeted entity search
docker exec jarvis-local-resources-db psql -U postgres -d msjarvisgis --pset=pager=off -c "
SELECT fullownern, COUNT(*) as parcels, ROUND(SUM(acres_c)::numeric, 1) as total_acres 
FROM public.fayette_parcels
WHERE fullownern ILIKE '%orbis%'
   OR fullownern ILIKE '%quercus%'
   OR fullownern ILIKE '%oak hill%'
   OR fullownern ILIKE '%anew%'
   OR fullownern ILIKE '%oha%'
   OR fullownern ILIKE '%vilcom%'
   OR fullownern ILIKE '%nmtc%'
   OR fullownern ILIKE '%chapel hill%'
   OR fullownern ILIKE '%conservation%'
   OR fullownern ILIKE '%carbon%'
   OR fullownern ILIKE '%climate%'
GROUP BY fullownern
ORDER BY total_acres DESC;"
                      fullownern                      | parcels | total_acres 
------------------------------------------------------+---------+-------------
 QUERCUS WV LLC ICO: ORBIS INC                        |      71 |     24807.6
 OAK HILL FORESTLANDS NMTC LLC C/O ORBIS INC          |      77 |      9613.3
 CITY OF OAK HILL WEST VIRGINIA                       |       1 |       280.7
 CITY OF OAK HILL                                     |      24 |       136.7
 WEST VIRGINIA CONSERVATION COMMISSION                |       3 |        76.4
 OAK HILL FORESTLANDS NMTC LLC                        |       1 |        57.7
 WVA CONSERVATION COMM                                |       1 |        53.5
 MOLLOHAN DAVID & TAMMY                               |       1 |        38.2
 OAK HILL CITY OF                                     |      18 |        14.0
 LG-OHI OAK HILL LLC                                  |       7 |         5.6
 CITY OF OAK HILL BUILDING COMMISSION                 |       1 |         5.4
 THE CITY OF OAK HILL                                 |       6 |         5.1
 CARBONDALE BAPTIST CHURCH TRUSTEES                   |       2 |         5.1
 SANITARY BOARD OF THE CITY OF OAK HILL               |       2 |         4.4
 OAK HILL CH NAZARENE                                 |       1 |         3.9
 OAK HILL CHRISTIAN CHURCH                            |       1 |         3.9
 OAK HILL AID II PROPCO LLC                           |       3 |         3.8
 OAK HILL CITY                                        |       1 |         3.8
 W VA CONSERVATION COMM                               |       1 |         3.3
 OAK HILLS PROPERTIES LLC                             |       2 |         2.7
 OAK HILL BAP CH                                      |       3 |         2.1
 VEARD-OAK HILL LIMITED PARTNERSHIP                   |       1 |         2.0
 OAK HILL BUILDING COMMISSION                         |       3 |         1.7
 OAK HILL UNITED METHODIST CHURCH TRSTS               |       2 |         1.7
 TIMYCHA OAK HILL HOLDINGS LLC                        |       2 |         1.5
 BOHANNA GARFIELD JR                                  |       1 |         1.3
 OAK HILL CITIZENS FOR BETTER HOUSING                 |       1 |         1.1
 OAK HILL SWIM CLUB INC                               |       2 |         1.1
 CARBON WEST VIRGINIA COMPANY LLC                     |      10 |         1.0
 OAK HILL LODGE NO 120 AF & AM ET ALS                 |       1 |         0.9
 CALVARY BAPTIST CHURCH OF OAK HILL TRUSTEES          |       1 |         0.8
 OAK HILL UNITED METHODIST CHURCH                     |       1 |         0.7
 OAK HILL PROFESSIONAL BLDG CO INC                    |       1 |         0.7
 W VA CONSERVATION COMMISSION                         |       1 |         0.7
 VIRGINIA ST BAPIST CHURCH OF OAK HILL                |       1 |         0.7
 OHARA JAMES W & SARA M                               |       2 |         0.6
 UNITED STATES AMERICA OAK HILL POST OFFICE           |       1 |         0.6
 OAK HILL FREEWILL BAP                                |       2 |         0.5
 OAK HILL UNITED METHODIST CHURCH TRUSTEES            |       2 |         0.4
 TRUSTEES OF THE GOSPEL TABERNACLE CHURCH OF OAK HILL |       2 |         0.4
 TRUSTEES OF CALVARY BAPTIST CH OF OAK HILL           |       1 |         0.3
 OAK HILL FREEWILL BAPT CHURCH                        |       1 |         0.3
 OAK HILL BAP CH TRSTS                                |       1 |         0.2
 OAK HILL GOSPEL TABERNACLE TRUSTEES                  |       2 |         0.2
 TRUSTEES OAK HILL UNITED METHODIST CHURCH            |       1 |         0.2
 TRUSTEES OF THE CALVARY BAPTIST CHURCH OF OAK HILL   |       1 |         0.2
 BOHANNA DAVID                                        |       1 |         0.2
 OAK HILL FIRST BRETHREN CHURCH                       |       1 |         0.1
 OAK HILL UNITED METHODIST CHURC H                    |       1 |         0.1
 OAK HILL BRETHREN CHURCH                             |       1 |         0.1
 CARBON WEST VIRGINIA COMPNAY LLC                     |       1 |         0.1
 BOHANNA GARFIELD JR & RITA J                         |       1 |         0.1
 BOHANNA GARFIELD                                     |       1 |         0.1
 OAK HILL BAPTIST CHURCH TRUSTEES                     |       1 |         0.0
(54 rows)

(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:/opt/msjarvis-rebuild$ # 2. Top 40 landowners by acreage — full Fayette County
docker exec jarvis-local-resources-db psql -U postgres -d msjarvisgis --pset=pager=off -c "
SELECT fullownern, COUNT(*) as parcels, ROUND(SUM(acres_c)::numeric, 1) as total_acres 
FROM public.fayette_parcels
GROUP BY fullownern
ORDER BY total_acres DESC
LIMIT 40;"
                        fullownern                         | parcels | total_acres 
-----------------------------------------------------------+---------+-------------
 UNITED STATES OF AMERICA                                  |     200 |     33542.4
 QUERCUS WV LLC ICO: ORBIS INC                             |      71 |     24807.6
 WEYERHAEUSER COMPANY                                      |      67 |     23968.1
 POCAHONTAS SURFACE INT LLC                                |     105 |     21656.4
 NUTTALL LLC C/O TAX DEPT                                  |      26 |     15694.3
 ARROW WV INC C/O BOY SCOUTS OF AMERICA                    |      50 |     13450.2
 IMPERIAL COLLIERY CO                                      |       7 |     12512.0
                                                           |     536 |     11157.0
 OAK HILL FORESTLANDS NMTC LLC C/O ORBIS INC               |      77 |      9613.3
 PENN VIRGINIA OPERATING CO LLC                            |       9 |      9367.8
 KANAWHA GAULEY C & C CO                                   |       2 |      7963.0
 HEARTWOOD FORESTLAND FUND VII LLC                         |      17 |      6623.4
 HEARTWOOD FORRESTLAND FUND IV LLC                         |       1 |      6335.5
 APPALACHIAN FORREST B LLC                                 |       6 |      5926.2
 BEURY HELEN C EST C/O BEURY LAUREL LTD PART               |      14 |      5086.9
 WESTERN POCAHONTAS PROPERTIES                             |      28 |      4397.8
 CHRISTIAN COLLIERY CO C/O MELVIN AND COMPANY              |      42 |      3935.9
 BELLWOOD CORPORATION                                      |      14 |      3827.6
 W VA DEPT OF NAT RES                                      |      19 |      3294.1
 WVA DNR                                                   |       1 |      3256.6
 W VA STATE CONS COMM                                      |      11 |      2958.9
 MIDVALE COLLIERY CO                                       |       3 |      2808.2
 DIVISION OF NATURAL RESOURCES                             |       1 |      2447.5
 EAGLE LAND CO                                             |       2 |      2391.9
 UNITED STATES OF AMERICA NEW RIVER GORGE CORP             |       9 |      2242.5
 DEITZ T A                                                 |       2 |      2153.0
 GLADE CREEK LIMITED PARTNERSHIP                           |      11 |      2101.3
 HATFIELD-MCCOY REGIONAL RECREATIONAL AUTHORITY            |       6 |      2044.2
 ACIN LLC                                                  |      14 |      1777.7
 RICH CREEK HOLDINGS LLC                                   |       3 |      1526.5
 GAULEY OUTDOOR CENTER INC                                 |      32 |      1387.0
 AUXIER FARMS INC                                          |       1 |      1372.0
 HEARTWOOD FORESTLAND FUND IV LLC                          |       4 |      1355.4
 HAWKS NEST HYDRO LLC C/O BARCLAY DAMON LLP                |      13 |      1345.8
 MEADOW CREEK COAL CORPORATION                             |      39 |      1333.8
 WE-R-FARMERS LLC                                          |       2 |      1301.4
 JOHNSON LANDS LLC                                         |       3 |      1264.2
 BIG CREEK LAND CO                                         |       5 |      1243.7
 AUXIER WELDING INC                                        |       3 |      1237.3
 STATE OF WV DEPT OF COMMERCE DIVISON OF NATURAL RESOURCES |       1 |      1213.4
(40 rows)

(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:/opt/msjarvis-rebuild$ # 3. Address-based network sweep (fullownera = mailing address)
docker exec jarvis-local-resources-db psql -U postgres -d msjarvisgis --pset=pager=off -c "
SELECT fullownern, fullownera, COUNT(*) as parcels, ROUND(SUM(acres_c)::numeric, 1) as acres
FROM public.fayette_parcels
WHERE fullownera ILIKE '%chapel hill%'
   OR fullownera ILIKE '%charlotte%'
   OR fullownera ILIKE '%vilcom%'
   OR fullownera ILIKE '%carbon%'
   OR fullownera ILIKE '%orbis%'
   OR fullownera ILIKE '%27517%'
   OR fullownera ILIKE '%28202%'
GROUP BY fullownern, fullownera
ORDER BY acres DESC;"
                          fullownern                          |                                 fullownera                                  | parcels |  acres  
--------------------------------------------------------------+-----------------------------------------------------------------------------+---------+---------
 QUERCUS WV LLC ICO: ORBIS INC                                | 8809 LENOX POINTE DR STE B, CHARLOTTE, NC 28273                             |      70 | 24807.4
 OAK HILL FORESTLANDS NMTC LLC C/O ORBIS INC                  | 8809 LENOX POINTE DR STE B, CHARLOTTE, NC 28273                             |      77 |  9613.3
 HEARTWOOD FORRESTLAND FUND IV LLC                            | C/O FORESTLAND GROUP, 1512 E FRANKLIN ST STE 104, CHAPEL HILL, NC 27514     |       1 |  6335.5
 HEARTWOOD FORESTLAND FUND VII LLC                            | C/O FORESTLAND GRP LLC, 1512 E FRANKLIN ST STE 104, CHAPEL HILL, NC 27514   |      11 |  6213.0
 APPALACHIAN FORREST B LLC                                    | 1512 E FRANKLIN ST STE 104, CHAPEL HILL, NC 27514                           |       6 |  5926.2
 HEARTWOOD FORESTLAND FUND IV LLC                             | C/O FORESTLAND GROUP, 1512 E FRANKLIN ST STE 104, CHAPEL HILL, NC 27514     |       3 |   946.2
 HEARTWOOD FORESTLAND FUND IV LLC                             | 1512 E FRANKLIN ST STE 104, CHAPEL HILL, NC 27514                           |       1 |   409.2
 HEARTWOOD FORESTLAND FUND VII LLC                            | C/O THE FORESTLAND GROUP, 1512 E FRANKLIN ST STE 104, CHAPEL HILL, NC 27514 |       3 |   215.5
 HEARTWOOD FORESTLAND FUND VII LLC                            | C/O FORESTLAND GROUP, 1512 E FRANKLIN ST STE 104, CHAPEL HILL, NC 27514     |       3 |   194.8
 ABBOTT CHAS A                                                | C/O DONNA MACHELLE ABBOTT, PO BOX 284, MOUNT CARBON, WV 25139               |       1 |   101.7
 TIMBAYAN ADIN                                                | PO BOX 36, MT CARBON, WV 25139                                              |       2 |    64.0
 BOUNDS MORRIS A JR                                           | PO BOX 272, MOUNT CARBON, WV 25139                                          |       1 |    54.4
 HURLEY MARK                                                  | PO BOX 141, MOUNT CARBON, WV 25139                                          |       1 |    51.8
 BRYANT KRISTOPHER M                                          | 1443 PLANTERS KNOB LN, CHARLOTTE, NC 28273                                  |       1 |    42.9
 TIMBAYAN MARISSA EDUC TRUST & TIMBAYAN ALADDIN JOHN EDUC TRU | PO BOX 36, MT CARBON, WV 25139                                              |       3 |    42.0
 PLAID FAMILY LLC                                             | PO BOX 533, MOUNT CARBON, WV 25139                                          |       3 |    24.7
 LHA PROPERTIES LLC                                           | PO BOX 141, MOUNT CARBON, WV 25139                                          |       8 |    18.6
 BAUGH JANE KELLY                                             | C/O BLAIR KELLY, 2140 GARTH RD, CHARLOTTESVILLE, VA 22901                   |      14 |     9.6
 WATSON DAVID M                                               | PO BOX 3, MOUNT CARBON, WV 25139                                            |      12 |     8.5
 DICKINSON STEVEN TODD                                        | PO BOX 454, MOUNT CARBON, WV 25139                                          |       2 |     6.7
 BROOKSIDE MINISTRIES CHURCH OF GOD IN CHRIST INC             | 18419 DEEP WATER MTN RD, MOUNT CARBON, WV 25139                             |       1 |     6.4
 PENNINGTON JAMES G & BILLIE J                                | PO BOX 263, MT CARBON, WV 25136                                             |       1 |     5.4
 MAYES SUE SIGLER ETAL                                        | C/O TERRY SIGLER, PO BOX 67, MT CARBON, WV 25139                            |       1 |     3.2
 ANGEL IRIS M                                                 | C/O IRIS KEFFER, PO BOX 161, MT CARBON, WV 25139                            |       1 |     3.0
 TOMLISON KEARNAN K & WEAVER SEAN R & SICZEK ROBIN            | 3051 COMMONWEALTH AVE, CHARLOTTE, NC 28205                                  |       1 |     2.8
 HOSEY EDWARD & ETALS                                         | C/O SHEILA HOSEY, 7711 HIDDEN CREEK DR, CHARLOTTE, NC 28214                 |       1 |     2.6
 LHA PROPERTIES LLC                                           | PO BOX 141, MT CARBON, WV 25139                                             |       7 |     2.6
 ZAMIELA BETTY J                                              | 5925 BARRINGTON DR, CHARLOTTE, NC 28215                                     |       1 |     2.5
 LOVE SUSAN MCDANALD                                          | 8512 HEADFORD RD, CHARLOTTE, NC 28277                                       |       1 |     2.3
 WHEELER ROBERT E OR TIMARA L                                 | PO BOX 433, MOUNT CARBON, WV 25139                                          |       2 |     1.7
 WHEELER ROBERT E & TIMARA L                                  | PO BOX 433, MOUNT CARBON, WV 25139                                          |       2 |     1.7
 HUDNALL TROY                                                 | PO BOX 132, MOUNT CARBON, WV 25139                                          |       1 |     1.4
 NALEVANKO MICHAEL A & ALEXIS M G                             | 2001 WENSLEY DR, CHARLOTTE, NC 28210                                        |       1 |     1.3
 LEE RUDOLPH W SR & VIRGINIA ETAL                             | C/O LUCINDA LEE, 6501 MONTEZUMA TRAILS, CHARLOTTE, NC 28227                 |       1 |     1.3
 ADKINS WALLACE A                                             | 4741 ELLENOR DR, CHARLOTTE, NC 28208                                        |       3 |     1.3
 NICHOLAS TRINITY                                             | C/O TERRY SIGLER, PO BOX 131, MOUNT CARBON, WV 25139                        |       1 |     1.2
 ANGEL DONNIE E                                               | PO BOX 223, MT CARBON, WV 25139                                             |       1 |     1.1
 MARSICO TONY S & DEANA                                       | 66 FORTUNA DR, MOUNT CARBON, WV 25139                                       |       2 |     1.0
 SHORT RONNIE B & SHERRY L                                    | 19691 DEEPWATER MTN RD, MOUNT CARBON, WV 25139                              |       3 |     1.0
 SLATE STEVEN W & MELISSA D                                   | PO BOX 333, MOUNT CARBON, WV 25139                                          |       2 |     0.9
 MILLER CHRIS & PERRY URSULA                                  | PO BOX 154, MOUNT CARBON, WV 25139                                          |       3 |     0.9
 HUDNALL TROY MICHAEL                                         | PO BOX 132, MOUNT CARBON, WV 25139                                          |       1 |     0.9
 TONEY GREGORY A & JENNIFER J                                 | PO BOX 372, MOUNT CARBON, WV 25139                                          |       3 |     0.8
 THOMAS CATHERINE L                                           | 911 CHARLOTTE DR, NEWPORT NEWS, VA 23601                                    |       4 |     0.8
 ROWE GARY                                                    | PO BOX 262, MOUNT CARBON, WV 25139                                          |       3 |     0.8
 LANE WILLIAM J & ETAL                                        | CHARLOTTE COTTRELL, 5525 VARNA DR, INDIANAPOLIS, IN 46221                   |       1 |     0.8
 SODDER JOSEPH S III                                          | 98 MONTGOMERY HEIGHTS RD, MOUNT CARBON, WV 25139                            |       1 |     0.8
 DEAN DOUGLAS L & AMY B                                       | PO BOX 313, MT CARBON, WV 25139                                             |       2 |     0.8
 CRINITI DORIS M                                              | PO BOX 362, MT CARBON, WV 25139                                             |       5 |     0.8
 LEE LUCINDA M & NATALIE M ETAL                               | 6501 MONTEZUMA TRAILS, CHARLOTTE, NC 28227                                  |       1 |     0.7
 GIPSON DEBORAH                                               | PO BOX 171, MT CARBON, WV 25139                                             |       1 |     0.7
 ELGIN VICTORIA DAWN (LE) JUDITH RIDER                        | PO BOX 363, MT CARBON, WV 25139                                             |       3 |     0.7
 WILSON JOEY L & ALLISON                                      | PO BOX 93, MOUNT CARBON, WV 25139                                           |       1 |     0.7
 FOSTER CHRISSY L SPAULDING                                   | PO BOX 103, MT CARBON, WV 25139                                             |       1 |     0.7
 CRINITI DORIS M                                              | PO BOX 362, MOUNT CARBON, WV 25139                                          |       9 |     0.7
 MT OLIVE BAPTIST CHURCH (TRUSTEES)                           | PO BOX 70, MOUNT CARBON, WV 25139                                           |       1 |     0.7
 SPAULDING MICHAEL W & ROSE M                                 | PO BOX 324, MT CARBON, WV 25139                                             |       1 |     0.6
 RIDENOUR TODD A                                              | PO BOX 192, MOUNT CARBON, WV 25139                                          |       1 |     0.6
 MIDDLETON TANYA                                              | PO BOX 293, MOUNT CARBON, WV 25139                                          |       4 |     0.6
 WHITE GARY                                                   | 17075 DEEPWATER MT RD, MOUNT CARBON, WV 25139                               |       1 |     0.6
 COALFIELD LAND CO                                            | C/O BLAIR KELLY, 2140 GARTH RD, CHARLOTTESVILLE, VA 22901                   |       1 |     0.6
 WHITE GARY                                                   | 17075 DEEPWATER MTN RD, MOUNT CARBON, WV 25139                              |       1 |     0.6
 SKAGGS ANNA K                                                | PO BOX 73, MOUNT CARBON, WV 25139                                           |       2 |     0.6
 ANGEL KAREN J & CLARK MONTICA Y                              | PO BOX 279, MOUNT CARBON, WV 25139                                          |       1 |     0.6
 SLATE STEVEN W & MELISSA D                                   | C/O STEVEN & MELISSA SLATE, PO BOX 333, MOUNT CARBON, WV 25139              |       1 |     0.6
 JOHNSTON JOHNNY W & MARILYN                                  | PO BOX 373, MOUNT CARBON, WV 25139                                          |       1 |     0.6
 ANGEL DONNIE E                                               | PO BOX 223, MOUNT CARBON, WV 25139                                          |       2 |     0.6
 HUFFER RAY C                                                 | PO BOX 216, MT CARBON, WV 25139                                             |       1 |     0.5
 HILL MAXWELL H III & KATHRYN LEE                             | PO BOX 183, MOUNT CARBON, WV 25139                                          |       1 |     0.5
 PANKEY LUCY ETALS                                            | C/O DEMETRIUS YOUNG, 2417 ARDEN GATE LN, CHARLOTTE, NC 28262                |       1 |     0.5
 PERDUE LINDA L                                               | PO BOX 92, MT CARBON, WV 25139                                              |       1 |     0.5
 PETRY CLAYTON & AMY                                          | PO BOX 483, MOUNT CARBON, WV 25139                                          |       1 |     0.5
 HUFFER RAY C & LINDA L                                       | PO BOX 216, MT CARBON, WV 25139                                             |       1 |     0.5
 HUGHES CARL & NANCY                                          | PO BOX 87, MT CARBON, WV 25139                                              |       1 |     0.5
 ESTERBY PATRICIA JENETTE                                     | PO BOX 244, MOUNT CARBON, WV 25139                                          |       2 |     0.5
 TERRELL PHILLIP CARL JR & DEBBIE ANN                         | 138 GINA ST, MOUNT CARBON, WV 25139                                         |       2 |     0.5
 TACKETT WILLIAM J & ANNA M                                   | PO BOX 413, MOUNT CARBON, WV 25139                                          |       2 |     0.5
 ABBOTT DONNA MACHELLE                                        | PO BOX 284, MT CARBON, WV 25139                                             |       2 |     0.5
 SKIRPAN SUSAN MAE & ETAL                                     | 1921 CARBON HILL DR, MIDLOTHIAN, VA 23112                                   |       1 |     0.5
 SMITH RONALD E & KANDY L                                     | 17047 DEEPWATER MTN RD, MT CARBON, WV 25139                                 |       3 |     0.5
 JUDY ROY S & LINDSEY C                                       | PO BOX 97, MOUNT CARBON, WV 25139                                           |       1 |     0.5
 WISEMAN TODD & KRISTA C                                      | PO BOX 33, MOUNT CARBON, WV 25139                                           |       1 |     0.5
 COLEMAN RICHARD H & CAROL S                                  | PO BOX 472, MT CARBON, WV 25139                                             |       1 |     0.5
 LEGG JOHN CLEVE ET AL                                        | C/O TONI HALTER, 4312 STOURTON LN, CHARLOTTE, NC 28226                      |       1 |     0.5
 LOREA STEVEN E & SHERRY D                                    | PO BOX 522, MOUNT CARBON, WV 25139                                          |       1 |     0.5
 AKERS ELIZABETH A                                            | PO BOX 83, MT CARBON, WV 25139                                              |       1 |     0.5
 ALTON JACOB & TAYLOR                                         | 46 ADENA DR, MOUNT CARBON, WV 25139                                         |       1 |     0.5
 WALKER RONALD L & AMY ELAINE                                 | PO BOX 203, MOUNT CARBON, WV 25139                                          |       2 |     0.4
 SCHOOLCRAFT LINDA M                                          | PO BOX 274, MOUNT CARBON, WV 25139                                          |       2 |     0.4
 STEVENSON LORA L & PROCTOR JUSTIN R                          | 104 CEMETERY LN, MOUNT CARBON, WV 25139                                     |       2 |     0.4
 ANGEL SAMUEL W & ANGEL KAREN J                               | PO BOX 279, MT CARBON, WV 25139                                             |       2 |     0.4
 PETTRY LON                                                   | PO BOX 127, MT CARBON, WV 25139                                             |       1 |     0.4
 TIMBAYAN DR A                                                | PO BOX 36, MOUNT CARBON, WV 25139                                           |       1 |     0.4
 MATHENY REID & THERESA QUEEN NATHAN & MARY                   | 303 SUMMERMORE DR, CHARLOTTE, NC 28270                                      |       1 |     0.4
 BROWN LAWRENCE E II                                          | PO BOX 153, MT CARBON, WV 25139                                             |       1 |     0.4
 FRUIT CANDIDA KINCAID                                        | 5209 JUNE FURR RD, CHARLOTTE, NC 28216                                      |       1 |     0.4
 DUNN WILLIAM & TERA                                          | PO BOX 402, MT CARBON, WV 25139                                             |       2 |     0.4
 GIVEN TYLER SCOTT & HARVEY TAYLOR NICOLE                     | PO BOX 314, MOUNT CARBON, WV 25139                                          |       2 |     0.4
 MUNSON ANITA ETAL                                            | PO BOX 62, MT CARBON, WV 25139                                              |       1 |     0.4
 BOBBITT RONALD E                                             | BOX 4, MT CARBON, WV 25139                                                  |       2 |     0.4
 BLUE STEEL SOLUTIONS LLC                                     | 733 WOODRUFF PL, CHARLOTTE, NC 28208                                        |       1 |     0.4
 WISEMAN SONYA J                                              | PO BOX 125, MT CARBON, WV 25139                                             |       1 |     0.4
 BROWN LAWRENCE E II & JEAN ANN                               | PO BOX 153, MT CARBON, WV 25139                                             |       1 |     0.4
 MILLER CHRISTOPHER L                                         | PO BOX 154, MOUNT CARBON, WV 25139                                          |       1 |     0.4
 RIDENOUR MELISSA DAWN                                        | PO BOX 282, MOUNT CARBON, WV 25139                                          |       1 |     0.4
 RIDENOUR SCOTT                                               | PO BOX 231, MOUNT CARBON, WV 25139                                          |       1 |     0.4
 RIDENOUR CLINTON                                             | PO BOX 282, MT CARBON, WV 25139                                             |       1 |     0.4
 FERTIG RICHARD & KATHERINE                                   | 17163 DEEPWATER MTN RD, MOUNT CARBON, WV 25139                              |       1 |     0.4
 ROWE JANET L & PERRY URSULA                                  | P O BOX 54, MT CARBON, WV 25139                                             |       1 |     0.4
 FLEMING DENVER T & CAITLIN                                   | PO BOX 382, MOUNT CARBON, WV 25139                                          |       1 |     0.4
 RYAN MARSHA & MICHAEL                                        | PO BOX 253, MOUNT CARBON, WV 25139                                          |       2 |     0.4
 LOCKMAN JEFFREY ALLEN & DIANA                                | PO BOX 206, MOUNT CARBON, WV 25139                                          |       1 |     0.3
 FLEMING MICHAEL J                                            | PO BOX 241, MOUNT CARBON, WV 25139                                          |       1 |     0.3
 COLEMAN BONNIE L                                             | PO BOX 194, MT CARBON, WV 25139                                             |       1 |     0.3
 HARVEY GARY F II & MARY C                                    | BRANDIE STARCHER WVA FED CREDI, 75 ADENA DR, MOUNT CARBON, WV 25139         |       1 |     0.3
 DUNLAP JEFFREY & RITA                                        | PO BOX 64, MOUNT CARBON, WV 25139                                           |       1 |     0.3
 HANNIGAN SCOTT A                                             | 108 ELM ST, MT CARBON, WV 25139                                             |       2 |     0.3
 BELL SIDNEY & ETAL                                           | PO BOX 5, MOUNT CARBON, WV 25139                                            |       1 |     0.3
 MIDDLETON JOHN                                               | PO BOX 293, MOUNT CARBON, WV 25139                                          |       1 |     0.3
 DAVIS PATRICK L & HARRIET SUE                                | PO BOX 51, MOUNT CARBON, WV 25139                                           |       1 |     0.3
 JEFFERY KELLY R                                              | PO BOX 11, MOUNT CARBON, WV 25139                                           |       1 |     0.3
 MORRIS MIKE & KELLY                                          | PO BOX 52, MOUNT CARBON, WV 25139                                           |       1 |     0.3
 DEAN DOUGLAS L & AMY B                                       | PO BOX 313, MOUNT CARBON, WV 25139                                          |       1 |     0.3
 SCHOOLCRAFT EMMITT JR & LINDA                                | PO BOX 274, MOUNT CARBON, WV 25139                                          |       2 |     0.3
 MIDDLETON JOHN                                               | C/O ERIC HARVILLE, PO BOX 181, MOUNT CARBON, WV 25139                       |       1 |     0.3
 SCOTT JUDITH A                                               | PO BOX 175, MT CARBON, WV 25139                                             |       1 |     0.3
 SCOTT MIKKI                                                  | PO BOX 145, MOUNT CARBON, WV 25139                                          |       1 |     0.3
 CLARK FRANKLIN PERRY JR & MONICA ANGEL                       | PO BOX 207, MT CARBON, WV 25139                                             |       1 |     0.3
 JOHNSON GERALD & TERRI L                                     | LE CHARLOTTE M JOHNSON, 440 ELLISON CIR, OAK HILL, WV 25901                 |       1 |     0.3
 SIGMON BOBBIE J & SHEPPHARD JIMMY J                          | PO BOX 393, MOUNT CARBON, WV 25139                                          |       1 |     0.3
 WALLACE WATSON ET UX                                         | C/O CHARLOTTE BOYD, 9126 S PULASKI RD, OAK LAWN, IL 60453                   |       1 |     0.3
 STEVENSON CHARLES                                            | 16977 DEEPWATER MTN RD, MT CARBON, WV 25139                                 |       1 |     0.3
 SIMPSON TERESA A                                             | PO BOX 441, MOUNT CARBON, WV 25139                                          |       1 |     0.3
 RIDDLE JOHN II & ETAL                                        | PO BOX 344, MT CARBON, WV 25139                                             |       1 |     0.3
 WALKER CONNIE S                                              | PO BOX 235, MOUNT CARBON, WV 25139                                          |       1 |     0.3
 SKAGGS RICHARD L & KAREN E                                   | PO BOX 205, MOUNT CARBON, WV 25139                                          |       1 |     0.3
 CHAPMAN BARBARA & MIDDLETON BEVERLY                          | PO BOX 411, MOUNT CARBON, WV 25139                                          |       1 |     0.3
 PRETE JASON P                                                | PO BOX 142, MOUNT CARBON, WV 25139                                          |       1 |     0.3
 LILLY TOMMY & LINDA                                          | PO BOX 74, MOUNT CARBON, WV 25139                                           |       1 |     0.3
 SMITH RONALD E                                               | 17047 DEEPWATER MTN RD, MOUNT CARBON, WV 25139                              |       1 |     0.3
 SMITH RONALD E                                               | 17047 DEEPWATER MTN RD, MT CARBON, WV 25139                                 |       2 |     0.3
 WASHINGTON LAWRENCE & ET AL                                  | PO BOX 12, MOUNT CARBON, WV 25139                                           |       1 |     0.3
 SMITH RONALD E & KANDY L                                     | 17047 DEEPWATER MTN RD, MOUNT CARBON, WV 25139                              |       1 |     0.3
 LOCKMAN DIANA L & JEFFREY A                                  | PO BOX 206, MT CARBON, WV 25139                                             |       1 |     0.3
 HUDNALL MARK L                                               | PO BOX 24, MT CARBON, WV 25139                                              |       1 |     0.3
 CLARK FRANKLIN PERRY JR & MONTICA ANGEL                      | PO BOX 207, MT CARBON, WV 25139                                             |       1 |     0.3
 BYERS VONDALERE & FAIRFAX JERMAINE                           | PO BOX 294, MOUNT CARBON, WV 25139                                          |       3 |     0.2
 COLEMAN CHARLOTTE J                                          | PO BOX 422, MOUNT CARBON, WV 25139                                          |       1 |     0.2
 CRIDER JOHN & HUMPHREY MARY                                  | 169 CARMEN DR, MT CARBON, WV 25139                                          |       1 |     0.2
 DECKER RONALD ARTHUR                                         | PO BOX 473, MOUNT CARBON, WV 25139                                          |       1 |     0.2
 BURROUGH JASON E & NICHOLE                                   | 102 ELM DR, MT CARBON, WV 25136                                             |       1 |     0.2
 FERRELL SETH                                                 | PO BOX 423, MOUNT CARBON, WV 25139                                          |       1 |     0.2
 FRANCIS SCOTT A & CHRISTIAN                                  | PO BOX 302, MOUNT CARBON, WV 25139                                          |       1 |     0.2
 GARRETSON JERRY W & TERRY D                                  | PO BOX 134, MOUNT CARBON, WV 25139                                          |       1 |     0.2
 GRAHAM HAYLE M & MICHAEL K                                   | PO BOX 511, MOUNT CARBON, WV 25139                                          |       1 |     0.2
 GRAHAM HAYLE M & MICHAEL K                                   | PO BOX 511, MT CARBON, WV 25139                                             |       1 |     0.2
 HALL MICHAEL T                                               | PO BOX 354, MT CARBON, WV 25139                                             |       1 |     0.2
 HANCOCK JOHN & ANNA M                                        | PO BOX 232, MT CARBON, WV 25139                                             |       1 |     0.2
 HANNIGAN JOHN A ETUX                                         | PO BOX 94, MOUNT CARBON, WV 25139                                           |       1 |     0.2
 HARPER PEGGY S & GINGISE EMORY JOHN II                       | PO BOX 331, MT CARBON, WV 25136                                             |       1 |     0.2
 HARVEY GARY F II & MARY C                                    | PO BOX 301, MT CARBON, WV 25139                                             |       1 |     0.2
 BURROUGH ERNEST & MARGARET                                   | BOX 163, MT CARBON, WV 25139                                                |       1 |     0.2
 BUCKNER TERRY WAYNE                                          | PO BOX 21, MT CARBON, WV 25139                                              |       1 |     0.2
 BROWN VALENTINE LAYNA SUE & TIMOTHY JOHN                     | PO BOX 254, MOUNT CARBON, WV 25139                                          |       1 |     0.2
 BROWN LAWRENCE E & JEAN ANN                                  | BOX 153, MT CARBON, WV 25139                                                |       1 |     0.2
 HILL MAXWELL JR & DEBORAH A                                  | PO BOX 201, MT CARBON, WV 25139                                             |       1 |     0.2
 HOPKINS VINCENT E & STEPHANIE                                | PO BOX 451, MOUNT CARBON, WV 25139                                          |       1 |     0.2
 BOWEN MARGARET ELLEN                                         | PO BOX 443, MT CARBON, WV 25139                                             |       1 |     0.2
 BOGGS EARL E                                                 | 6803 CHARLOTTE HARBOR WAY, TAMPA, FL 33625                                  |       1 |     0.2
 INGRAM JAMES W & TERRY L                                     | PO BOX 145, MOUNT CARBON, WV 25139                                          |       1 |     0.2
 INGRAM KRISTI L                                              | 156 GINA DR, MT CARBON, WV 25139                                            |       1 |     0.2
 JACKSON SHERMAN W JR                                         | PO BOX 202, MOUNT CARBON, WV 25139                                          |       1 |     0.2
 JARRETT JEFFERY E                                            | PO BOX 71, MOUNT CARBON, WV 25139                                           |       2 |     0.2
 JOHNSON ALFONSO R & THERESA L                                | PO BOX 68, MOUNT CARBON, WV 25139                                           |       1 |     0.2
 JOHNSON GREGORY S & MARSHA L                                 | PO BOX 481, MOUNT CARBON, WV 25139                                          |       1 |     0.2
 JOHNSON MELISSA D & TOMMY L II                               | PO BOX 2, MOUNT CARBON, WV 25139                                            |       1 |     0.2
 JONES RICHARD D & PHILLISA A                                 | 5908 STIRLING SHIRE CT, CHARLOTTE, NC 28278                                 |       1 |     0.2
 JONES TIMOTHY E                                              | PO BOX 215, MOUNT CARBON, WV 25139                                          |       2 |     0.2
 KINCAID ALYSSA L & NOTTINGHAM RYAN J                         | PO BOX 502, MOUNT CARBON, WV 25139                                          |       1 |     0.2
 KINDER MARY B                                                | GEN DEL, MT CARBON, WV 25139                                                |       1 |     0.2
 LEAKE GEORGE R SR AND KAY L                                  | PO BOX 31, MT CARBON, WV 25139                                              |       1 |     0.2
 LEAKE KAY LYNN & GEORGE                                      | PO BOX 31, MT CARBON, WV 25139                                              |       1 |     0.2
 BOGGESS BETTY JO                                             | C/O RICHARD SKAGGS, PO BOX 7, MOUNT CARBON, WV 25139                        |       1 |     0.2
 LIDDLE STACEY RENEA                                          | PO BOX 182, MOUNT CARBON, WV 25139                                          |       1 |     0.2
 LINKENHOKER MICHAEL B                                        | PO BOX 212, MOUNT CARBON, WV 25139                                          |       1 |     0.2
 LOCKMAN JEFFREY A & DIANA L                                  | PO BOX 206, MOUNT CARBON, WV 25139                                          |       1 |     0.2
 LOKSHIN NATALYA & DIANA                                      | 302 VISTA GRANDE CIR, CHARLOTTE, NC 28226                                   |       1 |     0.2
 BLANKENSHIP TYLER AUSTIN                                     | PO BOX 400, MOUNT CARBON, WV 25139                                          |       1 |     0.2
 MARTIN JOE BILL                                              | 36 ELM DR, MOUNT CARBON, WV 25139                                           |       1 |     0.2
 BLAKE RONALD                                                 | 52 MONTGOMERY HGTS RD, MT CARBON, WV 25139                                  |       1 |     0.2
 MCCOMMACK DEBRA M FLEMING & BONDURANT ANGELA D               | PO BOX 312, MT CARBON, WV 25139                                             |       1 |     0.2
 MCDONALD SANDRA G                                            | PO BOX 124, MOUNT CARBON, WV 25139                                          |       2 |     0.2
 MILLER CHRISTOPHER LEE & LINDA LOU                           | PO BOX 154, MT CARBON, WV 25139                                             |       1 |     0.2
 MILLER CHRISTOPHER LEE LINDA LOU                             | PO BOX 154, MT CARBON, WV 25139                                             |       1 |     0.2
 MILLS ROBYN J & JOHN C                                       | 149 GINA ST, MOUNT CARBON, WV 25139                                         |       1 |     0.2
 MILLS ROBYN J & JOHN C                                       | 149 GINA ST, MT CARBON, WV 25139                                            |       1 |     0.2
 MOORE TINA MARIE                                             | C/O TINA JACKSON, PO BOX 202, MOUNT CARBON, WV 25139                        |       1 |     0.2
 BLAIR DEBORAH ANN WALKER                                     | PO BOX 61, MOUNT CARBON, WV 25139                                           |       1 |     0.2
 BALDWIN TAYLOR C & JARRELL BRADLEY J                         | 106 ELM DR, MOUNT CARBON, WV 25139                                          |       1 |     0.2
 OILER ROSEMARY                                               | 1233 ROBINHOOD DR, CHARLOTTE, NC 28227                                      |       1 |     0.2
 PAGE CHURCH OF GOD                                           | PO BOX 67, MOUNT CARBON, WV 25139                                           |       1 |     0.2
 ANGEL VALERIE ANN                                            | PO BOX 123, MOUNT CARBON, WV 25139                                          |       1 |     0.2
 PENNINGTON JAMES G & BILLIE JEAN                             | PO BOX 263, MT CARBON, WV 25139                                             |       2 |     0.2
 ANGEL SAMUEL W & KAREN J                                     | PO BOX 279, MT CARBON, WV 25139                                             |       1 |     0.2
 PROCTOR JAMES E                                              | 178 CARMEN DR, MOUNT CARBON, WV 25139                                       |       2 |     0.2
 PUGH SUSAN                                                   | PO BOX 174, MOUNT CARBON, WV 25139                                          |       1 |     0.2
 PUTTAIAH GOVINDAPPA ETUX                                     | PO BOX 184, MOUNT CARBON, WV 25139                                          |       1 |     0.2
 RAYNES COLTON W                                              | 11 FORTUNA DR, MOUNT CARBON, WV 25139                                       |       1 |     0.2
 RIDENOUR CLINTON D                                           | PO BOX 282, MOUNT CARBON, WV 25139                                          |       1 |     0.2
 RIDENOUR CLINTON DALE                                        | PO BOX 282, MOUNT CARBON, WV 25139                                          |       1 |     0.2
 ROWE GARY A                                                  | PO BOX 262, MT CARBON, WV 25319                                             |       1 |     0.2
 ROWE GARY A & MILLER CHRIS                                   | PO BOX 262, MOUNT CARBON, WV 25139                                          |       1 |     0.2
 ROWSEY WM BYRON & BILLIE JANE                                | PO BOX 98, MT CARBON, WV 25139                                              |       1 |     0.2
 RYAN CLINTON & THERESA                                       | PO BOX 1, MOUNT CARBON, WV 25139                                            |       1 |     0.2
 SCHOOLCRAFT EMMETT & LINDA MARIE                             | PO BOX 274, MOUNT CARBON, WV 25139                                          |       1 |     0.2
 SIGLER TERRY                                                 | PO BOX 67, MT CARBON, WV 25139                                              |       1 |     0.2
 SIZEMORE BRIANNA N                                           | 161 CARMEN DR, MOUNT CARBON, WV 25139                                       |       1 |     0.2
 SMITH RONALD E                                               | 17065 DEEPWATER MTN RD, MOUNT CARBON, WV 25139                              |       1 |     0.2
 SMITH RONALD & KANDY & MEGAN                                 | 17047 DEEPWATER MTN RD, MOUNT CARBON, WV 25139                              |       2 |     0.2
 SNUFFER SHARON LEE & JERRY LEE SR                            | LE & C/O CHARLOTTE K ALIFF, 4588 DENMAR RD, HILLSBORO, WV 24946             |       1 |     0.2
 SODDER ALICIA D & JOSEPH S III                               | 98 MONTGOMERY HEIGHTS RD, MOUNT CARBON, WV 25139                            |       1 |     0.2
 STILTNER ELMER DEAN & MARSHA L                               | PO BOX 81, MT CARBON, WV 25139                                              |       1 |     0.2
 STONE BREYANNA G                                             | 177 CARMEN DR, MOUNT CARBON, WV 25139                                       |       1 |     0.2
 TAYLOR JOHN & AMY                                            | PO BOX 211, MOUNT CARBON, WV 25139                                          |       1 |     0.2
 TAYLOR JOHN & AMY                                            | PO BOX 211, MT CARBON, WV 25139                                             |       1 |     0.2
 TERRELL DEBBIE & MIDDELTON TAMERIA & BELCHER BRIAN           | PO BOX 501, MOUNT CARBON, WV 25139                                          |       1 |     0.2
 THOMAS BRIAN DAVID                                           | 143 GINA DR, MOUNT CARBON, WV 25139                                         |       1 |     0.2
 THOMAS BRIAN DAVID                                           | 143 GINA DR, MT CARBON, WV 25139                                            |       1 |     0.2
 TONEY GREGORY A & JENNIFER F                                 | PO BOX 372, MOUNT CARBON, WV 25139                                          |       1 |     0.2
 TUCKER JERRY L & ANGELA G                                    | 129 GINA DR, MT CARBON, WV 25139                                            |       1 |     0.2
 ALEXANDER JARED ISAIAH                                       | 147 GINA ST, MOUNT CARBON, WV 25139                                         |       1 |     0.2
 ABBOTT TERRY L & DEBORAH L                                   | PO BOX 63, MT CARBON, WV 25139                                              |       1 |     0.2
 WHITE GARY WAYNE                                             | C/O GARY WHITE, 17075 DEEPWATER MTN RD, MT CARBON, WV 25139                 |       1 |     0.2
 WHITT ERNEST A JR & KAREN S                                  | PO BOX 303, MOUNT CARBON, WV 25139                                          |       1 |     0.2
 WILLIAMS MELISSA                                             | PO BOX 87, MOUNT CARBON, WV 25139                                           |       1 |     0.2
 WILLIAMS ROBERT G                                            | PO BOX 503, MOUNT CARBON, WV 25139                                          |       1 |     0.2
 WILSON ANGELA                                                | PO BOX 434, MT CARBON, WV 25139                                             |       1 |     0.2
 CARELLI JOSEPH D & BONNIE J LE FRANK & JOYCE CARTE           | PO BOX 42, MOUNT CARBON, WV 25139                                           |       1 |     0.2
 WHITLOCK ALIVIA NICHOLE                                      | PO BOX 82, MOUNT CARBON, WV 25139                                           |       1 |     0.1
 QUEEN CLIFTON & PARKER WILLIAM                               | PO BOX 7, MOUNT CARBON, WV 25139                                            |       1 |     0.1
 PETRY DIANNA LOU                                             | 17135 DEEPWATER MTN RD, MOUNT CARBON, WV 25139                              |       1 |     0.1
 TIMBAYAN ADIN L                                              | PO BOX 36, MOUNT CARBON, WV 25139                                           |       1 |     0.1
 PETRY DIANNA                                                 | 17145 DEEPWATER MTN RD, MOUNT CARBON, WV 25139                              |       1 |     0.1
 RHODES PATRICIA A                                            | 90 MONTGOMERY HEIGHTS RD, MT CARBON, WV 25139                               |       1 |     0.1
 WISEMAN TODD W & KRISTA C                                    | 64 FORTUNA DR, MOUNT CARBON, WV 25139                                       |       1 |     0.1
 THOMAS CATHERINE  L                                          | 911 CHARLOTTE DR, NEWPORT NEWS, VA 23601                                    |       1 |     0.1
 MCGRAW DWAYNE E                                              | PO BOX 123, MOUNT CARBON, WV 25139                                          |       1 |     0.1
 MCCANN JESSICA & COX DUSTIN                                  | PO BOX 512, MOUNT CARBON, WV 25139                                          |       1 |     0.1
 CRINITI DORIS MARIE                                          | PO BOX 362, MOUNT CARBON, WV 25139                                          |       1 |     0.1
 BLAKE RONALD L                                               | 52 MONTGOMERY HTS RD, MT CARBON, WV 25139                                   |       1 |     0.1
 WHITT JOHN M & TIFFANY R                                     | PO BOX 283, MT CARBON, WV 25139                                             |       1 |     0.1
 MANTOWSKI RENEE & JEFFRIES TODD                              | 15 CEMETERY RD, MOUNT CARBON, WV 25139                                      |       1 |     0.1
 LOCKMAN JEFFREY ALLEN & DIANNA L                             | PO BOX 206, MOUNT CARBON, WV 25139                                          |       1 |     0.1
 JACKSON CARL M III                                           | 17193 DEEPWATER MTN RD, MOUNT CARBON, WV 25139                              |       1 |     0.1
 BROWN LAWRENCE E II & JEAN ANN                               | BOX 153, MT CARBON, WV 25139                                                |       1 |     0.1
 CHAPMAN BARBARA E                                            | PO BOX 411, MOUNT CARBON, WV 25139                                          |       1 |     0.1
 SNYDER P M ET AL                                             | PHILIP M SNYDER AGENT, 2228 GRAYSTONE LN, CHAPEL HILL, NC 27514             |       1 |     0.1
 SMITH RONALD & KANDY L                                       | HC 69 BOX 26, MT CARBON, WV 25139                                           |       1 |     0.1
 SPAULDING MIKE & ROSE                                        | PO BOX 324, MT CARBON, WV 25139                                             |       1 |     0.1
 SIGMON CHARLES & SHIRLEY                                     | PO BXO 234, MT CARBON, WV 25139                                             |       1 |     0.1
 SIGMON CHARLES & SHIRLEY                                     | PO BOX 234, MOUNT CARBON, WV 25139                                          |       1 |     0.1
 STEWART HAROLD G & LINDA S                                   | 17 MONT HEIGHTS RD, MT CARBON, WV 25139                                     |       1 |     0.1
 STEWART JEFFREY & BRANDI                                     | PO BOX 384, MOUNT CARBON, WV 25139                                          |       1 |     0.1
 HANNIGAN SCOTT A                                             | PO BOX 94, MOUNT CARBON, WV 25139                                           |       1 |     0.1
 WHEELER ROBERT E & TAMARA                                    | PO BOX 433, MOUNT CARBON, WV 25139                                          |       1 |     0.1
 SCHNITZLER ANNA MARIE LE LARRY E & ANNA L LUCAS              | PO BOX 91, MT CARBON, WV 25139                                              |       1 |     0.1
 TACY JACQUELINE                                              | 3500 ARMSTRONG CRK RD, MOUNT CARBON, WV 25139                               |       1 |     0.1
 GRAHAM MICHAEL KENNETH                                       | PO BOX 511, MOUNT CARBON, WV 25139                                          |       1 |     0.1
 FERTIG RICHARD BRIAN & FERTIG-GLOVER KATHERINE ANN           | 17163 DEEPWATER MTN RD, MOUNT CARBON, WV 25139                              |       1 |     0.1
 TIMBAYAN MARISSA EDUC TRUST & TIMBAYAN ALADDIN JOHN ED TRUST | C/O MARISSA TIMBAYAN, PO BOX 36, MT CARBON, WV 25139                        |       1 |     0.0
 TIMBAYAN MARISSA EDUC TRUST & TIMBAYAN ALADDIN JOHN ED TRUST | PO BOX 36, MT CARBON, WV 25139                                              |       1 |     0.0
 CARR GLORIA MAE                                              | C/O ANNA HANCOCK, PO BOX 232, MOUNT CARBON, WV 25139                        |       1 |     0.0
(272 rows)

(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:/opt/msjarvis-rebuild$ # 4. Total parcel count and acreage baseline
docker exec jarvis-local-resources-db psql -U postgres -d msjarvisgis --pset=pager=off -c "
SELECT COUNT(*) as total_parcels, ROUND(SUM(acres_c)::numeric, 1) as total_acres
FROM public.fayette_parcels;"
 total_parcels | total_acres 
---------------+-------------
         39515 |    430416.8
(1 row)

(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:/opt/msjarvis-rebuild$ 

