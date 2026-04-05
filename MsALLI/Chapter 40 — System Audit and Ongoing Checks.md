# Chapter 40 — System Audit and Ongoing Checks

Carrie Kidd (Mamma Kidd) — Mount Hope, WV  
Last updated: April 2, 2026

### 40.1 What This Chapter Covers

This chapter explains how the system is checked and watched over time so it does not slowly drift away from what the rest of the thesis describes. It records what was running as of early April 2026, which machines and ports are in use, and which tests must pass before the system is considered healthy.

By this point, the system is running 96 containers on a single host. Three main databases are in use, a large Chroma memory store is online, and a number of AI and gateway services sit in front of them. This chapter sets out the “ground truth” for those pieces: which port each one uses, what data it holds, and what a healthy response looks like.

The goal is simple: after any change, restart, or repair, you should be able to run a small set of commands and know whether the system is sound or needs attention.

---

### 40.2 Key Corrections and Current Layout

On March 28, 2026, a focused check of the system cleared up several old mistakes and set the current baseline. In plain terms:

- The Chroma memory service listens on port 8002 on the host. Inside the container it still uses port 8000, but any script on the host must talk to 8002. As of that day, it held 40 collections and a little over 6.6 million stored vectors.
- The main belief database (`msjarvis`) uses port 5433. It held more than 5.4 million belief records, each now carrying a “how fresh is this” value so older information can be treated with more caution.
- The geographic database (`gisdb` / `msjarvisgis`) uses port 5432. It held about 91 GB of data, including 993 ZIP‑code centroids and more than 20,000 beliefs about land ownership.
- The local resources database uses port 5435. Its connection details were fixed, and its “resolve” endpoint was confirmed working.
- The Redis cache uses port 6380 on the host, and jobs signal that they are finished by setting their status to the word “complete.”
- The total container count was confirmed as 96. Older references to 83 containers are now out of date. The added containers include the memory audit service, three EEG‑related services, and five governance‑related services.
- The main brain of the system accepts traffic on port 8050. A separate gateway at port 8010 is present but treated as a weaker, backup path.
- The safety gateway (BBB) has six filters active. Its final output step is currently in “log and pass through” mode: it notes questionable cases but does not yet block them. All of its decisions are written to the memory audit service.
- The learning collection is named `autonomous_learner` with an underscore. A similar name without the underscore is now considered obsolete.
- The autonomous learner service listens on port 8020. Any use of port 8425 for that service is wrong and should be corrected.
- The general RAG service listens on port 8003, both inside and outside its container. Earlier references to 8016 for that container are no longer valid.
- The unified gateway at port 18018 has been patched to avoid errors when working with decision dictionaries.
- The land‑owner query service is correctly named `jarvis-gbim-query-router` and uses port 7205.
- All Chroma collections use a 384‑dimension embedding model. Using a different size model would silently break search quality.

This corrected map is the starting point for every test and check described in the rest of the chapter.

---

### 40.3 Why These Checks Matter

This system is not just a toy model. It answers questions about real places, land ownership, benefits, and community resources in West Virginia and nearby regions. It also carries a record of safety decisions and self‑checks meant to protect the people who use it.

For those reasons, it is not enough to say “it worked last month.” This chapter provides a living test plan that can be run again and again. It helps answer questions like:

- Are all the core services still running on the right ports?
- Are the key databases and collections still there and filled?
- Are the gateways still locked down properly?
- Are safety decisions still being written to the audit log?
- Is the main “ask a question” path still going through all of its stages?

If the answer to any of these becomes “no,” this chapter should make it obvious where things went wrong.

---

### 40.4 Overall Health and Watchdog Script

A script called `VERIFYANDTEST.sh` acts as the main health check for the system. It lives in a monitoring directory and is also reachable via a shortcut in the code repository. A clean run of that script, as of March 28, confirms:

- All core services are up.
- Twenty‑one out of twenty‑two model proxies actively contribute to group answers, with one present but not used for community questions.
- Ninety‑six Docker containers are running.
- Twenty‑six models are available in the local model runtime.
- The three main databases accept connections and respond as expected.
- Chroma memory is reachable at port 8002 with the expected number of collections and vectors.
- The consciousness‑related services (WOAH, Chroma, bridge, RAG server, and gateway) all respond to their health checks.
- The safety gateway and audit service are secured and logging as intended.
- The governance‑related services and EEG‑related services are present and running, even if some of their endpoints are not yet fully tested.
- No ports are accidentally exposed to the full internet.
- The system status is reported as “operational.”

