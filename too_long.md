(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~/msjarvis-rebuild$ sed -i 's/                buf\["documents"\].append(documents\[i\] if documents and i < len(documents) else None)/                buf["documents"].append(documents[i] if documents and i < len(documents) else None)\n                if len(buf["ids"]) >= 100_000:\n                    flushed = flush_buffer(client, cur_layer, buf, known_ids)\n                    total_migrated += flushed\n                    completed[cur_layer] = completed.get(cur_layer, 0) + flushed\n                    ckpt.update({"offset": offset, "layer_collection_ids": known_ids, "completed_layers": completed})\n                    save_checkpoint(ckpt)\n                    buf = {"ids": [], "embeddings": [], "metadatas": [], "documents": []}/' ~/msjarvis-rebuild/migrate_to_layer_collections_v3.py
(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~/msjarvis-rebuild$ grep -n "MidFlush\|100_000\|buf = {" ~/msjarvis-rebuild/migrate_to_layer_collections_v3.py
150:        buf = {"ids": [], "embeddings": [], "metadatas": [], "documents": []}
180:                        buf = {"ids": [], "embeddings": [], "metadatas": [], "documents": []}
187:                if len(buf["ids"]) >= 100_000:
193:                    buf = {"ids": [], "embeddings": [], "metadatas": [], "documents": []}
(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~/msjarvis-rebuild$ python3 ~/msjarvis-rebuild/migrate_to_layer_collections_v3.py
Migration v3 (streaming flush): geospatialfeatures (12,389,268 vectors)
Resuming from offset 110,000 | 12 layers already completed
  Flushed blocks_census_2020_utm83: 24 | total 110,048 | 48900/s | ETA 4.2min
  ...      115,000/12,389,268 | buf=4,976 (blocks_census_2020_wma84) | 51064/s | ETA 4.0min
  ...      120,000/12,389,268 | buf=9,976 (blocks_census_2020_wma84) | 28532/s | ETA 7.2min
  ...      125,000/12,389,268 | buf=14,976 (blocks_census_2020_wma84) | 20004/s | ETA 10.2min
  ...      130,000/12,389,268 | buf=19,976 (blocks_census_2020_wma84) | 15615/s | ETA 13.1min
  ...      135,000/12,389,268 | buf=24,976 (blocks_census_2020_wma84) | 13038/s | ETA 15.7min
  ...      140,000/12,389,268 | buf=29,976 (blocks_census_2020_wma84) | 11168/s | ETA 18.3min
  ...      145,000/12,389,268 | buf=34,976 (blocks_census_2020_wma84) | 9917/s | ETA 20.6min
  ...      150,000/12,389,268 | buf=39,976 (blocks_census_2020_wma84) | 8940/s | ETA 22.8min
  ...      155,000/12,389,268 | buf=44,976 (blocks_census_2020_wma84) | 8198/s | ETA 24.9min
  ...      160,000/12,389,268 | buf=49,976 (blocks_census_2020_wma84) | 7549/s | ETA 27.0min
  ...      165,000/12,389,268 | buf=54,976 (blocks_census_2020_wma84) | 7027/s | ETA 29.0min
  ...      170,000/12,389,268 | buf=59,976 (blocks_census_2020_wma84) | 6581/s | ETA 30.9min
  ...      175,000/12,389,268 | buf=64,976 (blocks_census_2020_wma84) | 6203/s | ETA 32.8min
  ...      180,000/12,389,268 | buf=69,976 (blocks_census_2020_wma84) | 5869/s | ETA 34.7min
  Flushed blocks_census_2020_wma84: 72,558 | total 182,606 | 892/s | ETA 228.2min
  Flushed boundaryappalachianbasin_wvges_1996_utm83: 313 | total 182,919 | 889/s | ETA 228.8min
  ...      185,000/12,389,268 | buf=2,105 (bridges) | 899/s | ETA 226.1min
  ...      190,000/12,389,268 | buf=7,105 (bridges) | 913/s | ETA 222.8min
  Flushed bridges: 7,357 | total 190,276 | 845/s | ETA 240.8min
  Flushed calderl_reg_ll83: 9 | total 190,285 | 844/s | ETA 241.0min
  Flushed census_block_groups_2020_utm83: 1,639 | total 191,924 | 840/s | ETA 242.1min
  ...      195,000/12,389,268 | buf=3,100 (census_blocks_2020_utm83) | 854/s | ETA 238.1min
  ...      200,000/12,389,268 | buf=8,100 (census_blocks_2020_utm83) | 866/s | ETA 234.7min
  ...      205,000/12,389,268 | buf=13,100 (census_blocks_2020_utm83) | 878/s | ETA 231.3min
  ...      210,000/12,389,268 | buf=18,100 (census_blocks_2020_utm83) | 889/s | ETA 228.2min
  ...      215,000/12,389,268 | buf=23,100 (census_blocks_2020_utm83) | 901/s | ETA 225.3min
  ...      220,000/12,389,268 | buf=28,100 (census_blocks_2020_utm83) | 912/s | ETA 222.4min
  ...      225,000/12,389,268 | buf=33,100 (census_blocks_2020_utm83) | 923/s | ETA 219.7min
  ...      230,000/12,389,268 | buf=38,100 (census_blocks_2020_utm83) | 933/s | ETA 217.1min
  ...      235,000/12,389,268 | buf=43,100 (census_blocks_2020_utm83) | 943/s | ETA 214.7min
  ...      240,000/12,389,268 | buf=48,100 (census_blocks_2020_utm83) | 953/s | ETA 212.5min
  ...      245,000/12,389,268 | buf=53,100 (census_blocks_2020_utm83) | 962/s | ETA 210.4min
  ...      250,000/12,389,268 | buf=58,100 (census_blocks_2020_utm83) | 971/s | ETA 208.4min
  ...      255,000/12,389,268 | buf=63,100 (census_blocks_2020_utm83) | 979/s | ETA 206.5min
  ...      260,000/12,389,268 | buf=68,100 (census_blocks_2020_utm83) | 987/s | ETA 204.8min
  Flushed census_blocks_2020_utm83: 72,558 | total 264,482 | 695/s | ETA 290.7min
  Flushed census_cities_over10k_2020_utm83: 14 | total 264,496 | 695/s | ETA 290.9min
  Flushed census_cities_over2500_2020_utm83: 63 | total 264,559 | 695/s | ETA 291.0min
  Flushed census_county_boundaries_2021_utm83: 55 | total 264,614 | 694/s | ETA 291.1min
  Flushed census_designated_places_2021_utm83: 207 | total 264,821 | 694/s | ETA 291.2min
  Flushed census_empowerment_zones_2002_utm83: 11 | total 264,832 | 694/s | ETA 291.3min
  Flushed census_historical_pop_by_county_2006_utm83: 55 | total 264,887 | 694/s | ETA 291.4min
  ...      265,000/12,389,268 | buf=137 (census_incorporated_places_2021_utm83) | 694/s | ETA 291.1min
  Flushed census_incorporated_places_2021_utm83: 464 | total 265,351 | 687/s | ETA 294.0min
  Flushed census_metro_micro_areas_2020_utm83: 17 | total 265,368 | 687/s | ETA 294.1min
  Flushed census_minor_civil_divisions_2020_utm83: 228 | total 265,596 | 687/s | ETA 294.2min
  Flushed census_misc_transportation_2000_utm83: 5 | total 265,601 | 686/s | ETA 294.4min
  Flushed census_pop_change_communities_2020_utm83: 284 | total 265,885 | 686/s | ETA 294.5min
  Flushed census_pop_change_counties_2020_utm83: 55 | total 265,940 | 686/s | ETA 294.6min
  Flushed census_populated_places_2020_utm83: 439 | total 266,379 | 686/s | ETA 294.7min
  Flushed census_railroads_2023_utm83: 1,505 | total 267,884 | 686/s | ETA 294.5min
  ...      270,000/12,389,268 | buf=2,140 (census_roads_2023_utm83) | 692/s | ETA 292.1min
  ...      275,000/12,389,268 | buf=7,140 (census_roads_2023_utm83) | 698/s | ETA 289.2min
  ...      280,000/12,389,268 | buf=12,140 (census_roads_2023_utm83) | 705/s | ETA 286.5min
  ...      285,000/12,389,268 | buf=17,140 (census_roads_2023_utm83) | 711/s | ETA 283.9min
  ...      290,000/12,389,268 | buf=22,140 (census_roads_2023_utm83) | 717/s | ETA 281.4min
  ...      295,000/12,389,268 | buf=27,140 (census_roads_2023_utm83) | 722/s | ETA 279.1min
  ...      300,000/12,389,268 | buf=32,140 (census_roads_2023_utm83) | 728/s | ETA 276.9min
  ...      305,000/12,389,268 | buf=37,140 (census_roads_2023_utm83) | 733/s | ETA 274.7min
  ...      310,000/12,389,268 | buf=42,140 (census_roads_2023_utm83) | 738/s | ETA 272.7min
  ...      315,000/12,389,268 | buf=47,140 (census_roads_2023_utm83) | 743/s | ETA 270.8min
  ...      320,000/12,389,268 | buf=52,140 (census_roads_2023_utm83) | 748/s | ETA 268.9min
  ...      325,000/12,389,268 | buf=57,140 (census_roads_2023_utm83) | 753/s | ETA 267.2min
  ...      330,000/12,389,268 | buf=62,140 (census_roads_2023_utm83) | 757/s | ETA 265.6min
  ...      335,000/12,389,268 | buf=67,140 (census_roads_2023_utm83) | 761/s | ETA 264.1min
  ...      340,000/12,389,268 | buf=72,140 (census_roads_2023_utm83) | 765/s | ETA 262.6min
  ...      345,000/12,389,268 | buf=77,140 (census_roads_2023_utm83) | 768/s | ETA 261.3min
  ...      350,000/12,389,268 | buf=82,140 (census_roads_2023_utm83) | 771/s | ETA 260.1min
  ...      355,000/12,389,268 | buf=87,140 (census_roads_2023_utm83) | 772/s | ETA 259.7min
  ...      360,000/12,389,268 | buf=92,140 (census_roads_2023_utm83) | 773/s | ETA 259.3min
  ...      365,000/12,389,268 | buf=97,140 (census_roads_2023_utm83) | 776/s | ETA 258.1min
  ...      370,000/12,389,268 | buf=2,140 (census_roads_2023_utm83) | 605/s | ETA 331.1min
  ...      375,000/12,389,268 | buf=7,140 (census_roads_2023_utm83) | 608/s | ETA 329.1min
  ...      380,000/12,389,268 | buf=12,140 (census_roads_2023_utm83) | 612/s | ETA 327.2min
  ...      385,000/12,389,268 | buf=17,140 (census_roads_2023_utm83) | 615/s | ETA 325.4min
  ...      390,000/12,389,268 | buf=22,140 (census_roads_2023_utm83) | 618/s | ETA 323.7min
  ...      395,000/12,389,268 | buf=27,140 (census_roads_2023_utm83) | 621/s | ETA 322.0min
  ...      400,000/12,389,268 | buf=32,140 (census_roads_2023_utm83) | 624/s | ETA 320.4min
  ...      405,000/12,389,268 | buf=37,140 (census_roads_2023_utm83) | 626/s | ETA 318.8min
  ...      410,000/12,389,268 | buf=42,140 (census_roads_2023_utm83) | 629/s | ETA 317.3min
  ...      415,000/12,389,268 | buf=47,140 (census_roads_2023_utm83) | 632/s | ETA 315.9min
  ...      420,000/12,389,268 | buf=52,140 (census_roads_2023_utm83) | 634/s | ETA 314.5min
  ...      425,000/12,389,268 | buf=57,140 (census_roads_2023_utm83) | 637/s | ETA 313.2min
  ...      430,000/12,389,268 | buf=62,140 (census_roads_2023_utm83) | 639/s | ETA 312.0min
  ...      435,000/12,389,268 | buf=67,140 (census_roads_2023_utm83) | 641/s | ETA 310.8min
  ...      440,000/12,389,268 | buf=72,140 (census_roads_2023_utm83) | 643/s | ETA 309.6min
  ...      445,000/12,389,268 | buf=77,140 (census_roads_2023_utm83) | 645/s | ETA 308.6min
  ...      450,000/12,389,268 | buf=82,140 (census_roads_2023_utm83) | 647/s | ETA 307.6min
  ...      455,000/12,389,268 | buf=87,140 (census_roads_2023_utm83) | 649/s | ETA 306.7min
  ...      460,000/12,389,268 | buf=92,140 (census_roads_2023_utm83) | 651/s | ETA 305.6min
  ...      465,000/12,389,268 | buf=97,140 (census_roads_2023_utm83) | 652/s | ETA 304.9min
  ...      470,000/12,389,268 | buf=2,140 (census_roads_2023_utm83) | 555/s | ETA 357.8min
  ...      475,000/12,389,268 | buf=7,140 (census_roads_2023_utm83) | 557/s | ETA 356.4min
  ...      480,000/12,389,268 | buf=12,140 (census_roads_2023_utm83) | 559/s | ETA 355.0min
  ...      485,000/12,389,268 | buf=17,140 (census_roads_2023_utm83) | 561/s | ETA 353.7min
  ...      490,000/12,389,268 | buf=22,140 (census_roads_2023_utm83) | 563/s | ETA 352.3min
  ...      495,000/12,389,268 | buf=27,140 (census_roads_2023_utm83) | 565/s | ETA 351.1min
  ...      500,000/12,389,268 | buf=32,140 (census_roads_2023_utm83) | 566/s | ETA 350.0min
  ...      505,000/12,389,268 | buf=37,140 (census_roads_2023_utm83) | 568/s | ETA 348.9min
  ...      510,000/12,389,268 | buf=42,140 (census_roads_2023_utm83) | 569/s | ETA 347.7min
  ...      515,000/12,389,268 | buf=47,140 (census_roads_2023_utm83) | 571/s | ETA 346.6min
  ...      520,000/12,389,268 | buf=52,140 (census_roads_2023_utm83) | 572/s | ETA 345.6min
  ...      525,000/12,389,268 | buf=57,140 (census_roads_2023_utm83) | 574/s | ETA 344.6min
  ...      530,000/12,389,268 | buf=62,140 (census_roads_2023_utm83) | 575/s | ETA 343.8min
  ...      535,000/12,389,268 | buf=67,140 (census_roads_2023_utm83) | 576/s | ETA 342.9min
  ...      540,000/12,389,268 | buf=72,140 (census_roads_2023_utm83) | 578/s | ETA 342.0min
  ...      545,000/12,389,268 | buf=77,140 (census_roads_2023_utm83) | 579/s | ETA 341.1min
  ...      550,000/12,389,268 | buf=82,140 (census_roads_2023_utm83) | 580/s | ETA 340.2min
  ...      555,000/12,389,268 | buf=87,140 (census_roads_2023_utm83) | 581/s | ETA 339.4min
  Flushed census_roads_2023_utm83: 87,515 | total 555,399 | 513/s | ETA 384.2min
  ...      560,000/12,389,268 | buf=4,625 (census_streams_waterbodies_2023_utm83) | 518/s | ETA 380.9min
  ...      565,000/12,389,268 | buf=9,625 (census_streams_waterbodies_2023_utm83) | 519/s | ETA 379.9min
  ...      570,000/12,389,268 | buf=14,625 (census_streams_waterbodies_2023_utm83) | 520/s | ETA 378.9min
  ...      575,000/12,389,268 | buf=19,625 (census_streams_waterbodies_2023_utm83) | 520/s | ETA 378.9min
  ...      580,000/12,389,268 | buf=24,625 (census_streams_waterbodies_2023_utm83) | 520/s | ETA 378.2min
  ...      585,000/12,389,268 | buf=29,625 (census_streams_waterbodies_2023_utm83) | 522/s | ETA 377.2min
  ...      590,000/12,389,268 | buf=34,625 (census_streams_waterbodies_2023_utm83) | 523/s | ETA 376.2min
  ...      595,000/12,389,268 | buf=39,625 (census_streams_waterbodies_2023_utm83) | 524/s | ETA 375.4min
  ...      600,000/12,389,268 | buf=44,625 (census_streams_waterbodies_2023_utm83) | 525/s | ETA 374.5min
  ...      605,000/12,389,268 | buf=49,625 (census_streams_waterbodies_2023_utm83) | 526/s | ETA 373.6min
  ...      610,000/12,389,268 | buf=54,625 (census_streams_waterbodies_2023_utm83) | 527/s | ETA 372.8min
  ...      615,000/12,389,268 | buf=59,625 (census_streams_waterbodies_2023_utm83) | 527/s | ETA 372.1min
  ...      620,000/12,389,268 | buf=64,625 (census_streams_waterbodies_2023_utm83) | 528/s | ETA 371.4min
  Flushed census_streams_waterbodies_2023_utm83: 67,774 | total 623,173 | 497/s | ETA 394.6min
  Flushed census_tl_2020_54_bg: 1,639 | total 624,812 | 497/s | ETA 394.5min
  ...      625,000/12,389,268 | buf=212 (census_tl_2020_54_tabblock20) | 497/s | ETA 394.2min
  ...      630,000/12,389,268 | buf=5,212 (census_tl_2020_54_tabblock20) | 498/s | ETA 393.3min
  ...      635,000/12,389,268 | buf=10,212 (census_tl_2020_54_tabblock20) | 499/s | ETA 392.5min
  ...      640,000/12,389,268 | buf=15,212 (census_tl_2020_54_tabblock20) | 500/s | ETA 391.7min
  ...      645,000/12,389,268 | buf=20,212 (census_tl_2020_54_tabblock20) | 501/s | ETA 390.9min
  ...      650,000/12,389,268 | buf=25,212 (census_tl_2020_54_tabblock20) | 502/s | ETA 390.1min
  ...      655,000/12,389,268 | buf=30,212 (census_tl_2020_54_tabblock20) | 502/s | ETA 389.5min
  ...      660,000/12,389,268 | buf=35,212 (census_tl_2020_54_tabblock20) | 503/s | ETA 388.8min
  ...      665,000/12,389,268 | buf=40,212 (census_tl_2020_54_tabblock20) | 503/s | ETA 388.2min
  ...      670,000/12,389,268 | buf=45,212 (census_tl_2020_54_tabblock20) | 504/s | ETA 387.5min
  ...      675,000/12,389,268 | buf=50,212 (census_tl_2020_54_tabblock20) | 505/s | ETA 386.9min
  ...      680,000/12,389,268 | buf=55,212 (census_tl_2020_54_tabblock20) | 505/s | ETA 386.3min
  ...      685,000/12,389,268 | buf=60,212 (census_tl_2020_54_tabblock20) | 506/s | ETA 385.7min
  ...      690,000/12,389,268 | buf=65,212 (census_tl_2020_54_tabblock20) | 506/s | ETA 385.0min
  ...      695,000/12,389,268 | buf=70,212 (census_tl_2020_54_tabblock20) | 507/s | ETA 384.4min
  Flushed census_tl_2020_54_tabblock20: 72,558 | total 697,370 | 467/s | ETA 417.4min
  ...      700,000/12,389,268 | buf=2,654 (census_tl_2020_us_county) | 469/s | ETA 415.7min
  Flushed census_tl_2020_us_county: 3,234 | total 700,604 | 465/s | ETA 419.0min
  ...      705,000/12,389,268 | buf=4,420 (census_tl_2020_us_zcta510) | 468/s | ETA 416.2min
  ...      710,000/12,389,268 | buf=9,420 (census_tl_2020_us_zcta510) | 468/s | ETA 415.6min
  ...      715,000/12,389,268 | buf=14,420 (census_tl_2020_us_zcta510) | 469/s | ETA 415.1min
  ...      720,000/12,389,268 | buf=19,420 (census_tl_2020_us_zcta510) | 469/s | ETA 415.0min
  ...      725,000/12,389,268 | buf=24,420 (census_tl_2020_us_zcta510) | 468/s | ETA 415.0min
  ...      730,000/12,389,268 | buf=29,420 (census_tl_2020_us_zcta510) | 468/s | ETA 414.8min
  Flushed census_tl_2020_us_zcta510: 33,144 | total 733,748 | 459/s | ETA 423.2min
  ...      735,000/12,389,268 | buf=1,276 (census_tl_2020_us_zcta520) | 460/s | ETA 422.4min
  ...      740,000/12,389,268 | buf=6,276 (census_tl_2020_us_zcta520) | 460/s | ETA 421.7min
  ...      745,000/12,389,268 | buf=11,276 (census_tl_2020_us_zcta520) | 461/s | ETA 421.1min
  ...      750,000/12,389,268 | buf=16,276 (census_tl_2020_us_zcta520) | 461/s | ETA 420.6min
  ...      755,000/12,389,268 | buf=21,276 (census_tl_2020_us_zcta520) | 462/s | ETA 420.0min
  ...      760,000/12,389,268 | buf=26,276 (census_tl_2020_us_zcta520) | 462/s | ETA 419.6min
  ...      765,000/12,389,268 | buf=31,276 (census_tl_2020_us_zcta520) | 462/s | ETA 419.1min
  Flushed census_tl_2020_us_zcta520: 33,791 | total 767,539 | 453/s | ETA 428.0min
  Flushed census_tracts_2020_utm83: 546 | total 768,085 | 453/s | ETA 427.9min
  Flushed census_urban_areas_100k_2020_utm83: 56 | total 768,141 | 453/s | ETA 428.0min
  Flushed census_zcta_2020_utm83: 741 | total 768,882 | 453/s | ETA 427.8min
  Flushed citieswithpopulation_2500_census_201111_gcs83: 65 | total 768,947 | 453/s | ETA 427.8min
  Flushed citieswithpopulation_2500_census_201111_utm83: 65 | total 769,012 | 453/s | ETA 427.9min
  Flushed citieswithpopulationover10k_census_201111_gcs83: 15 | total 769,027 | 453/s | ETA 427.9min
  Flushed citieswithpopulationover10k_uscensus_1990_ll83: 16 | total 769,043 | 453/s | ETA 427.9min
  Flushed citieswithpopulationover2500_uscensus_1990_ll83: 277 | total 769,320 | 453/s | ETA 427.9min
  Flushed citieswithpopulationsover10k_census_2020_utm83: 14 | total 769,334 | 453/s | ETA 427.9min
  Flushed citieswithpopulationsover2500_census_2020_utm83: 63 | total 769,397 | 453/s | ETA 428.0min
  Flushed citieswithpopulatoinover2500_uscensus_1990_utm83: 277 | total 769,674 | 453/s | ETA 427.9min
  Flushed coals2_ll83: 15 | total 769,689 | 453/s | ETA 428.0min
  Flushed coals2_utm27: 15 | total 769,704 | 453/s | ETA 428.0min
  Flushed coals2_utm83: 15 | total 769,719 | 453/s | ETA 428.0min
  Flushed communityboundary_min_att_20250121_utm83: 292 | total 770,011 | 453/s | ETA 428.0min
  ...      770,000/12,389,268 | buf=13 (communityboundary_min_att_20250121_wma84) | 453/s | ETA 427.8min
  Flushed communityboundary_min_att_20250121_wma84: 292 | total 770,303 | 450/s | ETA 430.3min
  Flushed communityhealthproviders_wvhealthcareauthority_200802_utm83: 150 | total 770,453 | 450/s | ETA 430.3min
  Flushed conversation_history: 1,434 | total 771,887 | 451/s | ETA 429.8min
  Flushed correctionalinstitutions_hsip_20091230_utm83: 108 | total 771,995 | 450/s | ETA 429.9min
  Flushed correctionalinstitutions_hsip_20091230_wgs84: 108 | total 772,103 | 450/s | ETA 430.0min
  ...      775,000/12,389,268 | buf=2,921 (county) | 452/s | ETA 428.2min
  Flushed county: 3,234 | total 775,337 | 449/s | ETA 431.0min
  Flushed countycityparkboundaries_20201104_utm83: 596 | total 775,933 | 449/s | ETA 431.0min
  Flushed countyseats_usgs_ll83: 55 | total 775,988 | 449/s | ETA 431.0min
  Flushed countyseats_usgs_utm83: 55 | total 776,043 | 449/s | ETA 431.0min
  Flushed courthousescounty_manysources_200203_ll83: 55 | total 776,098 | 449/s | ETA 431.1min
  Flushed courthousescounty_manysources_200203_utm83: 55 | total 776,153 | 449/s | ETA 431.1min
  Flushed courthousesfederal_manysources_200203_ll83: 10 | total 776,163 | 449/s | ETA 431.2min
  Flushed courthousesfederal_manysources_200203_utm: 10 | total 776,173 | 449/s | ETA 431.2min
  Flushed cousub: 228 | total 776,401 | 449/s | ETA 431.2min
  Flushed cvfault_ll83: 5 | total 776,406 | 449/s | ETA 431.2min
  Flushed cvfault_utm27: 5 | total 776,411 | 449/s | ETA 431.3min
  Flushed cvfault_utm83: 5 | total 776,416 | 449/s | ETA 431.3min
  Flushed cvpoly_ll83: 38 | total 776,454 | 449/s | ETA 431.4min
  Flushed cvpoly_utm27: 38 | total 776,492 | 449/s | ETA 431.4min
  Flushed cvpoly_utm83: 38 | total 776,530 | 449/s | ETA 431.4min
  Flushed dams_usarmycorpsofengineers_200010_utm83: 575 | total 777,105 | 449/s | ETA 431.5min
  Flushed dams_usarmycropsofengineers_200010_ll83: 575 | total 777,680 | 449/s | ETA 431.4min
  Flushed damsnoncoal_usgs_2002_ll27: 468 | total 778,148 | 449/s | ETA 431.3min
  ...      780,000/12,389,268 | buf=1,876 (edges) | 450/s | ETA 430.1min
  Flushed edges: 2,330 | total 780,478 | 446/s | ETA 433.5min
  Flushed empowermentzonesandenterprisecommunities_uscensus_2002_utm83: 11 | total 780,489 | 446/s | ETA 433.6min
  Flushed empowermentzonesandenterprisecommunitiesbytract_uscens_30c72907: 459 | total 780,948 | 446/s | ETA 433.5min
  Flushed equity_timesheet: 50 | total 780,998 | 446/s | ETA 433.6min
  Flushed excursionpassengertrains_wvdof_200102_ll83: 8 | total 781,006 | 446/s | ETA 433.7min
  Flushed excursionpassengertrains_wvdof_200102_utm83: 8 | total 781,014 | 446/s | ETA 433.7min
  ...      785,000/12,389,268 | buf=4,010 (faces) | 448/s | ETA 431.3min
  ...      790,000/12,389,268 | buf=9,010 (faces) | 449/s | ETA 430.7min
  Flushed faces: 9,165 | total 790,179 | 444/s | ETA 435.1min
  Flushed facilities_epa_200203_ll83: 2,137 | total 792,316 | 445/s | ETA 434.6min
  Flushed facilities_epa_200203_utm83: 2,137 | total 794,453 | 445/s | ETA 434.0min
  Flushed fault_reg_ll83: 124 | total 794,577 | 445/s | ETA 434.0min
  ...      795,000/12,389,268 | buf=447 (faultgl_reg_ll83) | 446/s | ETA 433.6min
  ...      800,000/12,389,268 | buf=5,447 (faultgl_reg_ll83) | 446/s | ETA 433.0min
  ...      805,000/12,389,268 | buf=10,447 (faultgl_reg_ll83) | 446/s | ETA 432.5min
  ...      810,000/12,389,268 | buf=15,447 (faultgl_reg_ll83) | 447/s | ETA 432.0min
  ...      815,000/12,389,268 | buf=20,447 (faultgl_reg_ll83) | 447/s | ETA 431.6min
  ...      820,000/12,389,268 | buf=25,447 (faultgl_reg_ll83) | 447/s | ETA 431.2min
  ...      825,000/12,389,268 | buf=30,447 (faultgl_reg_ll83) | 447/s | ETA 430.8min
  ...      830,000/12,389,268 | buf=35,447 (faultgl_reg_ll83) | 448/s | ETA 430.4min
  ...      835,000/12,389,268 | buf=40,447 (faultgl_reg_ll83) | 448/s | ETA 430.0min
  Flushed faultgl_reg_ll83: 43,084 | total 837,661 | 433/s | ETA 444.7min
  ...      840,000/12,389,268 | buf=2,363 (fayette_parcels) | 434/s | ETA 443.3min
  ...      845,000/12,389,268 | buf=7,363 (fayette_parcels) | 434/s | ETA 443.1min
  ...      850,000/12,389,268 | buf=12,363 (fayette_parcels) | 434/s | ETA 442.8min
  ...      855,000/12,389,268 | buf=17,363 (fayette_parcels) | 434/s | ETA 442.6min
  ...      860,000/12,389,268 | buf=22,363 (fayette_parcels) | 434/s | ETA 442.4min
  ...      865,000/12,389,268 | buf=27,363 (fayette_parcels) | 434/s | ETA 442.4min
  ...      870,000/12,389,268 | buf=32,363 (fayette_parcels) | 434/s | ETA 442.2min
  ...      875,000/12,389,268 | buf=37,363 (fayette_parcels) | 434/s | ETA 441.9min
  Flushed fayette_parcels: 39,515 | total 877,176 | 426/s | ETA 450.6min
  ...      880,000/12,389,268 | buf=2,848 (features) | 427/s | ETA 448.9min
  ...      885,000/12,389,268 | buf=7,848 (features) | 427/s | ETA 448.9min
  ...      890,000/12,389,268 | buf=12,848 (features) | 427/s | ETA 448.6min
  ...      895,000/12,389,268 | buf=17,848 (features) | 427/s | ETA 448.3min
  ...      900,000/12,389,268 | buf=22,848 (features) | 427/s | ETA 448.0min
  ...      905,000/12,389,268 | buf=27,848 (features) | 428/s | ETA 447.5min
  ...      910,000/12,389,268 | buf=32,848 (features) | 428/s | ETA 447.3min
  ...      915,000/12,389,268 | buf=37,848 (features) | 428/s | ETA 447.0min
  ...      920,000/12,389,268 | buf=42,848 (features) | 428/s | ETA 446.7min
  ...      925,000/12,389,268 | buf=47,848 (features) | 428/s | ETA 446.3min
  ...      930,000/12,389,268 | buf=52,848 (features) | 428/s | ETA 446.0min
  ...      935,000/12,389,268 | buf=57,848 (features) | 428/s | ETA 445.6min
  ...      940,000/12,389,268 | buf=62,848 (features) | 428/s | ETA 445.4min
  ...      945,000/12,389,268 | buf=67,848 (features) | 429/s | ETA 445.0min
  Flushed features: 72,558 | total 949,734 | 405/s | ETA 471.1min
  ...      950,000/12,389,268 | buf=290 (fire_departments) | 405/s | ETA 470.8min
  Flushed fire_departments: 548 | total 950,282 | 403/s | ETA 473.3min
  Flushed fire_dept_wvdem_092017_utm83: 548 | total 950,830 | 403/s | ETA 473.3min
  ...      955,000/12,389,268 | buf=4,194 (floodplainstructuresatrisk_usarmycorpsofengineers_200303_utm83) | 405/s | ETA 471.0min
  ...      960,000/12,389,268 | buf=9,194 (floodplainstructuresatrisk_usarmycorpsofengineers_200303_utm83) | 405/s | ETA 470.7min
  ...      965,000/12,389,268 | buf=14,194 (floodplainstructuresatrisk_usarmycorpsofengineers_200303_utm83) | 404/s | ETA 471.1min
  ...      970,000/12,389,268 | buf=19,194 (floodplainstructuresatrisk_usarmycorpsofengineers_200303_utm83) | 404/s | ETA 470.8min
  ...      975,000/12,389,268 | buf=24,194 (floodplainstructuresatrisk_usarmycorpsofengineers_200303_utm83) | 404/s | ETA 470.4min
  ...      980,000/12,389,268 | buf=29,194 (floodplainstructuresatrisk_usarmycorpsofengineers_200303_utm83) | 405/s | ETA 470.0min
  ...      985,000/12,389,268 | buf=34,194 (floodplainstructuresatrisk_usarmycorpsofengineers_200303_utm83) | 405/s | ETA 469.8min
  ...      990,000/12,389,268 | buf=39,194 (floodplainstructuresatrisk_usarmycorpsofengineers_200303_utm83) | 405/s | ETA 469.5min
  ...      995,000/12,389,268 | buf=44,194 (floodplainstructuresatrisk_usarmycorpsofengineers_200303_utm83) | 405/s | ETA 469.2min
  ...    1,000,000/12,389,268 | buf=49,194 (floodplainstructuresatrisk_usarmycorpsofengineers_200303_utm83) | 405/s | ETA 468.9min
  ...    1,005,000/12,389,268 | buf=54,194 (floodplainstructuresatrisk_usarmycorpsofengineers_200303_utm83) | 405/s | ETA 468.5min
  ...    1,010,000/12,389,268 | buf=59,194 (floodplainstructuresatrisk_usarmycorpsofengineers_200303_utm83) | 405/s | ETA 468.2min
  ...    1,015,000/12,389,268 | buf=64,194 (floodplainstructuresatrisk_usarmycorpsofengineers_200303_utm83) | 405/s | ETA 468.0min
  ...    1,020,000/12,389,268 | buf=69,194 (floodplainstructuresatrisk_usarmycorpsofengineers_200303_utm83) | 405/s | ETA 467.8min
  ...    1,025,000/12,389,268 | buf=74,194 (floodplainstructuresatrisk_usarmycorpsofengineers_200303_utm83) | 405/s | ETA 467.6min
  ...    1,030,000/12,389,268 | buf=79,194 (floodplainstructuresatrisk_usarmycorpsofengineers_200303_utm83) | 405/s | ETA 467.4min
  Flushed floodplainstructuresatrisk_usarmycorpsofengineers_200303_utm83: 81,054 | total 1,031,884 | 386/s | ETA 490.2min
  Flushed founder_tokens: 1 | total 1,031,885 | 386/s | ETA 490.3min
  ...    1,035,000/12,389,268 | buf=3,139 (gbim_entities) | 387/s | ETA 488.6min
  ...    1,040,000/12,389,268 | buf=8,139 (gbim_entities) | 387/s | ETA 488.3min
  ...    1,045,000/12,389,268 | buf=13,139 (gbim_entities) | 387/s | ETA 488.1min
  ...    1,050,000/12,389,268 | buf=18,139 (gbim_entities) | 387/s | ETA 488.4min
  ...    1,055,000/12,389,268 | buf=23,139 (gbim_entities) | 387/s | ETA 488.2min
  ...    1,060,000/12,389,268 | buf=28,139 (gbim_entities) | 387/s | ETA 487.9min
  ...    1,065,000/12,389,268 | buf=33,139 (gbim_entities) | 387/s | ETA 487.6min
  ...    1,070,000/12,389,268 | buf=38,139 (gbim_entities) | 387/s | ETA 487.3min
  ...    1,075,000/12,389,268 | buf=43,139 (gbim_entities) | 387/s | ETA 487.1min
  ...    1,080,000/12,389,268 | buf=48,139 (gbim_entities) | 387/s | ETA 487.0min
  ...    1,085,000/12,389,268 | buf=53,139 (gbim_entities) | 387/s | ETA 487.0min
  ...    1,090,000/12,389,268 | buf=58,139 (gbim_entities) | 387/s | ETA 486.9min
  ...    1,095,000/12,389,268 | buf=63,139 (gbim_entities) | 387/s | ETA 486.8min
  ...    1,100,000/12,389,268 | buf=68,139 (gbim_entities) | 387/s | ETA 486.5min
  ...    1,105,000/12,389,268 | buf=73,139 (gbim_entities) | 387/s | ETA 486.2min
  ...    1,110,000/12,389,268 | buf=78,139 (gbim_entities) | 387/s | ETA 485.9min
  ...    1,115,000/12,389,268 | buf=83,139 (gbim_entities) | 387/s | ETA 485.8min
  ...    1,120,000/12,389,268 | buf=88,139 (gbim_entities) | 387/s | ETA 485.6min
  ...    1,125,000/12,389,268 | buf=93,139 (gbim_entities) | 387/s | ETA 485.4min
  ...    1,130,000/12,389,268 | buf=98,139 (gbim_entities) | 387/s | ETA 485.2min
  ...    1,135,000/12,389,268 | buf=3,139 (gbim_entities) | 353/s | ETA 531.3min
  ...    1,140,000/12,389,268 | buf=8,139 (gbim_entities) | 353/s | ETA 530.8min
  ...    1,145,000/12,389,268 | buf=13,139 (gbim_entities) | 353/s | ETA 530.4min
  ...    1,150,000/12,389,268 | buf=18,139 (gbim_entities) | 353/s | ETA 530.0min
  ...    1,155,000/12,389,268 | buf=23,139 (gbim_entities) | 354/s | ETA 529.6min
  ...    1,160,000/12,389,268 | buf=28,139 (gbim_entities) | 354/s | ETA 529.2min
  ...    1,165,000/12,389,268 | buf=33,139 (gbim_entities) | 354/s | ETA 528.8min
  ...    1,170,000/12,389,268 | buf=38,139 (gbim_entities) | 354/s | ETA 528.5min
  ...    1,175,000/12,389,268 | buf=43,139 (gbim_entities) | 354/s | ETA 528.2min
  ...    1,180,000/12,389,268 | buf=48,139 (gbim_entities) | 354/s | ETA 527.8min
  ...    1,185,000/12,389,268 | buf=53,139 (gbim_entities) | 354/s | ETA 527.9min
  ...    1,190,000/12,389,268 | buf=58,139 (gbim_entities) | 354/s | ETA 527.7min
  ...    1,195,000/12,389,268 | buf=63,139 (gbim_entities) | 354/s | ETA 527.4min
  ...    1,200,000/12,389,268 | buf=68,139 (gbim_entities) | 354/s | ETA 527.1min
  ...    1,205,000/12,389,268 | buf=73,139 (gbim_entities) | 354/s | ETA 526.8min
  ...    1,210,000/12,389,268 | buf=78,139 (gbim_entities) | 354/s | ETA 526.4min
  ...    1,215,000/12,389,268 | buf=83,139 (gbim_entities) | 354/s | ETA 526.0min
  ...    1,220,000/12,389,268 | buf=88,139 (gbim_entities) | 354/s | ETA 525.6min
  ...    1,225,000/12,389,268 | buf=93,139 (gbim_entities) | 354/s | ETA 525.4min
  ...    1,230,000/12,389,268 | buf=98,139 (gbim_entities) | 354/s | ETA 525.1min
  ...    1,235,000/12,389,268 | buf=3,139 (gbim_entities) | 320/s | ETA 580.2min
  ...    1,240,000/12,389,268 | buf=8,139 (gbim_entities) | 321/s | ETA 579.7min
  ...    1,245,000/12,389,268 | buf=13,139 (gbim_entities) | 321/s | ETA 579.3min
  ...    1,250,000/12,389,268 | buf=18,139 (gbim_entities) | 321/s | ETA 578.8min
  ...    1,255,000/12,389,268 | buf=23,139 (gbim_entities) | 321/s | ETA 578.7min
  ...    1,260,000/12,389,268 | buf=28,139 (gbim_entities) | 321/s | ETA 578.3min
  ...    1,265,000/12,389,268 | buf=33,139 (gbim_entities) | 321/s | ETA 577.8min
  ...    1,270,000/12,389,268 | buf=38,139 (gbim_entities) | 321/s | ETA 577.4min
  ...    1,275,000/12,389,268 | buf=43,139 (gbim_entities) | 321/s | ETA 577.0min
  ...    1,280,000/12,389,268 | buf=48,139 (gbim_entities) | 321/s | ETA 576.6min
  ...    1,285,000/12,389,268 | buf=53,139 (gbim_entities) | 321/s | ETA 576.5min
  ...    1,290,000/12,389,268 | buf=58,139 (gbim_entities) | 321/s | ETA 576.1min
  ...    1,295,000/12,389,268 | buf=63,139 (gbim_entities) | 321/s | ETA 575.6min
  ...    1,300,000/12,389,268 | buf=68,139 (gbim_entities) | 321/s | ETA 575.2min
  ...    1,305,000/12,389,268 | buf=73,139 (gbim_entities) | 321/s | ETA 574.7min
  ...    1,310,000/12,389,268 | buf=78,139 (gbim_entities) | 322/s | ETA 574.3min
  ...    1,315,000/12,389,268 | buf=83,139 (gbim_entities) | 322/s | ETA 573.9min
  ...    1,320,000/12,389,268 | buf=88,139 (gbim_entities) | 322/s | ETA 573.5min
  ...    1,325,000/12,389,268 | buf=93,139 (gbim_entities) | 322/s | ETA 573.1min
  ...    1,330,000/12,389,268 | buf=98,139 (gbim_entities) | 322/s | ETA 572.8min
  ...    1,335,000/12,389,268 | buf=3,139 (gbim_entities) | 289/s | ETA 637.0min
  ...    1,340,000/12,389,268 | buf=8,139 (gbim_entities) | 288/s | ETA 640.3min
  ...    1,345,000/12,389,268 | buf=13,139 (gbim_entities) | 288/s | ETA 640.1min
  ...    1,350,000/12,389,268 | buf=18,139 (gbim_entities) | 288/s | ETA 639.4min
  ...    1,355,000/12,389,268 | buf=23,139 (gbim_entities) | 288/s | ETA 638.7min
  ...    1,360,000/12,389,268 | buf=28,139 (gbim_entities) | 288/s | ETA 638.1min
  ...    1,365,000/12,389,268 | buf=33,139 (gbim_entities) | 288/s | ETA 637.5min
  ...    1,370,000/12,389,268 | buf=38,139 (gbim_entities) | 288/s | ETA 636.9min
  ...    1,375,000/12,389,268 | buf=43,139 (gbim_entities) | 288/s | ETA 636.3min
  ...    1,380,000/12,389,268 | buf=48,139 (gbim_entities) | 289/s | ETA 635.7min
  ...    1,385,000/12,389,268 | buf=53,139 (gbim_entities) | 289/s | ETA 635.1min
  ...    1,390,000/12,389,268 | buf=58,139 (gbim_entities) | 289/s | ETA 634.6min
  ...    1,395,000/12,389,268 | buf=63,139 (gbim_entities) | 289/s | ETA 634.0min
  ...    1,400,000/12,389,268 | buf=68,139 (gbim_entities) | 289/s | ETA 633.4min
  ...    1,405,000/12,389,268 | buf=73,139 (gbim_entities) | 289/s | ETA 632.8min
  ...    1,410,000/12,389,268 | buf=78,139 (gbim_entities) | 289/s | ETA 632.2min
  ...    1,415,000/12,389,268 | buf=83,139 (gbim_entities) | 290/s | ETA 631.7min
  ...    1,420,000/12,389,268 | buf=88,139 (gbim_entities) | 290/s | ETA 631.2min
  ...    1,425,000/12,389,268 | buf=93,139 (gbim_entities) | 290/s | ETA 630.7min
  ...    1,430,000/12,389,268 | buf=98,139 (gbim_entities) | 290/s | ETA 630.1min
  ...    1,435,000/12,389,268 | buf=3,139 (gbim_entities) | 276/s | ETA 661.4min
  ...    1,440,000/12,389,268 | buf=8,139 (gbim_entities) | 276/s | ETA 660.8min
  ...    1,445,000/12,389,268 | buf=13,139 (gbim_entities) | 276/s | ETA 660.1min
  ...    1,450,000/12,389,268 | buf=18,139 (gbim_entities) | 276/s | ETA 659.5min
  ...    1,455,000/12,389,268 | buf=23,139 (gbim_entities) | 277/s | ETA 658.9min
  ...    1,460,000/12,389,268 | buf=28,139 (gbim_entities) | 277/s | ETA 658.4min
  ...    1,465,000/12,389,268 | buf=33,139 (gbim_entities) | 277/s | ETA 657.8min
  ...    1,470,000/12,389,268 | buf=38,139 (gbim_entities) | 277/s | ETA 657.5min
  ...    1,475,000/12,389,268 | buf=43,139 (gbim_entities) | 277/s | ETA 657.1min
  ...    1,480,000/12,389,268 | buf=48,139 (gbim_entities) | 277/s | ETA 656.6min
  ...    1,485,000/12,389,268 | buf=53,139 (gbim_entities) | 277/s | ETA 656.1min
  ...    1,490,000/12,389,268 | buf=58,139 (gbim_entities) | 277/s | ETA 655.5min
  ...    1,495,000/12,389,268 | buf=63,139 (gbim_entities) | 277/s | ETA 655.1min
  ...    1,500,000/12,389,268 | buf=68,139 (gbim_entities) | 277/s | ETA 654.6min
  ...    1,505,000/12,389,268 | buf=73,139 (gbim_entities) | 277/s | ETA 654.1min
  ...    1,510,000/12,389,268 | buf=78,139 (gbim_entities) | 277/s | ETA 653.5min
  ...    1,515,000/12,389,268 | buf=83,139 (gbim_entities) | 278/s | ETA 653.0min
  ...    1,520,000/12,389,268 | buf=88,139 (gbim_entities) | 278/s | ETA 652.5min
  ...    1,525,000/12,389,268 | buf=93,139 (gbim_entities) | 278/s | ETA 651.9min
  ...    1,530,000/12,389,268 | buf=98,139 (gbim_entities) | 278/s | ETA 651.6min
  ...    1,535,000/12,389,268 | buf=3,139 (gbim_entities) | 265/s | ETA 683.2min
  ...    1,540,000/12,389,268 | buf=8,139 (gbim_entities) | 265/s | ETA 682.7min
  ...    1,545,000/12,389,268 | buf=13,139 (gbim_entities) | 265/s | ETA 682.2min
  ...    1,550,000/12,389,268 | buf=18,139 (gbim_entities) | 265/s | ETA 681.7min
  ...    1,555,000/12,389,268 | buf=23,139 (gbim_entities) | 265/s | ETA 681.2min
  ...    1,560,000/12,389,268 | buf=28,139 (gbim_entities) | 265/s | ETA 680.7min
  ...    1,565,000/12,389,268 | buf=33,139 (gbim_entities) | 265/s | ETA 680.1min
  ...    1,570,000/12,389,268 | buf=38,139 (gbim_entities) | 265/s | ETA 679.5min
  ...    1,575,000/12,389,268 | buf=43,139 (gbim_entities) | 265/s | ETA 679.1min
  ...    1,580,000/12,389,268 | buf=48,139 (gbim_entities) | 265/s | ETA 678.7min
  ...    1,585,000/12,389,268 | buf=53,139 (gbim_entities) | 265/s | ETA 678.4min
  ...    1,590,000/12,389,268 | buf=58,139 (gbim_entities) | 266/s | ETA 677.9min
  ...    1,595,000/12,389,268 | buf=63,139 (gbim_entities) | 266/s | ETA 677.4min
  ...    1,600,000/12,389,268 | buf=68,139 (gbim_entities) | 266/s | ETA 676.9min
  ...    1,605,000/12,389,268 | buf=73,139 (gbim_entities) | 266/s | ETA 676.4min
  ...    1,610,000/12,389,268 | buf=78,139 (gbim_entities) | 266/s | ETA 675.9min
  ...    1,615,000/12,389,268 | buf=83,139 (gbim_entities) | 266/s | ETA 675.5min
  ...    1,620,000/12,389,268 | buf=88,139 (gbim_entities) | 266/s | ETA 675.0min
  ...    1,625,000/12,389,268 | buf=93,139 (gbim_entities) | 266/s | ETA 674.5min
  ...    1,630,000/12,389,268 | buf=98,139 (gbim_entities) | 266/s | ETA 674.1min
  ...    1,635,000/12,389,268 | buf=3,139 (gbim_entities) | 255/s | ETA 702.5min
  ...    1,640,000/12,389,268 | buf=8,139 (gbim_entities) | 255/s | ETA 702.0min
  ...    1,645,000/12,389,268 | buf=13,139 (gbim_entities) | 255/s | ETA 701.5min
  ...    1,650,000/12,389,268 | buf=18,139 (gbim_entities) | 255/s | ETA 701.0min
  ...    1,655,000/12,389,268 | buf=23,139 (gbim_entities) | 255/s | ETA 700.4min
  ...    1,660,000/12,389,268 | buf=28,139 (gbim_entities) | 256/s | ETA 699.8min
  ...    1,665,000/12,389,268 | buf=33,139 (gbim_entities) | 256/s | ETA 699.4min
  ...    1,670,000/12,389,268 | buf=38,139 (gbim_entities) | 256/s | ETA 698.9min
  ...    1,675,000/12,389,268 | buf=43,139 (gbim_entities) | 256/s | ETA 698.4min
  ...    1,680,000/12,389,268 | buf=48,139 (gbim_entities) | 256/s | ETA 697.9min
  ...    1,685,000/12,389,268 | buf=53,139 (gbim_entities) | 256/s | ETA 697.4min
  ...    1,690,000/12,389,268 | buf=58,139 (gbim_entities) | 256/s | ETA 697.3min
  ...    1,695,000/12,389,268 | buf=63,139 (gbim_entities) | 256/s | ETA 696.8min
  ...    1,700,000/12,389,268 | buf=68,139 (gbim_entities) | 256/s | ETA 696.4min
  ...    1,705,000/12,389,268 | buf=73,139 (gbim_entities) | 256/s | ETA 695.9min
  ...    1,710,000/12,389,268 | buf=78,139 (gbim_entities) | 256/s | ETA 695.5min
  ...    1,715,000/12,389,268 | buf=83,139 (gbim_entities) | 256/s | ETA 695.1min
  ...    1,720,000/12,389,268 | buf=88,139 (gbim_entities) | 256/s | ETA 694.6min
  ...    1,725,000/12,389,268 | buf=93,139 (gbim_entities) | 256/s | ETA 694.1min
  ...    1,730,000/12,389,268 | buf=98,139 (gbim_entities) | 256/s | ETA 693.6min
  ...    1,735,000/12,389,268 | buf=3,139 (gbim_entities) | 244/s | ETA 726.3min
  ...    1,740,000/12,389,268 | buf=8,139 (gbim_entities) | 244/s | ETA 727.7min
  ...    1,745,000/12,389,268 | buf=13,139 (gbim_entities) | 244/s | ETA 727.8min
  ...    1,750,000/12,389,268 | buf=18,139 (gbim_entities) | 244/s | ETA 727.2min
  ...    1,755,000/12,389,268 | buf=23,139 (gbim_entities) | 244/s | ETA 726.7min
  ...    1,760,000/12,389,268 | buf=28,139 (gbim_entities) | 244/s | ETA 726.2min
  ...    1,765,000/12,389,268 | buf=33,139 (gbim_entities) | 244/s | ETA 725.8min
  ...    1,770,000/12,389,268 | buf=38,139 (gbim_entities) | 244/s | ETA 725.4min
  ...    1,775,000/12,389,268 | buf=43,139 (gbim_entities) | 244/s | ETA 725.0min
  ...    1,780,000/12,389,268 | buf=48,139 (gbim_entities) | 244/s | ETA 724.5min
  ...    1,785,000/12,389,268 | buf=53,139 (gbim_entities) | 244/s | ETA 724.0min
  ...    1,790,000/12,389,268 | buf=58,139 (gbim_entities) | 244/s | ETA 723.4min
  ...    1,795,000/12,389,268 | buf=63,139 (gbim_entities) | 244/s | ETA 723.1min
  ...    1,800,000/12,389,268 | buf=68,139 (gbim_entities) | 244/s | ETA 722.6min
  ...    1,805,000/12,389,268 | buf=73,139 (gbim_entities) | 244/s | ETA 722.2min
  ...    1,810,000/12,389,268 | buf=78,139 (gbim_entities) | 244/s | ETA 721.7min
  ...    1,815,000/12,389,268 | buf=83,139 (gbim_entities) | 244/s | ETA 721.2min
  ...    1,820,000/12,389,268 | buf=88,139 (gbim_entities) | 244/s | ETA 720.8min
  ...    1,825,000/12,389,268 | buf=93,139 (gbim_entities) | 244/s | ETA 720.4min
  ...    1,830,000/12,389,268 | buf=98,139 (gbim_entities) | 244/s | ETA 719.9min
  ...    1,835,000/12,389,268 | buf=3,139 (gbim_entities) | 236/s | ETA 746.1min
  ...    1,840,000/12,389,268 | buf=8,139 (gbim_entities) | 236/s | ETA 745.6min
  ...    1,845,000/12,389,268 | buf=13,139 (gbim_entities) | 236/s | ETA 745.2min
  ...    1,850,000/12,389,268 | buf=18,139 (gbim_entities) | 236/s | ETA 744.6min
  ...    1,855,000/12,389,268 | buf=23,139 (gbim_entities) | 236/s | ETA 744.1min
  ...    1,860,000/12,389,268 | buf=28,139 (gbim_entities) | 236/s | ETA 743.7min
  ...    1,865,000/12,389,268 | buf=33,139 (gbim_entities) | 236/s | ETA 743.4min
  ...    1,870,000/12,389,268 | buf=38,139 (gbim_entities) | 236/s | ETA 742.9min
  ...    1,875,000/12,389,268 | buf=43,139 (gbim_entities) | 236/s | ETA 742.4min
  ...    1,880,000/12,389,268 | buf=48,139 (gbim_entities) | 236/s | ETA 741.9min
  ...    1,885,000/12,389,268 | buf=53,139 (gbim_entities) | 236/s | ETA 741.5min
  ...    1,890,000/12,389,268 | buf=58,139 (gbim_entities) | 236/s | ETA 740.9min
  ...    1,895,000/12,389,268 | buf=63,139 (gbim_entities) | 236/s | ETA 740.5min
  ...    1,900,000/12,389,268 | buf=68,139 (gbim_entities) | 236/s | ETA 740.0min
  ...    1,905,000/12,389,268 | buf=73,139 (gbim_entities) | 236/s | ETA 739.5min
  ...    1,910,000/12,389,268 | buf=78,139 (gbim_entities) | 236/s | ETA 739.0min
  ...    1,915,000/12,389,268 | buf=83,139 (gbim_entities) | 236/s | ETA 738.6min
  ...    1,920,000/12,389,268 | buf=88,139 (gbim_entities) | 236/s | ETA 738.2min
  ...    1,925,000/12,389,268 | buf=93,139 (gbim_entities) | 236/s | ETA 737.7min
  ...    1,930,000/12,389,268 | buf=98,139 (gbim_entities) | 236/s | ETA 737.2min
  ...    1,935,000/12,389,268 | buf=3,139 (gbim_entities) | 228/s | ETA 764.1min
  ...    1,940,000/12,389,268 | buf=8,139 (gbim_entities) | 227/s | ETA 766.7min
  ...    1,945,000/12,389,268 | buf=13,139 (gbim_entities) | 227/s | ETA 766.3min
  ...    1,950,000/12,389,268 | buf=18,139 (gbim_entities) | 227/s | ETA 765.8min
  ...    1,955,000/12,389,268 | buf=23,139 (gbim_entities) | 227/s | ETA 765.2min
  ...    1,960,000/12,389,268 | buf=28,139 (gbim_entities) | 227/s | ETA 764.7min
  ...    1,965,000/12,389,268 | buf=33,139 (gbim_entities) | 227/s | ETA 764.2min
  ...    1,970,000/12,389,268 | buf=38,139 (gbim_entities) | 227/s | ETA 763.7min
  ...    1,975,000/12,389,268 | buf=43,139 (gbim_entities) | 227/s | ETA 763.2min
  ...    1,980,000/12,389,268 | buf=48,139 (gbim_entities) | 228/s | ETA 762.6min
  ...    1,985,000/12,389,268 | buf=53,139 (gbim_entities) | 228/s | ETA 762.0min
  ...    1,990,000/12,389,268 | buf=58,139 (gbim_entities) | 228/s | ETA 761.5min
  ...    1,995,000/12,389,268 | buf=63,139 (gbim_entities) | 228/s | ETA 761.0min
  ...    2,000,000/12,389,268 | buf=68,139 (gbim_entities) | 228/s | ETA 760.5min
  ...    2,005,000/12,389,268 | buf=73,139 (gbim_entities) | 228/s | ETA 760.0min
  ...    2,010,000/12,389,268 | buf=78,139 (gbim_entities) | 228/s | ETA 759.5min
  ...    2,015,000/12,389,268 | buf=83,139 (gbim_entities) | 228/s | ETA 759.0min
  ...    2,020,000/12,389,268 | buf=88,139 (gbim_entities) | 228/s | ETA 758.5min
  ...    2,025,000/12,389,268 | buf=93,139 (gbim_entities) | 228/s | ETA 758.3min
  ...    2,030,000/12,389,268 | buf=98,139 (gbim_entities) | 228/s | ETA 757.8min
  ...    2,035,000/12,389,268 | buf=3,139 (gbim_entities) | 221/s | ETA 781.1min
  ...    2,040,000/12,389,268 | buf=8,139 (gbim_entities) | 221/s | ETA 780.7min
  ...    2,045,000/12,389,268 | buf=13,139 (gbim_entities) | 221/s | ETA 780.3min
  ...    2,050,000/12,389,268 | buf=18,139 (gbim_entities) | 221/s | ETA 779.8min
  ...    2,055,000/12,389,268 | buf=23,139 (gbim_entities) | 221/s | ETA 779.3min
  ...    2,060,000/12,389,268 | buf=28,139 (gbim_entities) | 221/s | ETA 778.8min
  ...    2,065,000/12,389,268 | buf=33,139 (gbim_entities) | 221/s | ETA 778.2min
  ...    2,070,000/12,389,268 | buf=38,139 (gbim_entities) | 221/s | ETA 777.7min
  ...    2,075,000/12,389,268 | buf=43,139 (gbim_entities) | 221/s | ETA 777.2min
  ...    2,080,000/12,389,268 | buf=48,139 (gbim_entities) | 221/s | ETA 776.7min
  ...    2,085,000/12,389,268 | buf=53,139 (gbim_entities) | 221/s | ETA 776.2min
  ...    2,090,000/12,389,268 | buf=58,139 (gbim_entities) | 221/s | ETA 775.6min
  ...    2,095,000/12,389,268 | buf=63,139 (gbim_entities) | 221/s | ETA 775.2min
  ...    2,100,000/12,389,268 | buf=68,139 (gbim_entities) | 221/s | ETA 774.8min
  ...    2,105,000/12,389,268 | buf=73,139 (gbim_entities) | 221/s | ETA 774.3min
  ...    2,110,000/12,389,268 | buf=78,139 (gbim_entities) | 221/s | ETA 774.2min
  ...    2,115,000/12,389,268 | buf=83,139 (gbim_entities) | 221/s | ETA 773.7min
  ...    2,120,000/12,389,268 | buf=88,139 (gbim_entities) | 221/s | ETA 773.3min
  ...    2,125,000/12,389,268 | buf=93,139 (gbim_entities) | 221/s | ETA 772.8min
  ...    2,130,000/12,389,268 | buf=98,139 (gbim_entities) | 221/s | ETA 772.3min
  ...    2,135,000/12,389,268 | buf=3,139 (gbim_entities) | 215/s | ETA 794.9min
  ...    2,140,000/12,389,268 | buf=8,139 (gbim_entities) | 214/s | ETA 797.1min
  ...    2,145,000/12,389,268 | buf=13,139 (gbim_entities) | 214/s | ETA 796.6min
  ...    2,150,000/12,389,268 | buf=18,139 (gbim_entities) | 214/s | ETA 796.1min
  ...    2,155,000/12,389,268 | buf=23,139 (gbim_entities) | 214/s | ETA 795.6min
  ...    2,160,000/12,389,268 | buf=28,139 (gbim_entities) | 214/s | ETA 795.0min
  ...    2,165,000/12,389,268 | buf=33,139 (gbim_entities) | 215/s | ETA 794.4min
  ...    2,170,000/12,389,268 | buf=38,139 (gbim_entities) | 215/s | ETA 793.9min
  ...    2,175,000/12,389,268 | buf=43,139 (gbim_entities) | 215/s | ETA 793.3min
  ...    2,180,000/12,389,268 | buf=48,139 (gbim_entities) | 215/s | ETA 792.7min
  ...    2,185,000/12,389,268 | buf=53,139 (gbim_entities) | 215/s | ETA 792.4min
  ...    2,190,000/12,389,268 | buf=58,139 (gbim_entities) | 215/s | ETA 791.9min
  ...    2,195,000/12,389,268 | buf=63,139 (gbim_entities) | 215/s | ETA 791.3min
  ...    2,200,000/12,389,268 | buf=68,139 (gbim_entities) | 215/s | ETA 790.7min
  ...    2,205,000/12,389,268 | buf=73,139 (gbim_entities) | 215/s | ETA 790.2min
  ...    2,210,000/12,389,268 | buf=78,139 (gbim_entities) | 215/s | ETA 789.7min
  ...    2,215,000/12,389,268 | buf=83,139 (gbim_entities) | 215/s | ETA 789.1min
  ...    2,220,000/12,389,268 | buf=88,139 (gbim_entities) | 215/s | ETA 788.6min
  ...    2,225,000/12,389,268 | buf=93,139 (gbim_entities) | 215/s | ETA 788.1min
  ...    2,230,000/12,389,268 | buf=98,139 (gbim_entities) | 215/s | ETA 787.6min
  ...    2,235,000/12,389,268 | buf=3,139 (gbim_entities) | 209/s | ETA 809.3min
  ...    2,240,000/12,389,268 | buf=8,139 (gbim_entities) | 209/s | ETA 808.9min
  ...    2,245,000/12,389,268 | buf=13,139 (gbim_entities) | 209/s | ETA 808.3min
  ...    2,250,000/12,389,268 | buf=18,139 (gbim_entities) | 209/s | ETA 807.7min
  ...    2,255,000/12,389,268 | buf=23,139 (gbim_entities) | 209/s | ETA 807.2min
  ...    2,260,000/12,389,268 | buf=28,139 (gbim_entities) | 209/s | ETA 806.6min
  ...    2,265,000/12,389,268 | buf=33,139 (gbim_entities) | 209/s | ETA 806.0min
  ...    2,270,000/12,389,268 | buf=38,139 (gbim_entities) | 209/s | ETA 805.8min
  ...    2,275,000/12,389,268 | buf=43,139 (gbim_entities) | 209/s | ETA 805.2min
  ...    2,280,000/12,389,268 | buf=48,139 (gbim_entities) | 209/s | ETA 804.7min
  ...    2,285,000/12,389,268 | buf=53,139 (gbim_entities) | 209/s | ETA 804.1min
  ...    2,290,000/12,389,268 | buf=58,139 (gbim_entities) | 209/s | ETA 803.5min
  ...    2,295,000/12,389,268 | buf=63,139 (gbim_entities) | 210/s | ETA 802.9min
  ...    2,300,000/12,389,268 | buf=68,139 (gbim_entities) | 210/s | ETA 802.3min
  ...    2,305,000/12,389,268 | buf=73,139 (gbim_entities) | 210/s | ETA 801.8min
  ...    2,310,000/12,389,268 | buf=78,139 (gbim_entities) | 210/s | ETA 801.2min
  ...    2,315,000/12,389,268 | buf=83,139 (gbim_entities) | 210/s | ETA 800.6min
  ...    2,320,000/12,389,268 | buf=88,139 (gbim_entities) | 210/s | ETA 800.1min
  ...    2,325,000/12,389,268 | buf=93,139 (gbim_entities) | 210/s | ETA 799.5min
  ...    2,330,000/12,389,268 | buf=98,139 (gbim_entities) | 210/s | ETA 799.0min
  ...    2,335,000/12,389,268 | buf=3,139 (gbim_entities) | 203/s | ETA 825.3min
  ...    2,340,000/12,389,268 | buf=8,139 (gbim_entities) | 202/s | ETA 827.3min
  ...    2,345,000/12,389,268 | buf=13,139 (gbim_entities) | 202/s | ETA 826.8min
  ...    2,350,000/12,389,268 | buf=18,139 (gbim_entities) | 202/s | ETA 826.3min
  ...    2,355,000/12,389,268 | buf=23,139 (gbim_entities) | 203/s | ETA 825.8min
  ...    2,360,000/12,389,268 | buf=28,139 (gbim_entities) | 203/s | ETA 825.2min
  ...    2,365,000/12,389,268 | buf=33,139 (gbim_entities) | 203/s | ETA 824.7min
  ...    2,370,000/12,389,268 | buf=38,139 (gbim_entities) | 203/s | ETA 824.2min
  ...    2,375,000/12,389,268 | buf=43,139 (gbim_entities) | 203/s | ETA 823.7min
  ...    2,380,000/12,389,268 | buf=48,139 (gbim_entities) | 203/s | ETA 823.2min
  ...    2,385,000/12,389,268 | buf=53,139 (gbim_entities) | 203/s | ETA 822.6min
  ...    2,390,000/12,389,268 | buf=58,139 (gbim_entities) | 203/s | ETA 822.3min
  ...    2,395,000/12,389,268 | buf=63,139 (gbim_entities) | 203/s | ETA 821.8min
  ...    2,400,000/12,389,268 | buf=68,139 (gbim_entities) | 203/s | ETA 821.3min
  ...    2,405,000/12,389,268 | buf=73,139 (gbim_entities) | 203/s | ETA 820.8min
  ...    2,410,000/12,389,268 | buf=78,139 (gbim_entities) | 203/s | ETA 820.2min
  ...    2,415,000/12,389,268 | buf=83,139 (gbim_entities) | 203/s | ETA 819.8min
  ...    2,420,000/12,389,268 | buf=88,139 (gbim_entities) | 203/s | ETA 819.4min
  ...    2,425,000/12,389,268 | buf=93,139 (gbim_entities) | 203/s | ETA 818.9min
  ...    2,430,000/12,389,268 | buf=98,139 (gbim_entities) | 203/s | ETA 818.5min
  ...    2,435,000/12,389,268 | buf=3,139 (gbim_entities) | 198/s | ETA 839.1min
  ...    2,440,000/12,389,268 | buf=8,139 (gbim_entities) | 197/s | ETA 841.2min
  ...    2,445,000/12,389,268 | buf=13,139 (gbim_entities) | 197/s | ETA 842.4min
  ...    2,450,000/12,389,268 | buf=18,139 (gbim_entities) | 197/s | ETA 842.0min
  ...    2,455,000/12,389,268 | buf=23,139 (gbim_entities) | 197/s | ETA 842.0min
  ...    2,460,000/12,389,268 | buf=28,139 (gbim_entities) | 197/s | ETA 841.5min
  ...    2,465,000/12,389,268 | buf=33,139 (gbim_entities) | 197/s | ETA 841.2min
  ...    2,470,000/12,389,268 | buf=38,139 (gbim_entities) | 197/s | ETA 840.6min
  ...    2,475,000/12,389,268 | buf=43,139 (gbim_entities) | 197/s | ETA 840.2min
  ...    2,480,000/12,389,268 | buf=48,139 (gbim_entities) | 197/s | ETA 840.4min
  ...    2,485,000/12,389,268 | buf=53,139 (gbim_entities) | 197/s | ETA 839.9min
  ...    2,490,000/12,389,268 | buf=58,139 (gbim_entities) | 197/s | ETA 839.4min
  ...    2,495,000/12,389,268 | buf=63,139 (gbim_entities) | 197/s | ETA 839.0min
  ...    2,500,000/12,389,268 | buf=68,139 (gbim_entities) | 197/s | ETA 838.5min
  ...    2,505,000/12,389,268 | buf=73,139 (gbim_entities) | 197/s | ETA 838.0min
  ...    2,510,000/12,389,268 | buf=78,139 (gbim_entities) | 197/s | ETA 837.8min
  ...    2,515,000/12,389,268 | buf=83,139 (gbim_entities) | 196/s | ETA 837.8min
  ...    2,520,000/12,389,268 | buf=88,139 (gbim_entities) | 196/s | ETA 837.8min
  ...    2,525,000/12,389,268 | buf=93,139 (gbim_entities) | 196/s | ETA 837.7min
  ...    2,530,000/12,389,268 | buf=98,139 (gbim_entities) | 196/s | ETA 837.7min
  ...    2,535,000/12,389,268 | buf=3,139 (gbim_entities) | 191/s | ETA 860.3min
  ...    2,540,000/12,389,268 | buf=8,139 (gbim_entities) | 191/s | ETA 861.2min
  ...    2,545,000/12,389,268 | buf=13,139 (gbim_entities) | 191/s | ETA 860.7min
  ...    2,550,000/12,389,268 | buf=18,139 (gbim_entities) | 191/s | ETA 860.2min
  ...    2,555,000/12,389,268 | buf=23,139 (gbim_entities) | 191/s | ETA 860.0min
  ...    2,560,000/12,389,268 | buf=28,139 (gbim_entities) | 191/s | ETA 859.4min
  ...    2,565,000/12,389,268 | buf=33,139 (gbim_entities) | 191/s | ETA 859.1min
  ...    2,570,000/12,389,268 | buf=38,139 (gbim_entities) | 191/s | ETA 858.6min
  ...    2,575,000/12,389,268 | buf=43,139 (gbim_entities) | 191/s | ETA 858.0min
  ...    2,580,000/12,389,268 | buf=48,139 (gbim_entities) | 191/s | ETA 857.5min
  ...    2,585,000/12,389,268 | buf=53,139 (gbim_entities) | 191/s | ETA 857.0min
  ...    2,590,000/12,389,268 | buf=58,139 (gbim_entities) | 191/s | ETA 856.5min
  ...    2,595,000/12,389,268 | buf=63,139 (gbim_entities) | 191/s | ETA 855.9min
  ...    2,600,000/12,389,268 | buf=68,139 (gbim_entities) | 191/s | ETA 855.3min
  ...    2,605,000/12,389,268 | buf=73,139 (gbim_entities) | 191/s | ETA 855.1min
  ...    2,610,000/12,389,268 | buf=78,139 (gbim_entities) | 191/s | ETA 854.6min
  ...    2,615,000/12,389,268 | buf=83,139 (gbim_entities) | 191/s | ETA 854.1min
  ...    2,620,000/12,389,268 | buf=88,139 (gbim_entities) | 191/s | ETA 854.0min
  [READ retry 1] HTTP 500 -> 1s
  [READ retry 2] HTTP 500 -> 2s
  [READ retry 3] HTTP 500 -> 4s
  [READ retry 4] HTTP 500 -> 8s
  [READ retry 5] HTTP 500 -> 16s
  [READ retry 6] HTTP 500 -> 32s
  [READ retry 7] HTTP 500 -> 64s
  [READ retry 8] HTTP 500 -> 128s
Traceback (most recent call last):
  File "/home/cakidd/msjarvis-rebuild/migrate_to_layer_collections_v3.py", line 214, in <module>
    main()
  File "/home/cakidd/msjarvis-rebuild/migrate_to_layer_collections_v3.py", line 153, in main
    batch = retry_post(client, get_url, {
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/cakidd/msjarvis-rebuild/migrate_to_layer_collections_v3.py", line 59, in retry_post
    raise RuntimeError(f"Exhausted retries: {label} {url}")
RuntimeError: Exhausted retries: READ http://localhost:8002/api/v2/tenants/default_tenant/databases/default_database/collections/497a6c83-cbd4-4162-9f61-55e447533557/get
(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~/msjarvis-rebuild$ 

