# Installation Workflow for Crew

## Purpose
This document is a field guide for the crew installing the public equipment. It explains what equipment is being installed, how materials are staged, the order of work, what must be tested, and what must be documented before the installation is complete.

## Project Scope
This installation covers equipment located at 704 Main Street and the public kiosk location serving the Mount Hope walking trail. The installed system includes an indoor internet and equipment point at 704 Main Street and an outdoor public-use location with its own power and communications hardware.

## Equipment Covered by This Workflow
The crew should plan around the following equipment groups:

- Starlink internet hardware for the main building.
- Local network equipment for distribution at the main building.
- One small edge computer or mini PC at the main building.
- One existing outdoor kiosk location used as a hotspot point.
- One outdoor Starlink receiver point with solar power support.
- One LoRa backup communications node with solar support.
- Supporting parts such as brackets, enclosures, poles, cable runs, anchors, conduit, weather protection, and power accessories.

## Responsibilities

| Area | Responsible party |
|------|-------------------|
| Equipment ownership | H4H |
| Site access and placement approval | H4H |
| Power and internet service | H4H |
| Monthly internet cost | H4H |
| Equipment records after install | H4H |
| Physical maintenance after install | H4H |
| Optional outside technical help | Only if separately contracted by H4H |

## Installation Order
The crew should complete the work in the following order:

1. Complete procurement and staging.
2. Verify all site kits and parts.
3. Confirm the install points.
4. Inspect hardware before field placement.
5. Prepare the building and kiosk locations.
6. Install internet equipment and local network hardware.
7. Install solar hardware and weatherproof enclosures.
8. Mount the kiosk and related field equipment.
9. Connect power and network lines.
10. Start and test all equipment.
11. Photograph, label, and log each completed install.
12. Report any missing, unsafe, or incomplete work before leaving the site.

## Step-by-Step Workflow

### Phase 1: Procurement and Staging
This phase takes place before any field installation begins. The purpose is to make sure every location has the correct equipment, all required parts are present, and the crew is not forced to improvise on site.

#### 1. Define Equipment by Location
The crew lead or project lead should assign every item to a specific install point before ordering.

Location groups for this project:
- 704 Main Street indoor equipment point.
- Walking trail kiosk location.
- Outdoor solar and communications mounting point.

#### 2. Parts List for Procurement and Staging
The following list should be used as the working procurement and staging list for the crew. Where a real product page has already been verified, it is linked directly below. Where no exact product has been locked yet, the entry is marked for final source selection before ordering.

