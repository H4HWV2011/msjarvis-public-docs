# Phase 7: Install Kiosk Hotspot Equipment
## Field Learning Guide — Mount Hope Walking Trail Pilot Site

---

## What This Document Is For

This document expands on Phase 7 of the installation workflow. It explains what the kiosk hotspot equipment is, why it is being installed the way it is, what each step accomplishes, and what the finished installation should look like. Because this is a pilot site, it also captures the thinking behind the decisions made here so that H4H can apply those lessons to future community installations.

---

## What Phase 7 Covers

Phase 7 installs the public-facing hotspot equipment at the existing kiosk structure on the Mount Hope walking trail. This is the point in the installation that the public will actually interact with. Every other phase installs infrastructure that supports this location. This phase makes the service visible and accessible to the people the project is designed to serve.

The equipment installed in this phase:

- Raspberry Pi (installed inside the weatherproof outdoor enclosure)
- MicroSD storage card (loaded into the Raspberry Pi)
- Raspberry Pi power supply (connected to the outdoor power source)
- Short HDMI or display adapter cable (as needed for any diagnostic display use)
- Outdoor weatherproof enclosure (Sixfab IP65 or equivalent)
- Outdoor power cable (Southwire 12/3 SJTW or equivalent)
- Exterior cable glands (for sealed cable entry)
- Wi-Fi hotspot sign (mounted at the kiosk for public visibility)

---

## Before Phase 7 Begins: What Must Already Be True

Phase 7 cannot start until the following conditions from earlier phases are confirmed:

- The existing kiosk structure has been inspected and confirmed structurally sound (Phase 4).
- The solar power system is installed and the charge controller shows the system is live (Phase 6).
- The indoor Starlink internet connection is confirmed active (Phase 5).
- The outdoor power cable path from the power source to the kiosk location has been confirmed clear and safe.

If any of these conditions are not met, stop and report to H4H before proceeding. Installing hotspot equipment at a kiosk that has no power, no internet, or a structural problem creates a finished-looking installation that does not work — and diagnosing it later is harder than catching the dependency now.

---

## The Step Sequence and the Reason for Each Step

### Step 1: Inspect the existing kiosk structure

**Context for this site:** This kiosk has been standing on the Mount Hope walking trail for five years. That is not a reason to skip this inspection — it is the reason the inspection is mandatory. Five years of Fayette County winters, freeze-thaw cycling, summer humidity, UV exposure, and seasonal rainfall is enough time to degrade wood joinery, corrode metal fasteners, soften post bases where they contact soil or concrete, and create surface conditions that look intact from a distance but are not sound enough to carry additional hardware. A structure that was solid at installation is not assumed to be solid five years later. It is verified.

**What to do:** Before attaching any hardware to the kiosk, perform the following inspection systematically:

**Posts and base:**
Push each structural post from multiple directions with firm, deliberate pressure. A sound post does not move. Any movement at the base — rocking, shifting, or soft give — indicates that the post base has degraded, whether from rot, heaved concrete, or corrosion of any metal anchor hardware. Check the post bases visually at ground level. Probe any area where the post contacts soil or a concrete pad with a pocket knife or a screwdriver tip. Sound wood resists the probe. Rotted wood yields to it.

**Mounting surfaces:**
Press firmly on the surfaces where the enclosure will be mounted. Solid surfaces do not flex or give. A surface that moves under hand pressure is not structurally adequate for an enclosure, regardless of how it looks. If the kiosk is wood-framed, check the grain direction and surface condition of the proposed mount panel. Check for delamination on plywood panels — five-year-old exterior plywood in a high-humidity environment may have edge delamination that is not visible from the face.

**Roof or canopy:**
The enclosure will be mounted in the area protected by the kiosk roof. Confirm the roof is intact, that there are no gaps or warped sections that would allow direct rainfall onto the equipment area, and that the roof attachment points are secure. Check the underside of the roof for water staining, which indicates past infiltration and may indicate ongoing risk.

**Existing hardware and signage:**
Any fasteners, brackets, or signs already on the kiosk should be checked for security. A loose sign that falls onto newly mounted electronics is a preventable equipment damage event.