The same script also runs a “pre‑flight” section that counts how many checks passed. At the end of March, that number was 24 out of 24. This number is expected to grow as new checks are added.

If any of these are not true in a future run, the script prints clear hints about where to look next: which service is down, which port is wrong, or which collection cannot be found.

---

### 40.5 Service Map in Everyday Terms

The full port map stretches over many lines, but a few anchors help:

- The main “ask a question” route uses port 8050.
- The safety gate uses port 8016.
- The RAG server uses port 8003.
- The Chroma memory service uses port 8002.
- The psychological domain is reached through port 8006.
- The spiritual and belief domain uses port 8005.
- Geographic RAG queries use port 8004.
- The judge services use ports in the 7230–7239 range.
- The land‑owner query router uses port 7205.
- The consciousness‑related services use ports 7012, 8002, 8020, 8003, and 18018.
- The memory audit service uses port 8056.
- The EEG services use ports 8073–8075.
- The governance layer uses ports 8080–8084.
- The crypto policy service uses port 8099.
- The local resources database uses port 5435; the belief and geographic databases use 5433 and 5432.

All of these are bound to the local machine. If any service appears on “0.0.0.0” instead, that is treated as a security issue and must be fixed.

---

### 40.6 The Main Watchdog Script in Use

When a developer or operator wants to know “is everything still okay,” they run the watchdog script. A typical run:

- Prints how many core services are up.
- Confirms the counts of running containers, models, and collections.
- Lists the health of key services like the main brain, RAG, Chroma, and the audit service.
- Checks the most important database tables for presence and rough counts.
- Verifies that no services are listening where they should not.

A clean run is treated as a green light: the system matches the layout described in this chapter and is ready for deeper tests. A run that shows missing services, missing columns, or wrong counts is a red light: further work is needed before trusting it with community‑facing traffic.

---

### 40.7 Basic and Advanced Smoke Tests

Beyond the watchdog, the chapter lays out a set of “smoke tests” that anyone can run from the command line. These are grouped by area:

- The safety gate can be asked for a simple “are you up” check, and can be given a harmless question about local health resources; the expected result is that it passes the question and records the decision.
- The main chat endpoint can be asked a question like “what can you tell me about Mount Hope, West Virginia?” The expected answer should:
  - Be in the assistant’s voice, without revealing its underlying model labels.
  - Show that it went through all the internal layers described elsewhere (judges, safety, memory, and so on).
  - Report a processing time in the expected GPU‑backed range.
- An asynchronous chat path can be used to check that the job queue and Redis storage are working, with job statuses moving from queued to complete.
- The “I‑containers” and psychology services can be probed to ensure they return structured results and not error stubs.
- The psychological memory collection can be tested by asking for entries related to grief and community support and checking that results come back.
- The hippocampus service can be checked to see that it both reads from and writes to memory collections.
- The autonomous learner service can be asked about community resource questions and should return relevant learned entries.

There are also tests for the judge pipeline, governance endpoints, and EEG‑related services. Each one is framed as a small command and a clear expectation: “this should return 200,” “this count should be at least this many,” or “this field should be present in the response.”

---

### 40.8 Database Checks

The chapter specifies a handful of database checks that act as anchors:

- Counting total beliefs in the main belief table, with an expected value around 5.4 million.
- Confirming that the “confidence decay” column exists and has non‑null values.
- Confirming the presence of fields that track when a belief was last checked and whether it needs review.
- Counting the number of ZIP‑code centroids in the geographic database, with an expected count just under a thousand.
- Counting the number of land‑owner beliefs and listing the largest landholding entities.
- Counting verified community resource entries in the local resources database, with an expected minimum number for a specific county.

These checks are simple, but they give a clear signal when something is badly wrong, such as a missing table, an empty column, or a mis‑wired database connection.

---

### 40.9 Regression Test for a Simple Question

As a reference point, the chapter uses a specific question — “What is the capital of West Virginia?” — as a full pipeline test.

For this question:

- The answer should name Charleston.
- The answer should not leak model names or generic “as an AI” disclaimers.
- The judges should give scores above certain thresholds for truth, consistency, alignment, and ethics.
- The reported number of active layers and validating components should meet or exceed defined minimums.
- The safety gate should confirm that it received and checked the full verdict.

