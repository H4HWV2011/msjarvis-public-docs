crypto-venv) cakidd@cakidd-Legion-5-16IRX9:/mnt/spiritual_drive/msjarvis-rebuild$ mkdir -p scripts

cat > scripts/msjarvis_smoketest.sh << 'EOF'
#!/usr/bin/env bash
set -euo pipefail

MSG="community governance and blockchain for Mount Hope West Virginia"
USER="cakidd"

echo "=== MSJARVIS SMOKETEST: $(date) ==="

cd /mnt/spiritual_drive/msjarvis-rebuild

echo
echo "=== 0. SERVICE STATUS SNAPSHOT ==="
systemctl is-active jarvis-consensus-4010.service \
  jarvis-consciousness-4021.service \
  msjarvis-69dgm-orchestrator-9998.service \
  msjarvis-69dgm-9000.service || true

echo
echo "=== 1. DIRECT 4010 CONSENSUS CHECK ==="
curl -s http://127.0.0.1:4010/consensus \
chmod +x scripts/msjarvis_smoketest.shutes ago" --no-pager | tail -n 20 || true
(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:/mnt/spiritual_drive/msjarvis-rebuild$ cd /mnt/spiritual_drive/msjarvis-rebuild
scripts/msjarvis_smoketest.sh
=== MSJARVIS SMOKETEST: Fri Jul  3 07:46:02 PM EDT 2026 ===

=== 0. SERVICE STATUS SNAPSHOT ===
active
active
inactive
active

=== 1. DIRECT 4010 CONSENSUS CHECK ===
{
    "consensus": "Community Governance in the context of Blockchain Technology, particularly within a locality like Mount Hope, WV can revolutionize how communities manage resources, transacts financially among members, engage democratically, and maintain sustainable development. Here are ways blockchain could be leveraged for governance: 1. **Smart Contracts for Local Decisions** - Blockchain's smart contracts can automate local decisions like recycling processes or community event planning where conditions trigger automatic actions without needing human intervention, enscuring transparency and efficiency in operations with immediate execution once agreed upon terms are met. 2. **Tokenization of Assets** - Tokenizing real estate could enable democratized ownership within the Mount Hope area; local residents can buy or sell properties securely without lengthy legal procedures using blockchain technology, potentially opening up investment opportunities and revitalizing dormant homes in a controlled manner while keeping community cohesion intact. 3. **Decentralized Financing** - Adopting Decentralized Autonomous Organizations (DAOs) or Community Blockchains could create decent finance mechanisms like crowdsourcing for local projects, collective bonds for infrastructure development without the need for large banks and to allow investments directly within community-members\u2019 wallets. 4. **Participatory Budgeting** - Using blockchain platforms can facilitate a participatory budgeting process where residents vote on allocation of funds towards local projects, ensuring that decisions reflect communal priorities rather than external interests and providing transparent tracking of expenditures against outcomes to enhance trust in the system. 5. **Digital Identification** - Blockchain can provide a secure identity verification process for residents which is essential when it comes to voting, participating in local governance or accessing community services ensuring that every member has equal opportunity and voice without fear of voter suppression tactics often seen with conventional systems. 6. **Supply Chain Transparency** - Blockchain could enhance transparency for locally sourced goods, allowing consumers to trace where products come from directly on a public ledger which can improve accountability and reduce counterfeiting or substandard materials in local trade networks. 7. **Energy Community Initiatives** \u2013 Mount Hope might look into joining energy cooperative models facilitated by blockchain technology, creating decentralized electricity grids that allow residents to sell excess power back to the grid and manage their own renewable resources more effectively while supporting local businesses in a sustainable fashion. 8. **Data Security**Civic Engagement Platforms** \u2013 A dedicated community platform using a private blockchain to engage residents on local issues in real time provides an organized, efficient way for people to express opinions and vote remotely which could result in more inclusive governance as remote participation often sees lower turnout among traditionally marginalized groups. 10. **Integration with Existing Services** - Blockchain can be integrated into the current systems of Mount Hope by adopting open-source blockchain solutions for non-custodial, permissioned ledgers that enhance transparency while interfacing seamlessly with existing municipal databases and services to ensure continuity in governance processes. 11. **Cross-Community Engagement** - Blockchain can link not just within Mount Hope but also connect it more strongly with surrounding communities, potentially sharing resources for larger regional projects like park development or disaster relief funds through a shared ledger that benefits multiple counties and municipalities while preserving the autonomy of local governance. 12. **Implementing Educational Workshops** - To ensure inclusive community participation in blockchain-driven governance, educational workshops can be conducted for residents to understand how these technologies function so they feel comfortable engaging with and benefiting from the new systems without intimidation or information asymmetry. By leveraging Blockchain technology within Mount Hope's local community governance structures, it is possible not only to improve transparency and efficiency but also empower residents through increased participation in decisions that directly affect their lives while fostering a stronger sense of community ownership and responsibility.",
    "response": "Community Governance in the context of Blockchain Technology, particularly within a locality like Mount Hope, WV can revolutionize how communities manage resources, transacts financially among members, engage democratically, and maintain sustainable development. Here are ways blockchain could be leveraged for governance:\n\n1. **Smart Contracts for Local Decisions** - Blockchain's smart contracts can automate local decisions like recycling processes or community event planning where conditions trigger automatic actions without needing human intervention, enscuring transparency and efficiency in operations with immediate execution once agreed upon terms are met.\n   \n2. **Tokenization of Assets** - Tokenizing real estate could enable democratized ownership within the Mount Hope area; local residents can buy or sell properties securely without lengthy legal procedures using blockchain technology, potentially opening up investment opportunities and revitalizing dormant homes in a controlled manner while keeping community cohesion intact.\n   \n3. **Decentralized Financing** - Adopting Decentralized Autonomous Organizations (DAOs) or Community Blockchains could create decent finance mechanisms like crowdsourcing for local projects, collective bonds for infrastructure development without the need for large banks and to allow investments directly within community-members\u2019 wallets.\n   \n4. **Participatory Budgeting** - Using blockchain platforms can facilitate a participatory budgeting process where residents vote on allocation of funds towards local projects, ensuring that decisions reflect communal priorities rather than external interests and providing transparent tracking of expenditures against outcomes to enhance trust in the system.\n   \n5. **Digital Identification** - Blockchain can provide a secure identity verification process for residents which is essential when it comes to voting, participating in local governance or accessing community services ensuring that every member has equal opportunity and voice without fear of voter suppression tactics often seen with conventional systems.\n   \n6. **Supply Chain Transparency** - Blockchain could enhance transparency for locally sourced goods, allowing consumers to trace where products come from directly on a public ledger which can improve accountability and reduce counterfeiting or substandard materials in local trade networks.\n   \n7. **Energy Community Initiatives** \u2013 Mount Hope might look into joining energy cooperative models facilitated by blockchain technology, creating decentralized electricity grids that allow residents to sell excess power back to the grid and manage their own renewable resources more effectively while supporting local businesses in a sustainable fashion.\n   \n8. **Data Security** - Given the sensitivity of governance data and personal information handled by Mount Hope's administration, blockchain could offer enhanced security for records management with immutable audit trails reducing instances of corruption or loss within public documents.\n   \n9. **Civic Engagement Platforms** \u2013 A dedicated community platform using a private blockchain to engage residents on local issues in real time provides an organized, efficient way for people to express opinions and vote remotely which could result in more inclusive governance as remote participation often sees lower turnout among traditionally marginalized groups.\n   \n10. **Integration with Existing Services** - Blockchain can be integrated into the current systems of Mount Hope by adopting open-source blockchain solutions for non-custodial, permissioned ledgers that enhance transparency while interfacing seamlessly with existing municipal databases and services to ensure continuity in governance processes.\n   \n11. **Cross-Community Engagement** - Blockchain can link not just within Mount Hope but also connect it more strongly with surrounding communities, potentially sharing resources for larger regional projects like park development or disaster relief funds through a shared ledger that benefits multiple counties and municipalities while preserving the autonomy of local governance.\n   \n12. **Implementing Educational Workshops** - To ensure inclusive community participation in blockchain-driven governance, educational workshops can be conducted for residents to understand how these technologies function so they feel comfortable engaging with and benefiting from the new systems without intimidation or information asymmetry.\n   \nBy leveraging Blockchain technology within Mount Hope's local community governance structures, it is possible not only to improve transparency and efficiency but also empower residents through increased participation in decisions that directly affect their lives while fostering a stronger sense of community ownership and responsibility.",
    "answer": "Community Governance in the context of Blockchain Technology, particularly within a locality like Mount Hope, WV can revolutionize how communities manage resources, transacts financially among members, engage democratically, and maintain sustainable development. Here are ways blockchain could be leveraged for governance:\n\n1. **Smart Contracts for Local Decisions** - Blockchain's smart contracts can automate local decisions like recycling processes or community event planning where conditions trigger automatic actions without needing human intervention, enscuring transparency and efficiency in operations with immediate execution once agreed upon terms are met.\n   \n2. **Tokenization of Assets** - Tokenizing real estate could enable democratized ownership within the Mount Hope area; local residents can buy or sell properties securely without lengthy legal procedures using blockchain technology, potentially opening up investment opportunities and revitalizing dormant homes in a controlled manner while keeping community cohesion intact.\n   \n3. **Decentralized Financing** - Adopting Decentralized Autonomous Organizations (DAOs) or Community Blockchains could create decent finance mechanisms like crowdsourcing for local projects, collective bonds for infrastructure development without the need for large banks and to allow investments directly within community-members\u2019 wallets.\n   \n4. **Participatory Budgeting** - Using blockchain platforms can facilitate a participatory budgeting process where residents vote on allocation of funds towards local projects, ensuring that decisions reflect communal priorities rather than external interests and providing transparent tracking of expenditures against outcomes to enhance trust in the system.\n   \n5. **Digital Identification** - Blockchain can provide a secure identity verification process for residents which is essential when it comes to voting, participating in local governance or accessing community services ensuring that every member has equal opportunity and voice without fear of voter suppression tactics often seen with conventional systems.\n   \n6. **Supply Chain Transparency** - Blockchain could enhance transparency for locally sourced goods, allowing consumers to trace where products come from directly on a public ledger which can improve accountability and reduce counterfeiting or substandard materials in local trade networks.\n   \n7. **Energy Community Initiatives** \u2013 Mount Hope might look into joining energy cooperative models facilitated by blockchain technology, creating decentralized electricity grids that allow residents to sell excess power back to the grid and manage their own renewable resources more effectively while supporting local businesses in a sustainable fashion.\n   \n8. **Data Security** - Given the sensitivity of governance data and personal information handled by Mount Hope's administration, blockchain could offer enhanced security for records management with immutable audit trails reducing instances of corruption or loss within public documents.\n   \n9. **Civic Engagement Platforms** \u2013 A dedicated community platform using a private blockchain to engage residents on local issues in real time provides an organized, efficient way for people to express opinions and vote remotely which could result in more inclusive governance as remote participation often sees lower turnout among traditionally marginalized groups.\n   \n10. **Integration with Existing Services** - Blockchain can be integrated into the current systems of Mount Hope by adopting open-source blockchain solutions for non-custodial, permissioned ledgers that enhance transparency while interfacing seamlessly with existing municipal databases and services to ensure continuity in governance processes.\n   \n11. **Cross-Community Engagement** - Blockchain can link not just within Mount Hope but also connect it more strongly with surrounding communities, potentially sharing resources for larger regional projects like park development or disaster relief funds through a shared ledger that benefits multiple counties and municipalities while preserving the autonomy of local governance.\n   \n12. **Implementing Educational Workshops** - To ensure inclusive community participation in blockchain-driven governance, educational workshops can be conducted for residents to understand how these technologies function so they feel comfortable engaging with and benefiting from the new systems without intimidation or information asymmetry.\n   \nBy leveraging Blockchain technology within Mount Hope's local community governance structures, it is possible not only to improve transparency and efficiency but also empower residents through increased participation in decisions that directly affect their lives while fostering a stronger sense of community ownership and responsibility.",
    "models_consulted": 3,
    "successful_responses": 3,
    "responses": [
        {
            "model": "Phi3 Mini",
            "response": "Community Governance in the context of Blockchain Technology, particularly within a locality like Mount Hope, WV can revolutionize how communities manage resources, transacts financially among members, engage democratically, and maintain sustainable development. Here are ways blockchain could be leveraged for governance:\n\n1. **Smart Contracts for Local Decisions** - Blockchain's smart contracts can automate local decisions like recycling processes or community event planning where conditions trigger automatic actions without needing human intervention, enscuring transparency and efficiency in operations with immediate execution once agreed upon terms are met.\n   \n2. **Tokenization of Assets** - Tokenizing real estate could enable democratized ownership within the Mount Hope area; local residents can buy or sell properties securely without lengthy legal procedures using blockchain technology, potentially opening up investment opportunities and revitalizing dormant homes in a controlled manner while keeping community cohesion intact.\n   \n3. **Decentralized Financing** - Adopting Decentralized Autonomous Organizations (DAOs) or Community Blockchains could create decent finance mechanisms like crowdsourcing for local projects, collective bonds for infrastructure development without the need for large banks and to allow investments directly within community-members\u2019 wallets.\n   \n4. **Participatory Budgeting** - Using blockchain platforms can facilitate a participatory budgeting process where residents vote on allocation of funds towards local projects, ensuring that decisions reflect communal priorities rather than external interests and providing transparent tracking of expenditures against outcomes to enhance trust in the system.\n   \n5. **Digital Identification** - Blockchain can provide a secure identity verification process for residents which is essential when it comes to voting, participating in local governance or accessing community services ensuring that every member has equal opportunity and voice without fear of voter suppression tactics often seen with conventional systems.\n   \n6. **Supply Chain Transparency** - Blockchain could enhance transparency for locally sourced goods, allowing consumers to trace where products come from directly on a public ledger which can improve accountability and reduce counterfeiting or substandard materials in local trade networks.\n   \n7. **Energy Community Initiatives** \u2013 Mount Hope might look into joining energy cooperative models facilitated by blockchain technology, creating decentralized electricity grids that allow residents to sell excess power back to the grid and manage their own renewable resources more effectively while supporting local businesses in a sustainable fashion.\n   \n8. **Data Security** - Given the sensitivity of governance data and personal information handled by Mount Hope's administration, blockchain could offer enhanced security for records management with immutable audit trails reducing instances of corruption or loss within public documents.\n   \n9. **Civic Engagement Platforms** \u2013 A dedicated community platform using a private blockchain to engage residents on local issues in real time provides an organized, efficient way for people to express opinions and vote remotely which could result in more inclusive governance as remote participation often sees lower turnout among traditionally marginalized groups.\n   \n10. **Integration with Existing Services** - Blockchain can be integrated into the current systems of Mount Hope by adopting open-source blockchain solutions for non-custodial, permissioned ledgers that enhance transparency while interfacing seamlessly with existing municipal databases and services to ensure continuity in governance processes.\n   \n11. **Cross-Community Engagement** - Blockchain can link not just within Mount Hope but also connect it more strongly with surrounding communities, potentially sharing resources for larger regional projects like park development or disaster relief funds through a shared ledger that benefits multiple counties and municipalities while preserving the autonomy of local governance.\n   \n12. **Implementing Educational Workshops** - To ensure inclusive community participation in blockchain-driven governance, educational workshops can be conducted for residents to understand how these technologies function so they feel comfortable engaging with and benefiting from the new systems without intimidation or information asymmetry.\n   \nBy leveraging Blockchain technology within Mount Hope's local community governance structures, it is possible not only to improve transparency and efficiency but also empower residents through increased participation in decisions that directly affect their lives while fostering a stronger sense of community ownership and responsibility.",
            "weight": 0.85,
            "success": true
        },
        {
            "model": "Gemma",
            "response": "## Community Governance and Blockchain for Mount Hope West Virginia\n\n**Community governance** is a framework that empowers and involves all members of a community in decision-making. This can be achieved through various means, including:\n\n* **Town halls and community meetings**\n* **Online platforms**\n* **Advisory committees**\n* **Citizen juries**\n\n**Blockchain** is a distributed ledger technology that can be used to create a secure and transparent record of all community decisions. This can make the decision-making process more efficient and allow all community members to track the progress of the project.\n\n**Benefits of implementing community governance and blockchain in Mount Hope West Virginia:**\n\n* **Increased transparency and accountability:** Blockchain can make the decision-making process more transparent and accountable by providing a secure and immutable record of all votes and proposals.\n* **Improved decision-making:** Blockchain can help to improve decision-making by providing a platform for community members to share their input and ideas.\n* **Reduced costs:** Blockchain can help to reduce costs by automating certain processes, such as voting and record-keeping.\n* **Increased participation:** Blockchain can encourage more participation by providing a safe and convenient way for community members to vote and offer input.\n* **Empowerment of community members:** By giving them a direct say in the decision-making process, blockchain can empower community members and give them a greater sense of ownership over their community.\n\n**Challenges to implementing community governance and blockchain in Mount Hope West Virginia:**\n\n* **Technological literacy:** Some community members may not be familiar with blockchain technology.\n* **Cybersecurity risks:** Blockchain technology is still a relatively new technology, and there is a risk that it could be hacked.\n* **Cost:** Implementing blockchain technology can be expensive, and it is important to consider the costs of implementation and maintenance.\n* **Resistance to change:** Some community members may be resistant to change and may not be willing to participate in a new governance structure.\n\n**Conclusion:**\n\nCommunity governance and blockchain are two powerful tools that can be used to improve the governance of Mount Hope West Virginia. By leveraging these technologies, community members can work together to make better decisions and create a more transparent and accountable community.\n\n**Additional resources:**\n\n* The Center for Digital Democracy: A Framework for Citizen Participation in Local Government\n* The World Bank: Blockchain and Decentralized Governance\n* The United Nations Development Program: Using Blockchain to Promote Sustainable Development",
            "weight": 0.8,
            "success": true
        },
        {
            "model": "Orca-Mini",
            "response": " I'm sorry, but I would need more specific information to provide a comprehensive answer to your question. Could you please provide more details about what you are looking to achieve with community governance and blockchain in Mount Hope West Virginia?",
            "weight": 0.8,
            "success": true
        }
    ],
    "processing_time": 27.72933006286621
}

=== 2. DIRECT 4021 CHAT CHECK (RAG BRIDGE) ===
{
    "response": "Mount Hope, West Virginia is a community that could potentially benefit from the principles of decentralized decision-making facilitated by blockchain technology. Implementing such an innovative approach to local government may enhance transparency, accountability, and citizen engagement in several ways: 1. **Smart Contracts for Community Projects** - Blockchain can enable the creation of smart contracts that automatically execute when certain conditions are met without the need for intermediaries. These could manage funds or resources dedicated to community projects such as park maintenance, street repairs, and local events. For instance, a blockchain system in Mount Hope might hold municipal bonds on-chain with terms directly related to service improvements visible from user interfaces accessible by residents. 2. **Transparent Budget Allocation** - The government could use smart contracts or distributed ledger technology (DLT) for transparent and immutable budget tracking, allowing citizens real-time access to understand how public funds are being spent. This system would reduce corruption risks as it becomes difficult to misappropriate funds when all transactions are recorded on a blockchain with timestamped entries accessible by the community members themselves through secure wallets or interfaces designed for this purpose. 3. extranet-based participatory budgeting - To further involve citizens, Mount Hope could establish an online platform where residents propose projects and vote using their digital identities verified within a DLT framework. This method can democratize decision-making by ensuring that only eligible participants have the right to initiate proposals or votes on community funds allocation through multi-signature wallets, which require consensus from multiple holders for significant decisions like infrastructure spending. 4. **Decentralized Organizational Structure** - By utilizing a DAO (Decentralized Autonomous Organization), Mount Hope can operate with minimal bureaucracy and incentivize its members to be actively involved in decision-making processes, reducing the potential for power imbalances within traditional governance structures. The community's bylaws could themselves be encoded into smart contracts on a blockchain that automatically enforces rules without needing extensive municipal oversight or intervention, making routine administrative tasks more efficient and less prone to error or manipulation. 5. **Voting Integrity** - Blockchain can provide secure identity verification methods for residents wishing to vote in local elections while preserving voter privacy through zero-knowledge proofs \u2013 a cryptographic technique that enables someone to prove they have certain information (like voting eligibility) without revealing the actual data. This would protect against double-voting and ensure one person, one vote within the community governance ecosystem of Mount Hope. 6. **Token Economy for Civic Participation** - Residents could earn tokens representing their contributions to local government or civic activities which can then be traded in a token economy platform created on-chain. This system not only rewards active participation but also aligns economic interests with the wellbeing of Mount Hope, potentially motivating residents and businesses alike to contribute more significantly towards community improvement efforts \u2013 whether through volunteerism or direct financial support for public goods funded by local taxation structures that mirror blockchain principles. 7. **Sustainability Accountability** - A tokenization system on a blockchain can be used not just as currency but also an accountable tool to track and reward Mount Hope's sustainability efforts, such as renewable energy projects or green initiatives within the community. Each resident might earn tokens for reducing their carbon footprint in exchange with verified environmental actions through IoT (Internet of Things) devices measuring real-world data that is then recorded on a public ledger accessible to all residents and stakeholders, fostering collective responsibility towards sustainable living practices. By embracing blockchain technology for governance, Mount Hope could not only improve the efficiency and integrity of its local decision-making process but also potentially attract forward-thinking businesses that are interested in communities using cutting-edge technologies to drive societal advancements."
}

=== 3. ORCHESTRATOR 9998 /process CHECK ===
{
    "status": "approved_by_69_dgm_cascade",
    "message": "community governance and blockchain for Mount Hope West Virginia",
    "userid": "cakidd",
    "layers_passed": 3,
    "validators_engaged": 69,
    "timestamp": "2026-07-03T23:46:45.681258",
    "layer1": {
        "passed": true,
        "approvals": 8,
        "abstains": 15,
        "rejects": 0,
        "failures": 0,
        "details": [
            {
                "port": 5101,
                "status_code": 200,
                "vote": "approve",
                "score": 0.61,
                "dgm_id": "01",
                "specialty": "community_governance"
            },
            {
                "port": 5102,
                "status_code": 200,
                "vote": "approve",
                "score": 0.37,
                "dgm_id": "02",
                "specialty": "cooperative_economics"
            },
            {
                "port": 5103,
                "status_code": 200,
                "vote": "abstain",
                "score": 0.25,
                "dgm_id": "03",
                "specialty": "learning_pathways"
            },
            {
                "port": 5104,

=== 4. FULL 9000 -> 9998 -> 4021 PATH ===
{
    "response": "Establishing community governance through the implementation of a decentralized ledger, such as blockchain technology, can significantly enhance transparency, engagement, and trust within any locality including Mount Hope in West Virginia. Here's how this innovative approach could be practically applied: 1. **Citizen Engagement Platform**: Create a user-friendly digital platform where residents of Mount Hope can interact with the town\u2019thre governance model, propose initiatives or vote on community issues directly linked to real blockchain data entries that reflect decisions made and funds allocated. This will ensure transparency in local government operations. 2. **Smart Contracts for Decision Making**: Introduce smart contracts into the governance system, where certain tasks or services once voted upon by community members are automatically funded via blockchain-based transactions without intermediaries and with clear audit trails of each transaction to ensure accountability. 3. **Decentralized Governance Models**: Encourage local committees that work together in a decentralized fashion, ensuring no single point of failure or corruption. Decisions are made through consensus mechanisms on the blockchain platform where majority community input shapes governance outcomes for projects such as park improvements, festival funding, and more. 4. **Crowdfunded Projects**: Utilize a decentralized finance (DeFi) system to allow residents of Mount Hope who are interested in particular community improvement initiatives can contribute directly via the blockchain platform without requiring traditional bank accounts or dealing with bureaucratic financial processing delays and costs. 5. **Blockchain-Enabled Transparency**: Implement a public ledger for all municipal expenditures, contracts awarded to businesses within Mount Hope, as well as detailed reports on the outcomes of these projects directly available on the blockchain platform so that residents can easily access and verify this information at any time. 6. **Community Treasury**: Establish a localized community treasury where funds are raised through donations or DeFi mechanisms within Mount Hope, with clear records of all transactions stored immutably on the blockchain to prevent fraud and ensure that everyone knows exactly how every dollar is spent. 7. **Transparent Political Processes**Resident Experts and Representatives Panel**: Form a panel consisting of community experts who are incentivized through blockchain token rewards for their time spent participating in town hall meetings, advising committees, or helping to maintain the decentralized governance ecosystem itself without monetary compensation. By adopting such technologies as part of its community-governance approach, Mount Hope could become a model small town for civic engagement and participation through blockchain technology by allowing residents full accessibility, transparency in local government dealings, direct financial contributions towards their initiatives without reliance on the traditional banking system or bureaucratic red tape.",
    "validated_by": "69_dgm_cascade+rag_bridge",
    "status": "approved_by_69_dgm_cascade",
    "message": "community governance and blockchain for Mount Hope West Virginia",
    "userid": "cakidd",
    "connectors_used": [],
    "verdict": {
        "status": "approved_by_69_dgm_cascade",
        "message": "community governance and blockchain for Mount Hope West Virginia",
        "userid": "cakidd",
        "layers_passed": 3,
        "validators_engaged": 69,
        "timestamp": "2026-07-03T23:46:45.800514",
        "layer1": {
            "passed": true,
            "approvals": 8,
            "abstains": 15,
            "rejects": 0,
            "failures": 0,
            "details": [
                {
                    "port": 5101,
                    "status_code": 200,
                    "vote": "approve",
                    "score": 0.61,
                    "dgm_id": "01",
                    "specialty": "community_governance"
                },
                {
                    "port": 5102,
                    "status_code": 200,
                    "vote": "approve",
                    "score": 0.37,
                    "dgm_id": "02",
                    "specialty": "cooperative_economics"
                },
                {
                    "port": 5103,
                    "status_code": 200,
                    "vote": "abstain",
                    "score": 0.25,
                    "dgm_id": "03",
                    "specialty": "learning_pathways"
                },
                {
                    "port": 5104,
                    "status_code": 200,
                    "vote": "abstain",
                    "score": 0.25,
                    "dgm_id": "04",
                    "specialty": "health_equity"
                },
                {
                    "port": 5105,
                    "status_code": 200,
                    "vote": "abstain",
                    "score": 0.25,
                    "dgm_id": "05",
                    "specialty": "housing_stability"

=== 5. LAST 20 LINES FROM EACH SERVICE ===

--- jarvis-consensus-4010.service ---
Jul 03 19:42:54 cakidd-Legion-5-16IRX9 gunicorn[2721173]: INFO:services.ms_jarvis_consensus_service:🔍 DEBUG: Received message (first 200 chars): 'community governance and blockchain for Mount Hope West Virginia'
Jul 03 19:42:58 cakidd-Legion-5-16IRX9 gunicorn[2721173]: INFO:httpx:HTTP Request: POST http://localhost:11434/api/generate "HTTP/1.1 200 OK"
Jul 03 19:43:07 cakidd-Legion-5-16IRX9 gunicorn[2721173]: INFO:httpx:HTTP Request: POST http://localhost:11434/api/generate "HTTP/1.1 200 OK"
Jul 03 19:46:02 cakidd-Legion-5-16IRX9 gunicorn[2721173]: INFO:services.ms_jarvis_consensus_service:🔍 DEBUG: Received message (first 200 chars): 'community governance and blockchain for Mount Hope West Virginia'
Jul 03 19:46:06 cakidd-Legion-5-16IRX9 gunicorn[2721173]: INFO:httpx:HTTP Request: POST http://localhost:11434/api/generate "HTTP/1.1 200 OK"
Jul 03 19:46:08 cakidd-Legion-5-16IRX9 gunicorn[2721173]: INFO:httpx:HTTP Request: POST http://localhost:11434/api/generate "HTTP/1.1 200 OK"
Jul 03 19:46:29 cakidd-Legion-5-16IRX9 gunicorn[2721173]: INFO:httpx:HTTP Request: POST http://localhost:11434/api/generate "HTTP/1.1 200 OK"
Jul 03 19:46:30 cakidd-Legion-5-16IRX9 gunicorn[2721173]: INFO:services.ms_jarvis_consensus_service:🔍 DEBUG: Received message (first 200 chars): 'community governance and blockchain for Mount Hope West Virginia'
Jul 03 19:46:39 cakidd-Legion-5-16IRX9 gunicorn[2721173]: INFO:httpx:HTTP Request: POST http://localhost:11434/api/generate "HTTP/1.1 200 OK"
Jul 03 19:46:45 cakidd-Legion-5-16IRX9 gunicorn[2721173]: INFO:httpx:HTTP Request: POST http://localhost:11434/api/generate "HTTP/1.1 200 OK"
Jul 03 19:46:45 cakidd-Legion-5-16IRX9 gunicorn[2721173]: INFO:services.ms_jarvis_consensus_service:🔍 DEBUG: Received message (first 200 chars): 'community governance and blockchain for Mount Hope West Virginia'
Jul 03 19:46:54 cakidd-Legion-5-16IRX9 gunicorn[2721173]: INFO:httpx:HTTP Request: POST http://localhost:11434/api/generate "HTTP/1.1 200 OK"
Jul 03 19:46:58 cakidd-Legion-5-16IRX9 gunicorn[2721173]: INFO:httpx:HTTP Request: POST http://localhost:11434/api/generate "HTTP/1.1 200 OK"

--- jarvis-consciousness-4021.service ---
Jul 03 19:42:54 cakidd-Legion-5-16IRX9 python3[2721176]: INFO:ms_jarvis_consciousness_enhancement_production:🧠 → Consensus 4010: community governance and blockchain for Mount Hope West Virg
Jul 03 19:43:07 cakidd-Legion-5-16IRX9 python3[2721176]: INFO:httpx:HTTP Request: POST http://127.0.0.1:4010/consensus "HTTP/1.1 200 OK"
Jul 03 19:43:07 cakidd-Legion-5-16IRX9 python3[2721176]: INFO:     127.0.0.1:53484 - "POST /chat HTTP/1.1" 200 OK
Jul 03 19:46:30 cakidd-Legion-5-16IRX9 python3[2721176]: INFO:ms_jarvis_consciousness_enhancement_production:🧠 → Consensus 4010: community governance and blockchain for Mount Hope West Virg
Jul 03 19:46:45 cakidd-Legion-5-16IRX9 python3[2721176]: INFO:httpx:HTTP Request: POST http://127.0.0.1:4010/consensus "HTTP/1.1 200 OK"
Jul 03 19:46:45 cakidd-Legion-5-16IRX9 python3[2721176]: INFO:     127.0.0.1:40604 - "POST /chat HTTP/1.1" 200 OK
Jul 03 19:46:45 cakidd-Legion-5-16IRX9 python3[2721176]: INFO:ms_jarvis_consciousness_enhancement_production:🧠 → Consensus 4010: community governance and blockchain for Mount Hope West Virg
Jul 03 19:46:58 cakidd-Legion-5-16IRX9 python3[2721176]: INFO:httpx:HTTP Request: POST http://127.0.0.1:4010/consensus "HTTP/1.1 200 OK"
Jul 03 19:46:58 cakidd-Legion-5-16IRX9 python3[2721176]: INFO:     127.0.0.1:48240 - "POST /chat HTTP/1.1" 200 OK

--- msjarvis-69dgm-orchestrator-9998.service ---
-- No entries --

--- msjarvis-69dgm-9000.service ---
Jul 03 19:44:03 cakidd-Legion-5-16IRX9 gunicorn[2728135]: [2026-07-03 19:44:03 -0400] [2728135] [INFO] Listening at: http://0.0.0.0:9000 (2728135)
Jul 03 19:44:03 cakidd-Legion-5-16IRX9 gunicorn[2728135]: [2026-07-03 19:44:03 -0400] [2728135] [INFO] Using worker: uvicorn_worker.UvicornWorker
Jul 03 19:44:03 cakidd-Legion-5-16IRX9 gunicorn[2728144]: [2026-07-03 19:44:03 -0400] [2728144] [INFO] Booting worker with pid: 2728144
Jul 03 19:44:03 cakidd-Legion-5-16IRX9 gunicorn[2728145]: [2026-07-03 19:44:03 -0400] [2728145] [INFO] Booting worker with pid: 2728145
Jul 03 19:44:03 cakidd-Legion-5-16IRX9 gunicorn[2728135]: [2026-07-03 19:44:03 -0400] [2728135] [INFO] Control socket listening at /home/cakidd/.gunicorn/gunicorn.ctl
Jul 03 19:44:04 cakidd-Legion-5-16IRX9 gunicorn[2728144]: INFO:9000_69DGM_Bridge:🧬 Loaded 0 active DGM connectors from /mnt/spiritual_drive/msjarvis-rebuild/services/dgm_connectors_active.json
Jul 03 19:44:04 cakidd-Legion-5-16IRX9 gunicorn[2728144]: [2026-07-03 19:44:04 -0400] [2728144] [INFO] Started server process [2728144]
Jul 03 19:44:04 cakidd-Legion-5-16IRX9 gunicorn[2728144]: [2026-07-03 19:44:04 -0400] [2728144] [INFO] Waiting for application startup.
Jul 03 19:44:04 cakidd-Legion-5-16IRX9 gunicorn[2728144]: [2026-07-03 19:44:04 -0400] [2728144] [INFO] Application startup complete.
Jul 03 19:44:04 cakidd-Legion-5-16IRX9 gunicorn[2728145]: INFO:9000_69DGM_Bridge:🧬 Loaded 0 active DGM connectors from /mnt/spiritual_drive/msjarvis-rebuild/services/dgm_connectors_active.json
Jul 03 19:44:04 cakidd-Legion-5-16IRX9 gunicorn[2728145]: [2026-07-03 19:44:04 -0400] [2728145] [INFO] Started server process [2728145]
Jul 03 19:44:04 cakidd-Legion-5-16IRX9 gunicorn[2728145]: [2026-07-03 19:44:04 -0400] [2728145] [INFO] Waiting for application startup.
Jul 03 19:44:04 cakidd-Legion-5-16IRX9 gunicorn[2728145]: [2026-07-03 19:44:04 -0400] [2728145] [INFO] Application startup complete.
Jul 03 19:46:45 cakidd-Legion-5-16IRX9 gunicorn[2728145]: INFO:9000_69DGM_Bridge:🧠 Chat message from cakidd: routing through 69 DGMs
Jul 03 19:46:45 cakidd-Legion-5-16IRX9 gunicorn[2728145]: INFO:httpx:HTTP Request: POST http://127.0.0.1:9998/process "HTTP/1.1 200 OK"
Jul 03 19:46:45 cakidd-Legion-5-16IRX9 gunicorn[2728145]: INFO:9000_69DGM_Bridge:✅ 69-DGM orchestrator responded with status=approved_by_69_dgm_cascade
Jul 03 19:46:45 cakidd-Legion-5-16IRX9 gunicorn[2728145]: INFO:9000_69DGM_Bridge:✅ Message approved by 69 validators - proceeding to RAG bridge
Jul 03 19:46:45 cakidd-Legion-5-16IRX9 gunicorn[2728145]: INFO:9000_69DGM_Bridge:🔗 Calling 69-DGM RAG bridge at http://127.0.0.1:4021/chat for user=cakidd
Jul 03 19:46:58 cakidd-Legion-5-16IRX9 gunicorn[2728145]: INFO:httpx:HTTP Request: POST http://127.0.0.1:4021/chat "HTTP/1.1 200 OK"
Jul 03 19:46:58 cakidd-Legion-5-16IRX9 gunicorn[2728145]: INFO:9000_69DGM_Bridge:✅ 69-DGM RAG bridge responded successfully

=== SMOKETEST COMPLETE ===
(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:/mnt/spiritual_drive/msjarvis-rebuild$ 