**Biological occupants:**
Five-year-old outdoor structures in West Virginia frequently house wasps, mud daubers, paper wasps, and occasionally rodents. Check enclosed spaces, underside cavities, and any hollow structural elements before beginning work. Do not reach into enclosed spaces without looking first.

**Why this level of inspection is required on a structure H4H knows:**
Knowing a structure's history is not the same as knowing its current condition. H4H installed this kiosk and has maintained the surrounding trail area, but the kiosk itself has not necessarily been assessed for mounting load readiness. The inspection is also the first time the crew is close to and handling the kiosk with the specific purpose of attaching hardware to it. Problems visible from a few feet away during a trail walk may not have triggered concern. Problems that appear when a crew member puts their hand on the post and feels it shift require immediate action.

**What counts as a stop-and-report condition:**

- Any post that moves under firm pressure.
- Any mounting surface that flexes under hand pressure.
- Any visible rot in structural members or mounting surfaces — probe anything suspicious.
- Roof damage that would expose the equipment area to direct rainfall.
- Any metal fastener at a load-bearing point that shows active corrosion (rust that flakes or powders, not surface discoloration).
- Active wasp or rodent activity that has not been cleared.

If any of these conditions exist, stop and contact H4H before mounting anything. The kiosk may need repair work before the installation continues. That work is not the crew's job to improvise — it is H4H's decision to authorize and scope.

**What healthy condition looks like at five years:**
A well-sited and constructed outdoor kiosk at five years in a protected trail location should still be fundamentally sound, with surface weathering (fading, minor surface checking in wood, some UV discoloration) that is cosmetic rather than structural. The inspection is not expected to find catastrophic failure — but it is designed to catch the specific degradation that five-year-old outdoor structures in this climate do develop and that does matter for a mounted electronics installation.

**Lesson for future sites:** At any future site where H4H installs equipment on an existing structure — regardless of how well H4H knows that structure — this inspection happens first. Age the structure appropriately: a two-year-old kiosk gets a lighter inspection than a five-year-old one. A ten-year-old one gets a heavier one. Document the inspection result, including the estimated remaining service life of the structure, so H4H can plan maintenance on the right timeline.

---

### Step 2: Run the outdoor power cable to the kiosk

**What to do:** Route the outdoor-rated power cable (12/3 SJTW or equivalent) from the power source — which in this installation is the solar system's power output via an appropriate DC-to-AC inverter or a directly supported DC power path — to the kiosk location. Secure the cable along its run using UV-rated clips or cable ties spaced no more than 24 inches apart. Protect any section of the cable that crosses an area where foot traffic occurs, by routing it above head height, below grade in conduit, or along a structure that keeps it out of the path of pedestrians.

**Why at this stage:** Power must be at the kiosk before the enclosure is mounted and the Raspberry Pi is connected. Running the cable first establishes the power path and determines how much cable is needed. Cutting or connecting cable after the enclosure is already mounted in a tight space is significantly harder than routing the cable first while the enclosure is not yet in the way.

**Why this specific cable type:** The Southwire Yellow Jacket 12/3 SJTW and comparable products are outdoor-rated, weather-resistant, and designed for use in conditions that include moisture, UV, and temperature variation. Standard indoor extension cord material will degrade in outdoor conditions within one to two seasons, develop cracked insulation, and create a shock hazard. The heavier gauge (12 AWG) is appropriate for a run that may be twenty feet or longer and ensures that voltage drop along the cable does not reduce the available power at the Raspberry Pi's power supply below its operating range.

**What to check before moving on:** The cable is routed and secured along its full length. No section of the cable runs across a surface where it could be stepped on, driven over, or abraded by regular contact. The cable end at the kiosk has enough slack to reach the intended entry point on the enclosure without pulling tight.

**Lesson for future sites:** Note the actual cable run length at this site and the voltage at the Raspberry Pi power supply under load. That measurement tells you whether 12 AWG was the right choice for this run length. For longer runs at future sites, a heavier gauge or a shorter run using local power may be required.

---