This simple question becomes a kind of “heartbeat” for the entire system. If the system cannot answer it properly, something is wrong with the deeper layers.

---

### 40.10 Confidence Decay and Aging Facts

Since older information can become unreliable, the system tracks a “decay” value for belief entries. This chapter includes:

- A check that the decay column exists and is filled for at least some rows.
- A chat‑level test where a question about services in a town returns metadata indicating whether decay was applied and whether any cited beliefs need re‑verification.

There is also an early design for alerting: a separate file outlines how a monitoring system might warn when too many “stale” beliefs are being used. At the time of this writing, that alerting logic is planned but not yet fully active.

---

### 40.11 RAG and Safety Behavior

The chapter walks through tests that:

- Confirm that the RAG server can answer a question about community resources in a county, drawing from Chroma and the local model runtime.
- Confirm that the spiritual/GBIM RAG path and the GIS RAG path can answer basic questions and stay connected to their underlying databases.
- Confirm that the safety gateway allows benign community questions.
- Confirm that the output safety stage logs flagged cases without blocking them while tuning is still underway.
- Confirm that the safety gateway’s “truth” endpoint correctly rejects false statements about the assistant’s identity.

A separate script exists to run a small “red team” test set against the safety gateway. This harness has been created and run once, but the full catalog of adversarial tests and automated schedules for them are still planned future work.

---

### 40.12 Continuous Monitoring and Cron Jobs

The system uses scheduled tasks (cron jobs) to run some of the health checks automatically. As of April 2, 2026:

- A schedule file shows hourly checks for disk, services, databases, and belief materialized views.
- A dedicated script checks the safety gateway regularly (every five minutes).
- The main watchdog script has been restored and is reachable both in the monitoring directory and via a repository shortcut.
- Evidence files record that the watchdog and safety checks have been running in the expected time windows.

At the same time, some nightly tasks — such as automated red‑team runs, consciousness baseline tests, and operation‑history exports — are documented but not yet turned on. That work is reserved for future sprints.

---

### 40.13 Observability and Tracing

An OpenTelemetry collector has been set up and is listening on standard ports, ready to accept traces from the main brain service. The main brain has been updated to initialize a tracer at startup.

However, no actual span data was ingested during the April 1 sprint. For now, ordinary logs and the health scripts remain the main way to monitor performance and latency. The plan is to gradually add more detailed timing information (for example, how long each stage of the pipeline takes), but this is not yet complete.

Separately, a draft alert rule has been created to watch for unusual patterns in the confidence‑decay values. This will eventually help catch cases where too many answers rely on stale information.

---

### 40.14 Extra Test Harnesses

Several smaller harnesses have been built:

- A baseline harness for “WOAH” tests, checking that the consciousness pipeline responds as expected to a small set of questions.
- An export harness that gathers selected operational logs into a format that later can be embedded and stored in a dedicated “operations history” collection.

In both cases, the harnesses exist and have been run at least once. They rely on future work to attach clear pass/fail rules and to hook into automatic runs.

---

### 40.15 Recent Sprint Highlights

In late March and early April, a series of short work periods focused on:

- Moving all key ports and services onto a single, well‑documented map.
- Tightening network exposure so that everything is bound to the local machine or tunneled.
- Restoring and double‑checking key data, including psychological collections, confidence‑decay metadata, and ZIP‑code centroids.
- Expanding the stack to include governance services and EEG‑related processes.
- Securing the memory audit service and proving that safety decisions are being logged.
- Setting up cron jobs, the main watchdog script, a basic red‑team harness, a consciousness baseline harness, and an operations export harness.
- Starting observability work with an OpenTelemetry collector and alert rule sketches.

Some items, such as detailed tracing, full red‑team coverage, and embedding of operations history, are marked as “in progress” rather than fully done, but the foundation for them is now in place.

---

### 40.16 How This Supports the Broader System

This chapter keeps the system honest. It takes many claims scattered across other chapters—about land‑owner maps, benefits tables, cultural collections, psychological domains, safety filters, and governance tools—and pins them down to concrete checks that either pass or fail.

When everything passes, it means the running system in Pax, West Virginia, matches what the thesis describes on paper. When something fails, the mismatch is visible, and the relevant chapter can be updated or the system can be repaired.

In this way, the system is treated less like a one‑off prototype and more like a piece of community infrastructure that must prove, day after day, that it is still doing what it promised to do.