| Site ID | Location | Item | Description | Qty | Link status |
|---------|----------|------|-------------|-----|-------------|
| FCCAC-01 | 704 Main Street | Starlink kit | Main Starlink internet hardware kit | 1 | [Starlink Standard 4 X kit](https://www.homedepot.com/p/STARLINK-Standard-4-X-High-Speed-Low-Latency-Internet-Kit-Latest-Model-02534001/329052560) |
| FCCAC-01 | 704 Main Street | Starlink mount | Roof, wall, or pole mount for Starlink dish | 1 | Final mount type must be chosen per site |
| FCCAC-01 | 704 Main Street | Router | Main internet router | 1 | Included with Starlink kit |
| FCCAC-01 | 704 Main Street | Small network switch | Local wired distribution switch | 1 | Exact switch model still needed |
| FCCAC-01 | 704 Main Street | Wi-Fi access point | Indoor wireless coverage unit if needed | 1 | May not be needed until testing |
| FCCAC-01 | 704 Main Street | Mini PC | Small edge computer or NUC-style unit | 1 | Exact mini PC model still needed |
| FCCAC-01 | 704 Main Street | UPS battery backup | Small battery backup for router and mini PC | 1 | Exact UPS model still needed |
| FCCAC-01 | 704 Main Street | Surge protector | Power protection strip | 2 | Exact surge strip model still needed |
| FCCAC-01 | 704 Main Street | Ethernet cable | Pre-made or bulk CAT6 cable | 4 | Exact cable length and source still needed |
| FCCAC-01 | 704 Main Street | Cable clips and ties | Cable management supplies | 1 lot | Exact source still needed |
| FCCAC-01 | 704 Main Street | Wall anchors and screws | Mounting fasteners | 1 lot | Exact source still needed |
| FCCAC-01 | 704 Main Street | Conduit or raceway | Cable protection for exposed runs | 1 lot | Exact source still needed |
| KIOSK-01 | Walking trail kiosk | Existing kiosk structure | Existing kiosk already on site | 1 | Existing asset, no purchase needed |
| KIOSK-01 | Walking trail kiosk | Hotspot sign | Small Wi-Fi sign or Wi-Fi symbol sign | 1 | Final sign source still needed |
| KIOSK-01 | Walking trail kiosk | Outdoor weatherproof enclosure | Lockable enclosure for equipment | 1 | [Sixfab IP65 enclosure](https://sixfab.com/product/raspberry-pi-ip65-outdoor-iot-project-enclosure/) |
| KIOSK-01 | Walking trail kiosk | Raspberry Pi | Small controller or receiver unit | 1 | Final source still needed |
| KIOSK-01 | Walking trail kiosk | Raspberry Pi power supply | Power adapter for Raspberry Pi | 1 | Exact source still needed |
| KIOSK-01 | Walking trail kiosk | MicroSD card | Storage card for Raspberry Pi | 1 | Exact source still needed |
| KIOSK-01 | Walking trail kiosk | Short HDMI or adapter cable | Display connection as needed | 1 | Exact source still needed |
| KIOSK-01 | Walking trail kiosk | Outdoor power cable | Weather-rated power cable | 1 | Exact source still needed |
| KIOSK-01 | Walking trail kiosk | Exterior cable gland set | Waterproof cable pass-through fittings | 1 set | Included with some enclosures; verify before ordering |
| SOLAR-01 | Outdoor solar point | Solar panel | 200W solar panel | 1 | [Rich Solar MEGA 200](https://richsolar.com/products/mega-200-200-watt-12-volt-solar-panel) |
| SOLAR-01 | Outdoor solar point | Solar charge controller | Charge controller sized for the panel and battery | 1 | Exact controller model still needed |
| SOLAR-01 | Outdoor solar point | Battery | 12V 100Ah battery | 1 | Exact battery model still needed |
| SOLAR-01 | Outdoor solar point | Battery box | Weather-protected battery housing | 1 | Exact box model still needed |
| SOLAR-01 | Outdoor solar point | Pole or mounting frame | Support for solar panel and radio hardware | 1 | Exact mount still needed |
| SOLAR-01 | Outdoor solar point | Panel mounting brackets | Hardware for securing solar panel | 1 set | Exact bracket set still needed |
| SOLAR-01 | Outdoor solar point | Weatherproof electronics enclosure | Sealed box for power and communication parts | 1 | Exact enclosure still needed |
| SOLAR-01 | Outdoor solar point | Fuse block or inline fuses | Electrical protection hardware | 1 set | Exact source still needed |
| SOLAR-01 | Outdoor solar point | DC wiring set | Power wire, terminals, and connectors | 1 lot | Exact source still needed |
| SOLAR-01 | Outdoor solar point | Grounding hardware | Ground rod, clamp, and wire if required | 1 set | Exact source still needed |
| SOLAR-01 | Outdoor solar point | Starlink receiver point hardware | Hardware needed at the outdoor receive point | 1 set | Depends on final mount and enclosure layout |
| LORA-01 | Outdoor communications point | LoRa node | LILYGO T-Beam or Heltec LoRa32 class device | 1 | Exact board revision still needed |
| LORA-01 | Outdoor communications point | LoRa antenna | External or matched antenna | 1 | Exact antenna still needed |
| LORA-01 | Outdoor communications point | Small solar support kit | Solar support for LoRa backup node | 1 | Exact source still needed |
| LORA-01 | Outdoor communications point | LoRa enclosure | Small weatherproof box | 1 | Exact enclosure still needed |
| LORA-01 | Outdoor communications point | Pole clamps or mount straps | Hardware for mounting the node | 1 set | Exact source still needed |
| ALL-LOC | All locations | Labels | Equipment ID labels | 1 lot | Exact source still needed |
| ALL-LOC | All locations | Photo log sheet | Install record sheet | 1 set | Internal print item |
| ALL-LOC | All locations | Spare fasteners | Spare screws, anchors, bolts, and washers | 1 lot | Exact source still needed |
| ALL-LOC | All locations | Sealant | Outdoor weather sealant | 1 tube | Exact source still needed |
| ALL-LOC | All locations | Electrical tape and heat shrink | Wire protection supplies | 1 lot | Exact source still needed |

#### 3. Receive and Inspect Equipment
All equipment should be checked as soon as it arrives.

Checklist:
- Match each delivered item to the parts list.
- Inspect for broken parts, dents, cracks, or missing accessories.
- Record serial numbers for Starlink hardware, mini PC, Raspberry Pi, and radio hardware where available.
- Separate damaged or incomplete items from field-ready items.

#### 4. Stage Site Kits
Each location should have its own labeled kit so the crew can load and unload efficiently.

Required site kits:
- FCCAC-01 indoor kit.
- KIOSK-01 outdoor kiosk kit.
- SOLAR-01 solar power kit.
- LORA-01 backup communications kit.

Each kit should include:
- Main device or hardware assigned to that site.
- All required fasteners and mounts.
- Power parts and adapters.
- Cables and cable protection.
- Printed copy of that site's parts list.
- Printed site notes.

#### 5. Pre-Field Verification
Before vehicles are loaded, confirm the following:

- All site kits are complete.
- Internet hardware is in hand.
- Solar parts are complete.
- Batteries are ready for installation.
- Labels, paperwork, and tools are packed.
- Spare fasteners and spare cable are packed.

### Phase 2: Confirm the Work Plan
Before installation begins, the crew reviews the install points and confirms the final placement of each device.

Checklist:
- Confirm 704 Main Street equipment placement.
- Confirm kiosk placement.
- Confirm solar mounting point.
- Confirm where the LoRa backup node will be attached.
- Confirm who approves final placement on site.

### Phase 3: Inspect Hardware Before Placement
Every item should be checked again before field placement.

Checklist:
- Verify the correct device is in the correct site kit.
- Check that no hardware was damaged during transport.
- Check that all required power supplies, brackets, and cables are present.

### Phase 4: Prepare the Site
Each location must be ready before any device is mounted.

Checklist:
- Check walls, poles, surfaces, and install heights.
- Confirm safe cable routes.
- Confirm public safety and access.
- Confirm weather exposure and drainage.
- Confirm power access where needed.

### Phase 5: Install Internet and Indoor Equipment
The indoor building point should be installed first so the main connection is active.

Checklist:
- Install the Starlink mount.
- Install the Starlink hardware.
- Route cable safely into the building.
- Install router, switch, and indoor wireless unit if used.
- Install the mini PC.
- Install UPS and surge protection.
- Confirm internet service is live.

### Phase 6: Install Solar and Outdoor Support Hardware
The outdoor support systems should be installed before the public-facing kiosk device is closed up.

Checklist:
- Mount the 200W solar panel.
- Install the panel brackets and support frame.
- Install the charge controller.
- Install the 12V 100Ah battery in its battery box.
- Install fuse protection and DC wiring.
- Install the weatherproof equipment enclosure.
- Confirm secure weather protection.

### Phase 7: Install Kiosk Hotspot Equipment
After support hardware is in place, install the hotspot equipment at the existing kiosk location.

Checklist:
- Confirm the existing kiosk is structurally sound.
- Install the outdoor enclosure.
- Install the Raspberry Pi and storage card if used for local control or monitoring.
- Install the hotspot sign or Wi-Fi symbol sign.
- Secure and protect all exposed wiring.

### Phase 8: Install Backup Communications Node
The backup communications equipment should be mounted and protected after the main outdoor hardware is in place.

Checklist:
- Install the LoRa node.
- Install the antenna.
- Install the small solar support kit if separate from the main solar hardware.
- Mount the node in the weatherproof box.
- Confirm it is secure and protected.

### Phase 9: Connect Power and Network
Once all hardware is mounted, connect final power and network paths.

Checklist:
- Connect indoor equipment to power and UPS.
- Connect outdoor kiosk equipment to the assigned power source.
- Connect internet and local network lines as required.
- Confirm cable strain relief and weather sealing.
- Confirm exposed wiring is protected.

### Phase 10: Start and Test Equipment
Each location must be tested before the crew leaves.

Checklist:
- Power on Starlink and confirm connection.
- Power on router, switch, and mini PC.
- Confirm indoor network access.
- Power on kiosk equipment.
- Confirm the Raspberry Pi starts correctly.
- Confirm the kiosk display or public function works.
- Confirm the LoRa backup node powers on.
- Restart each main device once if needed to confirm stable startup.

### Phase 11: Record the Installation
All completed work must be documented.

Checklist:
- Apply equipment labels.
- Photograph each installed device.
- Photograph cable runs, enclosures, and solar hardware.
- Record the final install location.
- Record any issue, limitation, or follow-up need.

### Phase 12: Close Out the Site
Before leaving, the crew should confirm whether the location is complete or whether a return trip is needed.

Checklist:
- Confirm the site is clean and safe.
- Remove packaging and scrap material.
- List incomplete items.
- Report any condition that prevents public use.

## Minimum Acceptance Standard
A location is complete only when all of the following are true:

- The correct hardware is installed in the correct location.
- Indoor internet hardware is active.
- The mini PC is installed and powered.
- The kiosk is secure and weather protected.
- The Raspberry Pi starts correctly.
- The solar panel, controller, and battery are installed safely.
- The LoRa backup node is mounted and powered.
- Required photos and equipment records are complete.
- Any unresolved issue has been reported to H4H.

## Issues That Must Be Reported Immediately
The crew should stop and report the issue if any of the following occur:

- No safe mounting surface is available.
- No usable power path is available.
- Internet service cannot be activated.
- Solar hardware cannot be mounted safely.
- Equipment arrives damaged or incomplete.
- A mounted unit cannot be secured.
- Weather or site conditions prevent safe completion.

## Site Kit Checklist
Each site kit should include all parts needed for one location.

### FCCAC-01 Indoor Kit
- Starlink kit.
- Starlink mount.
- Router.
- Small network switch.
- Wi-Fi unit if used.
- Mini PC.
- UPS battery backup.
- Surge protector.
- Ethernet cables.
- Cable clips, ties, anchors, and screws.

### KIOSK-01 Outdoor Kiosk Kit
- Existing kiosk structure.
- Hotspot sign.
- Outdoor weatherproof enclosure.
- Raspberry Pi.
- Raspberry Pi power supply.
- MicroSD card.
- Short display cable or adapter.
- Outdoor power cable.
- Exterior cable glands.

### SOLAR-01 Solar Kit
- 200W solar panel.
- Solar charge controller.
- 12V 100Ah battery.
- Battery box.
- Pole or support frame.
- Panel mounting brackets.
- Weatherproof electronics enclosure.
- Fuse protection.
- DC wiring set.
- Grounding hardware if required.

### LORA-01 Backup Communications Kit
- LoRa node.
- LoRa antenna.
- Small solar support kit.
- LoRa enclosure.
- Pole clamps or mount straps.

## After Installation
After the crew finishes the installation, H4H remains responsible for the equipment, internet service, ongoing costs, and future upkeep. Outside technical help may be brought in later only if H4H chooses to contract for it separately.

## Procurement SKU Sheet
This section is appended for ordering. The links below are live product pages for the main items already identified for this build. Items without a locked source should be finalized before purchase.

| Category | Item | Model / SKU | Vendor | Purchase link | Notes |
|----------|------|-------------|--------|---------------|-------|
| Internet uplink | Starlink Standard kit | Model 02534001, Internet #329052560, Store SKU #1011034206 | Home Depot | [Starlink Standard 4 X kit](https://www.homedepot.com/p/STARLINK-Standard-4-X-High-Speed-Low-Latency-Internet-Kit-Latest-Model-02534001/329052560) | Includes Starlink, power supply, cables, base, and router. Monthly service plan required. |
| Solar panel | 200W solar panel | MEGA 200 | Rich Solar | [Rich Solar MEGA 200](https://richsolar.com/products/mega-200-200-watt-12-volt-solar-panel) | 200W panel only; battery and controller ordered separately unless a full kit is chosen. |
| Outdoor enclosure | Raspberry Pi weatherproof enclosure | Sixfab IP65 Outdoor Project Enclosure | Sixfab | [Sixfab IP65 enclosure](https://sixfab.com/product/raspberry-pi-ip65-outdoor-iot-project-enclosure/) | Compatible with Raspberry Pi and outdoor cable routing. |

## Procurement Notes
- The Starlink hardware link above is a real retail listing for the Standard 4 X kit and is the lowest-cost grounded starting point identified for this pilot. It is appropriate for a first site unless later traffic or uptime needs justify a business-class upgrade.
- The Rich Solar panel link is a real manufacturer page for the 200W panel, but it is only the panel. Battery, controller, mounts, and wiring still need exact SKU selection.
- The Sixfab enclosure link is a real product page for outdoor Raspberry Pi protection, but the Raspberry Pi board itself, storage card, power supply, and any display hardware still need exact SKU selection.
- Before ordering, each remaining line item should be completed with the same fields used above: model, vendor, and direct purchase link.