### Step 3: Mount the weatherproof outdoor enclosure to the kiosk

**What to do:** Attach the Sixfab IP65 outdoor enclosure (or equivalent) to the kiosk mounting surface using fasteners appropriate for the surface material. At a wood kiosk, use stainless steel wood screws long enough to reach solid wood behind any surface treatment or paneling. At a metal kiosk, use stainless machine screws with backing nuts or self-tapping screws rated for the material thickness. Mount the enclosure at a height that:

- Places the equipment inside within the protected area of the kiosk canopy or roof.
- Keeps the cable entry ports accessible.
- Is reachable for maintenance without a ladder, if possible.
- Is not so low that it is at risk of direct contact with water pooling at the base of the kiosk.

**Why the enclosure before the Pi:** The Raspberry Pi is a small, static-sensitive circuit board. It should not be handled in an outdoor field environment any longer than necessary. The enclosure provides the protected environment the Pi needs before the Pi is placed in it. Mount the housing first, confirm it is solid, then bring the Pi out of its protective packaging and place it inside.

**Why stainless fasteners:** Standard zinc or uncoated steel fasteners will rust in outdoor conditions. At an outdoor kiosk in a location with regular rainfall and humidity, rust begins within one to two seasons. Rusted fasteners are difficult to remove for maintenance and can stain the kiosk surface. Stainless steel fasteners cost marginally more and last significantly longer.

**What to check before moving on:** The enclosure is solidly attached and does not rock or shift when pushed. The door opens fully without obstruction. The proposed cable entry points are facing in the direction the cable will come from.

---

### Step 4: Install the cable glands

**What to do:** Install the cable glands in the enclosure entry ports before running any cables through them. Each cable entering the enclosure needs its own gland. Tighten the glands to the enclosure wall first, then route the cable through the gland, and tighten the gland around the cable last.

**Why glands before cables:** A cable gland installed with the cable already in place is harder to tighten correctly and may not seal fully against the cable jacket. Installing the gland body first, then threading the cable through it, allows the gland to compress evenly around the cable when tightened. The result is a seal that holds against water infiltration. A gland installed the other way may appear sealed but leak under sustained rain or condensation.

**What glands are needed:** At minimum, this installation requires one gland for the power cable entering the enclosure. If any additional cables enter the enclosure — such as a network cable from the indoor network — each needs its own gland. Any enclosure port that is not used should be plugged with the included blanking plug and sealed with outdoor sealant.

**Lesson for future sites:** The specific cable diameter matters for gland selection. The gland must match the outer diameter of the cable jacket to compress and seal correctly. At this site, document which gland size was used for the 12/3 SJTW cable, as that information directly applies to any future site using the same cable type.

---

### Step 5: Prepare the Raspberry Pi and storage card

**What to do:** Outside the enclosure, in a clean and dry working environment — this may mean the interior of a vehicle, a table in the building, or a staging area protected from wind and moisture — do the following:

- Confirm the MicroSD card has been imaged with the correct operating system and configuration before arrival at the site. If it has not been pre-imaged, this must happen before the Pi is placed in the enclosure.
- Insert the MicroSD card into the Raspberry Pi.
- Confirm no physical damage to the Pi board — check for bent pins, cracked components, or missing connectors.
- Connect the short HDMI or display adapter if a diagnostic display will be used during initial startup.

**Why pre-image the card before the site visit:** Imaging a MicroSD card requires a computer and takes time. Doing it on site in the field, particularly at an outdoor location, introduces risk of errors, interruptions, and delays. If the correct software is not on the card when the crew arrives, the hotspot will not function when power is applied in Phase 10, and the crew will either have to wait on site or return for a second visit. Pre-imaging is preparation that cannot be skipped.

**Why outside the enclosure:** The Raspberry Pi board is small and the enclosure mounting hardware — standoffs, screws, brackets — requires careful alignment. Handling these components in a protected environment reduces the risk of dropping the board, losing small fasteners, or incorrectly seating components. Once the Pi is mounted and the cables are connected, it should not need to be removed again unless there is a hardware failure.

**Lesson for future sites:** At this pilot site, document the specific operating system image used, the version number, and where the image file is stored in H4H's records. Every future site that uses a Raspberry Pi for a similar purpose should use the same base image unless there is a deliberate reason to change it. Consistent images make maintenance and troubleshooting consistent.

---

### Step 6: Mount the Raspberry Pi inside the enclosure and connect power

**What to do:** Place the Raspberry Pi into the enclosure on the mounting standoffs provided. Secure it with the appropriate fasteners. Connect the Raspberry Pi power supply to the outdoor power cable that was run in Step 2. Connect the power supply output to the Raspberry Pi's USB-C power input. Do not power on yet.

**Why standoffs:** The Raspberry Pi board must not rest directly against the metal enclosure floor or against any surface that could cause an electrical short to the board's solder points. Standoffs hold the board above the enclosure floor by several millimeters, preventing contact and allowing air circulation under the board.

**Why not power on yet:** The full connection sequence — power, network, and any additional connections — should be completed before power is applied for the first time. Powering on a partially connected system can cause the Pi to boot into an unexpected state that requires a manual reset. Complete all connections first, then power on in the sequence described in Phase 10.

**What to check before moving on:** The Pi is secured on standoffs, the power supply is connected, and no cables are pinched against the enclosure edges or the board components.

---

### Step 7: Connect network cable if applicable

**What to do:** If the kiosk hotspot is designed to receive its internet connection from the indoor network via a wired Ethernet connection, run that cable to the kiosk location and connect it to the Raspberry Pi's Ethernet port. Route the cable through its own cable gland. If the connection to the indoor network is wireless, confirm the Pi's wireless configuration was set up during the pre-imaging step.

**Why wired is preferable to wireless for this link:** A wired Ethernet connection between the indoor network and the Pi at the kiosk is more reliable than a wireless connection over that same distance. Wireless connections are subject to interference, signal fading, and configuration drift. A wired connection either works or it does not, and diagnosing a fault is straightforward. For a public-facing hotspot that needs to be reliably available, the wired option is worth the additional cable run if the distance and physical conditions allow it.

**Why not discussed in more detail here:** The exact network architecture for this site — whether the Pi connects via wired or wireless to the indoor network, and what software it runs to create the public-facing hotspot — is a software configuration decision that is outside the scope of the physical installation workflow. That configuration should be documented separately and confirmed to be loaded on the MicroSD card before the site visit.

---

### Step 8: Mount the hotspot sign at the kiosk

**What to do:** Mount the Wi-Fi hotspot sign at the kiosk in a location that is:

- Visible to a person approaching the kiosk from the walking trail.
- At eye level or close to it for an adult standing in front of the kiosk.
- Not obstructed by any other signage, hardware, or structural element.
- Secured with fasteners appropriate for the kiosk surface.

Apply outdoor-rated sealant over any fastener holes drilled through the kiosk canopy or roof to prevent water infiltration at those points.

**Why the sign is the last item in this phase:** All physical hardware is in place before the sign goes up. The sign communicates to the public that the service is here. Installing it before the hardware is in place and tested would be premature — if the service is not ready, the sign creates an expectation that cannot be fulfilled. The sign goes up when the hardware is in place and ready for the testing phase.

**What to check before moving on:** The sign is level, secure, and readable from the trail approach. The sign clearly indicates that a Wi-Fi hotspot is available at this location — not just a generic Wi-Fi symbol, but a sign that a person unfamiliar with the project can understand.

**Lesson for future sites:** At this pilot site, note how people respond to the sign in the first weeks of operation. Does anyone stop and look for a network name? Do people understand that it is free? That feedback informs how signage is designed for future sites. The sign is not just a label — it is the first interaction the public has with the service.

---

### Step 9: Secure and protect all exposed wiring

**What to do:** Walk the full cable run from the power source to the kiosk and confirm the following:

- Every section of exposed cable is secured to a surface or structure.
- No cable hangs freely in a location where wind, foot traffic, or equipment contact could pull it.
- All connections at both ends of every cable are covered with appropriate strain relief.
- Any cable passing through a hole in wood or metal is protected by a grommet or a sealed cable gland — not resting against the raw edge of the hole.
- All cable glands on the enclosure are tightened against the cable jackets.
- Outdoor sealant is applied to any cable entry point that is not fully sealed by the gland alone.

**Why this step is its own item and not an afterthought:** Exposed cables in a public outdoor location are subject to forces that cables in an indoor installation are not. Wind causes cables to flex repeatedly at stress points, leading to fatigue failure over months. Curious hands sometimes pull at cables that look accessible. Animals, particularly rodents, investigate and sometimes chew cables that are at ground level or accessible. Rain drives into any opening that is not sealed. Making cable runs clean and fully protected at the time of installation is the difference between a system that runs for years and one that fails in the first season.

**What a correctly completed Phase 7 looks like:** The outdoor enclosure is mounted solidly on the kiosk, sealed at all cable entry points, with the Raspberry Pi inside on standoffs and connected to power and network. The power cable is routed cleanly from the power source to the enclosure without loops or exposed connections at intermediate points. The hotspot sign is visible, level, and readable. No cables hang freely. The enclosure door latches closed without forcing. The kiosk looks maintained, intentional, and ready for public use.

---

## What Happens If This Phase Is Rushed or Skipped in Part

**Structural inspection skipped on an aged structure:** Five-year-old outdoor wood structures in high-humidity Appalachian climates develop rot at post bases, fastener points, and any location where water can pool or wick into end grain. These failure points are often not visible from standing height and are not apparent without probing. A post base that has lost 30 percent of its cross-section to rot may hold the original sign panel without any visible problem and still fail under the additional torque load of a mounted electronics enclosure in a wind event. The inspection described in Step 1 exists specifically to find these conditions before hardware is committed to the structure. Skipping it because the kiosk is familiar and trusted is the most common way this class of failure occurs — familiarity creates an assumption of soundness that a hands-on inspection might not support.

**Cable glands not fully tightened:** Moisture infiltration through a loose cable gland at a comparable installation caused a Raspberry Pi board failure at the USB-C power input connector within one year. The failure presented as intermittent power loss and was initially diagnosed as a power supply problem. Full diagnosis required removing and inspecting the board. The gland could have been tightened in under a minute at installation.

**MicroSD not pre-imaged:** A crew that arrived on site without a pre-imaged card spent two hours imaging the card in the field using a laptop, consuming the afternoon and requiring the testing phase to be deferred to a return trip. The return trip cost a full day of crew time and delayed public availability of the service by two weeks.

**Sign installed before testing:** A hotspot sign installed before the service was confirmed active at a similar site generated public complaints when users could not find a working network. Managing those complaints consumed time and damaged the community's confidence in the project. The sign should go up when the service is ready.

---

## What to Record When Phase 7 Is Complete

Before moving to Phase 8, record and photograph the following:

- Raspberry Pi serial number and the MicroSD card image version loaded on it.
- Photograph of the Pi inside the mounted enclosure before the door is closed.
- Photograph of the sealed and closed enclosure on the kiosk.
- Photograph of the cable run from the power source to the kiosk.
- Photograph of the hotspot sign in its installed position.
- Note of the kiosk structural inspection result and any observations about kiosk condition.
- Note of any deviation from the planned installation and the reason for it.

---

## Carrying These Lessons Forward

At future sites, the core lessons from this phase are:

1. Structural inspection is not a formality on a structure you know. It is especially necessary on one you know, because familiarity creates assumptions that a hands-on inspection is designed to test. Five years of Appalachian weather changes a structure. Assess it accordingly.
2. Pre-image the storage card before arriving on site. This is preparation, not optional.
3. Cable glands must be tightened against the cable jacket, not just installed in the enclosure wall.
4. Wired network connections are more reliable than wireless for the link between the indoor network and the kiosk Pi.
5. The sign goes up after the hardware is in place and confirmed ready to test — not before.
6. Clean cable runs in public outdoor spaces are not cosmetic. They are structural protection for the cable.
7. This kiosk is the public face of the project. How it looks and how accessible it is matter to the community's trust in H4H and in this service.
