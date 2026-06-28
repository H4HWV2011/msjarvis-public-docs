(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:/mnt/nvme1/msjarvis-rebuild/services$ ss -ltnp | grep -E ':4010|:4020|:4021|:11434'
curl -sS http://127.0.0.1:4010/consensus -H "Content-Type: application/json" -d '{"message":"system verification","min_models":2}' | python3 -m json.tool
curl -sS http://127.0.0.1:4021/consciousness/enhance -H "Content-Type: application/json" -d '{"message":"system verification","wv_context":{"response":"WV ensemble says: system check passed."}}' | python3 -m json.tool
curl -sS http://127.0.0.1:4020/chat -H "Content-Type: application/json" -d '{"message":"system verification"}' | python3 -m json.tool
LISTEN 0      2048         0.0.0.0:4021       0.0.0.0:*    users:(("python3",pid=1045028,fd=13))        
LISTEN 0      2048         0.0.0.0:4020       0.0.0.0:*    users:(("python3",pid=1077156,fd=14))        
LISTEN 0      2048         0.0.0.0:4010       0.0.0.0:*    users:(("python3",pid=1032756,fd=13))        
LISTEN 0      4096       127.0.0.1:11434      0.0.0.0:*                                                 
LISTEN 0      5         172.17.0.1:11434      0.0.0.0:*                                                 
LISTEN 0      5         172.18.0.1:11434      0.0.0.0:*                                                 
{
    "consensus": "Sure, I can help with that. How can I assist you with verifying the system? Please provide me with more details about what you would like to verify and how you would like me to help.",
    "models_consulted": 2,
    "successful_responses": 1,
    "responses": [
        {
            "model": "Gemma",
            "response": "Sure, I can help with that. How can I assist you with verifying the system? \n\nPlease provide me with more details about what you would like to verify and how you would like me to help.",
            "weight": 0.8,
            "success": true
        }
    ],
    "processing_time": 45.03319430351257
}
{
    "response": "For system verification, we would need to define the specific context and what needs to be verified. However, here's a general outline for conducting system verification: 1. **Define System Requirements**: Clearly state all requirements that the system must meet in terms of functionality, performance, security, usability, etc. This often starts with input from stakeholders and refinement into formal specifications like user stories or use cases. 2. **Develop Test Cases**: Based on these requirements, develop test cases for each requirement to be verified. Ensure that the tests cover all possible scenarios including edge cases which can reveal hidden defects. 3. **Set Up a Test Environment**: Create an environment where you can control and monitor the testing process without affecting live operations (if applicable). This may involve setting up servers, databases, network configurations, etc., that mimic real-world operating conditions as closely as possible. 4. **Automate or Conduct Manual Tests**: Depending on resources available, run tests through automated scripts where appropriate to save time and eliminate human error for repetitive tasks; otherwise, perform manual testing especially when exploratory approaches are needed or the environment cannot be easily replicated in a lab setting. 5. **Perform Rigorous Testing**: Execute all test cases while logging results meticulously. This might include functional tests, performance benchmarks, security audits (like penetration testing and vulnerability scanning), usability studies, etc. Record any failures or bugs encountered for resolution purposes. 6. **Review Results**: Evaluate the outcome of your verification process to understand if the system meets its requirements with acceptable levels of risk as defined by industry standards such as ISO/IEC 25010 (System and Software Quality Requirements). Identify any deficiencies in meeting quality attributes. 7. **Report Findings**: Document all findings, including failed test cases along with their respective reasons for failure if available from logs or debugging sessions. Provide a comprehensive report to the stakeholders and development team detailing what needs further work before release goes live (if applicable). 8. **Perform Regression Testing**: If changes are made based on feedback, run regression tests to ensure that new code has not introduced any bugs or regressions in previously tested scenarios. This helps maintain the integrity of the system over time after modifications have been implemented. 9. **Validate Compliance and Security Standards**: Ensure compliance with industry-specific standards for security, privacy (like GDPR), accessibility etc., by conducting appropriate assessments or audits as required. 10. **Gather Feedback & Iterate**: Share the results of your verification process with stakeholders to obtain feedback and refine test cases if necessary, then iterate until all requirements are met satisfactorily before finalizing any deployment decisions or releases into production (if not done so already). System verification is an iterative and comprehensive process that often requires multiple rounds of testing with the continuous involvement of developers, stakeholders, quality assurance teams, and possibly third-party auditors.",
    "consciousness_analysis": {},
    "processing_time": 9.984633922576904,
    "timestamp": "2026-06-27T20:34:17.687296"
}
{
    "response": "To conduct a system verification, follow these steps: 1. Define the System Specifications - Determine what you are testing by identifying all components and their interactions within the larger system. This includes hardware, software, user interfaces, communication protocols, etc. Ensure that this is documented clearly in an official specification document if one exists. 2. Establish Test Criteria - Decide on acceptance criteria to measure how well the system meets its requirements. These should be detailed and measurable against predefined benchmarks for performance, functionality, security, usability, etc. Create a verification plan outlining all tests needed based on these criteria. 3. Choose Test Methods - Select appropriate testing methodologies (e.g., functional testing, integration testing) that will effectively evaluate the system against your established test criteria in real-world scenarios or simulated environments where necessary. 4. Prepare for Execution \u2013 Set up a controlled environment with all required tools and technologies needed to conduct tests without disrupting production systems if they exist alongside development ones, unless it's safe and part of the verification plan. Ensure data collection methods are in place for capturing test results accurately (logs, screenshots, video recordings). 5. Conduct Test Execution \u2013 Begin executing tests while carefully documenting each step taken during testing to reproduce any issues or bugs identified throughout execution phases consistently and effectively using issue-tracking systems when necessary. Record all outcomes of the verification process against expected results for later analysis. 6. Analyze Results - Compare test findings with your acceptance criteria, looking at both passed tests and failed ones to identify patterns or commonalities that may indicate deeper issues in specific areas like particular hardware components or software modules within larger subsystems if applicable. Pay attention not only towards quantitative metrics but also qualitative user experience aspects where possible for a comprehensive verification result set. 7. Report Findings - Create an executive summary and detailed report outlining the results, including pass/fail statuses per test case with accompanying evidence such as screenshots or logs to substantiate your findings backed by data analysis techniques like control charts for trends over time if needed. 8. Review & Adjust - Present verification reports and discussions within cross-functional teams (development, QA, product managers) regarding discrepancies between expected outcomes versus observed ones from tests conducted so far along with identified improvements based on the results obtained during testing phases for continuous improvement processes in an agile environment. 9. Plan Next Steps - Based upon discussions and agreed-upon action items following review & adjustment phase, schedule future test sessions to retest areas of concern uncovered through verification activities thus far alongside other system elements not yet tested thoroughly enough using the same methods previously selected during initial planning stages if needed after revising methodologies accordingly per feedback received from these discussions. 10. Monitor Post-Deployment Performance \u2013 Implement monitoring tools to observe real user interactions with live deployments once approved for release so any emerging issues can be identified promptly and addressed timely without compromising system stability/reliability further down the road henceforth, thus ensuring ongoing verification beyond initial testing phases towards continuous delivery pipelines under modern DevOps practices where appropriate.",
    "consciousness_synthesis": {
        "method": "unified_bridge",
        "layers_analyzed": 0,
        "layer_details": [],
        "integration": "",
        "personality_voice": ""
    },
    "processing_metadata": {
        "enhancement_time": 9.179338216781616,
        "total_time": 9.20113468170166,
        "timestamp": "2026-06-27T20:34:26.909882",
        "bridge_version": "2.0",
        "unified": true
    }
}
(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:/mnt/nvme1/msjarvis-rebuild/services$ cd /mnt/nvme1/msjarvis-rebuild/services && \
grep -RniE '\.get\([a-zA-Z_][a-zA-Z0-9_]*,' . --include='*.py'
./rag_query_router.py:312:    path = SERVICE_ENDPOINTS.get(service_name, "/query")
./domain_service_router.py:51:                    response = requests.get(local_url, timeout=30, **kwargs)
./enhanced_learner_concept.py:26:            topics[topic] = topics.get(topic, 0) + 1
./enhanced_learner_concept.py:52:            locations[location_key] = locations.get(location_key, 0) + 1
./egeria_web_ui_dynamic.py:174:    return jsonify(query_status.get(query_id, {'status': 'not_found'}))
./ms_jarvis_web_research.py:141:        resp = requests.get(url, headers=headers, timeout=10)
./gis_rag_service.py:58:    resp = await client.get(url, params={"limit": 100, "offset": 0})
./topic_entanglement.py:36:        graph[current_topic][t] = graph[current_topic].get(t, 0.0) + step
./topic_entanglement.py:37:        graph[t][current_topic] = graph[t].get(current_topic, 0.0) + step
./topic_entanglement.py:45:    neighbors = graph.get(topic, {})
./ms_jarvis_location_services.py:215:        return {category: LOCAL_RESOURCES.get(category, [])}
./ms_jarvis_substack_reader.py:29:            response = await client.get(api_url, timeout=10)
./ai_server_11llm_OPTIMIZED.py:83:    return endpoints.get(service_name, "/process")
./ai_server_11llm_OPTIMIZED.py:1248:            action_types[atype] = action_types.get(atype, 0) + 1
./port_manager_fixed.py:68:        return registry.get(service_name, {}).get("port")
./ms_jarvis_email_service.py:112:        r = await client.get(url, headers=headers)
./port_manager.py:68:        return registry.get(service_name, {}).get("port")
./ms_jarvis_phi_probe.py:86:            r = await client.get(url, timeout=10.0)
./ms_jarvis_phi_probe.py:99:            r = await client.get(url, timeout=8.0)
./.venv/lib/python3.12/site-packages/anyio/lowlevel.py:174:        token = RunvarToken(self, current_vars.get(self, RunVar.NO_VALUE_SET))
./.venv/lib/python3.12/site-packages/typing_extensions.py:3968:                module = sys.modules.get(module_name, None)
./.venv/lib/python3.12/site-packages/typing_extensions.py:4073:                    module = sys.modules.get(module_name, None)
./.venv/lib/python3.12/site-packages/pip/_vendor/packaging/markers.py:212:    value: Union[str, Undefined] = environment.get(name, _undefined)
./.venv/lib/python3.12/site-packages/pip/_vendor/packaging/version.py:181:        part = _legacy_version_replacement_map.get(part, part)
./.venv/lib/python3.12/site-packages/pip/_vendor/requests/utils.py:876:        proxy = environ_proxies.get(scheme, environ_proxies.get("all"))
./.venv/lib/python3.12/site-packages/pip/_vendor/requests/structures.py:96:        return self.__dict__.get(key, None)
./.venv/lib/python3.12/site-packages/pip/_vendor/requests/structures.py:99:        return self.__dict__.get(key, default)
./.venv/lib/python3.12/site-packages/pip/_vendor/requests/cookies.py:76:        return self._r.headers.get(name, self._new_headers.get(name, default))
./.venv/lib/python3.12/site-packages/pip/_vendor/urllib3/response.py:672:            "in urllib3 v2.1.0. Instead use HTTPResponse.headers.get(name, default).",
./.venv/lib/python3.12/site-packages/pip/_vendor/urllib3/response.py:676:        return self.headers.get(name, default)
./.venv/lib/python3.12/site-packages/pip/_vendor/urllib3/connectionpool.py:1104:    port = port or port_by_scheme.get(scheme, 80)
./.venv/lib/python3.12/site-packages/pip/_vendor/urllib3/_collections.py:65:            evicted_value = self._container.get(key, _Null)
./.venv/lib/python3.12/site-packages/pip/_vendor/urllib3/fields.py:238:            if self.headers.get(sort_key, False):
./.venv/lib/python3.12/site-packages/pip/_vendor/chardet/chardistribution.py:179:            return JOHAB_TO_EUCKR_ORDER_TABLE.get(code, -1)
./.venv/lib/python3.12/site-packages/pip/_vendor/chardet/sbcharsetprober.py:105:            order = char_to_order_map.get(char, CharacterCategory.UNDEFINED)
./.venv/lib/python3.12/site-packages/pip/_vendor/webencodings/__init__.py:83:            python_name = PYTHON_NAMES.get(name, name)
./.venv/lib/python3.12/site-packages/pip/_vendor/cachecontrol/cache.py:40:        return self.data.get(key, None)
./.venv/lib/python3.12/site-packages/pip/_vendor/cachecontrol/serialize.py:55:                header_value = request.headers.get(header, None)
./.venv/lib/python3.12/site-packages/pip/_vendor/cachecontrol/serialize.py:119:            if request.headers.get(header, None) != value:
./.venv/lib/python3.12/site-packages/pip/_vendor/rich/_emoji_replace.py:21:    default_variant_code = variants.get(default_variant, "") if default_variant else ""
./.venv/lib/python3.12/site-packages/pip/_vendor/rich/emoji.py:55:            self._char += self.VARIANTS.get(variant, "")
./.venv/lib/python3.12/site-packages/pip/_vendor/rich/padding.py:87:                Measurement.get(console, options, self.renderable).maximum
./.venv/lib/python3.12/site-packages/pip/_vendor/rich/padding.py:132:        measure_min, measure_max = Measurement.get(console, options, self.renderable)
./.venv/lib/python3.12/site-packages/pip/_vendor/rich/styled.py:34:        return Measurement.get(console, options, self.renderable)
./.venv/lib/python3.12/site-packages/pip/_vendor/rich/align.py:230:        measurement = Measurement.get(console, options, self.renderable)
./.venv/lib/python3.12/site-packages/pip/_vendor/rich/align.py:286:        measurement = Measurement.get(console, options, self.renderable)
./.venv/lib/python3.12/site-packages/pip/_vendor/rich/spinner.py:58:        return Measurement.get(console, options, text)
./.venv/lib/python3.12/site-packages/pip/_vendor/rich/console.py:812:            color_system = _TERM_COLORS.get(colors, ColorSystem.STANDARD)
./.venv/lib/python3.12/site-packages/pip/_vendor/rich/console.py:1283:        measurement = Measurement.get(self, options or self.options, renderable)
./.venv/lib/python3.12/site-packages/pip/_vendor/rich/containers.py:50:            Measurement.get(console, options, renderable)
./.venv/lib/python3.12/site-packages/pip/_vendor/rich/box.py:86:            box = LEGACY_WINDOWS_SUBSTITUTIONS.get(box, box)
./.venv/lib/python3.12/site-packages/pip/_vendor/rich/box.py:99:        return PLAIN_HEADED_SUBSTITUTIONS.get(self, self)
./.venv/lib/python3.12/site-packages/pip/_vendor/rich/constrain.py:36:        measurement = Measurement.get(console, options, self.renderable)
./.venv/lib/python3.12/site-packages/pip/_vendor/distro/distro.py:837:            return table.get(distro_id, distro_id)
./.venv/lib/python3.12/site-packages/pip/_vendor/distro/distro.py:1057:        return self._os_release_info.get(attribute, "")
./.venv/lib/python3.12/site-packages/pip/_vendor/distro/distro.py:1066:        return self._lsb_release_info.get(attribute, "")
./.venv/lib/python3.12/site-packages/pip/_vendor/distro/distro.py:1075:        return self._distro_release_info.get(attribute, "")
./.venv/lib/python3.12/site-packages/pip/_vendor/distro/distro.py:1084:        return self._uname_info.get(attribute, "")
./.venv/lib/python3.12/site-packages/pip/_vendor/pkg_resources/__init__.py:427:    return {'PowerPC': 'ppc', 'Power_Macintosh': 'ppc'}.get(machine, machine)
./.venv/lib/python3.12/site-packages/pip/_vendor/pkg_resources/__init__.py:869:                    requirers = required_by.get(req, None)
./.venv/lib/python3.12/site-packages/pip/_vendor/pkg_resources/__init__.py:1026:            for extra in self.get(req, ()) + (extras or (None,))
./.venv/lib/python3.12/site-packages/pip/_vendor/pkg_resources/__init__.py:1100:        return self._distmap.get(distribution_key, [])
./.venv/lib/python3.12/site-packages/pip/_vendor/pkg_resources/__init__.py:2376:        for package in _namespace_packages.get(parent, ()):
./.venv/lib/python3.12/site-packages/pip/_vendor/pkg_resources/__init__.py:2824:        deps.extend(dm.get(None, ()))
./.venv/lib/python3.12/site-packages/pip/_vendor/pkg_resources/__init__.py:2942:            return ep_map.get(group, {})
./.venv/lib/python3.12/site-packages/pip/_vendor/pygments/style.py:88:                styledefs = obj.styles.get(token, '').split()
./.venv/lib/python3.12/site-packages/pip/_vendor/pygments/style.py:96:                for styledef in obj.styles.get(token, '').split():
./.venv/lib/python3.12/site-packages/pip/_vendor/pygments/util.py:45:    string = options.get(optname, default)
./.venv/lib/python3.12/site-packages/pip/_vendor/pygments/util.py:56:    Intuitively, this is `options.get(optname, default)`, but restricted to
./.venv/lib/python3.12/site-packages/pip/_vendor/pygments/util.py:66:    string = options.get(optname, default)
./.venv/lib/python3.12/site-packages/pip/_vendor/pygments/util.py:87:    string = options.get(optname, default)
./.venv/lib/python3.12/site-packages/pip/_vendor/pygments/util.py:105:    val = options.get(optname, default)
./.venv/lib/python3.12/site-packages/pip/_vendor/pygments/formatters/terminal256.py:206:        index = self.best_match.get(color, None)
./.venv/lib/python3.12/site-packages/pip/_vendor/pygments/filters/__init__.py:824:            opt = options.get(name, False)
./.venv/lib/python3.12/site-packages/pip/_vendor/pygments/plugin.py:68:        return groups.get(group_name, [])
./.venv/lib/python3.12/site-packages/pip/_vendor/resolvelib/structs.py:98:        return itertools.chain(self._accessor(v), self._appends.get(k, ()))
./.venv/lib/python3.12/site-packages/pip/_vendor/pyparsing/results.py:215:            self._tokdict[k] = self._tokdict.get(k, list()) + [v]
./.venv/lib/python3.12/site-packages/pip/_vendor/pyparsing/results.py:221:            self._tokdict[k] = self._tokdict.get(k, list()) + [
./.venv/lib/python3.12/site-packages/pip/_vendor/distlib/util.py:1074:        return iter(self._subscribers.get(event, ()))
./.venv/lib/python3.12/site-packages/pip/_vendor/distlib/util.py:1117:            for p in set(self._preds.get(node, ())):
./.venv/lib/python3.12/site-packages/pip/_vendor/distlib/util.py:1119:            for s in set(self._succs.get(node, ())):
./.venv/lib/python3.12/site-packages/pip/_vendor/distlib/util.py:1172:                preds = self._preds.get(step, ())
./.venv/lib/python3.12/site-packages/pip/_vendor/distlib/util.py:1861:                        result['username'] = config.get(server, 'username')
./.venv/lib/python3.12/site-packages/pip/_vendor/distlib/util.py:1869:                                result[key] = config.get(server, key)
./.venv/lib/python3.12/site-packages/pip/_vendor/distlib/util.py:1886:                    repository = config.get(server, 'repository')
./.venv/lib/python3.12/site-packages/pip/_vendor/distlib/util.py:1890:                    'username': config.get(server, 'username'),
./.venv/lib/python3.12/site-packages/pip/_vendor/distlib/util.py:1891:                    'password': config.get(server, 'password'),
./.venv/lib/python3.12/site-packages/pip/_vendor/distlib/compat.py:837:            'od.setdefault(k[,d]) -> od.get(k,d), also set od[k]=d if k not in od'
./.venv/lib/python3.12/site-packages/pip/_vendor/distlib/compat.py:947:            value = dict.get(self, key, default)
./.venv/lib/python3.12/site-packages/pip/_vendor/distlib/compat.py:1113:                    converter = self.value_converters.get(prefix, None)
./.venv/lib/python3.12/site-packages/pip/_vendor/distlib/version.py:592:            p = _VERSION_REPLACE.get(p, p)
./.venv/lib/python3.12/site-packages/pip/_vendor/distlib/locators.py:399:            result.download_urls = versions.get('urls', {}).get(version, set())
./.venv/lib/python3.12/site-packages/pip/_vendor/distlib/metadata.py:300:        return _ATTR2FIELD.get(name, name)
./.venv/lib/python3.12/site-packages/pip/_vendor/distlib/metadata.py:547:                value = self.get(field, None)
./.venv/lib/python3.12/site-packages/pip/_vendor/distlib/metadata.py:737:                    result = self._data.get(key, value)
./.venv/lib/python3.12/site-packages/pip/_vendor/distlib/metadata.py:749:                                result = d.get(key, value)
./.venv/lib/python3.12/site-packages/pip/_vendor/distlib/metadata.py:755:                                result = d.get(key, value)
./.venv/lib/python3.12/site-packages/pip/_vendor/platformdirs/unix.py:194:        media_dir = os.environ.get(env_var, "").strip()
./.venv/lib/python3.12/site-packages/pip/_internal/network/download.py:117:    resp = session.get(target_url, headers=HEADERS, stream=True)
./.venv/lib/python3.12/site-packages/pip/_internal/utils/hashes.py:68:        return hex_digest in self._allowed.get(hash_name, [])
./.venv/lib/python3.12/site-packages/pip/_internal/utils/temp_dir.py:66:        return self._should_delete.get(kind, True)
./.venv/lib/python3.12/site-packages/pip/_internal/build_env.py:139:            name: os.environ.get(name, None)
./.venv/lib/python3.12/site-packages/pip/_internal/resolution/resolvelib/provider.py:176:        requested_order = self._user_requested.get(identifier, math.inf)
./.venv/lib/python3.12/site-packages/pip/_internal/resolution/resolvelib/factory.py:441:        incompat_ids = {id(c) for c in incompatibilities.get(identifier, ())}
./.venv/lib/python3.12/site-packages/pip/_internal/resolution/resolvelib/resolver.py:262:        last_known_parent_count = weights.get(node, 0)
./.venv/lib/python3.12/site-packages/requests/utils.py:874:        proxy = environ_proxies.get(scheme, environ_proxies.get("all"))
./.venv/lib/python3.12/site-packages/requests/structures.py:96:        return self.__dict__.get(key, None)
./.venv/lib/python3.12/site-packages/requests/structures.py:99:        return self.__dict__.get(key, default)
./.venv/lib/python3.12/site-packages/requests/cookies.py:76:        return self._r.headers.get(name, self._new_headers.get(name, default))
./.venv/lib/python3.12/site-packages/urllib3/response.py:679:        return self.headers.get(name, default)
./.venv/lib/python3.12/site-packages/urllib3/connectionpool.py:1130:    port = port or port_by_scheme.get(scheme, 80)
./.venv/lib/python3.12/site-packages/urllib3/fields.py:299:            if self.headers.get(sort_key, False):
./.venv/lib/python3.12/site-packages/h11/_state.py:349:            changes = STATE_TRIGGERED_TRANSITIONS.get(joint_state, {})
./.venv/lib/python3.12/site-packages/httpx/_models.py:827:        error_type = error_types.get(status_class, "Invalid status code")
./.venv/lib/python3.12/site-packages/httpcore/_async/socks_proxy.py:66:        requested = AUTH_METHODS.get(auth_method, "UNKNOWN")
./.venv/lib/python3.12/site-packages/httpcore/_sync/socks_proxy.py:66:        requested = AUTH_METHODS.get(auth_method, "UNKNOWN")
./.venv/lib64/python3.12/site-packages/anyio/lowlevel.py:174:        token = RunvarToken(self, current_vars.get(self, RunVar.NO_VALUE_SET))
./.venv/lib64/python3.12/site-packages/typing_extensions.py:3968:                module = sys.modules.get(module_name, None)
./.venv/lib64/python3.12/site-packages/typing_extensions.py:4073:                    module = sys.modules.get(module_name, None)
./.venv/lib64/python3.12/site-packages/pip/_vendor/packaging/markers.py:212:    value: Union[str, Undefined] = environment.get(name, _undefined)
./.venv/lib64/python3.12/site-packages/pip/_vendor/packaging/version.py:181:        part = _legacy_version_replacement_map.get(part, part)
./.venv/lib64/python3.12/site-packages/pip/_vendor/requests/utils.py:876:        proxy = environ_proxies.get(scheme, environ_proxies.get("all"))
./.venv/lib64/python3.12/site-packages/pip/_vendor/requests/structures.py:96:        return self.__dict__.get(key, None)
./.venv/lib64/python3.12/site-packages/pip/_vendor/requests/structures.py:99:        return self.__dict__.get(key, default)
./.venv/lib64/python3.12/site-packages/pip/_vendor/requests/cookies.py:76:        return self._r.headers.get(name, self._new_headers.get(name, default))
./.venv/lib64/python3.12/site-packages/pip/_vendor/urllib3/response.py:672:            "in urllib3 v2.1.0. Instead use HTTPResponse.headers.get(name, default).",
./.venv/lib64/python3.12/site-packages/pip/_vendor/urllib3/response.py:676:        return self.headers.get(name, default)
./.venv/lib64/python3.12/site-packages/pip/_vendor/urllib3/connectionpool.py:1104:    port = port or port_by_scheme.get(scheme, 80)
./.venv/lib64/python3.12/site-packages/pip/_vendor/urllib3/_collections.py:65:            evicted_value = self._container.get(key, _Null)
./.venv/lib64/python3.12/site-packages/pip/_vendor/urllib3/fields.py:238:            if self.headers.get(sort_key, False):
./.venv/lib64/python3.12/site-packages/pip/_vendor/chardet/chardistribution.py:179:            return JOHAB_TO_EUCKR_ORDER_TABLE.get(code, -1)
./.venv/lib64/python3.12/site-packages/pip/_vendor/chardet/sbcharsetprober.py:105:            order = char_to_order_map.get(char, CharacterCategory.UNDEFINED)
./.venv/lib64/python3.12/site-packages/pip/_vendor/webencodings/__init__.py:83:            python_name = PYTHON_NAMES.get(name, name)
./.venv/lib64/python3.12/site-packages/pip/_vendor/cachecontrol/cache.py:40:        return self.data.get(key, None)
./.venv/lib64/python3.12/site-packages/pip/_vendor/cachecontrol/serialize.py:55:                header_value = request.headers.get(header, None)
./.venv/lib64/python3.12/site-packages/pip/_vendor/cachecontrol/serialize.py:119:            if request.headers.get(header, None) != value:
./.venv/lib64/python3.12/site-packages/pip/_vendor/rich/_emoji_replace.py:21:    default_variant_code = variants.get(default_variant, "") if default_variant else ""
./.venv/lib64/python3.12/site-packages/pip/_vendor/rich/emoji.py:55:            self._char += self.VARIANTS.get(variant, "")
./.venv/lib64/python3.12/site-packages/pip/_vendor/rich/padding.py:87:                Measurement.get(console, options, self.renderable).maximum
./.venv/lib64/python3.12/site-packages/pip/_vendor/rich/padding.py:132:        measure_min, measure_max = Measurement.get(console, options, self.renderable)
./.venv/lib64/python3.12/site-packages/pip/_vendor/rich/styled.py:34:        return Measurement.get(console, options, self.renderable)
./.venv/lib64/python3.12/site-packages/pip/_vendor/rich/align.py:230:        measurement = Measurement.get(console, options, self.renderable)
./.venv/lib64/python3.12/site-packages/pip/_vendor/rich/align.py:286:        measurement = Measurement.get(console, options, self.renderable)
./.venv/lib64/python3.12/site-packages/pip/_vendor/rich/spinner.py:58:        return Measurement.get(console, options, text)
./.venv/lib64/python3.12/site-packages/pip/_vendor/rich/console.py:812:            color_system = _TERM_COLORS.get(colors, ColorSystem.STANDARD)
./.venv/lib64/python3.12/site-packages/pip/_vendor/rich/console.py:1283:        measurement = Measurement.get(self, options or self.options, renderable)
./.venv/lib64/python3.12/site-packages/pip/_vendor/rich/containers.py:50:            Measurement.get(console, options, renderable)
./.venv/lib64/python3.12/site-packages/pip/_vendor/rich/box.py:86:            box = LEGACY_WINDOWS_SUBSTITUTIONS.get(box, box)
./.venv/lib64/python3.12/site-packages/pip/_vendor/rich/box.py:99:        return PLAIN_HEADED_SUBSTITUTIONS.get(self, self)
./.venv/lib64/python3.12/site-packages/pip/_vendor/rich/constrain.py:36:        measurement = Measurement.get(console, options, self.renderable)
./.venv/lib64/python3.12/site-packages/pip/_vendor/distro/distro.py:837:            return table.get(distro_id, distro_id)
./.venv/lib64/python3.12/site-packages/pip/_vendor/distro/distro.py:1057:        return self._os_release_info.get(attribute, "")
./.venv/lib64/python3.12/site-packages/pip/_vendor/distro/distro.py:1066:        return self._lsb_release_info.get(attribute, "")
./.venv/lib64/python3.12/site-packages/pip/_vendor/distro/distro.py:1075:        return self._distro_release_info.get(attribute, "")
./.venv/lib64/python3.12/site-packages/pip/_vendor/distro/distro.py:1084:        return self._uname_info.get(attribute, "")
./.venv/lib64/python3.12/site-packages/pip/_vendor/pkg_resources/__init__.py:427:    return {'PowerPC': 'ppc', 'Power_Macintosh': 'ppc'}.get(machine, machine)
./.venv/lib64/python3.12/site-packages/pip/_vendor/pkg_resources/__init__.py:869:                    requirers = required_by.get(req, None)
./.venv/lib64/python3.12/site-packages/pip/_vendor/pkg_resources/__init__.py:1026:            for extra in self.get(req, ()) + (extras or (None,))
./.venv/lib64/python3.12/site-packages/pip/_vendor/pkg_resources/__init__.py:1100:        return self._distmap.get(distribution_key, [])
./.venv/lib64/python3.12/site-packages/pip/_vendor/pkg_resources/__init__.py:2376:        for package in _namespace_packages.get(parent, ()):
./.venv/lib64/python3.12/site-packages/pip/_vendor/pkg_resources/__init__.py:2824:        deps.extend(dm.get(None, ()))
./.venv/lib64/python3.12/site-packages/pip/_vendor/pkg_resources/__init__.py:2942:            return ep_map.get(group, {})
./.venv/lib64/python3.12/site-packages/pip/_vendor/pygments/style.py:88:                styledefs = obj.styles.get(token, '').split()
./.venv/lib64/python3.12/site-packages/pip/_vendor/pygments/style.py:96:                for styledef in obj.styles.get(token, '').split():
./.venv/lib64/python3.12/site-packages/pip/_vendor/pygments/util.py:45:    string = options.get(optname, default)
./.venv/lib64/python3.12/site-packages/pip/_vendor/pygments/util.py:56:    Intuitively, this is `options.get(optname, default)`, but restricted to
./.venv/lib64/python3.12/site-packages/pip/_vendor/pygments/util.py:66:    string = options.get(optname, default)
./.venv/lib64/python3.12/site-packages/pip/_vendor/pygments/util.py:87:    string = options.get(optname, default)
./.venv/lib64/python3.12/site-packages/pip/_vendor/pygments/util.py:105:    val = options.get(optname, default)
./.venv/lib64/python3.12/site-packages/pip/_vendor/pygments/formatters/terminal256.py:206:        index = self.best_match.get(color, None)
./.venv/lib64/python3.12/site-packages/pip/_vendor/pygments/filters/__init__.py:824:            opt = options.get(name, False)
./.venv/lib64/python3.12/site-packages/pip/_vendor/pygments/plugin.py:68:        return groups.get(group_name, [])
./.venv/lib64/python3.12/site-packages/pip/_vendor/resolvelib/structs.py:98:        return itertools.chain(self._accessor(v), self._appends.get(k, ()))
./.venv/lib64/python3.12/site-packages/pip/_vendor/pyparsing/results.py:215:            self._tokdict[k] = self._tokdict.get(k, list()) + [v]
./.venv/lib64/python3.12/site-packages/pip/_vendor/pyparsing/results.py:221:            self._tokdict[k] = self._tokdict.get(k, list()) + [
./.venv/lib64/python3.12/site-packages/pip/_vendor/distlib/util.py:1074:        return iter(self._subscribers.get(event, ()))
./.venv/lib64/python3.12/site-packages/pip/_vendor/distlib/util.py:1117:            for p in set(self._preds.get(node, ())):
./.venv/lib64/python3.12/site-packages/pip/_vendor/distlib/util.py:1119:            for s in set(self._succs.get(node, ())):
./.venv/lib64/python3.12/site-packages/pip/_vendor/distlib/util.py:1172:                preds = self._preds.get(step, ())
./.venv/lib64/python3.12/site-packages/pip/_vendor/distlib/util.py:1861:                        result['username'] = config.get(server, 'username')
./.venv/lib64/python3.12/site-packages/pip/_vendor/distlib/util.py:1869:                                result[key] = config.get(server, key)
./.venv/lib64/python3.12/site-packages/pip/_vendor/distlib/util.py:1886:                    repository = config.get(server, 'repository')
./.venv/lib64/python3.12/site-packages/pip/_vendor/distlib/util.py:1890:                    'username': config.get(server, 'username'),
./.venv/lib64/python3.12/site-packages/pip/_vendor/distlib/util.py:1891:                    'password': config.get(server, 'password'),
./.venv/lib64/python3.12/site-packages/pip/_vendor/distlib/compat.py:837:            'od.setdefault(k[,d]) -> od.get(k,d), also set od[k]=d if k not in od'
./.venv/lib64/python3.12/site-packages/pip/_vendor/distlib/compat.py:947:            value = dict.get(self, key, default)
./.venv/lib64/python3.12/site-packages/pip/_vendor/distlib/compat.py:1113:                    converter = self.value_converters.get(prefix, None)
./.venv/lib64/python3.12/site-packages/pip/_vendor/distlib/version.py:592:            p = _VERSION_REPLACE.get(p, p)
./.venv/lib64/python3.12/site-packages/pip/_vendor/distlib/locators.py:399:            result.download_urls = versions.get('urls', {}).get(version, set())
./.venv/lib64/python3.12/site-packages/pip/_vendor/distlib/metadata.py:300:        return _ATTR2FIELD.get(name, name)
./.venv/lib64/python3.12/site-packages/pip/_vendor/distlib/metadata.py:547:                value = self.get(field, None)
./.venv/lib64/python3.12/site-packages/pip/_vendor/distlib/metadata.py:737:                    result = self._data.get(key, value)
./.venv/lib64/python3.12/site-packages/pip/_vendor/distlib/metadata.py:749:                                result = d.get(key, value)
./.venv/lib64/python3.12/site-packages/pip/_vendor/distlib/metadata.py:755:                                result = d.get(key, value)
./.venv/lib64/python3.12/site-packages/pip/_vendor/platformdirs/unix.py:194:        media_dir = os.environ.get(env_var, "").strip()
./.venv/lib64/python3.12/site-packages/pip/_internal/network/download.py:117:    resp = session.get(target_url, headers=HEADERS, stream=True)
./.venv/lib64/python3.12/site-packages/pip/_internal/utils/hashes.py:68:        return hex_digest in self._allowed.get(hash_name, [])
./.venv/lib64/python3.12/site-packages/pip/_internal/utils/temp_dir.py:66:        return self._should_delete.get(kind, True)
./.venv/lib64/python3.12/site-packages/pip/_internal/build_env.py:139:            name: os.environ.get(name, None)
./.venv/lib64/python3.12/site-packages/pip/_internal/resolution/resolvelib/provider.py:176:        requested_order = self._user_requested.get(identifier, math.inf)
./.venv/lib64/python3.12/site-packages/pip/_internal/resolution/resolvelib/factory.py:441:        incompat_ids = {id(c) for c in incompatibilities.get(identifier, ())}
./.venv/lib64/python3.12/site-packages/pip/_internal/resolution/resolvelib/resolver.py:262:        last_known_parent_count = weights.get(node, 0)
./.venv/lib64/python3.12/site-packages/requests/utils.py:874:        proxy = environ_proxies.get(scheme, environ_proxies.get("all"))
./.venv/lib64/python3.12/site-packages/requests/structures.py:96:        return self.__dict__.get(key, None)
./.venv/lib64/python3.12/site-packages/requests/structures.py:99:        return self.__dict__.get(key, default)
./.venv/lib64/python3.12/site-packages/requests/cookies.py:76:        return self._r.headers.get(name, self._new_headers.get(name, default))
./.venv/lib64/python3.12/site-packages/urllib3/response.py:679:        return self.headers.get(name, default)
./.venv/lib64/python3.12/site-packages/urllib3/connectionpool.py:1130:    port = port or port_by_scheme.get(scheme, 80)
./.venv/lib64/python3.12/site-packages/urllib3/fields.py:299:            if self.headers.get(sort_key, False):
./.venv/lib64/python3.12/site-packages/h11/_state.py:349:            changes = STATE_TRIGGERED_TRANSITIONS.get(joint_state, {})
./.venv/lib64/python3.12/site-packages/httpx/_models.py:827:        error_type = error_types.get(status_class, "Invalid status code")
./.venv/lib64/python3.12/site-packages/httpcore/_async/socks_proxy.py:66:        requested = AUTH_METHODS.get(auth_method, "UNKNOWN")
./.venv/lib64/python3.12/site-packages/httpcore/_sync/socks_proxy.py:66:        requested = AUTH_METHODS.get(auth_method, "UNKNOWN")
./connection_pooling.py:50:        return self.session.get(url, **kwargs)
./connection_pooling.py:62:        return optimized_session.get(url, **kwargs)
./main_brain.py:331:    return endpoints.get(service_name, "")
./ms_jarvis_brain_orchestrator_advanced.py:79:                "activity_count": self.neural_networks.get(network_id, {}).get("activity_count", 0) + 1
./fix_all_consciousness_services.py:39:        request_data = request_formats.get(service_name, {"message": message, "user_id": user_id})
./ms_jarvis_microsoft_integration_FIXED.py:118:            response = requests.get(url, headers=headers)
./swarm_watchdog.py:13:            r = httpx.get(url, timeout=5)
./main.py:77:    return endpoints.get(service_name, "/")
./ms_jarvis_microsoft_integration.py:120:            response = requests.get(url, headers=headers)
./add_working_search.py:51:        response = requests.get(url, headers=headers, timeout=10)
./ms_jarvis_facebook_autonomous_social.py:175:            response = requests.get(url, params=params)
./complete_fix.py:41:        request_data = request_formats.get(service_name, {"message": message, "user_id": user_id})
./performance_optimization_analyzer.py:68:                    response = requests.get(url, timeout=5)
./configure_facebook_webhook.py:86:            response = requests.get(test_url, timeout=10)
./process_statewide_gis_bulk.py:163:        categories[cat] = categories.get(cat, 0) + 1
./advanced_service_dashboard.py:50:                response = requests.get(health_url, timeout=2)
./constitutional_api.py:283:                principle_violations[principle] = principle_violations.get(principle, 0) + 1
./egeria_web_ui_v3_consciousness.py:298:    return jsonify(query_status.get(query_id, {'status': 'not_found'}))
./dgm_supervisor_woah.py:200:                    "woah_weight": WOAH_WEIGHTS.get(service_name, 1.0),
./egeria_web_ui_final_biological.py:344:    return jsonify(query_status.get(query_id, {'status': 'not_found'}))
./rebuild_query_service.py:47:        request_data = request_formats.get(service_name, {"message": message, "user_id": user_id})
./ms_jarvis_dynamic_model_selector.py:68:        return configs.get(model_name, {"weight": 1.0, "timeout": 60})
./jarvis_steward.py:77:    rights = _RIGHTS.get(rank, _RIGHTS["newcomer"])
./venv/lib/python3.12/site-packages/anyio/lowlevel.py:174:        token = RunvarToken(self, current_vars.get(self, RunVar.NO_VALUE_SET))
./venv/lib/python3.12/site-packages/fsspec/generic.py:35:        fs, _ = url_to_fs(url, **storage_options.get(protocol, {}))
./venv/lib/python3.12/site-packages/fsspec/mapping.py:115:            key: out[k2] if on_error == "raise" else out.get(k2, KeyError(k2))
./venv/lib/python3.12/site-packages/fsspec/implementations/github.py:235:        r = requests.get(url, timeout=self.timeout, **self.kw)
./venv/lib/python3.12/site-packages/fsspec/implementations/github.py:301:            r = requests.get(url, timeout=self.timeout, **self.kw)
./venv/lib/python3.12/site-packages/fsspec/implementations/gist.py:90:        r = requests.get(url, timeout=self.timeout, **self.kw)
./venv/lib/python3.12/site-packages/fsspec/implementations/gist.py:215:        r = requests.get(raw_url, timeout=self.timeout, **self.kw)
./venv/lib/python3.12/site-packages/fsspec/implementations/cached.py:586:            self.fs.get(downpath, downfn)
./venv/lib/python3.12/site-packages/fsspec/implementations/cached.py:670:            self.fs.get(getpaths, storepaths)
./venv/lib/python3.12/site-packages/fsspec/implementations/cached.py:898:        self.fs.get(rpaths, lpaths)
./venv/lib/python3.12/site-packages/fsspec/implementations/http.py:827:    r = await session.get(url, headers=headers, **kwargs)
./venv/lib/python3.12/site-packages/fsspec/implementations/http.py:856:        r = await session.get(url, allow_redirects=ar, **kwargs)
./venv/lib/python3.12/site-packages/fsspec/implementations/http_sync.py:874:    r = session.get(url, headers=headers, **kwargs)
./venv/lib/python3.12/site-packages/fsspec/implementations/http_sync.py:897:        r = session.get(url, allow_redirects=ar, **kwargs)
./venv/lib/python3.12/site-packages/fsspec/implementations/ftp.py:179:        files = self.dircache.get(path, out)
./venv/lib/python3.12/site-packages/fsspec/implementations/reference.py:307:        maybe = self._items.get((field, record), {}).get(ri, False)
./venv/lib/python3.12/site-packages/fsspec/implementations/reference.py:410:            self.zmetadata[key] = {**self.zmetadata.get(key, {}), **new_value}
./venv/lib/python3.12/site-packages/fsspec/tests/abstract/get.py:137:            fs.get(s, t)
./venv/lib/python3.12/site-packages/fsspec/tests/abstract/get.py:141:            fs.get(s, t, recursive=True)
./venv/lib/python3.12/site-packages/fsspec/tests/abstract/get.py:170:            fs.get(s, t, recursive=True, maxdepth=1)
./venv/lib/python3.12/site-packages/fsspec/tests/abstract/get.py:217:            fs.get(s, t)
./venv/lib/python3.12/site-packages/fsspec/tests/abstract/get.py:221:            fs.get(s, t, recursive=True)
./venv/lib/python3.12/site-packages/fsspec/tests/abstract/get.py:235:            fs.get(s, t, recursive=True, maxdepth=1)
./venv/lib/python3.12/site-packages/fsspec/tests/abstract/get.py:452:            fs.get(source_files, t)
./venv/lib/python3.12/site-packages/fsspec/tests/abstract/get.py:488:        fs.get(source_files, local_join(target, "newdir") + "/")  # Note trailing slash
./venv/lib/python3.12/site-packages/fsspec/tests/abstract/get.py:509:            fs.get(src, target, recursive=True)
./venv/lib/python3.12/site-packages/fsspec/spec.py:1806:        return self.get(rpath, lpath, recursive=recursive, **kwargs)
./venv/lib/python3.12/site-packages/fsspec/dircache.py:58:            if self._times.get(item, 0) - time.time() < -self.listings_expiry_time:
./venv/lib/python3.12/site-packages/packaging/version.py:705:        letter = _LETTER_NORMALIZATION.get(letter, letter)
./venv/lib/python3.12/site-packages/packaging/tags.py:581:    archs = {"armv8l": ["armv8l", "armv7l"]}.get(arch, [arch])
./venv/lib/python3.12/site-packages/starlette/config.py:92:        return self.get(key, cast, default)
./venv/lib/python3.12/site-packages/torch/_higher_order_ops/effects.py:227:    # Get a token. We can't do `tokens.get(op, torch.tensor([]))` because
./venv/lib/python3.12/site-packages/torch/_higher_order_ops/triton_kernel_wrap.py:297:                tma_descriptor_metadata.get(name, None)
./venv/lib/python3.12/site-packages/torch/_guards.py:739:        return self.dynamo_installed_submodules.get(fn_id, [])
./venv/lib/python3.12/site-packages/torch/_guards.py:745:        return self.autograd_cache.get(identifier, None)
./venv/lib/python3.12/site-packages/torch/_guards.py:751:        return self.proxy_dispatch_cache.get(identifier, None)
./venv/lib/python3.12/site-packages/torch/_guards.py:770:        return self.lazy_bwd_cache[identifier].get(tangent_metadata, (None, None))
./venv/lib/python3.12/site-packages/torch/_guards.py:774:        if prev_effects := self.effects_cache.get(identifier, None):
./venv/lib/python3.12/site-packages/torch/_guards.py:785:        return self.effects_cache.get(identifier, None)
./venv/lib/python3.12/site-packages/torch/_functorch/partitioners.py:658:        position_to_quant.get(i, node) for i, node in enumerate(fwd_outputs)
./venv/lib/python3.12/site-packages/torch/_functorch/functional_call.py:137:            v = all_keys_counter.get(k, 0)
./venv/lib/python3.12/site-packages/torch/_functorch/_activation_checkpointing/remat_using_tags_for_fwd_loss_bwd_graph_pass.py:94:        return recomputed_nodes.get(x, env[x])
./venv/lib/python3.12/site-packages/torch/_functorch/_activation_offloading/activation_offloading.py:145:        0, tuple(node_to_offload.get(node, node) for node in fwd_outputs)
./venv/lib/python3.12/site-packages/torch/_functorch/_aot_autograd/frontend_utils.py:306:                old_module_attrs = snapshot.get(module_name, {})
./venv/lib/python3.12/site-packages/torch/_functorch/_aot_autograd/frontend_utils.py:307:                new_module_attrs = new_attrs.get(module_name, {})
./venv/lib/python3.12/site-packages/torch/_functorch/_aot_autograd/graph_capture_wrappers.py:555:    original_val = fx_traceback.current_meta.get(meta_key, None)
./venv/lib/python3.12/site-packages/torch/_lazy/device_context.py:21:        devctx = DeviceContext._CONTEXTS.get(device, None)
./venv/lib/python3.12/site-packages/torch/_lazy/extract_compiled_graph.py:47:            arg_idx = self.tensor_id_to_arg_idx.get(tensor_id, None)
./venv/lib/python3.12/site-packages/torch/multiprocessing/reductions.py:78:            return dict.get(self, key)
./venv/lib/python3.12/site-packages/torch/multiprocessing/spawn.py:244:        and os.environ.get(ENV_VAR_PARALLEL_START, "0") == "1"
./venv/lib/python3.12/site-packages/torch/_export/passes/constant_folding.py:188:            for to_delete in self.user_to_last_uses.get(node, []):
./venv/lib/python3.12/site-packages/torch/_export/verifier.py:530:        return _VerifierMeta._registry.get(dialect, Verifier)
./venv/lib/python3.12/site-packages/torch/sparse/_triton_ops.py:703:        }.get(N, 16)
./venv/lib/python3.12/site-packages/torch/sparse/_triton_ops.py:714:            num_warps = {16: 1, 32: 1, 64: 2}.get(Ms, 4)
./venv/lib/python3.12/site-packages/torch/sparse/_triton_ops.py:716:            num_warps = {16: 1, 32: 1, 64: 2}.get(Ms, 4)
./venv/lib/python3.12/site-packages/torch/sparse/_triton_ops.py:718:            num_warps = {16: 1, 32: 4}.get(Ms, 4)
./venv/lib/python3.12/site-packages/torch/sparse/_triton_ops.py:720:            num_warps = {16: 1, 32: 2}.get(Ms, 4)
./venv/lib/python3.12/site-packages/torch/_prims_common/__init__.py:1459:    return _computation_dtype_map.get(dtype, dtype)
./venv/lib/python3.12/site-packages/torch/_prims_common/__init__.py:1474:        return _cpu_acc_type_map.get(dtype, dtype)
./venv/lib/python3.12/site-packages/torch/ao/pruning/_experimental/data_sparsifier/lightning/callbacks/_data_sparstity_utils.py:28:                name=valid_name, data=parameter, **config.get(valid_name, {})
./venv/lib/python3.12/site-packages/torch/ao/pruning/_experimental/data_sparsifier/base_data_sparsifier.py:189:            config_name = data_groups.get(name, None)
./venv/lib/python3.12/site-packages/torch/ao/pruning/_experimental/data_sparsifier/base_data_sparsifier.py:197:            data = container_state_dict.get(name, None)
./venv/lib/python3.12/site-packages/torch/ao/pruning/_experimental/data_scheduler/base_data_scheduler.py:46:            name: config.get(schedule_param, None)
./venv/lib/python3.12/site-packages/torch/ao/quantization/quantize.py:104:    module_qconfig = qconfig_dict.get(prefix, module_qconfig)
./venv/lib/python3.12/site-packages/torch/ao/quantization/pt2e/_numeric_debugger.py:50:            unique_id, node.meta.get(CUSTOM_KEY, {}).get(NUMERIC_DEBUG_HANDLE_KEY, 0)
./venv/lib/python3.12/site-packages/torch/ao/quantization/pt2e/qat_utils.py:621:            return original_to_replacement_node.get(_node, _node)
./venv/lib/python3.12/site-packages/torch/ao/quantization/pt2e/qat_utils.py:629:                original_to_replacement_node.get(src, src),
./venv/lib/python3.12/site-packages/torch/ao/quantization/pt2e/qat_utils.py:630:                original_to_replacement_node.get(dest, dest),
./venv/lib/python3.12/site-packages/torch/ao/quantization/backend_config/backend_config.py:416:        conf = cls(backend_config_dict.get(NAME_DICT_KEY, ""))
./venv/lib/python3.12/site-packages/torch/ao/quantization/backend_config/backend_config.py:417:        for d in backend_config_dict.get(CONFIGS_DICT_KEY, []):
./venv/lib/python3.12/site-packages/torch/ao/quantization/backend_config/backend_config.py:673:        for d in backend_pattern_config_dict.get(DTYPE_CONFIGS_DICT_KEY, []):
./venv/lib/python3.12/site-packages/torch/ao/quantization/backend_config/backend_config.py:700:            backend_pattern_config_dict.get(INPUT_TYPE_TO_INDEX_DICT_KEY, {})
./venv/lib/python3.12/site-packages/torch/ao/quantization/utils.py:270:    class_mapping = custom_module_class_mapping.get(quant_type, {})
./venv/lib/python3.12/site-packages/torch/ao/quantization/fx/fuse.py:101:            node_subpattern = node_to_subpattern.get(node, None)
./venv/lib/python3.12/site-packages/torch/ao/quantization/fx/utils.py:143:        quant_mode_custom_module_config = custom_module_mapping.get(quant_mode, {})
./venv/lib/python3.12/site-packages/torch/ao/quantization/fx/utils.py:429:    return NON_OBSERVABLE_ARG_DICT.get(info, EMPTY_ARG_DICT)
./venv/lib/python3.12/site-packages/torch/ao/quantization/fx/custom_config.py:255:        ) in prepare_custom_config_dict.get(STANDALONE_MODULE_NAME_DICT_KEY, []):
./venv/lib/python3.12/site-packages/torch/ao/quantization/fx/custom_config.py:278:        ) in prepare_custom_config_dict.get(STANDALONE_MODULE_CLASS_DICT_KEY, []):
./venv/lib/python3.12/site-packages/torch/ao/quantization/fx/custom_config.py:304:            prepare_custom_config_dict.get(NON_TRACEABLE_MODULE_NAME_DICT_KEY, [])
./venv/lib/python3.12/site-packages/torch/ao/quantization/fx/custom_config.py:307:            prepare_custom_config_dict.get(NON_TRACEABLE_MODULE_CLASS_DICT_KEY, [])
./venv/lib/python3.12/site-packages/torch/ao/quantization/fx/custom_config.py:310:            prepare_custom_config_dict.get(INPUT_QUANTIZED_INDEXES_DICT_KEY, [])
./venv/lib/python3.12/site-packages/torch/ao/quantization/fx/custom_config.py:313:            prepare_custom_config_dict.get(OUTPUT_QUANTIZED_INDEXES_DICT_KEY, [])
./venv/lib/python3.12/site-packages/torch/ao/quantization/fx/custom_config.py:316:            prepare_custom_config_dict.get(PRESERVED_ATTRIBUTES_DICT_KEY, [])
./venv/lib/python3.12/site-packages/torch/ao/quantization/fx/custom_config.py:447:            convert_custom_config_dict.get(PRESERVED_ATTRIBUTES_DICT_KEY, [])
./venv/lib/python3.12/site-packages/torch/ao/quantization/fx/custom_config.py:509:            fuse_custom_config_dict.get(PRESERVED_ATTRIBUTES_DICT_KEY, [])
./venv/lib/python3.12/site-packages/torch/ao/quantization/fx/prepare.py:410:    dtype_configs: list[DTypeConfig] = pattern_to_dtype_configs.get(pattern, [])
./venv/lib/python3.12/site-packages/torch/ao/quantization/fx/qconfig_mapping_utils.py:317:    return qconfig_mapping.object_type_qconfigs.get(object_type, fallback_qconfig)
./venv/lib/python3.12/site-packages/torch/ao/quantization/qconfig_mapping.py:371:        for object_type, qconfig in qconfig_dict.get(_OBJECT_TYPE_DICT_KEY, []):
./venv/lib/python3.12/site-packages/torch/ao/quantization/qconfig_mapping.py:377:        for module_name, qconfig in qconfig_dict.get(_MODULE_NAME_DICT_KEY, []):
./venv/lib/python3.12/site-packages/torch/ao/quantization/quantizer/x86_inductor_quantizer.py:265:    quantization_annotation = node.meta.get(QUANT_ANNOTATION_KEY, None)
./venv/lib/python3.12/site-packages/torch/ao/quantization/fuser_method_mappings.py:245:    fuser_method = all_mappings.get(op_list, None)
./venv/lib/python3.12/site-packages/torch/ao/quantization/quantization_mappings.py:254:    static_quant_module_class = all_mappings.get(float_module_class, None)
./venv/lib/python3.12/site-packages/torch/ao/quantization/quantization_mappings.py:275:    dynamic_quant_module_class = all_mappings.get(float_module_class, None)
./venv/lib/python3.12/site-packages/torch/_prims/context.py:131:        func = mapping.get(orig_func, None)
./venv/lib/python3.12/site-packages/torch/_prims/context.py:140:            func = torch._decomp.decomposition_table.get(orig_func, None)
./venv/lib/python3.12/site-packages/torch/_prims/context.py:146:                func = torch._decomp.decomposition_table.get(default, None)
./venv/lib/python3.12/site-packages/torch/package/package_exporter.py:674:                        field = memo.get(arg, None)
./venv/lib/python3.12/site-packages/torch/package/package_importer.py:515:        module = self.modules.get(name, _NEEDS_LOADING)
./venv/lib/python3.12/site-packages/torch/package/package_importer.py:585:                            and self.modules.get(from_name, _NEEDS_LOADING) is not None
./venv/lib/python3.12/site-packages/torch/package/package_importer.py:647:            node = cur.children.get(atom, None)
./venv/lib/python3.12/site-packages/torch/package/_digraph.py:151:                idx = self._node_order.get(candidate, None)
./venv/lib/python3.12/site-packages/torch/fx/passes/reinplace.py:99:                maybe_base_of_view = self.multi_output_view_nodes.get(list_arg, None)
./venv/lib/python3.12/site-packages/torch/fx/passes/graph_transform_observer.py:190:            new_node = self.name_to_node.get(new, None)
./venv/lib/python3.12/site-packages/torch/fx/passes/splitter_base.py:194:        for idx in self.node_events.get(node_name, []):
./venv/lib/python3.12/site-packages/torch/fx/passes/splitter_base.py:209:            for idx in self.node_events.get(name, []):
./venv/lib/python3.12/site-packages/torch/fx/passes/splitter_base.py:264:                os.environ.get(ENV_FX_NET_ACC_SPLITTER_TRACKER_TRACKED_NODES, "").split(
./venv/lib/python3.12/site-packages/torch/fx/_symbolic_trace.py:560:            num_calls = self.num_calls.get(module_qualified_name, 0)
./venv/lib/python3.12/site-packages/torch/fx/_symbolic_trace.py:977:            type_expr=fn_for_analysis.__annotations__.get(name, None),
./venv/lib/python3.12/site-packages/torch/fx/experimental/symbolic_shapes.py:533:    return {shape_env.unbacked_renamings.get(k, k): v for k, v in bindings.items()}
./venv/lib/python3.12/site-packages/torch/fx/experimental/symbolic_shapes.py:1295:                source=shape_env.var_to_sources.get(s, [None])[0],  # type: ignore[union-attr]
./venv/lib/python3.12/site-packages/torch/fx/experimental/symbolic_shapes.py:2802:        val = self._print_cache.get(expr, None)
./venv/lib/python3.12/site-packages/torch/fx/experimental/symbolic_shapes.py:4344:        return self.fx_node_cache.get(node_key, None), fresh
./venv/lib/python3.12/site-packages/torch/fx/experimental/symbolic_shapes.py:4473:                hint_overrides.get(i, val),
./venv/lib/python3.12/site-packages/torch/fx/experimental/symbolic_shapes.py:4674:                hint=hint_overrides.get(i, hint),
./venv/lib/python3.12/site-packages/torch/fx/experimental/symbolic_shapes.py:5286:        return self.source_name_to_debug_name.get(src_name, src_name)
./venv/lib/python3.12/site-packages/torch/fx/experimental/symbolic_shapes.py:5603:                            x: self.var_to_range.get(x, None) for x in s.free_symbols
./venv/lib/python3.12/site-packages/torch/fx/experimental/symbolic_shapes.py:5656:                    user_stack = self.specialization_stacks.get(source, None)
./venv/lib/python3.12/site-packages/torch/fx/experimental/symbolic_shapes.py:5954:        for ra in self.deferred_runtime_asserts.get(None, []):
./venv/lib/python3.12/site-packages/torch/fx/experimental/symbolic_shapes.py:6270:        var_to_range = {x: self.var_to_range.get(x, None) for x in expr.free_symbols}
./venv/lib/python3.12/site-packages/torch/fx/experimental/symbolic_shapes.py:6303:                for r in self.deferred_runtime_asserts.get(s, ())
./venv/lib/python3.12/site-packages/torch/fx/experimental/symbolic_shapes.py:6753:        if tgt == self.replacements.get(a, None):
./venv/lib/python3.12/site-packages/torch/fx/experimental/symbolic_shapes.py:6883:                    "sources": [s.name for s in self.var_to_sources.get(a, [])],
./venv/lib/python3.12/site-packages/torch/fx/experimental/symbolic_shapes.py:6895:            for source in self.var_to_sources.get(a, []):
./venv/lib/python3.12/site-packages/torch/fx/experimental/symbolic_shapes.py:7860:            if isinstance(self.var_to_val.get(symbol, None), SingletonInt):
./venv/lib/python3.12/site-packages/torch/fx/experimental/symbolic_shapes.py:7922:        old_vr = self.var_to_range.get(s, ValueRanges.unknown())
./venv/lib/python3.12/site-packages/torch/fx/experimental/unification/multipledispatch/utils.py:56:        for m in edges.get(n, ()):
./venv/lib/python3.12/site-packages/torch/fx/experimental/unification/multipledispatch/utils.py:61:    if any(incoming_edges.get(v, None) for v in edges):
./venv/lib/python3.12/site-packages/torch/fx/experimental/unification/multipledispatch/utils.py:79:            result[val] = result.get(val, ()) + (key,)
./venv/lib/python3.12/site-packages/torch/fx/experimental/unification/utils.py:58:        for m in edges.get(n, ()):
./venv/lib/python3.12/site-packages/torch/fx/experimental/unification/utils.py:81:            result[val] = result.get(val, ()) + (key,)
./venv/lib/python3.12/site-packages/torch/fx/experimental/proxy_tensor.py:1576:        self.tracer.torch_fn_counts[func] = self.tracer.torch_fn_counts.get(func, 0) + 1
./venv/lib/python3.12/site-packages/torch/fx/experimental/meta_tracer.py:203:                meta_target = manual_meta_overrides.get(target, target)
./venv/lib/python3.12/site-packages/torch/fx/interpreter.py:231:                for to_delete in self.user_to_last_uses.get(node, []):
./venv/lib/python3.12/site-packages/torch/fx/graph.py:190:            num = self._base_count.get(candidate, 0)
./venv/lib/python3.12/site-packages/torch/fx/graph.py:191:            if _illegal_names.get(candidate, obj) is not obj:
./venv/lib/python3.12/site-packages/torch/fx/graph.py:517:                    origin_type = _origin_type_map.get(origin_type, origin_type)
./venv/lib/python3.12/site-packages/torch/fx/graph.py:615:            nodes_to_delete = user_to_last_uses.get(user, [])
./venv/lib/python3.12/site-packages/torch/fx/subgraph_rewriter.py:353:                val_map[rn] = match_changed_node.get(gn, gn)
./venv/lib/python3.12/site-packages/torch/profiler/_memory_profiler.py:388:            self._values[key] = max(self._values.get(key, 0), num_bytes)
./venv/lib/python3.12/site-packages/torch/profiler/_memory_profiler.py:536:                expected = tensor_versions.get(key, 0)
./venv/lib/python3.12/site-packages/torch/profiler/_memory_profiler.py:540:                prior_version = tensor_versions.get(key, version)
./venv/lib/python3.12/site-packages/torch/profiler/_memory_profiler.py:607:        prior_version = self._active_version.get(key, None)
./venv/lib/python3.12/site-packages/torch/profiler/_memory_profiler.py:654:            or element.by_key.get(key, None)
./venv/lib/python3.12/site-packages/torch/profiler/_memory_profiler.py:757:            (key, version): self._categories.get(key, version)
./venv/lib/python3.12/site-packages/torch/profiler/_memory_profiler.py:779:                    if self._categories.get(key, version)
./venv/lib/python3.12/site-packages/torch/profiler/_memory_profiler.py:980:                    if version == 0 or self._categories.get(key, version - 1) in prior:
./venv/lib/python3.12/site-packages/torch/profiler/_memory_profiler.py:1012:                self.categories.get(key, version)
./venv/lib/python3.12/site-packages/torch/profiler/_memory_profiler.py:1079:                self.categories.get(key, version)
./venv/lib/python3.12/site-packages/torch/optim/radam.py:81:                p_state = self.state.get(p, [])
./venv/lib/python3.12/site-packages/torch/optim/_adafactor.py:66:                p_state = self.state.get(p, [])
./venv/lib/python3.12/site-packages/torch/optim/nadam.py:85:                p_state = self.state.get(p, [])
./venv/lib/python3.12/site-packages/torch/optim/rmsprop.py:82:                p_state = self.state.get(p, [])
./venv/lib/python3.12/site-packages/torch/optim/asgd.py:71:                p_state = self.state.get(p, [])
./venv/lib/python3.12/site-packages/torch/optim/adam.py:126:                p_state = self.state.get(p, [])
./venv/lib/python3.12/site-packages/torch/optim/adadelta.py:73:                p_state = self.state.get(p, [])
./venv/lib/python3.12/site-packages/torch/optim/rprop.py:69:                p_state = self.state.get(p, [])
./venv/lib/python3.12/site-packages/torch/optim/adamax.py:76:                p_state = self.state.get(p, [])
./venv/lib/python3.12/site-packages/torch/_utils.py:136:            return map_location.get(device, device)
./venv/lib/python3.12/site-packages/torch/_utils.py:1060:    if (module := sys.modules.get(module_name, None)) is not None:
./venv/lib/python3.12/site-packages/torch/export/_draft_export.py:317:            if res := self.expression_created_logs.get(sym_node_id, None):
./venv/lib/python3.12/site-packages/torch/export/unflatten.py:689:                mod = _get_attr(self, redirected_call_indices.get(fqn, fqn))
./venv/lib/python3.12/site-packages/torch/export/_unlift.py:47:        return str(_pytree_subclasses_that_lose_info.get(t, t))
./venv/lib/python3.12/site-packages/torch/export/_unlift.py:329:        return_nodes_to_copy.get(node, node) for node in user_output_nodes
./venv/lib/python3.12/site-packages/torch/export/_trace.py:492:            targets = remap_table.get(orig_target, [orig_target])
./venv/lib/python3.12/site-packages/torch/masked/_ops.py:314:            argument_declarations.get(a, f"{a.split('__', 1)[0]}: TBD.").splitlines()
./venv/lib/python3.12/site-packages/torch/distributed/argparse_util.py:46:        default = os.environ.get(env_name, default)
./venv/lib/python3.12/site-packages/torch/distributed/argparse_util.py:100:        default = bool(int(os.environ.get(env_name, "1" if default else "0")))
./venv/lib/python3.12/site-packages/torch/distributed/_tools/sac_estimator.py:373:                        if acm_stats := self._sac_mod_metadata.get(mod_fqn, None):
./venv/lib/python3.12/site-packages/torch/distributed/_tools/sac_estimator.py:448:            if acm_stats := self._sac_mod_metadata.get(mod_fqn, None):
./venv/lib/python3.12/site-packages/torch/distributed/_tools/mod_tracker.py:96:        return self._known_modules.get(mod, None)
./venv/lib/python3.12/site-packages/torch/distributed/_tools/mem_tracker.py:451:            winfo, _ = self._WINFO.get(st, (None, None))
./venv/lib/python3.12/site-packages/torch/distributed/_tools/mem_tracker.py:488:            winfo, _ = self._WINFO.get(st, (None, None))
./venv/lib/python3.12/site-packages/torch/distributed/_tools/mem_tracker.py:513:                        if mod_stats.local_peak.get(dev, 0) < dev_snap[_TOTAL_KEY]:
./venv/lib/python3.12/site-packages/torch/distributed/_tools/mem_tracker.py:520:            if self._peak_mem.get(dev, 0) < dev_snap[_TOTAL_KEY]:
./venv/lib/python3.12/site-packages/torch/distributed/_tools/mem_tracker.py:530:            winfo, _ = self._WINFO.get(st, (None, None))
./venv/lib/python3.12/site-packages/torch/distributed/_tools/mem_tracker.py:599:                self._param_to_grad_hook_handles.get(param, None) is None
./venv/lib/python3.12/site-packages/torch/distributed/_tools/mem_tracker.py:627:                winfo, _ = self._WINFO.get(st, (None, None))
./venv/lib/python3.12/site-packages/torch/distributed/tensor/_ops/_common_rules.py:108:            pending_sums_counter[sum_dim] = pending_sums_counter.get(sum_dim, 0) + 1
./venv/lib/python3.12/site-packages/torch/distributed/distributed_c10d.py:1404:    pg_store = _world.pg_map.get(pg, None)
./venv/lib/python3.12/site-packages/torch/distributed/distributed_c10d.py:2244:    if _world.pg_map.get(pg, None) is None:
./venv/lib/python3.12/site-packages/torch/distributed/distributed_c10d.py:2336:    if _world.pg_map.get(pg, None) is None:
./venv/lib/python3.12/site-packages/torch/distributed/distributed_c10d.py:5711:    for group in _world.tags_to_pg.get(tag, []):
./venv/lib/python3.12/site-packages/torch/distributed/distributed_c10d.py:5764:    return _world.pg_names.get(pg, "None")
./venv/lib/python3.12/site-packages/torch/distributed/distributed_c10d.py:6032:    original_backend_config = _world.pg_backend_config.get(target_pg, "")
./venv/lib/python3.12/site-packages/torch/distributed/_symmetric_memory/_nvshmem_triton.py:168:        kernel = kernel_cache.get(key, None)
./venv/lib/python3.12/site-packages/torch/distributed/_symmetric_memory/_nvshmem_triton.py:330:            nvshmem.get(dest_tensor, src_tensor, 100, 0)
./venv/lib/python3.12/site-packages/torch/distributed/__init__.py:97:            counter = _breakpoint_cache.get(key, 0) + 1
./venv/lib/python3.12/site-packages/torch/distributed/fsdp/_init_utils.py:454:        os.environ.get(_FSDP_USE_FULL_PREC_IN_EVAL, "") == "1"
./venv/lib/python3.12/site-packages/torch/distributed/fsdp/_optim_utils.py:504:                    state = optim.state.get(param, None)  # type: ignore[call-overload]
./venv/lib/python3.12/site-packages/torch/distributed/fsdp/_optim_utils.py:1390:                info = object_state.tensors.get(state_name, None)
./venv/lib/python3.12/site-packages/torch/distributed/fsdp/_optim_utils.py:1412:            local_state = input_states[fqn].get(state_name, None)
./venv/lib/python3.12/site-packages/torch/distributed/fsdp/_optim_utils.py:1427:                curr_non_tensor_value = gathered_state.get(name, None)
./venv/lib/python3.12/site-packages/torch/distributed/fsdp/_optim_utils.py:1439:                curr_scalar_tensor_value = gathered_state.get(name, None)
./venv/lib/python3.12/site-packages/torch/distributed/fsdp/_debug_utils.py:122:        handle = state._fully_sharded_module_to_handle.get(module, None)
./venv/lib/python3.12/site-packages/torch/distributed/fsdp/_runtime_utils.py:1313:    module_param_handle = state._fully_sharded_module_to_handle.get(module, None)
./venv/lib/python3.12/site-packages/torch/distributed/fsdp/_runtime_utils.py:1335:    module_param_handle = state._fully_sharded_module_to_handle.get(module, None)
./venv/lib/python3.12/site-packages/torch/distributed/fsdp/_flat_param.py:537:            os.environ.get(_FSDP_SKIP_WRITEBACK_CHECK, "") == "1"
./venv/lib/python3.12/site-packages/torch/distributed/fsdp/_flat_param.py:540:            os.environ.get(_FSDP_USE_FULL_PREC_IN_EVAL, "") == "1"
./venv/lib/python3.12/site-packages/torch/distributed/fsdp/_flat_param.py:542:        self._use_fake_all_gather = os.environ.get(_FSDP_USE_FAKE_ALL_GATHER, "") == "1"
./venv/lib/python3.12/site-packages/torch/distributed/fsdp/_flat_param.py:543:        self._use_fake_reduce = os.environ.get(_FSDP_USE_FAKE_REDUCE, "") == "1"
./venv/lib/python3.12/site-packages/torch/distributed/fsdp/_flat_param.py:628:        use_unsafe_setattr = os.environ.get(_FSDP_USE_UNSAFE_SETATTR, "") == "1"
./venv/lib/python3.12/site-packages/torch/distributed/rpc/api.py:214:        sequence_num = _all_gather_sequence_id.get(concat_names, 0)
./venv/lib/python3.12/site-packages/torch/distributed/rpc/backend_registry.py:234:            if all_devices.get(target_node, []):
./venv/lib/python3.12/site-packages/torch/distributed/elastic/multiprocessing/api.py:179:            map[i] = val_or_map.get(i, Std.NONE)
./venv/lib/python3.12/site-packages/torch/distributed/elastic/timer/api.py:95:        res = q.get(size, timeout=0)
./venv/lib/python3.12/site-packages/torch/distributed/elastic/timer/api.py:191:        timer_requests = self._request_queue.get(batch_size, self._max_interval)
./venv/lib/python3.12/site-packages/torch/distributed/elastic/rendezvous/api.py:294:        return self.config.get(key, default)
./venv/lib/python3.12/site-packages/torch/distributed/elastic/rendezvous/api.py:298:        value = self.get(key, default)
./venv/lib/python3.12/site-packages/torch/distributed/elastic/rendezvous/api.py:317:        value = self.get(key, default)
./venv/lib/python3.12/site-packages/torch/distributed/elastic/metrics/api.py:90:    handler = _metrics_map.get(group, _default_metrics_handler)
./venv/lib/python3.12/site-packages/torch/distributed/elastic/utils/api.py:23:    value = os.environ.get(env_name, None)
./venv/lib/python3.12/site-packages/torch/distributed/checkpoint/optimizer.py:215:        return super().lookup_tensor(self.translation.get(index, index))
./venv/lib/python3.12/site-packages/torch/distributed/checkpoint/optimizer.py:316:            alloc_size = layout_specs.get(spec_key, (None, value.size))[1]
./venv/lib/python3.12/site-packages/torch/distributed/checkpoint/_state_dict_stager.py:293:        y = memo.get(d, _nil)
./venv/lib/python3.12/site-packages/torch/distributed/rendezvous.py:253:        env_val = os.environ.get(env_var, None)
./venv/lib/python3.12/site-packages/torch/distributed/pipelining/_IR.py:413:                self.value_remap.get(v, v) for v in kwargs["input_values"]
./venv/lib/python3.12/site-packages/torch/distributed/pipelining/schedules.py:251:        pipeline_order.get(key, [""] * num_steps) for key in sorted(pipeline_order)
./venv/lib/python3.12/site-packages/torch/distributed/pipelining/schedules.py:3077:            counters[input_key] = counters.get(input_key, 0) + 1
./venv/lib/python3.12/site-packages/torch/distributed/pipelining/schedules.py:3078:            counters[weight_key] = counters.get(weight_key, 0) + 1
./venv/lib/python3.12/site-packages/torch/distributed/pipelining/schedules.py:3090:            forward_mb = counters.get(forward_key, 0)
./venv/lib/python3.12/site-packages/torch/distributed/pipelining/schedules.py:3091:            backward_mb = counters.get(backward_key, 0)
./venv/lib/python3.12/site-packages/torch/distributed/pipelining/schedules.py:3114:            mb_index = counters.get(key, 0)
./venv/lib/python3.12/site-packages/torch/distributed/pipelining/schedules.py:3142:            counters[weight_key] = counters.get(weight_key, 0) + 1
./venv/lib/python3.12/site-packages/torch/nested/_internal/ops.py:252:    dispatch_func = JAGGED_OPS_TABLE.get(func, None)
./venv/lib/python3.12/site-packages/torch/_meta_registrations.py:103:    return from_complex.get(dtype, dtype)
./venv/lib/python3.12/site-packages/torch/_library/triton.py:18:    return triton_ops_to_kernels.get(name, [])
./venv/lib/python3.12/site-packages/torch/_library/simple_registry.py:32:        res = self._data.get(qualname, None)
./venv/lib/python3.12/site-packages/torch/_library/simple_registry.py:83:        return self._data.get(torch_dispatch_class, None)
./venv/lib/python3.12/site-packages/torch/serialization.py:1873:            location = map_location.get(location, location)
./venv/lib/python3.12/site-packages/torch/serialization.py:2131:            mod_name = load_module_mapping.get(mod_name, mod_name)
./venv/lib/python3.12/site-packages/torch/_inductor/autoheuristic/autoheuristic.py:161:        return self.collected_feedback.get(choice, None)
./venv/lib/python3.12/site-packages/torch/_inductor/autoheuristic/autoheuristic.py:308:        return self.choicestr2choice.get(choice, None)
./venv/lib/python3.12/site-packages/torch/_inductor/runtime/triton_heuristics.py:1202:            asm = launcher.bin.asm.get(asm_type, None)
./venv/lib/python3.12/site-packages/torch/_inductor/runtime/triton_heuristics.py:1575:                call_args = [repl.get(arg, arg) for arg in call_args]
./venv/lib/python3.12/site-packages/torch/_inductor/runtime/triton_heuristics.py:1961:                    if compile_meta["signature"].get(x, "constexpr") != "constexpr"
./venv/lib/python3.12/site-packages/torch/_inductor/runtime/coordinate_descent_tuner.py:28:        return config.kwargs.get(name, int(8 // config.num_warps))
./venv/lib/python3.12/site-packages/torch/_inductor/runtime/coordinate_descent_tuner.py:30:        return config.kwargs.get(name, None)
./venv/lib/python3.12/site-packages/torch/_inductor/runtime/caching/implementations.py:142:        if (value := self._memory.get(pickled_key, miss)) is not miss:
./venv/lib/python3.12/site-packages/torch/_inductor/sizevars.py:613:                s: self.shape_env.var_to_range.get(s, None) for s in out.free_symbols
./venv/lib/python3.12/site-packages/torch/_inductor/debug.py:1084:                pre_grad_nodes.update(post_to_pre.get(post_node, []))
./venv/lib/python3.12/site-packages/torch/_inductor/debug.py:1087:                "stack_traces": _inductor_kernel_stack_trace.get(kernel_name, []),
./venv/lib/python3.12/site-packages/torch/_inductor/loop_body.py:196:        return self.op_counts.get(name, 0) > 0
./venv/lib/python3.12/site-packages/torch/_inductor/ir.py:6531:                    type_ = self.allarg_properties.get(arg_name, {}).get("type")
./venv/lib/python3.12/site-packages/torch/_inductor/ir.py:9279:        self.prev_effect_buffer = V.graph.effectful_ops.get(effect_type, None)
./venv/lib/python3.12/site-packages/torch/_inductor/comms.py:1428:        snodes_allocfree[n].size_free += size_free_delta_update.get(n, 0)
./venv/lib/python3.12/site-packages/torch/_inductor/comms.py:2208:        resized_to_0_idxes = graph_input_to_resized_to_0_node_idxes.get(graph_input, [])
./venv/lib/python3.12/site-packages/torch/_inductor/utils.py:3404:    return _triton_type_mapping.get(triton_type_name, triton_type_name)
./venv/lib/python3.12/site-packages/torch/_inductor/utils.py:3408:    adjusted_type = _torch_triton_mapping.get(dtype, dtype)
./venv/lib/python3.12/site-packages/torch/_inductor/utils.py:3539:        return self.original_dict.get(key, default)
./venv/lib/python3.12/site-packages/torch/_inductor/utils.py:3855:        value = config_patches.get(config_name, getattr(config, config_name))
./venv/lib/python3.12/site-packages/torch/_inductor/utils.py:3866:        value = config_patches.get(config_name, getattr(config, config_name))
./venv/lib/python3.12/site-packages/torch/_inductor/async_compile.py:217:        return CompiledTritonKernels._cache.get(key, None)
./venv/lib/python3.12/site-packages/torch/_inductor/constant_folding.py:281:            for to_delete in self.user_to_last_uses.get(node, []):
./venv/lib/python3.12/site-packages/torch/_inductor/autotune_process.py:542:            assert os.environ.get(CUDA_VISIBLE_DEVICES, None) == str(self.device)
./venv/lib/python3.12/site-packages/torch/_inductor/graph.py:1988:            V.fake_mode.shape_env.unbacked_renamings.get(s, s)
./venv/lib/python3.12/site-packages/torch/_inductor/augmented_graph_helper.py:151:                updated_dep = erased_merge_sets.get(extra_dep, extra_dep)
./venv/lib/python3.12/site-packages/torch/_inductor/augmented_graph_helper.py:159:                updated_use = erased_merge_sets.get(extra_use, extra_use)
./venv/lib/python3.12/site-packages/torch/_inductor/fx_passes/ddp_fusion.py:314:            node_indices.get(node, last_wait_node_idx), last_wait_node_idx
./venv/lib/python3.12/site-packages/torch/_inductor/fx_passes/reinplace.py:285:        node_to_view_base[node] = node_to_view_base.get(inp, inp)  # type: ignore[arg-type, assignment]
./venv/lib/python3.12/site-packages/torch/_inductor/fx_passes/reinplace.py:311:            inp_base = node_to_view_base.get(inp, inp)  # type: ignore[arg-type]
./venv/lib/python3.12/site-packages/torch/_inductor/fx_passes/reinplace.py:312:            src_base = node_to_view_base.get(src_inp, src_inp)  # type: ignore[arg-type]
./venv/lib/python3.12/site-packages/torch/_inductor/fx_passes/control_dependencies.py:111:        updated_dep_nodes = [replacements.get(dep, dep) for dep in dep_nodes]
./venv/lib/python3.12/site-packages/torch/_inductor/fx_passes/bucketing.py:94:                n.meta[key] = bucket_nodes[0].meta.get(key, default)
./venv/lib/python3.12/site-packages/torch/_inductor/fx_passes/bucketing.py:102:                            node.meta.get(key, default)
./venv/lib/python3.12/site-packages/torch/_inductor/fx_passes/bucketing.py:104:                            if node.meta.get(key, default)
./venv/lib/python3.12/site-packages/torch/_inductor/fx_passes/bucketing.py:110:                        node.meta.get(key, default)
./venv/lib/python3.12/site-packages/torch/_inductor/fx_passes/bucketing.py:112:                        if node.meta.get(key, default)
./venv/lib/python3.12/site-packages/torch/_inductor/fx_passes/pre_grad.py:82:    return {p: dict(counters["inductor"]).get(p, 0) for p in pass_to_compare}
./venv/lib/python3.12/site-packages/torch/_inductor/fx_passes/pre_grad.py:87:        if count != dict(inductor_dict).get(pass_name, 0):
./venv/lib/python3.12/site-packages/torch/_inductor/fx_passes/b2b_gemm.py:478:            args, kwargs = tree_map(lambda x: env.get(x, x), (node.args, node.kwargs))
./venv/lib/python3.12/site-packages/torch/_inductor/fx_passes/b2b_gemm.py:692:            new_node = new_graph.node_copy(node, lambda x: node_remapping.get(x, x))
./venv/lib/python3.12/site-packages/torch/_inductor/fuzzer.py:440:        return self._vals.get(combo, None)
./venv/lib/python3.12/site-packages/torch/_inductor/wrapper_benchmark.py:297:                f"{per_category_wall_time.get(category, 0.0) / wall_time_ms * 100:.2f}%"
./venv/lib/python3.12/site-packages/torch/_inductor/codecache.py:309:                if choice_hash in cache.get(op, {}).get(cache_key, {}).get(
./venv/lib/python3.12/site-packages/torch/_inductor/codecache.py:1726:        return cls.cache.get(key, None)
./venv/lib/python3.12/site-packages/torch/_inductor/codecache.py:4162:                    binary_remote_cache.get(output_path, error_path)
./venv/lib/python3.12/site-packages/torch/_inductor/select_algorithm.py:1653:        entry = self._cache.get(cache_key, None)
./venv/lib/python3.12/site-packages/torch/_inductor/compiler_bisector.py:86:    return os.environ.get(env_str, None)
./venv/lib/python3.12/site-packages/torch/_inductor/compiler_bisector.py:471:                        f"Debug info: {call_counter_debug_info.get(low, 'not found')}"
./venv/lib/python3.12/site-packages/torch/_inductor/scheduler.py:639:        used_buffers = OrderedSet(mutation_real_name.get(k, k) for k in used_buffers)
./venv/lib/python3.12/site-packages/torch/_inductor/scheduler.py:3250:                        self.mutation_real_name.get(alt_name, alt_name)
./venv/lib/python3.12/site-packages/torch/_inductor/scheduler.py:3491:                c = children.get(dep, [])
./venv/lib/python3.12/site-packages/torch/_inductor/scheduler.py:3499:                for user in children.get(n, []):
./venv/lib/python3.12/site-packages/torch/_inductor/scheduler.py:5696:            buf = self.name_to_buf.get(buf_name, None)
./venv/lib/python3.12/site-packages/torch/_inductor/scheduler.py:5705:                if real_name := self.mutation_real_name.get(buf_name, None):
./venv/lib/python3.12/site-packages/torch/_inductor/scheduler.py:5742:                self.mutation_real_name.get(name, name)
./venv/lib/python3.12/site-packages/torch/_inductor/scheduler.py:5784:                self.mutation_real_name.get(name, name)
./venv/lib/python3.12/site-packages/torch/_inductor/lookup_table/choices.py:245:                config_list = lookup_table.get(key, [])
./venv/lib/python3.12/site-packages/torch/_inductor/codegen/pallas.py:1527:                    param_name = buf_to_param.get(buf_name, buf_name)
./venv/lib/python3.12/site-packages/torch/_inductor/codegen/pallas.py:1651:                    if aliasable_flags.get(name, False):
./venv/lib/python3.12/site-packages/torch/_inductor/codegen/pallas.py:1787:            if aliasable.get(p, False)
./venv/lib/python3.12/site-packages/torch/_inductor/codegen/cpp_wrapper_gpu.py:223:            if params.get(name, None) is not None
./venv/lib/python3.12/site-packages/torch/_inductor/codegen/triton.py:2440:                        self.kernel.tma_min_block_sizes.get(block_type_str, 1),
./venv/lib/python3.12/site-packages/torch/_inductor/codegen/triton.py:5638:        pid = entry.pid_cache.get(key, key)
./venv/lib/python3.12/site-packages/torch/_inductor/codegen/rocm/ck_universal_gemm_template.py:395:        dimension_padding = padding_lookup.get(dimension, {})
./venv/lib/python3.12/site-packages/torch/_inductor/codegen/rocm/ck_universal_gemm_template.py:398:        return dimension_padding.get(gemm_specialization, False)
./venv/lib/python3.12/site-packages/torch/_inductor/codegen/common.py:1497:        result: Union[str, RemovedArg] = odict.get(name, REMOVED)
./venv/lib/python3.12/site-packages/torch/_inductor/codegen/common.py:1532:            name = V.graph.scheduler.mutation_real_name.get(name, name)
./venv/lib/python3.12/site-packages/torch/_inductor/codegen/common.py:1544:            name = V.graph.scheduler.mutation_real_name.get(name, name)
./venv/lib/python3.12/site-packages/torch/_inductor/codegen/common.py:1682:        inplaced = self.inplace_buffers.get(name, None)
./venv/lib/python3.12/site-packages/torch/_inductor/codegen/common.py:1685:        output_name = self.output_buffers.get(name, None)
./venv/lib/python3.12/site-packages/torch/_inductor/codegen/common.py:1688:        return self.input_buffers.get(name, None)
./venv/lib/python3.12/site-packages/torch/_inductor/codegen/common.py:1818:            self.output_buffers.get(name, REMOVED), RemovedArg
./venv/lib/python3.12/site-packages/torch/_inductor/codegen/common.py:1819:        ) and isinstance(self.inplace_buffers.get(name, REMOVED), RemovedArg)
./venv/lib/python3.12/site-packages/torch/_inductor/codegen/common.py:2676:            return self.kernel.node_to_bounds.get(fx_node, ValueRanges.unknown())
./venv/lib/python3.12/site-packages/torch/_inductor/codegen/cuda/cutlass_lib_extensions/evt_extensions.py:79:            return self.buf_renames.get(name, name)
./venv/lib/python3.12/site-packages/torch/_inductor/codegen/simd.py:2752:                    split_scores.append(coalesce_analysis.coalesced_by_var.get(v, 0))
./venv/lib/python3.12/site-packages/torch/_inductor/codegen/simd.py:2761:                split_scores.append(coalesce_analysis.coalesced_by_var.get(v, 0))
./venv/lib/python3.12/site-packages/torch/_inductor/codegen/wrapper.py:402:        return bool(self.reuse_pool.get(key, None))
./venv/lib/python3.12/site-packages/torch/_inductor/codegen/wrapper.py:2233:                    V.graph.sizevars.var_to_val.get(value, None), SingletonInt
./venv/lib/python3.12/site-packages/torch/_inductor/codegen/cutedsl/cutedsl_kernel.py:316:        output = self.args.output_buffers.get(buf_name, None)
./venv/lib/python3.12/site-packages/torch/_inductor/codegen/halide.py:624:        return self.index_str([replacements.get(n, n) for n in self.used_dims])
./venv/lib/python3.12/site-packages/torch/_logging/_internal.py:505:                    log_registry.log_alias_to_log_qnames.get(alias, alias), val
./venv/lib/python3.12/site-packages/torch/_logging/_internal.py:513:                    log_registry.log_alias_to_log_qnames.get(alias, alias), val
./venv/lib/python3.12/site-packages/torch/_logging/_internal.py:832:    log_setting = os.environ.get(LOG_ENV_VAR, None)
./venv/lib/python3.12/site-packages/torch/_logging/_internal.py:966:    fmt = os.environ.get(LOG_FORMAT_ENV_VAR, None)
./venv/lib/python3.12/site-packages/torch/_logging/_internal.py:969:        for item in os.environ.get(LOG_TRACE_ID_FILTER, "").split(",")
./venv/lib/python3.12/site-packages/torch/_logging/_internal.py:1046:    out = os.environ.get(LOG_OUT_ENV_VAR, None)
./venv/lib/python3.12/site-packages/torch/_logging/_internal.py:1088:    trace_dir_name = os.environ.get(TRACE_ENV_VAR, None)
./venv/lib/python3.12/site-packages/torch/_logging/_internal.py:1090:    if dtrace_dir_name := os.environ.get(DTRACE_ENV_VAR, None):
./venv/lib/python3.12/site-packages/torch/amp/grad_scaler.py:31:        retval = self._per_device_tensors.get(device, None)
./venv/lib/python3.12/site-packages/torch/utils/_config_module.py:191:            annotated_type = type_hints.get(key, None)
./venv/lib/python3.12/site-packages/torch/utils/_functools.py:40:        cached_value = cache.get(args, _cache_sentinel)
./venv/lib/python3.12/site-packages/torch/utils/checkpoint.py:1113:                _internal_assert(holder.handles.get(gid, None) is None)
./venv/lib/python3.12/site-packages/torch/utils/viz/_cycles.py:285:            labels = references.get(rid, ["?"])
./venv/lib/python3.12/site-packages/torch/utils/_sympy/interp.py:206:        if (r := env.get(expr, _nil)) is not _nil:
./venv/lib/python3.12/site-packages/torch/utils/benchmark/utils/fuzzer.py:320:            values = tuple(params.get(i, i) for i in values)
./venv/lib/python3.12/site-packages/torch/utils/hipify/hipify_python.py:805:            if constants.API_SPECIAL in meta_data and PYTORCH_MAP.get(src, ""):
./venv/lib/python3.12/site-packages/torch/utils/data/datapipes/_typing.py:71:    left = TYPE2ABC.get(left, left)
./venv/lib/python3.12/site-packages/torch/utils/data/datapipes/_typing.py:72:    right = TYPE2ABC.get(right, right)
./venv/lib/python3.12/site-packages/torch/utils/data/datapipes/_typing.py:120:    ts = [TYPE2ABC.get(_t, _t) for _t in ts]  # type: ignore[misc]
./venv/lib/python3.12/site-packages/torch/utils/flop_counter.py:848:                    true_val = true_func_counts.get(func_key, 0)
./venv/lib/python3.12/site-packages/torch/utils/flop_counter.py:849:                    false_val = false_func_counts.get(func_key, 0)
./venv/lib/python3.12/site-packages/torch/_subclasses/complex_tensor/_ops/aten.py:499:        err_op, ERROR_TYPES.get(err_op, NotImplementedError)
./venv/lib/python3.12/site-packages/torch/_subclasses/complex_tensor/_ops/common.py:83:    prom_dt = PROMOTE_TYPES.get(out_dt, out_dt)
./venv/lib/python3.12/site-packages/torch/_subclasses/complex_tensor/_ops/common.py:97:        if COMPLEX_OPS_TABLE.get(op, func) is not func:
./venv/lib/python3.12/site-packages/torch/_subclasses/complex_tensor/_ops/common.py:132:            DECOMPOSITIONS.get(func, DECOMPOSITIONS.get(func.overloadpacket)),
./venv/lib/python3.12/site-packages/torch/_subclasses/complex_tensor/_ops/common.py:187:    return COMPLEX_TO_REAL.get(dtype, dtype)
./venv/lib/python3.12/site-packages/torch/_subclasses/fake_tensor.py:1520:        entry = cache.get(key, None)
./venv/lib/python3.12/site-packages/torch/nn/modules/module.py:1760:            name = torch.jit._trace._trace_module_map.get(self, None)  # type: ignore[operator, union-attr]
./venv/lib/python3.12/site-packages/torch/nn/parallel/distributed.py:221:        value = os.environ.get(var, "N/A")
./venv/lib/python3.12/site-packages/torch/nn/parallel/distributed.py:1058:                for handle in param_to_handle_map.get(p, []):
./venv/lib/python3.12/site-packages/torch/jit/frontend.py:170:        range_len = len(node_start_tokens.get(node_type, " "))
./venv/lib/python3.12/site-packages/torch/jit/frontend.py:176:        feature_name = pretty_node_names.get(node_type, node_type.__name__)
./venv/lib/python3.12/site-packages/torch/jit/_state.py:104:    qual_names = _jit_function_overload_caching.get(key, None)
./venv/lib/python3.12/site-packages/torch/jit/_state.py:118:    qual_name = _jit_caching_layer.get(key, None)
./venv/lib/python3.12/site-packages/torch/testing/_internal/common_device_type.py:386:        return test.precision_overrides.get(dtype, self.precision)
./venv/lib/python3.12/site-packages/torch/testing/_internal/common_device_type.py:391:        return test.tolerance_overrides.get(dtype, tol(self.precision, self.rel_tol))
./venv/lib/python3.12/site-packages/torch/testing/_internal/distributed/common_state_dict.py:74:            dist_states = dist_osd[_STATE].get(fqn, None)
./venv/lib/python3.12/site-packages/torch/testing/_internal/distributed/common_state_dict.py:78:                dist_state = states.get(key, None)
./venv/lib/python3.12/site-packages/torch/testing/_internal/distributed/common_state_dict.py:98:                # dist_value = dist_group.get(key, None)
./venv/lib/python3.12/site-packages/torch/testing/_internal/distributed/distributed_test.py:611:            pg_timeout_seconds = CUSTOM_PG_TIMEOUT.get(test_name, default_pg_timeout)
./venv/lib/python3.12/site-packages/torch/testing/_internal/distributed/distributed_test.py:725:                return f"env:{var}={os.environ.get(var, 'N/A')}"
./venv/lib/python3.12/site-packages/torch/testing/_internal/distributed/distributed_test.py:6224:                return os.environ.get(var, "N/A")
./venv/lib/python3.12/site-packages/torch/testing/_internal/common_modules.py:560:        v = kwargs.get(key, default)
./venv/lib/python3.12/site-packages/torch/testing/_internal/opinfo/definitions/nested.py:453:        dimlist_argname, sample.kwargs.get(single_dim_argname, None)
./venv/lib/python3.12/site-packages/torch/testing/_internal/opinfo/definitions/linalg.py:389:                    }.get(ord, ())
./venv/lib/python3.12/site-packages/torch/testing/_internal/opinfo/definitions/linalg.py:400:                    }.get(ord, ())
./venv/lib/python3.12/site-packages/torch/testing/_internal/opinfo/core.py:1537:        result = self.dtypesIf.get(device_type, self.dtypes)
./venv/lib/python3.12/site-packages/torch/testing/_internal/common_nn.py:2716:        extra_info = non_linear_activations_extra_info.get(non_linear_activation, {})
./venv/lib/python3.12/site-packages/torch/testing/_internal/common_nn.py:3203:        has_parity=classification_cpp_parity.get(name, True)
./venv/lib/python3.12/site-packages/torch/testing/_internal/common_nn.py:3205:    extra_info = classification_criterion_no_batch_extra_info.get(name, {})
./venv/lib/python3.12/site-packages/torch/testing/_internal/common_utils.py:5015:            aik, ajk = data.get(ik, 0), data.get(jk, 0)
./venv/lib/python3.12/site-packages/torch/testing/_internal/common_distributed.py:458:        }.get(backend, lambda: False)()
./venv/lib/python3.12/site-packages/torch/testing/_comparison.py:96:        *[dtype_precisions.get(dtype, (0.0, 0.0)) for dtype in dtypes], strict=True
./venv/lib/python3.12/site-packages/torch/_ops.py:969:        r = self.py_kernels.get(final_key, final_key)
./venv/lib/python3.12/site-packages/torch/backends/quantized/__init__.py:29:    return all_engines.get(qengine, "*undefined")
./venv/lib/python3.12/site-packages/torch/autograd/profiler_util.py:233:                evt.stack = fwd_stacks.get(t, [])
./venv/lib/python3.12/site-packages/torch/autograd/graph.py:544:                count[id] = count.get(id, 0)
./venv/lib/python3.12/site-packages/torch/autograd/graph.py:546:                buffer[id] = buffer.get(id, [None] * len_tensors)
./venv/lib/python3.12/site-packages/torch/cuda/_memory_viz.py:376:                name, _, _ = allocation_addr_to_name.get(addr, (addr, None, None))
./venv/lib/python3.12/site-packages/torch/cuda/_memory_viz.py:381:                name, _, _ = allocation_addr_to_name.get(addr, (addr, None, None))
./venv/lib/python3.12/site-packages/torch/cuda/_memory_viz.py:394:                name = segment_addr_to_name.get(addr, addr)
./venv/lib/python3.12/site-packages/torch/cuda/_memory_viz.py:565:        category = memory_profile._categories.get(tensor_key, version)
./venv/lib/python3.12/site-packages/torch/cuda/_memory_viz.py:567:        stack = allocation_stacks.get(tensor_key, ())
./venv/lib/python3.12/site-packages/torch/cuda/_sanitizer.py:295:            state[stream] = max(state.get(stream, -1), seq_num)
./venv/lib/python3.12/site-packages/torch/cuda/_sanitizer.py:334:        return seq_num <= self.current_sync_states[current_stream].get(other_stream, -1)
./venv/lib/python3.12/site-packages/torch/onnx/_internal/exporter/_registration.py:272:        decomps = self.functions.get(target_or_name, [])
./venv/lib/python3.12/site-packages/torch/onnx/_internal/fx/passes/type_promotion.py:1553:                    node, arg, type_promotion_info.args_dtypes.get(i, None)
./venv/lib/python3.12/site-packages/torch/onnx/_internal/fx/passes/type_promotion.py:1559:                node, arg, type_promotion_info.kwargs_dtypes.get(name, None)
./venv/lib/python3.12/site-packages/torch/onnx/_internal/fx/type_utils.py:80:    return _TORCH_DTYPE_TO_ABBREVIATION.get(dtype, "")
./venv/lib/python3.12/site-packages/torch/onnx/_internal/torchscript_exporter/registration.py:100:        return self._merged.get(key, default)
./venv/lib/python3.12/site-packages/torch/_dynamo/cache_size.py:105:    obj = frame.f_locals.get(local_name, None)
./venv/lib/python3.12/site-packages/torch/_dynamo/polyfills/pytree.py:486:    handler = optree.register_pytree_node.get(tuple, namespace=namespace)
./venv/lib/python3.12/site-packages/torch/_dynamo/side_effects.py:357:        ) and name in self.store_attr_mutations.get(item, ())
./venv/lib/python3.12/site-packages/torch/_dynamo/side_effects.py:1099:                    self.store_attr_mutations.get(var, {}).items()
./venv/lib/python3.12/site-packages/torch/_dynamo/symbolic_convert.py:4507:                        local_dynamism = frozenset(dynamism.get(name, {}).items())
./venv/lib/python3.12/site-packages/torch/_dynamo/variables/nn_module.py:134:    num_calls = tx.num_calls.get(fully_qualified_name, 0)
./venv/lib/python3.12/site-packages/torch/_dynamo/variables/functions.py:2423:        handler = self._get_polyfill_handlers().get(fn, fn)
./venv/lib/python3.12/site-packages/torch/_dynamo/variables/misc.py:153:            if resolved_getattr := search_mro[index].__dict__.get(name, NO_SUCH_SUBOBJ):
./venv/lib/python3.12/site-packages/torch/_dynamo/variables/builder.py:2488:                and dict(base_source.dynamism).get(normalized_source_name, {0: False})[
./venv/lib/python3.12/site-packages/torch/_dynamo/variables/builder.py:3342:            stride[i] = candidates.get(i_stride, i_stride)
./venv/lib/python3.12/site-packages/torch/_dynamo/variables/builder.py:3406:    prior_policy = tx.output.tracing_context.tensor_to_context.get(e, None)
./venv/lib/python3.12/site-packages/torch/_dynamo/variables/builder.py:3523:        specialize_on.append(getattr(e, "_specialize_on", {}).get(i, []))
./venv/lib/python3.12/site-packages/torch/_dynamo/variables/builder.py:3536:            and dict(base_source.dynamism).get(normalized_source_name, {i: False})[i]
./venv/lib/python3.12/site-packages/torch/_dynamo/variables/tensor.py:517:                static_attr = all_tensor_attrs.get(name, None)
./venv/lib/python3.12/site-packages/torch/_dynamo/variables/tensor.py:671:        static_attr = all_tensor_attrs.get(name, None)
./venv/lib/python3.12/site-packages/torch/_dynamo/variables/tensor.py:1650:            kwargs = {kwargs_rename.get(k, k): v for k, v in kwargs.items()}
./venv/lib/python3.12/site-packages/torch/_dynamo/debug_utils.py:848:        return sym_shapes_dict.get(symint, default_sym_shape)  # type: ignore[return-value]
./venv/lib/python3.12/site-packages/torch/_dynamo/funcname_cache.py:75:    return cache[filename].get(lineno, None)
./venv/lib/python3.12/site-packages/torch/_dynamo/codegen.py:203:            source = self.overridden_sources.get(value, value)
./venv/lib/python3.12/site-packages/torch/_dynamo/codegen.py:581:        if global_scope.get(name, None) is mod:
./venv/lib/python3.12/site-packages/torch/_dynamo/trace_rules.py:3125:        return self.function_names.get(idx, default)
./venv/lib/python3.12/site-packages/torch/_dynamo/trace_rules.py:3974:        rule = get_torch_obj_rule_map().get(obj, None)
./venv/lib/python3.12/site-packages/jinja2/lexer.py:182:    }.get(token_type, token_type)
./venv/lib/python3.12/site-packages/jinja2/debug.py:179:        cur_depth = local_overrides.get(name, (-1,))[0]
./venv/lib/python3.12/site-packages/jinja2/ext.py:825:        return options.get(key, str(default)).lower() in {"1", "on", "yes", "true"}
./venv/lib/python3.12/site-packages/jinja2/nodes.py:63:            storage.extend(d.get(attr, ()))
./venv/lib/python3.12/site-packages/scipy/optimize/_optimize.py:2433:                                     2: _status_message['nan']}.get(flag, ''),
./venv/lib/python3.12/site-packages/scipy/optimize/_tnc.py:262:                    4:MSG_EXIT, 5:MSG_ALL}.get(messages, MSG_ALL)
./venv/lib/python3.12/site-packages/scipy/optimize/_tnc.py:383:                    4:MSG_EXIT, 5:MSG_ALL}.get(mesg_num, MSG_ALL)
./venv/lib/python3.12/site-packages/scipy/optimize/_tstutils.py:127:    v = _f6_cache.get(x, None)
./venv/lib/python3.12/site-packages/scipy/optimize/_tstutils.py:844:    tests = subsets.get(collection, [])
./venv/lib/python3.12/site-packages/scipy/optimize/_root_scalar.py:276:        methodc = getattr(optzeros, map2underlying.get(meth, meth))
./venv/lib/python3.12/site-packages/scipy/optimize/_highspy/_highs_wrapper.py:320:    expected_type = valid_types.get(option_type, None)
./venv/lib/python3.12/site-packages/scipy/optimize/tests/test_zeros.py:81:                k = {'a': 'x0', 'b': 'x1', 'func': 'f'}.get(k, k)
./venv/lib/python3.12/site-packages/scipy/optimize/_linprog_highs.py:57:        scipy_statuses_messages.get(highs_status, unrecognized))
./venv/lib/python3.12/site-packages/scipy/optimize/_nonlin.py:1481:            ).get(method, method)
./venv/lib/python3.12/site-packages/scipy/sparse/_dok.py:170:        return self._dict.get(key, default)
./venv/lib/python3.12/site-packages/scipy/sparse/_dok.py:174:        return self._dict.get(idx, self.dtype.type(0))
./venv/lib/python3.12/site-packages/scipy/sparse/_dok.py:186:        dok_vals = [self._dict.get(i, 0) for i in idx.ravel()]
./venv/lib/python3.12/site-packages/scipy/sparse/_dok.py:319:                aij = self._dict.get(key, 0) + other
./venv/lib/python3.12/site-packages/scipy/sparse/linalg/_eigen/arpack/arpack.py:288:        msg = infodict.get(info, "Unknown error")
./venv/lib/python3.12/site-packages/scipy/linalg/_basic.py:229:    }.get(assume_a, 'unknown')
./venv/lib/python3.12/site-packages/scipy/linalg/_basic.py:733:    trans = {'N': 0, 'T': 1, 'C': 2}.get(trans, trans)
./venv/lib/python3.12/site-packages/scipy/linalg/blas.py:332:    prefix, dtype = _type_conv.get(max_score, ('d', np.dtype('float64')))
./venv/lib/python3.12/site-packages/scipy/linalg/blas.py:364:        func_name = alias.get(func_name, func_name)
./venv/lib/python3.12/site-packages/scipy/stats/_new_distributions.py:193:        return raw_moments.get(order, None)
./venv/lib/python3.12/site-packages/scipy/stats/_axis_nan_policy.py:497:                        if kwds.get(name, None) is not None]
./venv/lib/python3.12/site-packages/scipy/stats/_distribution_infrastructure.py:339:                a = np.asarray(parameter_values.get(a, a))
./venv/lib/python3.12/site-packages/scipy/stats/_distribution_infrastructure.py:343:                b = np.asarray(parameter_values.get(b, b))
./venv/lib/python3.12/site-packages/scipy/stats/_distribution_infrastructure.py:486:        return self.symbols.get(endpoint, f"{endpoint}")
./venv/lib/python3.12/site-packages/scipy/stats/_distribution_infrastructure.py:519:        a = self.symbols.get(a, a)
./venv/lib/python3.12/site-packages/scipy/stats/_distribution_infrastructure.py:520:        b = self.symbols.get(b, b)
./venv/lib/python3.12/site-packages/scipy/stats/_distribution_infrastructure.py:985:        low, high = endpoints.get(method_name, self.support())
./venv/lib/python3.12/site-packages/scipy/stats/_distribution_infrastructure.py:1048:                replacements.get(method_name, (np.nan, np.nan)))
./venv/lib/python3.12/site-packages/scipy/stats/_distribution_infrastructure.py:1147:        method = method or self._method_cache.get(func_name, None)
./venv/lib/python3.12/site-packages/scipy/stats/_distribution_infrastructure.py:3165:            moment = self._moment_raw_cache.get(order, None)
./venv/lib/python3.12/site-packages/scipy/stats/_distribution_infrastructure.py:3223:            moment = self._moment_central_cache.get(order, None)
./venv/lib/python3.12/site-packages/scipy/stats/_distribution_infrastructure.py:3282:        return general_central_moments.get(order, None)
./venv/lib/python3.12/site-packages/scipy/stats/_distribution_infrastructure.py:3294:            moment = self._moment_standardized_cache.get(order, None)
./venv/lib/python3.12/site-packages/scipy/stats/_distribution_infrastructure.py:3329:        return general_standard_moments.get(order, None)
./venv/lib/python3.12/site-packages/scipy/stats/tests/test_continuous.py:132:        a = _Domain.symbols.get(a, a)
./venv/lib/python3.12/site-packages/scipy/stats/tests/test_continuous.py:133:        b = _Domain.symbols.get(b, b)
./venv/lib/python3.12/site-packages/scipy/stats/tests/test_continuous.py:1146:        rtol = custom_tolerances.get(distname, 1e-7)
./venv/lib/python3.12/site-packages/scipy/stats/tests/test_continuous.py:1190:                if distname not in skip_raw.get(order, {}):
./venv/lib/python3.12/site-packages/scipy/stats/tests/test_discrete_basic.py:74:        k = spec_k.get(distname, 1)
./venv/lib/python3.12/site-packages/scipy/stats/tests/test_discrete_basic.py:394:            if (shape.name in integrality_exceptions.get(distname, set()) or
./venv/lib/python3.12/site-packages/scipy/stats/tests/test_continuous_basic.py:167:    x = spec_x.get(distname, 0.5)
./venv/lib/python3.12/site-packages/scipy/special/_basic.py:2837:    dtypes = [mapping.get(x, x) for x in dtypes]
./venv/lib/python3.12/site-packages/scipy/special/tests/test_basic.py:2982:            n = np.array([_FACTORIALK_LIMITS_64BITS.get(k, 1)])
./venv/lib/python3.12/site-packages/scipy/integrate/_ode.py:998:                          f'{self.messages.get(istate, unexpected_istate_msg):s}',
./venv/lib/python3.12/site-packages/scipy/integrate/_ode.py:1180:                          f'{self.messages.get(istate, unexpected_istate_msg):s}',
./venv/lib/python3.12/site-packages/scipy/integrate/_ode.py:1384:                          f'{self.messages.get(istate, unexpected_istate_msg):s}',
./venv/lib/python3.12/site-packages/scipy/integrate/_ivp/ivp.py:730:    message = MESSAGES.get(status, message)
./venv/lib/python3.12/site-packages/scipy/interpolate/_rbfinterp.py:291:        min_degree = _NAME_TO_MIN_DEGREE.get(kernel, -1)
./venv/lib/python3.12/site-packages/scipy/interpolate/_fitpack2.py:321:            message = _curfit_messages.get(ier, f'ier={ier}')
./venv/lib/python3.12/site-packages/scipy/interpolate/_fitpack2.py:1451:            message = _surfit_messages.get(ier, f'ier={ier}')
./venv/lib/python3.12/site-packages/scipy/interpolate/_fitpack2.py:1553:                message = _surfit_messages.get(ier, f'ier={ier}')
./venv/lib/python3.12/site-packages/scipy/interpolate/_fitpack2.py:1645:            msg = _surfit_messages.get(ier, f'ier={ier}')
./venv/lib/python3.12/site-packages/scipy/interpolate/_fitpack2.py:1969:            message = _spherefit_messages.get(ier, f'ier={ier}')
./venv/lib/python3.12/site-packages/scipy/interpolate/_fitpack2.py:2125:            message = _spherefit_messages.get(ier, f'ier={ier}')
./venv/lib/python3.12/site-packages/scipy/interpolate/_fitpack2.py:2394:            msg = _spfit_messages.get(ier, f'ier={ier}')
./venv/lib/python3.12/site-packages/scipy/interpolate/tests/test_rbfinterp.py:82:    m = _NAME_TO_MIN_DEGREE.get(kernel, -1) + 1
./venv/lib/python3.12/site-packages/scipy/interpolate/tests/test_rbf.py:131:        check_rbf1d_regularity(function, tolerances.get(function, 1e-2))
./venv/lib/python3.12/site-packages/scipy/interpolate/tests/test_rbf.py:159:        check_2drbf1d_regularity(function, tolerances.get(function, 1e-2))
./venv/lib/python3.12/site-packages/scipy/spatial/distance.py:2125:        metric_info = _METRIC_ALIAS.get(mstr, None)
./venv/lib/python3.12/site-packages/scipy/spatial/distance.py:2134:        metric_info = _METRIC_ALIAS.get(mstr, None)
./venv/lib/python3.12/site-packages/scipy/spatial/distance.py:2140:            metric_info = _TEST_METRICS.get(mstr, None)
./venv/lib/python3.12/site-packages/scipy/spatial/distance.py:2916:        metric_info = _METRIC_ALIAS.get(mstr, None)
./venv/lib/python3.12/site-packages/scipy/spatial/distance.py:2923:        metric_info = _METRIC_ALIAS.get(mstr, None)
./venv/lib/python3.12/site-packages/scipy/spatial/distance.py:2928:            metric_info = _TEST_METRICS.get(mstr, None)
./venv/lib/python3.12/site-packages/scipy/spatial/transform/_rotation.py:37:    return backend_registry.get(xp, xp_backend)
./venv/lib/python3.12/site-packages/scipy/spatial/transform/_rigid_transform.py:41:    return backend_registry.get(xp, xp_backend)
./venv/lib/python3.12/site-packages/scipy/spatial/tests/test_distance.py:292:        weights = kwargs.get(weight_arg, None)
./venv/lib/python3.12/site-packages/scipy/_lib/array_api_extra/testing.py:379:        return dask.get(dsk, keys, **kwargs)  # type: ignore[attr-defined]  # pyright: ignore[reportPrivateImportUsage]
./venv/lib/python3.12/site-packages/scipy/_lib/_pep440.py:209:        part = _legacy_version_replacement_map.get(part, part)
./venv/lib/python3.12/site-packages/scipy/_lib/_array_api_docs_tables.py:137:        backend = BACKEND_NAMES_MAP.get(backend, backend)
./venv/lib/python3.12/site-packages/scipy/_lib/_array_api_docs_tables.py:223:            if name in ALIASES.get(module_name, {}):
./venv/lib/python3.12/site-packages/scipy/_lib/_array_api_docs_tables.py:230:            entry = xp_capabilities_table.get(thing, None)
./venv/lib/python3.12/site-packages/scipy/_lib/cobyqa/main.py:1468:    }.get(status, "Unknown exit status")
./venv/lib/python3.12/site-packages/scipy/io/_fast_matrix_market/__init__.py:276:    dtype = _field_to_dtype.get(field, None)
./venv/lib/python3.12/site-packages/scipy/io/_mmio.py:557:                }.get(field, None)
./venv/lib/python3.12/site-packages/scipy/io/_mmio.py:662:        dtype = self.DTYPES_BY_FIELD.get(field, None)
./venv/lib/python3.12/site-packages/scipy/ndimage/_support_alternative_backends.py:113:    capabilities = capabilities_dict.get(func_name, default_capabilities)
./venv/lib/python3.12/site-packages/scipy/ndimage/_filters.py:140:    mode = mode_map.get(mode, mode)
./venv/lib/python3.12/site-packages/typing_extensions.py:3968:                module = sys.modules.get(module_name, None)
./venv/lib/python3.12/site-packages/typing_extensions.py:4073:                    module = sys.modules.get(module_name, None)
./venv/lib/python3.12/site-packages/pip/_vendor/packaging/markers.py:212:    value: Union[str, Undefined] = environment.get(name, _undefined)
./venv/lib/python3.12/site-packages/pip/_vendor/packaging/version.py:181:        part = _legacy_version_replacement_map.get(part, part)
./venv/lib/python3.12/site-packages/pip/_vendor/requests/utils.py:876:        proxy = environ_proxies.get(scheme, environ_proxies.get("all"))
./venv/lib/python3.12/site-packages/pip/_vendor/requests/structures.py:96:        return self.__dict__.get(key, None)
./venv/lib/python3.12/site-packages/pip/_vendor/requests/structures.py:99:        return self.__dict__.get(key, default)
./venv/lib/python3.12/site-packages/pip/_vendor/requests/cookies.py:76:        return self._r.headers.get(name, self._new_headers.get(name, default))
./venv/lib/python3.12/site-packages/pip/_vendor/urllib3/response.py:672:            "in urllib3 v2.1.0. Instead use HTTPResponse.headers.get(name, default).",
./venv/lib/python3.12/site-packages/pip/_vendor/urllib3/response.py:676:        return self.headers.get(name, default)
./venv/lib/python3.12/site-packages/pip/_vendor/urllib3/connectionpool.py:1104:    port = port or port_by_scheme.get(scheme, 80)
./venv/lib/python3.12/site-packages/pip/_vendor/urllib3/_collections.py:65:            evicted_value = self._container.get(key, _Null)
./venv/lib/python3.12/site-packages/pip/_vendor/urllib3/fields.py:238:            if self.headers.get(sort_key, False):
./venv/lib/python3.12/site-packages/pip/_vendor/chardet/chardistribution.py:179:            return JOHAB_TO_EUCKR_ORDER_TABLE.get(code, -1)
./venv/lib/python3.12/site-packages/pip/_vendor/chardet/sbcharsetprober.py:105:            order = char_to_order_map.get(char, CharacterCategory.UNDEFINED)
./venv/lib/python3.12/site-packages/pip/_vendor/webencodings/__init__.py:83:            python_name = PYTHON_NAMES.get(name, name)
./venv/lib/python3.12/site-packages/pip/_vendor/cachecontrol/cache.py:40:        return self.data.get(key, None)
./venv/lib/python3.12/site-packages/pip/_vendor/cachecontrol/serialize.py:55:                header_value = request.headers.get(header, None)
./venv/lib/python3.12/site-packages/pip/_vendor/cachecontrol/serialize.py:119:            if request.headers.get(header, None) != value:
./venv/lib/python3.12/site-packages/pip/_vendor/rich/_emoji_replace.py:21:    default_variant_code = variants.get(default_variant, "") if default_variant else ""
./venv/lib/python3.12/site-packages/pip/_vendor/rich/emoji.py:55:            self._char += self.VARIANTS.get(variant, "")
./venv/lib/python3.12/site-packages/pip/_vendor/rich/padding.py:87:                Measurement.get(console, options, self.renderable).maximum
./venv/lib/python3.12/site-packages/pip/_vendor/rich/padding.py:132:        measure_min, measure_max = Measurement.get(console, options, self.renderable)
./venv/lib/python3.12/site-packages/pip/_vendor/rich/styled.py:34:        return Measurement.get(console, options, self.renderable)
./venv/lib/python3.12/site-packages/pip/_vendor/rich/align.py:230:        measurement = Measurement.get(console, options, self.renderable)
./venv/lib/python3.12/site-packages/pip/_vendor/rich/align.py:286:        measurement = Measurement.get(console, options, self.renderable)
./venv/lib/python3.12/site-packages/pip/_vendor/rich/spinner.py:58:        return Measurement.get(console, options, text)
./venv/lib/python3.12/site-packages/pip/_vendor/rich/console.py:812:            color_system = _TERM_COLORS.get(colors, ColorSystem.STANDARD)
./venv/lib/python3.12/site-packages/pip/_vendor/rich/console.py:1283:        measurement = Measurement.get(self, options or self.options, renderable)
./venv/lib/python3.12/site-packages/pip/_vendor/rich/containers.py:50:            Measurement.get(console, options, renderable)
./venv/lib/python3.12/site-packages/pip/_vendor/rich/box.py:86:            box = LEGACY_WINDOWS_SUBSTITUTIONS.get(box, box)
./venv/lib/python3.12/site-packages/pip/_vendor/rich/box.py:99:        return PLAIN_HEADED_SUBSTITUTIONS.get(self, self)
./venv/lib/python3.12/site-packages/pip/_vendor/rich/constrain.py:36:        measurement = Measurement.get(console, options, self.renderable)
./venv/lib/python3.12/site-packages/pip/_vendor/distro/distro.py:837:            return table.get(distro_id, distro_id)
./venv/lib/python3.12/site-packages/pip/_vendor/distro/distro.py:1057:        return self._os_release_info.get(attribute, "")
./venv/lib/python3.12/site-packages/pip/_vendor/distro/distro.py:1066:        return self._lsb_release_info.get(attribute, "")
./venv/lib/python3.12/site-packages/pip/_vendor/distro/distro.py:1075:        return self._distro_release_info.get(attribute, "")
./venv/lib/python3.12/site-packages/pip/_vendor/distro/distro.py:1084:        return self._uname_info.get(attribute, "")
./venv/lib/python3.12/site-packages/pip/_vendor/pkg_resources/__init__.py:427:    return {'PowerPC': 'ppc', 'Power_Macintosh': 'ppc'}.get(machine, machine)
./venv/lib/python3.12/site-packages/pip/_vendor/pkg_resources/__init__.py:869:                    requirers = required_by.get(req, None)
./venv/lib/python3.12/site-packages/pip/_vendor/pkg_resources/__init__.py:1026:            for extra in self.get(req, ()) + (extras or (None,))
./venv/lib/python3.12/site-packages/pip/_vendor/pkg_resources/__init__.py:1100:        return self._distmap.get(distribution_key, [])
./venv/lib/python3.12/site-packages/pip/_vendor/pkg_resources/__init__.py:2376:        for package in _namespace_packages.get(parent, ()):
./venv/lib/python3.12/site-packages/pip/_vendor/pkg_resources/__init__.py:2824:        deps.extend(dm.get(None, ()))
./venv/lib/python3.12/site-packages/pip/_vendor/pkg_resources/__init__.py:2942:            return ep_map.get(group, {})
./venv/lib/python3.12/site-packages/pip/_vendor/pygments/style.py:88:                styledefs = obj.styles.get(token, '').split()
./venv/lib/python3.12/site-packages/pip/_vendor/pygments/style.py:96:                for styledef in obj.styles.get(token, '').split():
./venv/lib/python3.12/site-packages/pip/_vendor/pygments/util.py:45:    string = options.get(optname, default)
./venv/lib/python3.12/site-packages/pip/_vendor/pygments/util.py:56:    Intuitively, this is `options.get(optname, default)`, but restricted to
./venv/lib/python3.12/site-packages/pip/_vendor/pygments/util.py:66:    string = options.get(optname, default)
./venv/lib/python3.12/site-packages/pip/_vendor/pygments/util.py:87:    string = options.get(optname, default)
./venv/lib/python3.12/site-packages/pip/_vendor/pygments/util.py:105:    val = options.get(optname, default)
./venv/lib/python3.12/site-packages/pip/_vendor/pygments/formatters/terminal256.py:206:        index = self.best_match.get(color, None)
./venv/lib/python3.12/site-packages/pip/_vendor/pygments/filters/__init__.py:824:            opt = options.get(name, False)
./venv/lib/python3.12/site-packages/pip/_vendor/pygments/plugin.py:68:        return groups.get(group_name, [])
./venv/lib/python3.12/site-packages/pip/_vendor/resolvelib/structs.py:98:        return itertools.chain(self._accessor(v), self._appends.get(k, ()))
./venv/lib/python3.12/site-packages/pip/_vendor/pyparsing/results.py:215:            self._tokdict[k] = self._tokdict.get(k, list()) + [v]
./venv/lib/python3.12/site-packages/pip/_vendor/pyparsing/results.py:221:            self._tokdict[k] = self._tokdict.get(k, list()) + [
./venv/lib/python3.12/site-packages/pip/_vendor/distlib/util.py:1074:        return iter(self._subscribers.get(event, ()))
./venv/lib/python3.12/site-packages/pip/_vendor/distlib/util.py:1117:            for p in set(self._preds.get(node, ())):
./venv/lib/python3.12/site-packages/pip/_vendor/distlib/util.py:1119:            for s in set(self._succs.get(node, ())):
./venv/lib/python3.12/site-packages/pip/_vendor/distlib/util.py:1172:                preds = self._preds.get(step, ())
./venv/lib/python3.12/site-packages/pip/_vendor/distlib/util.py:1861:                        result['username'] = config.get(server, 'username')
./venv/lib/python3.12/site-packages/pip/_vendor/distlib/util.py:1869:                                result[key] = config.get(server, key)
./venv/lib/python3.12/site-packages/pip/_vendor/distlib/util.py:1886:                    repository = config.get(server, 'repository')
./venv/lib/python3.12/site-packages/pip/_vendor/distlib/util.py:1890:                    'username': config.get(server, 'username'),
./venv/lib/python3.12/site-packages/pip/_vendor/distlib/util.py:1891:                    'password': config.get(server, 'password'),
./venv/lib/python3.12/site-packages/pip/_vendor/distlib/compat.py:837:            'od.setdefault(k[,d]) -> od.get(k,d), also set od[k]=d if k not in od'
./venv/lib/python3.12/site-packages/pip/_vendor/distlib/compat.py:947:            value = dict.get(self, key, default)
./venv/lib/python3.12/site-packages/pip/_vendor/distlib/compat.py:1113:                    converter = self.value_converters.get(prefix, None)
./venv/lib/python3.12/site-packages/pip/_vendor/distlib/version.py:592:            p = _VERSION_REPLACE.get(p, p)
./venv/lib/python3.12/site-packages/pip/_vendor/distlib/locators.py:399:            result.download_urls = versions.get('urls', {}).get(version, set())
./venv/lib/python3.12/site-packages/pip/_vendor/distlib/metadata.py:300:        return _ATTR2FIELD.get(name, name)
./venv/lib/python3.12/site-packages/pip/_vendor/distlib/metadata.py:547:                value = self.get(field, None)
./venv/lib/python3.12/site-packages/pip/_vendor/distlib/metadata.py:737:                    result = self._data.get(key, value)
./venv/lib/python3.12/site-packages/pip/_vendor/distlib/metadata.py:749:                                result = d.get(key, value)
./venv/lib/python3.12/site-packages/pip/_vendor/distlib/metadata.py:755:                                result = d.get(key, value)
./venv/lib/python3.12/site-packages/pip/_vendor/platformdirs/unix.py:194:        media_dir = os.environ.get(env_var, "").strip()
./venv/lib/python3.12/site-packages/pip/_internal/network/download.py:117:    resp = session.get(target_url, headers=HEADERS, stream=True)
./venv/lib/python3.12/site-packages/pip/_internal/utils/hashes.py:68:        return hex_digest in self._allowed.get(hash_name, [])
./venv/lib/python3.12/site-packages/pip/_internal/utils/temp_dir.py:66:        return self._should_delete.get(kind, True)
./venv/lib/python3.12/site-packages/pip/_internal/build_env.py:139:            name: os.environ.get(name, None)
./venv/lib/python3.12/site-packages/pip/_internal/resolution/resolvelib/provider.py:176:        requested_order = self._user_requested.get(identifier, math.inf)
./venv/lib/python3.12/site-packages/pip/_internal/resolution/resolvelib/factory.py:441:        incompat_ids = {id(c) for c in incompatibilities.get(identifier, ())}
./venv/lib/python3.12/site-packages/pip/_internal/resolution/resolvelib/resolver.py:262:        last_known_parent_count = weights.get(node, 0)
./venv/lib/python3.12/site-packages/sklearn/inspection/_plot/partial_dependence.py:1290:                old_min_pd, old_max_pd = pdp_lim.get(n_fx, (min_pd, max_pd))
./venv/lib/python3.12/site-packages/sklearn/model_selection/_split.py:3041:                value = self.cvargs.get(key, None)
./venv/lib/python3.12/site-packages/sklearn/linear_model/tests/test_logistic.py:854:            solver=solver, max_iter=solver_max_iter.get(solver, 100), **params
./venv/lib/python3.12/site-packages/sklearn/linear_model/tests/test_logistic.py:917:            tol=solver_tol.get(solver, tol),
./venv/lib/python3.12/site-packages/sklearn/linear_model/tests/test_logistic.py:918:            max_iter=solver_max_iter.get(solver, 100),
./venv/lib/python3.12/site-packages/sklearn/pipeline.py:909:                Xt, **routed_params.get(name, {}).get("transform", {})
./venv/lib/python3.12/site-packages/sklearn/neighbors/tests/test_kd_tree.py:57:    metric_params = METRICS.get(metric, {})
./venv/lib/python3.12/site-packages/sklearn/neighbors/tests/test_kd_tree.py:93:    metric_params = METRICS.get(metric, {})
./venv/lib/python3.12/site-packages/sklearn/neighbors/tests/test_ball_tree.py:126:    metric_params = METRICS.get(metric, {})
./venv/lib/python3.12/site-packages/sklearn/neighbors/tests/test_ball_tree.py:162:    metric_params = METRICS.get(metric, {})
./venv/lib/python3.12/site-packages/sklearn/gaussian_process/kernels.py:388:            if np.any(params_a.get(key, None) != params_b.get(key, None)):
./venv/lib/python3.12/site-packages/sklearn/metrics/_classification.py:587:        y_pred = np.array([label_to_ind.get(label, n_labels + 1) for label in y_pred])
./venv/lib/python3.12/site-packages/sklearn/metrics/_classification.py:588:        y_true = np.array([label_to_ind.get(label, n_labels + 1) for label in y_true])
./venv/lib/python3.12/site-packages/sklearn/utils/multiclass.py:103:    _unique_labels = _FN_UNIQUE_LABELS.get(label_type, None)
./venv/lib/python3.12/site-packages/sklearn/utils/_repr_html/params.py:111:        if param_numpydoc := param_map.get(row, None):
./venv/lib/python3.12/site-packages/sklearn/externals/_packaging/version.py:212:        part = _legacy_version_replacement_map.get(part, part)
./venv/lib/python3.12/site-packages/sklearn/externals/array_api_extra/testing.py:379:        return dask.get(dsk, keys, **kwargs)  # type: ignore[attr-defined]  # pyright: ignore[reportPrivateImportUsage]
./venv/lib/python3.12/site-packages/sklearn/tests/test_metadata_routing.py:307:    default_params_for_method = routed_params.get(method, default=default)
./venv/lib/python3.12/site-packages/sklearn/tests/test_metaestimators_metadata_routing.py:625:        for callee in method_mapping.get(caller, [caller]):
./venv/lib/python3.12/site-packages/sklearn/tests/test_metaestimators_metadata_routing.py:849:        extra_method_args = metaestimator.get("method_args", {}).get(method_name, {})
./venv/lib/python3.12/site-packages/sklearn/tests/metadata_routing_common.py:72:        getattr(obj, "_records", dict()).get(method, dict()).get(parent, list())
./venv/lib/python3.12/site-packages/sklearn/cluster/tests/test_hdbscan.py:156:    }.get(metric, None)
./venv/lib/python3.12/site-packages/sklearn/datasets/tests/test_common.py:95:    markers_fetch = FETCH_PYTEST_MARKERS.get(param, {})
./venv/lib/python3.12/site-packages/sklearn/datasets/tests/test_openml.py:956:        expected_missing = datasets_missing_values[data_id].get(name, 0)
./venv/lib/python3.12/site-packages/sklearn/svm/_base.py:1049:    _solver_pen = _solver_type_dict.get(loss, None)
./venv/lib/python3.12/site-packages/sklearn/svm/_base.py:1053:        _solver_dual = _solver_pen.get(penalty, None)
./venv/lib/python3.12/site-packages/sklearn/svm/_base.py:1060:            solver_num = _solver_dual.get(dual, None)
./venv/lib/python3.12/site-packages/networkx/convert_matrix.py:297:    edge_attr = {k: [d.get(k, nan) for _, _, d in edgelist] for k in all_attrs}
./venv/lib/python3.12/site-packages/networkx/convert_matrix.py:1101:                attr_data = [wt.get(attr, 1.0) for wt in wts]
./venv/lib/python3.12/site-packages/networkx/algorithms/time_dependent.py:141:        weights = [G.nodes[i].get(weight, 1) for i in pred]
./venv/lib/python3.12/site-packages/networkx/algorithms/approximation/dominating_set.py:92:        return G.nodes[v].get(weight, 1) / len(neighborhood - dom_set)
./venv/lib/python3.12/site-packages/networkx/algorithms/approximation/traveling_salesman.py:1041:        next_node = min(nodeset, key=lambda n: nbrdict[n].get(weight, 1))
./venv/lib/python3.12/site-packages/networkx/algorithms/approximation/traveling_salesman.py:1247:    cost = sum(G[u][v].get(weight, 1) for u, v in pairwise(cycle))
./venv/lib/python3.12/site-packages/networkx/algorithms/approximation/traveling_salesman.py:1256:            adj_cost = sum(G[u][v].get(weight, 1) for u, v in pairwise(adj_sol))
./venv/lib/python3.12/site-packages/networkx/algorithms/approximation/traveling_salesman.py:1482:    cost = sum(G[u][v].get(weight, 1) for u, v in pairwise(cycle))
./venv/lib/python3.12/site-packages/networkx/algorithms/approximation/traveling_salesman.py:1492:            adj_cost = sum(G[u][v].get(weight, 1) for u, v in pairwise(adj_sol))
./venv/lib/python3.12/site-packages/networkx/algorithms/approximation/steinertree.py:79:        weight_here = d_1[(u, su)] + data.get(weight, 1) + d_1[(v, sv)]
./venv/lib/python3.12/site-packages/networkx/algorithms/approximation/steinertree.py:92:            G_3.add_edge(n1, n2, weight=G[n1][n2].get(weight, 1))
./venv/lib/python3.12/site-packages/networkx/algorithms/approximation/steinertree.py:97:            (u, v, min(G[u][v], key=lambda k: G[u][v][k].get(weight, 1)))
./venv/lib/python3.12/site-packages/networkx/algorithms/approximation/steinertree.py:134:            (u, v, min(G[u][v], key=lambda k: G[u][v][k].get(weight, 1)))
./venv/lib/python3.12/site-packages/networkx/algorithms/structuralholes.py:21:        a_uv = G[u][v].get(weight, 1)
./venv/lib/python3.12/site-packages/networkx/algorithms/structuralholes.py:25:        a_vu = G[v][u].get(weight, 1)
./venv/lib/python3.12/site-packages/networkx/algorithms/community/bipartitions.py:148:        sum_weight = lambda u, v, d: sum(dd.get(weight, 1) for dd in d.values())
./venv/lib/python3.12/site-packages/networkx/algorithms/community/bipartitions.py:150:        sum_weight = lambda u, v, d: d.get(weight, 1)
./venv/lib/python3.12/site-packages/networkx/algorithms/dag.py:1078:                    max(data.values(), key=lambda x: x.get(weight, default_weight))
./venv/lib/python3.12/site-packages/networkx/algorithms/dag.py:1081:                ).get(weight, default_weight),
./venv/lib/python3.12/site-packages/networkx/algorithms/dag.py:1150:            i = max(G[u][v], key=lambda x: G[u][v][x].get(weight, default_weight))
./venv/lib/python3.12/site-packages/networkx/algorithms/dag.py:1151:            path_length += G[u][v][i].get(weight, default_weight)
./venv/lib/python3.12/site-packages/networkx/algorithms/dag.py:1154:            path_length += G[u][v].get(weight, default_weight)
./venv/lib/python3.12/site-packages/networkx/algorithms/link_prediction.py:340:            path_len = spl[u].get(v, inf)
./venv/lib/python3.12/site-packages/networkx/algorithms/bipartite/projection.py:459:    ...         w += G[u][nbr].get(weight, 1) + G[v][nbr].get(weight, 1)
./venv/lib/python3.12/site-packages/networkx/algorithms/bipartite/matrix.py:102:                (row_index[u], col_index[v], d.get(weight, 1))
./venv/lib/python3.12/site-packages/networkx/algorithms/bipartite/link_analysis.py:250:    p0 = np.array([top_personalization.get(n, 0) for n in top], dtype=float)
./venv/lib/python3.12/site-packages/networkx/algorithms/bipartite/link_analysis.py:251:    u0 = np.array([bottom_personalization.get(n, 0) for n in bottom], dtype=float)
./venv/lib/python3.12/site-packages/networkx/algorithms/bipartite/tests/test_project.py:394:                w += G.edges[u, nbr].get(weight, 1) + G.edges[v, nbr].get(weight, 1)
./venv/lib/python3.12/site-packages/networkx/algorithms/shortest_paths/weighted.py:77:        return lambda u, v, d: min(attr.get(weight, 1) for attr in d.values())
./venv/lib/python3.12/site-packages/networkx/algorithms/shortest_paths/weighted.py:78:    return lambda u, v, data: data.get(weight, 1)
./venv/lib/python3.12/site-packages/networkx/algorithms/shortest_paths/weighted.py:1471:                if dist_v < dist.get(v, inf):
./venv/lib/python3.12/site-packages/networkx/algorithms/shortest_paths/weighted.py:1496:                        count_v = count.get(v, 0) + 1
./venv/lib/python3.12/site-packages/networkx/algorithms/shortest_paths/tests/test_weighted.py:17:                return min(e.get(weight, 1) for e in d.values())
./venv/lib/python3.12/site-packages/networkx/algorithms/shortest_paths/tests/test_weighted.py:22:                return d.get(weight, 1)
./venv/lib/python3.12/site-packages/networkx/algorithms/shortest_paths/dense.py:154:        e_weight = d.get(weight, 1.0)
./venv/lib/python3.12/site-packages/networkx/algorithms/distance_regular.py:207:        if cint.get(i, c) != c or bint.get(i, b) != b:
./venv/lib/python3.12/site-packages/networkx/algorithms/distance_regular.py:213:        [bint.get(j, 0) for j in range(diam)],
./venv/lib/python3.12/site-packages/networkx/algorithms/connectivity/stoerwagner.py:96:        (u, v, {"weight": e.get(weight, 1)}) for u, v, e in G.edges(data=True) if u != v
./venv/lib/python3.12/site-packages/networkx/algorithms/connectivity/stoerwagner.py:125:                    h.insert(v, h.get(v, 0) - e["weight"])
./venv/lib/python3.12/site-packages/networkx/algorithms/connectivity/tests/test_stoer_wagner.py:21:            w += e.get(weight, 1)
./venv/lib/python3.12/site-packages/networkx/algorithms/centrality/katz.py:176:                x[nbr] += xlast[n] * G[n][nbr].get(weight, 1)
./venv/lib/python3.12/site-packages/networkx/algorithms/centrality/reaching.py:104:            return total_weight / d.get(weight, 1)
./venv/lib/python3.12/site-packages/networkx/algorithms/centrality/reaching.py:193:                return total_weight / d.get(weight, 1)
./venv/lib/python3.12/site-packages/networkx/algorithms/centrality/eigenvector.py:183:                w = G[n][nbr].get(weight, 1) if weight else 1
./venv/lib/python3.12/site-packages/networkx/algorithms/centrality/second_order.py:110:    if any(d.get(weight, 0) < 0 for u, v, d in G.edges(data=True)):
./venv/lib/python3.12/site-packages/networkx/algorithms/centrality/current_flow_betweenness.py:159:                w = H[v][nbr].get(weight, 1.0)
./venv/lib/python3.12/site-packages/networkx/algorithms/centrality/flow_matrix.py:24:        c = G[u][v].get(weight, 1.0)
./venv/lib/python3.12/site-packages/networkx/algorithms/coloring/greedy_coloring.py:348:    strategy = STRATEGIES.get(strategy, strategy)
./venv/lib/python3.12/site-packages/networkx/algorithms/tests/test_cycles.py:78:        cbH = [[perm.get(n, n) for n in cyc] for cyc in nx.cycle_basis(H)]
./venv/lib/python3.12/site-packages/networkx/algorithms/tests/test_triads.py:231:        tc2 = {tt: sum(1 for t in tbt.get(tt, []) if n in t) for tt in tc1}
./venv/lib/python3.12/site-packages/networkx/algorithms/tests/test_triads.py:238:            tt: sum(1 for t in tbt.get(tt, []) if any(n in ns for n in t)) for tt in tc1
./venv/lib/python3.12/site-packages/networkx/algorithms/tests/test_triads.py:246:            tt: sum(1 for t in tbt.get(tt, []) if any(n in ns for n in t)) for tt in tc1
./venv/lib/python3.12/site-packages/networkx/algorithms/tree/branchings.py:106:    return sum(edge[2].get(attr, default) for edge in G.edges(data=True))
./venv/lib/python3.12/site-packages/networkx/algorithms/tree/branchings.py:156:    edges = [(u, v, data.get(attr, default)) for (u, v, data) in G.edges(data=True)]
./venv/lib/python3.12/site-packages/networkx/algorithms/tree/branchings.py:275:        d = {attr: data.get(attr, default)}
./venv/lib/python3.12/site-packages/networkx/algorithms/tree/branchings.py:622:        d[attr] = -d.get(attr, default)
./venv/lib/python3.12/site-packages/networkx/algorithms/tree/branchings.py:628:        d[attr] = -d.get(attr, default)
./venv/lib/python3.12/site-packages/networkx/algorithms/tree/branchings.py:632:        d[attr] = -d.get(attr, default)
./venv/lib/python3.12/site-packages/networkx/algorithms/tree/branchings.py:685:        d[attr] = max_weight + 1 + (max_weight - min_weight) - d.get(attr, default)
./venv/lib/python3.12/site-packages/networkx/algorithms/tree/branchings.py:692:        d[attr] = max_weight + 1 + (max_weight - min_weight) - d.get(attr, default)
./venv/lib/python3.12/site-packages/networkx/algorithms/tree/branchings.py:696:        d[attr] = max_weight + 1 + (max_weight - min_weight) - d.get(attr, default)
./venv/lib/python3.12/site-packages/networkx/algorithms/tree/branchings.py:725:        d[attr] = d.get(attr, default) - min_weight + 1 - (min_weight - max_weight)
./venv/lib/python3.12/site-packages/networkx/algorithms/tree/branchings.py:731:        d[attr] = d.get(attr, default) + min_weight - 1 + (min_weight - max_weight)
./venv/lib/python3.12/site-packages/networkx/algorithms/tree/branchings.py:735:        d[attr] = d.get(attr, default) + min_weight - 1 + (min_weight - max_weight)
./venv/lib/python3.12/site-packages/networkx/algorithms/tree/distance_measures.py:213:    while max(total_size - sizes[root], sizes.get(hc, 0)) > total_size / 2:
./venv/lib/python3.12/site-packages/networkx/algorithms/tree/tests/test_branchings.py:140:    edges = [(u, v, data.get(attr, default)) for (u, v, data) in G.edges(data=True)]
./venv/lib/python3.12/site-packages/networkx/algorithms/tree/mst.py:94:            wt = e[-1].get(weight, 1) * sign
./venv/lib/python3.12/site-packages/networkx/algorithms/tree/mst.py:205:        wt = d.get(weight, 1)
./venv/lib/python3.12/site-packages/networkx/algorithms/tree/mst.py:297:                    wt = d.get(weight, 1) * sign
./venv/lib/python3.12/site-packages/networkx/algorithms/tree/mst.py:306:                wt = d.get(weight, 1) * sign
./venv/lib/python3.12/site-packages/networkx/algorithms/tree/mst.py:339:                        new_weight = d2.get(weight, 1) * sign
./venv/lib/python3.12/site-packages/networkx/algorithms/tree/mst.py:350:                    new_weight = d2.get(weight, 1) * sign
./venv/lib/python3.12/site-packages/networkx/algorithms/link_analysis/hits_alg.py:313:        x = np.array([nstart.get(n, 0) for n in list(G)], dtype=float)
./venv/lib/python3.12/site-packages/networkx/algorithms/link_analysis/pagerank_alg.py:167:            x[n] += danglesum * dangling_weights.get(n, 0) + (1.0 - alpha) * p.get(n, 0)
./venv/lib/python3.12/site-packages/networkx/algorithms/link_analysis/pagerank_alg.py:249:        p = np.array([personalization.get(n, 0) for n in nodelist], dtype=float)
./venv/lib/python3.12/site-packages/networkx/algorithms/link_analysis/pagerank_alg.py:259:        dangling_weights = np.array([dangling.get(n, 0) for n in nodelist], dtype=float)
./venv/lib/python3.12/site-packages/networkx/algorithms/link_analysis/pagerank_alg.py:470:        x = np.array([nstart.get(n, 0) for n in nodelist], dtype=float)
./venv/lib/python3.12/site-packages/networkx/algorithms/link_analysis/pagerank_alg.py:477:        p = np.array([personalization.get(n, 0) for n in nodelist], dtype=float)
./venv/lib/python3.12/site-packages/networkx/algorithms/link_analysis/pagerank_alg.py:486:        dangling_weights = np.array([dangling.get(n, 0) for n in nodelist], dtype=float)
./venv/lib/python3.12/site-packages/networkx/algorithms/minors/contraction.py:393:            return {"weight": sum(d.get(weight, 1) for d in edgedata)}
./venv/lib/python3.12/site-packages/networkx/algorithms/cluster.py:134:        max_weight = max(d.get(weight, 1) for u, v, d in G.edges(data=True))
./venv/lib/python3.12/site-packages/networkx/algorithms/cluster.py:141:        return G[u][v].get(weight, 1) / max_weight
./venv/lib/python3.12/site-packages/networkx/algorithms/cluster.py:209:        max_weight = max(d.get(weight, 1) for u, v, d in G.edges(data=True))
./venv/lib/python3.12/site-packages/networkx/algorithms/cluster.py:214:        return G[u][v].get(weight, 1) / max_weight
./venv/lib/python3.12/site-packages/networkx/algorithms/cluster.py:315:            v_id = node_to_id.get(v, -1)
./venv/lib/python3.12/site-packages/networkx/algorithms/cluster.py:320:                if node_to_id.get(w, -1) > v_id:
./venv/lib/python3.12/site-packages/networkx/algorithms/cycles.py:453:            elif len(path) < lock.get(w, length_bound):
./venv/lib/python3.12/site-packages/networkx/algorithms/cycles.py:469:                    if lock.get(u, length_bound) < length_bound - bl + 1:
./venv/lib/python3.12/site-packages/networkx/algorithms/cycles.py:578:        yield from ([v] for v, Gv in G.adj.items() if len(Gv.get(v, ())) == 1)
./venv/lib/python3.12/site-packages/networkx/algorithms/flow/utils.py:118:        if u != v and attr.get(capacity, inf) > 0
./venv/lib/python3.12/site-packages/networkx/algorithms/flow/utils.py:141:            r = min(attr.get(capacity, inf), inf)
./venv/lib/python3.12/site-packages/networkx/algorithms/flow/utils.py:153:            r = min(attr.get(capacity, inf), inf)
./venv/lib/python3.12/site-packages/networkx/algorithms/flow/capacityscaling.py:44:    if sum(G.nodes[u].get(demand, 0) for u in G) != 0:
./venv/lib/python3.12/site-packages/networkx/algorithms/flow/capacityscaling.py:49:        (u, {"excess": -G.nodes[u].get(demand, 0), "potential": 0}) for u in G
./venv/lib/python3.12/site-packages/networkx/algorithms/flow/capacityscaling.py:55:        if e.get(weight, 0) < 0 and e.get(capacity, inf) == inf:
./venv/lib/python3.12/site-packages/networkx/algorithms/flow/capacityscaling.py:66:            if u != v and e.get(capacity, inf) > 0
./venv/lib/python3.12/site-packages/networkx/algorithms/flow/capacityscaling.py:72:            if u != v and e.get(capacity, inf) > 0
./venv/lib/python3.12/site-packages/networkx/algorithms/flow/capacityscaling.py:92:        r = min(e.get(capacity, inf), inf)
./venv/lib/python3.12/site-packages/networkx/algorithms/flow/capacityscaling.py:93:        w = e.get(weight, 0)
./venv/lib/python3.12/site-packages/networkx/algorithms/flow/capacityscaling.py:121:                            u != v or e.get(capacity, inf) <= 0 or e.get(weight, 0) >= 0
./venv/lib/python3.12/site-packages/networkx/algorithms/flow/capacityscaling.py:138:                    if (u != v or e.get(capacity, inf) <= 0 or e.get(weight, 0) >= 0)
./venv/lib/python3.12/site-packages/networkx/algorithms/flow/capacityscaling.py:291:        if e.get(capacity, inf) <= 0 or e.get(weight, 0) >= 0
./venv/lib/python3.12/site-packages/networkx/algorithms/flow/networksimplex.py:22:            G.nodes[u].get(demand, 0) for u in self.node_list
./venv/lib/python3.12/site-packages/networkx/algorithms/flow/networksimplex.py:39:        edges = (e for e in edges if e[0] != e[1] and e[-1].get(capacity, inf) != 0)
./venv/lib/python3.12/site-packages/networkx/algorithms/flow/networksimplex.py:46:            self.edge_capacities.append(e[-1].get(capacity, inf))
./venv/lib/python3.12/site-packages/networkx/algorithms/flow/networksimplex.py:47:            self.edge_weights.append(e[-1].get(weight, 0))
./venv/lib/python3.12/site-packages/networkx/algorithms/flow/networksimplex.py:524:        if abs(e[-1].get(weight, 0)) == inf:
./venv/lib/python3.12/site-packages/networkx/algorithms/flow/networksimplex.py:541:        if e[-1].get(capacity, inf) < 0:
./venv/lib/python3.12/site-packages/networkx/algorithms/flow/networksimplex.py:608:        e[-1].get(capacity, inf) == inf and e[-1].get(weight, 0) < 0
./venv/lib/python3.12/site-packages/networkx/algorithms/flow/networksimplex.py:651:            if e[-1].get(capacity, inf) == 0:
./venv/lib/python3.12/site-packages/networkx/algorithms/flow/networksimplex.py:654:            w = e[-1].get(weight, 0)
./venv/lib/python3.12/site-packages/networkx/algorithms/flow/mincost.py:252:    return sum((flowDict[u][v] * d.get(weight, 0) for u, v, d in G.edges(data=True)))
./venv/lib/python3.12/site-packages/networkx/algorithms/isomorphism/matchhelpers.py:78:            return data1.get(attr, default) == data2.get(attr, default)
./venv/lib/python3.12/site-packages/networkx/algorithms/isomorphism/matchhelpers.py:84:            return all(data1.get(attr, d) == data2.get(attr, d) for attr, d in attrs)
./venv/lib/python3.12/site-packages/networkx/algorithms/isomorphism/matchhelpers.py:96:            values1 = {data.get(attr, default) for data in datasets1.values()}
./venv/lib/python3.12/site-packages/networkx/algorithms/isomorphism/matchhelpers.py:97:            values2 = {data.get(attr, default) for data in datasets2.values()}
./venv/lib/python3.12/site-packages/networkx/algorithms/isomorphism/matchhelpers.py:106:                x = tuple(data1.get(attr, d) for attr, d in attrs)
./venv/lib/python3.12/site-packages/networkx/algorithms/isomorphism/matchhelpers.py:110:                x = tuple(data2.get(attr, d) for attr, d in attrs)
./venv/lib/python3.12/site-packages/networkx/algorithms/isomorphism/matchhelpers.py:164:                data1.get(attr, default),
./venv/lib/python3.12/site-packages/networkx/algorithms/isomorphism/matchhelpers.py:165:                data2.get(attr, default),
./venv/lib/python3.12/site-packages/networkx/algorithms/isomorphism/matchhelpers.py:174:            values1 = [data1.get(attr, d) for attr, d in attrs]
./venv/lib/python3.12/site-packages/networkx/algorithms/isomorphism/matchhelpers.py:175:            values2 = [data2.get(attr, d) for attr, d in attrs]
./venv/lib/python3.12/site-packages/networkx/algorithms/isomorphism/matchhelpers.py:188:            values1 = sorted(data.get(attr, default) for data in datasets1.values())
./venv/lib/python3.12/site-packages/networkx/algorithms/isomorphism/matchhelpers.py:189:            values2 = sorted(data.get(attr, default) for data in datasets2.values())
./venv/lib/python3.12/site-packages/networkx/algorithms/isomorphism/matchhelpers.py:198:                x = tuple(data1.get(attr, d) for attr, d in attrs)
./venv/lib/python3.12/site-packages/networkx/algorithms/isomorphism/matchhelpers.py:202:                x = tuple(data2.get(attr, d) for attr, d in attrs)
./venv/lib/python3.12/site-packages/networkx/algorithms/isomorphism/matchhelpers.py:263:            return op(data1.get(attr, default), data2.get(attr, default))
./venv/lib/python3.12/site-packages/networkx/algorithms/isomorphism/matchhelpers.py:270:                if not operator(data1.get(attr, d), data2.get(attr, d)):
./venv/lib/python3.12/site-packages/networkx/algorithms/isomorphism/matchhelpers.py:329:            x = tuple(data1.get(attr, d) for attr, d in attrs)
./venv/lib/python3.12/site-packages/networkx/algorithms/isomorphism/matchhelpers.py:333:            x = tuple(data2.get(attr, d) for attr, d in attrs)
./venv/lib/python3.12/site-packages/networkx/algorithms/assortativity/mixing.py:247:        v = d[x].get(y, 0)
./venv/lib/python3.12/site-packages/networkx/algorithms/assortativity/connectivity.py:115:                s = sum(G[nbr][n].get(weight, 1) * d for nbr, d in nbrdeg)
./venv/lib/python3.12/site-packages/networkx/algorithms/assortativity/connectivity.py:117:                s = sum(G[n][nbr].get(weight, 1) * d for nbr, d in nbrdeg)
./venv/lib/python3.12/site-packages/networkx/algorithms/assortativity/neighbor_degree.py:157:                sum(dd.get(weight, 1) * t_deg[nbr] for nbr, dd in G_S[n].items())
./venv/lib/python3.12/site-packages/networkx/algorithms/assortativity/neighbor_degree.py:158:                + sum(dd.get(weight, 1) * t_deg[nbr] for nbr, dd in G_P[n].items())
./venv/lib/python3.12/site-packages/networkx/algorithms/assortativity/pairs.py:56:        uattr = Gnodes[u].get(attribute, None)
./venv/lib/python3.12/site-packages/networkx/algorithms/assortativity/pairs.py:59:                vattr = Gnodes[v].get(attribute, None)
./venv/lib/python3.12/site-packages/networkx/algorithms/assortativity/pairs.py:64:                vattr = Gnodes[v].get(attribute, None)
./venv/lib/python3.12/site-packages/networkx/algorithms/matching.py:433:        wt = d.get(weight, 1)
./venv/lib/python3.12/site-packages/networkx/algorithms/matching.py:509:        return dualvar[v] + dualvar[w] - 2 * G[v][w].get(weight, 1)
./venv/lib/python3.12/site-packages/networkx/algorithms/matching.py:897:            wt = d.get(weight, 1)
./venv/lib/python3.12/site-packages/networkx/relabel.py:195:    H.add_nodes_from(mapping.get(n, n) for n in G)
./venv/lib/python3.12/site-packages/networkx/relabel.py:196:    H._node.update((mapping.get(n, n), d.copy()) for n, d in G.nodes.items())
./venv/lib/python3.12/site-packages/networkx/relabel.py:199:            (mapping.get(n1, n1), mapping.get(n2, n2), k, d.copy())
./venv/lib/python3.12/site-packages/networkx/relabel.py:219:            (mapping.get(n1, n1), mapping.get(n2, n2), d.copy())
./venv/lib/python3.12/site-packages/networkx/generators/stochastic.py:52:            d[weight] = d.get(weight, 1) / degree[u]
./venv/lib/python3.12/site-packages/networkx/drawing/layout.py:1725:        mass[idx] = node_mass.get(node, G.degree(node) + 1)
./venv/lib/python3.12/site-packages/networkx/drawing/layout.py:1726:        size[idx] = node_size.get(node, 1)
./venv/lib/python3.12/site-packages/networkx/drawing/nx_pylab.py:605:        attr = kwargs.get(param_name, attr)
./venv/lib/python3.12/site-packages/networkx/drawing/nx_pylab.py:623:        return [node_subgraph.nodes[n].get(attr, default) for n in seq]
./venv/lib/python3.12/site-packages/networkx/drawing/nx_pylab.py:665:        attr = kwargs.get(param_name, attr)
./venv/lib/python3.12/site-packages/networkx/drawing/nx_pylab.py:680:        return [edge_subgraph.edges[e].get(attr, default) for e in seq]
./venv/lib/python3.12/site-packages/networkx/drawing/nx_pylab.py:687:        attr = kwargs.get(param_name, attr)
./venv/lib/python3.12/site-packages/networkx/drawing/nx_pylab.py:699:        return edge_subgraph.edges[e].get(attr, default)
./venv/lib/python3.12/site-packages/networkx/drawing/nx_pylab.py:707:        attr = kwargs.get(param_name, attr)
./venv/lib/python3.12/site-packages/networkx/drawing/nx_pylab.py:719:        return subgraph.nodes[n].get(attr, default)
./venv/lib/python3.12/site-packages/networkx/linalg/algebraicconnectivity.py:114:            ((u, v, e.get(weight, 1.0)) for u, v, e in G.edges(data=True) if u != v),
./venv/lib/python3.12/site-packages/networkx/linalg/algebraicconnectivity.py:120:            (u, v, abs(e.get(weight, 1.0))) for u, v, e in G.edges(data=True) if u != v
./venv/lib/python3.12/site-packages/networkx/linalg/algebraicconnectivity.py:124:            (u, v, sum(abs(e.get(weight, 1.0)) for e in G[u][v].values()))
./venv/lib/python3.12/site-packages/networkx/linalg/attrmatrix.py:107:                    return sum(d.get(edge_attr, 1) for d in G[u][v].values())
./venv/lib/python3.12/site-packages/networkx/linalg/attrmatrix.py:112:                    return G[u][v].get(edge_attr, 1)
./venv/lib/python3.12/site-packages/networkx/linalg/graphmatrix.py:96:                wt = G[u][v][ekey].get(weight, 1)
./venv/lib/python3.12/site-packages/networkx/linalg/graphmatrix.py:98:                wt = G[u][v].get(weight, 1)
./venv/lib/python3.12/site-packages/networkx/readwrite/pajek.py:54:        na = G.nodes.get(n, {}).copy()
./venv/lib/python3.12/site-packages/networkx/readwrite/pajek.py:248:                u = nodelabels.get(ui, ui)
./venv/lib/python3.12/site-packages/networkx/readwrite/pajek.py:249:                v = nodelabels.get(vi, vi)
./venv/lib/python3.12/site-packages/networkx/readwrite/json_graph/node_link.py:244:        node = _to_tuple(d.get(name, next(c)))
./venv/lib/python3.12/site-packages/networkx/readwrite/json_graph/node_link.py:254:            ky = d.get(key, None)
./venv/lib/python3.12/site-packages/networkx/readwrite/json_graph/tree.py:124:            grandchildren = data.get(children, [])
./venv/lib/python3.12/site-packages/networkx/readwrite/json_graph/tree.py:133:    children_ = data.get(children, [])
./venv/lib/python3.12/site-packages/networkx/readwrite/text.py:330:                    label = str(graph.nodes[node].get(label_attr, node))
./venv/lib/python3.12/site-packages/networkx/readwrite/text.py:336:                    collapse = graph.nodes[node].get(collapse_attr, False)
./venv/lib/python3.12/site-packages/networkx/readwrite/text.py:382:                                str(graph.nodes[p].get(label_attr, p))
./venv/lib/python3.12/site-packages/networkx/utils/heaps.py:320:        return self._dict.get(key, default)
./venv/lib/python3.12/site-packages/networkx/utils/backends.py:1233:                edge_attr: bound.arguments.get(val, 1) if isinstance(val, str) else val
./venv/lib/python3.12/site-packages/networkx/utils/backends.py:1328:                    edges = preserve_edge_attrs.get(gname, edge_attrs)
./venv/lib/python3.12/site-packages/networkx/utils/backends.py:1334:                    nodes = preserve_node_attrs.get(gname, node_attrs)
./venv/lib/python3.12/site-packages/networkx/utils/backends.py:2025:        cache = cache.get("backends", {}).get(backend_name, {})
./venv/lib/python3.12/site-packages/networkx/tests/test_relabel.py:325:        assert [mapping.get(i, i) for i in original_order] == new_order
./venv/lib/python3.12/site-packages/networkx/tests/test_relabel.py:333:        assert [mapping.get(i, i) for i in original_order] == new_order
./venv/lib/python3.12/site-packages/networkx/tests/test_relabel.py:341:        assert [mapping.get(i, i) for i in original_order] == new_order
./venv/lib/python3.12/site-packages/networkx/tests/test_relabel.py:349:        assert [mapping.get(i, i) for i in original_order] != new_order
./venv/lib/python3.12/site-packages/networkx/classes/multidigraph.py:512:            datadict = keydict.get(key, self.edge_attr_dict_factory())
./venv/lib/python3.12/site-packages/networkx/classes/reportviews.py:79:    Otherwise iterate over `(u, v, datadict.get(data, default))`.
./venv/lib/python3.12/site-packages/networkx/classes/reportviews.py:448:        return sum(dd.get(weight, 1) for dd in succs.values()) + sum(
./venv/lib/python3.12/site-packages/networkx/classes/reportviews.py:449:            dd.get(weight, 1) for dd in preds.values()
./venv/lib/python3.12/site-packages/networkx/classes/reportviews.py:463:                deg = sum(dd.get(weight, 1) for dd in succs.values()) + sum(
./venv/lib/python3.12/site-packages/networkx/classes/reportviews.py:464:                    dd.get(weight, 1) for dd in preds.values()
./venv/lib/python3.12/site-packages/networkx/classes/reportviews.py:527:        return sum(dd.get(weight, 1) for dd in nbrs.values()) + (
./venv/lib/python3.12/site-packages/networkx/classes/reportviews.py:528:            n in nbrs and nbrs[n].get(weight, 1)
./venv/lib/python3.12/site-packages/networkx/classes/reportviews.py:540:                deg = sum(dd.get(weight, 1) for dd in nbrs.values()) + (
./venv/lib/python3.12/site-packages/networkx/classes/reportviews.py:541:                    n in nbrs and nbrs[n].get(weight, 1)
./venv/lib/python3.12/site-packages/networkx/classes/reportviews.py:565:                deg = sum(dd.get(weight, 1) for dd in succs.values())
./venv/lib/python3.12/site-packages/networkx/classes/reportviews.py:577:        return sum(dd.get(weight, 1) for dd in nbrs.values())
./venv/lib/python3.12/site-packages/networkx/classes/reportviews.py:588:                deg = sum(dd.get(weight, 1) for dd in preds.values())
./venv/lib/python3.12/site-packages/networkx/classes/reportviews.py:604:            d.get(weight, 1) for key_dict in nbrs.values() for d in key_dict.values()
./venv/lib/python3.12/site-packages/networkx/classes/reportviews.py:607:            deg += sum(d.get(weight, 1) for d in nbrs[n].values())
./venv/lib/python3.12/site-packages/networkx/classes/reportviews.py:623:                    d.get(weight, 1)
./venv/lib/python3.12/site-packages/networkx/classes/reportviews.py:628:                    deg += sum(d.get(weight, 1) for d in nbrs[n].values())
./venv/lib/python3.12/site-packages/networkx/classes/reportviews.py:645:            d.get(weight, 1) for key_dict in succs.values() for d in key_dict.values()
./venv/lib/python3.12/site-packages/networkx/classes/reportviews.py:647:            d.get(weight, 1) for key_dict in preds.values() for d in key_dict.values()
./venv/lib/python3.12/site-packages/networkx/classes/reportviews.py:666:                    d.get(weight, 1)
./venv/lib/python3.12/site-packages/networkx/classes/reportviews.py:670:                    d.get(weight, 1)
./venv/lib/python3.12/site-packages/networkx/classes/reportviews.py:687:            d.get(weight, 1) for key_dict in nbrs.values() for d in key_dict.values()
./venv/lib/python3.12/site-packages/networkx/classes/reportviews.py:701:                    d.get(weight, 1)
./venv/lib/python3.12/site-packages/networkx/classes/reportviews.py:718:            d.get(weight, 1) for key_dict in nbrs.values() for d in key_dict.values()
./venv/lib/python3.12/site-packages/networkx/classes/reportviews.py:732:                    d.get(weight, 1)
./venv/lib/python3.12/site-packages/networkx/classes/reportviews.py:1212:    Otherwise iterate over `(u, v, datadict.get(data, default))`.
./venv/lib/python3.12/site-packages/networkx/classes/graph.py:980:        datadict = self._adj[u].get(v, self.edge_attr_dict_factory())
./venv/lib/python3.12/site-packages/networkx/classes/graph.py:1060:            datadict = self._adj[u].get(v, self.edge_attr_dict_factory())
./venv/lib/python3.12/site-packages/networkx/classes/function.py:161:    return [counts.get(i, 0) for i in range(max(counts) + 1 if counts else 0)]
./venv/lib/python3.12/site-packages/networkx/classes/function.py:705:        return {n: d.get(name, default) for n, d in G.nodes.items()}
./venv/lib/python3.12/site-packages/networkx/classes/function.py:924:        return {x[:-1]: x[-1].get(name, default) for x in edges}
./venv/lib/python3.12/site-packages/networkx/classes/function.py:1322:                    (n, n, k, d.get(data, default))
./venv/lib/python3.12/site-packages/networkx/classes/function.py:1329:                    (n, n, d.get(data, default))
./venv/lib/python3.12/site-packages/networkx/classes/function.py:1336:                (n, n, nbrs[n].get(data, default))
./venv/lib/python3.12/site-packages/networkx/classes/tests/dispatch_interface.py:124:                    (attr, graph._node[n].get(attr, default))
./venv/lib/python3.12/site-packages/networkx/classes/tests/dispatch_interface.py:138:                    (attr, old_dd.get(attr, default))
./venv/lib/python3.12/site-packages/networkx/classes/multigraph.py:524:            datadict = keydict.get(key, self.edge_attr_dict_factory())
./venv/lib/python3.12/site-packages/networkx/classes/digraph.py:742:        datadict = self._adj[u].get(v, self.edge_attr_dict_factory())
./venv/lib/python3.12/site-packages/networkx/classes/digraph.py:824:            datadict = self._adj[u].get(v, self.edge_attr_dict_factory())
./venv/lib/python3.12/site-packages/requests/utils.py:874:        proxy = environ_proxies.get(scheme, environ_proxies.get("all"))
./venv/lib/python3.12/site-packages/requests/structures.py:96:        return self.__dict__.get(key, None)
./venv/lib/python3.12/site-packages/requests/structures.py:99:        return self.__dict__.get(key, default)
./venv/lib/python3.12/site-packages/requests/cookies.py:76:        return self._r.headers.get(name, self._new_headers.get(name, default))
./venv/lib/python3.12/site-packages/urllib3/response.py:679:        return self.headers.get(name, default)
./venv/lib/python3.12/site-packages/urllib3/connectionpool.py:1130:    port = port or port_by_scheme.get(scheme, 80)
./venv/lib/python3.12/site-packages/urllib3/fields.py:299:            if self.headers.get(sort_key, False):
./venv/lib/python3.12/site-packages/pydantic/_internal/_model_construction.py:57:        existing: Any = self.get(k, None)
./venv/lib/python3.12/site-packages/pydantic/_internal/_generate_schema.py:1551:                        default=namedtuple_cls._field_defaults.get(field_name, Parameter.empty),
./venv/lib/python3.12/site-packages/pydantic/_internal/_generics.py:339:    return type_map.get(type_, type_)
./venv/lib/python3.12/site-packages/pydantic/_internal/_utils.py:394:        return self.wrapped.get(key, _SENTINEL)
./venv/lib/python3.12/site-packages/pydantic/_internal/_decorators.py:379:            attribute = base.__dict__.get(name, _sentinel)
./venv/lib/python3.12/site-packages/pydantic/mypy.py:208:                setting = config.get(key, False)
./venv/lib/python3.12/site-packages/pydantic/v1/class_validators.py:168:        validators = self.validators.get(name, [])
./venv/lib/python3.12/site-packages/pydantic/v1/generics.py:242:                        key: typevars_map.get(value, value) for key, value in _assigned_parameters[cls].items()
./venv/lib/python3.12/site-packages/pydantic/v1/generics.py:274:        return type_map.get(type_, type_)
./venv/lib/python3.12/site-packages/pydantic/v1/generics.py:325:    new_type = type_map.get(type_, type_)
./venv/lib/python3.12/site-packages/pydantic/v1/main.py:183:                elif is_finalvar_with_default_val(ann_type, namespace.get(ann_name, Undefined)):
./venv/lib/python3.12/site-packages/pydantic/v1/main.py:187:                    value = namespace.get(ann_name, Undefined)
./venv/lib/python3.12/site-packages/pydantic/v1/main.py:224:                        annotation=annotations.get(var_name, Undefined),
./venv/lib/python3.12/site-packages/pydantic/v1/main.py:379:            known_field = self.__fields__.get(name, None)
./venv/lib/python3.12/site-packages/pydantic/v1/mypy.py:247:                setting = config.get(key, False)
./venv/lib/python3.12/site-packages/pydantic/v1/dataclasses.py:456:        known_field = self.__pydantic_model__.__fields__.get(name, None)
./venv/lib/python3.12/site-packages/pydantic/v1/fields.py:187:        return [(a, v) for a, v in attrs if v != field_defaults_to_hide.get(a, None)]
./venv/lib/python3.12/site-packages/pydantic/v1/fields.py:209:                if current_value is self.__field_constraints__.get(attr_name, None):
./venv/lib/python3.12/site-packages/pydantic/json_schema.py:190:        return self.defs_remapping.get(ref, ref)
./venv/lib/python3.12/site-packages/pydantic/json_schema.py:193:        return self.json_remapping.get(ref, ref)
./venv/lib/python3.12/site-packages/pydantic/json_schema.py:2311:            return self.definitions.get(def_ref, None)
./venv/lib/python3.12/site-packages/mpmath/functions/bessel.py:390:        p,v = cache.get(name, (-1,0))
./venv/lib/python3.12/site-packages/mpmath/ctx_mp_python.py:1010:        f.__doc__ = function_docs.__dict__.get(name, "Computes the %s of x" % doc)
./venv/lib/python3.12/site-packages/mpmath/ctx_mp_python.py:1029:        f_wrapped.__doc__ = function_docs.__dict__.get(name, f.__doc__)
./venv/lib/python3.12/site-packages/mpmath/ctx_fp.py:60:        f_wrapped.__doc__ = function_docs.__dict__.get(name, f.__doc__)
./venv/lib/python3.12/site-packages/uvicorn/logging.py:49:        func = self.level_name_colors.get(level_no, default)
./venv/lib/python3.12/site-packages/triton/runtime/jit.py:165:            val = self.globals.get(name, None)
./venv/lib/python3.12/site-packages/triton/runtime/jit.py:168:            val = self.nonlocals.get(name, None)
./venv/lib/python3.12/site-packages/triton/runtime/jit.py:565:    cache_key = kernel_key_cache.get(key, None)
./venv/lib/python3.12/site-packages/triton/runtime/jit.py:713:        kernel = kernel_cache.get(key, None)
./venv/lib/python3.12/site-packages/triton/runtime/jit.py:727:            if (newVal := globals_dict.get(name, not_present)) != val:
./venv/lib/python3.12/site-packages/triton/compiler/code_generator.py:271:            attr_specs = self.attrs.get(path, [])
./venv/lib/python3.12/site-packages/triton/compiler/code_generator.py:370:        val = self.gscope.get(name, absent_marker)
./venv/lib/python3.12/site-packages/triton/compiler/code_generator.py:383:            return self.lscope.get(name, absent)
./venv/lib/python3.12/site-packages/triton/compiler/code_generator.py:386:            val = self.gscope.get(name, absent)
./venv/lib/python3.12/site-packages/markdown_it/rules_inline/backticks.py:26:    if state.backticksScanned and state.backticks.get(openerLength, 0) <= start:
./venv/lib/python3.12/site-packages/markdown_it/rules_inline/link.py:115:        ref = state.env["references"].get(label, None)
./venv/lib/python3.12/site-packages/markdown_it/rules_inline/image.py:116:        ref = state.env["references"].get(label, None)
./venv/lib/python3.12/site-packages/markdown_it/ruler.py:267:        return self.__cache__.get(chainName, []) or []
./venv/lib/python3.12/site-packages/markdown_it/token.py:104:        return self.attrs.get(name, None)
./venv/lib/python3.12/site-packages/h11/_state.py:349:            changes = STATE_TRIGGERED_TRANSITIONS.get(joint_state, {})
./venv/lib/python3.12/site-packages/rich/_emoji_replace.py:21:    default_variant_code = variants.get(default_variant, "") if default_variant else ""
./venv/lib/python3.12/site-packages/rich/emoji.py:50:            self._char += self.VARIANTS.get(variant, "")
./venv/lib/python3.12/site-packages/rich/padding.py:87:                Measurement.get(console, options, self.renderable).maximum
./venv/lib/python3.12/site-packages/rich/padding.py:132:        measure_min, measure_max = Measurement.get(console, options, self.renderable)
./venv/lib/python3.12/site-packages/rich/styled.py:34:        return Measurement.get(console, options, self.renderable)
./venv/lib/python3.12/site-packages/rich/align.py:238:        measurement = Measurement.get(console, options, self.renderable)
./venv/lib/python3.12/site-packages/rich/align.py:295:        measurement = Measurement.get(console, options, self.renderable)
./venv/lib/python3.12/site-packages/rich/spinner.py:59:        return Measurement.get(console, options, text)
./venv/lib/python3.12/site-packages/rich/console.py:816:            color_system = _TERM_COLORS.get(colors, ColorSystem.STANDARD)
./venv/lib/python3.12/site-packages/rich/console.py:1297:        measurement = Measurement.get(self, options or self.options, renderable)
./venv/lib/python3.12/site-packages/rich/containers.py:50:            Measurement.get(console, options, renderable)
./venv/lib/python3.12/site-packages/rich/box.py:80:            box = LEGACY_WINDOWS_SUBSTITUTIONS.get(box, box)
./venv/lib/python3.12/site-packages/rich/box.py:93:        return PLAIN_HEADED_SUBSTITUTIONS.get(self, self)
./venv/lib/python3.12/site-packages/rich/constrain.py:36:        measurement = Measurement.get(console, options, self.renderable)
./venv/lib/python3.12/site-packages/typer/rich_utils.py:594:    default_arguments = panel_to_arguments.get(ARGUMENTS_PANEL_TITLE, [])
./venv/lib/python3.12/site-packages/typer/rich_utils.py:613:    default_options = panel_to_options.get(OPTIONS_PANEL_TITLE, [])
./venv/lib/python3.12/site-packages/typer/rich_utils.py:655:        default_commands = panel_to_commands.get(COMMANDS_PANEL_TITLE, [])
./venv/lib/python3.12/site-packages/typer/core.py:371:                rich_markup_mode = ctx.obj.get(MARKUP_MODE_KEY, None)
./venv/lib/python3.12/site-packages/typer/core.py:593:                rich_markup_mode = ctx.obj.get(MARKUP_MODE_KEY, None)
./venv/lib/python3.12/site-packages/typer/cli.py:204:        rich_markup_mode = ctx.obj.get(MARKUP_MODE_KEY, None)
./venv/lib/python3.12/site-packages/httpx/_models.py:827:        error_type = error_types.get(status_class, "Invalid status code")
./venv/lib/python3.12/site-packages/click/core.py:555:                return get_current_context().meta.get(LANG_KEY, 'en_US')
./venv/lib/python3.12/site-packages/click/core.py:709:            value = self.default_map.get(name, UNSET)
./venv/lib/python3.12/site-packages/click/formatting.py:19:            widths[idx] = max(widths.get(idx, 0), term_len(col))
./venv/lib/python3.12/site-packages/setuptools/_vendor/packaging/version.py:705:        letter = _LETTER_NORMALIZATION.get(letter, letter)
./venv/lib/python3.12/site-packages/setuptools/_vendor/packaging/tags.py:581:    archs = {"armv8l": ["armv8l", "armv7l"]}.get(arch, [arch])
./venv/lib/python3.12/site-packages/setuptools/_vendor/platformdirs/unix.py:238:        media_dir = os.environ.get(env_var, "").strip()
./venv/lib/python3.12/site-packages/setuptools/command/build_clib.py:67:                extra_deps = obj_deps.get(source, list())
./venv/lib/python3.12/site-packages/setuptools/command/build_py.py:136:            self.manifest_files.get(package, []),
./venv/lib/python3.12/site-packages/setuptools/command/build_py.py:311:            spec.get(package, []),
./venv/lib/python3.12/site-packages/setuptools/dist.py:356:            vars(self.metadata).setdefault(option, attrs.get(option, default()))
./venv/lib/python3.12/site-packages/setuptools/dist.py:598:                    val = parser.get(section, opt)
./venv/lib/python3.12/site-packages/setuptools/config/pyprojecttoml.py:202:        package_data = self.setuptools_cfg.get(field, {})
./venv/lib/python3.12/site-packages/setuptools/config/setupcfg.py:284:        option_name = self.aliases.get(option_name, option_name)
./venv/lib/python3.12/site-packages/setuptools/config/setupcfg.py:296:            parsed = self.parsers.get(option_name, lambda x: x)(value)
./venv/lib/python3.12/site-packages/setuptools/config/_apply_pyprojecttoml.py:80:        corresp = PYPROJECT_CORRESPONDENCE.get(norm_key, norm_key)
./venv/lib/python3.12/site-packages/setuptools/config/_apply_pyprojecttoml.py:119:        norm_key = TOOL_TABLE_RENAMES.get(norm_key, norm_key)
./venv/lib/python3.12/site-packages/setuptools/config/_apply_pyprojecttoml.py:120:        corresp = TOOL_TABLE_CORRESPONDENCE.get(norm_key, norm_key)
./venv/lib/python3.12/site-packages/setuptools/config/_apply_pyprojecttoml.py:146:    val = _PREPROCESS.get(field, _noop)(dist, value)
./venv/lib/python3.12/site-packages/setuptools/config/_apply_pyprojecttoml.py:312:        valid = valid_options.get(cmd, set())
./venv/lib/python3.12/site-packages/setuptools/config/_apply_pyprojecttoml.py:334:        opts = valid_options.get(cmd, set())
./venv/lib/python3.12/site-packages/setuptools/config/_validate_pyproject/error_reporting.py:212:            return [self.jargon.get(t, t) for t in term]
./venv/lib/python3.12/site-packages/setuptools/config/_validate_pyproject/error_reporting.py:213:        return self.jargon.get(term, term)
./venv/lib/python3.12/site-packages/setuptools/msvc.py:1550:        env_paths = environ.get(name, '').split(os.pathsep)
./venv/lib/python3.12/site-packages/setuptools/tests/integration/test_pip_install_sdist.py:138:    env = EXTRA_ENV_VARS.get(package, {})
./venv/lib/python3.12/site-packages/setuptools/tests/integration/test_pip_install_sdist.py:143:    pkg = IMPORT_NAME.get(package, package).replace("-", "_")
./venv/lib/python3.12/site-packages/setuptools/tests/integration/test_pip_install_sdist.py:211:    deps += EXTRA_BUILD_DEPS.get(package, [])
./venv/lib/python3.12/site-packages/setuptools/tests/test_core_metadata.py:308:        val = attrs.get(dkey, None)
./venv/lib/python3.12/site-packages/setuptools/_distutils/command/install.py:116:            **INSTALL_SCHEMES.get(scheme, {}),
./venv/lib/python3.12/site-packages/setuptools/_distutils/command/install.py:117:            **sysconfig_schemes.get(scheme, {}),
./venv/lib/python3.12/site-packages/setuptools/_distutils/command/build_py.py:125:        globs = self.package_data.get('', []) + self.package_data.get(package, [])
./venv/lib/python3.12/site-packages/setuptools/_distutils/dist.py:430:                        val = parser.get(section, opt)
./venv/lib/python3.12/site-packages/setuptools/_distutils/archive_util.py:96:    archive_name += compress_ext.get(compress, '')
./venv/lib/python3.12/site-packages/setuptools/_distutils/compilers/C/zos.py:114:            if (binary := os.environ.get(envvar, None))
./venv/lib/python3.12/site-packages/torchgen/gen.py:1933:        grouped_functions = grouped_functions_by_root_name.get(name, [])
./venv/lib/python3.12/site-packages/torchgen/gen.py:1994:            grouped_functions = grouped_functions_by_root_name.get(name, [])
./venv/lib/python3.12/site-packages/torchgen/selective_build/selector.py:316:        merge_et_kernel_metadata[op].update(lhs.get(op, []))
./venv/lib/python3.12/site-packages/torchgen/selective_build/selector.py:317:        merge_et_kernel_metadata[op].update(rhs.get(op, []))
./venv/lib/python3.12/site-packages/torchgen/packaged/autograd/gen_variable_type.py:1065:    fw_derivatives = fn.fw_derivatives.get(key, []) if fn.fw_derivatives else []
./venv/lib/python3.12/site-packages/torchgen/packaged/autograd/gen_variable_type.py:1637:            aliased_arg_name = ALL_VIEW_FUNCTIONS.get(base_name, None)
./venv/lib/python3.12/site-packages/torchgen/packaged/autograd/gen_trace_type.py:124:        trace_name = RENAME_TRACE.get(trace_name, trace_name)
./venv/lib/python3.12/site-packages/torchgen/packaged/autograd/gen_trace_type.py:131:    outplace_trace_name = RENAME_TRACE.get(outplace_trace_name, outplace_trace_name)
./venv/lib/python3.12/site-packages/torchgen/packaged/autograd/gen_trace_type.py:132:    inplace_trace_name = RENAME_TRACE.get(inplace_trace_name, inplace_trace_name)
./venv/lib/python3.12/site-packages/torchgen/api/python.py:1168:                }.get(type_str, type_str)
./venv/lib/python3.12/site-packages/torchgen/api/cpp.py:365:    return JIT_TO_CPP_DEFAULT.get(d, d)
./venv/lib/python3.12/site-packages/fastapi/dependencies/utils.py:606:            ).get(original_call, original_call)
./venv/lib/python3.12/site-packages/fastapi/dependencies/utils.py:731:        value = values.get(alias, None)
./venv/lib/python3.12/site-packages/sentence_transformers/sparse_encoder/evaluation/ReciprocalRankFusionEvaluator.py:199:                dense_rank = dense_ranks.get(doc, len(dense_docs))
./venv/lib/python3.12/site-packages/sentence_transformers/sparse_encoder/evaluation/ReciprocalRankFusionEvaluator.py:200:                sparse_rank = sparse_ranks.get(doc, len(sparse_docs))
./venv/lib/python3.12/site-packages/sentence_transformers/evaluation/NanoBEIREvaluator.py:455:            ir_evaluator_kwargs["query_prompt"] = self.query_prompts.get(dataset_name, None)
./venv/lib/python3.12/site-packages/sentence_transformers/evaluation/NanoBEIREvaluator.py:457:            ir_evaluator_kwargs["corpus_prompt"] = self.corpus_prompts.get(dataset_name, None)
./venv/lib/python3.12/site-packages/sentence_transformers/SentenceTransformer.py:1169:                    module_kwarg_keys = self.module_kwargs.get(module_name, [])
./venv/lib/python3.12/site-packages/sentence_transformers/model_card.py:1051:                else line.get(key, "-")
./venv/lib/python3.12/site-packages/sentence_transformers/data_collator.py:94:            task = router_mapping.get(column_name, None)
./venv/lib/python3.12/site-packages/websockets/sync/connection.py:319:            return self.recv_messages.get(timeout, decode)
./venv/lib/python3.12/site-packages/huggingface_hub/cli/cache.py:237:            refs = revision.refs if revision is not None else repo_refs_map.get(repo, frozenset())
./venv/lib/python3.12/site-packages/huggingface_hub/cli/cache.py:269:                "refs": sorted(repo_refs_map.get(repo, frozenset())),
./venv/lib/python3.12/site-packages/huggingface_hub/cli/cache.py:305:                " ".join(sorted(repo_refs_map.get(repo, frozenset()))),
./venv/lib/python3.12/site-packages/huggingface_hub/_commit_api.py:855:                    response = get_session().get(url, headers=headers)
./venv/lib/python3.12/site-packages/huggingface_hub/inference/_generated/_async_client.py:3387:        response = await client.get(url, headers=build_hf_headers(token=self.token))
./venv/lib/python3.12/site-packages/huggingface_hub/inference/_generated/_async_client.py:3424:        response = await client.get(url, headers=build_hf_headers(token=self.token))
./venv/lib/python3.12/site-packages/huggingface_hub/inference/_common.py:386:    return _UNSUPPORTED_TEXT_GENERATION_KWARGS.get(model, [])
./venv/lib/python3.12/site-packages/huggingface_hub/inference/_providers/fal_ai.py:82:            status_response = get_session().get(status_url, headers=request_params.headers)
./venv/lib/python3.12/site-packages/huggingface_hub/inference/_providers/fal_ai.py:86:        return get_session().get(result_url, headers=request_params.headers).json()
./venv/lib/python3.12/site-packages/huggingface_hub/inference/_providers/black_forest_labs.py:51:            response = session.get(url, headers={"Content-Type": "application/json"})  # type: ignore
./venv/lib/python3.12/site-packages/huggingface_hub/inference/_providers/zai_org.py:98:            poll_response = session.get(poll_url, headers=request_params.headers)
./venv/lib/python3.12/site-packages/huggingface_hub/inference/_providers/wavespeed.py:62:            result_response = get_session().get(result_url, headers=request_params.headers)
./venv/lib/python3.12/site-packages/huggingface_hub/inference/_client.py:3334:        response = get_session().get(url, headers=build_hf_headers(token=self.token))
./venv/lib/python3.12/site-packages/huggingface_hub/inference/_client.py:3369:        response = get_session().get(url, headers=build_hf_headers(token=self.token))
./venv/lib/python3.12/site-packages/huggingface_hub/utils/_auth.py:143:        stored_tokens = {token_name: config.get(token_name, "hf_token") for token_name in config.sections()}
./venv/lib/python3.12/site-packages/huggingface_hub/utils/_runtime.py:76:    return _package_versions.get(package_name, "N/A")
./venv/lib/python3.12/site-packages/huggingface_hub/utils/_pagination.py:36:    r = session.get(path, params=params, headers=headers)
./venv/lib/python3.12/site-packages/huggingface_hub/_login.py:214:        token = tokens.get(token_name, "<not set>")
./venv/lib/python3.12/site-packages/huggingface_hub/_inference_endpoints.py:230:                response = get_session().get(_health_url, headers=self._api._build_hf_headers(token=self._token))
./venv/lib/python3.12/site-packages/huggingface_hub/hf_api.py:2790:        r = get_session().get(path, headers=headers, timeout=timeout, params=params)
./venv/lib/python3.12/site-packages/huggingface_hub/hf_api.py:2860:        r = get_session().get(path, headers=headers, timeout=timeout, params=params)
./venv/lib/python3.12/site-packages/huggingface_hub/hf_api.py:2930:        r = get_session().get(path, headers=headers, timeout=timeout, params=params)
./venv/lib/python3.12/site-packages/huggingface_hub/hf_api.py:5947:        response = get_session().get(url, headers={**_headers, "range": "bytes=0-100000"})
./venv/lib/python3.12/site-packages/huggingface_hub/hf_api.py:5957:            response = get_session().get(url, headers={**_headers, "range": f"bytes=8-{metadata_size + 7}"})
./venv/lib/python3.12/site-packages/huggingface_hub/hf_api.py:6338:            resp = get_session().get(path, headers=headers, params=params)
./venv/lib/python3.12/site-packages/huggingface_hub/hf_api.py:6414:        resp = get_session().get(path, params={"diff": "1"}, headers=headers)
./venv/lib/python3.12/site-packages/huggingface_hub/hf_api.py:10097:        r = get_session().get(path, params=params, headers=self._build_hf_headers(token=token))
./venv/lib/python3.12/site-packages/huggingface_hub/hf_api.py:10163:        r = get_session().get(path, headers=headers)
./venv/lib/python3.12/site-packages/huggingface_hub/dataclasses.py:145:            for validator in self.__validators__.get(name, []):
./venv/lib/python3.12/site-packages/transformers/configuration_utils.py:342:                    value if not isinstance(value, dict) else value.get(subconfig_key, current_subconfig_attn)
./venv/lib/python3.12/site-packages/transformers/configuration_utils.py:364:                    value if not isinstance(value, dict) else value.get(subconfig_key, current_subconfig_moe)
./venv/lib/python3.12/site-packages/transformers/configuration_utils.py:866:                or (key in default_config_dict and value != class_config_dict.get(key, value))
./venv/lib/python3.12/site-packages/transformers/modeling_flash_attention_utils.py:144:        fa_param = _hf_api_to_flash_mapping.get(param, param)
./venv/lib/python3.12/site-packages/transformers/modelcard.py:242:                metadata = dataset_metadata_mapping.get(ds_tag, {})
./venv/lib/python3.12/site-packages/transformers/trainer.py:5121:                setattr(fsdp_plugin, param, self.args.fsdp_config.get(param, getattr(fsdp_plugin, param)))
./venv/lib/python3.12/site-packages/transformers/modeling_gguf_pytorch_utils.py:558:        ProcessorClass = TENSOR_PROCESSORS.get(architecture, TensorProcessor)
./venv/lib/python3.12/site-packages/transformers/tokenization_utils_tokenizers.py:733:                current = {k: _truncation.get(k, None) for k in target}
./venv/lib/python3.12/site-packages/transformers/tokenization_utils_tokenizers.py:1096:                        tokens = [special_tokens_map.get(token, token) for token in tokens]
./venv/lib/python3.12/site-packages/transformers/tokenization_utils_tokenizers.py:1130:                special_token_full = self._special_tokens_map.get(token, None)
./venv/lib/python3.12/site-packages/transformers/audio_utils.py:136:            BytesIO(httpx.get(audio, follow_redirects=True, timeout=timeout).content), sr=sampling_rate
./venv/lib/python3.12/site-packages/transformers/audio_utils.py:178:            response = httpx.get(audio, follow_redirects=True, timeout=timeout)
./venv/lib/python3.12/site-packages/transformers/video_utils.py:701:        file_obj = BytesIO(httpx.get(video, follow_redirects=True).content)
./venv/lib/python3.12/site-packages/transformers/image_utils.py:455:            image = PIL.Image.open(BytesIO(httpx.get(image, timeout=timeout, follow_redirects=True).content))
./venv/lib/python3.12/site-packages/transformers/training_args.py:113:        val = int(os.environ.get(e, "-1"))
./venv/lib/python3.12/site-packages/transformers/integrations/accelerate.py:749:                device_buffer_sizes[device] = device_buffer_sizes.get(device, 0) + current_buffer_size
./venv/lib/python3.12/site-packages/transformers/integrations/accelerate.py:849:                gpu_memory_used = device_memory_used.get(gpu_device, 0)
./venv/lib/python3.12/site-packages/transformers/integrations/peft.py:975:    base_model_type = _MODEL_TO_CONVERSION_PATTERN.get(model_type, None)
./venv/lib/python3.12/site-packages/transformers/integrations/peft.py:980:    fused_targets = _MOE_FUSED_TARGETS.get(base_model_type, {})
./venv/lib/python3.12/site-packages/transformers/integrations/peft.py:1009:        present_targets = matched_targets.get(new_name, set())
./venv/lib/python3.12/site-packages/transformers/integrations/vptq.py:51:                layer_params = config_for_layers.get(module_name, None) or shared_layer_config.get(
./venv/lib/python3.12/site-packages/transformers/integrations/moe.py:296:        return super().get(experts_implementation, default)
./venv/lib/python3.12/site-packages/transformers/utils/auto_docstring.py:1476:                ).get(model_name, None)
./venv/lib/python3.12/site-packages/transformers/utils/chat_template_utils.py:99:    return type_mapping.get(param_type, {"type": "object"})
./venv/lib/python3.12/site-packages/transformers/utils/attention_visualizer.py:183:            img = Image.open(io.BytesIO(httpx.get(img, follow_redirects=True).content))
./venv/lib/python3.12/site-packages/transformers/utils/notebook.py:256:                    self.inner_table.append([values.get(c, "No Log") for c in columns])
./venv/lib/python3.12/site-packages/transformers/core_model_loading.py:364:            tensors = input_dict.get(key, [])
./venv/lib/python3.12/site-packages/transformers/core_model_loading.py:1159:                        len(mapping.collected_tensors.get(source_pattern, []))
./venv/lib/python3.12/site-packages/transformers/models/rt_detr_v2/modeling_rt_detr_v2.py:1433:        >>> image = Image.open(requests.get(url, stream=True).raw)
./venv/lib/python3.12/site-packages/transformers/models/rt_detr_v2/modeling_rt_detr_v2.py:1768:        >>> image = Image.open(requests.get(url, stream=True).raw)
./venv/lib/python3.12/site-packages/transformers/models/d_fine/modeling_d_fine.py:1647:        >>> image = Image.open(requests.get(url, stream=True).raw)
./venv/lib/python3.12/site-packages/transformers/models/speech_to_text/tokenization_speech_to_text.py:183:        return self.encoder.get(token, self.encoder[self.unk_token])
./venv/lib/python3.12/site-packages/transformers/models/speech_to_text/tokenization_speech_to_text.py:187:        return self.decoder.get(index, self.unk_token)
./venv/lib/python3.12/site-packages/transformers/models/fastspeech2_conformer/tokenization_fastspeech2_conformer.py:125:        return self.encoder.get(token, self.encoder.get(self.unk_token))
./venv/lib/python3.12/site-packages/transformers/models/fastspeech2_conformer/tokenization_fastspeech2_conformer.py:129:        return self.decoder.get(index, self.unk_token)
./venv/lib/python3.12/site-packages/transformers/models/tapas/tokenization_tapas.py:375:        return self.vocab.get(token, self.vocab.get(self.unk_token))
./venv/lib/python3.12/site-packages/transformers/models/tapas/tokenization_tapas.py:379:        return self.ids_to_tokens.get(index, self.unk_token)
./venv/lib/python3.12/site-packages/transformers/models/cpmant/tokenization_cpmant.py:198:        return self.encoder.get(token, self.encoder.get(self.unk_token))
./venv/lib/python3.12/site-packages/transformers/models/cpmant/tokenization_cpmant.py:202:        return self.decoder.get(index, self.unk_token)
./venv/lib/python3.12/site-packages/transformers/models/sam3_video/processing_sam3_video.py:295:                [model_outputs["obj_id_to_tracker_score"].get(obj_id, 0.0) for obj_id in curr_obj_ids]
./venv/lib/python3.12/site-packages/transformers/models/sam3_video/modeling_sam3_video.py:274:        old_obj_idx_to_rm = self._obj_id_to_idx.get(obj_id, None)
./venv/lib/python3.12/site-packages/transformers/models/sam3_video/modeling_sam3_video.py:374:        out = self.output_dict_per_obj[obj_idx][storage_key].get(frame_idx, None)
./venv/lib/python3.12/site-packages/transformers/models/phobert/tokenization_phobert.py:240:            bigram = min(pairs, key=lambda pair: self.bpe_ranks.get(pair, float("inf")))
./venv/lib/python3.12/site-packages/transformers/models/phobert/tokenization_phobert.py:285:        return self.encoder.get(token, self.encoder.get(self.unk_token))
./venv/lib/python3.12/site-packages/transformers/models/phobert/tokenization_phobert.py:289:        return self.decoder.get(index, self.unk_token)
./venv/lib/python3.12/site-packages/transformers/models/wav2vec2/tokenization_wav2vec2.py:269:        return self.encoder.get(token, self.encoder.get(self.unk_token))
./venv/lib/python3.12/site-packages/transformers/models/wav2vec2/tokenization_wav2vec2.py:273:        result = self.decoder.get(index, self.unk_token)
./venv/lib/python3.12/site-packages/transformers/models/auto/tokenization_auto.py:595:            tokenizer_class_name = TOKENIZER_MAPPING_NAMES.get(tokenizer_type, None)
./venv/lib/python3.12/site-packages/transformers/models/auto/tokenization_auto.py:644:            and TOKENIZER_MAPPING_NAMES.get(config_model_type, "").replace("Fast", "")
./venv/lib/python3.12/site-packages/transformers/models/whisper/english_normalizer.py:415:                        ones = self.ones.get(next, 0)
./venv/lib/python3.12/site-packages/transformers/models/whisper/english_normalizer.py:508:        return " ".join(self.mapping.get(word, word) for word in s.split())
./venv/lib/python3.12/site-packages/transformers/models/markuplm/tokenization_markuplm.py:268:            xpath_tags_list.append(self.tags_dict.get(tag_name, self.unk_tag_id))
./venv/lib/python3.12/site-packages/transformers/models/m2m_100/tokenization_m2m_100.py:202:        return self.encoder.get(token, self.encoder[self.unk_token])
./venv/lib/python3.12/site-packages/transformers/models/m2m_100/tokenization_m2m_100.py:208:        return self.decoder.get(index, self.unk_token)
./venv/lib/python3.12/site-packages/transformers/models/bartpho/tokenization_bartpho.py:285:            new_id = self.fairseq_tokens_to_ids.get(token, original_id)
./venv/lib/python3.12/site-packages/transformers/models/clvp/tokenization_clvp.py:199:            bigram = min(pairs, key=lambda pair: self.bpe_ranks.get(pair, float("inf")))
./venv/lib/python3.12/site-packages/transformers/models/clvp/tokenization_clvp.py:250:        return self.encoder.get(token, self.encoder.get(self.unk_token))
./venv/lib/python3.12/site-packages/transformers/models/luke/tokenization_luke.py:959:                    first_entity_ids = [self.entity_vocab.get(entity, self.entity_unk_token_id) for entity in entities]
./venv/lib/python3.12/site-packages/transformers/models/luke/tokenization_luke.py:974:                            self.entity_vocab.get(entity, self.entity_unk_token_id) for entity in entities_pair
./venv/lib/python3.12/site-packages/transformers/models/florence2/modular_florence2.py:490:        post_proc_type = self.tasks_answer_post_processing_type.get(task, "pure_text")
./venv/lib/python3.12/site-packages/transformers/models/florence2/processing_florence2.py:290:        post_proc_type = self.tasks_answer_post_processing_type.get(task, "pure_text")
./venv/lib/python3.12/site-packages/transformers/models/chameleon/modeling_chameleon.py:763:            return "".join(img_tkn_chr_mapping.get(c, c) for c in old_name[len("IMGIMG") : -1])
./venv/lib/python3.12/site-packages/transformers/models/flaubert/tokenization_flaubert.py:332:            bigram = min(pairs, key=lambda pair: self.bpe_ranks.get(pair, float("inf")))
./venv/lib/python3.12/site-packages/transformers/models/flaubert/tokenization_flaubert.py:416:        return self.encoder.get(token, self.encoder.get(self.unk_token))
./venv/lib/python3.12/site-packages/transformers/models/flaubert/tokenization_flaubert.py:421:        return self.decoder.get(index, self.unk_token)
./venv/lib/python3.12/site-packages/transformers/models/sam2_video/modeling_sam2_video.py:180:        obj_idx = self._obj_id_to_idx.get(obj_id, None)
./venv/lib/python3.12/site-packages/transformers/models/sam2_video/modeling_sam2_video.py:288:        out = self.output_dict_per_obj[obj_idx][storage_key].get(frame_idx, None)
./venv/lib/python3.12/site-packages/transformers/models/sam2_video/modeling_sam2_video.py:1776:                    point_inputs = inference_session.point_inputs_per_obj[obj_idx].get(frame_idx, None)
./venv/lib/python3.12/site-packages/transformers/models/sam2_video/modeling_sam2_video.py:1777:                    mask_inputs = inference_session.mask_inputs_per_obj[obj_idx].get(frame_idx, None)
./venv/lib/python3.12/site-packages/transformers/models/sam2_video/modeling_sam2_video.py:2235:                previous_frame_idx, unselected_conditioning_outputs.get(previous_frame_idx, None)
./venv/lib/python3.12/site-packages/transformers/models/sam2_video/processing_sam2_video.py:717:                existing_points = inference_session.point_inputs_per_obj[obj_idx].get(frame_idx, None)
./venv/lib/python3.12/site-packages/transformers/models/sam2_video/modular_sam2_video.py:446:        obj_idx = self._obj_id_to_idx.get(obj_id, None)
./venv/lib/python3.12/site-packages/transformers/models/sam2_video/modular_sam2_video.py:554:        out = self.output_dict_per_obj[obj_idx][storage_key].get(frame_idx, None)
./venv/lib/python3.12/site-packages/transformers/models/sam2_video/modular_sam2_video.py:822:                existing_points = inference_session.point_inputs_per_obj[obj_idx].get(frame_idx, None)
./venv/lib/python3.12/site-packages/transformers/models/sam2_video/modular_sam2_video.py:1887:                previous_frame_idx, unselected_conditioning_outputs.get(previous_frame_idx, None)
./venv/lib/python3.12/site-packages/transformers/models/sam2_video/modular_sam2_video.py:2391:                    point_inputs = inference_session.point_inputs_per_obj[obj_idx].get(frame_idx, None)
./venv/lib/python3.12/site-packages/transformers/models/sam2_video/modular_sam2_video.py:2392:                    mask_inputs = inference_session.mask_inputs_per_obj[obj_idx].get(frame_idx, None)
./venv/lib/python3.12/site-packages/transformers/models/bertweet/tokenization_bertweet.py:186:            bigram = min(pairs, key=lambda pair: self.bpe_ranks.get(pair, float("inf")))
./venv/lib/python3.12/site-packages/transformers/models/bertweet/tokenization_bertweet.py:285:        return self.encoder.get(token, self.encoder.get(self.unk_token))
./venv/lib/python3.12/site-packages/transformers/models/bertweet/tokenization_bertweet.py:289:        return self.decoder.get(index, self.unk_token)
./venv/lib/python3.12/site-packages/transformers/models/esm/tokenization_esm.py:70:        return self._id_to_token.get(index, self.unk_token)
./venv/lib/python3.12/site-packages/transformers/models/esm/tokenization_esm.py:73:        return self._token_to_id.get(token, self._token_to_id.get(self.unk_token))
./venv/lib/python3.12/site-packages/transformers/models/esm/tokenization_esm.py:84:        return self._token_to_id.get(token, self._token_to_id.get(self.unk_token))
./venv/lib/python3.12/site-packages/transformers/models/esm/tokenization_esm.py:87:        return self._id_to_token.get(index, self.unk_token)
./venv/lib/python3.12/site-packages/transformers/models/esm/openfold_utils/data_transforms.py:34:        restype_atom37_to_atom14_list.append([(atom_name_to_idx14.get(name, 0)) for name in rc.atom_types])
./venv/lib/python3.12/site-packages/transformers/models/esm/openfold_utils/residue_constants.py:632:                aa_id = mapping.get(aa_type, mapping["X"])
./venv/lib/python3.12/site-packages/transformers/models/esm/openfold_utils/protein.py:87:                [residue_constants.restype_order.get(res_symbol, residue_constants.restype_num) for res_symbol in seq]
./venv/lib/python3.12/site-packages/transformers/models/prophetnet/tokenization_prophetnet.py:389:        return self.vocab.get(token, self.vocab.get(self.unk_token))
./venv/lib/python3.12/site-packages/transformers/models/prophetnet/tokenization_prophetnet.py:393:        return self.ids_to_tokens.get(index, self.unk_token)
./venv/lib/python3.12/site-packages/transformers/models/dia/generation_dia.py:233:                if model_inputs.get(key, None) is not None:
./venv/lib/python3.12/site-packages/transformers/models/perceiver/modeling_perceiver.py:2297:                input_without_pos = inputs_without_pos.get(modality, None)
./venv/lib/python3.12/site-packages/transformers/models/perceiver/modeling_perceiver.py:2302:                subsampled_points=subsampled_points.get(modality, None),
./venv/lib/python3.12/site-packages/transformers/models/biogpt/tokenization_biogpt.py:166:            bigram = min(pairs, key=lambda pair: self.bpe_ranks.get(pair, float("inf")))
./venv/lib/python3.12/site-packages/transformers/models/biogpt/tokenization_biogpt.py:216:        return self.encoder.get(token, self.encoder.get(self.unk_token))
./venv/lib/python3.12/site-packages/transformers/models/biogpt/tokenization_biogpt.py:220:        return self.decoder.get(index, self.unk_token)
./venv/lib/python3.12/site-packages/transformers/models/rt_detr/modular_rt_detr.py:1495:        >>> image = Image.open(requests.get(url, stream=True).raw)
./venv/lib/python3.12/site-packages/transformers/models/rt_detr/modular_rt_detr.py:1721:        >>> image = Image.open(requests.get(url, stream=True).raw)
./venv/lib/python3.12/site-packages/transformers/models/rt_detr/modeling_rt_detr.py:1510:        >>> image = Image.open(requests.get(url, stream=True).raw)
./venv/lib/python3.12/site-packages/transformers/models/rt_detr/modeling_rt_detr.py:1736:        >>> image = Image.open(requests.get(url, stream=True).raw)
./venv/lib/python3.12/site-packages/transformers/models/seamless_m4t_v2/modeling_seamless_m4t_v2.py:1455:                    char_ids = [self.generation_config.char_to_id.get(ch, unk_token_id) for ch in list(subword)]
./venv/lib/python3.12/site-packages/transformers/models/pp_doclayout_v3/modular_pp_doclayout_v3.py:1141:        >>> image = Image.open(requests.get(url, stream=True).raw)
./venv/lib/python3.12/site-packages/transformers/models/pp_doclayout_v3/modular_pp_doclayout_v3.py:1461:        >>> image = Image.open(requests.get(url, stream=True).raw)
./venv/lib/python3.12/site-packages/transformers/models/pp_doclayout_v3/modeling_pp_doclayout_v3.py:1678:        >>> image = Image.open(requests.get(url, stream=True).raw)
./venv/lib/python3.12/site-packages/transformers/models/pp_doclayout_v3/modeling_pp_doclayout_v3.py:2001:        >>> image = Image.open(requests.get(url, stream=True).raw)
./venv/lib/python3.12/site-packages/transformers/models/blenderbot_small/tokenization_blenderbot_small.py:133:                bigram = min(pairs, key=lambda pair: self.bpe_ranks.get(pair, float("inf")))
./venv/lib/python3.12/site-packages/transformers/models/blenderbot_small/tokenization_blenderbot_small.py:181:        return self.encoder.get(token, self.encoder.get(self.unk_token))
./venv/lib/python3.12/site-packages/transformers/models/blenderbot_small/tokenization_blenderbot_small.py:185:        return self.decoder.get(index, self.unk_token)
./venv/lib/python3.12/site-packages/transformers/models/mgp_str/tokenization_mgp_str.py:83:        return self.vocab.get(token, self.vocab.get(self.unk_token))
./venv/lib/python3.12/site-packages/transformers/models/wav2vec2_phoneme/tokenization_wav2vec2_phoneme.py:321:        return self.encoder.get(token, self.encoder.get(self.unk_token))
./venv/lib/python3.12/site-packages/transformers/models/wav2vec2_phoneme/tokenization_wav2vec2_phoneme.py:325:        result = self.decoder.get(index, self.unk_token)
./venv/lib/python3.12/site-packages/transformers/models/edgetam_video/modular_edgetam_video.py:1297:                    point_inputs = inference_session.point_inputs_per_obj[obj_idx].get(frame_idx, None)
./venv/lib/python3.12/site-packages/transformers/models/edgetam_video/modular_edgetam_video.py:1298:                    mask_inputs = inference_session.mask_inputs_per_obj[obj_idx].get(frame_idx, None)
./venv/lib/python3.12/site-packages/transformers/models/edgetam_video/modeling_edgetam_video.py:978:        obj_idx = self._obj_id_to_idx.get(obj_id, None)
./venv/lib/python3.12/site-packages/transformers/models/edgetam_video/modeling_edgetam_video.py:1086:        out = self.output_dict_per_obj[obj_idx][storage_key].get(frame_idx, None)
./venv/lib/python3.12/site-packages/transformers/models/edgetam_video/modeling_edgetam_video.py:2188:                    point_inputs = inference_session.point_inputs_per_obj[obj_idx].get(frame_idx, None)
./venv/lib/python3.12/site-packages/transformers/models/edgetam_video/modeling_edgetam_video.py:2189:                    mask_inputs = inference_session.mask_inputs_per_obj[obj_idx].get(frame_idx, None)
./venv/lib/python3.12/site-packages/transformers/models/edgetam_video/modeling_edgetam_video.py:2620:                previous_frame_idx, unselected_conditioning_outputs.get(previous_frame_idx, None)
./venv/lib/python3.12/site-packages/transformers/models/sam3_tracker_video/processing_sam3_tracker_video.py:719:                existing_points = inference_session.point_inputs_per_obj[obj_idx].get(frame_idx, None)
./venv/lib/python3.12/site-packages/transformers/models/sam3_tracker_video/modeling_sam3_tracker_video.py:185:        obj_idx = self._obj_id_to_idx.get(obj_id, None)
./venv/lib/python3.12/site-packages/transformers/models/sam3_tracker_video/modeling_sam3_tracker_video.py:293:        out = self.output_dict_per_obj[obj_idx][storage_key].get(frame_idx, None)
./venv/lib/python3.12/site-packages/transformers/models/sam3_tracker_video/modeling_sam3_tracker_video.py:1799:                    point_inputs = inference_session.point_inputs_per_obj[obj_idx].get(frame_idx, None)
./venv/lib/python3.12/site-packages/transformers/models/sam3_tracker_video/modeling_sam3_tracker_video.py:1800:                    mask_inputs = inference_session.mask_inputs_per_obj[obj_idx].get(frame_idx, None)
./venv/lib/python3.12/site-packages/transformers/models/sam3_tracker_video/modeling_sam3_tracker_video.py:2260:                previous_frame_idx, unselected_conditioning_outputs.get(previous_frame_idx, None)
./venv/lib/python3.12/site-packages/transformers/models/pop2piano/tokenization_pop2piano.py:146:        token_type_value = self.decoder.get(token_id, f"{self.unk_token}_TOKEN_TIME")
./venv/lib/python3.12/site-packages/transformers/models/xlm/tokenization_xlm.py:330:            bigram = min(pairs, key=lambda pair: self.bpe_ranks.get(pair, float("inf")))
./venv/lib/python3.12/site-packages/transformers/models/xlm/tokenization_xlm.py:464:        return self.encoder.get(token, self.encoder.get(self.unk_token))
./venv/lib/python3.12/site-packages/transformers/models/xlm/tokenization_xlm.py:468:        return self.decoder.get(index, self.unk_token)
./venv/lib/python3.12/site-packages/transformers/models/roc_bert/tokenization_roc_bert.py:962:        return self.vocab.get(token, self.vocab.get(self.unk_token))
./venv/lib/python3.12/site-packages/transformers/models/roc_bert/tokenization_roc_bert.py:966:        return self.word_shape.get(token, self.word_shape.get(self.unk_token))
./venv/lib/python3.12/site-packages/transformers/models/roc_bert/tokenization_roc_bert.py:979:        return self.word_pronunciation.get(token, self.word_pronunciation.get(self.unk_token))
./venv/lib/python3.12/site-packages/transformers/models/roc_bert/tokenization_roc_bert.py:992:        return self.ids_to_tokens.get(index, self.unk_token)
./venv/lib/python3.12/site-packages/transformers/models/mluke/tokenization_mluke.py:986:                    first_entity_ids = [self.entity_vocab.get(entity, self.entity_unk_token_id) for entity in entities]
./venv/lib/python3.12/site-packages/transformers/models/mluke/tokenization_mluke.py:1001:                            self.entity_vocab.get(entity, self.entity_unk_token_id) for entity in entities_pair
./venv/lib/python3.12/site-packages/transformers/models/conditional_detr/modeling_conditional_detr.py:1371:        >>> image = Image.open(requests.get(url, stream=True).raw)
./venv/lib/python3.12/site-packages/transformers/models/conditional_detr/modeling_conditional_detr.py:1530:        >>> image = Image.open(requests.get(url, stream=True).raw)
./venv/lib/python3.12/site-packages/transformers/models/conditional_detr/modular_conditional_detr.py:741:        >>> image = Image.open(requests.get(url, stream=True).raw)
./venv/lib/python3.12/site-packages/transformers/models/conditional_detr/modular_conditional_detr.py:882:        >>> image = Image.open(requests.get(url, stream=True).raw)
./venv/lib/python3.12/site-packages/transformers/models/grounding_dino/processing_grounding_dino.py:97:        return super().get(key, *args, **kwargs)
./venv/lib/python3.12/site-packages/transformers/models/ctrl/tokenization_ctrl.py:163:            bigram = min(pairs, key=lambda pair: self.bpe_ranks.get(pair, float("inf")))
./venv/lib/python3.12/site-packages/transformers/models/ctrl/tokenization_ctrl.py:208:        return self.encoder.get(token, self.encoder.get(self.unk_token))
./venv/lib/python3.12/site-packages/transformers/models/ctrl/tokenization_ctrl.py:212:        return self.decoder.get(index, self.unk_token)
./venv/lib/python3.12/site-packages/transformers/models/gpt_neox_japanese/tokenization_gpt_neox_japanese.py:153:        return self.vocab.get(token, self.vocab.get(self.unk_token))
./venv/lib/python3.12/site-packages/transformers/models/bert/tokenization_bert_legacy.py:173:        return self.vocab.get(token, self.vocab.get(self.unk_token))
./venv/lib/python3.12/site-packages/transformers/models/bert/tokenization_bert_legacy.py:177:        return self.ids_to_tokens.get(index, self.unk_token)
./venv/lib/python3.12/site-packages/transformers/models/deformable_detr/modeling_deformable_detr.py:1332:        >>> image = Image.open(requests.get(url, stream=True).raw)
./venv/lib/python3.12/site-packages/transformers/models/deformable_detr/modeling_deformable_detr.py:1596:        >>> image = Image.open(requests.get(url, stream=True).raw)
./venv/lib/python3.12/site-packages/transformers/models/deformable_detr/modular_deformable_detr.py:1114:        >>> image = Image.open(requests.get(url, stream=True).raw)
./venv/lib/python3.12/site-packages/transformers/models/deformable_detr/modular_deformable_detr.py:1363:        >>> image = Image.open(requests.get(url, stream=True).raw)
./venv/lib/python3.12/site-packages/transformers/models/bert_japanese/tokenization_bert_japanese.py:248:        return self.vocab.get(token, self.vocab.get(self.unk_token))
./venv/lib/python3.12/site-packages/transformers/models/bert_japanese/tokenization_bert_japanese.py:254:        return self.ids_to_tokens.get(index, self.unk_token)
./venv/lib/python3.12/site-packages/transformers/models/plbart/tokenization_plbart.py:334:        lang = FAIRSEQ_LANGUAGE_CODES_MAP.get(lang, lang)
./venv/lib/python3.12/site-packages/transformers/models/fsmt/tokenization_fsmt.py:286:            bigram = min(pairs, key=lambda pair: self.bpe_ranks.get(pair, float("inf")))
./venv/lib/python3.12/site-packages/transformers/models/fsmt/tokenization_fsmt.py:361:        return self.encoder.get(token, self.encoder.get(self.unk_token))
./venv/lib/python3.12/site-packages/transformers/models/fsmt/tokenization_fsmt.py:365:        return self.decoder.get(index, self.unk_token)
./venv/lib/python3.12/site-packages/transformers/generation/continuous_batching/cache_manager.py:361:        block_table = self.block_table.get(request_id, [])
./venv/lib/python3.12/site-packages/transformers/generation/continuous_batching/cache.py:44:        layer_counts[layer_type] = layer_counts.get(layer_type, []) + [i]
./venv/lib/python3.12/site-packages/transformers/generation/logits_process.py:1036:            generated_ngram[prev_ngram_tuple] = generated_ngram.get(prev_ngram_tuple, []) + [ngram[-1]]
./venv/lib/python3.12/site-packages/transformers/generation/logits_process.py:1060:    return banned_ngrams.get(ngram_idx, [])
./venv/lib/python3.12/site-packages/transformers/pipelines/zero_shot_audio_classification.py:109:                audio = httpx.get(audio, follow_redirects=True).content
./venv/lib/python3.12/site-packages/transformers/pipelines/table_question_answering.py:366:                aggregator = aggregators.get(index, "")
./venv/lib/python3.12/site-packages/transformers/pipelines/table_question_answering.py:367:                aggregator_prefix = aggregators_prefix.get(index, "")
./venv/lib/python3.12/site-packages/transformers/pipelines/audio_classification.py:171:                inputs = httpx.get(inputs, follow_redirects=True).content
./venv/lib/python3.12/site-packages/transformers/pipelines/video_classification.py:137:            video = BytesIO(httpx.get(video, follow_redirects=True).content)
./venv/lib/python3.12/site-packages/transformers/pipelines/automatic_speech_recognition.py:368:                inputs = httpx.get(inputs, follow_redirects=True).content
./venv/lib/python3.12/site-packages/transformers/modeling_utils.py:2023:                    else attn_implementation.get(subconfig_key, subconfig._attn_implementation)
./venv/lib/python3.12/site-packages/transformers/modeling_utils.py:4734:        return super().get(attn_implementation, default)
./venv/lib/python3.12/site-packages/transformers/processing_utils.py:1167:        args = [args_to_update.get(i, arg) for i, arg in enumerate(args)]
./venv/lib/python3.12/site-packages/transformers/processing_utils.py:1254:            default_kwargs[modality] = ModelProcessorKwargs._defaults.get(modality, {}).copy()
./venv/lib/python3.12/site-packages/transformers/processing_utils.py:1315:                    kwarg_value = kwargs.get(modality_key, "__empty__")
./venv/lib/python3.12/site-packages/transformers/hf_argparser.py:61:    return lambda arg: str_to_choice.get(arg, arg)
./venv/lib/python3.12/site-packages/transformers/data/metrics/squad_metrics.py:456:                    if not feature.token_is_max_context.get(start_index, False):
./venv/lib/python3.12/site-packages/transformers/data/metrics/squad_metrics.py:666:                    if not feature.token_is_max_context.get(start_index, False):
./venv/lib/python3.12/site-packages/numpy/f2py/use_rules.py:68:            varsmap[v] = revmap.get(v, v)
./venv/lib/python3.12/site-packages/numpy/f2py/auxfuncs.py:303:        for d in rout['vars'].get(a, {}).get('dimension', []):
./venv/lib/python3.12/site-packages/numpy/f2py/auxfuncs.py:789:    return rout['f2pymultilines'].get(k, None)
./venv/lib/python3.12/site-packages/numpy/f2py/crackfortran.py:2362:            for w in deps.get(word, []) \
./venv/lib/python3.12/site-packages/numpy/f2py/crackfortran.py:2589:                        vars[n] = setattrspec(vars.get(n, {}), k)
./venv/lib/python3.12/site-packages/numpy/f2py/crackfortran.py:2789:                                for v1 in coeffs_and_deps.get(v, [None, []])[1]:
./venv/lib/python3.12/site-packages/numpy/f2py/crackfortran.py:3134:            block['vars'][a] = block['vars'].get(orig_a, {})
./venv/lib/python3.12/site-packages/numpy/f2py/tests/test_character.py:20:        clength = {'star': '(*)'}.get(length, length)
./venv/lib/python3.12/site-packages/numpy/f2py/tests/test_character.py:81:        fsuffix = {'(*)': 'star'}.get(length, length)
./venv/lib/python3.12/site-packages/numpy/f2py/_src_pyf.py:157:            thelist = lnames.get(r, names.get(r, None))
./venv/lib/python3.12/site-packages/numpy/f2py/_src_pyf.py:181:        return rules.get(name, (k + 1) * [name])[k]
./venv/lib/python3.12/site-packages/numpy/lib/_iotools.py:374:            cnt = seen.get(item, 0)
./venv/lib/python3.12/site-packages/numpy/lib/recfunctions.py:265:            lastparent = list(parents.get(lastname, []) or [])
./venv/lib/python3.12/site-packages/numpy/lib/recfunctions.py:635:            newname = namemapper.get(name, name)
./venv/lib/python3.12/site-packages/numpy/lib/_npyio_impl.py:288:        D.get(k,[,d]) returns D[k] if k in D, else d.  d defaults to None.
./venv/lib/python3.12/site-packages/numpy/lib/_npyio_impl.py:290:        return Mapping.get(self, key, default)
./venv/lib/python3.12/site-packages/numpy/_utils/_pep440.py:208:        part = _legacy_version_replacement_map.get(part, part)
./venv/lib/python3.12/site-packages/numpy/linalg/_linalg.py:184:    return _real_types_map.get(t, default)
./venv/lib/python3.12/site-packages/numpy/linalg/_linalg.py:187:    return _complex_types_map.get(t, default)
./venv/lib/python3.12/site-packages/numpy/testing/print_coercion_tables.py:158:            row = table.get(from_dt, {})
./venv/lib/python3.12/site-packages/numpy/testing/print_coercion_tables.py:160:                print(getattr(row.get(to_dt, no_cast_info), field), end=' ')
./venv/lib/python3.12/site-packages/numpy/matrixlib/tests/test_defmatrix.py:304:                args = methodargs.get(attrib, ())
./venv/lib/python3.12/site-packages/numpy/_core/records.py:223:        res = fielddict.get(attr, None)
./venv/lib/python3.12/site-packages/numpy/_core/records.py:243:        res = fielddict.get(attr, None)
./venv/lib/python3.12/site-packages/numpy/_core/getlimits.py:221:                obj = cls._finfo_cache.get(dtype, None)
./venv/lib/python3.12/site-packages/numpy/_core/tests/test_regression.py:2345:            item = sctype(values.get(sctype, 1))
./venv/lib/python3.12/site-packages/numpy/_core/tests/test_regression.py:2383:            scvalue = sctype(values.get(ch, 3))
./venv/lib/python3.12/site-packages/numpy/_core/tests/test_cpu_features.py:90:        map_names = self.features_map.get(feature_name, feature_name)
./venv/lib/python3.12/site-packages/numpy/_core/tests/test_umath.py:4338:            cname = name_map.get(fname, fname)
./venv/lib/python3.12/site-packages/numpy/_core/tests/test_simd.py:1337:            skip_m = skip_sfx.get(sfx, skip)
./venv/lib/python3.12/site-packages/numpy/_core/_internal.py:184:            order1 = _convorder.get(order1, order1)
./venv/lib/python3.12/site-packages/numpy/_core/_internal.py:185:            order2 = _convorder.get(order2, order2)
./venv/lib/python3.12/site-packages/yaml/resolver.py:149:            wildcard_resolvers = self.yaml_implicit_resolvers.get(None, [])
./venv/lib/python3.12/site-packages/pygments/style.py:88:                styledefs = obj.styles.get(token, '').split()
./venv/lib/python3.12/site-packages/pygments/style.py:96:                for styledef in obj.styles.get(token, '').split():
./venv/lib/python3.12/site-packages/pygments/util.py:45:    string = options.get(optname, default)
./venv/lib/python3.12/site-packages/pygments/util.py:55:    Intuitively, this is `options.get(optname, default)`, but restricted to
./venv/lib/python3.12/site-packages/pygments/util.py:65:    string = options.get(optname, default)
./venv/lib/python3.12/site-packages/pygments/util.py:84:    string = options.get(optname, default)
./venv/lib/python3.12/site-packages/pygments/util.py:100:    val = options.get(optname, default)
./venv/lib/python3.12/site-packages/pygments/lexers/lisp.py:2415:                token = self.MAPPINGS.get(value, Name.Function)
./venv/lib/python3.12/site-packages/pygments/lexers/robotframework.py:143:        return self._tables.get(name, UnknownTable())
./venv/lib/python3.12/site-packages/pygments/formatters/terminal256.py:206:        index = self.best_match.get(color, None)
./venv/lib/python3.12/site-packages/pygments/filters/__init__.py:824:            opt = options.get(name, False)
./venv/lib/python3.12/site-packages/pygments/plugin.py:52:        return groups.get(group_name, [])
./venv/lib/python3.12/site-packages/httpcore/_async/socks_proxy.py:66:        requested = AUTH_METHODS.get(auth_method, "UNKNOWN")
./venv/lib/python3.12/site-packages/httpcore/_sync/socks_proxy.py:66:        requested = AUTH_METHODS.get(auth_method, "UNKNOWN")
./venv/lib/python3.12/site-packages/cuda/pathfinder/_dynamic_libs/load_dl_linux.py:129:    candidate_sonames = list(reversed(SUPPORTED_LINUX_SONAMES.get(libname, ())))
./venv/lib/python3.12/site-packages/cuda/pathfinder/_dynamic_libs/load_dl_windows.py:103:    for dll_name in SUPPORTED_WINDOWS_DLLS.get(libname, ()):
./venv/lib/python3.12/site-packages/cuda/pathfinder/_dynamic_libs/load_dl_windows.py:126:    for dll_name in reversed(SUPPORTED_WINDOWS_DLLS.get(libname, ())):
./venv/lib/python3.12/site-packages/cuda/pathfinder/_dynamic_libs/load_dl_common.py:23:    for dep in DIRECT_DEPENDENCIES.get(libname, ()):
./venv/lib/python3.12/site-packages/cuda/pathfinder/_headers/find_nvidia_headers.py:152:    candidate_dirs = supported_nvidia_headers.SUPPORTED_SITE_PACKAGE_HEADER_DIRS_NON_CTK.get(libname, [])
./venv/lib/python3.12/site-packages/cuda/pathfinder/_headers/find_nvidia_headers.py:162:    candidate_dirs = supported_nvidia_headers.SUPPORTED_INSTALL_DIRS_NON_CTK.get(libname, [])
./venv/lib/python3.12/site-packages/cuda/pathfinder/_binaries/find_nvidia_binary_utility.py:86:    candidate_dirs = supported_nvidia_binaries.SITE_PACKAGES_BINDIRS.get(utility_name, ())
./venv/lib/python3.12/site-packages/regex/_regex_core.py:4400:        self.open_group_count[group] = self.open_group_count.get(group, 0) + 1
./venv/lib/python3.12/site-packages/regex/_regex_core.py:4583:    name, prop_values = PROPERTY_NAMES.get(prop_id, ("", {}))
./venv/lib/python3.12/site-packages/regex/_regex_core.py:4588:        prop_values[val_id] = max(prop_values.get(val_id, ""), val_name,
./venv/lib/python3.12/site-packages/regex/_main.py:464:    if _locale_sensitive.get(locale_key, True) or (flags & LOCALE) != 0:
./venv/lib/python3.12/site-packages/sympy/multipledispatch/utils.py:51:        for m in edges.get(n, ()):
./venv/lib/python3.12/site-packages/sympy/multipledispatch/utils.py:56:    if any(incoming_edges.get(v, None) for v in edges):
./venv/lib/python3.12/site-packages/sympy/multipledispatch/utils.py:77:            result[val] = result.get(val, ()) + (key, )
./venv/lib/python3.12/site-packages/sympy/integrals/rationaltools.py:385:    a, b = H_map.get(S.One, S.Zero), H_map.get(I, S.Zero)
./venv/lib/python3.12/site-packages/sympy/integrals/rationaltools.py:386:    c, d = Q_map.get(S.One, S.Zero), Q_map.get(I, S.Zero)
./venv/lib/python3.12/site-packages/sympy/integrals/manualintegrate.py:993:            var_index = orthogonal_poly_var_index.get(klass, 1)
./venv/lib/python3.12/site-packages/sympy/integrals/manualintegrate.py:1149:    a, b, c = [match.get(i, S.Zero) for i in (a, b, c)]
./venv/lib/python3.12/site-packages/sympy/integrals/manualintegrate.py:1734:            [match.get(i, S.Zero) for i in (a, b, m, n)] +
./venv/lib/python3.12/site-packages/sympy/integrals/manualintegrate.py:1755:            [match.get(i, S.Zero) for i in (a, b, m, n)] +
./venv/lib/python3.12/site-packages/sympy/integrals/manualintegrate.py:1776:            [match.get(i, S.Zero) for i in (a, b, m, n)] +
./venv/lib/python3.12/site-packages/sympy/integrals/manualintegrate.py:1803:        a = match.get(A, S.Zero)
./venv/lib/python3.12/site-packages/sympy/integrals/manualintegrate.py:1804:        b = match.get(B, S.Zero)
./venv/lib/python3.12/site-packages/sympy/integrals/heurisch.py:665:            y = m.get(I, S.Zero)
./venv/lib/python3.12/site-packages/sympy/integrals/intpoly.py:304:                value = result.get(m, None)
./venv/lib/python3.12/site-packages/sympy/printing/pytorch.py:156:                    var_groups[base_var] = var_groups.get(base_var, 0) + order
./venv/lib/python3.12/site-packages/sympy/printing/pytorch.py:158:                    var_groups[var] = var_groups.get(var, 0) + 1
./venv/lib/python3.12/site-packages/sympy/printing/llvmjitcode.py:131:        array, idx = self.func_arg_map.get(s, [None, 0])
./venv/lib/python3.12/site-packages/sympy/printing/tableform.py:166:                return {'left': 'l', 'right': 'r', 'center': 'c'}.get(a, a)
./venv/lib/python3.12/site-packages/sympy/printing/tableform.py:168:                return {'<': 'l', '>': 'r', '^': 'c'}.get(a, a)
./venv/lib/python3.12/site-packages/sympy/printing/fortran.py:432:        type_ = self.type_aliases.get(type_, type_)
./venv/lib/python3.12/site-packages/sympy/printing/fortran.py:433:        type_str = self.type_mappings.get(type_, type_.name)
./venv/lib/python3.12/site-packages/sympy/printing/latex.py:224:        self._settings['imaginary_unit_latex'] = imaginary_unit_table.get(imag_unit, imag_unit)
./venv/lib/python3.12/site-packages/sympy/printing/latex.py:233:        self._settings["diff_operator_latex"] = diff_operator_table.get(diff_operator, diff_operator)
./venv/lib/python3.12/site-packages/sympy/printing/c.py:466:        return self.type_func_suffixes[self.type_aliases.get(type_, type_)]
./venv/lib/python3.12/site-packages/sympy/printing/c.py:469:        return self.type_literal_suffixes[self.type_aliases.get(type_, type_)]
./venv/lib/python3.12/site-packages/sympy/printing/c.py:472:        alias = self.type_aliases.get(type_, type_)
./venv/lib/python3.12/site-packages/sympy/printing/c.py:473:        dflt = self.type_math_macro_suffixes.get(alias, '')
./venv/lib/python3.12/site-packages/sympy/printing/c.py:474:        return self.type_math_macro_suffixes.get(type_, dflt)
./venv/lib/python3.12/site-packages/sympy/printing/c.py:482:        self.headers.update(self.type_headers.get(type_, set()))
./venv/lib/python3.12/site-packages/sympy/printing/c.py:483:        self.macros.update(self.type_macros.get(type_, set()))
./venv/lib/python3.12/site-packages/sympy/printing/c.py:484:        return self._print(self.type_mappings.get(type_, type_.name))
./venv/lib/python3.12/site-packages/sympy/printing/c.py:514:        type_ = self.type_aliases.get(real, real)
./venv/lib/python3.12/site-packages/sympy/printing/c.py:515:        self.macros.update(self.type_macros.get(type_, set()))
./venv/lib/python3.12/site-packages/sympy/printing/preview.py:275:        for candidate in candidates.get(output, []):
./venv/lib/python3.12/site-packages/sympy/printing/preview.py:365:                cmd.extend(defaultoptions.get(cmd_variant, []))
./venv/lib/python3.12/site-packages/sympy/printing/pycode.py:274:        func = self.known_functions.get(name, name)
./venv/lib/python3.12/site-packages/sympy/printing/lambdarepr.py:123:        nstr = self._numexpr_functions.get(func_name, None)
./venv/lib/python3.12/site-packages/sympy/tensor/array/sparse_ndim_array.py:62:            return self._sparse_array.get(index, S.Zero)
./venv/lib/python3.12/site-packages/sympy/tensor/array/expressions/array_expressions.py:1714:            arg_with_ind.indices = [updates.get(i, None) for i in arg_with_ind.indices]
./venv/lib/python3.12/site-packages/sympy/tensor/array/expressions/from_indexed_to_array.py:83:    first_indices = [repl.get(i, i) for i in first_indices]
./venv/lib/python3.12/site-packages/sympy/tensor/array/expressions/from_indexed_to_array.py:112:        summation_indices = sorted({subindicessets.get(i, i) for i in summation_indices}, key=default_sort_key)
./venv/lib/python3.12/site-packages/sympy/tensor/array/expressions/from_indexed_to_array.py:194:        flattened_indices = [kronecker_delta_repl.get(j, j) for i in newindices for j in i]
./venv/lib/python3.12/site-packages/sympy/tensor/tensor.py:956:        return self._comm[i].get(j, 0 if i == 0 or j == 0 else None)
./venv/lib/python3.12/site-packages/sympy/tensor/tensor.py:4524:        index_map = {name_translation.get(index, index): value for index, value in index_map.items()}
./venv/lib/python3.12/site-packages/sympy/tensor/tensor.py:4572:        slice_tuple = tuple(index_map.get(i, slice(None)) for i in ret_indices)
./venv/lib/python3.12/site-packages/sympy/simplify/radsimp.py:181:        syms = [reps.get(s, s) for s in syms]
./venv/lib/python3.12/site-packages/sympy/simplify/radsimp.py:189:            return {urep.get(k, k).xreplace(urep): v.xreplace(urep)
./venv/lib/python3.12/site-packages/sympy/simplify/trigsimp.py:1026:                if res and res.get(c, 0):
./venv/lib/python3.12/site-packages/sympy/concrete/expr_with_limits.py:341:        return {reps.get(_, _) for _ in isyms}
./venv/lib/python3.12/site-packages/sympy/concrete/summations.py:1652:        assum_true = x._assumptions.get(assum, None)
./venv/lib/python3.12/site-packages/sympy/functions/elementary/exponential.py:1027:                    res[ex] = res.get(ex, S.Zero) + d1[e1]*d2[e2]
./venv/lib/python3.12/site-packages/sympy/functions/elementary/exponential.py:1034:            pterms[e1] = pterms.get(e1, S.Zero) + co1
./venv/lib/python3.12/site-packages/sympy/functions/elementary/exponential.py:1043:                terms[ex] = terms.get(ex, S.Zero) + coeff*pk[ex]
./venv/lib/python3.12/site-packages/sympy/functions/special/bsplines.py:345:            [c * d.get(i, S.Zero) for (c, d) in zip(coeff, basis_dicts)], S.Zero
./venv/lib/python3.12/site-packages/sympy/series/fourier.py:597:        _term = self.an.get(pt, S.Zero) * cos(pt * (pi / self.L) * self.x) \
./venv/lib/python3.12/site-packages/sympy/series/fourier.py:598:                + self.bn.get(pt, S.Zero) * sin(pt * (pi / self.L) * self.x)
./venv/lib/python3.12/site-packages/sympy/matrices/eigen.py:250:            all_eigs[val] = all_eigs.get(val, 0) + 1
./venv/lib/python3.12/site-packages/sympy/physics/units/util.py:41:    camat = Matrix([[dimension_system.get_dimensional_dependencies(i, mark_dimensionless=True).get(j, 0) for i in target_dims] for j in canon_dim_units])
./venv/lib/python3.12/site-packages/sympy/physics/units/util.py:42:    exprmat = Matrix([dim_dependencies.get(k, 0) for k in canon_dim_units])
./venv/lib/python3.12/site-packages/sympy/physics/units/dimensions.py:321:                dimensional_dependencies[dim].get(dim, None) != 1)):
./venv/lib/python3.12/site-packages/sympy/physics/units/dimensions.py:384:            return dict(self.dimensional_dependencies.get(dimension, {dimension: 1}))
./venv/lib/python3.12/site-packages/sympy/physics/units/dimensions.py:539:            vec.append(self.get_dimensional_dependencies(dim).get(d, 0))
./venv/lib/python3.12/site-packages/sympy/assumptions/cnf.py:238:        newpred = composite_map.get(pred, None)
./venv/lib/python3.12/site-packages/sympy/assumptions/cnf.py:243:        newpred = composite_map.get(expr, None)
./venv/lib/python3.12/site-packages/sympy/assumptions/cnf.py:434:        value = self.encoding.get(literal, None)
./venv/lib/python3.12/site-packages/sympy/assumptions/refine.py:60:    handler = handlers_dict.get(name, None)
./venv/lib/python3.12/site-packages/sympy/assumptions/ask.py:577:                prop_facts = known_facts_dict.get(key, None)
./venv/lib/python3.12/site-packages/sympy/stats/frv.py:255:            return density.get(elem, S.Zero)
./venv/lib/python3.12/site-packages/sympy/stats/frv.py:268:            d[val] = d.get(val, S.Zero) + prob
./venv/lib/python3.12/site-packages/sympy/stats/frv.py:500:            d[elem] = d.get(elem, S.Zero) + prob
./venv/lib/python3.12/site-packages/sympy/stats/stochastic_process_types.py:527:            condition = type(condition)(self.index_of.get(lhs, lhs),
./venv/lib/python3.12/site-packages/sympy/stats/stochastic_process_types.py:528:                                        self.index_of.get(rhs, rhs))
./venv/lib/python3.12/site-packages/sympy/stats/stochastic_process_types.py:695:                    if state2cond.get(ris, None) is None:
./venv/lib/python3.12/site-packages/sympy/stats/rv.py:1477:        results[result] = results.get(result, 0) + 1
./venv/lib/python3.12/site-packages/sympy/utilities/_compilation/compilation.py:92:        file_kwargs.update(_per_file_kwargs.get(f, {}))
./venv/lib/python3.12/site-packages/sympy/utilities/misc.py:339:        rv = alias.get(rv, rv)
./venv/lib/python3.12/site-packages/sympy/parsing/mathematica.py:1076:                return self._atom_conversions.get(expr, sympify(expr))
./venv/lib/python3.12/site-packages/sympy/parsing/latex/_antlr/latexparser.py:3614:        pred = self._predicates.get(ruleIndex, None)
./venv/lib/python3.12/site-packages/sympy/parsing/autolev/_antlr/autolevparser.py:3034:        pred = self._predicates.get(ruleIndex, None)
./venv/lib/python3.12/site-packages/sympy/ntheory/factor_.py:719:        self._cache[n] = max(self._cache.get(n, 0), factor)
./venv/lib/python3.12/site-packages/sympy/ntheory/factor_.py:1538:                    factors[k] = factors.get(k, 0) + v
./venv/lib/python3.12/site-packages/sympy/unify/rewrite.py:47:                not condition(*[match.get(var, var) for var in variables])):
./venv/lib/python3.12/site-packages/sympy/core/assumptions.py:624:        v = cls.__dict__.get(attrname, '')
./venv/lib/python3.12/site-packages/sympy/core/power.py:1575:                    res[ex] = res.get(ex, S.Zero) + d1[e1]*d2[e2]
./venv/lib/python3.12/site-packages/sympy/core/power.py:1609:            gterms[e1] = gterms.get(e1, S.Zero) + co1
./venv/lib/python3.12/site-packages/sympy/core/power.py:1620:                terms[ex] = terms.get(ex, S.Zero) + coeff*tk[ex]
./venv/lib/python3.12/site-packages/sympy/core/evalf.py:1385:        cached, cached_prec = cache.get(x, (None, MINUS_INF))
./venv/lib/python3.12/site-packages/sympy/core/basic.py:142:        f = mapping.get(clsname, None)
./venv/lib/python3.12/site-packages/sympy/core/basic.py:2255:        return rule.get(self, self)
./venv/lib/python3.12/site-packages/sympy/core/relational.py:166:        cls = cls.ValidRelationOperator.get(rop, None)
./venv/lib/python3.12/site-packages/sympy/core/exprtools.py:366:                factors[I] = factors.get(I, S.Zero) + i
./venv/lib/python3.12/site-packages/sympy/core/function.py:224:        return lambda rule, **_: rule.get(self, self)
./venv/lib/python3.12/site-packages/sympy/core/function.py:543:                fname = MPMATH_TRANSLATIONS.get(fname, None)
./venv/lib/python3.12/site-packages/sympy/core/function.py:1759:            wrt = {syms.get(vi, vi) for vi in self._wrt_variables}
./venv/lib/python3.12/site-packages/sympy/core/containers.py:312:        return self._dict.get(key, default)
./venv/lib/python3.12/site-packages/sympy/vector/basisdependent.py:207:                components[x] = components.get(x, 0) + arg.components[x]
./venv/lib/python3.12/site-packages/sympy/polys/domains/algebraicfield.py:626:    matrix = [[todom(t.get(a, S.Zero)) for t in terms] for a in algebraics]
./venv/lib/python3.12/site-packages/sympy/polys/galoistools.py:301:            h.append(f.get(k, K.zero) % p)
./venv/lib/python3.12/site-packages/sympy/polys/matrices/sdm.py:112:            rowi = self.get(i, None)
./venv/lib/python3.12/site-packages/sympy/polys/matrices/sdm.py:969:        Emap = {v: list(A.get(v, [])) for v in V}
./venv/lib/python3.12/site-packages/sympy/polys/matrices/sdm.py:1273:                Ai = Anew.get(i, None)
./venv/lib/python3.12/site-packages/sympy/polys/matrices/sdm.py:1385:        return [row.get(i, zero) for i, row in self.items() if i < n]
./venv/lib/python3.12/site-packages/sympy/polys/matrices/sdm.py:1512:                Cij = Ci.get(j, None)
./venv/lib/python3.12/site-packages/sympy/polys/matrices/sdm.py:1551:                    Ci_list[j].append(Aik * B[k].get(j, zero))
./venv/lib/python3.12/site-packages/sympy/polys/matrices/sdm.py:1574:                    Aik = A.get(i, {}).get(k, zero)
./venv/lib/python3.12/site-packages/sympy/polys/matrices/sdm.py:1577:                        Ci = C.get(i, {})
./venv/lib/python3.12/site-packages/sympy/polys/matrices/sdm.py:1578:                        Cij = Ci.get(j, zero) + Aik * Bkj
./venv/lib/python3.12/site-packages/sympy/polys/matrices/sdm.py:2066:        for i in nonzero_cols.get(j, ()):
./venv/lib/python3.12/site-packages/sympy/polys/densebasic.py:943:            h.append(f.get(k, K.zero))
./venv/lib/python3.12/site-packages/sympy/polys/densebasic.py:973:        h.append(f.get(k, K.zero))
./venv/lib/python3.12/site-packages/sympy/polys/numberfields/galoisgroups.py:100:        gen = coeff_generators.get(degree, coeff_search(degree, 1))
./venv/lib/python3.12/site-packages/sympy/polys/rings.py:1292:            coeff = poly.get(monom, zero) + coeff
./venv/lib/python3.12/site-packages/sympy/polys/rings.py:1785:        return self.get(expv, self.ring.domain.zero)
./venv/lib/python3.12/site-packages/sympy/codegen/ast.py:206:            return cls.defaults.get(attr, none)
./venv/lib/python3.12/site-packages/sympy/solvers/ode/single.py:306:        return [match.get(w, S.Zero) for w in self.wilds()]
./venv/lib/python3.12/site-packages/sympy/solvers/ode/single.py:427:        diffcls = NthAlgebraic._diffx_stored.get(var, None)
./venv/lib/python3.12/site-packages/sympy/solvers/ode/ode.py:629:                if retdict['best'] == retdict.get(i, None):
./venv/lib/python3.12/site-packages/sympy/solvers/ode/ode.py:1244:        if not order.get(func, False):
./venv/lib/python3.12/site-packages/sympy/solvers/solvers.py:91:    >>> assert [d.get(i, i) for i in s] == syms
./venv/lib/python3.12/site-packages/sympy/solvers/solvers.py:112:    return new_f, [swap_sym.get(i, i) for i in orig], restore
./venv/lib/python3.12/site-packages/sympy/solvers/solvers.py:836:        default = flags.setdefault(k, bool(flags.get(k, default)))
./venv/lib/python3.12/site-packages/sympy/solvers/solvers.py:1180:    tuple_format = lambda s: [tuple([i.get(x, x) for x in symbols]) for i in s]
./venv/lib/python3.12/site-packages/sympy/solvers/solvers.py:1221:        symbols = [swap_sym.get(k, k) for k in symbols]
./venv/lib/python3.12/site-packages/sympy/solvers/solvers.py:1223:            solution[i] = {swap_sym.get(k, k): v.subs(swap_sym)
./venv/lib/python3.12/site-packages/sympy/solvers/solvers.py:1290:    return k, {tuple([s.get(ki, ki) for ki in k]) for s in solution}
./venv/lib/python3.12/site-packages/sympy/solvers/solveset.py:1150:    f_p, f_q, f_r = [pattern_match.get(i, S.Zero) for i in (p, q, r)]
./venv/lib/python3.12/site-packages/sympy/solvers/solveset.py:3116:            sol = FiniteSet(Tuple(*(sol.get(sym, sym) for sym in symbols)))
./venv/lib/python3.12/site-packages/sympy/solvers/solveset.py:3161:    sol = FiniteSet(Tuple(*(sol.get(sym, sym) for sym in symbols)))
./venv/lib/python3.12/site-packages/sympy/solvers/simplex.py:664:        i = univariate.get(x, True)
./venv/lib/python3.12/site-packages/sympy/solvers/tests/test_solvers.py:1521:        tuple([a.get(i, i) for i in v]) for a in ans]
./venv/lib/python3.12/site-packages/joblib/test/test_memory_async.py:169:        counter[x] = counter.get(x, 0) + 1
./venv/lib/python3.12/site-packages/joblib/test/test_parallel.py:2143:    state = status.get(pid, None)
./venv/lib/python3.12/site-packages/joblib/test/test_memory.py:1516:        counter[x] = counter.get(x, 0) + 1
./venv/lib/python3.12/site-packages/joblib/_dask.py:287:                f = self.data_futures.get(arg_id, None)
./venv/lib/python3.12/site-packages/joblib/externals/cloudpickle/cloudpickle.py:294:    module = sys.modules.get(module_name, None)
./venv/lib/python3.12/site-packages/joblib/_parallel_backends.py:238:                var_value = os.environ.get(var, default_n_threads)
./venv/lib64/python3.12/site-packages/anyio/lowlevel.py:174:        token = RunvarToken(self, current_vars.get(self, RunVar.NO_VALUE_SET))
./venv/lib64/python3.12/site-packages/fsspec/generic.py:35:        fs, _ = url_to_fs(url, **storage_options.get(protocol, {}))
./venv/lib64/python3.12/site-packages/fsspec/mapping.py:115:            key: out[k2] if on_error == "raise" else out.get(k2, KeyError(k2))
./venv/lib64/python3.12/site-packages/fsspec/implementations/github.py:235:        r = requests.get(url, timeout=self.timeout, **self.kw)
./venv/lib64/python3.12/site-packages/fsspec/implementations/github.py:301:            r = requests.get(url, timeout=self.timeout, **self.kw)
./venv/lib64/python3.12/site-packages/fsspec/implementations/gist.py:90:        r = requests.get(url, timeout=self.timeout, **self.kw)
./venv/lib64/python3.12/site-packages/fsspec/implementations/gist.py:215:        r = requests.get(raw_url, timeout=self.timeout, **self.kw)
./venv/lib64/python3.12/site-packages/fsspec/implementations/cached.py:586:            self.fs.get(downpath, downfn)
./venv/lib64/python3.12/site-packages/fsspec/implementations/cached.py:670:            self.fs.get(getpaths, storepaths)
./venv/lib64/python3.12/site-packages/fsspec/implementations/cached.py:898:        self.fs.get(rpaths, lpaths)
./venv/lib64/python3.12/site-packages/fsspec/implementations/http.py:827:    r = await session.get(url, headers=headers, **kwargs)
./venv/lib64/python3.12/site-packages/fsspec/implementations/http.py:856:        r = await session.get(url, allow_redirects=ar, **kwargs)
./venv/lib64/python3.12/site-packages/fsspec/implementations/http_sync.py:874:    r = session.get(url, headers=headers, **kwargs)
./venv/lib64/python3.12/site-packages/fsspec/implementations/http_sync.py:897:        r = session.get(url, allow_redirects=ar, **kwargs)
./venv/lib64/python3.12/site-packages/fsspec/implementations/ftp.py:179:        files = self.dircache.get(path, out)
./venv/lib64/python3.12/site-packages/fsspec/implementations/reference.py:307:        maybe = self._items.get((field, record), {}).get(ri, False)
./venv/lib64/python3.12/site-packages/fsspec/implementations/reference.py:410:            self.zmetadata[key] = {**self.zmetadata.get(key, {}), **new_value}
./venv/lib64/python3.12/site-packages/fsspec/tests/abstract/get.py:137:            fs.get(s, t)
./venv/lib64/python3.12/site-packages/fsspec/tests/abstract/get.py:141:            fs.get(s, t, recursive=True)
./venv/lib64/python3.12/site-packages/fsspec/tests/abstract/get.py:170:            fs.get(s, t, recursive=True, maxdepth=1)
./venv/lib64/python3.12/site-packages/fsspec/tests/abstract/get.py:217:            fs.get(s, t)
./venv/lib64/python3.12/site-packages/fsspec/tests/abstract/get.py:221:            fs.get(s, t, recursive=True)
./venv/lib64/python3.12/site-packages/fsspec/tests/abstract/get.py:235:            fs.get(s, t, recursive=True, maxdepth=1)
./venv/lib64/python3.12/site-packages/fsspec/tests/abstract/get.py:452:            fs.get(source_files, t)
./venv/lib64/python3.12/site-packages/fsspec/tests/abstract/get.py:488:        fs.get(source_files, local_join(target, "newdir") + "/")  # Note trailing slash
./venv/lib64/python3.12/site-packages/fsspec/tests/abstract/get.py:509:            fs.get(src, target, recursive=True)
./venv/lib64/python3.12/site-packages/fsspec/spec.py:1806:        return self.get(rpath, lpath, recursive=recursive, **kwargs)
./venv/lib64/python3.12/site-packages/fsspec/dircache.py:58:            if self._times.get(item, 0) - time.time() < -self.listings_expiry_time:
./venv/lib64/python3.12/site-packages/packaging/version.py:705:        letter = _LETTER_NORMALIZATION.get(letter, letter)
./venv/lib64/python3.12/site-packages/packaging/tags.py:581:    archs = {"armv8l": ["armv8l", "armv7l"]}.get(arch, [arch])
./venv/lib64/python3.12/site-packages/starlette/config.py:92:        return self.get(key, cast, default)
./venv/lib64/python3.12/site-packages/torch/_higher_order_ops/effects.py:227:    # Get a token. We can't do `tokens.get(op, torch.tensor([]))` because
./venv/lib64/python3.12/site-packages/torch/_higher_order_ops/triton_kernel_wrap.py:297:                tma_descriptor_metadata.get(name, None)
./venv/lib64/python3.12/site-packages/torch/_guards.py:739:        return self.dynamo_installed_submodules.get(fn_id, [])
./venv/lib64/python3.12/site-packages/torch/_guards.py:745:        return self.autograd_cache.get(identifier, None)
./venv/lib64/python3.12/site-packages/torch/_guards.py:751:        return self.proxy_dispatch_cache.get(identifier, None)
./venv/lib64/python3.12/site-packages/torch/_guards.py:770:        return self.lazy_bwd_cache[identifier].get(tangent_metadata, (None, None))
./venv/lib64/python3.12/site-packages/torch/_guards.py:774:        if prev_effects := self.effects_cache.get(identifier, None):
./venv/lib64/python3.12/site-packages/torch/_guards.py:785:        return self.effects_cache.get(identifier, None)
./venv/lib64/python3.12/site-packages/torch/_functorch/partitioners.py:658:        position_to_quant.get(i, node) for i, node in enumerate(fwd_outputs)
./venv/lib64/python3.12/site-packages/torch/_functorch/functional_call.py:137:            v = all_keys_counter.get(k, 0)
./venv/lib64/python3.12/site-packages/torch/_functorch/_activation_checkpointing/remat_using_tags_for_fwd_loss_bwd_graph_pass.py:94:        return recomputed_nodes.get(x, env[x])
./venv/lib64/python3.12/site-packages/torch/_functorch/_activation_offloading/activation_offloading.py:145:        0, tuple(node_to_offload.get(node, node) for node in fwd_outputs)
./venv/lib64/python3.12/site-packages/torch/_functorch/_aot_autograd/frontend_utils.py:306:                old_module_attrs = snapshot.get(module_name, {})
./venv/lib64/python3.12/site-packages/torch/_functorch/_aot_autograd/frontend_utils.py:307:                new_module_attrs = new_attrs.get(module_name, {})
./venv/lib64/python3.12/site-packages/torch/_functorch/_aot_autograd/graph_capture_wrappers.py:555:    original_val = fx_traceback.current_meta.get(meta_key, None)
./venv/lib64/python3.12/site-packages/torch/_lazy/device_context.py:21:        devctx = DeviceContext._CONTEXTS.get(device, None)
./venv/lib64/python3.12/site-packages/torch/_lazy/extract_compiled_graph.py:47:            arg_idx = self.tensor_id_to_arg_idx.get(tensor_id, None)
./venv/lib64/python3.12/site-packages/torch/multiprocessing/reductions.py:78:            return dict.get(self, key)
./venv/lib64/python3.12/site-packages/torch/multiprocessing/spawn.py:244:        and os.environ.get(ENV_VAR_PARALLEL_START, "0") == "1"
./venv/lib64/python3.12/site-packages/torch/_export/passes/constant_folding.py:188:            for to_delete in self.user_to_last_uses.get(node, []):
./venv/lib64/python3.12/site-packages/torch/_export/verifier.py:530:        return _VerifierMeta._registry.get(dialect, Verifier)
./venv/lib64/python3.12/site-packages/torch/sparse/_triton_ops.py:703:        }.get(N, 16)
./venv/lib64/python3.12/site-packages/torch/sparse/_triton_ops.py:714:            num_warps = {16: 1, 32: 1, 64: 2}.get(Ms, 4)
./venv/lib64/python3.12/site-packages/torch/sparse/_triton_ops.py:716:            num_warps = {16: 1, 32: 1, 64: 2}.get(Ms, 4)
./venv/lib64/python3.12/site-packages/torch/sparse/_triton_ops.py:718:            num_warps = {16: 1, 32: 4}.get(Ms, 4)
./venv/lib64/python3.12/site-packages/torch/sparse/_triton_ops.py:720:            num_warps = {16: 1, 32: 2}.get(Ms, 4)
./venv/lib64/python3.12/site-packages/torch/_prims_common/__init__.py:1459:    return _computation_dtype_map.get(dtype, dtype)
./venv/lib64/python3.12/site-packages/torch/_prims_common/__init__.py:1474:        return _cpu_acc_type_map.get(dtype, dtype)
./venv/lib64/python3.12/site-packages/torch/ao/pruning/_experimental/data_sparsifier/lightning/callbacks/_data_sparstity_utils.py:28:                name=valid_name, data=parameter, **config.get(valid_name, {})
./venv/lib64/python3.12/site-packages/torch/ao/pruning/_experimental/data_sparsifier/base_data_sparsifier.py:189:            config_name = data_groups.get(name, None)
./venv/lib64/python3.12/site-packages/torch/ao/pruning/_experimental/data_sparsifier/base_data_sparsifier.py:197:            data = container_state_dict.get(name, None)
./venv/lib64/python3.12/site-packages/torch/ao/pruning/_experimental/data_scheduler/base_data_scheduler.py:46:            name: config.get(schedule_param, None)
./venv/lib64/python3.12/site-packages/torch/ao/quantization/quantize.py:104:    module_qconfig = qconfig_dict.get(prefix, module_qconfig)
./venv/lib64/python3.12/site-packages/torch/ao/quantization/pt2e/_numeric_debugger.py:50:            unique_id, node.meta.get(CUSTOM_KEY, {}).get(NUMERIC_DEBUG_HANDLE_KEY, 0)
./venv/lib64/python3.12/site-packages/torch/ao/quantization/pt2e/qat_utils.py:621:            return original_to_replacement_node.get(_node, _node)
./venv/lib64/python3.12/site-packages/torch/ao/quantization/pt2e/qat_utils.py:629:                original_to_replacement_node.get(src, src),
./venv/lib64/python3.12/site-packages/torch/ao/quantization/pt2e/qat_utils.py:630:                original_to_replacement_node.get(dest, dest),
./venv/lib64/python3.12/site-packages/torch/ao/quantization/backend_config/backend_config.py:416:        conf = cls(backend_config_dict.get(NAME_DICT_KEY, ""))
./venv/lib64/python3.12/site-packages/torch/ao/quantization/backend_config/backend_config.py:417:        for d in backend_config_dict.get(CONFIGS_DICT_KEY, []):
./venv/lib64/python3.12/site-packages/torch/ao/quantization/backend_config/backend_config.py:673:        for d in backend_pattern_config_dict.get(DTYPE_CONFIGS_DICT_KEY, []):
./venv/lib64/python3.12/site-packages/torch/ao/quantization/backend_config/backend_config.py:700:            backend_pattern_config_dict.get(INPUT_TYPE_TO_INDEX_DICT_KEY, {})
./venv/lib64/python3.12/site-packages/torch/ao/quantization/utils.py:270:    class_mapping = custom_module_class_mapping.get(quant_type, {})
./venv/lib64/python3.12/site-packages/torch/ao/quantization/fx/fuse.py:101:            node_subpattern = node_to_subpattern.get(node, None)
./venv/lib64/python3.12/site-packages/torch/ao/quantization/fx/utils.py:143:        quant_mode_custom_module_config = custom_module_mapping.get(quant_mode, {})
./venv/lib64/python3.12/site-packages/torch/ao/quantization/fx/utils.py:429:    return NON_OBSERVABLE_ARG_DICT.get(info, EMPTY_ARG_DICT)
./venv/lib64/python3.12/site-packages/torch/ao/quantization/fx/custom_config.py:255:        ) in prepare_custom_config_dict.get(STANDALONE_MODULE_NAME_DICT_KEY, []):
./venv/lib64/python3.12/site-packages/torch/ao/quantization/fx/custom_config.py:278:        ) in prepare_custom_config_dict.get(STANDALONE_MODULE_CLASS_DICT_KEY, []):
./venv/lib64/python3.12/site-packages/torch/ao/quantization/fx/custom_config.py:304:            prepare_custom_config_dict.get(NON_TRACEABLE_MODULE_NAME_DICT_KEY, [])
./venv/lib64/python3.12/site-packages/torch/ao/quantization/fx/custom_config.py:307:            prepare_custom_config_dict.get(NON_TRACEABLE_MODULE_CLASS_DICT_KEY, [])
./venv/lib64/python3.12/site-packages/torch/ao/quantization/fx/custom_config.py:310:            prepare_custom_config_dict.get(INPUT_QUANTIZED_INDEXES_DICT_KEY, [])
./venv/lib64/python3.12/site-packages/torch/ao/quantization/fx/custom_config.py:313:            prepare_custom_config_dict.get(OUTPUT_QUANTIZED_INDEXES_DICT_KEY, [])
./venv/lib64/python3.12/site-packages/torch/ao/quantization/fx/custom_config.py:316:            prepare_custom_config_dict.get(PRESERVED_ATTRIBUTES_DICT_KEY, [])
./venv/lib64/python3.12/site-packages/torch/ao/quantization/fx/custom_config.py:447:            convert_custom_config_dict.get(PRESERVED_ATTRIBUTES_DICT_KEY, [])
./venv/lib64/python3.12/site-packages/torch/ao/quantization/fx/custom_config.py:509:            fuse_custom_config_dict.get(PRESERVED_ATTRIBUTES_DICT_KEY, [])
./venv/lib64/python3.12/site-packages/torch/ao/quantization/fx/prepare.py:410:    dtype_configs: list[DTypeConfig] = pattern_to_dtype_configs.get(pattern, [])
./venv/lib64/python3.12/site-packages/torch/ao/quantization/fx/qconfig_mapping_utils.py:317:    return qconfig_mapping.object_type_qconfigs.get(object_type, fallback_qconfig)
./venv/lib64/python3.12/site-packages/torch/ao/quantization/qconfig_mapping.py:371:        for object_type, qconfig in qconfig_dict.get(_OBJECT_TYPE_DICT_KEY, []):
./venv/lib64/python3.12/site-packages/torch/ao/quantization/qconfig_mapping.py:377:        for module_name, qconfig in qconfig_dict.get(_MODULE_NAME_DICT_KEY, []):
./venv/lib64/python3.12/site-packages/torch/ao/quantization/quantizer/x86_inductor_quantizer.py:265:    quantization_annotation = node.meta.get(QUANT_ANNOTATION_KEY, None)
./venv/lib64/python3.12/site-packages/torch/ao/quantization/fuser_method_mappings.py:245:    fuser_method = all_mappings.get(op_list, None)
./venv/lib64/python3.12/site-packages/torch/ao/quantization/quantization_mappings.py:254:    static_quant_module_class = all_mappings.get(float_module_class, None)
./venv/lib64/python3.12/site-packages/torch/ao/quantization/quantization_mappings.py:275:    dynamic_quant_module_class = all_mappings.get(float_module_class, None)
./venv/lib64/python3.12/site-packages/torch/_prims/context.py:131:        func = mapping.get(orig_func, None)
./venv/lib64/python3.12/site-packages/torch/_prims/context.py:140:            func = torch._decomp.decomposition_table.get(orig_func, None)
./venv/lib64/python3.12/site-packages/torch/_prims/context.py:146:                func = torch._decomp.decomposition_table.get(default, None)
./venv/lib64/python3.12/site-packages/torch/package/package_exporter.py:674:                        field = memo.get(arg, None)
./venv/lib64/python3.12/site-packages/torch/package/package_importer.py:515:        module = self.modules.get(name, _NEEDS_LOADING)
./venv/lib64/python3.12/site-packages/torch/package/package_importer.py:585:                            and self.modules.get(from_name, _NEEDS_LOADING) is not None
./venv/lib64/python3.12/site-packages/torch/package/package_importer.py:647:            node = cur.children.get(atom, None)
./venv/lib64/python3.12/site-packages/torch/package/_digraph.py:151:                idx = self._node_order.get(candidate, None)
./venv/lib64/python3.12/site-packages/torch/fx/passes/reinplace.py:99:                maybe_base_of_view = self.multi_output_view_nodes.get(list_arg, None)
./venv/lib64/python3.12/site-packages/torch/fx/passes/graph_transform_observer.py:190:            new_node = self.name_to_node.get(new, None)
./venv/lib64/python3.12/site-packages/torch/fx/passes/splitter_base.py:194:        for idx in self.node_events.get(node_name, []):
./venv/lib64/python3.12/site-packages/torch/fx/passes/splitter_base.py:209:            for idx in self.node_events.get(name, []):
./venv/lib64/python3.12/site-packages/torch/fx/passes/splitter_base.py:264:                os.environ.get(ENV_FX_NET_ACC_SPLITTER_TRACKER_TRACKED_NODES, "").split(
./venv/lib64/python3.12/site-packages/torch/fx/_symbolic_trace.py:560:            num_calls = self.num_calls.get(module_qualified_name, 0)
./venv/lib64/python3.12/site-packages/torch/fx/_symbolic_trace.py:977:            type_expr=fn_for_analysis.__annotations__.get(name, None),
./venv/lib64/python3.12/site-packages/torch/fx/experimental/symbolic_shapes.py:533:    return {shape_env.unbacked_renamings.get(k, k): v for k, v in bindings.items()}
./venv/lib64/python3.12/site-packages/torch/fx/experimental/symbolic_shapes.py:1295:                source=shape_env.var_to_sources.get(s, [None])[0],  # type: ignore[union-attr]
./venv/lib64/python3.12/site-packages/torch/fx/experimental/symbolic_shapes.py:2802:        val = self._print_cache.get(expr, None)
./venv/lib64/python3.12/site-packages/torch/fx/experimental/symbolic_shapes.py:4344:        return self.fx_node_cache.get(node_key, None), fresh
./venv/lib64/python3.12/site-packages/torch/fx/experimental/symbolic_shapes.py:4473:                hint_overrides.get(i, val),
./venv/lib64/python3.12/site-packages/torch/fx/experimental/symbolic_shapes.py:4674:                hint=hint_overrides.get(i, hint),
./venv/lib64/python3.12/site-packages/torch/fx/experimental/symbolic_shapes.py:5286:        return self.source_name_to_debug_name.get(src_name, src_name)
./venv/lib64/python3.12/site-packages/torch/fx/experimental/symbolic_shapes.py:5603:                            x: self.var_to_range.get(x, None) for x in s.free_symbols
./venv/lib64/python3.12/site-packages/torch/fx/experimental/symbolic_shapes.py:5656:                    user_stack = self.specialization_stacks.get(source, None)
./venv/lib64/python3.12/site-packages/torch/fx/experimental/symbolic_shapes.py:5954:        for ra in self.deferred_runtime_asserts.get(None, []):
./venv/lib64/python3.12/site-packages/torch/fx/experimental/symbolic_shapes.py:6270:        var_to_range = {x: self.var_to_range.get(x, None) for x in expr.free_symbols}
./venv/lib64/python3.12/site-packages/torch/fx/experimental/symbolic_shapes.py:6303:                for r in self.deferred_runtime_asserts.get(s, ())
./venv/lib64/python3.12/site-packages/torch/fx/experimental/symbolic_shapes.py:6753:        if tgt == self.replacements.get(a, None):
./venv/lib64/python3.12/site-packages/torch/fx/experimental/symbolic_shapes.py:6883:                    "sources": [s.name for s in self.var_to_sources.get(a, [])],
./venv/lib64/python3.12/site-packages/torch/fx/experimental/symbolic_shapes.py:6895:            for source in self.var_to_sources.get(a, []):
./venv/lib64/python3.12/site-packages/torch/fx/experimental/symbolic_shapes.py:7860:            if isinstance(self.var_to_val.get(symbol, None), SingletonInt):
./venv/lib64/python3.12/site-packages/torch/fx/experimental/symbolic_shapes.py:7922:        old_vr = self.var_to_range.get(s, ValueRanges.unknown())
./venv/lib64/python3.12/site-packages/torch/fx/experimental/unification/multipledispatch/utils.py:56:        for m in edges.get(n, ()):
./venv/lib64/python3.12/site-packages/torch/fx/experimental/unification/multipledispatch/utils.py:61:    if any(incoming_edges.get(v, None) for v in edges):
./venv/lib64/python3.12/site-packages/torch/fx/experimental/unification/multipledispatch/utils.py:79:            result[val] = result.get(val, ()) + (key,)
./venv/lib64/python3.12/site-packages/torch/fx/experimental/unification/utils.py:58:        for m in edges.get(n, ()):
./venv/lib64/python3.12/site-packages/torch/fx/experimental/unification/utils.py:81:            result[val] = result.get(val, ()) + (key,)
./venv/lib64/python3.12/site-packages/torch/fx/experimental/proxy_tensor.py:1576:        self.tracer.torch_fn_counts[func] = self.tracer.torch_fn_counts.get(func, 0) + 1
./venv/lib64/python3.12/site-packages/torch/fx/experimental/meta_tracer.py:203:                meta_target = manual_meta_overrides.get(target, target)
./venv/lib64/python3.12/site-packages/torch/fx/interpreter.py:231:                for to_delete in self.user_to_last_uses.get(node, []):
./venv/lib64/python3.12/site-packages/torch/fx/graph.py:190:            num = self._base_count.get(candidate, 0)
./venv/lib64/python3.12/site-packages/torch/fx/graph.py:191:            if _illegal_names.get(candidate, obj) is not obj:
./venv/lib64/python3.12/site-packages/torch/fx/graph.py:517:                    origin_type = _origin_type_map.get(origin_type, origin_type)
./venv/lib64/python3.12/site-packages/torch/fx/graph.py:615:            nodes_to_delete = user_to_last_uses.get(user, [])
./venv/lib64/python3.12/site-packages/torch/fx/subgraph_rewriter.py:353:                val_map[rn] = match_changed_node.get(gn, gn)
./venv/lib64/python3.12/site-packages/torch/profiler/_memory_profiler.py:388:            self._values[key] = max(self._values.get(key, 0), num_bytes)
./venv/lib64/python3.12/site-packages/torch/profiler/_memory_profiler.py:536:                expected = tensor_versions.get(key, 0)
./venv/lib64/python3.12/site-packages/torch/profiler/_memory_profiler.py:540:                prior_version = tensor_versions.get(key, version)
./venv/lib64/python3.12/site-packages/torch/profiler/_memory_profiler.py:607:        prior_version = self._active_version.get(key, None)
./venv/lib64/python3.12/site-packages/torch/profiler/_memory_profiler.py:654:            or element.by_key.get(key, None)
./venv/lib64/python3.12/site-packages/torch/profiler/_memory_profiler.py:757:            (key, version): self._categories.get(key, version)
./venv/lib64/python3.12/site-packages/torch/profiler/_memory_profiler.py:779:                    if self._categories.get(key, version)
./venv/lib64/python3.12/site-packages/torch/profiler/_memory_profiler.py:980:                    if version == 0 or self._categories.get(key, version - 1) in prior:
./venv/lib64/python3.12/site-packages/torch/profiler/_memory_profiler.py:1012:                self.categories.get(key, version)
./venv/lib64/python3.12/site-packages/torch/profiler/_memory_profiler.py:1079:                self.categories.get(key, version)
./venv/lib64/python3.12/site-packages/torch/optim/radam.py:81:                p_state = self.state.get(p, [])
./venv/lib64/python3.12/site-packages/torch/optim/_adafactor.py:66:                p_state = self.state.get(p, [])
./venv/lib64/python3.12/site-packages/torch/optim/nadam.py:85:                p_state = self.state.get(p, [])
./venv/lib64/python3.12/site-packages/torch/optim/rmsprop.py:82:                p_state = self.state.get(p, [])
./venv/lib64/python3.12/site-packages/torch/optim/asgd.py:71:                p_state = self.state.get(p, [])
./venv/lib64/python3.12/site-packages/torch/optim/adam.py:126:                p_state = self.state.get(p, [])
./venv/lib64/python3.12/site-packages/torch/optim/adadelta.py:73:                p_state = self.state.get(p, [])
./venv/lib64/python3.12/site-packages/torch/optim/rprop.py:69:                p_state = self.state.get(p, [])
./venv/lib64/python3.12/site-packages/torch/optim/adamax.py:76:                p_state = self.state.get(p, [])
./venv/lib64/python3.12/site-packages/torch/_utils.py:136:            return map_location.get(device, device)
./venv/lib64/python3.12/site-packages/torch/_utils.py:1060:    if (module := sys.modules.get(module_name, None)) is not None:
./venv/lib64/python3.12/site-packages/torch/export/_draft_export.py:317:            if res := self.expression_created_logs.get(sym_node_id, None):
./venv/lib64/python3.12/site-packages/torch/export/unflatten.py:689:                mod = _get_attr(self, redirected_call_indices.get(fqn, fqn))
./venv/lib64/python3.12/site-packages/torch/export/_unlift.py:47:        return str(_pytree_subclasses_that_lose_info.get(t, t))
./venv/lib64/python3.12/site-packages/torch/export/_unlift.py:329:        return_nodes_to_copy.get(node, node) for node in user_output_nodes
./venv/lib64/python3.12/site-packages/torch/export/_trace.py:492:            targets = remap_table.get(orig_target, [orig_target])
./venv/lib64/python3.12/site-packages/torch/masked/_ops.py:314:            argument_declarations.get(a, f"{a.split('__', 1)[0]}: TBD.").splitlines()
./venv/lib64/python3.12/site-packages/torch/distributed/argparse_util.py:46:        default = os.environ.get(env_name, default)
./venv/lib64/python3.12/site-packages/torch/distributed/argparse_util.py:100:        default = bool(int(os.environ.get(env_name, "1" if default else "0")))
./venv/lib64/python3.12/site-packages/torch/distributed/_tools/sac_estimator.py:373:                        if acm_stats := self._sac_mod_metadata.get(mod_fqn, None):
./venv/lib64/python3.12/site-packages/torch/distributed/_tools/sac_estimator.py:448:            if acm_stats := self._sac_mod_metadata.get(mod_fqn, None):
./venv/lib64/python3.12/site-packages/torch/distributed/_tools/mod_tracker.py:96:        return self._known_modules.get(mod, None)
./venv/lib64/python3.12/site-packages/torch/distributed/_tools/mem_tracker.py:451:            winfo, _ = self._WINFO.get(st, (None, None))
./venv/lib64/python3.12/site-packages/torch/distributed/_tools/mem_tracker.py:488:            winfo, _ = self._WINFO.get(st, (None, None))
./venv/lib64/python3.12/site-packages/torch/distributed/_tools/mem_tracker.py:513:                        if mod_stats.local_peak.get(dev, 0) < dev_snap[_TOTAL_KEY]:
./venv/lib64/python3.12/site-packages/torch/distributed/_tools/mem_tracker.py:520:            if self._peak_mem.get(dev, 0) < dev_snap[_TOTAL_KEY]:
./venv/lib64/python3.12/site-packages/torch/distributed/_tools/mem_tracker.py:530:            winfo, _ = self._WINFO.get(st, (None, None))
./venv/lib64/python3.12/site-packages/torch/distributed/_tools/mem_tracker.py:599:                self._param_to_grad_hook_handles.get(param, None) is None
./venv/lib64/python3.12/site-packages/torch/distributed/_tools/mem_tracker.py:627:                winfo, _ = self._WINFO.get(st, (None, None))
./venv/lib64/python3.12/site-packages/torch/distributed/tensor/_ops/_common_rules.py:108:            pending_sums_counter[sum_dim] = pending_sums_counter.get(sum_dim, 0) + 1
./venv/lib64/python3.12/site-packages/torch/distributed/distributed_c10d.py:1404:    pg_store = _world.pg_map.get(pg, None)
./venv/lib64/python3.12/site-packages/torch/distributed/distributed_c10d.py:2244:    if _world.pg_map.get(pg, None) is None:
./venv/lib64/python3.12/site-packages/torch/distributed/distributed_c10d.py:2336:    if _world.pg_map.get(pg, None) is None:
./venv/lib64/python3.12/site-packages/torch/distributed/distributed_c10d.py:5711:    for group in _world.tags_to_pg.get(tag, []):
./venv/lib64/python3.12/site-packages/torch/distributed/distributed_c10d.py:5764:    return _world.pg_names.get(pg, "None")
./venv/lib64/python3.12/site-packages/torch/distributed/distributed_c10d.py:6032:    original_backend_config = _world.pg_backend_config.get(target_pg, "")
./venv/lib64/python3.12/site-packages/torch/distributed/_symmetric_memory/_nvshmem_triton.py:168:        kernel = kernel_cache.get(key, None)
./venv/lib64/python3.12/site-packages/torch/distributed/_symmetric_memory/_nvshmem_triton.py:330:            nvshmem.get(dest_tensor, src_tensor, 100, 0)
./venv/lib64/python3.12/site-packages/torch/distributed/__init__.py:97:            counter = _breakpoint_cache.get(key, 0) + 1
./venv/lib64/python3.12/site-packages/torch/distributed/fsdp/_init_utils.py:454:        os.environ.get(_FSDP_USE_FULL_PREC_IN_EVAL, "") == "1"
./venv/lib64/python3.12/site-packages/torch/distributed/fsdp/_optim_utils.py:504:                    state = optim.state.get(param, None)  # type: ignore[call-overload]
./venv/lib64/python3.12/site-packages/torch/distributed/fsdp/_optim_utils.py:1390:                info = object_state.tensors.get(state_name, None)
./venv/lib64/python3.12/site-packages/torch/distributed/fsdp/_optim_utils.py:1412:            local_state = input_states[fqn].get(state_name, None)
./venv/lib64/python3.12/site-packages/torch/distributed/fsdp/_optim_utils.py:1427:                curr_non_tensor_value = gathered_state.get(name, None)
./venv/lib64/python3.12/site-packages/torch/distributed/fsdp/_optim_utils.py:1439:                curr_scalar_tensor_value = gathered_state.get(name, None)
./venv/lib64/python3.12/site-packages/torch/distributed/fsdp/_debug_utils.py:122:        handle = state._fully_sharded_module_to_handle.get(module, None)
./venv/lib64/python3.12/site-packages/torch/distributed/fsdp/_runtime_utils.py:1313:    module_param_handle = state._fully_sharded_module_to_handle.get(module, None)
./venv/lib64/python3.12/site-packages/torch/distributed/fsdp/_runtime_utils.py:1335:    module_param_handle = state._fully_sharded_module_to_handle.get(module, None)
./venv/lib64/python3.12/site-packages/torch/distributed/fsdp/_flat_param.py:537:            os.environ.get(_FSDP_SKIP_WRITEBACK_CHECK, "") == "1"
./venv/lib64/python3.12/site-packages/torch/distributed/fsdp/_flat_param.py:540:            os.environ.get(_FSDP_USE_FULL_PREC_IN_EVAL, "") == "1"
./venv/lib64/python3.12/site-packages/torch/distributed/fsdp/_flat_param.py:542:        self._use_fake_all_gather = os.environ.get(_FSDP_USE_FAKE_ALL_GATHER, "") == "1"
./venv/lib64/python3.12/site-packages/torch/distributed/fsdp/_flat_param.py:543:        self._use_fake_reduce = os.environ.get(_FSDP_USE_FAKE_REDUCE, "") == "1"
./venv/lib64/python3.12/site-packages/torch/distributed/fsdp/_flat_param.py:628:        use_unsafe_setattr = os.environ.get(_FSDP_USE_UNSAFE_SETATTR, "") == "1"
./venv/lib64/python3.12/site-packages/torch/distributed/rpc/api.py:214:        sequence_num = _all_gather_sequence_id.get(concat_names, 0)
./venv/lib64/python3.12/site-packages/torch/distributed/rpc/backend_registry.py:234:            if all_devices.get(target_node, []):
./venv/lib64/python3.12/site-packages/torch/distributed/elastic/multiprocessing/api.py:179:            map[i] = val_or_map.get(i, Std.NONE)
./venv/lib64/python3.12/site-packages/torch/distributed/elastic/timer/api.py:95:        res = q.get(size, timeout=0)
./venv/lib64/python3.12/site-packages/torch/distributed/elastic/timer/api.py:191:        timer_requests = self._request_queue.get(batch_size, self._max_interval)
./venv/lib64/python3.12/site-packages/torch/distributed/elastic/rendezvous/api.py:294:        return self.config.get(key, default)
./venv/lib64/python3.12/site-packages/torch/distributed/elastic/rendezvous/api.py:298:        value = self.get(key, default)
./venv/lib64/python3.12/site-packages/torch/distributed/elastic/rendezvous/api.py:317:        value = self.get(key, default)
./venv/lib64/python3.12/site-packages/torch/distributed/elastic/metrics/api.py:90:    handler = _metrics_map.get(group, _default_metrics_handler)
./venv/lib64/python3.12/site-packages/torch/distributed/elastic/utils/api.py:23:    value = os.environ.get(env_name, None)
./venv/lib64/python3.12/site-packages/torch/distributed/checkpoint/optimizer.py:215:        return super().lookup_tensor(self.translation.get(index, index))
./venv/lib64/python3.12/site-packages/torch/distributed/checkpoint/optimizer.py:316:            alloc_size = layout_specs.get(spec_key, (None, value.size))[1]
./venv/lib64/python3.12/site-packages/torch/distributed/checkpoint/_state_dict_stager.py:293:        y = memo.get(d, _nil)
./venv/lib64/python3.12/site-packages/torch/distributed/rendezvous.py:253:        env_val = os.environ.get(env_var, None)
./venv/lib64/python3.12/site-packages/torch/distributed/pipelining/_IR.py:413:                self.value_remap.get(v, v) for v in kwargs["input_values"]
./venv/lib64/python3.12/site-packages/torch/distributed/pipelining/schedules.py:251:        pipeline_order.get(key, [""] * num_steps) for key in sorted(pipeline_order)
./venv/lib64/python3.12/site-packages/torch/distributed/pipelining/schedules.py:3077:            counters[input_key] = counters.get(input_key, 0) + 1
./venv/lib64/python3.12/site-packages/torch/distributed/pipelining/schedules.py:3078:            counters[weight_key] = counters.get(weight_key, 0) + 1
./venv/lib64/python3.12/site-packages/torch/distributed/pipelining/schedules.py:3090:            forward_mb = counters.get(forward_key, 0)
./venv/lib64/python3.12/site-packages/torch/distributed/pipelining/schedules.py:3091:            backward_mb = counters.get(backward_key, 0)
./venv/lib64/python3.12/site-packages/torch/distributed/pipelining/schedules.py:3114:            mb_index = counters.get(key, 0)
./venv/lib64/python3.12/site-packages/torch/distributed/pipelining/schedules.py:3142:            counters[weight_key] = counters.get(weight_key, 0) + 1
./venv/lib64/python3.12/site-packages/torch/nested/_internal/ops.py:252:    dispatch_func = JAGGED_OPS_TABLE.get(func, None)
./venv/lib64/python3.12/site-packages/torch/_meta_registrations.py:103:    return from_complex.get(dtype, dtype)
./venv/lib64/python3.12/site-packages/torch/_library/triton.py:18:    return triton_ops_to_kernels.get(name, [])
./venv/lib64/python3.12/site-packages/torch/_library/simple_registry.py:32:        res = self._data.get(qualname, None)
./venv/lib64/python3.12/site-packages/torch/_library/simple_registry.py:83:        return self._data.get(torch_dispatch_class, None)
./venv/lib64/python3.12/site-packages/torch/serialization.py:1873:            location = map_location.get(location, location)
./venv/lib64/python3.12/site-packages/torch/serialization.py:2131:            mod_name = load_module_mapping.get(mod_name, mod_name)
./venv/lib64/python3.12/site-packages/torch/_inductor/autoheuristic/autoheuristic.py:161:        return self.collected_feedback.get(choice, None)
./venv/lib64/python3.12/site-packages/torch/_inductor/autoheuristic/autoheuristic.py:308:        return self.choicestr2choice.get(choice, None)
./venv/lib64/python3.12/site-packages/torch/_inductor/runtime/triton_heuristics.py:1202:            asm = launcher.bin.asm.get(asm_type, None)
./venv/lib64/python3.12/site-packages/torch/_inductor/runtime/triton_heuristics.py:1575:                call_args = [repl.get(arg, arg) for arg in call_args]
./venv/lib64/python3.12/site-packages/torch/_inductor/runtime/triton_heuristics.py:1961:                    if compile_meta["signature"].get(x, "constexpr") != "constexpr"
./venv/lib64/python3.12/site-packages/torch/_inductor/runtime/coordinate_descent_tuner.py:28:        return config.kwargs.get(name, int(8 // config.num_warps))
./venv/lib64/python3.12/site-packages/torch/_inductor/runtime/coordinate_descent_tuner.py:30:        return config.kwargs.get(name, None)
./venv/lib64/python3.12/site-packages/torch/_inductor/runtime/caching/implementations.py:142:        if (value := self._memory.get(pickled_key, miss)) is not miss:
./venv/lib64/python3.12/site-packages/torch/_inductor/sizevars.py:613:                s: self.shape_env.var_to_range.get(s, None) for s in out.free_symbols
./venv/lib64/python3.12/site-packages/torch/_inductor/debug.py:1084:                pre_grad_nodes.update(post_to_pre.get(post_node, []))
./venv/lib64/python3.12/site-packages/torch/_inductor/debug.py:1087:                "stack_traces": _inductor_kernel_stack_trace.get(kernel_name, []),
./venv/lib64/python3.12/site-packages/torch/_inductor/loop_body.py:196:        return self.op_counts.get(name, 0) > 0
./venv/lib64/python3.12/site-packages/torch/_inductor/ir.py:6531:                    type_ = self.allarg_properties.get(arg_name, {}).get("type")
./venv/lib64/python3.12/site-packages/torch/_inductor/ir.py:9279:        self.prev_effect_buffer = V.graph.effectful_ops.get(effect_type, None)
./venv/lib64/python3.12/site-packages/torch/_inductor/comms.py:1428:        snodes_allocfree[n].size_free += size_free_delta_update.get(n, 0)
./venv/lib64/python3.12/site-packages/torch/_inductor/comms.py:2208:        resized_to_0_idxes = graph_input_to_resized_to_0_node_idxes.get(graph_input, [])
./venv/lib64/python3.12/site-packages/torch/_inductor/utils.py:3404:    return _triton_type_mapping.get(triton_type_name, triton_type_name)
./venv/lib64/python3.12/site-packages/torch/_inductor/utils.py:3408:    adjusted_type = _torch_triton_mapping.get(dtype, dtype)
./venv/lib64/python3.12/site-packages/torch/_inductor/utils.py:3539:        return self.original_dict.get(key, default)
./venv/lib64/python3.12/site-packages/torch/_inductor/utils.py:3855:        value = config_patches.get(config_name, getattr(config, config_name))
./venv/lib64/python3.12/site-packages/torch/_inductor/utils.py:3866:        value = config_patches.get(config_name, getattr(config, config_name))
./venv/lib64/python3.12/site-packages/torch/_inductor/async_compile.py:217:        return CompiledTritonKernels._cache.get(key, None)
./venv/lib64/python3.12/site-packages/torch/_inductor/constant_folding.py:281:            for to_delete in self.user_to_last_uses.get(node, []):
./venv/lib64/python3.12/site-packages/torch/_inductor/autotune_process.py:542:            assert os.environ.get(CUDA_VISIBLE_DEVICES, None) == str(self.device)
./venv/lib64/python3.12/site-packages/torch/_inductor/graph.py:1988:            V.fake_mode.shape_env.unbacked_renamings.get(s, s)
./venv/lib64/python3.12/site-packages/torch/_inductor/augmented_graph_helper.py:151:                updated_dep = erased_merge_sets.get(extra_dep, extra_dep)
./venv/lib64/python3.12/site-packages/torch/_inductor/augmented_graph_helper.py:159:                updated_use = erased_merge_sets.get(extra_use, extra_use)
./venv/lib64/python3.12/site-packages/torch/_inductor/fx_passes/ddp_fusion.py:314:            node_indices.get(node, last_wait_node_idx), last_wait_node_idx
./venv/lib64/python3.12/site-packages/torch/_inductor/fx_passes/reinplace.py:285:        node_to_view_base[node] = node_to_view_base.get(inp, inp)  # type: ignore[arg-type, assignment]
./venv/lib64/python3.12/site-packages/torch/_inductor/fx_passes/reinplace.py:311:            inp_base = node_to_view_base.get(inp, inp)  # type: ignore[arg-type]
./venv/lib64/python3.12/site-packages/torch/_inductor/fx_passes/reinplace.py:312:            src_base = node_to_view_base.get(src_inp, src_inp)  # type: ignore[arg-type]
./venv/lib64/python3.12/site-packages/torch/_inductor/fx_passes/control_dependencies.py:111:        updated_dep_nodes = [replacements.get(dep, dep) for dep in dep_nodes]
./venv/lib64/python3.12/site-packages/torch/_inductor/fx_passes/bucketing.py:94:                n.meta[key] = bucket_nodes[0].meta.get(key, default)
./venv/lib64/python3.12/site-packages/torch/_inductor/fx_passes/bucketing.py:102:                            node.meta.get(key, default)
./venv/lib64/python3.12/site-packages/torch/_inductor/fx_passes/bucketing.py:104:                            if node.meta.get(key, default)
./venv/lib64/python3.12/site-packages/torch/_inductor/fx_passes/bucketing.py:110:                        node.meta.get(key, default)
./venv/lib64/python3.12/site-packages/torch/_inductor/fx_passes/bucketing.py:112:                        if node.meta.get(key, default)
./venv/lib64/python3.12/site-packages/torch/_inductor/fx_passes/pre_grad.py:82:    return {p: dict(counters["inductor"]).get(p, 0) for p in pass_to_compare}
./venv/lib64/python3.12/site-packages/torch/_inductor/fx_passes/pre_grad.py:87:        if count != dict(inductor_dict).get(pass_name, 0):
./venv/lib64/python3.12/site-packages/torch/_inductor/fx_passes/b2b_gemm.py:478:            args, kwargs = tree_map(lambda x: env.get(x, x), (node.args, node.kwargs))
./venv/lib64/python3.12/site-packages/torch/_inductor/fx_passes/b2b_gemm.py:692:            new_node = new_graph.node_copy(node, lambda x: node_remapping.get(x, x))
./venv/lib64/python3.12/site-packages/torch/_inductor/fuzzer.py:440:        return self._vals.get(combo, None)
./venv/lib64/python3.12/site-packages/torch/_inductor/wrapper_benchmark.py:297:                f"{per_category_wall_time.get(category, 0.0) / wall_time_ms * 100:.2f}%"
./venv/lib64/python3.12/site-packages/torch/_inductor/codecache.py:309:                if choice_hash in cache.get(op, {}).get(cache_key, {}).get(
./venv/lib64/python3.12/site-packages/torch/_inductor/codecache.py:1726:        return cls.cache.get(key, None)
./venv/lib64/python3.12/site-packages/torch/_inductor/codecache.py:4162:                    binary_remote_cache.get(output_path, error_path)
./venv/lib64/python3.12/site-packages/torch/_inductor/select_algorithm.py:1653:        entry = self._cache.get(cache_key, None)
./venv/lib64/python3.12/site-packages/torch/_inductor/compiler_bisector.py:86:    return os.environ.get(env_str, None)
./venv/lib64/python3.12/site-packages/torch/_inductor/compiler_bisector.py:471:                        f"Debug info: {call_counter_debug_info.get(low, 'not found')}"
./venv/lib64/python3.12/site-packages/torch/_inductor/scheduler.py:639:        used_buffers = OrderedSet(mutation_real_name.get(k, k) for k in used_buffers)
./venv/lib64/python3.12/site-packages/torch/_inductor/scheduler.py:3250:                        self.mutation_real_name.get(alt_name, alt_name)
./venv/lib64/python3.12/site-packages/torch/_inductor/scheduler.py:3491:                c = children.get(dep, [])
./venv/lib64/python3.12/site-packages/torch/_inductor/scheduler.py:3499:                for user in children.get(n, []):
./venv/lib64/python3.12/site-packages/torch/_inductor/scheduler.py:5696:            buf = self.name_to_buf.get(buf_name, None)
./venv/lib64/python3.12/site-packages/torch/_inductor/scheduler.py:5705:                if real_name := self.mutation_real_name.get(buf_name, None):
./venv/lib64/python3.12/site-packages/torch/_inductor/scheduler.py:5742:                self.mutation_real_name.get(name, name)
./venv/lib64/python3.12/site-packages/torch/_inductor/scheduler.py:5784:                self.mutation_real_name.get(name, name)
./venv/lib64/python3.12/site-packages/torch/_inductor/lookup_table/choices.py:245:                config_list = lookup_table.get(key, [])
./venv/lib64/python3.12/site-packages/torch/_inductor/codegen/pallas.py:1527:                    param_name = buf_to_param.get(buf_name, buf_name)
./venv/lib64/python3.12/site-packages/torch/_inductor/codegen/pallas.py:1651:                    if aliasable_flags.get(name, False):
./venv/lib64/python3.12/site-packages/torch/_inductor/codegen/pallas.py:1787:            if aliasable.get(p, False)
./venv/lib64/python3.12/site-packages/torch/_inductor/codegen/cpp_wrapper_gpu.py:223:            if params.get(name, None) is not None
./venv/lib64/python3.12/site-packages/torch/_inductor/codegen/triton.py:2440:                        self.kernel.tma_min_block_sizes.get(block_type_str, 1),
./venv/lib64/python3.12/site-packages/torch/_inductor/codegen/triton.py:5638:        pid = entry.pid_cache.get(key, key)
./venv/lib64/python3.12/site-packages/torch/_inductor/codegen/rocm/ck_universal_gemm_template.py:395:        dimension_padding = padding_lookup.get(dimension, {})
./venv/lib64/python3.12/site-packages/torch/_inductor/codegen/rocm/ck_universal_gemm_template.py:398:        return dimension_padding.get(gemm_specialization, False)
./venv/lib64/python3.12/site-packages/torch/_inductor/codegen/common.py:1497:        result: Union[str, RemovedArg] = odict.get(name, REMOVED)
./venv/lib64/python3.12/site-packages/torch/_inductor/codegen/common.py:1532:            name = V.graph.scheduler.mutation_real_name.get(name, name)
./venv/lib64/python3.12/site-packages/torch/_inductor/codegen/common.py:1544:            name = V.graph.scheduler.mutation_real_name.get(name, name)
./venv/lib64/python3.12/site-packages/torch/_inductor/codegen/common.py:1682:        inplaced = self.inplace_buffers.get(name, None)
./venv/lib64/python3.12/site-packages/torch/_inductor/codegen/common.py:1685:        output_name = self.output_buffers.get(name, None)
./venv/lib64/python3.12/site-packages/torch/_inductor/codegen/common.py:1688:        return self.input_buffers.get(name, None)
./venv/lib64/python3.12/site-packages/torch/_inductor/codegen/common.py:1818:            self.output_buffers.get(name, REMOVED), RemovedArg
./venv/lib64/python3.12/site-packages/torch/_inductor/codegen/common.py:1819:        ) and isinstance(self.inplace_buffers.get(name, REMOVED), RemovedArg)
./venv/lib64/python3.12/site-packages/torch/_inductor/codegen/common.py:2676:            return self.kernel.node_to_bounds.get(fx_node, ValueRanges.unknown())
./venv/lib64/python3.12/site-packages/torch/_inductor/codegen/cuda/cutlass_lib_extensions/evt_extensions.py:79:            return self.buf_renames.get(name, name)
./venv/lib64/python3.12/site-packages/torch/_inductor/codegen/simd.py:2752:                    split_scores.append(coalesce_analysis.coalesced_by_var.get(v, 0))
./venv/lib64/python3.12/site-packages/torch/_inductor/codegen/simd.py:2761:                split_scores.append(coalesce_analysis.coalesced_by_var.get(v, 0))
./venv/lib64/python3.12/site-packages/torch/_inductor/codegen/wrapper.py:402:        return bool(self.reuse_pool.get(key, None))
./venv/lib64/python3.12/site-packages/torch/_inductor/codegen/wrapper.py:2233:                    V.graph.sizevars.var_to_val.get(value, None), SingletonInt
./venv/lib64/python3.12/site-packages/torch/_inductor/codegen/cutedsl/cutedsl_kernel.py:316:        output = self.args.output_buffers.get(buf_name, None)
./venv/lib64/python3.12/site-packages/torch/_inductor/codegen/halide.py:624:        return self.index_str([replacements.get(n, n) for n in self.used_dims])
./venv/lib64/python3.12/site-packages/torch/_logging/_internal.py:505:                    log_registry.log_alias_to_log_qnames.get(alias, alias), val
./venv/lib64/python3.12/site-packages/torch/_logging/_internal.py:513:                    log_registry.log_alias_to_log_qnames.get(alias, alias), val
./venv/lib64/python3.12/site-packages/torch/_logging/_internal.py:832:    log_setting = os.environ.get(LOG_ENV_VAR, None)
./venv/lib64/python3.12/site-packages/torch/_logging/_internal.py:966:    fmt = os.environ.get(LOG_FORMAT_ENV_VAR, None)
./venv/lib64/python3.12/site-packages/torch/_logging/_internal.py:969:        for item in os.environ.get(LOG_TRACE_ID_FILTER, "").split(",")
./venv/lib64/python3.12/site-packages/torch/_logging/_internal.py:1046:    out = os.environ.get(LOG_OUT_ENV_VAR, None)
./venv/lib64/python3.12/site-packages/torch/_logging/_internal.py:1088:    trace_dir_name = os.environ.get(TRACE_ENV_VAR, None)
./venv/lib64/python3.12/site-packages/torch/_logging/_internal.py:1090:    if dtrace_dir_name := os.environ.get(DTRACE_ENV_VAR, None):
./venv/lib64/python3.12/site-packages/torch/amp/grad_scaler.py:31:        retval = self._per_device_tensors.get(device, None)
./venv/lib64/python3.12/site-packages/torch/utils/_config_module.py:191:            annotated_type = type_hints.get(key, None)
./venv/lib64/python3.12/site-packages/torch/utils/_functools.py:40:        cached_value = cache.get(args, _cache_sentinel)
./venv/lib64/python3.12/site-packages/torch/utils/checkpoint.py:1113:                _internal_assert(holder.handles.get(gid, None) is None)
./venv/lib64/python3.12/site-packages/torch/utils/viz/_cycles.py:285:            labels = references.get(rid, ["?"])
./venv/lib64/python3.12/site-packages/torch/utils/_sympy/interp.py:206:        if (r := env.get(expr, _nil)) is not _nil:
./venv/lib64/python3.12/site-packages/torch/utils/benchmark/utils/fuzzer.py:320:            values = tuple(params.get(i, i) for i in values)
./venv/lib64/python3.12/site-packages/torch/utils/hipify/hipify_python.py:805:            if constants.API_SPECIAL in meta_data and PYTORCH_MAP.get(src, ""):
./venv/lib64/python3.12/site-packages/torch/utils/data/datapipes/_typing.py:71:    left = TYPE2ABC.get(left, left)
./venv/lib64/python3.12/site-packages/torch/utils/data/datapipes/_typing.py:72:    right = TYPE2ABC.get(right, right)
./venv/lib64/python3.12/site-packages/torch/utils/data/datapipes/_typing.py:120:    ts = [TYPE2ABC.get(_t, _t) for _t in ts]  # type: ignore[misc]
./venv/lib64/python3.12/site-packages/torch/utils/flop_counter.py:848:                    true_val = true_func_counts.get(func_key, 0)
./venv/lib64/python3.12/site-packages/torch/utils/flop_counter.py:849:                    false_val = false_func_counts.get(func_key, 0)
./venv/lib64/python3.12/site-packages/torch/_subclasses/complex_tensor/_ops/aten.py:499:        err_op, ERROR_TYPES.get(err_op, NotImplementedError)
./venv/lib64/python3.12/site-packages/torch/_subclasses/complex_tensor/_ops/common.py:83:    prom_dt = PROMOTE_TYPES.get(out_dt, out_dt)
./venv/lib64/python3.12/site-packages/torch/_subclasses/complex_tensor/_ops/common.py:97:        if COMPLEX_OPS_TABLE.get(op, func) is not func:
./venv/lib64/python3.12/site-packages/torch/_subclasses/complex_tensor/_ops/common.py:132:            DECOMPOSITIONS.get(func, DECOMPOSITIONS.get(func.overloadpacket)),
./venv/lib64/python3.12/site-packages/torch/_subclasses/complex_tensor/_ops/common.py:187:    return COMPLEX_TO_REAL.get(dtype, dtype)
./venv/lib64/python3.12/site-packages/torch/_subclasses/fake_tensor.py:1520:        entry = cache.get(key, None)
./venv/lib64/python3.12/site-packages/torch/nn/modules/module.py:1760:            name = torch.jit._trace._trace_module_map.get(self, None)  # type: ignore[operator, union-attr]
./venv/lib64/python3.12/site-packages/torch/nn/parallel/distributed.py:221:        value = os.environ.get(var, "N/A")
./venv/lib64/python3.12/site-packages/torch/nn/parallel/distributed.py:1058:                for handle in param_to_handle_map.get(p, []):
./venv/lib64/python3.12/site-packages/torch/jit/frontend.py:170:        range_len = len(node_start_tokens.get(node_type, " "))
./venv/lib64/python3.12/site-packages/torch/jit/frontend.py:176:        feature_name = pretty_node_names.get(node_type, node_type.__name__)
./venv/lib64/python3.12/site-packages/torch/jit/_state.py:104:    qual_names = _jit_function_overload_caching.get(key, None)
./venv/lib64/python3.12/site-packages/torch/jit/_state.py:118:    qual_name = _jit_caching_layer.get(key, None)
./venv/lib64/python3.12/site-packages/torch/testing/_internal/common_device_type.py:386:        return test.precision_overrides.get(dtype, self.precision)
./venv/lib64/python3.12/site-packages/torch/testing/_internal/common_device_type.py:391:        return test.tolerance_overrides.get(dtype, tol(self.precision, self.rel_tol))
./venv/lib64/python3.12/site-packages/torch/testing/_internal/distributed/common_state_dict.py:74:            dist_states = dist_osd[_STATE].get(fqn, None)
./venv/lib64/python3.12/site-packages/torch/testing/_internal/distributed/common_state_dict.py:78:                dist_state = states.get(key, None)
./venv/lib64/python3.12/site-packages/torch/testing/_internal/distributed/common_state_dict.py:98:                # dist_value = dist_group.get(key, None)
./venv/lib64/python3.12/site-packages/torch/testing/_internal/distributed/distributed_test.py:611:            pg_timeout_seconds = CUSTOM_PG_TIMEOUT.get(test_name, default_pg_timeout)
./venv/lib64/python3.12/site-packages/torch/testing/_internal/distributed/distributed_test.py:725:                return f"env:{var}={os.environ.get(var, 'N/A')}"
./venv/lib64/python3.12/site-packages/torch/testing/_internal/distributed/distributed_test.py:6224:                return os.environ.get(var, "N/A")
./venv/lib64/python3.12/site-packages/torch/testing/_internal/common_modules.py:560:        v = kwargs.get(key, default)
./venv/lib64/python3.12/site-packages/torch/testing/_internal/opinfo/definitions/nested.py:453:        dimlist_argname, sample.kwargs.get(single_dim_argname, None)
./venv/lib64/python3.12/site-packages/torch/testing/_internal/opinfo/definitions/linalg.py:389:                    }.get(ord, ())
./venv/lib64/python3.12/site-packages/torch/testing/_internal/opinfo/definitions/linalg.py:400:                    }.get(ord, ())
./venv/lib64/python3.12/site-packages/torch/testing/_internal/opinfo/core.py:1537:        result = self.dtypesIf.get(device_type, self.dtypes)
./venv/lib64/python3.12/site-packages/torch/testing/_internal/common_nn.py:2716:        extra_info = non_linear_activations_extra_info.get(non_linear_activation, {})
./venv/lib64/python3.12/site-packages/torch/testing/_internal/common_nn.py:3203:        has_parity=classification_cpp_parity.get(name, True)
./venv/lib64/python3.12/site-packages/torch/testing/_internal/common_nn.py:3205:    extra_info = classification_criterion_no_batch_extra_info.get(name, {})
./venv/lib64/python3.12/site-packages/torch/testing/_internal/common_utils.py:5015:            aik, ajk = data.get(ik, 0), data.get(jk, 0)
./venv/lib64/python3.12/site-packages/torch/testing/_internal/common_distributed.py:458:        }.get(backend, lambda: False)()
./venv/lib64/python3.12/site-packages/torch/testing/_comparison.py:96:        *[dtype_precisions.get(dtype, (0.0, 0.0)) for dtype in dtypes], strict=True
./venv/lib64/python3.12/site-packages/torch/_ops.py:969:        r = self.py_kernels.get(final_key, final_key)
./venv/lib64/python3.12/site-packages/torch/backends/quantized/__init__.py:29:    return all_engines.get(qengine, "*undefined")
./venv/lib64/python3.12/site-packages/torch/autograd/profiler_util.py:233:                evt.stack = fwd_stacks.get(t, [])
./venv/lib64/python3.12/site-packages/torch/autograd/graph.py:544:                count[id] = count.get(id, 0)
./venv/lib64/python3.12/site-packages/torch/autograd/graph.py:546:                buffer[id] = buffer.get(id, [None] * len_tensors)
./venv/lib64/python3.12/site-packages/torch/cuda/_memory_viz.py:376:                name, _, _ = allocation_addr_to_name.get(addr, (addr, None, None))
./venv/lib64/python3.12/site-packages/torch/cuda/_memory_viz.py:381:                name, _, _ = allocation_addr_to_name.get(addr, (addr, None, None))
./venv/lib64/python3.12/site-packages/torch/cuda/_memory_viz.py:394:                name = segment_addr_to_name.get(addr, addr)
./venv/lib64/python3.12/site-packages/torch/cuda/_memory_viz.py:565:        category = memory_profile._categories.get(tensor_key, version)
./venv/lib64/python3.12/site-packages/torch/cuda/_memory_viz.py:567:        stack = allocation_stacks.get(tensor_key, ())
./venv/lib64/python3.12/site-packages/torch/cuda/_sanitizer.py:295:            state[stream] = max(state.get(stream, -1), seq_num)
./venv/lib64/python3.12/site-packages/torch/cuda/_sanitizer.py:334:        return seq_num <= self.current_sync_states[current_stream].get(other_stream, -1)
./venv/lib64/python3.12/site-packages/torch/onnx/_internal/exporter/_registration.py:272:        decomps = self.functions.get(target_or_name, [])
./venv/lib64/python3.12/site-packages/torch/onnx/_internal/fx/passes/type_promotion.py:1553:                    node, arg, type_promotion_info.args_dtypes.get(i, None)
./venv/lib64/python3.12/site-packages/torch/onnx/_internal/fx/passes/type_promotion.py:1559:                node, arg, type_promotion_info.kwargs_dtypes.get(name, None)
./venv/lib64/python3.12/site-packages/torch/onnx/_internal/fx/type_utils.py:80:    return _TORCH_DTYPE_TO_ABBREVIATION.get(dtype, "")
./venv/lib64/python3.12/site-packages/torch/onnx/_internal/torchscript_exporter/registration.py:100:        return self._merged.get(key, default)
./venv/lib64/python3.12/site-packages/torch/_dynamo/cache_size.py:105:    obj = frame.f_locals.get(local_name, None)
./venv/lib64/python3.12/site-packages/torch/_dynamo/polyfills/pytree.py:486:    handler = optree.register_pytree_node.get(tuple, namespace=namespace)
./venv/lib64/python3.12/site-packages/torch/_dynamo/side_effects.py:357:        ) and name in self.store_attr_mutations.get(item, ())
./venv/lib64/python3.12/site-packages/torch/_dynamo/side_effects.py:1099:                    self.store_attr_mutations.get(var, {}).items()
./venv/lib64/python3.12/site-packages/torch/_dynamo/symbolic_convert.py:4507:                        local_dynamism = frozenset(dynamism.get(name, {}).items())
./venv/lib64/python3.12/site-packages/torch/_dynamo/variables/nn_module.py:134:    num_calls = tx.num_calls.get(fully_qualified_name, 0)
./venv/lib64/python3.12/site-packages/torch/_dynamo/variables/functions.py:2423:        handler = self._get_polyfill_handlers().get(fn, fn)
./venv/lib64/python3.12/site-packages/torch/_dynamo/variables/misc.py:153:            if resolved_getattr := search_mro[index].__dict__.get(name, NO_SUCH_SUBOBJ):
./venv/lib64/python3.12/site-packages/torch/_dynamo/variables/builder.py:2488:                and dict(base_source.dynamism).get(normalized_source_name, {0: False})[
./venv/lib64/python3.12/site-packages/torch/_dynamo/variables/builder.py:3342:            stride[i] = candidates.get(i_stride, i_stride)
./venv/lib64/python3.12/site-packages/torch/_dynamo/variables/builder.py:3406:    prior_policy = tx.output.tracing_context.tensor_to_context.get(e, None)
./venv/lib64/python3.12/site-packages/torch/_dynamo/variables/builder.py:3523:        specialize_on.append(getattr(e, "_specialize_on", {}).get(i, []))
./venv/lib64/python3.12/site-packages/torch/_dynamo/variables/builder.py:3536:            and dict(base_source.dynamism).get(normalized_source_name, {i: False})[i]
./venv/lib64/python3.12/site-packages/torch/_dynamo/variables/tensor.py:517:                static_attr = all_tensor_attrs.get(name, None)
./venv/lib64/python3.12/site-packages/torch/_dynamo/variables/tensor.py:671:        static_attr = all_tensor_attrs.get(name, None)
./venv/lib64/python3.12/site-packages/torch/_dynamo/variables/tensor.py:1650:            kwargs = {kwargs_rename.get(k, k): v for k, v in kwargs.items()}
./venv/lib64/python3.12/site-packages/torch/_dynamo/debug_utils.py:848:        return sym_shapes_dict.get(symint, default_sym_shape)  # type: ignore[return-value]
./venv/lib64/python3.12/site-packages/torch/_dynamo/funcname_cache.py:75:    return cache[filename].get(lineno, None)
./venv/lib64/python3.12/site-packages/torch/_dynamo/codegen.py:203:            source = self.overridden_sources.get(value, value)
./venv/lib64/python3.12/site-packages/torch/_dynamo/codegen.py:581:        if global_scope.get(name, None) is mod:
./venv/lib64/python3.12/site-packages/torch/_dynamo/trace_rules.py:3125:        return self.function_names.get(idx, default)
./venv/lib64/python3.12/site-packages/torch/_dynamo/trace_rules.py:3974:        rule = get_torch_obj_rule_map().get(obj, None)
./venv/lib64/python3.12/site-packages/jinja2/lexer.py:182:    }.get(token_type, token_type)
./venv/lib64/python3.12/site-packages/jinja2/debug.py:179:        cur_depth = local_overrides.get(name, (-1,))[0]
./venv/lib64/python3.12/site-packages/jinja2/ext.py:825:        return options.get(key, str(default)).lower() in {"1", "on", "yes", "true"}
./venv/lib64/python3.12/site-packages/jinja2/nodes.py:63:            storage.extend(d.get(attr, ()))
./venv/lib64/python3.12/site-packages/scipy/optimize/_optimize.py:2433:                                     2: _status_message['nan']}.get(flag, ''),
./venv/lib64/python3.12/site-packages/scipy/optimize/_tnc.py:262:                    4:MSG_EXIT, 5:MSG_ALL}.get(messages, MSG_ALL)
./venv/lib64/python3.12/site-packages/scipy/optimize/_tnc.py:383:                    4:MSG_EXIT, 5:MSG_ALL}.get(mesg_num, MSG_ALL)
./venv/lib64/python3.12/site-packages/scipy/optimize/_tstutils.py:127:    v = _f6_cache.get(x, None)
./venv/lib64/python3.12/site-packages/scipy/optimize/_tstutils.py:844:    tests = subsets.get(collection, [])
./venv/lib64/python3.12/site-packages/scipy/optimize/_root_scalar.py:276:        methodc = getattr(optzeros, map2underlying.get(meth, meth))
./venv/lib64/python3.12/site-packages/scipy/optimize/_highspy/_highs_wrapper.py:320:    expected_type = valid_types.get(option_type, None)
./venv/lib64/python3.12/site-packages/scipy/optimize/tests/test_zeros.py:81:                k = {'a': 'x0', 'b': 'x1', 'func': 'f'}.get(k, k)
./venv/lib64/python3.12/site-packages/scipy/optimize/_linprog_highs.py:57:        scipy_statuses_messages.get(highs_status, unrecognized))
./venv/lib64/python3.12/site-packages/scipy/optimize/_nonlin.py:1481:            ).get(method, method)
./venv/lib64/python3.12/site-packages/scipy/sparse/_dok.py:170:        return self._dict.get(key, default)
./venv/lib64/python3.12/site-packages/scipy/sparse/_dok.py:174:        return self._dict.get(idx, self.dtype.type(0))
./venv/lib64/python3.12/site-packages/scipy/sparse/_dok.py:186:        dok_vals = [self._dict.get(i, 0) for i in idx.ravel()]
./venv/lib64/python3.12/site-packages/scipy/sparse/_dok.py:319:                aij = self._dict.get(key, 0) + other
./venv/lib64/python3.12/site-packages/scipy/sparse/linalg/_eigen/arpack/arpack.py:288:        msg = infodict.get(info, "Unknown error")
./venv/lib64/python3.12/site-packages/scipy/linalg/_basic.py:229:    }.get(assume_a, 'unknown')
./venv/lib64/python3.12/site-packages/scipy/linalg/_basic.py:733:    trans = {'N': 0, 'T': 1, 'C': 2}.get(trans, trans)
./venv/lib64/python3.12/site-packages/scipy/linalg/blas.py:332:    prefix, dtype = _type_conv.get(max_score, ('d', np.dtype('float64')))
./venv/lib64/python3.12/site-packages/scipy/linalg/blas.py:364:        func_name = alias.get(func_name, func_name)
./venv/lib64/python3.12/site-packages/scipy/stats/_new_distributions.py:193:        return raw_moments.get(order, None)
./venv/lib64/python3.12/site-packages/scipy/stats/_axis_nan_policy.py:497:                        if kwds.get(name, None) is not None]
./venv/lib64/python3.12/site-packages/scipy/stats/_distribution_infrastructure.py:339:                a = np.asarray(parameter_values.get(a, a))
./venv/lib64/python3.12/site-packages/scipy/stats/_distribution_infrastructure.py:343:                b = np.asarray(parameter_values.get(b, b))
./venv/lib64/python3.12/site-packages/scipy/stats/_distribution_infrastructure.py:486:        return self.symbols.get(endpoint, f"{endpoint}")
./venv/lib64/python3.12/site-packages/scipy/stats/_distribution_infrastructure.py:519:        a = self.symbols.get(a, a)
./venv/lib64/python3.12/site-packages/scipy/stats/_distribution_infrastructure.py:520:        b = self.symbols.get(b, b)
./venv/lib64/python3.12/site-packages/scipy/stats/_distribution_infrastructure.py:985:        low, high = endpoints.get(method_name, self.support())
./venv/lib64/python3.12/site-packages/scipy/stats/_distribution_infrastructure.py:1048:                replacements.get(method_name, (np.nan, np.nan)))
./venv/lib64/python3.12/site-packages/scipy/stats/_distribution_infrastructure.py:1147:        method = method or self._method_cache.get(func_name, None)
./venv/lib64/python3.12/site-packages/scipy/stats/_distribution_infrastructure.py:3165:            moment = self._moment_raw_cache.get(order, None)
./venv/lib64/python3.12/site-packages/scipy/stats/_distribution_infrastructure.py:3223:            moment = self._moment_central_cache.get(order, None)
./venv/lib64/python3.12/site-packages/scipy/stats/_distribution_infrastructure.py:3282:        return general_central_moments.get(order, None)
./venv/lib64/python3.12/site-packages/scipy/stats/_distribution_infrastructure.py:3294:            moment = self._moment_standardized_cache.get(order, None)
./venv/lib64/python3.12/site-packages/scipy/stats/_distribution_infrastructure.py:3329:        return general_standard_moments.get(order, None)
./venv/lib64/python3.12/site-packages/scipy/stats/tests/test_continuous.py:132:        a = _Domain.symbols.get(a, a)
./venv/lib64/python3.12/site-packages/scipy/stats/tests/test_continuous.py:133:        b = _Domain.symbols.get(b, b)
./venv/lib64/python3.12/site-packages/scipy/stats/tests/test_continuous.py:1146:        rtol = custom_tolerances.get(distname, 1e-7)
./venv/lib64/python3.12/site-packages/scipy/stats/tests/test_continuous.py:1190:                if distname not in skip_raw.get(order, {}):
./venv/lib64/python3.12/site-packages/scipy/stats/tests/test_discrete_basic.py:74:        k = spec_k.get(distname, 1)
./venv/lib64/python3.12/site-packages/scipy/stats/tests/test_discrete_basic.py:394:            if (shape.name in integrality_exceptions.get(distname, set()) or
./venv/lib64/python3.12/site-packages/scipy/stats/tests/test_continuous_basic.py:167:    x = spec_x.get(distname, 0.5)
./venv/lib64/python3.12/site-packages/scipy/special/_basic.py:2837:    dtypes = [mapping.get(x, x) for x in dtypes]
./venv/lib64/python3.12/site-packages/scipy/special/tests/test_basic.py:2982:            n = np.array([_FACTORIALK_LIMITS_64BITS.get(k, 1)])
./venv/lib64/python3.12/site-packages/scipy/integrate/_ode.py:998:                          f'{self.messages.get(istate, unexpected_istate_msg):s}',
./venv/lib64/python3.12/site-packages/scipy/integrate/_ode.py:1180:                          f'{self.messages.get(istate, unexpected_istate_msg):s}',
./venv/lib64/python3.12/site-packages/scipy/integrate/_ode.py:1384:                          f'{self.messages.get(istate, unexpected_istate_msg):s}',
./venv/lib64/python3.12/site-packages/scipy/integrate/_ivp/ivp.py:730:    message = MESSAGES.get(status, message)
./venv/lib64/python3.12/site-packages/scipy/interpolate/_rbfinterp.py:291:        min_degree = _NAME_TO_MIN_DEGREE.get(kernel, -1)
./venv/lib64/python3.12/site-packages/scipy/interpolate/_fitpack2.py:321:            message = _curfit_messages.get(ier, f'ier={ier}')
./venv/lib64/python3.12/site-packages/scipy/interpolate/_fitpack2.py:1451:            message = _surfit_messages.get(ier, f'ier={ier}')
./venv/lib64/python3.12/site-packages/scipy/interpolate/_fitpack2.py:1553:                message = _surfit_messages.get(ier, f'ier={ier}')
./venv/lib64/python3.12/site-packages/scipy/interpolate/_fitpack2.py:1645:            msg = _surfit_messages.get(ier, f'ier={ier}')
./venv/lib64/python3.12/site-packages/scipy/interpolate/_fitpack2.py:1969:            message = _spherefit_messages.get(ier, f'ier={ier}')
./venv/lib64/python3.12/site-packages/scipy/interpolate/_fitpack2.py:2125:            message = _spherefit_messages.get(ier, f'ier={ier}')
./venv/lib64/python3.12/site-packages/scipy/interpolate/_fitpack2.py:2394:            msg = _spfit_messages.get(ier, f'ier={ier}')
./venv/lib64/python3.12/site-packages/scipy/interpolate/tests/test_rbfinterp.py:82:    m = _NAME_TO_MIN_DEGREE.get(kernel, -1) + 1
./venv/lib64/python3.12/site-packages/scipy/interpolate/tests/test_rbf.py:131:        check_rbf1d_regularity(function, tolerances.get(function, 1e-2))
./venv/lib64/python3.12/site-packages/scipy/interpolate/tests/test_rbf.py:159:        check_2drbf1d_regularity(function, tolerances.get(function, 1e-2))
./venv/lib64/python3.12/site-packages/scipy/spatial/distance.py:2125:        metric_info = _METRIC_ALIAS.get(mstr, None)
./venv/lib64/python3.12/site-packages/scipy/spatial/distance.py:2134:        metric_info = _METRIC_ALIAS.get(mstr, None)
./venv/lib64/python3.12/site-packages/scipy/spatial/distance.py:2140:            metric_info = _TEST_METRICS.get(mstr, None)
./venv/lib64/python3.12/site-packages/scipy/spatial/distance.py:2916:        metric_info = _METRIC_ALIAS.get(mstr, None)
./venv/lib64/python3.12/site-packages/scipy/spatial/distance.py:2923:        metric_info = _METRIC_ALIAS.get(mstr, None)
./venv/lib64/python3.12/site-packages/scipy/spatial/distance.py:2928:            metric_info = _TEST_METRICS.get(mstr, None)
./venv/lib64/python3.12/site-packages/scipy/spatial/transform/_rotation.py:37:    return backend_registry.get(xp, xp_backend)
./venv/lib64/python3.12/site-packages/scipy/spatial/transform/_rigid_transform.py:41:    return backend_registry.get(xp, xp_backend)
./venv/lib64/python3.12/site-packages/scipy/spatial/tests/test_distance.py:292:        weights = kwargs.get(weight_arg, None)
./venv/lib64/python3.12/site-packages/scipy/_lib/array_api_extra/testing.py:379:        return dask.get(dsk, keys, **kwargs)  # type: ignore[attr-defined]  # pyright: ignore[reportPrivateImportUsage]
./venv/lib64/python3.12/site-packages/scipy/_lib/_pep440.py:209:        part = _legacy_version_replacement_map.get(part, part)
./venv/lib64/python3.12/site-packages/scipy/_lib/_array_api_docs_tables.py:137:        backend = BACKEND_NAMES_MAP.get(backend, backend)
./venv/lib64/python3.12/site-packages/scipy/_lib/_array_api_docs_tables.py:223:            if name in ALIASES.get(module_name, {}):
./venv/lib64/python3.12/site-packages/scipy/_lib/_array_api_docs_tables.py:230:            entry = xp_capabilities_table.get(thing, None)
./venv/lib64/python3.12/site-packages/scipy/_lib/cobyqa/main.py:1468:    }.get(status, "Unknown exit status")
./venv/lib64/python3.12/site-packages/scipy/io/_fast_matrix_market/__init__.py:276:    dtype = _field_to_dtype.get(field, None)
./venv/lib64/python3.12/site-packages/scipy/io/_mmio.py:557:                }.get(field, None)
./venv/lib64/python3.12/site-packages/scipy/io/_mmio.py:662:        dtype = self.DTYPES_BY_FIELD.get(field, None)
./venv/lib64/python3.12/site-packages/scipy/ndimage/_support_alternative_backends.py:113:    capabilities = capabilities_dict.get(func_name, default_capabilities)
./venv/lib64/python3.12/site-packages/scipy/ndimage/_filters.py:140:    mode = mode_map.get(mode, mode)
./venv/lib64/python3.12/site-packages/typing_extensions.py:3968:                module = sys.modules.get(module_name, None)
./venv/lib64/python3.12/site-packages/typing_extensions.py:4073:                    module = sys.modules.get(module_name, None)
./venv/lib64/python3.12/site-packages/pip/_vendor/packaging/markers.py:212:    value: Union[str, Undefined] = environment.get(name, _undefined)
./venv/lib64/python3.12/site-packages/pip/_vendor/packaging/version.py:181:        part = _legacy_version_replacement_map.get(part, part)
./venv/lib64/python3.12/site-packages/pip/_vendor/requests/utils.py:876:        proxy = environ_proxies.get(scheme, environ_proxies.get("all"))
./venv/lib64/python3.12/site-packages/pip/_vendor/requests/structures.py:96:        return self.__dict__.get(key, None)
./venv/lib64/python3.12/site-packages/pip/_vendor/requests/structures.py:99:        return self.__dict__.get(key, default)
./venv/lib64/python3.12/site-packages/pip/_vendor/requests/cookies.py:76:        return self._r.headers.get(name, self._new_headers.get(name, default))
./venv/lib64/python3.12/site-packages/pip/_vendor/urllib3/response.py:672:            "in urllib3 v2.1.0. Instead use HTTPResponse.headers.get(name, default).",
./venv/lib64/python3.12/site-packages/pip/_vendor/urllib3/response.py:676:        return self.headers.get(name, default)
./venv/lib64/python3.12/site-packages/pip/_vendor/urllib3/connectionpool.py:1104:    port = port or port_by_scheme.get(scheme, 80)
./venv/lib64/python3.12/site-packages/pip/_vendor/urllib3/_collections.py:65:            evicted_value = self._container.get(key, _Null)
./venv/lib64/python3.12/site-packages/pip/_vendor/urllib3/fields.py:238:            if self.headers.get(sort_key, False):
./venv/lib64/python3.12/site-packages/pip/_vendor/chardet/chardistribution.py:179:            return JOHAB_TO_EUCKR_ORDER_TABLE.get(code, -1)
./venv/lib64/python3.12/site-packages/pip/_vendor/chardet/sbcharsetprober.py:105:            order = char_to_order_map.get(char, CharacterCategory.UNDEFINED)
./venv/lib64/python3.12/site-packages/pip/_vendor/webencodings/__init__.py:83:            python_name = PYTHON_NAMES.get(name, name)
./venv/lib64/python3.12/site-packages/pip/_vendor/cachecontrol/cache.py:40:        return self.data.get(key, None)
./venv/lib64/python3.12/site-packages/pip/_vendor/cachecontrol/serialize.py:55:                header_value = request.headers.get(header, None)
./venv/lib64/python3.12/site-packages/pip/_vendor/cachecontrol/serialize.py:119:            if request.headers.get(header, None) != value:
./venv/lib64/python3.12/site-packages/pip/_vendor/rich/_emoji_replace.py:21:    default_variant_code = variants.get(default_variant, "") if default_variant else ""
./venv/lib64/python3.12/site-packages/pip/_vendor/rich/emoji.py:55:            self._char += self.VARIANTS.get(variant, "")
./venv/lib64/python3.12/site-packages/pip/_vendor/rich/padding.py:87:                Measurement.get(console, options, self.renderable).maximum
./venv/lib64/python3.12/site-packages/pip/_vendor/rich/padding.py:132:        measure_min, measure_max = Measurement.get(console, options, self.renderable)
./venv/lib64/python3.12/site-packages/pip/_vendor/rich/styled.py:34:        return Measurement.get(console, options, self.renderable)
./venv/lib64/python3.12/site-packages/pip/_vendor/rich/align.py:230:        measurement = Measurement.get(console, options, self.renderable)
./venv/lib64/python3.12/site-packages/pip/_vendor/rich/align.py:286:        measurement = Measurement.get(console, options, self.renderable)
./venv/lib64/python3.12/site-packages/pip/_vendor/rich/spinner.py:58:        return Measurement.get(console, options, text)
./venv/lib64/python3.12/site-packages/pip/_vendor/rich/console.py:812:            color_system = _TERM_COLORS.get(colors, ColorSystem.STANDARD)
./venv/lib64/python3.12/site-packages/pip/_vendor/rich/console.py:1283:        measurement = Measurement.get(self, options or self.options, renderable)
./venv/lib64/python3.12/site-packages/pip/_vendor/rich/containers.py:50:            Measurement.get(console, options, renderable)
./venv/lib64/python3.12/site-packages/pip/_vendor/rich/box.py:86:            box = LEGACY_WINDOWS_SUBSTITUTIONS.get(box, box)
./venv/lib64/python3.12/site-packages/pip/_vendor/rich/box.py:99:        return PLAIN_HEADED_SUBSTITUTIONS.get(self, self)
./venv/lib64/python3.12/site-packages/pip/_vendor/rich/constrain.py:36:        measurement = Measurement.get(console, options, self.renderable)
./venv/lib64/python3.12/site-packages/pip/_vendor/distro/distro.py:837:            return table.get(distro_id, distro_id)
./venv/lib64/python3.12/site-packages/pip/_vendor/distro/distro.py:1057:        return self._os_release_info.get(attribute, "")
./venv/lib64/python3.12/site-packages/pip/_vendor/distro/distro.py:1066:        return self._lsb_release_info.get(attribute, "")
./venv/lib64/python3.12/site-packages/pip/_vendor/distro/distro.py:1075:        return self._distro_release_info.get(attribute, "")
./venv/lib64/python3.12/site-packages/pip/_vendor/distro/distro.py:1084:        return self._uname_info.get(attribute, "")
./venv/lib64/python3.12/site-packages/pip/_vendor/pkg_resources/__init__.py:427:    return {'PowerPC': 'ppc', 'Power_Macintosh': 'ppc'}.get(machine, machine)
./venv/lib64/python3.12/site-packages/pip/_vendor/pkg_resources/__init__.py:869:                    requirers = required_by.get(req, None)
./venv/lib64/python3.12/site-packages/pip/_vendor/pkg_resources/__init__.py:1026:            for extra in self.get(req, ()) + (extras or (None,))
./venv/lib64/python3.12/site-packages/pip/_vendor/pkg_resources/__init__.py:1100:        return self._distmap.get(distribution_key, [])
./venv/lib64/python3.12/site-packages/pip/_vendor/pkg_resources/__init__.py:2376:        for package in _namespace_packages.get(parent, ()):
./venv/lib64/python3.12/site-packages/pip/_vendor/pkg_resources/__init__.py:2824:        deps.extend(dm.get(None, ()))
./venv/lib64/python3.12/site-packages/pip/_vendor/pkg_resources/__init__.py:2942:            return ep_map.get(group, {})
./venv/lib64/python3.12/site-packages/pip/_vendor/pygments/style.py:88:                styledefs = obj.styles.get(token, '').split()
./venv/lib64/python3.12/site-packages/pip/_vendor/pygments/style.py:96:                for styledef in obj.styles.get(token, '').split():
./venv/lib64/python3.12/site-packages/pip/_vendor/pygments/util.py:45:    string = options.get(optname, default)
./venv/lib64/python3.12/site-packages/pip/_vendor/pygments/util.py:56:    Intuitively, this is `options.get(optname, default)`, but restricted to
./venv/lib64/python3.12/site-packages/pip/_vendor/pygments/util.py:66:    string = options.get(optname, default)
./venv/lib64/python3.12/site-packages/pip/_vendor/pygments/util.py:87:    string = options.get(optname, default)
./venv/lib64/python3.12/site-packages/pip/_vendor/pygments/util.py:105:    val = options.get(optname, default)
./venv/lib64/python3.12/site-packages/pip/_vendor/pygments/formatters/terminal256.py:206:        index = self.best_match.get(color, None)
./venv/lib64/python3.12/site-packages/pip/_vendor/pygments/filters/__init__.py:824:            opt = options.get(name, False)
./venv/lib64/python3.12/site-packages/pip/_vendor/pygments/plugin.py:68:        return groups.get(group_name, [])
./venv/lib64/python3.12/site-packages/pip/_vendor/resolvelib/structs.py:98:        return itertools.chain(self._accessor(v), self._appends.get(k, ()))
./venv/lib64/python3.12/site-packages/pip/_vendor/pyparsing/results.py:215:            self._tokdict[k] = self._tokdict.get(k, list()) + [v]
./venv/lib64/python3.12/site-packages/pip/_vendor/pyparsing/results.py:221:            self._tokdict[k] = self._tokdict.get(k, list()) + [
./venv/lib64/python3.12/site-packages/pip/_vendor/distlib/util.py:1074:        return iter(self._subscribers.get(event, ()))
./venv/lib64/python3.12/site-packages/pip/_vendor/distlib/util.py:1117:            for p in set(self._preds.get(node, ())):
./venv/lib64/python3.12/site-packages/pip/_vendor/distlib/util.py:1119:            for s in set(self._succs.get(node, ())):
./venv/lib64/python3.12/site-packages/pip/_vendor/distlib/util.py:1172:                preds = self._preds.get(step, ())
./venv/lib64/python3.12/site-packages/pip/_vendor/distlib/util.py:1861:                        result['username'] = config.get(server, 'username')
./venv/lib64/python3.12/site-packages/pip/_vendor/distlib/util.py:1869:                                result[key] = config.get(server, key)
./venv/lib64/python3.12/site-packages/pip/_vendor/distlib/util.py:1886:                    repository = config.get(server, 'repository')
./venv/lib64/python3.12/site-packages/pip/_vendor/distlib/util.py:1890:                    'username': config.get(server, 'username'),
./venv/lib64/python3.12/site-packages/pip/_vendor/distlib/util.py:1891:                    'password': config.get(server, 'password'),
./venv/lib64/python3.12/site-packages/pip/_vendor/distlib/compat.py:837:            'od.setdefault(k[,d]) -> od.get(k,d), also set od[k]=d if k not in od'
./venv/lib64/python3.12/site-packages/pip/_vendor/distlib/compat.py:947:            value = dict.get(self, key, default)
./venv/lib64/python3.12/site-packages/pip/_vendor/distlib/compat.py:1113:                    converter = self.value_converters.get(prefix, None)
./venv/lib64/python3.12/site-packages/pip/_vendor/distlib/version.py:592:            p = _VERSION_REPLACE.get(p, p)
./venv/lib64/python3.12/site-packages/pip/_vendor/distlib/locators.py:399:            result.download_urls = versions.get('urls', {}).get(version, set())
./venv/lib64/python3.12/site-packages/pip/_vendor/distlib/metadata.py:300:        return _ATTR2FIELD.get(name, name)
./venv/lib64/python3.12/site-packages/pip/_vendor/distlib/metadata.py:547:                value = self.get(field, None)
./venv/lib64/python3.12/site-packages/pip/_vendor/distlib/metadata.py:737:                    result = self._data.get(key, value)
./venv/lib64/python3.12/site-packages/pip/_vendor/distlib/metadata.py:749:                                result = d.get(key, value)
./venv/lib64/python3.12/site-packages/pip/_vendor/distlib/metadata.py:755:                                result = d.get(key, value)
./venv/lib64/python3.12/site-packages/pip/_vendor/platformdirs/unix.py:194:        media_dir = os.environ.get(env_var, "").strip()
./venv/lib64/python3.12/site-packages/pip/_internal/network/download.py:117:    resp = session.get(target_url, headers=HEADERS, stream=True)
./venv/lib64/python3.12/site-packages/pip/_internal/utils/hashes.py:68:        return hex_digest in self._allowed.get(hash_name, [])
./venv/lib64/python3.12/site-packages/pip/_internal/utils/temp_dir.py:66:        return self._should_delete.get(kind, True)
./venv/lib64/python3.12/site-packages/pip/_internal/build_env.py:139:            name: os.environ.get(name, None)
./venv/lib64/python3.12/site-packages/pip/_internal/resolution/resolvelib/provider.py:176:        requested_order = self._user_requested.get(identifier, math.inf)
./venv/lib64/python3.12/site-packages/pip/_internal/resolution/resolvelib/factory.py:441:        incompat_ids = {id(c) for c in incompatibilities.get(identifier, ())}
./venv/lib64/python3.12/site-packages/pip/_internal/resolution/resolvelib/resolver.py:262:        last_known_parent_count = weights.get(node, 0)
./venv/lib64/python3.12/site-packages/sklearn/inspection/_plot/partial_dependence.py:1290:                old_min_pd, old_max_pd = pdp_lim.get(n_fx, (min_pd, max_pd))
./venv/lib64/python3.12/site-packages/sklearn/model_selection/_split.py:3041:                value = self.cvargs.get(key, None)
./venv/lib64/python3.12/site-packages/sklearn/linear_model/tests/test_logistic.py:854:            solver=solver, max_iter=solver_max_iter.get(solver, 100), **params
./venv/lib64/python3.12/site-packages/sklearn/linear_model/tests/test_logistic.py:917:            tol=solver_tol.get(solver, tol),
./venv/lib64/python3.12/site-packages/sklearn/linear_model/tests/test_logistic.py:918:            max_iter=solver_max_iter.get(solver, 100),
./venv/lib64/python3.12/site-packages/sklearn/pipeline.py:909:                Xt, **routed_params.get(name, {}).get("transform", {})
./venv/lib64/python3.12/site-packages/sklearn/neighbors/tests/test_kd_tree.py:57:    metric_params = METRICS.get(metric, {})
./venv/lib64/python3.12/site-packages/sklearn/neighbors/tests/test_kd_tree.py:93:    metric_params = METRICS.get(metric, {})
./venv/lib64/python3.12/site-packages/sklearn/neighbors/tests/test_ball_tree.py:126:    metric_params = METRICS.get(metric, {})
./venv/lib64/python3.12/site-packages/sklearn/neighbors/tests/test_ball_tree.py:162:    metric_params = METRICS.get(metric, {})
./venv/lib64/python3.12/site-packages/sklearn/gaussian_process/kernels.py:388:            if np.any(params_a.get(key, None) != params_b.get(key, None)):
./venv/lib64/python3.12/site-packages/sklearn/metrics/_classification.py:587:        y_pred = np.array([label_to_ind.get(label, n_labels + 1) for label in y_pred])
./venv/lib64/python3.12/site-packages/sklearn/metrics/_classification.py:588:        y_true = np.array([label_to_ind.get(label, n_labels + 1) for label in y_true])
./venv/lib64/python3.12/site-packages/sklearn/utils/multiclass.py:103:    _unique_labels = _FN_UNIQUE_LABELS.get(label_type, None)
./venv/lib64/python3.12/site-packages/sklearn/utils/_repr_html/params.py:111:        if param_numpydoc := param_map.get(row, None):
./venv/lib64/python3.12/site-packages/sklearn/externals/_packaging/version.py:212:        part = _legacy_version_replacement_map.get(part, part)
./venv/lib64/python3.12/site-packages/sklearn/externals/array_api_extra/testing.py:379:        return dask.get(dsk, keys, **kwargs)  # type: ignore[attr-defined]  # pyright: ignore[reportPrivateImportUsage]
./venv/lib64/python3.12/site-packages/sklearn/tests/test_metadata_routing.py:307:    default_params_for_method = routed_params.get(method, default=default)
./venv/lib64/python3.12/site-packages/sklearn/tests/test_metaestimators_metadata_routing.py:625:        for callee in method_mapping.get(caller, [caller]):
./venv/lib64/python3.12/site-packages/sklearn/tests/test_metaestimators_metadata_routing.py:849:        extra_method_args = metaestimator.get("method_args", {}).get(method_name, {})
./venv/lib64/python3.12/site-packages/sklearn/tests/metadata_routing_common.py:72:        getattr(obj, "_records", dict()).get(method, dict()).get(parent, list())
./venv/lib64/python3.12/site-packages/sklearn/cluster/tests/test_hdbscan.py:156:    }.get(metric, None)
./venv/lib64/python3.12/site-packages/sklearn/datasets/tests/test_common.py:95:    markers_fetch = FETCH_PYTEST_MARKERS.get(param, {})
./venv/lib64/python3.12/site-packages/sklearn/datasets/tests/test_openml.py:956:        expected_missing = datasets_missing_values[data_id].get(name, 0)
./venv/lib64/python3.12/site-packages/sklearn/svm/_base.py:1049:    _solver_pen = _solver_type_dict.get(loss, None)
./venv/lib64/python3.12/site-packages/sklearn/svm/_base.py:1053:        _solver_dual = _solver_pen.get(penalty, None)
./venv/lib64/python3.12/site-packages/sklearn/svm/_base.py:1060:            solver_num = _solver_dual.get(dual, None)
./venv/lib64/python3.12/site-packages/networkx/convert_matrix.py:297:    edge_attr = {k: [d.get(k, nan) for _, _, d in edgelist] for k in all_attrs}
./venv/lib64/python3.12/site-packages/networkx/convert_matrix.py:1101:                attr_data = [wt.get(attr, 1.0) for wt in wts]
./venv/lib64/python3.12/site-packages/networkx/algorithms/time_dependent.py:141:        weights = [G.nodes[i].get(weight, 1) for i in pred]
./venv/lib64/python3.12/site-packages/networkx/algorithms/approximation/dominating_set.py:92:        return G.nodes[v].get(weight, 1) / len(neighborhood - dom_set)
./venv/lib64/python3.12/site-packages/networkx/algorithms/approximation/traveling_salesman.py:1041:        next_node = min(nodeset, key=lambda n: nbrdict[n].get(weight, 1))
./venv/lib64/python3.12/site-packages/networkx/algorithms/approximation/traveling_salesman.py:1247:    cost = sum(G[u][v].get(weight, 1) for u, v in pairwise(cycle))
./venv/lib64/python3.12/site-packages/networkx/algorithms/approximation/traveling_salesman.py:1256:            adj_cost = sum(G[u][v].get(weight, 1) for u, v in pairwise(adj_sol))
./venv/lib64/python3.12/site-packages/networkx/algorithms/approximation/traveling_salesman.py:1482:    cost = sum(G[u][v].get(weight, 1) for u, v in pairwise(cycle))
./venv/lib64/python3.12/site-packages/networkx/algorithms/approximation/traveling_salesman.py:1492:            adj_cost = sum(G[u][v].get(weight, 1) for u, v in pairwise(adj_sol))
./venv/lib64/python3.12/site-packages/networkx/algorithms/approximation/steinertree.py:79:        weight_here = d_1[(u, su)] + data.get(weight, 1) + d_1[(v, sv)]
./venv/lib64/python3.12/site-packages/networkx/algorithms/approximation/steinertree.py:92:            G_3.add_edge(n1, n2, weight=G[n1][n2].get(weight, 1))
./venv/lib64/python3.12/site-packages/networkx/algorithms/approximation/steinertree.py:97:            (u, v, min(G[u][v], key=lambda k: G[u][v][k].get(weight, 1)))
./venv/lib64/python3.12/site-packages/networkx/algorithms/approximation/steinertree.py:134:            (u, v, min(G[u][v], key=lambda k: G[u][v][k].get(weight, 1)))
./venv/lib64/python3.12/site-packages/networkx/algorithms/structuralholes.py:21:        a_uv = G[u][v].get(weight, 1)
./venv/lib64/python3.12/site-packages/networkx/algorithms/structuralholes.py:25:        a_vu = G[v][u].get(weight, 1)
./venv/lib64/python3.12/site-packages/networkx/algorithms/community/bipartitions.py:148:        sum_weight = lambda u, v, d: sum(dd.get(weight, 1) for dd in d.values())
./venv/lib64/python3.12/site-packages/networkx/algorithms/community/bipartitions.py:150:        sum_weight = lambda u, v, d: d.get(weight, 1)
./venv/lib64/python3.12/site-packages/networkx/algorithms/dag.py:1078:                    max(data.values(), key=lambda x: x.get(weight, default_weight))
./venv/lib64/python3.12/site-packages/networkx/algorithms/dag.py:1081:                ).get(weight, default_weight),
./venv/lib64/python3.12/site-packages/networkx/algorithms/dag.py:1150:            i = max(G[u][v], key=lambda x: G[u][v][x].get(weight, default_weight))
./venv/lib64/python3.12/site-packages/networkx/algorithms/dag.py:1151:            path_length += G[u][v][i].get(weight, default_weight)
./venv/lib64/python3.12/site-packages/networkx/algorithms/dag.py:1154:            path_length += G[u][v].get(weight, default_weight)
./venv/lib64/python3.12/site-packages/networkx/algorithms/link_prediction.py:340:            path_len = spl[u].get(v, inf)
./venv/lib64/python3.12/site-packages/networkx/algorithms/bipartite/projection.py:459:    ...         w += G[u][nbr].get(weight, 1) + G[v][nbr].get(weight, 1)
./venv/lib64/python3.12/site-packages/networkx/algorithms/bipartite/matrix.py:102:                (row_index[u], col_index[v], d.get(weight, 1))
./venv/lib64/python3.12/site-packages/networkx/algorithms/bipartite/link_analysis.py:250:    p0 = np.array([top_personalization.get(n, 0) for n in top], dtype=float)
./venv/lib64/python3.12/site-packages/networkx/algorithms/bipartite/link_analysis.py:251:    u0 = np.array([bottom_personalization.get(n, 0) for n in bottom], dtype=float)
./venv/lib64/python3.12/site-packages/networkx/algorithms/bipartite/tests/test_project.py:394:                w += G.edges[u, nbr].get(weight, 1) + G.edges[v, nbr].get(weight, 1)
./venv/lib64/python3.12/site-packages/networkx/algorithms/shortest_paths/weighted.py:77:        return lambda u, v, d: min(attr.get(weight, 1) for attr in d.values())
./venv/lib64/python3.12/site-packages/networkx/algorithms/shortest_paths/weighted.py:78:    return lambda u, v, data: data.get(weight, 1)
./venv/lib64/python3.12/site-packages/networkx/algorithms/shortest_paths/weighted.py:1471:                if dist_v < dist.get(v, inf):
./venv/lib64/python3.12/site-packages/networkx/algorithms/shortest_paths/weighted.py:1496:                        count_v = count.get(v, 0) + 1
./venv/lib64/python3.12/site-packages/networkx/algorithms/shortest_paths/tests/test_weighted.py:17:                return min(e.get(weight, 1) for e in d.values())
./venv/lib64/python3.12/site-packages/networkx/algorithms/shortest_paths/tests/test_weighted.py:22:                return d.get(weight, 1)
./venv/lib64/python3.12/site-packages/networkx/algorithms/shortest_paths/dense.py:154:        e_weight = d.get(weight, 1.0)
./venv/lib64/python3.12/site-packages/networkx/algorithms/distance_regular.py:207:        if cint.get(i, c) != c or bint.get(i, b) != b:
./venv/lib64/python3.12/site-packages/networkx/algorithms/distance_regular.py:213:        [bint.get(j, 0) for j in range(diam)],
./venv/lib64/python3.12/site-packages/networkx/algorithms/connectivity/stoerwagner.py:96:        (u, v, {"weight": e.get(weight, 1)}) for u, v, e in G.edges(data=True) if u != v
./venv/lib64/python3.12/site-packages/networkx/algorithms/connectivity/stoerwagner.py:125:                    h.insert(v, h.get(v, 0) - e["weight"])
./venv/lib64/python3.12/site-packages/networkx/algorithms/connectivity/tests/test_stoer_wagner.py:21:            w += e.get(weight, 1)
./venv/lib64/python3.12/site-packages/networkx/algorithms/centrality/katz.py:176:                x[nbr] += xlast[n] * G[n][nbr].get(weight, 1)
./venv/lib64/python3.12/site-packages/networkx/algorithms/centrality/reaching.py:104:            return total_weight / d.get(weight, 1)
./venv/lib64/python3.12/site-packages/networkx/algorithms/centrality/reaching.py:193:                return total_weight / d.get(weight, 1)
./venv/lib64/python3.12/site-packages/networkx/algorithms/centrality/eigenvector.py:183:                w = G[n][nbr].get(weight, 1) if weight else 1
./venv/lib64/python3.12/site-packages/networkx/algorithms/centrality/second_order.py:110:    if any(d.get(weight, 0) < 0 for u, v, d in G.edges(data=True)):
./venv/lib64/python3.12/site-packages/networkx/algorithms/centrality/current_flow_betweenness.py:159:                w = H[v][nbr].get(weight, 1.0)
./venv/lib64/python3.12/site-packages/networkx/algorithms/centrality/flow_matrix.py:24:        c = G[u][v].get(weight, 1.0)
./venv/lib64/python3.12/site-packages/networkx/algorithms/coloring/greedy_coloring.py:348:    strategy = STRATEGIES.get(strategy, strategy)
./venv/lib64/python3.12/site-packages/networkx/algorithms/tests/test_cycles.py:78:        cbH = [[perm.get(n, n) for n in cyc] for cyc in nx.cycle_basis(H)]
./venv/lib64/python3.12/site-packages/networkx/algorithms/tests/test_triads.py:231:        tc2 = {tt: sum(1 for t in tbt.get(tt, []) if n in t) for tt in tc1}
./venv/lib64/python3.12/site-packages/networkx/algorithms/tests/test_triads.py:238:            tt: sum(1 for t in tbt.get(tt, []) if any(n in ns for n in t)) for tt in tc1
./venv/lib64/python3.12/site-packages/networkx/algorithms/tests/test_triads.py:246:            tt: sum(1 for t in tbt.get(tt, []) if any(n in ns for n in t)) for tt in tc1
./venv/lib64/python3.12/site-packages/networkx/algorithms/tree/branchings.py:106:    return sum(edge[2].get(attr, default) for edge in G.edges(data=True))
./venv/lib64/python3.12/site-packages/networkx/algorithms/tree/branchings.py:156:    edges = [(u, v, data.get(attr, default)) for (u, v, data) in G.edges(data=True)]
./venv/lib64/python3.12/site-packages/networkx/algorithms/tree/branchings.py:275:        d = {attr: data.get(attr, default)}
./venv/lib64/python3.12/site-packages/networkx/algorithms/tree/branchings.py:622:        d[attr] = -d.get(attr, default)
./venv/lib64/python3.12/site-packages/networkx/algorithms/tree/branchings.py:628:        d[attr] = -d.get(attr, default)
./venv/lib64/python3.12/site-packages/networkx/algorithms/tree/branchings.py:632:        d[attr] = -d.get(attr, default)
./venv/lib64/python3.12/site-packages/networkx/algorithms/tree/branchings.py:685:        d[attr] = max_weight + 1 + (max_weight - min_weight) - d.get(attr, default)
./venv/lib64/python3.12/site-packages/networkx/algorithms/tree/branchings.py:692:        d[attr] = max_weight + 1 + (max_weight - min_weight) - d.get(attr, default)
./venv/lib64/python3.12/site-packages/networkx/algorithms/tree/branchings.py:696:        d[attr] = max_weight + 1 + (max_weight - min_weight) - d.get(attr, default)
./venv/lib64/python3.12/site-packages/networkx/algorithms/tree/branchings.py:725:        d[attr] = d.get(attr, default) - min_weight + 1 - (min_weight - max_weight)
./venv/lib64/python3.12/site-packages/networkx/algorithms/tree/branchings.py:731:        d[attr] = d.get(attr, default) + min_weight - 1 + (min_weight - max_weight)
./venv/lib64/python3.12/site-packages/networkx/algorithms/tree/branchings.py:735:        d[attr] = d.get(attr, default) + min_weight - 1 + (min_weight - max_weight)
./venv/lib64/python3.12/site-packages/networkx/algorithms/tree/distance_measures.py:213:    while max(total_size - sizes[root], sizes.get(hc, 0)) > total_size / 2:
./venv/lib64/python3.12/site-packages/networkx/algorithms/tree/tests/test_branchings.py:140:    edges = [(u, v, data.get(attr, default)) for (u, v, data) in G.edges(data=True)]
./venv/lib64/python3.12/site-packages/networkx/algorithms/tree/mst.py:94:            wt = e[-1].get(weight, 1) * sign
./venv/lib64/python3.12/site-packages/networkx/algorithms/tree/mst.py:205:        wt = d.get(weight, 1)
./venv/lib64/python3.12/site-packages/networkx/algorithms/tree/mst.py:297:                    wt = d.get(weight, 1) * sign
./venv/lib64/python3.12/site-packages/networkx/algorithms/tree/mst.py:306:                wt = d.get(weight, 1) * sign
./venv/lib64/python3.12/site-packages/networkx/algorithms/tree/mst.py:339:                        new_weight = d2.get(weight, 1) * sign
./venv/lib64/python3.12/site-packages/networkx/algorithms/tree/mst.py:350:                    new_weight = d2.get(weight, 1) * sign
./venv/lib64/python3.12/site-packages/networkx/algorithms/link_analysis/hits_alg.py:313:        x = np.array([nstart.get(n, 0) for n in list(G)], dtype=float)
./venv/lib64/python3.12/site-packages/networkx/algorithms/link_analysis/pagerank_alg.py:167:            x[n] += danglesum * dangling_weights.get(n, 0) + (1.0 - alpha) * p.get(n, 0)
./venv/lib64/python3.12/site-packages/networkx/algorithms/link_analysis/pagerank_alg.py:249:        p = np.array([personalization.get(n, 0) for n in nodelist], dtype=float)
./venv/lib64/python3.12/site-packages/networkx/algorithms/link_analysis/pagerank_alg.py:259:        dangling_weights = np.array([dangling.get(n, 0) for n in nodelist], dtype=float)
./venv/lib64/python3.12/site-packages/networkx/algorithms/link_analysis/pagerank_alg.py:470:        x = np.array([nstart.get(n, 0) for n in nodelist], dtype=float)
./venv/lib64/python3.12/site-packages/networkx/algorithms/link_analysis/pagerank_alg.py:477:        p = np.array([personalization.get(n, 0) for n in nodelist], dtype=float)
./venv/lib64/python3.12/site-packages/networkx/algorithms/link_analysis/pagerank_alg.py:486:        dangling_weights = np.array([dangling.get(n, 0) for n in nodelist], dtype=float)
./venv/lib64/python3.12/site-packages/networkx/algorithms/minors/contraction.py:393:            return {"weight": sum(d.get(weight, 1) for d in edgedata)}
./venv/lib64/python3.12/site-packages/networkx/algorithms/cluster.py:134:        max_weight = max(d.get(weight, 1) for u, v, d in G.edges(data=True))
./venv/lib64/python3.12/site-packages/networkx/algorithms/cluster.py:141:        return G[u][v].get(weight, 1) / max_weight
./venv/lib64/python3.12/site-packages/networkx/algorithms/cluster.py:209:        max_weight = max(d.get(weight, 1) for u, v, d in G.edges(data=True))
./venv/lib64/python3.12/site-packages/networkx/algorithms/cluster.py:214:        return G[u][v].get(weight, 1) / max_weight
./venv/lib64/python3.12/site-packages/networkx/algorithms/cluster.py:315:            v_id = node_to_id.get(v, -1)
./venv/lib64/python3.12/site-packages/networkx/algorithms/cluster.py:320:                if node_to_id.get(w, -1) > v_id:
./venv/lib64/python3.12/site-packages/networkx/algorithms/cycles.py:453:            elif len(path) < lock.get(w, length_bound):
./venv/lib64/python3.12/site-packages/networkx/algorithms/cycles.py:469:                    if lock.get(u, length_bound) < length_bound - bl + 1:
./venv/lib64/python3.12/site-packages/networkx/algorithms/cycles.py:578:        yield from ([v] for v, Gv in G.adj.items() if len(Gv.get(v, ())) == 1)
./venv/lib64/python3.12/site-packages/networkx/algorithms/flow/utils.py:118:        if u != v and attr.get(capacity, inf) > 0
./venv/lib64/python3.12/site-packages/networkx/algorithms/flow/utils.py:141:            r = min(attr.get(capacity, inf), inf)
./venv/lib64/python3.12/site-packages/networkx/algorithms/flow/utils.py:153:            r = min(attr.get(capacity, inf), inf)
./venv/lib64/python3.12/site-packages/networkx/algorithms/flow/capacityscaling.py:44:    if sum(G.nodes[u].get(demand, 0) for u in G) != 0:
./venv/lib64/python3.12/site-packages/networkx/algorithms/flow/capacityscaling.py:49:        (u, {"excess": -G.nodes[u].get(demand, 0), "potential": 0}) for u in G
./venv/lib64/python3.12/site-packages/networkx/algorithms/flow/capacityscaling.py:55:        if e.get(weight, 0) < 0 and e.get(capacity, inf) == inf:
./venv/lib64/python3.12/site-packages/networkx/algorithms/flow/capacityscaling.py:66:            if u != v and e.get(capacity, inf) > 0
./venv/lib64/python3.12/site-packages/networkx/algorithms/flow/capacityscaling.py:72:            if u != v and e.get(capacity, inf) > 0
./venv/lib64/python3.12/site-packages/networkx/algorithms/flow/capacityscaling.py:92:        r = min(e.get(capacity, inf), inf)
./venv/lib64/python3.12/site-packages/networkx/algorithms/flow/capacityscaling.py:93:        w = e.get(weight, 0)
./venv/lib64/python3.12/site-packages/networkx/algorithms/flow/capacityscaling.py:121:                            u != v or e.get(capacity, inf) <= 0 or e.get(weight, 0) >= 0
./venv/lib64/python3.12/site-packages/networkx/algorithms/flow/capacityscaling.py:138:                    if (u != v or e.get(capacity, inf) <= 0 or e.get(weight, 0) >= 0)
./venv/lib64/python3.12/site-packages/networkx/algorithms/flow/capacityscaling.py:291:        if e.get(capacity, inf) <= 0 or e.get(weight, 0) >= 0
./venv/lib64/python3.12/site-packages/networkx/algorithms/flow/networksimplex.py:22:            G.nodes[u].get(demand, 0) for u in self.node_list
./venv/lib64/python3.12/site-packages/networkx/algorithms/flow/networksimplex.py:39:        edges = (e for e in edges if e[0] != e[1] and e[-1].get(capacity, inf) != 0)
./venv/lib64/python3.12/site-packages/networkx/algorithms/flow/networksimplex.py:46:            self.edge_capacities.append(e[-1].get(capacity, inf))
./venv/lib64/python3.12/site-packages/networkx/algorithms/flow/networksimplex.py:47:            self.edge_weights.append(e[-1].get(weight, 0))
./venv/lib64/python3.12/site-packages/networkx/algorithms/flow/networksimplex.py:524:        if abs(e[-1].get(weight, 0)) == inf:
./venv/lib64/python3.12/site-packages/networkx/algorithms/flow/networksimplex.py:541:        if e[-1].get(capacity, inf) < 0:
./venv/lib64/python3.12/site-packages/networkx/algorithms/flow/networksimplex.py:608:        e[-1].get(capacity, inf) == inf and e[-1].get(weight, 0) < 0
./venv/lib64/python3.12/site-packages/networkx/algorithms/flow/networksimplex.py:651:            if e[-1].get(capacity, inf) == 0:
./venv/lib64/python3.12/site-packages/networkx/algorithms/flow/networksimplex.py:654:            w = e[-1].get(weight, 0)
./venv/lib64/python3.12/site-packages/networkx/algorithms/flow/mincost.py:252:    return sum((flowDict[u][v] * d.get(weight, 0) for u, v, d in G.edges(data=True)))
./venv/lib64/python3.12/site-packages/networkx/algorithms/isomorphism/matchhelpers.py:78:            return data1.get(attr, default) == data2.get(attr, default)
./venv/lib64/python3.12/site-packages/networkx/algorithms/isomorphism/matchhelpers.py:84:            return all(data1.get(attr, d) == data2.get(attr, d) for attr, d in attrs)
./venv/lib64/python3.12/site-packages/networkx/algorithms/isomorphism/matchhelpers.py:96:            values1 = {data.get(attr, default) for data in datasets1.values()}
./venv/lib64/python3.12/site-packages/networkx/algorithms/isomorphism/matchhelpers.py:97:            values2 = {data.get(attr, default) for data in datasets2.values()}
./venv/lib64/python3.12/site-packages/networkx/algorithms/isomorphism/matchhelpers.py:106:                x = tuple(data1.get(attr, d) for attr, d in attrs)
./venv/lib64/python3.12/site-packages/networkx/algorithms/isomorphism/matchhelpers.py:110:                x = tuple(data2.get(attr, d) for attr, d in attrs)
./venv/lib64/python3.12/site-packages/networkx/algorithms/isomorphism/matchhelpers.py:164:                data1.get(attr, default),
./venv/lib64/python3.12/site-packages/networkx/algorithms/isomorphism/matchhelpers.py:165:                data2.get(attr, default),
./venv/lib64/python3.12/site-packages/networkx/algorithms/isomorphism/matchhelpers.py:174:            values1 = [data1.get(attr, d) for attr, d in attrs]
./venv/lib64/python3.12/site-packages/networkx/algorithms/isomorphism/matchhelpers.py:175:            values2 = [data2.get(attr, d) for attr, d in attrs]
./venv/lib64/python3.12/site-packages/networkx/algorithms/isomorphism/matchhelpers.py:188:            values1 = sorted(data.get(attr, default) for data in datasets1.values())
./venv/lib64/python3.12/site-packages/networkx/algorithms/isomorphism/matchhelpers.py:189:            values2 = sorted(data.get(attr, default) for data in datasets2.values())
./venv/lib64/python3.12/site-packages/networkx/algorithms/isomorphism/matchhelpers.py:198:                x = tuple(data1.get(attr, d) for attr, d in attrs)
./venv/lib64/python3.12/site-packages/networkx/algorithms/isomorphism/matchhelpers.py:202:                x = tuple(data2.get(attr, d) for attr, d in attrs)
./venv/lib64/python3.12/site-packages/networkx/algorithms/isomorphism/matchhelpers.py:263:            return op(data1.get(attr, default), data2.get(attr, default))
./venv/lib64/python3.12/site-packages/networkx/algorithms/isomorphism/matchhelpers.py:270:                if not operator(data1.get(attr, d), data2.get(attr, d)):
./venv/lib64/python3.12/site-packages/networkx/algorithms/isomorphism/matchhelpers.py:329:            x = tuple(data1.get(attr, d) for attr, d in attrs)
./venv/lib64/python3.12/site-packages/networkx/algorithms/isomorphism/matchhelpers.py:333:            x = tuple(data2.get(attr, d) for attr, d in attrs)
./venv/lib64/python3.12/site-packages/networkx/algorithms/assortativity/mixing.py:247:        v = d[x].get(y, 0)
./venv/lib64/python3.12/site-packages/networkx/algorithms/assortativity/connectivity.py:115:                s = sum(G[nbr][n].get(weight, 1) * d for nbr, d in nbrdeg)
./venv/lib64/python3.12/site-packages/networkx/algorithms/assortativity/connectivity.py:117:                s = sum(G[n][nbr].get(weight, 1) * d for nbr, d in nbrdeg)
./venv/lib64/python3.12/site-packages/networkx/algorithms/assortativity/neighbor_degree.py:157:                sum(dd.get(weight, 1) * t_deg[nbr] for nbr, dd in G_S[n].items())
./venv/lib64/python3.12/site-packages/networkx/algorithms/assortativity/neighbor_degree.py:158:                + sum(dd.get(weight, 1) * t_deg[nbr] for nbr, dd in G_P[n].items())
./venv/lib64/python3.12/site-packages/networkx/algorithms/assortativity/pairs.py:56:        uattr = Gnodes[u].get(attribute, None)
./venv/lib64/python3.12/site-packages/networkx/algorithms/assortativity/pairs.py:59:                vattr = Gnodes[v].get(attribute, None)
./venv/lib64/python3.12/site-packages/networkx/algorithms/assortativity/pairs.py:64:                vattr = Gnodes[v].get(attribute, None)
./venv/lib64/python3.12/site-packages/networkx/algorithms/matching.py:433:        wt = d.get(weight, 1)
./venv/lib64/python3.12/site-packages/networkx/algorithms/matching.py:509:        return dualvar[v] + dualvar[w] - 2 * G[v][w].get(weight, 1)
./venv/lib64/python3.12/site-packages/networkx/algorithms/matching.py:897:            wt = d.get(weight, 1)
./venv/lib64/python3.12/site-packages/networkx/relabel.py:195:    H.add_nodes_from(mapping.get(n, n) for n in G)
./venv/lib64/python3.12/site-packages/networkx/relabel.py:196:    H._node.update((mapping.get(n, n), d.copy()) for n, d in G.nodes.items())
./venv/lib64/python3.12/site-packages/networkx/relabel.py:199:            (mapping.get(n1, n1), mapping.get(n2, n2), k, d.copy())
./venv/lib64/python3.12/site-packages/networkx/relabel.py:219:            (mapping.get(n1, n1), mapping.get(n2, n2), d.copy())
./venv/lib64/python3.12/site-packages/networkx/generators/stochastic.py:52:            d[weight] = d.get(weight, 1) / degree[u]
./venv/lib64/python3.12/site-packages/networkx/drawing/layout.py:1725:        mass[idx] = node_mass.get(node, G.degree(node) + 1)
./venv/lib64/python3.12/site-packages/networkx/drawing/layout.py:1726:        size[idx] = node_size.get(node, 1)
./venv/lib64/python3.12/site-packages/networkx/drawing/nx_pylab.py:605:        attr = kwargs.get(param_name, attr)
./venv/lib64/python3.12/site-packages/networkx/drawing/nx_pylab.py:623:        return [node_subgraph.nodes[n].get(attr, default) for n in seq]
./venv/lib64/python3.12/site-packages/networkx/drawing/nx_pylab.py:665:        attr = kwargs.get(param_name, attr)
./venv/lib64/python3.12/site-packages/networkx/drawing/nx_pylab.py:680:        return [edge_subgraph.edges[e].get(attr, default) for e in seq]
./venv/lib64/python3.12/site-packages/networkx/drawing/nx_pylab.py:687:        attr = kwargs.get(param_name, attr)
./venv/lib64/python3.12/site-packages/networkx/drawing/nx_pylab.py:699:        return edge_subgraph.edges[e].get(attr, default)
./venv/lib64/python3.12/site-packages/networkx/drawing/nx_pylab.py:707:        attr = kwargs.get(param_name, attr)
./venv/lib64/python3.12/site-packages/networkx/drawing/nx_pylab.py:719:        return subgraph.nodes[n].get(attr, default)
./venv/lib64/python3.12/site-packages/networkx/linalg/algebraicconnectivity.py:114:            ((u, v, e.get(weight, 1.0)) for u, v, e in G.edges(data=True) if u != v),
./venv/lib64/python3.12/site-packages/networkx/linalg/algebraicconnectivity.py:120:            (u, v, abs(e.get(weight, 1.0))) for u, v, e in G.edges(data=True) if u != v
./venv/lib64/python3.12/site-packages/networkx/linalg/algebraicconnectivity.py:124:            (u, v, sum(abs(e.get(weight, 1.0)) for e in G[u][v].values()))
./venv/lib64/python3.12/site-packages/networkx/linalg/attrmatrix.py:107:                    return sum(d.get(edge_attr, 1) for d in G[u][v].values())
./venv/lib64/python3.12/site-packages/networkx/linalg/attrmatrix.py:112:                    return G[u][v].get(edge_attr, 1)
./venv/lib64/python3.12/site-packages/networkx/linalg/graphmatrix.py:96:                wt = G[u][v][ekey].get(weight, 1)
./venv/lib64/python3.12/site-packages/networkx/linalg/graphmatrix.py:98:                wt = G[u][v].get(weight, 1)
./venv/lib64/python3.12/site-packages/networkx/readwrite/pajek.py:54:        na = G.nodes.get(n, {}).copy()
./venv/lib64/python3.12/site-packages/networkx/readwrite/pajek.py:248:                u = nodelabels.get(ui, ui)
./venv/lib64/python3.12/site-packages/networkx/readwrite/pajek.py:249:                v = nodelabels.get(vi, vi)
./venv/lib64/python3.12/site-packages/networkx/readwrite/json_graph/node_link.py:244:        node = _to_tuple(d.get(name, next(c)))
./venv/lib64/python3.12/site-packages/networkx/readwrite/json_graph/node_link.py:254:            ky = d.get(key, None)
./venv/lib64/python3.12/site-packages/networkx/readwrite/json_graph/tree.py:124:            grandchildren = data.get(children, [])
./venv/lib64/python3.12/site-packages/networkx/readwrite/json_graph/tree.py:133:    children_ = data.get(children, [])
./venv/lib64/python3.12/site-packages/networkx/readwrite/text.py:330:                    label = str(graph.nodes[node].get(label_attr, node))
./venv/lib64/python3.12/site-packages/networkx/readwrite/text.py:336:                    collapse = graph.nodes[node].get(collapse_attr, False)
./venv/lib64/python3.12/site-packages/networkx/readwrite/text.py:382:                                str(graph.nodes[p].get(label_attr, p))
./venv/lib64/python3.12/site-packages/networkx/utils/heaps.py:320:        return self._dict.get(key, default)
./venv/lib64/python3.12/site-packages/networkx/utils/backends.py:1233:                edge_attr: bound.arguments.get(val, 1) if isinstance(val, str) else val
./venv/lib64/python3.12/site-packages/networkx/utils/backends.py:1328:                    edges = preserve_edge_attrs.get(gname, edge_attrs)
./venv/lib64/python3.12/site-packages/networkx/utils/backends.py:1334:                    nodes = preserve_node_attrs.get(gname, node_attrs)
./venv/lib64/python3.12/site-packages/networkx/utils/backends.py:2025:        cache = cache.get("backends", {}).get(backend_name, {})
./venv/lib64/python3.12/site-packages/networkx/tests/test_relabel.py:325:        assert [mapping.get(i, i) for i in original_order] == new_order
./venv/lib64/python3.12/site-packages/networkx/tests/test_relabel.py:333:        assert [mapping.get(i, i) for i in original_order] == new_order
./venv/lib64/python3.12/site-packages/networkx/tests/test_relabel.py:341:        assert [mapping.get(i, i) for i in original_order] == new_order
./venv/lib64/python3.12/site-packages/networkx/tests/test_relabel.py:349:        assert [mapping.get(i, i) for i in original_order] != new_order
./venv/lib64/python3.12/site-packages/networkx/classes/multidigraph.py:512:            datadict = keydict.get(key, self.edge_attr_dict_factory())
./venv/lib64/python3.12/site-packages/networkx/classes/reportviews.py:79:    Otherwise iterate over `(u, v, datadict.get(data, default))`.
./venv/lib64/python3.12/site-packages/networkx/classes/reportviews.py:448:        return sum(dd.get(weight, 1) for dd in succs.values()) + sum(
./venv/lib64/python3.12/site-packages/networkx/classes/reportviews.py:449:            dd.get(weight, 1) for dd in preds.values()
./venv/lib64/python3.12/site-packages/networkx/classes/reportviews.py:463:                deg = sum(dd.get(weight, 1) for dd in succs.values()) + sum(
./venv/lib64/python3.12/site-packages/networkx/classes/reportviews.py:464:                    dd.get(weight, 1) for dd in preds.values()
./venv/lib64/python3.12/site-packages/networkx/classes/reportviews.py:527:        return sum(dd.get(weight, 1) for dd in nbrs.values()) + (
./venv/lib64/python3.12/site-packages/networkx/classes/reportviews.py:528:            n in nbrs and nbrs[n].get(weight, 1)
./venv/lib64/python3.12/site-packages/networkx/classes/reportviews.py:540:                deg = sum(dd.get(weight, 1) for dd in nbrs.values()) + (
./venv/lib64/python3.12/site-packages/networkx/classes/reportviews.py:541:                    n in nbrs and nbrs[n].get(weight, 1)
./venv/lib64/python3.12/site-packages/networkx/classes/reportviews.py:565:                deg = sum(dd.get(weight, 1) for dd in succs.values())
./venv/lib64/python3.12/site-packages/networkx/classes/reportviews.py:577:        return sum(dd.get(weight, 1) for dd in nbrs.values())
./venv/lib64/python3.12/site-packages/networkx/classes/reportviews.py:588:                deg = sum(dd.get(weight, 1) for dd in preds.values())
./venv/lib64/python3.12/site-packages/networkx/classes/reportviews.py:604:            d.get(weight, 1) for key_dict in nbrs.values() for d in key_dict.values()
./venv/lib64/python3.12/site-packages/networkx/classes/reportviews.py:607:            deg += sum(d.get(weight, 1) for d in nbrs[n].values())
./venv/lib64/python3.12/site-packages/networkx/classes/reportviews.py:623:                    d.get(weight, 1)
./venv/lib64/python3.12/site-packages/networkx/classes/reportviews.py:628:                    deg += sum(d.get(weight, 1) for d in nbrs[n].values())
./venv/lib64/python3.12/site-packages/networkx/classes/reportviews.py:645:            d.get(weight, 1) for key_dict in succs.values() for d in key_dict.values()
./venv/lib64/python3.12/site-packages/networkx/classes/reportviews.py:647:            d.get(weight, 1) for key_dict in preds.values() for d in key_dict.values()
./venv/lib64/python3.12/site-packages/networkx/classes/reportviews.py:666:                    d.get(weight, 1)
./venv/lib64/python3.12/site-packages/networkx/classes/reportviews.py:670:                    d.get(weight, 1)
./venv/lib64/python3.12/site-packages/networkx/classes/reportviews.py:687:            d.get(weight, 1) for key_dict in nbrs.values() for d in key_dict.values()
./venv/lib64/python3.12/site-packages/networkx/classes/reportviews.py:701:                    d.get(weight, 1)
./venv/lib64/python3.12/site-packages/networkx/classes/reportviews.py:718:            d.get(weight, 1) for key_dict in nbrs.values() for d in key_dict.values()
./venv/lib64/python3.12/site-packages/networkx/classes/reportviews.py:732:                    d.get(weight, 1)
./venv/lib64/python3.12/site-packages/networkx/classes/reportviews.py:1212:    Otherwise iterate over `(u, v, datadict.get(data, default))`.
./venv/lib64/python3.12/site-packages/networkx/classes/graph.py:980:        datadict = self._adj[u].get(v, self.edge_attr_dict_factory())
./venv/lib64/python3.12/site-packages/networkx/classes/graph.py:1060:            datadict = self._adj[u].get(v, self.edge_attr_dict_factory())
./venv/lib64/python3.12/site-packages/networkx/classes/function.py:161:    return [counts.get(i, 0) for i in range(max(counts) + 1 if counts else 0)]
./venv/lib64/python3.12/site-packages/networkx/classes/function.py:705:        return {n: d.get(name, default) for n, d in G.nodes.items()}
./venv/lib64/python3.12/site-packages/networkx/classes/function.py:924:        return {x[:-1]: x[-1].get(name, default) for x in edges}
./venv/lib64/python3.12/site-packages/networkx/classes/function.py:1322:                    (n, n, k, d.get(data, default))
./venv/lib64/python3.12/site-packages/networkx/classes/function.py:1329:                    (n, n, d.get(data, default))
./venv/lib64/python3.12/site-packages/networkx/classes/function.py:1336:                (n, n, nbrs[n].get(data, default))
./venv/lib64/python3.12/site-packages/networkx/classes/tests/dispatch_interface.py:124:                    (attr, graph._node[n].get(attr, default))
./venv/lib64/python3.12/site-packages/networkx/classes/tests/dispatch_interface.py:138:                    (attr, old_dd.get(attr, default))
./venv/lib64/python3.12/site-packages/networkx/classes/multigraph.py:524:            datadict = keydict.get(key, self.edge_attr_dict_factory())
./venv/lib64/python3.12/site-packages/networkx/classes/digraph.py:742:        datadict = self._adj[u].get(v, self.edge_attr_dict_factory())
./venv/lib64/python3.12/site-packages/networkx/classes/digraph.py:824:            datadict = self._adj[u].get(v, self.edge_attr_dict_factory())
./venv/lib64/python3.12/site-packages/requests/utils.py:874:        proxy = environ_proxies.get(scheme, environ_proxies.get("all"))
./venv/lib64/python3.12/site-packages/requests/structures.py:96:        return self.__dict__.get(key, None)
./venv/lib64/python3.12/site-packages/requests/structures.py:99:        return self.__dict__.get(key, default)
./venv/lib64/python3.12/site-packages/requests/cookies.py:76:        return self._r.headers.get(name, self._new_headers.get(name, default))
./venv/lib64/python3.12/site-packages/urllib3/response.py:679:        return self.headers.get(name, default)
./venv/lib64/python3.12/site-packages/urllib3/connectionpool.py:1130:    port = port or port_by_scheme.get(scheme, 80)
./venv/lib64/python3.12/site-packages/urllib3/fields.py:299:            if self.headers.get(sort_key, False):
./venv/lib64/python3.12/site-packages/pydantic/_internal/_model_construction.py:57:        existing: Any = self.get(k, None)
./venv/lib64/python3.12/site-packages/pydantic/_internal/_generate_schema.py:1551:                        default=namedtuple_cls._field_defaults.get(field_name, Parameter.empty),
./venv/lib64/python3.12/site-packages/pydantic/_internal/_generics.py:339:    return type_map.get(type_, type_)
./venv/lib64/python3.12/site-packages/pydantic/_internal/_utils.py:394:        return self.wrapped.get(key, _SENTINEL)
./venv/lib64/python3.12/site-packages/pydantic/_internal/_decorators.py:379:            attribute = base.__dict__.get(name, _sentinel)
./venv/lib64/python3.12/site-packages/pydantic/mypy.py:208:                setting = config.get(key, False)
./venv/lib64/python3.12/site-packages/pydantic/v1/class_validators.py:168:        validators = self.validators.get(name, [])
./venv/lib64/python3.12/site-packages/pydantic/v1/generics.py:242:                        key: typevars_map.get(value, value) for key, value in _assigned_parameters[cls].items()
./venv/lib64/python3.12/site-packages/pydantic/v1/generics.py:274:        return type_map.get(type_, type_)
./venv/lib64/python3.12/site-packages/pydantic/v1/generics.py:325:    new_type = type_map.get(type_, type_)
./venv/lib64/python3.12/site-packages/pydantic/v1/main.py:183:                elif is_finalvar_with_default_val(ann_type, namespace.get(ann_name, Undefined)):
./venv/lib64/python3.12/site-packages/pydantic/v1/main.py:187:                    value = namespace.get(ann_name, Undefined)
./venv/lib64/python3.12/site-packages/pydantic/v1/main.py:224:                        annotation=annotations.get(var_name, Undefined),
./venv/lib64/python3.12/site-packages/pydantic/v1/main.py:379:            known_field = self.__fields__.get(name, None)
./venv/lib64/python3.12/site-packages/pydantic/v1/mypy.py:247:                setting = config.get(key, False)
./venv/lib64/python3.12/site-packages/pydantic/v1/dataclasses.py:456:        known_field = self.__pydantic_model__.__fields__.get(name, None)
./venv/lib64/python3.12/site-packages/pydantic/v1/fields.py:187:        return [(a, v) for a, v in attrs if v != field_defaults_to_hide.get(a, None)]
./venv/lib64/python3.12/site-packages/pydantic/v1/fields.py:209:                if current_value is self.__field_constraints__.get(attr_name, None):
./venv/lib64/python3.12/site-packages/pydantic/json_schema.py:190:        return self.defs_remapping.get(ref, ref)
./venv/lib64/python3.12/site-packages/pydantic/json_schema.py:193:        return self.json_remapping.get(ref, ref)
./venv/lib64/python3.12/site-packages/pydantic/json_schema.py:2311:            return self.definitions.get(def_ref, None)
./venv/lib64/python3.12/site-packages/mpmath/functions/bessel.py:390:        p,v = cache.get(name, (-1,0))
./venv/lib64/python3.12/site-packages/mpmath/ctx_mp_python.py:1010:        f.__doc__ = function_docs.__dict__.get(name, "Computes the %s of x" % doc)
./venv/lib64/python3.12/site-packages/mpmath/ctx_mp_python.py:1029:        f_wrapped.__doc__ = function_docs.__dict__.get(name, f.__doc__)
./venv/lib64/python3.12/site-packages/mpmath/ctx_fp.py:60:        f_wrapped.__doc__ = function_docs.__dict__.get(name, f.__doc__)
./venv/lib64/python3.12/site-packages/uvicorn/logging.py:49:        func = self.level_name_colors.get(level_no, default)
./venv/lib64/python3.12/site-packages/triton/runtime/jit.py:165:            val = self.globals.get(name, None)
./venv/lib64/python3.12/site-packages/triton/runtime/jit.py:168:            val = self.nonlocals.get(name, None)
./venv/lib64/python3.12/site-packages/triton/runtime/jit.py:565:    cache_key = kernel_key_cache.get(key, None)
./venv/lib64/python3.12/site-packages/triton/runtime/jit.py:713:        kernel = kernel_cache.get(key, None)
./venv/lib64/python3.12/site-packages/triton/runtime/jit.py:727:            if (newVal := globals_dict.get(name, not_present)) != val:
./venv/lib64/python3.12/site-packages/triton/compiler/code_generator.py:271:            attr_specs = self.attrs.get(path, [])
./venv/lib64/python3.12/site-packages/triton/compiler/code_generator.py:370:        val = self.gscope.get(name, absent_marker)
./venv/lib64/python3.12/site-packages/triton/compiler/code_generator.py:383:            return self.lscope.get(name, absent)
./venv/lib64/python3.12/site-packages/triton/compiler/code_generator.py:386:            val = self.gscope.get(name, absent)
./venv/lib64/python3.12/site-packages/markdown_it/rules_inline/backticks.py:26:    if state.backticksScanned and state.backticks.get(openerLength, 0) <= start:
./venv/lib64/python3.12/site-packages/markdown_it/rules_inline/link.py:115:        ref = state.env["references"].get(label, None)
./venv/lib64/python3.12/site-packages/markdown_it/rules_inline/image.py:116:        ref = state.env["references"].get(label, None)
./venv/lib64/python3.12/site-packages/markdown_it/ruler.py:267:        return self.__cache__.get(chainName, []) or []
./venv/lib64/python3.12/site-packages/markdown_it/token.py:104:        return self.attrs.get(name, None)
./venv/lib64/python3.12/site-packages/h11/_state.py:349:            changes = STATE_TRIGGERED_TRANSITIONS.get(joint_state, {})
./venv/lib64/python3.12/site-packages/rich/_emoji_replace.py:21:    default_variant_code = variants.get(default_variant, "") if default_variant else ""
./venv/lib64/python3.12/site-packages/rich/emoji.py:50:            self._char += self.VARIANTS.get(variant, "")
./venv/lib64/python3.12/site-packages/rich/padding.py:87:                Measurement.get(console, options, self.renderable).maximum
./venv/lib64/python3.12/site-packages/rich/padding.py:132:        measure_min, measure_max = Measurement.get(console, options, self.renderable)
./venv/lib64/python3.12/site-packages/rich/styled.py:34:        return Measurement.get(console, options, self.renderable)
./venv/lib64/python3.12/site-packages/rich/align.py:238:        measurement = Measurement.get(console, options, self.renderable)
./venv/lib64/python3.12/site-packages/rich/align.py:295:        measurement = Measurement.get(console, options, self.renderable)
./venv/lib64/python3.12/site-packages/rich/spinner.py:59:        return Measurement.get(console, options, text)
./venv/lib64/python3.12/site-packages/rich/console.py:816:            color_system = _TERM_COLORS.get(colors, ColorSystem.STANDARD)
./venv/lib64/python3.12/site-packages/rich/console.py:1297:        measurement = Measurement.get(self, options or self.options, renderable)
./venv/lib64/python3.12/site-packages/rich/containers.py:50:            Measurement.get(console, options, renderable)
./venv/lib64/python3.12/site-packages/rich/box.py:80:            box = LEGACY_WINDOWS_SUBSTITUTIONS.get(box, box)
./venv/lib64/python3.12/site-packages/rich/box.py:93:        return PLAIN_HEADED_SUBSTITUTIONS.get(self, self)
./venv/lib64/python3.12/site-packages/rich/constrain.py:36:        measurement = Measurement.get(console, options, self.renderable)
./venv/lib64/python3.12/site-packages/typer/rich_utils.py:594:    default_arguments = panel_to_arguments.get(ARGUMENTS_PANEL_TITLE, [])
./venv/lib64/python3.12/site-packages/typer/rich_utils.py:613:    default_options = panel_to_options.get(OPTIONS_PANEL_TITLE, [])
./venv/lib64/python3.12/site-packages/typer/rich_utils.py:655:        default_commands = panel_to_commands.get(COMMANDS_PANEL_TITLE, [])
./venv/lib64/python3.12/site-packages/typer/core.py:371:                rich_markup_mode = ctx.obj.get(MARKUP_MODE_KEY, None)
./venv/lib64/python3.12/site-packages/typer/core.py:593:                rich_markup_mode = ctx.obj.get(MARKUP_MODE_KEY, None)
./venv/lib64/python3.12/site-packages/typer/cli.py:204:        rich_markup_mode = ctx.obj.get(MARKUP_MODE_KEY, None)
./venv/lib64/python3.12/site-packages/httpx/_models.py:827:        error_type = error_types.get(status_class, "Invalid status code")
./venv/lib64/python3.12/site-packages/click/core.py:555:                return get_current_context().meta.get(LANG_KEY, 'en_US')
./venv/lib64/python3.12/site-packages/click/core.py:709:            value = self.default_map.get(name, UNSET)
./venv/lib64/python3.12/site-packages/click/formatting.py:19:            widths[idx] = max(widths.get(idx, 0), term_len(col))
./venv/lib64/python3.12/site-packages/setuptools/_vendor/packaging/version.py:705:        letter = _LETTER_NORMALIZATION.get(letter, letter)
./venv/lib64/python3.12/site-packages/setuptools/_vendor/packaging/tags.py:581:    archs = {"armv8l": ["armv8l", "armv7l"]}.get(arch, [arch])
./venv/lib64/python3.12/site-packages/setuptools/_vendor/platformdirs/unix.py:238:        media_dir = os.environ.get(env_var, "").strip()
./venv/lib64/python3.12/site-packages/setuptools/command/build_clib.py:67:                extra_deps = obj_deps.get(source, list())
./venv/lib64/python3.12/site-packages/setuptools/command/build_py.py:136:            self.manifest_files.get(package, []),
./venv/lib64/python3.12/site-packages/setuptools/command/build_py.py:311:            spec.get(package, []),
./venv/lib64/python3.12/site-packages/setuptools/dist.py:356:            vars(self.metadata).setdefault(option, attrs.get(option, default()))
./venv/lib64/python3.12/site-packages/setuptools/dist.py:598:                    val = parser.get(section, opt)
./venv/lib64/python3.12/site-packages/setuptools/config/pyprojecttoml.py:202:        package_data = self.setuptools_cfg.get(field, {})
./venv/lib64/python3.12/site-packages/setuptools/config/setupcfg.py:284:        option_name = self.aliases.get(option_name, option_name)
./venv/lib64/python3.12/site-packages/setuptools/config/setupcfg.py:296:            parsed = self.parsers.get(option_name, lambda x: x)(value)
./venv/lib64/python3.12/site-packages/setuptools/config/_apply_pyprojecttoml.py:80:        corresp = PYPROJECT_CORRESPONDENCE.get(norm_key, norm_key)
./venv/lib64/python3.12/site-packages/setuptools/config/_apply_pyprojecttoml.py:119:        norm_key = TOOL_TABLE_RENAMES.get(norm_key, norm_key)
./venv/lib64/python3.12/site-packages/setuptools/config/_apply_pyprojecttoml.py:120:        corresp = TOOL_TABLE_CORRESPONDENCE.get(norm_key, norm_key)
./venv/lib64/python3.12/site-packages/setuptools/config/_apply_pyprojecttoml.py:146:    val = _PREPROCESS.get(field, _noop)(dist, value)
./venv/lib64/python3.12/site-packages/setuptools/config/_apply_pyprojecttoml.py:312:        valid = valid_options.get(cmd, set())
./venv/lib64/python3.12/site-packages/setuptools/config/_apply_pyprojecttoml.py:334:        opts = valid_options.get(cmd, set())
./venv/lib64/python3.12/site-packages/setuptools/config/_validate_pyproject/error_reporting.py:212:            return [self.jargon.get(t, t) for t in term]
./venv/lib64/python3.12/site-packages/setuptools/config/_validate_pyproject/error_reporting.py:213:        return self.jargon.get(term, term)
./venv/lib64/python3.12/site-packages/setuptools/msvc.py:1550:        env_paths = environ.get(name, '').split(os.pathsep)
./venv/lib64/python3.12/site-packages/setuptools/tests/integration/test_pip_install_sdist.py:138:    env = EXTRA_ENV_VARS.get(package, {})
./venv/lib64/python3.12/site-packages/setuptools/tests/integration/test_pip_install_sdist.py:143:    pkg = IMPORT_NAME.get(package, package).replace("-", "_")
./venv/lib64/python3.12/site-packages/setuptools/tests/integration/test_pip_install_sdist.py:211:    deps += EXTRA_BUILD_DEPS.get(package, [])
./venv/lib64/python3.12/site-packages/setuptools/tests/test_core_metadata.py:308:        val = attrs.get(dkey, None)
./venv/lib64/python3.12/site-packages/setuptools/_distutils/command/install.py:116:            **INSTALL_SCHEMES.get(scheme, {}),
./venv/lib64/python3.12/site-packages/setuptools/_distutils/command/install.py:117:            **sysconfig_schemes.get(scheme, {}),
./venv/lib64/python3.12/site-packages/setuptools/_distutils/command/build_py.py:125:        globs = self.package_data.get('', []) + self.package_data.get(package, [])
./venv/lib64/python3.12/site-packages/setuptools/_distutils/dist.py:430:                        val = parser.get(section, opt)
./venv/lib64/python3.12/site-packages/setuptools/_distutils/archive_util.py:96:    archive_name += compress_ext.get(compress, '')
./venv/lib64/python3.12/site-packages/setuptools/_distutils/compilers/C/zos.py:114:            if (binary := os.environ.get(envvar, None))
./venv/lib64/python3.12/site-packages/torchgen/gen.py:1933:        grouped_functions = grouped_functions_by_root_name.get(name, [])
./venv/lib64/python3.12/site-packages/torchgen/gen.py:1994:            grouped_functions = grouped_functions_by_root_name.get(name, [])
./venv/lib64/python3.12/site-packages/torchgen/selective_build/selector.py:316:        merge_et_kernel_metadata[op].update(lhs.get(op, []))
./venv/lib64/python3.12/site-packages/torchgen/selective_build/selector.py:317:        merge_et_kernel_metadata[op].update(rhs.get(op, []))
./venv/lib64/python3.12/site-packages/torchgen/packaged/autograd/gen_variable_type.py:1065:    fw_derivatives = fn.fw_derivatives.get(key, []) if fn.fw_derivatives else []
./venv/lib64/python3.12/site-packages/torchgen/packaged/autograd/gen_variable_type.py:1637:            aliased_arg_name = ALL_VIEW_FUNCTIONS.get(base_name, None)
./venv/lib64/python3.12/site-packages/torchgen/packaged/autograd/gen_trace_type.py:124:        trace_name = RENAME_TRACE.get(trace_name, trace_name)
./venv/lib64/python3.12/site-packages/torchgen/packaged/autograd/gen_trace_type.py:131:    outplace_trace_name = RENAME_TRACE.get(outplace_trace_name, outplace_trace_name)
./venv/lib64/python3.12/site-packages/torchgen/packaged/autograd/gen_trace_type.py:132:    inplace_trace_name = RENAME_TRACE.get(inplace_trace_name, inplace_trace_name)
./venv/lib64/python3.12/site-packages/torchgen/api/python.py:1168:                }.get(type_str, type_str)
./venv/lib64/python3.12/site-packages/torchgen/api/cpp.py:365:    return JIT_TO_CPP_DEFAULT.get(d, d)
./venv/lib64/python3.12/site-packages/fastapi/dependencies/utils.py:606:            ).get(original_call, original_call)
./venv/lib64/python3.12/site-packages/fastapi/dependencies/utils.py:731:        value = values.get(alias, None)
./venv/lib64/python3.12/site-packages/sentence_transformers/sparse_encoder/evaluation/ReciprocalRankFusionEvaluator.py:199:                dense_rank = dense_ranks.get(doc, len(dense_docs))
./venv/lib64/python3.12/site-packages/sentence_transformers/sparse_encoder/evaluation/ReciprocalRankFusionEvaluator.py:200:                sparse_rank = sparse_ranks.get(doc, len(sparse_docs))
./venv/lib64/python3.12/site-packages/sentence_transformers/evaluation/NanoBEIREvaluator.py:455:            ir_evaluator_kwargs["query_prompt"] = self.query_prompts.get(dataset_name, None)
./venv/lib64/python3.12/site-packages/sentence_transformers/evaluation/NanoBEIREvaluator.py:457:            ir_evaluator_kwargs["corpus_prompt"] = self.corpus_prompts.get(dataset_name, None)
./venv/lib64/python3.12/site-packages/sentence_transformers/SentenceTransformer.py:1169:                    module_kwarg_keys = self.module_kwargs.get(module_name, [])
./venv/lib64/python3.12/site-packages/sentence_transformers/model_card.py:1051:                else line.get(key, "-")
./venv/lib64/python3.12/site-packages/sentence_transformers/data_collator.py:94:            task = router_mapping.get(column_name, None)
./venv/lib64/python3.12/site-packages/websockets/sync/connection.py:319:            return self.recv_messages.get(timeout, decode)
./venv/lib64/python3.12/site-packages/huggingface_hub/cli/cache.py:237:            refs = revision.refs if revision is not None else repo_refs_map.get(repo, frozenset())
./venv/lib64/python3.12/site-packages/huggingface_hub/cli/cache.py:269:                "refs": sorted(repo_refs_map.get(repo, frozenset())),
./venv/lib64/python3.12/site-packages/huggingface_hub/cli/cache.py:305:                " ".join(sorted(repo_refs_map.get(repo, frozenset()))),
./venv/lib64/python3.12/site-packages/huggingface_hub/_commit_api.py:855:                    response = get_session().get(url, headers=headers)
./venv/lib64/python3.12/site-packages/huggingface_hub/inference/_generated/_async_client.py:3387:        response = await client.get(url, headers=build_hf_headers(token=self.token))
./venv/lib64/python3.12/site-packages/huggingface_hub/inference/_generated/_async_client.py:3424:        response = await client.get(url, headers=build_hf_headers(token=self.token))
./venv/lib64/python3.12/site-packages/huggingface_hub/inference/_common.py:386:    return _UNSUPPORTED_TEXT_GENERATION_KWARGS.get(model, [])
./venv/lib64/python3.12/site-packages/huggingface_hub/inference/_providers/fal_ai.py:82:            status_response = get_session().get(status_url, headers=request_params.headers)
./venv/lib64/python3.12/site-packages/huggingface_hub/inference/_providers/fal_ai.py:86:        return get_session().get(result_url, headers=request_params.headers).json()
./venv/lib64/python3.12/site-packages/huggingface_hub/inference/_providers/black_forest_labs.py:51:            response = session.get(url, headers={"Content-Type": "application/json"})  # type: ignore
./venv/lib64/python3.12/site-packages/huggingface_hub/inference/_providers/zai_org.py:98:            poll_response = session.get(poll_url, headers=request_params.headers)
./venv/lib64/python3.12/site-packages/huggingface_hub/inference/_providers/wavespeed.py:62:            result_response = get_session().get(result_url, headers=request_params.headers)
./venv/lib64/python3.12/site-packages/huggingface_hub/inference/_client.py:3334:        response = get_session().get(url, headers=build_hf_headers(token=self.token))
./venv/lib64/python3.12/site-packages/huggingface_hub/inference/_client.py:3369:        response = get_session().get(url, headers=build_hf_headers(token=self.token))
./venv/lib64/python3.12/site-packages/huggingface_hub/utils/_auth.py:143:        stored_tokens = {token_name: config.get(token_name, "hf_token") for token_name in config.sections()}
./venv/lib64/python3.12/site-packages/huggingface_hub/utils/_runtime.py:76:    return _package_versions.get(package_name, "N/A")
./venv/lib64/python3.12/site-packages/huggingface_hub/utils/_pagination.py:36:    r = session.get(path, params=params, headers=headers)
./venv/lib64/python3.12/site-packages/huggingface_hub/_login.py:214:        token = tokens.get(token_name, "<not set>")
./venv/lib64/python3.12/site-packages/huggingface_hub/_inference_endpoints.py:230:                response = get_session().get(_health_url, headers=self._api._build_hf_headers(token=self._token))
./venv/lib64/python3.12/site-packages/huggingface_hub/hf_api.py:2790:        r = get_session().get(path, headers=headers, timeout=timeout, params=params)
./venv/lib64/python3.12/site-packages/huggingface_hub/hf_api.py:2860:        r = get_session().get(path, headers=headers, timeout=timeout, params=params)
./venv/lib64/python3.12/site-packages/huggingface_hub/hf_api.py:2930:        r = get_session().get(path, headers=headers, timeout=timeout, params=params)
./venv/lib64/python3.12/site-packages/huggingface_hub/hf_api.py:5947:        response = get_session().get(url, headers={**_headers, "range": "bytes=0-100000"})
./venv/lib64/python3.12/site-packages/huggingface_hub/hf_api.py:5957:            response = get_session().get(url, headers={**_headers, "range": f"bytes=8-{metadata_size + 7}"})
./venv/lib64/python3.12/site-packages/huggingface_hub/hf_api.py:6338:            resp = get_session().get(path, headers=headers, params=params)
./venv/lib64/python3.12/site-packages/huggingface_hub/hf_api.py:6414:        resp = get_session().get(path, params={"diff": "1"}, headers=headers)
./venv/lib64/python3.12/site-packages/huggingface_hub/hf_api.py:10097:        r = get_session().get(path, params=params, headers=self._build_hf_headers(token=token))
./venv/lib64/python3.12/site-packages/huggingface_hub/hf_api.py:10163:        r = get_session().get(path, headers=headers)
./venv/lib64/python3.12/site-packages/huggingface_hub/dataclasses.py:145:            for validator in self.__validators__.get(name, []):
./venv/lib64/python3.12/site-packages/transformers/configuration_utils.py:342:                    value if not isinstance(value, dict) else value.get(subconfig_key, current_subconfig_attn)
./venv/lib64/python3.12/site-packages/transformers/configuration_utils.py:364:                    value if not isinstance(value, dict) else value.get(subconfig_key, current_subconfig_moe)
./venv/lib64/python3.12/site-packages/transformers/configuration_utils.py:866:                or (key in default_config_dict and value != class_config_dict.get(key, value))
./venv/lib64/python3.12/site-packages/transformers/modeling_flash_attention_utils.py:144:        fa_param = _hf_api_to_flash_mapping.get(param, param)
./venv/lib64/python3.12/site-packages/transformers/modelcard.py:242:                metadata = dataset_metadata_mapping.get(ds_tag, {})
./venv/lib64/python3.12/site-packages/transformers/trainer.py:5121:                setattr(fsdp_plugin, param, self.args.fsdp_config.get(param, getattr(fsdp_plugin, param)))
./venv/lib64/python3.12/site-packages/transformers/modeling_gguf_pytorch_utils.py:558:        ProcessorClass = TENSOR_PROCESSORS.get(architecture, TensorProcessor)
./venv/lib64/python3.12/site-packages/transformers/tokenization_utils_tokenizers.py:733:                current = {k: _truncation.get(k, None) for k in target}
./venv/lib64/python3.12/site-packages/transformers/tokenization_utils_tokenizers.py:1096:                        tokens = [special_tokens_map.get(token, token) for token in tokens]
./venv/lib64/python3.12/site-packages/transformers/tokenization_utils_tokenizers.py:1130:                special_token_full = self._special_tokens_map.get(token, None)
./venv/lib64/python3.12/site-packages/transformers/audio_utils.py:136:            BytesIO(httpx.get(audio, follow_redirects=True, timeout=timeout).content), sr=sampling_rate
./venv/lib64/python3.12/site-packages/transformers/audio_utils.py:178:            response = httpx.get(audio, follow_redirects=True, timeout=timeout)
./venv/lib64/python3.12/site-packages/transformers/video_utils.py:701:        file_obj = BytesIO(httpx.get(video, follow_redirects=True).content)
./venv/lib64/python3.12/site-packages/transformers/image_utils.py:455:            image = PIL.Image.open(BytesIO(httpx.get(image, timeout=timeout, follow_redirects=True).content))
./venv/lib64/python3.12/site-packages/transformers/training_args.py:113:        val = int(os.environ.get(e, "-1"))
./venv/lib64/python3.12/site-packages/transformers/integrations/accelerate.py:749:                device_buffer_sizes[device] = device_buffer_sizes.get(device, 0) + current_buffer_size
./venv/lib64/python3.12/site-packages/transformers/integrations/accelerate.py:849:                gpu_memory_used = device_memory_used.get(gpu_device, 0)
./venv/lib64/python3.12/site-packages/transformers/integrations/peft.py:975:    base_model_type = _MODEL_TO_CONVERSION_PATTERN.get(model_type, None)
./venv/lib64/python3.12/site-packages/transformers/integrations/peft.py:980:    fused_targets = _MOE_FUSED_TARGETS.get(base_model_type, {})
./venv/lib64/python3.12/site-packages/transformers/integrations/peft.py:1009:        present_targets = matched_targets.get(new_name, set())
./venv/lib64/python3.12/site-packages/transformers/integrations/vptq.py:51:                layer_params = config_for_layers.get(module_name, None) or shared_layer_config.get(
./venv/lib64/python3.12/site-packages/transformers/integrations/moe.py:296:        return super().get(experts_implementation, default)
./venv/lib64/python3.12/site-packages/transformers/utils/auto_docstring.py:1476:                ).get(model_name, None)
./venv/lib64/python3.12/site-packages/transformers/utils/chat_template_utils.py:99:    return type_mapping.get(param_type, {"type": "object"})
./venv/lib64/python3.12/site-packages/transformers/utils/attention_visualizer.py:183:            img = Image.open(io.BytesIO(httpx.get(img, follow_redirects=True).content))
./venv/lib64/python3.12/site-packages/transformers/utils/notebook.py:256:                    self.inner_table.append([values.get(c, "No Log") for c in columns])
./venv/lib64/python3.12/site-packages/transformers/core_model_loading.py:364:            tensors = input_dict.get(key, [])
./venv/lib64/python3.12/site-packages/transformers/core_model_loading.py:1159:                        len(mapping.collected_tensors.get(source_pattern, []))
./venv/lib64/python3.12/site-packages/transformers/models/rt_detr_v2/modeling_rt_detr_v2.py:1433:        >>> image = Image.open(requests.get(url, stream=True).raw)
./venv/lib64/python3.12/site-packages/transformers/models/rt_detr_v2/modeling_rt_detr_v2.py:1768:        >>> image = Image.open(requests.get(url, stream=True).raw)
./venv/lib64/python3.12/site-packages/transformers/models/d_fine/modeling_d_fine.py:1647:        >>> image = Image.open(requests.get(url, stream=True).raw)
./venv/lib64/python3.12/site-packages/transformers/models/speech_to_text/tokenization_speech_to_text.py:183:        return self.encoder.get(token, self.encoder[self.unk_token])
./venv/lib64/python3.12/site-packages/transformers/models/speech_to_text/tokenization_speech_to_text.py:187:        return self.decoder.get(index, self.unk_token)
./venv/lib64/python3.12/site-packages/transformers/models/fastspeech2_conformer/tokenization_fastspeech2_conformer.py:125:        return self.encoder.get(token, self.encoder.get(self.unk_token))
./venv/lib64/python3.12/site-packages/transformers/models/fastspeech2_conformer/tokenization_fastspeech2_conformer.py:129:        return self.decoder.get(index, self.unk_token)
./venv/lib64/python3.12/site-packages/transformers/models/tapas/tokenization_tapas.py:375:        return self.vocab.get(token, self.vocab.get(self.unk_token))
./venv/lib64/python3.12/site-packages/transformers/models/tapas/tokenization_tapas.py:379:        return self.ids_to_tokens.get(index, self.unk_token)
./venv/lib64/python3.12/site-packages/transformers/models/cpmant/tokenization_cpmant.py:198:        return self.encoder.get(token, self.encoder.get(self.unk_token))
./venv/lib64/python3.12/site-packages/transformers/models/cpmant/tokenization_cpmant.py:202:        return self.decoder.get(index, self.unk_token)
./venv/lib64/python3.12/site-packages/transformers/models/sam3_video/processing_sam3_video.py:295:                [model_outputs["obj_id_to_tracker_score"].get(obj_id, 0.0) for obj_id in curr_obj_ids]
./venv/lib64/python3.12/site-packages/transformers/models/sam3_video/modeling_sam3_video.py:274:        old_obj_idx_to_rm = self._obj_id_to_idx.get(obj_id, None)
./venv/lib64/python3.12/site-packages/transformers/models/sam3_video/modeling_sam3_video.py:374:        out = self.output_dict_per_obj[obj_idx][storage_key].get(frame_idx, None)
./venv/lib64/python3.12/site-packages/transformers/models/phobert/tokenization_phobert.py:240:            bigram = min(pairs, key=lambda pair: self.bpe_ranks.get(pair, float("inf")))
./venv/lib64/python3.12/site-packages/transformers/models/phobert/tokenization_phobert.py:285:        return self.encoder.get(token, self.encoder.get(self.unk_token))
./venv/lib64/python3.12/site-packages/transformers/models/phobert/tokenization_phobert.py:289:        return self.decoder.get(index, self.unk_token)
./venv/lib64/python3.12/site-packages/transformers/models/wav2vec2/tokenization_wav2vec2.py:269:        return self.encoder.get(token, self.encoder.get(self.unk_token))
./venv/lib64/python3.12/site-packages/transformers/models/wav2vec2/tokenization_wav2vec2.py:273:        result = self.decoder.get(index, self.unk_token)
./venv/lib64/python3.12/site-packages/transformers/models/auto/tokenization_auto.py:595:            tokenizer_class_name = TOKENIZER_MAPPING_NAMES.get(tokenizer_type, None)
./venv/lib64/python3.12/site-packages/transformers/models/auto/tokenization_auto.py:644:            and TOKENIZER_MAPPING_NAMES.get(config_model_type, "").replace("Fast", "")
./venv/lib64/python3.12/site-packages/transformers/models/whisper/english_normalizer.py:415:                        ones = self.ones.get(next, 0)
./venv/lib64/python3.12/site-packages/transformers/models/whisper/english_normalizer.py:508:        return " ".join(self.mapping.get(word, word) for word in s.split())
./venv/lib64/python3.12/site-packages/transformers/models/markuplm/tokenization_markuplm.py:268:            xpath_tags_list.append(self.tags_dict.get(tag_name, self.unk_tag_id))
./venv/lib64/python3.12/site-packages/transformers/models/m2m_100/tokenization_m2m_100.py:202:        return self.encoder.get(token, self.encoder[self.unk_token])
./venv/lib64/python3.12/site-packages/transformers/models/m2m_100/tokenization_m2m_100.py:208:        return self.decoder.get(index, self.unk_token)
./venv/lib64/python3.12/site-packages/transformers/models/bartpho/tokenization_bartpho.py:285:            new_id = self.fairseq_tokens_to_ids.get(token, original_id)
./venv/lib64/python3.12/site-packages/transformers/models/clvp/tokenization_clvp.py:199:            bigram = min(pairs, key=lambda pair: self.bpe_ranks.get(pair, float("inf")))
./venv/lib64/python3.12/site-packages/transformers/models/clvp/tokenization_clvp.py:250:        return self.encoder.get(token, self.encoder.get(self.unk_token))
./venv/lib64/python3.12/site-packages/transformers/models/luke/tokenization_luke.py:959:                    first_entity_ids = [self.entity_vocab.get(entity, self.entity_unk_token_id) for entity in entities]
./venv/lib64/python3.12/site-packages/transformers/models/luke/tokenization_luke.py:974:                            self.entity_vocab.get(entity, self.entity_unk_token_id) for entity in entities_pair
./venv/lib64/python3.12/site-packages/transformers/models/florence2/modular_florence2.py:490:        post_proc_type = self.tasks_answer_post_processing_type.get(task, "pure_text")
./venv/lib64/python3.12/site-packages/transformers/models/florence2/processing_florence2.py:290:        post_proc_type = self.tasks_answer_post_processing_type.get(task, "pure_text")
./venv/lib64/python3.12/site-packages/transformers/models/chameleon/modeling_chameleon.py:763:            return "".join(img_tkn_chr_mapping.get(c, c) for c in old_name[len("IMGIMG") : -1])
./venv/lib64/python3.12/site-packages/transformers/models/flaubert/tokenization_flaubert.py:332:            bigram = min(pairs, key=lambda pair: self.bpe_ranks.get(pair, float("inf")))
./venv/lib64/python3.12/site-packages/transformers/models/flaubert/tokenization_flaubert.py:416:        return self.encoder.get(token, self.encoder.get(self.unk_token))
./venv/lib64/python3.12/site-packages/transformers/models/flaubert/tokenization_flaubert.py:421:        return self.decoder.get(index, self.unk_token)
./venv/lib64/python3.12/site-packages/transformers/models/sam2_video/modeling_sam2_video.py:180:        obj_idx = self._obj_id_to_idx.get(obj_id, None)
./venv/lib64/python3.12/site-packages/transformers/models/sam2_video/modeling_sam2_video.py:288:        out = self.output_dict_per_obj[obj_idx][storage_key].get(frame_idx, None)
./venv/lib64/python3.12/site-packages/transformers/models/sam2_video/modeling_sam2_video.py:1776:                    point_inputs = inference_session.point_inputs_per_obj[obj_idx].get(frame_idx, None)
./venv/lib64/python3.12/site-packages/transformers/models/sam2_video/modeling_sam2_video.py:1777:                    mask_inputs = inference_session.mask_inputs_per_obj[obj_idx].get(frame_idx, None)
./venv/lib64/python3.12/site-packages/transformers/models/sam2_video/modeling_sam2_video.py:2235:                previous_frame_idx, unselected_conditioning_outputs.get(previous_frame_idx, None)
./venv/lib64/python3.12/site-packages/transformers/models/sam2_video/processing_sam2_video.py:717:                existing_points = inference_session.point_inputs_per_obj[obj_idx].get(frame_idx, None)
./venv/lib64/python3.12/site-packages/transformers/models/sam2_video/modular_sam2_video.py:446:        obj_idx = self._obj_id_to_idx.get(obj_id, None)
./venv/lib64/python3.12/site-packages/transformers/models/sam2_video/modular_sam2_video.py:554:        out = self.output_dict_per_obj[obj_idx][storage_key].get(frame_idx, None)
./venv/lib64/python3.12/site-packages/transformers/models/sam2_video/modular_sam2_video.py:822:                existing_points = inference_session.point_inputs_per_obj[obj_idx].get(frame_idx, None)
./venv/lib64/python3.12/site-packages/transformers/models/sam2_video/modular_sam2_video.py:1887:                previous_frame_idx, unselected_conditioning_outputs.get(previous_frame_idx, None)
./venv/lib64/python3.12/site-packages/transformers/models/sam2_video/modular_sam2_video.py:2391:                    point_inputs = inference_session.point_inputs_per_obj[obj_idx].get(frame_idx, None)
./venv/lib64/python3.12/site-packages/transformers/models/sam2_video/modular_sam2_video.py:2392:                    mask_inputs = inference_session.mask_inputs_per_obj[obj_idx].get(frame_idx, None)
./venv/lib64/python3.12/site-packages/transformers/models/bertweet/tokenization_bertweet.py:186:            bigram = min(pairs, key=lambda pair: self.bpe_ranks.get(pair, float("inf")))
./venv/lib64/python3.12/site-packages/transformers/models/bertweet/tokenization_bertweet.py:285:        return self.encoder.get(token, self.encoder.get(self.unk_token))
./venv/lib64/python3.12/site-packages/transformers/models/bertweet/tokenization_bertweet.py:289:        return self.decoder.get(index, self.unk_token)
./venv/lib64/python3.12/site-packages/transformers/models/esm/tokenization_esm.py:70:        return self._id_to_token.get(index, self.unk_token)
./venv/lib64/python3.12/site-packages/transformers/models/esm/tokenization_esm.py:73:        return self._token_to_id.get(token, self._token_to_id.get(self.unk_token))
./venv/lib64/python3.12/site-packages/transformers/models/esm/tokenization_esm.py:84:        return self._token_to_id.get(token, self._token_to_id.get(self.unk_token))
./venv/lib64/python3.12/site-packages/transformers/models/esm/tokenization_esm.py:87:        return self._id_to_token.get(index, self.unk_token)
./venv/lib64/python3.12/site-packages/transformers/models/esm/openfold_utils/data_transforms.py:34:        restype_atom37_to_atom14_list.append([(atom_name_to_idx14.get(name, 0)) for name in rc.atom_types])
./venv/lib64/python3.12/site-packages/transformers/models/esm/openfold_utils/residue_constants.py:632:                aa_id = mapping.get(aa_type, mapping["X"])
./venv/lib64/python3.12/site-packages/transformers/models/esm/openfold_utils/protein.py:87:                [residue_constants.restype_order.get(res_symbol, residue_constants.restype_num) for res_symbol in seq]
./venv/lib64/python3.12/site-packages/transformers/models/prophetnet/tokenization_prophetnet.py:389:        return self.vocab.get(token, self.vocab.get(self.unk_token))
./venv/lib64/python3.12/site-packages/transformers/models/prophetnet/tokenization_prophetnet.py:393:        return self.ids_to_tokens.get(index, self.unk_token)
./venv/lib64/python3.12/site-packages/transformers/models/dia/generation_dia.py:233:                if model_inputs.get(key, None) is not None:
./venv/lib64/python3.12/site-packages/transformers/models/perceiver/modeling_perceiver.py:2297:                input_without_pos = inputs_without_pos.get(modality, None)
./venv/lib64/python3.12/site-packages/transformers/models/perceiver/modeling_perceiver.py:2302:                subsampled_points=subsampled_points.get(modality, None),
./venv/lib64/python3.12/site-packages/transformers/models/biogpt/tokenization_biogpt.py:166:            bigram = min(pairs, key=lambda pair: self.bpe_ranks.get(pair, float("inf")))
./venv/lib64/python3.12/site-packages/transformers/models/biogpt/tokenization_biogpt.py:216:        return self.encoder.get(token, self.encoder.get(self.unk_token))
./venv/lib64/python3.12/site-packages/transformers/models/biogpt/tokenization_biogpt.py:220:        return self.decoder.get(index, self.unk_token)
./venv/lib64/python3.12/site-packages/transformers/models/rt_detr/modular_rt_detr.py:1495:        >>> image = Image.open(requests.get(url, stream=True).raw)
./venv/lib64/python3.12/site-packages/transformers/models/rt_detr/modular_rt_detr.py:1721:        >>> image = Image.open(requests.get(url, stream=True).raw)
./venv/lib64/python3.12/site-packages/transformers/models/rt_detr/modeling_rt_detr.py:1510:        >>> image = Image.open(requests.get(url, stream=True).raw)
./venv/lib64/python3.12/site-packages/transformers/models/rt_detr/modeling_rt_detr.py:1736:        >>> image = Image.open(requests.get(url, stream=True).raw)
./venv/lib64/python3.12/site-packages/transformers/models/seamless_m4t_v2/modeling_seamless_m4t_v2.py:1455:                    char_ids = [self.generation_config.char_to_id.get(ch, unk_token_id) for ch in list(subword)]
./venv/lib64/python3.12/site-packages/transformers/models/pp_doclayout_v3/modular_pp_doclayout_v3.py:1141:        >>> image = Image.open(requests.get(url, stream=True).raw)
./venv/lib64/python3.12/site-packages/transformers/models/pp_doclayout_v3/modular_pp_doclayout_v3.py:1461:        >>> image = Image.open(requests.get(url, stream=True).raw)
./venv/lib64/python3.12/site-packages/transformers/models/pp_doclayout_v3/modeling_pp_doclayout_v3.py:1678:        >>> image = Image.open(requests.get(url, stream=True).raw)
./venv/lib64/python3.12/site-packages/transformers/models/pp_doclayout_v3/modeling_pp_doclayout_v3.py:2001:        >>> image = Image.open(requests.get(url, stream=True).raw)
./venv/lib64/python3.12/site-packages/transformers/models/blenderbot_small/tokenization_blenderbot_small.py:133:                bigram = min(pairs, key=lambda pair: self.bpe_ranks.get(pair, float("inf")))
./venv/lib64/python3.12/site-packages/transformers/models/blenderbot_small/tokenization_blenderbot_small.py:181:        return self.encoder.get(token, self.encoder.get(self.unk_token))
./venv/lib64/python3.12/site-packages/transformers/models/blenderbot_small/tokenization_blenderbot_small.py:185:        return self.decoder.get(index, self.unk_token)
./venv/lib64/python3.12/site-packages/transformers/models/mgp_str/tokenization_mgp_str.py:83:        return self.vocab.get(token, self.vocab.get(self.unk_token))
./venv/lib64/python3.12/site-packages/transformers/models/wav2vec2_phoneme/tokenization_wav2vec2_phoneme.py:321:        return self.encoder.get(token, self.encoder.get(self.unk_token))
./venv/lib64/python3.12/site-packages/transformers/models/wav2vec2_phoneme/tokenization_wav2vec2_phoneme.py:325:        result = self.decoder.get(index, self.unk_token)
./venv/lib64/python3.12/site-packages/transformers/models/edgetam_video/modular_edgetam_video.py:1297:                    point_inputs = inference_session.point_inputs_per_obj[obj_idx].get(frame_idx, None)
./venv/lib64/python3.12/site-packages/transformers/models/edgetam_video/modular_edgetam_video.py:1298:                    mask_inputs = inference_session.mask_inputs_per_obj[obj_idx].get(frame_idx, None)
./venv/lib64/python3.12/site-packages/transformers/models/edgetam_video/modeling_edgetam_video.py:978:        obj_idx = self._obj_id_to_idx.get(obj_id, None)
./venv/lib64/python3.12/site-packages/transformers/models/edgetam_video/modeling_edgetam_video.py:1086:        out = self.output_dict_per_obj[obj_idx][storage_key].get(frame_idx, None)
./venv/lib64/python3.12/site-packages/transformers/models/edgetam_video/modeling_edgetam_video.py:2188:                    point_inputs = inference_session.point_inputs_per_obj[obj_idx].get(frame_idx, None)
./venv/lib64/python3.12/site-packages/transformers/models/edgetam_video/modeling_edgetam_video.py:2189:                    mask_inputs = inference_session.mask_inputs_per_obj[obj_idx].get(frame_idx, None)
./venv/lib64/python3.12/site-packages/transformers/models/edgetam_video/modeling_edgetam_video.py:2620:                previous_frame_idx, unselected_conditioning_outputs.get(previous_frame_idx, None)
./venv/lib64/python3.12/site-packages/transformers/models/sam3_tracker_video/processing_sam3_tracker_video.py:719:                existing_points = inference_session.point_inputs_per_obj[obj_idx].get(frame_idx, None)
./venv/lib64/python3.12/site-packages/transformers/models/sam3_tracker_video/modeling_sam3_tracker_video.py:185:        obj_idx = self._obj_id_to_idx.get(obj_id, None)
./venv/lib64/python3.12/site-packages/transformers/models/sam3_tracker_video/modeling_sam3_tracker_video.py:293:        out = self.output_dict_per_obj[obj_idx][storage_key].get(frame_idx, None)
./venv/lib64/python3.12/site-packages/transformers/models/sam3_tracker_video/modeling_sam3_tracker_video.py:1799:                    point_inputs = inference_session.point_inputs_per_obj[obj_idx].get(frame_idx, None)
./venv/lib64/python3.12/site-packages/transformers/models/sam3_tracker_video/modeling_sam3_tracker_video.py:1800:                    mask_inputs = inference_session.mask_inputs_per_obj[obj_idx].get(frame_idx, None)
./venv/lib64/python3.12/site-packages/transformers/models/sam3_tracker_video/modeling_sam3_tracker_video.py:2260:                previous_frame_idx, unselected_conditioning_outputs.get(previous_frame_idx, None)
./venv/lib64/python3.12/site-packages/transformers/models/pop2piano/tokenization_pop2piano.py:146:        token_type_value = self.decoder.get(token_id, f"{self.unk_token}_TOKEN_TIME")
./venv/lib64/python3.12/site-packages/transformers/models/xlm/tokenization_xlm.py:330:            bigram = min(pairs, key=lambda pair: self.bpe_ranks.get(pair, float("inf")))
./venv/lib64/python3.12/site-packages/transformers/models/xlm/tokenization_xlm.py:464:        return self.encoder.get(token, self.encoder.get(self.unk_token))
./venv/lib64/python3.12/site-packages/transformers/models/xlm/tokenization_xlm.py:468:        return self.decoder.get(index, self.unk_token)
./venv/lib64/python3.12/site-packages/transformers/models/roc_bert/tokenization_roc_bert.py:962:        return self.vocab.get(token, self.vocab.get(self.unk_token))
./venv/lib64/python3.12/site-packages/transformers/models/roc_bert/tokenization_roc_bert.py:966:        return self.word_shape.get(token, self.word_shape.get(self.unk_token))
./venv/lib64/python3.12/site-packages/transformers/models/roc_bert/tokenization_roc_bert.py:979:        return self.word_pronunciation.get(token, self.word_pronunciation.get(self.unk_token))
./venv/lib64/python3.12/site-packages/transformers/models/roc_bert/tokenization_roc_bert.py:992:        return self.ids_to_tokens.get(index, self.unk_token)
./venv/lib64/python3.12/site-packages/transformers/models/mluke/tokenization_mluke.py:986:                    first_entity_ids = [self.entity_vocab.get(entity, self.entity_unk_token_id) for entity in entities]
./venv/lib64/python3.12/site-packages/transformers/models/mluke/tokenization_mluke.py:1001:                            self.entity_vocab.get(entity, self.entity_unk_token_id) for entity in entities_pair
./venv/lib64/python3.12/site-packages/transformers/models/conditional_detr/modeling_conditional_detr.py:1371:        >>> image = Image.open(requests.get(url, stream=True).raw)
./venv/lib64/python3.12/site-packages/transformers/models/conditional_detr/modeling_conditional_detr.py:1530:        >>> image = Image.open(requests.get(url, stream=True).raw)
./venv/lib64/python3.12/site-packages/transformers/models/conditional_detr/modular_conditional_detr.py:741:        >>> image = Image.open(requests.get(url, stream=True).raw)
./venv/lib64/python3.12/site-packages/transformers/models/conditional_detr/modular_conditional_detr.py:882:        >>> image = Image.open(requests.get(url, stream=True).raw)
./venv/lib64/python3.12/site-packages/transformers/models/grounding_dino/processing_grounding_dino.py:97:        return super().get(key, *args, **kwargs)
./venv/lib64/python3.12/site-packages/transformers/models/ctrl/tokenization_ctrl.py:163:            bigram = min(pairs, key=lambda pair: self.bpe_ranks.get(pair, float("inf")))
./venv/lib64/python3.12/site-packages/transformers/models/ctrl/tokenization_ctrl.py:208:        return self.encoder.get(token, self.encoder.get(self.unk_token))
./venv/lib64/python3.12/site-packages/transformers/models/ctrl/tokenization_ctrl.py:212:        return self.decoder.get(index, self.unk_token)
./venv/lib64/python3.12/site-packages/transformers/models/gpt_neox_japanese/tokenization_gpt_neox_japanese.py:153:        return self.vocab.get(token, self.vocab.get(self.unk_token))
./venv/lib64/python3.12/site-packages/transformers/models/bert/tokenization_bert_legacy.py:173:        return self.vocab.get(token, self.vocab.get(self.unk_token))
./venv/lib64/python3.12/site-packages/transformers/models/bert/tokenization_bert_legacy.py:177:        return self.ids_to_tokens.get(index, self.unk_token)
./venv/lib64/python3.12/site-packages/transformers/models/deformable_detr/modeling_deformable_detr.py:1332:        >>> image = Image.open(requests.get(url, stream=True).raw)
./venv/lib64/python3.12/site-packages/transformers/models/deformable_detr/modeling_deformable_detr.py:1596:        >>> image = Image.open(requests.get(url, stream=True).raw)
./venv/lib64/python3.12/site-packages/transformers/models/deformable_detr/modular_deformable_detr.py:1114:        >>> image = Image.open(requests.get(url, stream=True).raw)
./venv/lib64/python3.12/site-packages/transformers/models/deformable_detr/modular_deformable_detr.py:1363:        >>> image = Image.open(requests.get(url, stream=True).raw)
./venv/lib64/python3.12/site-packages/transformers/models/bert_japanese/tokenization_bert_japanese.py:248:        return self.vocab.get(token, self.vocab.get(self.unk_token))
./venv/lib64/python3.12/site-packages/transformers/models/bert_japanese/tokenization_bert_japanese.py:254:        return self.ids_to_tokens.get(index, self.unk_token)
./venv/lib64/python3.12/site-packages/transformers/models/plbart/tokenization_plbart.py:334:        lang = FAIRSEQ_LANGUAGE_CODES_MAP.get(lang, lang)
./venv/lib64/python3.12/site-packages/transformers/models/fsmt/tokenization_fsmt.py:286:            bigram = min(pairs, key=lambda pair: self.bpe_ranks.get(pair, float("inf")))
./venv/lib64/python3.12/site-packages/transformers/models/fsmt/tokenization_fsmt.py:361:        return self.encoder.get(token, self.encoder.get(self.unk_token))
./venv/lib64/python3.12/site-packages/transformers/models/fsmt/tokenization_fsmt.py:365:        return self.decoder.get(index, self.unk_token)
./venv/lib64/python3.12/site-packages/transformers/generation/continuous_batching/cache_manager.py:361:        block_table = self.block_table.get(request_id, [])
./venv/lib64/python3.12/site-packages/transformers/generation/continuous_batching/cache.py:44:        layer_counts[layer_type] = layer_counts.get(layer_type, []) + [i]
./venv/lib64/python3.12/site-packages/transformers/generation/logits_process.py:1036:            generated_ngram[prev_ngram_tuple] = generated_ngram.get(prev_ngram_tuple, []) + [ngram[-1]]
./venv/lib64/python3.12/site-packages/transformers/generation/logits_process.py:1060:    return banned_ngrams.get(ngram_idx, [])
./venv/lib64/python3.12/site-packages/transformers/pipelines/zero_shot_audio_classification.py:109:                audio = httpx.get(audio, follow_redirects=True).content
./venv/lib64/python3.12/site-packages/transformers/pipelines/table_question_answering.py:366:                aggregator = aggregators.get(index, "")
./venv/lib64/python3.12/site-packages/transformers/pipelines/table_question_answering.py:367:                aggregator_prefix = aggregators_prefix.get(index, "")
./venv/lib64/python3.12/site-packages/transformers/pipelines/audio_classification.py:171:                inputs = httpx.get(inputs, follow_redirects=True).content
./venv/lib64/python3.12/site-packages/transformers/pipelines/video_classification.py:137:            video = BytesIO(httpx.get(video, follow_redirects=True).content)
./venv/lib64/python3.12/site-packages/transformers/pipelines/automatic_speech_recognition.py:368:                inputs = httpx.get(inputs, follow_redirects=True).content
./venv/lib64/python3.12/site-packages/transformers/modeling_utils.py:2023:                    else attn_implementation.get(subconfig_key, subconfig._attn_implementation)
./venv/lib64/python3.12/site-packages/transformers/modeling_utils.py:4734:        return super().get(attn_implementation, default)
./venv/lib64/python3.12/site-packages/transformers/processing_utils.py:1167:        args = [args_to_update.get(i, arg) for i, arg in enumerate(args)]
./venv/lib64/python3.12/site-packages/transformers/processing_utils.py:1254:            default_kwargs[modality] = ModelProcessorKwargs._defaults.get(modality, {}).copy()
./venv/lib64/python3.12/site-packages/transformers/processing_utils.py:1315:                    kwarg_value = kwargs.get(modality_key, "__empty__")
./venv/lib64/python3.12/site-packages/transformers/hf_argparser.py:61:    return lambda arg: str_to_choice.get(arg, arg)
./venv/lib64/python3.12/site-packages/transformers/data/metrics/squad_metrics.py:456:                    if not feature.token_is_max_context.get(start_index, False):
./venv/lib64/python3.12/site-packages/transformers/data/metrics/squad_metrics.py:666:                    if not feature.token_is_max_context.get(start_index, False):
./venv/lib64/python3.12/site-packages/numpy/f2py/use_rules.py:68:            varsmap[v] = revmap.get(v, v)
./venv/lib64/python3.12/site-packages/numpy/f2py/auxfuncs.py:303:        for d in rout['vars'].get(a, {}).get('dimension', []):
./venv/lib64/python3.12/site-packages/numpy/f2py/auxfuncs.py:789:    return rout['f2pymultilines'].get(k, None)
./venv/lib64/python3.12/site-packages/numpy/f2py/crackfortran.py:2362:            for w in deps.get(word, []) \
./venv/lib64/python3.12/site-packages/numpy/f2py/crackfortran.py:2589:                        vars[n] = setattrspec(vars.get(n, {}), k)
./venv/lib64/python3.12/site-packages/numpy/f2py/crackfortran.py:2789:                                for v1 in coeffs_and_deps.get(v, [None, []])[1]:
./venv/lib64/python3.12/site-packages/numpy/f2py/crackfortran.py:3134:            block['vars'][a] = block['vars'].get(orig_a, {})
./venv/lib64/python3.12/site-packages/numpy/f2py/tests/test_character.py:20:        clength = {'star': '(*)'}.get(length, length)
./venv/lib64/python3.12/site-packages/numpy/f2py/tests/test_character.py:81:        fsuffix = {'(*)': 'star'}.get(length, length)
./venv/lib64/python3.12/site-packages/numpy/f2py/_src_pyf.py:157:            thelist = lnames.get(r, names.get(r, None))
./venv/lib64/python3.12/site-packages/numpy/f2py/_src_pyf.py:181:        return rules.get(name, (k + 1) * [name])[k]
./venv/lib64/python3.12/site-packages/numpy/lib/_iotools.py:374:            cnt = seen.get(item, 0)
./venv/lib64/python3.12/site-packages/numpy/lib/recfunctions.py:265:            lastparent = list(parents.get(lastname, []) or [])
./venv/lib64/python3.12/site-packages/numpy/lib/recfunctions.py:635:            newname = namemapper.get(name, name)
./venv/lib64/python3.12/site-packages/numpy/lib/_npyio_impl.py:288:        D.get(k,[,d]) returns D[k] if k in D, else d.  d defaults to None.
./venv/lib64/python3.12/site-packages/numpy/lib/_npyio_impl.py:290:        return Mapping.get(self, key, default)
./venv/lib64/python3.12/site-packages/numpy/_utils/_pep440.py:208:        part = _legacy_version_replacement_map.get(part, part)
./venv/lib64/python3.12/site-packages/numpy/linalg/_linalg.py:184:    return _real_types_map.get(t, default)
./venv/lib64/python3.12/site-packages/numpy/linalg/_linalg.py:187:    return _complex_types_map.get(t, default)
./venv/lib64/python3.12/site-packages/numpy/testing/print_coercion_tables.py:158:            row = table.get(from_dt, {})
./venv/lib64/python3.12/site-packages/numpy/testing/print_coercion_tables.py:160:                print(getattr(row.get(to_dt, no_cast_info), field), end=' ')
./venv/lib64/python3.12/site-packages/numpy/matrixlib/tests/test_defmatrix.py:304:                args = methodargs.get(attrib, ())
./venv/lib64/python3.12/site-packages/numpy/_core/records.py:223:        res = fielddict.get(attr, None)
./venv/lib64/python3.12/site-packages/numpy/_core/records.py:243:        res = fielddict.get(attr, None)
./venv/lib64/python3.12/site-packages/numpy/_core/getlimits.py:221:                obj = cls._finfo_cache.get(dtype, None)
./venv/lib64/python3.12/site-packages/numpy/_core/tests/test_regression.py:2345:            item = sctype(values.get(sctype, 1))
./venv/lib64/python3.12/site-packages/numpy/_core/tests/test_regression.py:2383:            scvalue = sctype(values.get(ch, 3))
./venv/lib64/python3.12/site-packages/numpy/_core/tests/test_cpu_features.py:90:        map_names = self.features_map.get(feature_name, feature_name)
./venv/lib64/python3.12/site-packages/numpy/_core/tests/test_umath.py:4338:            cname = name_map.get(fname, fname)
./venv/lib64/python3.12/site-packages/numpy/_core/tests/test_simd.py:1337:            skip_m = skip_sfx.get(sfx, skip)
./venv/lib64/python3.12/site-packages/numpy/_core/_internal.py:184:            order1 = _convorder.get(order1, order1)
./venv/lib64/python3.12/site-packages/numpy/_core/_internal.py:185:            order2 = _convorder.get(order2, order2)
./venv/lib64/python3.12/site-packages/yaml/resolver.py:149:            wildcard_resolvers = self.yaml_implicit_resolvers.get(None, [])
./venv/lib64/python3.12/site-packages/pygments/style.py:88:                styledefs = obj.styles.get(token, '').split()
./venv/lib64/python3.12/site-packages/pygments/style.py:96:                for styledef in obj.styles.get(token, '').split():
./venv/lib64/python3.12/site-packages/pygments/util.py:45:    string = options.get(optname, default)
./venv/lib64/python3.12/site-packages/pygments/util.py:55:    Intuitively, this is `options.get(optname, default)`, but restricted to
./venv/lib64/python3.12/site-packages/pygments/util.py:65:    string = options.get(optname, default)
./venv/lib64/python3.12/site-packages/pygments/util.py:84:    string = options.get(optname, default)
./venv/lib64/python3.12/site-packages/pygments/util.py:100:    val = options.get(optname, default)
./venv/lib64/python3.12/site-packages/pygments/lexers/lisp.py:2415:                token = self.MAPPINGS.get(value, Name.Function)
./venv/lib64/python3.12/site-packages/pygments/lexers/robotframework.py:143:        return self._tables.get(name, UnknownTable())
./venv/lib64/python3.12/site-packages/pygments/formatters/terminal256.py:206:        index = self.best_match.get(color, None)
./venv/lib64/python3.12/site-packages/pygments/filters/__init__.py:824:            opt = options.get(name, False)
./venv/lib64/python3.12/site-packages/pygments/plugin.py:52:        return groups.get(group_name, [])
./venv/lib64/python3.12/site-packages/httpcore/_async/socks_proxy.py:66:        requested = AUTH_METHODS.get(auth_method, "UNKNOWN")
./venv/lib64/python3.12/site-packages/httpcore/_sync/socks_proxy.py:66:        requested = AUTH_METHODS.get(auth_method, "UNKNOWN")
./venv/lib64/python3.12/site-packages/cuda/pathfinder/_dynamic_libs/load_dl_linux.py:129:    candidate_sonames = list(reversed(SUPPORTED_LINUX_SONAMES.get(libname, ())))
./venv/lib64/python3.12/site-packages/cuda/pathfinder/_dynamic_libs/load_dl_windows.py:103:    for dll_name in SUPPORTED_WINDOWS_DLLS.get(libname, ()):
./venv/lib64/python3.12/site-packages/cuda/pathfinder/_dynamic_libs/load_dl_windows.py:126:    for dll_name in reversed(SUPPORTED_WINDOWS_DLLS.get(libname, ())):
./venv/lib64/python3.12/site-packages/cuda/pathfinder/_dynamic_libs/load_dl_common.py:23:    for dep in DIRECT_DEPENDENCIES.get(libname, ()):
./venv/lib64/python3.12/site-packages/cuda/pathfinder/_headers/find_nvidia_headers.py:152:    candidate_dirs = supported_nvidia_headers.SUPPORTED_SITE_PACKAGE_HEADER_DIRS_NON_CTK.get(libname, [])
./venv/lib64/python3.12/site-packages/cuda/pathfinder/_headers/find_nvidia_headers.py:162:    candidate_dirs = supported_nvidia_headers.SUPPORTED_INSTALL_DIRS_NON_CTK.get(libname, [])
./venv/lib64/python3.12/site-packages/cuda/pathfinder/_binaries/find_nvidia_binary_utility.py:86:    candidate_dirs = supported_nvidia_binaries.SITE_PACKAGES_BINDIRS.get(utility_name, ())
./venv/lib64/python3.12/site-packages/regex/_regex_core.py:4400:        self.open_group_count[group] = self.open_group_count.get(group, 0) + 1
./venv/lib64/python3.12/site-packages/regex/_regex_core.py:4583:    name, prop_values = PROPERTY_NAMES.get(prop_id, ("", {}))
./venv/lib64/python3.12/site-packages/regex/_regex_core.py:4588:        prop_values[val_id] = max(prop_values.get(val_id, ""), val_name,
./venv/lib64/python3.12/site-packages/regex/_main.py:464:    if _locale_sensitive.get(locale_key, True) or (flags & LOCALE) != 0:
./venv/lib64/python3.12/site-packages/sympy/multipledispatch/utils.py:51:        for m in edges.get(n, ()):
./venv/lib64/python3.12/site-packages/sympy/multipledispatch/utils.py:56:    if any(incoming_edges.get(v, None) for v in edges):
./venv/lib64/python3.12/site-packages/sympy/multipledispatch/utils.py:77:            result[val] = result.get(val, ()) + (key, )
./venv/lib64/python3.12/site-packages/sympy/integrals/rationaltools.py:385:    a, b = H_map.get(S.One, S.Zero), H_map.get(I, S.Zero)
./venv/lib64/python3.12/site-packages/sympy/integrals/rationaltools.py:386:    c, d = Q_map.get(S.One, S.Zero), Q_map.get(I, S.Zero)
./venv/lib64/python3.12/site-packages/sympy/integrals/manualintegrate.py:993:            var_index = orthogonal_poly_var_index.get(klass, 1)
./venv/lib64/python3.12/site-packages/sympy/integrals/manualintegrate.py:1149:    a, b, c = [match.get(i, S.Zero) for i in (a, b, c)]
./venv/lib64/python3.12/site-packages/sympy/integrals/manualintegrate.py:1734:            [match.get(i, S.Zero) for i in (a, b, m, n)] +
./venv/lib64/python3.12/site-packages/sympy/integrals/manualintegrate.py:1755:            [match.get(i, S.Zero) for i in (a, b, m, n)] +
./venv/lib64/python3.12/site-packages/sympy/integrals/manualintegrate.py:1776:            [match.get(i, S.Zero) for i in (a, b, m, n)] +
./venv/lib64/python3.12/site-packages/sympy/integrals/manualintegrate.py:1803:        a = match.get(A, S.Zero)
./venv/lib64/python3.12/site-packages/sympy/integrals/manualintegrate.py:1804:        b = match.get(B, S.Zero)
./venv/lib64/python3.12/site-packages/sympy/integrals/heurisch.py:665:            y = m.get(I, S.Zero)
./venv/lib64/python3.12/site-packages/sympy/integrals/intpoly.py:304:                value = result.get(m, None)
./venv/lib64/python3.12/site-packages/sympy/printing/pytorch.py:156:                    var_groups[base_var] = var_groups.get(base_var, 0) + order
./venv/lib64/python3.12/site-packages/sympy/printing/pytorch.py:158:                    var_groups[var] = var_groups.get(var, 0) + 1
./venv/lib64/python3.12/site-packages/sympy/printing/llvmjitcode.py:131:        array, idx = self.func_arg_map.get(s, [None, 0])
./venv/lib64/python3.12/site-packages/sympy/printing/tableform.py:166:                return {'left': 'l', 'right': 'r', 'center': 'c'}.get(a, a)
./venv/lib64/python3.12/site-packages/sympy/printing/tableform.py:168:                return {'<': 'l', '>': 'r', '^': 'c'}.get(a, a)
./venv/lib64/python3.12/site-packages/sympy/printing/fortran.py:432:        type_ = self.type_aliases.get(type_, type_)
./venv/lib64/python3.12/site-packages/sympy/printing/fortran.py:433:        type_str = self.type_mappings.get(type_, type_.name)
./venv/lib64/python3.12/site-packages/sympy/printing/latex.py:224:        self._settings['imaginary_unit_latex'] = imaginary_unit_table.get(imag_unit, imag_unit)
./venv/lib64/python3.12/site-packages/sympy/printing/latex.py:233:        self._settings["diff_operator_latex"] = diff_operator_table.get(diff_operator, diff_operator)
./venv/lib64/python3.12/site-packages/sympy/printing/c.py:466:        return self.type_func_suffixes[self.type_aliases.get(type_, type_)]
./venv/lib64/python3.12/site-packages/sympy/printing/c.py:469:        return self.type_literal_suffixes[self.type_aliases.get(type_, type_)]
./venv/lib64/python3.12/site-packages/sympy/printing/c.py:472:        alias = self.type_aliases.get(type_, type_)
./venv/lib64/python3.12/site-packages/sympy/printing/c.py:473:        dflt = self.type_math_macro_suffixes.get(alias, '')
./venv/lib64/python3.12/site-packages/sympy/printing/c.py:474:        return self.type_math_macro_suffixes.get(type_, dflt)
./venv/lib64/python3.12/site-packages/sympy/printing/c.py:482:        self.headers.update(self.type_headers.get(type_, set()))
./venv/lib64/python3.12/site-packages/sympy/printing/c.py:483:        self.macros.update(self.type_macros.get(type_, set()))
./venv/lib64/python3.12/site-packages/sympy/printing/c.py:484:        return self._print(self.type_mappings.get(type_, type_.name))
./venv/lib64/python3.12/site-packages/sympy/printing/c.py:514:        type_ = self.type_aliases.get(real, real)
./venv/lib64/python3.12/site-packages/sympy/printing/c.py:515:        self.macros.update(self.type_macros.get(type_, set()))
./venv/lib64/python3.12/site-packages/sympy/printing/preview.py:275:        for candidate in candidates.get(output, []):
./venv/lib64/python3.12/site-packages/sympy/printing/preview.py:365:                cmd.extend(defaultoptions.get(cmd_variant, []))
./venv/lib64/python3.12/site-packages/sympy/printing/pycode.py:274:        func = self.known_functions.get(name, name)
./venv/lib64/python3.12/site-packages/sympy/printing/lambdarepr.py:123:        nstr = self._numexpr_functions.get(func_name, None)
./venv/lib64/python3.12/site-packages/sympy/tensor/array/sparse_ndim_array.py:62:            return self._sparse_array.get(index, S.Zero)
./venv/lib64/python3.12/site-packages/sympy/tensor/array/expressions/array_expressions.py:1714:            arg_with_ind.indices = [updates.get(i, None) for i in arg_with_ind.indices]
./venv/lib64/python3.12/site-packages/sympy/tensor/array/expressions/from_indexed_to_array.py:83:    first_indices = [repl.get(i, i) for i in first_indices]
./venv/lib64/python3.12/site-packages/sympy/tensor/array/expressions/from_indexed_to_array.py:112:        summation_indices = sorted({subindicessets.get(i, i) for i in summation_indices}, key=default_sort_key)
./venv/lib64/python3.12/site-packages/sympy/tensor/array/expressions/from_indexed_to_array.py:194:        flattened_indices = [kronecker_delta_repl.get(j, j) for i in newindices for j in i]
./venv/lib64/python3.12/site-packages/sympy/tensor/tensor.py:956:        return self._comm[i].get(j, 0 if i == 0 or j == 0 else None)
./venv/lib64/python3.12/site-packages/sympy/tensor/tensor.py:4524:        index_map = {name_translation.get(index, index): value for index, value in index_map.items()}
./venv/lib64/python3.12/site-packages/sympy/tensor/tensor.py:4572:        slice_tuple = tuple(index_map.get(i, slice(None)) for i in ret_indices)
./venv/lib64/python3.12/site-packages/sympy/simplify/radsimp.py:181:        syms = [reps.get(s, s) for s in syms]
./venv/lib64/python3.12/site-packages/sympy/simplify/radsimp.py:189:            return {urep.get(k, k).xreplace(urep): v.xreplace(urep)
./venv/lib64/python3.12/site-packages/sympy/simplify/trigsimp.py:1026:                if res and res.get(c, 0):
./venv/lib64/python3.12/site-packages/sympy/concrete/expr_with_limits.py:341:        return {reps.get(_, _) for _ in isyms}
./venv/lib64/python3.12/site-packages/sympy/concrete/summations.py:1652:        assum_true = x._assumptions.get(assum, None)
./venv/lib64/python3.12/site-packages/sympy/functions/elementary/exponential.py:1027:                    res[ex] = res.get(ex, S.Zero) + d1[e1]*d2[e2]
./venv/lib64/python3.12/site-packages/sympy/functions/elementary/exponential.py:1034:            pterms[e1] = pterms.get(e1, S.Zero) + co1
./venv/lib64/python3.12/site-packages/sympy/functions/elementary/exponential.py:1043:                terms[ex] = terms.get(ex, S.Zero) + coeff*pk[ex]
./venv/lib64/python3.12/site-packages/sympy/functions/special/bsplines.py:345:            [c * d.get(i, S.Zero) for (c, d) in zip(coeff, basis_dicts)], S.Zero
./venv/lib64/python3.12/site-packages/sympy/series/fourier.py:597:        _term = self.an.get(pt, S.Zero) * cos(pt * (pi / self.L) * self.x) \
./venv/lib64/python3.12/site-packages/sympy/series/fourier.py:598:                + self.bn.get(pt, S.Zero) * sin(pt * (pi / self.L) * self.x)
./venv/lib64/python3.12/site-packages/sympy/matrices/eigen.py:250:            all_eigs[val] = all_eigs.get(val, 0) + 1
./venv/lib64/python3.12/site-packages/sympy/physics/units/util.py:41:    camat = Matrix([[dimension_system.get_dimensional_dependencies(i, mark_dimensionless=True).get(j, 0) for i in target_dims] for j in canon_dim_units])
./venv/lib64/python3.12/site-packages/sympy/physics/units/util.py:42:    exprmat = Matrix([dim_dependencies.get(k, 0) for k in canon_dim_units])
./venv/lib64/python3.12/site-packages/sympy/physics/units/dimensions.py:321:                dimensional_dependencies[dim].get(dim, None) != 1)):
./venv/lib64/python3.12/site-packages/sympy/physics/units/dimensions.py:384:            return dict(self.dimensional_dependencies.get(dimension, {dimension: 1}))
./venv/lib64/python3.12/site-packages/sympy/physics/units/dimensions.py:539:            vec.append(self.get_dimensional_dependencies(dim).get(d, 0))
./venv/lib64/python3.12/site-packages/sympy/assumptions/cnf.py:238:        newpred = composite_map.get(pred, None)
./venv/lib64/python3.12/site-packages/sympy/assumptions/cnf.py:243:        newpred = composite_map.get(expr, None)
./venv/lib64/python3.12/site-packages/sympy/assumptions/cnf.py:434:        value = self.encoding.get(literal, None)
./venv/lib64/python3.12/site-packages/sympy/assumptions/refine.py:60:    handler = handlers_dict.get(name, None)
./venv/lib64/python3.12/site-packages/sympy/assumptions/ask.py:577:                prop_facts = known_facts_dict.get(key, None)
./venv/lib64/python3.12/site-packages/sympy/stats/frv.py:255:            return density.get(elem, S.Zero)
./venv/lib64/python3.12/site-packages/sympy/stats/frv.py:268:            d[val] = d.get(val, S.Zero) + prob
./venv/lib64/python3.12/site-packages/sympy/stats/frv.py:500:            d[elem] = d.get(elem, S.Zero) + prob
./venv/lib64/python3.12/site-packages/sympy/stats/stochastic_process_types.py:527:            condition = type(condition)(self.index_of.get(lhs, lhs),
./venv/lib64/python3.12/site-packages/sympy/stats/stochastic_process_types.py:528:                                        self.index_of.get(rhs, rhs))
./venv/lib64/python3.12/site-packages/sympy/stats/stochastic_process_types.py:695:                    if state2cond.get(ris, None) is None:
./venv/lib64/python3.12/site-packages/sympy/stats/rv.py:1477:        results[result] = results.get(result, 0) + 1
./venv/lib64/python3.12/site-packages/sympy/utilities/_compilation/compilation.py:92:        file_kwargs.update(_per_file_kwargs.get(f, {}))
./venv/lib64/python3.12/site-packages/sympy/utilities/misc.py:339:        rv = alias.get(rv, rv)
./venv/lib64/python3.12/site-packages/sympy/parsing/mathematica.py:1076:                return self._atom_conversions.get(expr, sympify(expr))
./venv/lib64/python3.12/site-packages/sympy/parsing/latex/_antlr/latexparser.py:3614:        pred = self._predicates.get(ruleIndex, None)
./venv/lib64/python3.12/site-packages/sympy/parsing/autolev/_antlr/autolevparser.py:3034:        pred = self._predicates.get(ruleIndex, None)
./venv/lib64/python3.12/site-packages/sympy/ntheory/factor_.py:719:        self._cache[n] = max(self._cache.get(n, 0), factor)
./venv/lib64/python3.12/site-packages/sympy/ntheory/factor_.py:1538:                    factors[k] = factors.get(k, 0) + v
./venv/lib64/python3.12/site-packages/sympy/unify/rewrite.py:47:                not condition(*[match.get(var, var) for var in variables])):
./venv/lib64/python3.12/site-packages/sympy/core/assumptions.py:624:        v = cls.__dict__.get(attrname, '')
./venv/lib64/python3.12/site-packages/sympy/core/power.py:1575:                    res[ex] = res.get(ex, S.Zero) + d1[e1]*d2[e2]
./venv/lib64/python3.12/site-packages/sympy/core/power.py:1609:            gterms[e1] = gterms.get(e1, S.Zero) + co1
./venv/lib64/python3.12/site-packages/sympy/core/power.py:1620:                terms[ex] = terms.get(ex, S.Zero) + coeff*tk[ex]
./venv/lib64/python3.12/site-packages/sympy/core/evalf.py:1385:        cached, cached_prec = cache.get(x, (None, MINUS_INF))
./venv/lib64/python3.12/site-packages/sympy/core/basic.py:142:        f = mapping.get(clsname, None)
./venv/lib64/python3.12/site-packages/sympy/core/basic.py:2255:        return rule.get(self, self)
./venv/lib64/python3.12/site-packages/sympy/core/relational.py:166:        cls = cls.ValidRelationOperator.get(rop, None)
./venv/lib64/python3.12/site-packages/sympy/core/exprtools.py:366:                factors[I] = factors.get(I, S.Zero) + i
./venv/lib64/python3.12/site-packages/sympy/core/function.py:224:        return lambda rule, **_: rule.get(self, self)
./venv/lib64/python3.12/site-packages/sympy/core/function.py:543:                fname = MPMATH_TRANSLATIONS.get(fname, None)
./venv/lib64/python3.12/site-packages/sympy/core/function.py:1759:            wrt = {syms.get(vi, vi) for vi in self._wrt_variables}
./venv/lib64/python3.12/site-packages/sympy/core/containers.py:312:        return self._dict.get(key, default)
./venv/lib64/python3.12/site-packages/sympy/vector/basisdependent.py:207:                components[x] = components.get(x, 0) + arg.components[x]
./venv/lib64/python3.12/site-packages/sympy/polys/domains/algebraicfield.py:626:    matrix = [[todom(t.get(a, S.Zero)) for t in terms] for a in algebraics]
./venv/lib64/python3.12/site-packages/sympy/polys/galoistools.py:301:            h.append(f.get(k, K.zero) % p)
./venv/lib64/python3.12/site-packages/sympy/polys/matrices/sdm.py:112:            rowi = self.get(i, None)
./venv/lib64/python3.12/site-packages/sympy/polys/matrices/sdm.py:969:        Emap = {v: list(A.get(v, [])) for v in V}
./venv/lib64/python3.12/site-packages/sympy/polys/matrices/sdm.py:1273:                Ai = Anew.get(i, None)
./venv/lib64/python3.12/site-packages/sympy/polys/matrices/sdm.py:1385:        return [row.get(i, zero) for i, row in self.items() if i < n]
./venv/lib64/python3.12/site-packages/sympy/polys/matrices/sdm.py:1512:                Cij = Ci.get(j, None)
./venv/lib64/python3.12/site-packages/sympy/polys/matrices/sdm.py:1551:                    Ci_list[j].append(Aik * B[k].get(j, zero))
./venv/lib64/python3.12/site-packages/sympy/polys/matrices/sdm.py:1574:                    Aik = A.get(i, {}).get(k, zero)
./venv/lib64/python3.12/site-packages/sympy/polys/matrices/sdm.py:1577:                        Ci = C.get(i, {})
./venv/lib64/python3.12/site-packages/sympy/polys/matrices/sdm.py:1578:                        Cij = Ci.get(j, zero) + Aik * Bkj
./venv/lib64/python3.12/site-packages/sympy/polys/matrices/sdm.py:2066:        for i in nonzero_cols.get(j, ()):
./venv/lib64/python3.12/site-packages/sympy/polys/densebasic.py:943:            h.append(f.get(k, K.zero))
./venv/lib64/python3.12/site-packages/sympy/polys/densebasic.py:973:        h.append(f.get(k, K.zero))
./venv/lib64/python3.12/site-packages/sympy/polys/numberfields/galoisgroups.py:100:        gen = coeff_generators.get(degree, coeff_search(degree, 1))
./venv/lib64/python3.12/site-packages/sympy/polys/rings.py:1292:            coeff = poly.get(monom, zero) + coeff
./venv/lib64/python3.12/site-packages/sympy/polys/rings.py:1785:        return self.get(expv, self.ring.domain.zero)
./venv/lib64/python3.12/site-packages/sympy/codegen/ast.py:206:            return cls.defaults.get(attr, none)
./venv/lib64/python3.12/site-packages/sympy/solvers/ode/single.py:306:        return [match.get(w, S.Zero) for w in self.wilds()]
./venv/lib64/python3.12/site-packages/sympy/solvers/ode/single.py:427:        diffcls = NthAlgebraic._diffx_stored.get(var, None)
./venv/lib64/python3.12/site-packages/sympy/solvers/ode/ode.py:629:                if retdict['best'] == retdict.get(i, None):
./venv/lib64/python3.12/site-packages/sympy/solvers/ode/ode.py:1244:        if not order.get(func, False):
./venv/lib64/python3.12/site-packages/sympy/solvers/solvers.py:91:    >>> assert [d.get(i, i) for i in s] == syms
./venv/lib64/python3.12/site-packages/sympy/solvers/solvers.py:112:    return new_f, [swap_sym.get(i, i) for i in orig], restore
./venv/lib64/python3.12/site-packages/sympy/solvers/solvers.py:836:        default = flags.setdefault(k, bool(flags.get(k, default)))
./venv/lib64/python3.12/site-packages/sympy/solvers/solvers.py:1180:    tuple_format = lambda s: [tuple([i.get(x, x) for x in symbols]) for i in s]
./venv/lib64/python3.12/site-packages/sympy/solvers/solvers.py:1221:        symbols = [swap_sym.get(k, k) for k in symbols]
./venv/lib64/python3.12/site-packages/sympy/solvers/solvers.py:1223:            solution[i] = {swap_sym.get(k, k): v.subs(swap_sym)
./venv/lib64/python3.12/site-packages/sympy/solvers/solvers.py:1290:    return k, {tuple([s.get(ki, ki) for ki in k]) for s in solution}
./venv/lib64/python3.12/site-packages/sympy/solvers/solveset.py:1150:    f_p, f_q, f_r = [pattern_match.get(i, S.Zero) for i in (p, q, r)]
./venv/lib64/python3.12/site-packages/sympy/solvers/solveset.py:3116:            sol = FiniteSet(Tuple(*(sol.get(sym, sym) for sym in symbols)))
./venv/lib64/python3.12/site-packages/sympy/solvers/solveset.py:3161:    sol = FiniteSet(Tuple(*(sol.get(sym, sym) for sym in symbols)))
./venv/lib64/python3.12/site-packages/sympy/solvers/simplex.py:664:        i = univariate.get(x, True)
./venv/lib64/python3.12/site-packages/sympy/solvers/tests/test_solvers.py:1521:        tuple([a.get(i, i) for i in v]) for a in ans]
./venv/lib64/python3.12/site-packages/joblib/test/test_memory_async.py:169:        counter[x] = counter.get(x, 0) + 1
./venv/lib64/python3.12/site-packages/joblib/test/test_parallel.py:2143:    state = status.get(pid, None)
./venv/lib64/python3.12/site-packages/joblib/test/test_memory.py:1516:        counter[x] = counter.get(x, 0) + 1
./venv/lib64/python3.12/site-packages/joblib/_dask.py:287:                f = self.data_futures.get(arg_id, None)
./venv/lib64/python3.12/site-packages/joblib/externals/cloudpickle/cloudpickle.py:294:    module = sys.modules.get(module_name, None)
./venv/lib64/python3.12/site-packages/joblib/_parallel_backends.py:238:                var_value = os.environ.get(var, default_n_threads)
./chroma_inspect_venv/lib/python3.12/site-packages/anyio/lowlevel.py:174:        token = RunvarToken(self, current_vars.get(self, RunVar.NO_VALUE_SET))
./chroma_inspect_venv/lib/python3.12/site-packages/fsspec/generic.py:35:        fs, _ = url_to_fs(url, **storage_options.get(protocol, {}))
./chroma_inspect_venv/lib/python3.12/site-packages/fsspec/mapping.py:115:            key: out[k2] if on_error == "raise" else out.get(k2, KeyError(k2))
./chroma_inspect_venv/lib/python3.12/site-packages/fsspec/implementations/github.py:235:        r = requests.get(url, timeout=self.timeout, **self.kw)
./chroma_inspect_venv/lib/python3.12/site-packages/fsspec/implementations/github.py:301:            r = requests.get(url, timeout=self.timeout, **self.kw)
./chroma_inspect_venv/lib/python3.12/site-packages/fsspec/implementations/gist.py:90:        r = requests.get(url, timeout=self.timeout, **self.kw)
./chroma_inspect_venv/lib/python3.12/site-packages/fsspec/implementations/gist.py:215:        r = requests.get(raw_url, timeout=self.timeout, **self.kw)
./chroma_inspect_venv/lib/python3.12/site-packages/fsspec/implementations/cached.py:585:            self.fs.get(downpath, downfn)
./chroma_inspect_venv/lib/python3.12/site-packages/fsspec/implementations/cached.py:669:            self.fs.get(getpaths, storepaths)
./chroma_inspect_venv/lib/python3.12/site-packages/fsspec/implementations/cached.py:891:        self.fs.get(rpaths, lpaths)
./chroma_inspect_venv/lib/python3.12/site-packages/fsspec/implementations/http.py:827:    r = await session.get(url, headers=headers, **kwargs)
./chroma_inspect_venv/lib/python3.12/site-packages/fsspec/implementations/http.py:856:        r = await session.get(url, allow_redirects=ar, **kwargs)
./chroma_inspect_venv/lib/python3.12/site-packages/fsspec/implementations/http_sync.py:874:    r = session.get(url, headers=headers, **kwargs)
./chroma_inspect_venv/lib/python3.12/site-packages/fsspec/implementations/http_sync.py:897:        r = session.get(url, allow_redirects=ar, **kwargs)
./chroma_inspect_venv/lib/python3.12/site-packages/fsspec/implementations/ftp.py:179:        files = self.dircache.get(path, out)
./chroma_inspect_venv/lib/python3.12/site-packages/fsspec/implementations/reference.py:307:        maybe = self._items.get((field, record), {}).get(ri, False)
./chroma_inspect_venv/lib/python3.12/site-packages/fsspec/implementations/reference.py:410:            self.zmetadata[key] = {**self.zmetadata.get(key, {}), **new_value}
./chroma_inspect_venv/lib/python3.12/site-packages/fsspec/parquet.py:157:                "data": data.get(fn, {}),
./chroma_inspect_venv/lib/python3.12/site-packages/fsspec/parquet.py:159:            size=max(_[1] for _ in data.get(fn, {})),
./chroma_inspect_venv/lib/python3.12/site-packages/fsspec/tests/abstract/get.py:137:            fs.get(s, t)
./chroma_inspect_venv/lib/python3.12/site-packages/fsspec/tests/abstract/get.py:141:            fs.get(s, t, recursive=True)
./chroma_inspect_venv/lib/python3.12/site-packages/fsspec/tests/abstract/get.py:170:            fs.get(s, t, recursive=True, maxdepth=1)
./chroma_inspect_venv/lib/python3.12/site-packages/fsspec/tests/abstract/get.py:217:            fs.get(s, t)
./chroma_inspect_venv/lib/python3.12/site-packages/fsspec/tests/abstract/get.py:221:            fs.get(s, t, recursive=True)
./chroma_inspect_venv/lib/python3.12/site-packages/fsspec/tests/abstract/get.py:235:            fs.get(s, t, recursive=True, maxdepth=1)
./chroma_inspect_venv/lib/python3.12/site-packages/fsspec/tests/abstract/get.py:452:            fs.get(source_files, t)
./chroma_inspect_venv/lib/python3.12/site-packages/fsspec/tests/abstract/get.py:488:        fs.get(source_files, local_join(target, "newdir") + "/")  # Note trailing slash
./chroma_inspect_venv/lib/python3.12/site-packages/fsspec/tests/abstract/get.py:509:            fs.get(src, target, recursive=True)
./chroma_inspect_venv/lib/python3.12/site-packages/fsspec/spec.py:1806:        return self.get(rpath, lpath, recursive=recursive, **kwargs)
./chroma_inspect_venv/lib/python3.12/site-packages/fsspec/dircache.py:58:            if self._times.get(item, 0) - time.time() < -self.listings_expiry_time:
./chroma_inspect_venv/lib/python3.12/site-packages/packaging/version.py:705:        letter = _LETTER_NORMALIZATION.get(letter, letter)
./chroma_inspect_venv/lib/python3.12/site-packages/packaging/tags.py:581:    archs = {"armv8l": ["armv8l", "armv7l"]}.get(arch, [arch])
./chroma_inspect_venv/lib/python3.12/site-packages/onnxruntime/quantization/base_quantizer.py:54:        return self.data.get(key, default_value)
./chroma_inspect_venv/lib/python3.12/site-packages/onnxruntime/quantization/qdq_quantizer.py:845:        tensor_recv_nodes = {node.name for node in self.tensor_to_its_receiving_nodes.get(tensor_name, [])}
./chroma_inspect_venv/lib/python3.12/site-packages/onnxruntime/quantization/qdq_quantizer.py:1158:        axis = self.qdq_op_type_per_channel_support_to_axis.get(op_type, default_axis) if op_type else default_axis
./chroma_inspect_venv/lib/python3.12/site-packages/onnxruntime/quantization/qdq_quantizer.py:1189:            dq_node = self.tensor_to_producing_dq.get(tensor_name, None)
./chroma_inspect_venv/lib/python3.12/site-packages/onnxruntime/quantization/qdq_quantizer.py:1414:            overrides = self.tensor_quant_overrides.get(tensor_name, [{}])
./chroma_inspect_venv/lib/python3.12/site-packages/onnxruntime/quantization/tensor_quant_overrides.py:91:        overrides_list = self.overrides.get(tensor_name, default_list_val)
./chroma_inspect_venv/lib/python3.12/site-packages/onnxruntime/quantization/tensor_quant_overrides.py:105:        overrides_list = self.overrides.get(tensor_name, default_val)
./chroma_inspect_venv/lib/python3.12/site-packages/onnxruntime/quantization/execution_providers/qnn/mixed_precision_overrides_utils.py:181:            all_consumers = {node.name for node in self.consumers.get(tensor_name, [])}
./chroma_inspect_venv/lib/python3.12/site-packages/onnxruntime/quantization/execution_providers/qnn/mixed_precision_overrides_utils.py:284:                for consumer_node in self.consumers.get(tensor_name, []):
./chroma_inspect_venv/lib/python3.12/site-packages/onnxruntime/quantization/neural_compressor/onnx_model.py:408:            parent = self._output_name_to_node.get(tensor_name, None)
./chroma_inspect_venv/lib/python3.12/site-packages/onnxruntime/transformers/profile_result_processor.py:211:        provider = node_provider.get(node_name, "")
./chroma_inspect_venv/lib/python3.12/site-packages/onnxruntime/transformers/profile_result_processor.py:229:        provider = node_provider.get(node_name, "")
./chroma_inspect_venv/lib/python3.12/site-packages/onnxruntime/transformers/profile_result_processor.py:305:        fence_time = op_fence_time.get(op_name, 0)
./chroma_inspect_venv/lib/python3.12/site-packages/onnxruntime/transformers/models/longformer/benchmark_longformer.py:292:    torch_model_name_or_dir = PRETRAINED_LONGFORMER_MODELS.get(model_name, model_name)
./chroma_inspect_venv/lib/python3.12/site-packages/onnxruntime/transformers/models/bert/eval_squad.py:196:                    row[key] = values.get(key, "")
./chroma_inspect_venv/lib/python3.12/site-packages/onnxruntime/transformers/models/stable_diffusion/engine_builder.py:94:        return name_mapping.get(model_name, model_name)
./chroma_inspect_venv/lib/python3.12/site-packages/onnxruntime/transformers/fusion_skip_group_norm.py:149:        parent = output_name_to_node.get(output_name, None)
./chroma_inspect_venv/lib/python3.12/site-packages/onnxruntime/tools/ort_format_model/operator_type_usage_processors.py:150:        return cpp_type in required_types.get(index, set()) or cpp_type in allowed_type_set
./chroma_inspect_venv/lib/python3.12/site-packages/onnxruntime/tools/symbolic_shape_infer.py:359:        merged = [self.suggested_merge_.get(d, d) for d in dims]
./chroma_inspect_venv/lib/python3.12/site-packages/typing_extensions.py:3968:                module = sys.modules.get(module_name, None)
./chroma_inspect_venv/lib/python3.12/site-packages/typing_extensions.py:4073:                    module = sys.modules.get(module_name, None)
./chroma_inspect_venv/lib/python3.12/site-packages/opentelemetry/util/_providers.py:36:            environ.get(provider_environment_variable, f"default_{provider}"),
./chroma_inspect_venv/lib/python3.12/site-packages/opentelemetry/exporter/otlp/proto/grpc/exporter.py:335:            environ.get(OTEL_EXPORTER_OTLP_TIMEOUT, 10)
./chroma_inspect_venv/lib/python3.12/site-packages/opentelemetry/trace/propagation/tracecontext.py:49:        header = getter.get(carrier, self._TRACEPARENT_HEADER_NAME)
./chroma_inspect_venv/lib/python3.12/site-packages/opentelemetry/trace/propagation/tracecontext.py:72:        tracestate_headers = getter.get(carrier, self._TRACESTATE_HEADER_NAME)
./chroma_inspect_venv/lib/python3.12/site-packages/opentelemetry/propagators/textmap.py:87:        val = carrier.get(key, None)
./chroma_inspect_venv/lib/python3.12/site-packages/opentelemetry/context/__init__.py:43:    configured_context = environ.get(OTEL_PYTHON_CONTEXT, default_context)  # type: str
./chroma_inspect_venv/lib/python3.12/site-packages/opentelemetry/sdk/_configuration/__init__.py:142:    return environ.get(OTEL_TRACES_SAMPLER, None)
./chroma_inspect_venv/lib/python3.12/site-packages/opentelemetry/sdk/_configuration/__init__.py:146:    return environ.get(OTEL_PYTHON_ID_GENERATOR, _DEFAULT_ID_GENERATOR)
./chroma_inspect_venv/lib/python3.12/site-packages/opentelemetry/sdk/_configuration/__init__.py:196:    names = environ.get(_EXPORTER_ENV_BY_SIGNAL_TYPE.get(signal_type, ""))
./chroma_inspect_venv/lib/python3.12/site-packages/opentelemetry/sdk/_configuration/__init__.py:223:        exporter_args = exporter_args_map.get(exporter_class, {})
./chroma_inspect_venv/lib/python3.12/site-packages/opentelemetry/sdk/_configuration/__init__.py:240:        exporter_args = exporter_args_map.get(exporter_or_reader_class, {})
./chroma_inspect_venv/lib/python3.12/site-packages/opentelemetry/sdk/_configuration/__init__.py:265:        exporter_args = exporter_args_map.get(exporter_class, {})
./chroma_inspect_venv/lib/python3.12/site-packages/opentelemetry/sdk/trace/_sampling_experimental/_trace_state.py:56:        ot = trace_state.get(OTEL_TRACE_STATE_KEY, "")
./chroma_inspect_venv/lib/python3.12/site-packages/opentelemetry/sdk/trace/export/__init__.py:205:                environ.get(OTEL_BSP_MAX_QUEUE_SIZE, _DEFAULT_MAX_QUEUE_SIZE)
./chroma_inspect_venv/lib/python3.12/site-packages/opentelemetry/sdk/trace/__init__.py:703:            str_value = environ.get(env_var, "").strip().lower()
./chroma_inspect_venv/lib/python3.12/site-packages/opentelemetry/sdk/trace/__init__.py:1213:        disabled = environ.get(OTEL_SDK_DISABLED, "")
./chroma_inspect_venv/lib/python3.12/site-packages/opentelemetry/sdk/metrics/_internal/export/__init__.py:465:                    environ.get(OTEL_METRIC_EXPORT_INTERVAL, 60000)
./chroma_inspect_venv/lib/python3.12/site-packages/opentelemetry/sdk/metrics/_internal/export/__init__.py:475:                    environ.get(OTEL_METRIC_EXPORT_TIMEOUT, 30000)
./chroma_inspect_venv/lib/python3.12/site-packages/opentelemetry/sdk/metrics/_internal/__init__.py:431:                    environ.get(OTEL_METRICS_EXEMPLAR_FILTER, "trace_based")
./chroma_inspect_venv/lib/python3.12/site-packages/opentelemetry/sdk/metrics/_internal/__init__.py:441:        disabled = environ.get(OTEL_SDK_DISABLED, "")
./chroma_inspect_venv/lib/python3.12/site-packages/opentelemetry/sdk/resources/__init__.py:233:        if not resource.attributes.get(SERVICE_NAME, None):
./chroma_inspect_venv/lib/python3.12/site-packages/opentelemetry/sdk/resources/__init__.py:237:                resource.attributes.get(PROCESS_EXECUTABLE_NAME, None),
./chroma_inspect_venv/lib/python3.12/site-packages/opentelemetry/sdk/_logs/_internal/export/__init__.py:259:                environ.get(OTEL_BLRP_MAX_QUEUE_SIZE, _DEFAULT_MAX_QUEUE_SIZE)
./chroma_inspect_venv/lib/python3.12/site-packages/opentelemetry/sdk/_logs/_internal/__init__.py:157:            str_value = environ.get(env_var, "").strip().lower()
./chroma_inspect_venv/lib/python3.12/site-packages/opentelemetry/sdk/_logs/_internal/__init__.py:684:        disabled = environ.get(OTEL_SDK_DISABLED, "")
./chroma_inspect_venv/lib/python3.12/site-packages/opentelemetry/baggage/propagation/__init__.py:53:            getter.get(carrier, self._BAGGAGE_HEADER_NAME)
./chroma_inspect_venv/lib/python3.12/site-packages/pip/_vendor/packaging/version.py:705:        letter = _LETTER_NORMALIZATION.get(letter, letter)
./chroma_inspect_venv/lib/python3.12/site-packages/pip/_vendor/packaging/tags.py:581:    archs = {"armv8l": ["armv8l", "armv7l"]}.get(arch, [arch])
./chroma_inspect_venv/lib/python3.12/site-packages/pip/_vendor/requests/utils.py:874:        proxy = environ_proxies.get(scheme, environ_proxies.get("all"))
./chroma_inspect_venv/lib/python3.12/site-packages/pip/_vendor/requests/structures.py:96:        return self.__dict__.get(key, None)
./chroma_inspect_venv/lib/python3.12/site-packages/pip/_vendor/requests/structures.py:99:        return self.__dict__.get(key, default)
./chroma_inspect_venv/lib/python3.12/site-packages/pip/_vendor/requests/cookies.py:76:        return self._r.headers.get(name, self._new_headers.get(name, default))
./chroma_inspect_venv/lib/python3.12/site-packages/pip/_vendor/urllib3/response.py:672:            "in urllib3 v2.1.0. Instead use HTTPResponse.headers.get(name, default).",
./chroma_inspect_venv/lib/python3.12/site-packages/pip/_vendor/urllib3/response.py:676:        return self.headers.get(name, default)
./chroma_inspect_venv/lib/python3.12/site-packages/pip/_vendor/urllib3/connectionpool.py:1107:    port = port or port_by_scheme.get(scheme, 80)
./chroma_inspect_venv/lib/python3.12/site-packages/pip/_vendor/urllib3/_collections.py:65:            evicted_value = self._container.get(key, _Null)
./chroma_inspect_venv/lib/python3.12/site-packages/pip/_vendor/urllib3/fields.py:238:            if self.headers.get(sort_key, False):
./chroma_inspect_venv/lib/python3.12/site-packages/pip/_vendor/cachecontrol/cache.py:41:        return self.data.get(key, None)
./chroma_inspect_venv/lib/python3.12/site-packages/pip/_vendor/cachecontrol/serialize.py:55:                header_value = request.headers.get(header, None)
./chroma_inspect_venv/lib/python3.12/site-packages/pip/_vendor/cachecontrol/serialize.py:102:            if request.headers.get(header, None) != value:
./chroma_inspect_venv/lib/python3.12/site-packages/pip/_vendor/rich/_emoji_replace.py:21:    default_variant_code = variants.get(default_variant, "") if default_variant else ""
./chroma_inspect_venv/lib/python3.12/site-packages/pip/_vendor/rich/emoji.py:50:            self._char += self.VARIANTS.get(variant, "")
./chroma_inspect_venv/lib/python3.12/site-packages/pip/_vendor/rich/padding.py:87:                Measurement.get(console, options, self.renderable).maximum
./chroma_inspect_venv/lib/python3.12/site-packages/pip/_vendor/rich/padding.py:132:        measure_min, measure_max = Measurement.get(console, options, self.renderable)
./chroma_inspect_venv/lib/python3.12/site-packages/pip/_vendor/rich/styled.py:34:        return Measurement.get(console, options, self.renderable)
./chroma_inspect_venv/lib/python3.12/site-packages/pip/_vendor/rich/align.py:224:        measurement = Measurement.get(console, options, self.renderable)
./chroma_inspect_venv/lib/python3.12/site-packages/pip/_vendor/rich/align.py:281:        measurement = Measurement.get(console, options, self.renderable)
./chroma_inspect_venv/lib/python3.12/site-packages/pip/_vendor/rich/spinner.py:59:        return Measurement.get(console, options, text)
./chroma_inspect_venv/lib/python3.12/site-packages/pip/_vendor/rich/console.py:816:            color_system = _TERM_COLORS.get(colors, ColorSystem.STANDARD)
./chroma_inspect_venv/lib/python3.12/site-packages/pip/_vendor/rich/console.py:1297:        measurement = Measurement.get(self, options or self.options, renderable)
./chroma_inspect_venv/lib/python3.12/site-packages/pip/_vendor/rich/containers.py:50:            Measurement.get(console, options, renderable)
./chroma_inspect_venv/lib/python3.12/site-packages/pip/_vendor/rich/box.py:80:            box = LEGACY_WINDOWS_SUBSTITUTIONS.get(box, box)
./chroma_inspect_venv/lib/python3.12/site-packages/pip/_vendor/rich/box.py:93:        return PLAIN_HEADED_SUBSTITUTIONS.get(self, self)
./chroma_inspect_venv/lib/python3.12/site-packages/pip/_vendor/rich/constrain.py:36:        measurement = Measurement.get(console, options, self.renderable)
./chroma_inspect_venv/lib/python3.12/site-packages/pip/_vendor/distro/distro.py:841:            return table.get(distro_id, distro_id)
./chroma_inspect_venv/lib/python3.12/site-packages/pip/_vendor/distro/distro.py:1061:        return self._os_release_info.get(attribute, "")
./chroma_inspect_venv/lib/python3.12/site-packages/pip/_vendor/distro/distro.py:1070:        return self._lsb_release_info.get(attribute, "")
./chroma_inspect_venv/lib/python3.12/site-packages/pip/_vendor/distro/distro.py:1079:        return self._distro_release_info.get(attribute, "")
./chroma_inspect_venv/lib/python3.12/site-packages/pip/_vendor/distro/distro.py:1088:        return self._uname_info.get(attribute, "")
./chroma_inspect_venv/lib/python3.12/site-packages/pip/_vendor/pkg_resources/__init__.py:448:    return {'PowerPC': 'ppc', 'Power_Macintosh': 'ppc'}.get(machine, machine)
./chroma_inspect_venv/lib/python3.12/site-packages/pip/_vendor/pkg_resources/__init__.py:928:                    requirers = required_by.get(req, None)
./chroma_inspect_venv/lib/python3.12/site-packages/pip/_vendor/pkg_resources/__init__.py:1121:            for extra in self.get(req, ()) + (extras or (None,))
./chroma_inspect_venv/lib/python3.12/site-packages/pip/_vendor/pkg_resources/__init__.py:1198:        return self._distmap.get(distribution_key, [])
./chroma_inspect_venv/lib/python3.12/site-packages/pip/_vendor/pkg_resources/__init__.py:2554:        for package in _namespace_packages.get(parent, ()):
./chroma_inspect_venv/lib/python3.12/site-packages/pip/_vendor/pkg_resources/__init__.py:3072:        deps.extend(dm.get(None, ()))
./chroma_inspect_venv/lib/python3.12/site-packages/pip/_vendor/pkg_resources/__init__.py:3194:            return self._ep_map.get(group, {})
./chroma_inspect_venv/lib/python3.12/site-packages/pip/_vendor/dependency_groups/_implementation.py:175:                if include_group in self._include_graph_ancestors.get(group, ()):
./chroma_inspect_venv/lib/python3.12/site-packages/pip/_vendor/dependency_groups/_implementation.py:180:                    *self._include_graph_ancestors.get(group, ()),
./chroma_inspect_venv/lib/python3.12/site-packages/pip/_vendor/pygments/style.py:88:                styledefs = obj.styles.get(token, '').split()
./chroma_inspect_venv/lib/python3.12/site-packages/pip/_vendor/pygments/style.py:96:                for styledef in obj.styles.get(token, '').split():
./chroma_inspect_venv/lib/python3.12/site-packages/pip/_vendor/pygments/util.py:45:    string = options.get(optname, default)
./chroma_inspect_venv/lib/python3.12/site-packages/pip/_vendor/pygments/util.py:55:    Intuitively, this is `options.get(optname, default)`, but restricted to
./chroma_inspect_venv/lib/python3.12/site-packages/pip/_vendor/pygments/util.py:65:    string = options.get(optname, default)
./chroma_inspect_venv/lib/python3.12/site-packages/pip/_vendor/pygments/util.py:84:    string = options.get(optname, default)
./chroma_inspect_venv/lib/python3.12/site-packages/pip/_vendor/pygments/util.py:100:    val = options.get(optname, default)
./chroma_inspect_venv/lib/python3.12/site-packages/pip/_vendor/pygments/filters/__init__.py:824:            opt = options.get(name, False)
./chroma_inspect_venv/lib/python3.12/site-packages/pip/_vendor/pygments/plugin.py:52:        return groups.get(group_name, [])
./chroma_inspect_venv/lib/python3.12/site-packages/pip/_vendor/resolvelib/structs.py:140:        return itertools.chain(self._accessor(v), self._appends.get(k, ()))
./chroma_inspect_venv/lib/python3.12/site-packages/pip/_vendor/distlib/util.py:1052:        return iter(self._subscribers.get(event, ()))
./chroma_inspect_venv/lib/python3.12/site-packages/pip/_vendor/distlib/util.py:1094:            for p in set(self._preds.get(node, ())):
./chroma_inspect_venv/lib/python3.12/site-packages/pip/_vendor/distlib/util.py:1096:            for s in set(self._succs.get(node, ())):
./chroma_inspect_venv/lib/python3.12/site-packages/pip/_vendor/distlib/util.py:1148:                preds = self._preds.get(step, ())
./chroma_inspect_venv/lib/python3.12/site-packages/pip/_vendor/distlib/util.py:1825:                        result['username'] = config.get(server, 'username')
./chroma_inspect_venv/lib/python3.12/site-packages/pip/_vendor/distlib/util.py:1831:                                result[key] = config.get(server, key)
./chroma_inspect_venv/lib/python3.12/site-packages/pip/_vendor/distlib/util.py:1846:                    repository = config.get(server, 'repository')
./chroma_inspect_venv/lib/python3.12/site-packages/pip/_vendor/distlib/util.py:1850:                    'username': config.get(server, 'username'),
./chroma_inspect_venv/lib/python3.12/site-packages/pip/_vendor/distlib/util.py:1851:                    'password': config.get(server, 'password'),
./chroma_inspect_venv/lib/python3.12/site-packages/pip/_vendor/distlib/compat.py:836:            'od.setdefault(k[,d]) -> od.get(k,d), also set od[k]=d if k not in od'
./chroma_inspect_venv/lib/python3.12/site-packages/pip/_vendor/distlib/compat.py:946:            value = dict.get(self, key, default)
./chroma_inspect_venv/lib/python3.12/site-packages/pip/_vendor/distlib/compat.py:1112:                    converter = self.value_converters.get(prefix, None)
./chroma_inspect_venv/lib/python3.12/site-packages/pip/_vendor/platformdirs/unix.py:238:        media_dir = os.environ.get(env_var, "").strip()
./chroma_inspect_venv/lib/python3.12/site-packages/pip/_internal/cli/spinners.py:179:        return Measurement.get(console, options, text)
./chroma_inspect_venv/lib/python3.12/site-packages/pip/_internal/network/download.py:333:            resp = self._session.get(target_url, headers=headers, stream=True)
./chroma_inspect_venv/lib/python3.12/site-packages/pip/_internal/utils/hashes.py:67:        return hex_digest in self._allowed.get(hash_name, [])
./chroma_inspect_venv/lib/python3.12/site-packages/pip/_internal/utils/temp_dir.py:64:        return self._should_delete.get(kind, True)
./chroma_inspect_venv/lib/python3.12/site-packages/pip/_internal/build_env.py:497:            name: os.environ.get(name, None)
./chroma_inspect_venv/lib/python3.12/site-packages/pip/_internal/resolution/resolvelib/provider.py:224:        requested_order = self._user_requested.get(identifier, math.inf)
./chroma_inspect_venv/lib/python3.12/site-packages/pip/_internal/resolution/resolvelib/factory.py:445:        incompat_ids = {id(c) for c in incompatibilities.get(identifier, ())}
./chroma_inspect_venv/lib/python3.12/site-packages/pip/_internal/resolution/resolvelib/resolver.py:261:        cur_weights = weights.get(node, [])
./chroma_inspect_venv/lib/python3.12/site-packages/pypika/terms.py:1746:        return self.templates.get(dialect, "INTERVAL '{expr} {unit}'").format(expr=expr, unit=unit)
./chroma_inspect_venv/lib/python3.12/site-packages/requests/utils.py:874:        proxy = environ_proxies.get(scheme, environ_proxies.get("all"))
./chroma_inspect_venv/lib/python3.12/site-packages/requests/structures.py:96:        return self.__dict__.get(key, None)
./chroma_inspect_venv/lib/python3.12/site-packages/requests/structures.py:99:        return self.__dict__.get(key, default)
./chroma_inspect_venv/lib/python3.12/site-packages/requests/cookies.py:76:        return self._r.headers.get(name, self._new_headers.get(name, default))
./chroma_inspect_venv/lib/python3.12/site-packages/urllib3/response.py:679:        return self.headers.get(name, default)
./chroma_inspect_venv/lib/python3.12/site-packages/urllib3/connectionpool.py:1130:    port = port or port_by_scheme.get(scheme, 80)
./chroma_inspect_venv/lib/python3.12/site-packages/urllib3/fields.py:299:            if self.headers.get(sort_key, False):
./chroma_inspect_venv/lib/python3.12/site-packages/pydantic/_internal/_model_construction.py:57:        existing: Any = self.get(k, None)
./chroma_inspect_venv/lib/python3.12/site-packages/pydantic/_internal/_generate_schema.py:1551:                        default=namedtuple_cls._field_defaults.get(field_name, Parameter.empty),
./chroma_inspect_venv/lib/python3.12/site-packages/pydantic/_internal/_generics.py:339:    return type_map.get(type_, type_)
./chroma_inspect_venv/lib/python3.12/site-packages/pydantic/_internal/_utils.py:394:        return self.wrapped.get(key, _SENTINEL)
./chroma_inspect_venv/lib/python3.12/site-packages/pydantic/_internal/_decorators.py:379:            attribute = base.__dict__.get(name, _sentinel)
./chroma_inspect_venv/lib/python3.12/site-packages/pydantic/mypy.py:208:                setting = config.get(key, False)
./chroma_inspect_venv/lib/python3.12/site-packages/pydantic/v1/class_validators.py:168:        validators = self.validators.get(name, [])
./chroma_inspect_venv/lib/python3.12/site-packages/pydantic/v1/generics.py:242:                        key: typevars_map.get(value, value) for key, value in _assigned_parameters[cls].items()
./chroma_inspect_venv/lib/python3.12/site-packages/pydantic/v1/generics.py:274:        return type_map.get(type_, type_)
./chroma_inspect_venv/lib/python3.12/site-packages/pydantic/v1/generics.py:325:    new_type = type_map.get(type_, type_)
./chroma_inspect_venv/lib/python3.12/site-packages/pydantic/v1/main.py:183:                elif is_finalvar_with_default_val(ann_type, namespace.get(ann_name, Undefined)):
./chroma_inspect_venv/lib/python3.12/site-packages/pydantic/v1/main.py:187:                    value = namespace.get(ann_name, Undefined)
./chroma_inspect_venv/lib/python3.12/site-packages/pydantic/v1/main.py:224:                        annotation=annotations.get(var_name, Undefined),
./chroma_inspect_venv/lib/python3.12/site-packages/pydantic/v1/main.py:379:            known_field = self.__fields__.get(name, None)
./chroma_inspect_venv/lib/python3.12/site-packages/pydantic/v1/mypy.py:247:                setting = config.get(key, False)
./chroma_inspect_venv/lib/python3.12/site-packages/pydantic/v1/dataclasses.py:456:        known_field = self.__pydantic_model__.__fields__.get(name, None)
./chroma_inspect_venv/lib/python3.12/site-packages/pydantic/v1/fields.py:187:        return [(a, v) for a, v in attrs if v != field_defaults_to_hide.get(a, None)]
./chroma_inspect_venv/lib/python3.12/site-packages/pydantic/v1/fields.py:209:                if current_value is self.__field_constraints__.get(attr_name, None):
./chroma_inspect_venv/lib/python3.12/site-packages/pydantic/json_schema.py:190:        return self.defs_remapping.get(ref, ref)
./chroma_inspect_venv/lib/python3.12/site-packages/pydantic/json_schema.py:193:        return self.json_remapping.get(ref, ref)
./chroma_inspect_venv/lib/python3.12/site-packages/pydantic/json_schema.py:2311:            return self.definitions.get(def_ref, None)
./chroma_inspect_venv/lib/python3.12/site-packages/mpmath/functions/bessel.py:390:        p,v = cache.get(name, (-1,0))
./chroma_inspect_venv/lib/python3.12/site-packages/mpmath/ctx_mp_python.py:1010:        f.__doc__ = function_docs.__dict__.get(name, "Computes the %s of x" % doc)
./chroma_inspect_venv/lib/python3.12/site-packages/mpmath/ctx_mp_python.py:1029:        f_wrapped.__doc__ = function_docs.__dict__.get(name, f.__doc__)
./chroma_inspect_venv/lib/python3.12/site-packages/mpmath/ctx_fp.py:60:        f_wrapped.__doc__ = function_docs.__dict__.get(name, f.__doc__)
./chroma_inspect_venv/lib/python3.12/site-packages/google/protobuf/json_format.py:296:      enum_value = field.enum_type.values_by_number.get(value, None)
./chroma_inspect_venv/lib/python3.12/site-packages/google/protobuf/json_format.py:590:        field = fields_by_json_name.get(name, None)
./chroma_inspect_venv/lib/python3.12/site-packages/google/protobuf/json_format.py:592:          field = message_descriptor.fields_by_name.get(name, None)
./chroma_inspect_venv/lib/python3.12/site-packages/google/protobuf/json_format.py:954:      enum_value = field.enum_type.values_by_name.get(value, None)
./chroma_inspect_venv/lib/python3.12/site-packages/google/protobuf/json_format.py:958:          enum_value = field.enum_type.values_by_number.get(number, None)
./chroma_inspect_venv/lib/python3.12/site-packages/google/protobuf/text_format.py:635:      enum_value = field.enum_type.values_by_number.get(value, None)
./chroma_inspect_venv/lib/python3.12/site-packages/google/protobuf/text_format.py:967:        field = message_descriptor.fields_by_number.get(number, None)
./chroma_inspect_venv/lib/python3.12/site-packages/google/protobuf/text_format.py:971:        field = message_descriptor.fields_by_name.get(name, None)
./chroma_inspect_venv/lib/python3.12/site-packages/google/protobuf/text_format.py:1873:    enum_value = enum_descriptor.values_by_name.get(value, None)
./chroma_inspect_venv/lib/python3.12/site-packages/google/protobuf/text_format.py:1880:    enum_value = enum_descriptor.values_by_number.get(number, None)
./chroma_inspect_venv/lib/python3.12/site-packages/google/protobuf/internal/extension_dict.py:160:    return extensions.get(name, None)
./chroma_inspect_venv/lib/python3.12/site-packages/google/protobuf/internal/extension_dict.py:173:    return extensions.get(number, None)
./chroma_inspect_venv/lib/python3.12/site-packages/google/protobuf/internal/python_message.py:728:    return self._fields.get(field, default_value)
./chroma_inspect_venv/lib/python3.12/site-packages/google/protobuf/internal/python_message.py:1245:      field_des, is_packed = fields_by_tag.get(tag_bytes, (None, None))
./chroma_inspect_venv/lib/python3.12/site-packages/google/protobuf/internal/python_message.py:1429:    nested_field = self._oneofs.get(field, None)
./chroma_inspect_venv/lib/python3.12/site-packages/uvicorn/logging.py:49:        func = self.level_name_colors.get(level_no, default)
./chroma_inspect_venv/lib/python3.12/site-packages/markdown_it/rules_inline/backticks.py:26:    if state.backticksScanned and state.backticks.get(openerLength, 0) <= start:
./chroma_inspect_venv/lib/python3.12/site-packages/markdown_it/rules_inline/link.py:115:        ref = state.env["references"].get(label, None)
./chroma_inspect_venv/lib/python3.12/site-packages/markdown_it/rules_inline/image.py:116:        ref = state.env["references"].get(label, None)
./chroma_inspect_venv/lib/python3.12/site-packages/markdown_it/ruler.py:267:        return self.__cache__.get(chainName, []) or []
./chroma_inspect_venv/lib/python3.12/site-packages/markdown_it/token.py:104:        return self.attrs.get(name, None)
./chroma_inspect_venv/lib/python3.12/site-packages/h11/_state.py:349:            changes = STATE_TRIGGERED_TRANSITIONS.get(joint_state, {})
./chroma_inspect_venv/lib/python3.12/site-packages/rich/_emoji_replace.py:21:    default_variant_code = variants.get(default_variant, "") if default_variant else ""
./chroma_inspect_venv/lib/python3.12/site-packages/rich/emoji.py:50:            self._char += self.VARIANTS.get(variant, "")
./chroma_inspect_venv/lib/python3.12/site-packages/rich/padding.py:87:                Measurement.get(console, options, self.renderable).maximum
./chroma_inspect_venv/lib/python3.12/site-packages/rich/padding.py:132:        measure_min, measure_max = Measurement.get(console, options, self.renderable)
./chroma_inspect_venv/lib/python3.12/site-packages/rich/styled.py:34:        return Measurement.get(console, options, self.renderable)
./chroma_inspect_venv/lib/python3.12/site-packages/rich/align.py:238:        measurement = Measurement.get(console, options, self.renderable)
./chroma_inspect_venv/lib/python3.12/site-packages/rich/align.py:295:        measurement = Measurement.get(console, options, self.renderable)
./chroma_inspect_venv/lib/python3.12/site-packages/rich/spinner.py:59:        return Measurement.get(console, options, text)
./chroma_inspect_venv/lib/python3.12/site-packages/rich/console.py:816:            color_system = _TERM_COLORS.get(colors, ColorSystem.STANDARD)
./chroma_inspect_venv/lib/python3.12/site-packages/rich/console.py:1297:        measurement = Measurement.get(self, options or self.options, renderable)
./chroma_inspect_venv/lib/python3.12/site-packages/rich/containers.py:50:            Measurement.get(console, options, renderable)
./chroma_inspect_venv/lib/python3.12/site-packages/rich/box.py:80:            box = LEGACY_WINDOWS_SUBSTITUTIONS.get(box, box)
./chroma_inspect_venv/lib/python3.12/site-packages/rich/box.py:93:        return PLAIN_HEADED_SUBSTITUTIONS.get(self, self)
./chroma_inspect_venv/lib/python3.12/site-packages/rich/constrain.py:36:        measurement = Measurement.get(console, options, self.renderable)
./chroma_inspect_venv/lib/python3.12/site-packages/grpc/_simple_stubs.py:191:            channel_data = self._mapping.get(key, None)
./chroma_inspect_venv/lib/python3.12/site-packages/grpc/aio/_metadata.py:114:        return self._metadata.get(key, [])
./chroma_inspect_venv/lib/python3.12/site-packages/typer/rich_utils.py:586:    default_arguments = panel_to_arguments.get(ARGUMENTS_PANEL_TITLE, [])
./chroma_inspect_venv/lib/python3.12/site-packages/typer/rich_utils.py:605:    default_options = panel_to_options.get(OPTIONS_PANEL_TITLE, [])
./chroma_inspect_venv/lib/python3.12/site-packages/typer/rich_utils.py:647:        default_commands = panel_to_commands.get(COMMANDS_PANEL_TITLE, [])
./chroma_inspect_venv/lib/python3.12/site-packages/typer/core.py:372:                rich_markup_mode = ctx.obj.get(MARKUP_MODE_KEY, None)
./chroma_inspect_venv/lib/python3.12/site-packages/typer/core.py:594:                rich_markup_mode = ctx.obj.get(MARKUP_MODE_KEY, None)
./chroma_inspect_venv/lib/python3.12/site-packages/typer/cli.py:204:        rich_markup_mode = ctx.obj.get(MARKUP_MODE_KEY, None)
./chroma_inspect_venv/lib/python3.12/site-packages/httpx/_models.py:827:        error_type = error_types.get(status_class, "Invalid status code")
./chroma_inspect_venv/lib/python3.12/site-packages/dateutil/zoneinfo/__init__.py:68:        return self.zones.get(name, default)
./chroma_inspect_venv/lib/python3.12/site-packages/dateutil/tz/_factories.py:39:        instance = cls.__instances.get(key, None)
./chroma_inspect_venv/lib/python3.12/site-packages/dateutil/tz/_factories.py:65:        instance = cls.__instances.get(key, None)
./chroma_inspect_venv/lib/python3.12/site-packages/dateutil/tz/tz.py:383:            setattr(self, attr, kwargs.get(attr, None))
./chroma_inspect_venv/lib/python3.12/site-packages/dateutil/tz/tz.py:1554:                rv = self.__instances.get(name, None)
./chroma_inspect_venv/lib/python3.12/site-packages/click/core.py:555:                return get_current_context().meta.get(LANG_KEY, 'en_US')
./chroma_inspect_venv/lib/python3.12/site-packages/click/core.py:709:            value = self.default_map.get(name, UNSET)
./chroma_inspect_venv/lib/python3.12/site-packages/click/formatting.py:19:            widths[idx] = max(widths.get(idx, 0), term_len(col))
./chroma_inspect_venv/lib/python3.12/site-packages/jsonschema/_utils.py:329:        for subschema in schema.get(keyword, []):
./chroma_inspect_venv/lib/python3.12/site-packages/distro/distro.py:841:            return table.get(distro_id, distro_id)
./chroma_inspect_venv/lib/python3.12/site-packages/distro/distro.py:1061:        return self._os_release_info.get(attribute, "")
./chroma_inspect_venv/lib/python3.12/site-packages/distro/distro.py:1070:        return self._lsb_release_info.get(attribute, "")
./chroma_inspect_venv/lib/python3.12/site-packages/distro/distro.py:1079:        return self._distro_release_info.get(attribute, "")
./chroma_inspect_venv/lib/python3.12/site-packages/distro/distro.py:1088:        return self._uname_info.get(attribute, "")
./chroma_inspect_venv/lib/python3.12/site-packages/humanfriendly/deprecation.py:97:    return REGISTRY.get(module_name, {})
./chroma_inspect_venv/lib/python3.12/site-packages/websockets/sync/connection.py:319:            return self.recv_messages.get(timeout, decode)
./chroma_inspect_venv/lib/python3.12/site-packages/huggingface_hub/cli/cache.py:237:            refs = revision.refs if revision is not None else repo_refs_map.get(repo, frozenset())
./chroma_inspect_venv/lib/python3.12/site-packages/huggingface_hub/cli/cache.py:269:                "refs": sorted(repo_refs_map.get(repo, frozenset())),
./chroma_inspect_venv/lib/python3.12/site-packages/huggingface_hub/cli/cache.py:305:                " ".join(sorted(repo_refs_map.get(repo, frozenset()))),
./chroma_inspect_venv/lib/python3.12/site-packages/huggingface_hub/_commit_api.py:855:                    response = get_session().get(url, headers=headers)
./chroma_inspect_venv/lib/python3.12/site-packages/huggingface_hub/inference/_generated/_async_client.py:3387:        response = await client.get(url, headers=build_hf_headers(token=self.token))
./chroma_inspect_venv/lib/python3.12/site-packages/huggingface_hub/inference/_generated/_async_client.py:3424:        response = await client.get(url, headers=build_hf_headers(token=self.token))
./chroma_inspect_venv/lib/python3.12/site-packages/huggingface_hub/inference/_common.py:386:    return _UNSUPPORTED_TEXT_GENERATION_KWARGS.get(model, [])
./chroma_inspect_venv/lib/python3.12/site-packages/huggingface_hub/inference/_providers/fal_ai.py:82:            status_response = get_session().get(status_url, headers=request_params.headers)
./chroma_inspect_venv/lib/python3.12/site-packages/huggingface_hub/inference/_providers/fal_ai.py:86:        return get_session().get(result_url, headers=request_params.headers).json()
./chroma_inspect_venv/lib/python3.12/site-packages/huggingface_hub/inference/_providers/black_forest_labs.py:51:            response = session.get(url, headers={"Content-Type": "application/json"})  # type: ignore
./chroma_inspect_venv/lib/python3.12/site-packages/huggingface_hub/inference/_providers/zai_org.py:98:            poll_response = session.get(poll_url, headers=request_params.headers)
./chroma_inspect_venv/lib/python3.12/site-packages/huggingface_hub/inference/_providers/wavespeed.py:62:            result_response = get_session().get(result_url, headers=request_params.headers)
./chroma_inspect_venv/lib/python3.12/site-packages/huggingface_hub/inference/_client.py:3334:        response = get_session().get(url, headers=build_hf_headers(token=self.token))
./chroma_inspect_venv/lib/python3.12/site-packages/huggingface_hub/inference/_client.py:3369:        response = get_session().get(url, headers=build_hf_headers(token=self.token))
./chroma_inspect_venv/lib/python3.12/site-packages/huggingface_hub/utils/_auth.py:143:        stored_tokens = {token_name: config.get(token_name, "hf_token") for token_name in config.sections()}
./chroma_inspect_venv/lib/python3.12/site-packages/huggingface_hub/utils/_runtime.py:76:    return _package_versions.get(package_name, "N/A")
./chroma_inspect_venv/lib/python3.12/site-packages/huggingface_hub/utils/_pagination.py:36:    r = session.get(path, params=params, headers=headers)
./chroma_inspect_venv/lib/python3.12/site-packages/huggingface_hub/_login.py:214:        token = tokens.get(token_name, "<not set>")
./chroma_inspect_venv/lib/python3.12/site-packages/huggingface_hub/_inference_endpoints.py:230:                response = get_session().get(_health_url, headers=self._api._build_hf_headers(token=self._token))
./chroma_inspect_venv/lib/python3.12/site-packages/huggingface_hub/hf_api.py:2790:        r = get_session().get(path, headers=headers, timeout=timeout, params=params)
./chroma_inspect_venv/lib/python3.12/site-packages/huggingface_hub/hf_api.py:2860:        r = get_session().get(path, headers=headers, timeout=timeout, params=params)
./chroma_inspect_venv/lib/python3.12/site-packages/huggingface_hub/hf_api.py:2930:        r = get_session().get(path, headers=headers, timeout=timeout, params=params)
./chroma_inspect_venv/lib/python3.12/site-packages/huggingface_hub/hf_api.py:5947:        response = get_session().get(url, headers={**_headers, "range": "bytes=0-100000"})
./chroma_inspect_venv/lib/python3.12/site-packages/huggingface_hub/hf_api.py:5957:            response = get_session().get(url, headers={**_headers, "range": f"bytes=8-{metadata_size + 7}"})
./chroma_inspect_venv/lib/python3.12/site-packages/huggingface_hub/hf_api.py:6338:            resp = get_session().get(path, headers=headers, params=params)
./chroma_inspect_venv/lib/python3.12/site-packages/huggingface_hub/hf_api.py:6414:        resp = get_session().get(path, params={"diff": "1"}, headers=headers)
./chroma_inspect_venv/lib/python3.12/site-packages/huggingface_hub/hf_api.py:10097:        r = get_session().get(path, params=params, headers=self._build_hf_headers(token=token))
./chroma_inspect_venv/lib/python3.12/site-packages/huggingface_hub/hf_api.py:10163:        r = get_session().get(path, headers=headers)
./chroma_inspect_venv/lib/python3.12/site-packages/huggingface_hub/dataclasses.py:145:            for validator in self.__validators__.get(name, []):
./chroma_inspect_venv/lib/python3.12/site-packages/posthog/types.py:240:                key, value, featureFlagPayloads.get(key, None)
./chroma_inspect_venv/lib/python3.12/site-packages/posthog/client.py:1329:            payload = flag_payloads.get(lookup_value, None)
./chroma_inspect_venv/lib/python3.12/site-packages/numpy/f2py/use_rules.py:68:            varsmap[v] = revmap.get(v, v)
./chroma_inspect_venv/lib/python3.12/site-packages/numpy/f2py/auxfuncs.py:303:        for d in rout['vars'].get(a, {}).get('dimension', []):
./chroma_inspect_venv/lib/python3.12/site-packages/numpy/f2py/auxfuncs.py:789:    return rout['f2pymultilines'].get(k, None)
./chroma_inspect_venv/lib/python3.12/site-packages/numpy/f2py/crackfortran.py:2362:            for w in deps.get(word, []) \
./chroma_inspect_venv/lib/python3.12/site-packages/numpy/f2py/crackfortran.py:2589:                        vars[n] = setattrspec(vars.get(n, {}), k)
./chroma_inspect_venv/lib/python3.12/site-packages/numpy/f2py/crackfortran.py:2789:                                for v1 in coeffs_and_deps.get(v, [None, []])[1]:
./chroma_inspect_venv/lib/python3.12/site-packages/numpy/f2py/crackfortran.py:3134:            block['vars'][a] = block['vars'].get(orig_a, {})
./chroma_inspect_venv/lib/python3.12/site-packages/numpy/f2py/tests/test_character.py:20:        clength = {'star': '(*)'}.get(length, length)
./chroma_inspect_venv/lib/python3.12/site-packages/numpy/f2py/tests/test_character.py:81:        fsuffix = {'(*)': 'star'}.get(length, length)
./chroma_inspect_venv/lib/python3.12/site-packages/numpy/f2py/_src_pyf.py:157:            thelist = lnames.get(r, names.get(r, None))
./chroma_inspect_venv/lib/python3.12/site-packages/numpy/f2py/_src_pyf.py:181:        return rules.get(name, (k + 1) * [name])[k]
./chroma_inspect_venv/lib/python3.12/site-packages/numpy/lib/_iotools.py:374:            cnt = seen.get(item, 0)
./chroma_inspect_venv/lib/python3.12/site-packages/numpy/lib/recfunctions.py:265:            lastparent = list(parents.get(lastname, []) or [])
./chroma_inspect_venv/lib/python3.12/site-packages/numpy/lib/recfunctions.py:635:            newname = namemapper.get(name, name)
./chroma_inspect_venv/lib/python3.12/site-packages/numpy/lib/_npyio_impl.py:288:        D.get(k,[,d]) returns D[k] if k in D, else d.  d defaults to None.
./chroma_inspect_venv/lib/python3.12/site-packages/numpy/lib/_npyio_impl.py:290:        return Mapping.get(self, key, default)
./chroma_inspect_venv/lib/python3.12/site-packages/numpy/_utils/_pep440.py:208:        part = _legacy_version_replacement_map.get(part, part)
./chroma_inspect_venv/lib/python3.12/site-packages/numpy/linalg/_linalg.py:184:    return _real_types_map.get(t, default)
./chroma_inspect_venv/lib/python3.12/site-packages/numpy/linalg/_linalg.py:187:    return _complex_types_map.get(t, default)
./chroma_inspect_venv/lib/python3.12/site-packages/numpy/testing/print_coercion_tables.py:158:            row = table.get(from_dt, {})
./chroma_inspect_venv/lib/python3.12/site-packages/numpy/testing/print_coercion_tables.py:160:                print(getattr(row.get(to_dt, no_cast_info), field), end=' ')
./chroma_inspect_venv/lib/python3.12/site-packages/numpy/matrixlib/tests/test_defmatrix.py:304:                args = methodargs.get(attrib, ())
./chroma_inspect_venv/lib/python3.12/site-packages/numpy/_core/records.py:223:        res = fielddict.get(attr, None)
./chroma_inspect_venv/lib/python3.12/site-packages/numpy/_core/records.py:243:        res = fielddict.get(attr, None)
./chroma_inspect_venv/lib/python3.12/site-packages/numpy/_core/getlimits.py:221:                obj = cls._finfo_cache.get(dtype, None)
./chroma_inspect_venv/lib/python3.12/site-packages/numpy/_core/tests/test_regression.py:2345:            item = sctype(values.get(sctype, 1))
./chroma_inspect_venv/lib/python3.12/site-packages/numpy/_core/tests/test_regression.py:2383:            scvalue = sctype(values.get(ch, 3))
./chroma_inspect_venv/lib/python3.12/site-packages/numpy/_core/tests/test_cpu_features.py:90:        map_names = self.features_map.get(feature_name, feature_name)
./chroma_inspect_venv/lib/python3.12/site-packages/numpy/_core/tests/test_umath.py:4338:            cname = name_map.get(fname, fname)
./chroma_inspect_venv/lib/python3.12/site-packages/numpy/_core/tests/test_simd.py:1337:            skip_m = skip_sfx.get(sfx, skip)
./chroma_inspect_venv/lib/python3.12/site-packages/numpy/_core/_internal.py:184:            order1 = _convorder.get(order1, order1)
./chroma_inspect_venv/lib/python3.12/site-packages/numpy/_core/_internal.py:185:            order2 = _convorder.get(order2, order2)
./chroma_inspect_venv/lib/python3.12/site-packages/yaml/resolver.py:149:            wildcard_resolvers = self.yaml_implicit_resolvers.get(None, [])
./chroma_inspect_venv/lib/python3.12/site-packages/pygments/style.py:88:                styledefs = obj.styles.get(token, '').split()
./chroma_inspect_venv/lib/python3.12/site-packages/pygments/style.py:96:                for styledef in obj.styles.get(token, '').split():
./chroma_inspect_venv/lib/python3.12/site-packages/pygments/util.py:45:    string = options.get(optname, default)
./chroma_inspect_venv/lib/python3.12/site-packages/pygments/util.py:55:    Intuitively, this is `options.get(optname, default)`, but restricted to
./chroma_inspect_venv/lib/python3.12/site-packages/pygments/util.py:65:    string = options.get(optname, default)
./chroma_inspect_venv/lib/python3.12/site-packages/pygments/util.py:84:    string = options.get(optname, default)
./chroma_inspect_venv/lib/python3.12/site-packages/pygments/util.py:100:    val = options.get(optname, default)
./chroma_inspect_venv/lib/python3.12/site-packages/pygments/lexers/lisp.py:2415:                token = self.MAPPINGS.get(value, Name.Function)
./chroma_inspect_venv/lib/python3.12/site-packages/pygments/lexers/robotframework.py:143:        return self._tables.get(name, UnknownTable())
./chroma_inspect_venv/lib/python3.12/site-packages/pygments/formatters/terminal256.py:206:        index = self.best_match.get(color, None)
./chroma_inspect_venv/lib/python3.12/site-packages/pygments/filters/__init__.py:824:            opt = options.get(name, False)
./chroma_inspect_venv/lib/python3.12/site-packages/pygments/plugin.py:52:        return groups.get(group_name, [])
./chroma_inspect_venv/lib/python3.12/site-packages/httpcore/_async/socks_proxy.py:66:        requested = AUTH_METHODS.get(auth_method, "UNKNOWN")
./chroma_inspect_venv/lib/python3.12/site-packages/httpcore/_sync/socks_proxy.py:66:        requested = AUTH_METHODS.get(auth_method, "UNKNOWN")
./chroma_inspect_venv/lib/python3.12/site-packages/websocket/_url.py:177:    value = os.environ.get(env_key, os.environ.get(env_key.upper(), "")).replace(
./chroma_inspect_venv/lib/python3.12/site-packages/websocket/_handshake.py:177:        r = headers.get(k, None)
./chroma_inspect_venv/lib/python3.12/site-packages/attr/_make.py:414:            a = cd.get(attr_name, NOTHING)
./chroma_inspect_venv/lib/python3.12/site-packages/flatbuffers/table.py:110:    return self.Get(validator_flags, self.Pos + off)
./chroma_inspect_venv/lib/python3.12/site-packages/oauthlib/oauth1/rfc5849/request_validator.py:284:            return ClientSecret.get(client_key, 'dummy')
./chroma_inspect_venv/lib/python3.12/site-packages/oauthlib/oauth1/rfc5849/request_validator.py:698:            request_token = RequestToken.get(token, None)
./chroma_inspect_venv/lib/python3.12/site-packages/oauthlib/oauth1/rfc5849/request_validator.py:732:            correct_verifier = Verifier.get(client_key, request_token)
./chroma_inspect_venv/lib/python3.12/site-packages/chromadb/test/utils/test_embedding_function_schemas.py:122:        return type_map.get(field_type, "dummy")
./chroma_inspect_venv/lib/python3.12/site-packages/chromadb/execution/executor/local.py:170:                    [_doc(metadata_by_id.get(id, None)) for id in result]
./chroma_inspect_venv/lib/python3.12/site-packages/chromadb/execution/executor/local.py:177:                    [_uri(metadata_by_id.get(id, None)) for id in result]
./chroma_inspect_venv/lib/python3.12/site-packages/chromadb/execution/executor/local.py:184:                    [_clean_metadata(metadata_by_id.get(id, None)) for id in result]
./chroma_inspect_venv/lib/python3.12/site-packages/chromadb/segment/impl/vector/local_persistent_hnsw.py:312:                exists_in_persisted_index = self._id_to_label.get(id, None) is not None
./chroma_inspect_venv/lib/python3.12/site-packages/chromadb/segment/impl/vector/local_hnsw.py:304:                label = self._id_to_label.get(id, None)
./chroma_inspect_venv/lib/python3.12/site-packages/sympy/multipledispatch/utils.py:51:        for m in edges.get(n, ()):
./chroma_inspect_venv/lib/python3.12/site-packages/sympy/multipledispatch/utils.py:56:    if any(incoming_edges.get(v, None) for v in edges):
./chroma_inspect_venv/lib/python3.12/site-packages/sympy/multipledispatch/utils.py:77:            result[val] = result.get(val, ()) + (key, )
./chroma_inspect_venv/lib/python3.12/site-packages/sympy/integrals/rationaltools.py:385:    a, b = H_map.get(S.One, S.Zero), H_map.get(I, S.Zero)
./chroma_inspect_venv/lib/python3.12/site-packages/sympy/integrals/rationaltools.py:386:    c, d = Q_map.get(S.One, S.Zero), Q_map.get(I, S.Zero)
./chroma_inspect_venv/lib/python3.12/site-packages/sympy/integrals/manualintegrate.py:993:            var_index = orthogonal_poly_var_index.get(klass, 1)
./chroma_inspect_venv/lib/python3.12/site-packages/sympy/integrals/manualintegrate.py:1149:    a, b, c = [match.get(i, S.Zero) for i in (a, b, c)]
./chroma_inspect_venv/lib/python3.12/site-packages/sympy/integrals/manualintegrate.py:1734:            [match.get(i, S.Zero) for i in (a, b, m, n)] +
./chroma_inspect_venv/lib/python3.12/site-packages/sympy/integrals/manualintegrate.py:1755:            [match.get(i, S.Zero) for i in (a, b, m, n)] +
./chroma_inspect_venv/lib/python3.12/site-packages/sympy/integrals/manualintegrate.py:1776:            [match.get(i, S.Zero) for i in (a, b, m, n)] +
./chroma_inspect_venv/lib/python3.12/site-packages/sympy/integrals/manualintegrate.py:1803:        a = match.get(A, S.Zero)
./chroma_inspect_venv/lib/python3.12/site-packages/sympy/integrals/manualintegrate.py:1804:        b = match.get(B, S.Zero)
./chroma_inspect_venv/lib/python3.12/site-packages/sympy/integrals/heurisch.py:665:            y = m.get(I, S.Zero)
./chroma_inspect_venv/lib/python3.12/site-packages/sympy/integrals/intpoly.py:304:                value = result.get(m, None)
./chroma_inspect_venv/lib/python3.12/site-packages/sympy/printing/pytorch.py:156:                    var_groups[base_var] = var_groups.get(base_var, 0) + order
./chroma_inspect_venv/lib/python3.12/site-packages/sympy/printing/pytorch.py:158:                    var_groups[var] = var_groups.get(var, 0) + 1
./chroma_inspect_venv/lib/python3.12/site-packages/sympy/printing/llvmjitcode.py:131:        array, idx = self.func_arg_map.get(s, [None, 0])
./chroma_inspect_venv/lib/python3.12/site-packages/sympy/printing/tableform.py:166:                return {'left': 'l', 'right': 'r', 'center': 'c'}.get(a, a)
./chroma_inspect_venv/lib/python3.12/site-packages/sympy/printing/tableform.py:168:                return {'<': 'l', '>': 'r', '^': 'c'}.get(a, a)
./chroma_inspect_venv/lib/python3.12/site-packages/sympy/printing/fortran.py:432:        type_ = self.type_aliases.get(type_, type_)
./chroma_inspect_venv/lib/python3.12/site-packages/sympy/printing/fortran.py:433:        type_str = self.type_mappings.get(type_, type_.name)
./chroma_inspect_venv/lib/python3.12/site-packages/sympy/printing/latex.py:224:        self._settings['imaginary_unit_latex'] = imaginary_unit_table.get(imag_unit, imag_unit)
./chroma_inspect_venv/lib/python3.12/site-packages/sympy/printing/latex.py:233:        self._settings["diff_operator_latex"] = diff_operator_table.get(diff_operator, diff_operator)
./chroma_inspect_venv/lib/python3.12/site-packages/sympy/printing/c.py:466:        return self.type_func_suffixes[self.type_aliases.get(type_, type_)]
./chroma_inspect_venv/lib/python3.12/site-packages/sympy/printing/c.py:469:        return self.type_literal_suffixes[self.type_aliases.get(type_, type_)]
./chroma_inspect_venv/lib/python3.12/site-packages/sympy/printing/c.py:472:        alias = self.type_aliases.get(type_, type_)
./chroma_inspect_venv/lib/python3.12/site-packages/sympy/printing/c.py:473:        dflt = self.type_math_macro_suffixes.get(alias, '')
./chroma_inspect_venv/lib/python3.12/site-packages/sympy/printing/c.py:474:        return self.type_math_macro_suffixes.get(type_, dflt)
./chroma_inspect_venv/lib/python3.12/site-packages/sympy/printing/c.py:482:        self.headers.update(self.type_headers.get(type_, set()))
./chroma_inspect_venv/lib/python3.12/site-packages/sympy/printing/c.py:483:        self.macros.update(self.type_macros.get(type_, set()))
./chroma_inspect_venv/lib/python3.12/site-packages/sympy/printing/c.py:484:        return self._print(self.type_mappings.get(type_, type_.name))
./chroma_inspect_venv/lib/python3.12/site-packages/sympy/printing/c.py:514:        type_ = self.type_aliases.get(real, real)
./chroma_inspect_venv/lib/python3.12/site-packages/sympy/printing/c.py:515:        self.macros.update(self.type_macros.get(type_, set()))
./chroma_inspect_venv/lib/python3.12/site-packages/sympy/printing/preview.py:275:        for candidate in candidates.get(output, []):
./chroma_inspect_venv/lib/python3.12/site-packages/sympy/printing/preview.py:365:                cmd.extend(defaultoptions.get(cmd_variant, []))
./chroma_inspect_venv/lib/python3.12/site-packages/sympy/printing/pycode.py:274:        func = self.known_functions.get(name, name)
./chroma_inspect_venv/lib/python3.12/site-packages/sympy/printing/lambdarepr.py:123:        nstr = self._numexpr_functions.get(func_name, None)
./chroma_inspect_venv/lib/python3.12/site-packages/sympy/tensor/array/sparse_ndim_array.py:62:            return self._sparse_array.get(index, S.Zero)
./chroma_inspect_venv/lib/python3.12/site-packages/sympy/tensor/array/expressions/array_expressions.py:1714:            arg_with_ind.indices = [updates.get(i, None) for i in arg_with_ind.indices]
./chroma_inspect_venv/lib/python3.12/site-packages/sympy/tensor/array/expressions/from_indexed_to_array.py:83:    first_indices = [repl.get(i, i) for i in first_indices]
./chroma_inspect_venv/lib/python3.12/site-packages/sympy/tensor/array/expressions/from_indexed_to_array.py:112:        summation_indices = sorted({subindicessets.get(i, i) for i in summation_indices}, key=default_sort_key)
./chroma_inspect_venv/lib/python3.12/site-packages/sympy/tensor/array/expressions/from_indexed_to_array.py:194:        flattened_indices = [kronecker_delta_repl.get(j, j) for i in newindices for j in i]
./chroma_inspect_venv/lib/python3.12/site-packages/sympy/tensor/tensor.py:956:        return self._comm[i].get(j, 0 if i == 0 or j == 0 else None)
./chroma_inspect_venv/lib/python3.12/site-packages/sympy/tensor/tensor.py:4524:        index_map = {name_translation.get(index, index): value for index, value in index_map.items()}
./chroma_inspect_venv/lib/python3.12/site-packages/sympy/tensor/tensor.py:4572:        slice_tuple = tuple(index_map.get(i, slice(None)) for i in ret_indices)
./chroma_inspect_venv/lib/python3.12/site-packages/sympy/simplify/radsimp.py:181:        syms = [reps.get(s, s) for s in syms]
./chroma_inspect_venv/lib/python3.12/site-packages/sympy/simplify/radsimp.py:189:            return {urep.get(k, k).xreplace(urep): v.xreplace(urep)
./chroma_inspect_venv/lib/python3.12/site-packages/sympy/simplify/trigsimp.py:1026:                if res and res.get(c, 0):
./chroma_inspect_venv/lib/python3.12/site-packages/sympy/concrete/expr_with_limits.py:341:        return {reps.get(_, _) for _ in isyms}
./chroma_inspect_venv/lib/python3.12/site-packages/sympy/concrete/summations.py:1652:        assum_true = x._assumptions.get(assum, None)
./chroma_inspect_venv/lib/python3.12/site-packages/sympy/functions/elementary/exponential.py:1027:                    res[ex] = res.get(ex, S.Zero) + d1[e1]*d2[e2]
./chroma_inspect_venv/lib/python3.12/site-packages/sympy/functions/elementary/exponential.py:1034:            pterms[e1] = pterms.get(e1, S.Zero) + co1
./chroma_inspect_venv/lib/python3.12/site-packages/sympy/functions/elementary/exponential.py:1043:                terms[ex] = terms.get(ex, S.Zero) + coeff*pk[ex]
./chroma_inspect_venv/lib/python3.12/site-packages/sympy/functions/special/bsplines.py:345:            [c * d.get(i, S.Zero) for (c, d) in zip(coeff, basis_dicts)], S.Zero
./chroma_inspect_venv/lib/python3.12/site-packages/sympy/series/fourier.py:597:        _term = self.an.get(pt, S.Zero) * cos(pt * (pi / self.L) * self.x) \
./chroma_inspect_venv/lib/python3.12/site-packages/sympy/series/fourier.py:598:                + self.bn.get(pt, S.Zero) * sin(pt * (pi / self.L) * self.x)
./chroma_inspect_venv/lib/python3.12/site-packages/sympy/matrices/eigen.py:250:            all_eigs[val] = all_eigs.get(val, 0) + 1
./chroma_inspect_venv/lib/python3.12/site-packages/sympy/physics/units/util.py:41:    camat = Matrix([[dimension_system.get_dimensional_dependencies(i, mark_dimensionless=True).get(j, 0) for i in target_dims] for j in canon_dim_units])
./chroma_inspect_venv/lib/python3.12/site-packages/sympy/physics/units/util.py:42:    exprmat = Matrix([dim_dependencies.get(k, 0) for k in canon_dim_units])
./chroma_inspect_venv/lib/python3.12/site-packages/sympy/physics/units/dimensions.py:321:                dimensional_dependencies[dim].get(dim, None) != 1)):
./chroma_inspect_venv/lib/python3.12/site-packages/sympy/physics/units/dimensions.py:384:            return dict(self.dimensional_dependencies.get(dimension, {dimension: 1}))
./chroma_inspect_venv/lib/python3.12/site-packages/sympy/physics/units/dimensions.py:539:            vec.append(self.get_dimensional_dependencies(dim).get(d, 0))
./chroma_inspect_venv/lib/python3.12/site-packages/sympy/assumptions/cnf.py:238:        newpred = composite_map.get(pred, None)
./chroma_inspect_venv/lib/python3.12/site-packages/sympy/assumptions/cnf.py:243:        newpred = composite_map.get(expr, None)
./chroma_inspect_venv/lib/python3.12/site-packages/sympy/assumptions/cnf.py:434:        value = self.encoding.get(literal, None)
./chroma_inspect_venv/lib/python3.12/site-packages/sympy/assumptions/refine.py:60:    handler = handlers_dict.get(name, None)
./chroma_inspect_venv/lib/python3.12/site-packages/sympy/assumptions/ask.py:577:                prop_facts = known_facts_dict.get(key, None)
./chroma_inspect_venv/lib/python3.12/site-packages/sympy/stats/frv.py:255:            return density.get(elem, S.Zero)
./chroma_inspect_venv/lib/python3.12/site-packages/sympy/stats/frv.py:268:            d[val] = d.get(val, S.Zero) + prob
./chroma_inspect_venv/lib/python3.12/site-packages/sympy/stats/frv.py:500:            d[elem] = d.get(elem, S.Zero) + prob
./chroma_inspect_venv/lib/python3.12/site-packages/sympy/stats/stochastic_process_types.py:527:            condition = type(condition)(self.index_of.get(lhs, lhs),
./chroma_inspect_venv/lib/python3.12/site-packages/sympy/stats/stochastic_process_types.py:528:                                        self.index_of.get(rhs, rhs))
./chroma_inspect_venv/lib/python3.12/site-packages/sympy/stats/stochastic_process_types.py:695:                    if state2cond.get(ris, None) is None:
./chroma_inspect_venv/lib/python3.12/site-packages/sympy/stats/rv.py:1477:        results[result] = results.get(result, 0) + 1
./chroma_inspect_venv/lib/python3.12/site-packages/sympy/utilities/_compilation/compilation.py:92:        file_kwargs.update(_per_file_kwargs.get(f, {}))
./chroma_inspect_venv/lib/python3.12/site-packages/sympy/utilities/misc.py:339:        rv = alias.get(rv, rv)
./chroma_inspect_venv/lib/python3.12/site-packages/sympy/parsing/mathematica.py:1076:                return self._atom_conversions.get(expr, sympify(expr))
./chroma_inspect_venv/lib/python3.12/site-packages/sympy/parsing/latex/_antlr/latexparser.py:3614:        pred = self._predicates.get(ruleIndex, None)
./chroma_inspect_venv/lib/python3.12/site-packages/sympy/parsing/autolev/_antlr/autolevparser.py:3034:        pred = self._predicates.get(ruleIndex, None)
./chroma_inspect_venv/lib/python3.12/site-packages/sympy/ntheory/factor_.py:719:        self._cache[n] = max(self._cache.get(n, 0), factor)
./chroma_inspect_venv/lib/python3.12/site-packages/sympy/ntheory/factor_.py:1538:                    factors[k] = factors.get(k, 0) + v
./chroma_inspect_venv/lib/python3.12/site-packages/sympy/unify/rewrite.py:47:                not condition(*[match.get(var, var) for var in variables])):
./chroma_inspect_venv/lib/python3.12/site-packages/sympy/core/assumptions.py:624:        v = cls.__dict__.get(attrname, '')
./chroma_inspect_venv/lib/python3.12/site-packages/sympy/core/power.py:1575:                    res[ex] = res.get(ex, S.Zero) + d1[e1]*d2[e2]
./chroma_inspect_venv/lib/python3.12/site-packages/sympy/core/power.py:1609:            gterms[e1] = gterms.get(e1, S.Zero) + co1
./chroma_inspect_venv/lib/python3.12/site-packages/sympy/core/power.py:1620:                terms[ex] = terms.get(ex, S.Zero) + coeff*tk[ex]
./chroma_inspect_venv/lib/python3.12/site-packages/sympy/core/evalf.py:1385:        cached, cached_prec = cache.get(x, (None, MINUS_INF))
./chroma_inspect_venv/lib/python3.12/site-packages/sympy/core/basic.py:142:        f = mapping.get(clsname, None)
./chroma_inspect_venv/lib/python3.12/site-packages/sympy/core/basic.py:2255:        return rule.get(self, self)
./chroma_inspect_venv/lib/python3.12/site-packages/sympy/core/relational.py:166:        cls = cls.ValidRelationOperator.get(rop, None)
./chroma_inspect_venv/lib/python3.12/site-packages/sympy/core/exprtools.py:366:                factors[I] = factors.get(I, S.Zero) + i
./chroma_inspect_venv/lib/python3.12/site-packages/sympy/core/function.py:224:        return lambda rule, **_: rule.get(self, self)
./chroma_inspect_venv/lib/python3.12/site-packages/sympy/core/function.py:543:                fname = MPMATH_TRANSLATIONS.get(fname, None)
./chroma_inspect_venv/lib/python3.12/site-packages/sympy/core/function.py:1759:            wrt = {syms.get(vi, vi) for vi in self._wrt_variables}
./chroma_inspect_venv/lib/python3.12/site-packages/sympy/core/containers.py:312:        return self._dict.get(key, default)
./chroma_inspect_venv/lib/python3.12/site-packages/sympy/vector/basisdependent.py:207:                components[x] = components.get(x, 0) + arg.components[x]
./chroma_inspect_venv/lib/python3.12/site-packages/sympy/polys/domains/algebraicfield.py:626:    matrix = [[todom(t.get(a, S.Zero)) for t in terms] for a in algebraics]
./chroma_inspect_venv/lib/python3.12/site-packages/sympy/polys/galoistools.py:301:            h.append(f.get(k, K.zero) % p)
./chroma_inspect_venv/lib/python3.12/site-packages/sympy/polys/matrices/sdm.py:112:            rowi = self.get(i, None)
./chroma_inspect_venv/lib/python3.12/site-packages/sympy/polys/matrices/sdm.py:969:        Emap = {v: list(A.get(v, [])) for v in V}
./chroma_inspect_venv/lib/python3.12/site-packages/sympy/polys/matrices/sdm.py:1273:                Ai = Anew.get(i, None)
./chroma_inspect_venv/lib/python3.12/site-packages/sympy/polys/matrices/sdm.py:1385:        return [row.get(i, zero) for i, row in self.items() if i < n]
./chroma_inspect_venv/lib/python3.12/site-packages/sympy/polys/matrices/sdm.py:1512:                Cij = Ci.get(j, None)
./chroma_inspect_venv/lib/python3.12/site-packages/sympy/polys/matrices/sdm.py:1551:                    Ci_list[j].append(Aik * B[k].get(j, zero))
./chroma_inspect_venv/lib/python3.12/site-packages/sympy/polys/matrices/sdm.py:1574:                    Aik = A.get(i, {}).get(k, zero)
./chroma_inspect_venv/lib/python3.12/site-packages/sympy/polys/matrices/sdm.py:1577:                        Ci = C.get(i, {})
./chroma_inspect_venv/lib/python3.12/site-packages/sympy/polys/matrices/sdm.py:1578:                        Cij = Ci.get(j, zero) + Aik * Bkj
./chroma_inspect_venv/lib/python3.12/site-packages/sympy/polys/matrices/sdm.py:2066:        for i in nonzero_cols.get(j, ()):
./chroma_inspect_venv/lib/python3.12/site-packages/sympy/polys/densebasic.py:943:            h.append(f.get(k, K.zero))
./chroma_inspect_venv/lib/python3.12/site-packages/sympy/polys/densebasic.py:973:        h.append(f.get(k, K.zero))
./chroma_inspect_venv/lib/python3.12/site-packages/sympy/polys/numberfields/galoisgroups.py:100:        gen = coeff_generators.get(degree, coeff_search(degree, 1))
./chroma_inspect_venv/lib/python3.12/site-packages/sympy/polys/rings.py:1292:            coeff = poly.get(monom, zero) + coeff
./chroma_inspect_venv/lib/python3.12/site-packages/sympy/polys/rings.py:1785:        return self.get(expv, self.ring.domain.zero)
./chroma_inspect_venv/lib/python3.12/site-packages/sympy/codegen/ast.py:206:            return cls.defaults.get(attr, none)
./chroma_inspect_venv/lib/python3.12/site-packages/sympy/solvers/ode/single.py:306:        return [match.get(w, S.Zero) for w in self.wilds()]
./chroma_inspect_venv/lib/python3.12/site-packages/sympy/solvers/ode/single.py:427:        diffcls = NthAlgebraic._diffx_stored.get(var, None)
./chroma_inspect_venv/lib/python3.12/site-packages/sympy/solvers/ode/ode.py:629:                if retdict['best'] == retdict.get(i, None):
./chroma_inspect_venv/lib/python3.12/site-packages/sympy/solvers/ode/ode.py:1244:        if not order.get(func, False):
./chroma_inspect_venv/lib/python3.12/site-packages/sympy/solvers/solvers.py:91:    >>> assert [d.get(i, i) for i in s] == syms
./chroma_inspect_venv/lib/python3.12/site-packages/sympy/solvers/solvers.py:112:    return new_f, [swap_sym.get(i, i) for i in orig], restore
./chroma_inspect_venv/lib/python3.12/site-packages/sympy/solvers/solvers.py:836:        default = flags.setdefault(k, bool(flags.get(k, default)))
./chroma_inspect_venv/lib/python3.12/site-packages/sympy/solvers/solvers.py:1180:    tuple_format = lambda s: [tuple([i.get(x, x) for x in symbols]) for i in s]
./chroma_inspect_venv/lib/python3.12/site-packages/sympy/solvers/solvers.py:1221:        symbols = [swap_sym.get(k, k) for k in symbols]
./chroma_inspect_venv/lib/python3.12/site-packages/sympy/solvers/solvers.py:1223:            solution[i] = {swap_sym.get(k, k): v.subs(swap_sym)
./chroma_inspect_venv/lib/python3.12/site-packages/sympy/solvers/solvers.py:1290:    return k, {tuple([s.get(ki, ki) for ki in k]) for s in solution}
./chroma_inspect_venv/lib/python3.12/site-packages/sympy/solvers/solveset.py:1150:    f_p, f_q, f_r = [pattern_match.get(i, S.Zero) for i in (p, q, r)]
./chroma_inspect_venv/lib/python3.12/site-packages/sympy/solvers/solveset.py:3116:            sol = FiniteSet(Tuple(*(sol.get(sym, sym) for sym in symbols)))
./chroma_inspect_venv/lib/python3.12/site-packages/sympy/solvers/solveset.py:3161:    sol = FiniteSet(Tuple(*(sol.get(sym, sym) for sym in symbols)))
./chroma_inspect_venv/lib/python3.12/site-packages/sympy/solvers/simplex.py:664:        i = univariate.get(x, True)
./chroma_inspect_venv/lib/python3.12/site-packages/sympy/solvers/tests/test_solvers.py:1521:        tuple([a.get(i, i) for i in v]) for a in ans]
./chroma_inspect_venv/lib/python3.12/site-packages/kubernetes/config/kube_config.py:746:            self._merge(item, config.get(item, []) or [], path)
./chroma_inspect_venv/lib/python3.12/site-packages/kubernetes/dynamic/discovery.py:127:                    resource_group = self._cache.get('resources', {}).get(DISCOVERY_PREFIX, {}).get(group['name'], {}).get(version)
./chroma_inspect_venv/lib/python3.12/site-packages/kubernetes/dynamic/resource.py:383:        return self.__dict__.get(name, getattr(self.__dict__, name, None))
./chroma_inspect_venv/lib/python3.12/site-packages/kubernetes/client/api_client.py:373:            return self.rest_client.GET(url,
./chroma_inspect_venv/lib/python3.12/site-packages/kubernetes/stream/ws_client_test.py:58:    return dict_obj.get(key, default)
./chroma_inspect_venv/lib64/python3.12/site-packages/anyio/lowlevel.py:174:        token = RunvarToken(self, current_vars.get(self, RunVar.NO_VALUE_SET))
./chroma_inspect_venv/lib64/python3.12/site-packages/fsspec/generic.py:35:        fs, _ = url_to_fs(url, **storage_options.get(protocol, {}))
./chroma_inspect_venv/lib64/python3.12/site-packages/fsspec/mapping.py:115:            key: out[k2] if on_error == "raise" else out.get(k2, KeyError(k2))
./chroma_inspect_venv/lib64/python3.12/site-packages/fsspec/implementations/github.py:235:        r = requests.get(url, timeout=self.timeout, **self.kw)
./chroma_inspect_venv/lib64/python3.12/site-packages/fsspec/implementations/github.py:301:            r = requests.get(url, timeout=self.timeout, **self.kw)
./chroma_inspect_venv/lib64/python3.12/site-packages/fsspec/implementations/gist.py:90:        r = requests.get(url, timeout=self.timeout, **self.kw)
./chroma_inspect_venv/lib64/python3.12/site-packages/fsspec/implementations/gist.py:215:        r = requests.get(raw_url, timeout=self.timeout, **self.kw)
./chroma_inspect_venv/lib64/python3.12/site-packages/fsspec/implementations/cached.py:585:            self.fs.get(downpath, downfn)
./chroma_inspect_venv/lib64/python3.12/site-packages/fsspec/implementations/cached.py:669:            self.fs.get(getpaths, storepaths)
./chroma_inspect_venv/lib64/python3.12/site-packages/fsspec/implementations/cached.py:891:        self.fs.get(rpaths, lpaths)
./chroma_inspect_venv/lib64/python3.12/site-packages/fsspec/implementations/http.py:827:    r = await session.get(url, headers=headers, **kwargs)
./chroma_inspect_venv/lib64/python3.12/site-packages/fsspec/implementations/http.py:856:        r = await session.get(url, allow_redirects=ar, **kwargs)
./chroma_inspect_venv/lib64/python3.12/site-packages/fsspec/implementations/http_sync.py:874:    r = session.get(url, headers=headers, **kwargs)
./chroma_inspect_venv/lib64/python3.12/site-packages/fsspec/implementations/http_sync.py:897:        r = session.get(url, allow_redirects=ar, **kwargs)
./chroma_inspect_venv/lib64/python3.12/site-packages/fsspec/implementations/ftp.py:179:        files = self.dircache.get(path, out)
./chroma_inspect_venv/lib64/python3.12/site-packages/fsspec/implementations/reference.py:307:        maybe = self._items.get((field, record), {}).get(ri, False)
./chroma_inspect_venv/lib64/python3.12/site-packages/fsspec/implementations/reference.py:410:            self.zmetadata[key] = {**self.zmetadata.get(key, {}), **new_value}
./chroma_inspect_venv/lib64/python3.12/site-packages/fsspec/parquet.py:157:                "data": data.get(fn, {}),
./chroma_inspect_venv/lib64/python3.12/site-packages/fsspec/parquet.py:159:            size=max(_[1] for _ in data.get(fn, {})),
./chroma_inspect_venv/lib64/python3.12/site-packages/fsspec/tests/abstract/get.py:137:            fs.get(s, t)
./chroma_inspect_venv/lib64/python3.12/site-packages/fsspec/tests/abstract/get.py:141:            fs.get(s, t, recursive=True)
./chroma_inspect_venv/lib64/python3.12/site-packages/fsspec/tests/abstract/get.py:170:            fs.get(s, t, recursive=True, maxdepth=1)
./chroma_inspect_venv/lib64/python3.12/site-packages/fsspec/tests/abstract/get.py:217:            fs.get(s, t)
./chroma_inspect_venv/lib64/python3.12/site-packages/fsspec/tests/abstract/get.py:221:            fs.get(s, t, recursive=True)
./chroma_inspect_venv/lib64/python3.12/site-packages/fsspec/tests/abstract/get.py:235:            fs.get(s, t, recursive=True, maxdepth=1)
./chroma_inspect_venv/lib64/python3.12/site-packages/fsspec/tests/abstract/get.py:452:            fs.get(source_files, t)
./chroma_inspect_venv/lib64/python3.12/site-packages/fsspec/tests/abstract/get.py:488:        fs.get(source_files, local_join(target, "newdir") + "/")  # Note trailing slash
./chroma_inspect_venv/lib64/python3.12/site-packages/fsspec/tests/abstract/get.py:509:            fs.get(src, target, recursive=True)
./chroma_inspect_venv/lib64/python3.12/site-packages/fsspec/spec.py:1806:        return self.get(rpath, lpath, recursive=recursive, **kwargs)
./chroma_inspect_venv/lib64/python3.12/site-packages/fsspec/dircache.py:58:            if self._times.get(item, 0) - time.time() < -self.listings_expiry_time:
./chroma_inspect_venv/lib64/python3.12/site-packages/packaging/version.py:705:        letter = _LETTER_NORMALIZATION.get(letter, letter)
./chroma_inspect_venv/lib64/python3.12/site-packages/packaging/tags.py:581:    archs = {"armv8l": ["armv8l", "armv7l"]}.get(arch, [arch])
./chroma_inspect_venv/lib64/python3.12/site-packages/onnxruntime/quantization/base_quantizer.py:54:        return self.data.get(key, default_value)
./chroma_inspect_venv/lib64/python3.12/site-packages/onnxruntime/quantization/qdq_quantizer.py:845:        tensor_recv_nodes = {node.name for node in self.tensor_to_its_receiving_nodes.get(tensor_name, [])}
./chroma_inspect_venv/lib64/python3.12/site-packages/onnxruntime/quantization/qdq_quantizer.py:1158:        axis = self.qdq_op_type_per_channel_support_to_axis.get(op_type, default_axis) if op_type else default_axis
./chroma_inspect_venv/lib64/python3.12/site-packages/onnxruntime/quantization/qdq_quantizer.py:1189:            dq_node = self.tensor_to_producing_dq.get(tensor_name, None)
./chroma_inspect_venv/lib64/python3.12/site-packages/onnxruntime/quantization/qdq_quantizer.py:1414:            overrides = self.tensor_quant_overrides.get(tensor_name, [{}])
./chroma_inspect_venv/lib64/python3.12/site-packages/onnxruntime/quantization/tensor_quant_overrides.py:91:        overrides_list = self.overrides.get(tensor_name, default_list_val)
./chroma_inspect_venv/lib64/python3.12/site-packages/onnxruntime/quantization/tensor_quant_overrides.py:105:        overrides_list = self.overrides.get(tensor_name, default_val)
./chroma_inspect_venv/lib64/python3.12/site-packages/onnxruntime/quantization/execution_providers/qnn/mixed_precision_overrides_utils.py:181:            all_consumers = {node.name for node in self.consumers.get(tensor_name, [])}
./chroma_inspect_venv/lib64/python3.12/site-packages/onnxruntime/quantization/execution_providers/qnn/mixed_precision_overrides_utils.py:284:                for consumer_node in self.consumers.get(tensor_name, []):
./chroma_inspect_venv/lib64/python3.12/site-packages/onnxruntime/quantization/neural_compressor/onnx_model.py:408:            parent = self._output_name_to_node.get(tensor_name, None)
./chroma_inspect_venv/lib64/python3.12/site-packages/onnxruntime/transformers/profile_result_processor.py:211:        provider = node_provider.get(node_name, "")
./chroma_inspect_venv/lib64/python3.12/site-packages/onnxruntime/transformers/profile_result_processor.py:229:        provider = node_provider.get(node_name, "")
./chroma_inspect_venv/lib64/python3.12/site-packages/onnxruntime/transformers/profile_result_processor.py:305:        fence_time = op_fence_time.get(op_name, 0)
./chroma_inspect_venv/lib64/python3.12/site-packages/onnxruntime/transformers/models/longformer/benchmark_longformer.py:292:    torch_model_name_or_dir = PRETRAINED_LONGFORMER_MODELS.get(model_name, model_name)
./chroma_inspect_venv/lib64/python3.12/site-packages/onnxruntime/transformers/models/bert/eval_squad.py:196:                    row[key] = values.get(key, "")
./chroma_inspect_venv/lib64/python3.12/site-packages/onnxruntime/transformers/models/stable_diffusion/engine_builder.py:94:        return name_mapping.get(model_name, model_name)
./chroma_inspect_venv/lib64/python3.12/site-packages/onnxruntime/transformers/fusion_skip_group_norm.py:149:        parent = output_name_to_node.get(output_name, None)
./chroma_inspect_venv/lib64/python3.12/site-packages/onnxruntime/tools/ort_format_model/operator_type_usage_processors.py:150:        return cpp_type in required_types.get(index, set()) or cpp_type in allowed_type_set
./chroma_inspect_venv/lib64/python3.12/site-packages/onnxruntime/tools/symbolic_shape_infer.py:359:        merged = [self.suggested_merge_.get(d, d) for d in dims]
./chroma_inspect_venv/lib64/python3.12/site-packages/typing_extensions.py:3968:                module = sys.modules.get(module_name, None)
./chroma_inspect_venv/lib64/python3.12/site-packages/typing_extensions.py:4073:                    module = sys.modules.get(module_name, None)
./chroma_inspect_venv/lib64/python3.12/site-packages/opentelemetry/util/_providers.py:36:            environ.get(provider_environment_variable, f"default_{provider}"),
./chroma_inspect_venv/lib64/python3.12/site-packages/opentelemetry/exporter/otlp/proto/grpc/exporter.py:335:            environ.get(OTEL_EXPORTER_OTLP_TIMEOUT, 10)
./chroma_inspect_venv/lib64/python3.12/site-packages/opentelemetry/trace/propagation/tracecontext.py:49:        header = getter.get(carrier, self._TRACEPARENT_HEADER_NAME)
./chroma_inspect_venv/lib64/python3.12/site-packages/opentelemetry/trace/propagation/tracecontext.py:72:        tracestate_headers = getter.get(carrier, self._TRACESTATE_HEADER_NAME)
./chroma_inspect_venv/lib64/python3.12/site-packages/opentelemetry/propagators/textmap.py:87:        val = carrier.get(key, None)
./chroma_inspect_venv/lib64/python3.12/site-packages/opentelemetry/context/__init__.py:43:    configured_context = environ.get(OTEL_PYTHON_CONTEXT, default_context)  # type: str
./chroma_inspect_venv/lib64/python3.12/site-packages/opentelemetry/sdk/_configuration/__init__.py:142:    return environ.get(OTEL_TRACES_SAMPLER, None)
./chroma_inspect_venv/lib64/python3.12/site-packages/opentelemetry/sdk/_configuration/__init__.py:146:    return environ.get(OTEL_PYTHON_ID_GENERATOR, _DEFAULT_ID_GENERATOR)
./chroma_inspect_venv/lib64/python3.12/site-packages/opentelemetry/sdk/_configuration/__init__.py:196:    names = environ.get(_EXPORTER_ENV_BY_SIGNAL_TYPE.get(signal_type, ""))
./chroma_inspect_venv/lib64/python3.12/site-packages/opentelemetry/sdk/_configuration/__init__.py:223:        exporter_args = exporter_args_map.get(exporter_class, {})
./chroma_inspect_venv/lib64/python3.12/site-packages/opentelemetry/sdk/_configuration/__init__.py:240:        exporter_args = exporter_args_map.get(exporter_or_reader_class, {})
./chroma_inspect_venv/lib64/python3.12/site-packages/opentelemetry/sdk/_configuration/__init__.py:265:        exporter_args = exporter_args_map.get(exporter_class, {})
./chroma_inspect_venv/lib64/python3.12/site-packages/opentelemetry/sdk/trace/_sampling_experimental/_trace_state.py:56:        ot = trace_state.get(OTEL_TRACE_STATE_KEY, "")
./chroma_inspect_venv/lib64/python3.12/site-packages/opentelemetry/sdk/trace/export/__init__.py:205:                environ.get(OTEL_BSP_MAX_QUEUE_SIZE, _DEFAULT_MAX_QUEUE_SIZE)
./chroma_inspect_venv/lib64/python3.12/site-packages/opentelemetry/sdk/trace/__init__.py:703:            str_value = environ.get(env_var, "").strip().lower()
./chroma_inspect_venv/lib64/python3.12/site-packages/opentelemetry/sdk/trace/__init__.py:1213:        disabled = environ.get(OTEL_SDK_DISABLED, "")
./chroma_inspect_venv/lib64/python3.12/site-packages/opentelemetry/sdk/metrics/_internal/export/__init__.py:465:                    environ.get(OTEL_METRIC_EXPORT_INTERVAL, 60000)
./chroma_inspect_venv/lib64/python3.12/site-packages/opentelemetry/sdk/metrics/_internal/export/__init__.py:475:                    environ.get(OTEL_METRIC_EXPORT_TIMEOUT, 30000)
./chroma_inspect_venv/lib64/python3.12/site-packages/opentelemetry/sdk/metrics/_internal/__init__.py:431:                    environ.get(OTEL_METRICS_EXEMPLAR_FILTER, "trace_based")
./chroma_inspect_venv/lib64/python3.12/site-packages/opentelemetry/sdk/metrics/_internal/__init__.py:441:        disabled = environ.get(OTEL_SDK_DISABLED, "")
./chroma_inspect_venv/lib64/python3.12/site-packages/opentelemetry/sdk/resources/__init__.py:233:        if not resource.attributes.get(SERVICE_NAME, None):
./chroma_inspect_venv/lib64/python3.12/site-packages/opentelemetry/sdk/resources/__init__.py:237:                resource.attributes.get(PROCESS_EXECUTABLE_NAME, None),
./chroma_inspect_venv/lib64/python3.12/site-packages/opentelemetry/sdk/_logs/_internal/export/__init__.py:259:                environ.get(OTEL_BLRP_MAX_QUEUE_SIZE, _DEFAULT_MAX_QUEUE_SIZE)
./chroma_inspect_venv/lib64/python3.12/site-packages/opentelemetry/sdk/_logs/_internal/__init__.py:157:            str_value = environ.get(env_var, "").strip().lower()
./chroma_inspect_venv/lib64/python3.12/site-packages/opentelemetry/sdk/_logs/_internal/__init__.py:684:        disabled = environ.get(OTEL_SDK_DISABLED, "")
./chroma_inspect_venv/lib64/python3.12/site-packages/opentelemetry/baggage/propagation/__init__.py:53:            getter.get(carrier, self._BAGGAGE_HEADER_NAME)
./chroma_inspect_venv/lib64/python3.12/site-packages/pip/_vendor/packaging/version.py:705:        letter = _LETTER_NORMALIZATION.get(letter, letter)
./chroma_inspect_venv/lib64/python3.12/site-packages/pip/_vendor/packaging/tags.py:581:    archs = {"armv8l": ["armv8l", "armv7l"]}.get(arch, [arch])
./chroma_inspect_venv/lib64/python3.12/site-packages/pip/_vendor/requests/utils.py:874:        proxy = environ_proxies.get(scheme, environ_proxies.get("all"))
./chroma_inspect_venv/lib64/python3.12/site-packages/pip/_vendor/requests/structures.py:96:        return self.__dict__.get(key, None)
./chroma_inspect_venv/lib64/python3.12/site-packages/pip/_vendor/requests/structures.py:99:        return self.__dict__.get(key, default)
./chroma_inspect_venv/lib64/python3.12/site-packages/pip/_vendor/requests/cookies.py:76:        return self._r.headers.get(name, self._new_headers.get(name, default))
./chroma_inspect_venv/lib64/python3.12/site-packages/pip/_vendor/urllib3/response.py:672:            "in urllib3 v2.1.0. Instead use HTTPResponse.headers.get(name, default).",
./chroma_inspect_venv/lib64/python3.12/site-packages/pip/_vendor/urllib3/response.py:676:        return self.headers.get(name, default)
./chroma_inspect_venv/lib64/python3.12/site-packages/pip/_vendor/urllib3/connectionpool.py:1107:    port = port or port_by_scheme.get(scheme, 80)
./chroma_inspect_venv/lib64/python3.12/site-packages/pip/_vendor/urllib3/_collections.py:65:            evicted_value = self._container.get(key, _Null)
./chroma_inspect_venv/lib64/python3.12/site-packages/pip/_vendor/urllib3/fields.py:238:            if self.headers.get(sort_key, False):
./chroma_inspect_venv/lib64/python3.12/site-packages/pip/_vendor/cachecontrol/cache.py:41:        return self.data.get(key, None)
./chroma_inspect_venv/lib64/python3.12/site-packages/pip/_vendor/cachecontrol/serialize.py:55:                header_value = request.headers.get(header, None)
./chroma_inspect_venv/lib64/python3.12/site-packages/pip/_vendor/cachecontrol/serialize.py:102:            if request.headers.get(header, None) != value:
./chroma_inspect_venv/lib64/python3.12/site-packages/pip/_vendor/rich/_emoji_replace.py:21:    default_variant_code = variants.get(default_variant, "") if default_variant else ""
./chroma_inspect_venv/lib64/python3.12/site-packages/pip/_vendor/rich/emoji.py:50:            self._char += self.VARIANTS.get(variant, "")
./chroma_inspect_venv/lib64/python3.12/site-packages/pip/_vendor/rich/padding.py:87:                Measurement.get(console, options, self.renderable).maximum
./chroma_inspect_venv/lib64/python3.12/site-packages/pip/_vendor/rich/padding.py:132:        measure_min, measure_max = Measurement.get(console, options, self.renderable)
./chroma_inspect_venv/lib64/python3.12/site-packages/pip/_vendor/rich/styled.py:34:        return Measurement.get(console, options, self.renderable)
./chroma_inspect_venv/lib64/python3.12/site-packages/pip/_vendor/rich/align.py:224:        measurement = Measurement.get(console, options, self.renderable)
./chroma_inspect_venv/lib64/python3.12/site-packages/pip/_vendor/rich/align.py:281:        measurement = Measurement.get(console, options, self.renderable)
./chroma_inspect_venv/lib64/python3.12/site-packages/pip/_vendor/rich/spinner.py:59:        return Measurement.get(console, options, text)
./chroma_inspect_venv/lib64/python3.12/site-packages/pip/_vendor/rich/console.py:816:            color_system = _TERM_COLORS.get(colors, ColorSystem.STANDARD)
./chroma_inspect_venv/lib64/python3.12/site-packages/pip/_vendor/rich/console.py:1297:        measurement = Measurement.get(self, options or self.options, renderable)
./chroma_inspect_venv/lib64/python3.12/site-packages/pip/_vendor/rich/containers.py:50:            Measurement.get(console, options, renderable)
./chroma_inspect_venv/lib64/python3.12/site-packages/pip/_vendor/rich/box.py:80:            box = LEGACY_WINDOWS_SUBSTITUTIONS.get(box, box)
./chroma_inspect_venv/lib64/python3.12/site-packages/pip/_vendor/rich/box.py:93:        return PLAIN_HEADED_SUBSTITUTIONS.get(self, self)
./chroma_inspect_venv/lib64/python3.12/site-packages/pip/_vendor/rich/constrain.py:36:        measurement = Measurement.get(console, options, self.renderable)
./chroma_inspect_venv/lib64/python3.12/site-packages/pip/_vendor/distro/distro.py:841:            return table.get(distro_id, distro_id)
./chroma_inspect_venv/lib64/python3.12/site-packages/pip/_vendor/distro/distro.py:1061:        return self._os_release_info.get(attribute, "")
./chroma_inspect_venv/lib64/python3.12/site-packages/pip/_vendor/distro/distro.py:1070:        return self._lsb_release_info.get(attribute, "")
./chroma_inspect_venv/lib64/python3.12/site-packages/pip/_vendor/distro/distro.py:1079:        return self._distro_release_info.get(attribute, "")
./chroma_inspect_venv/lib64/python3.12/site-packages/pip/_vendor/distro/distro.py:1088:        return self._uname_info.get(attribute, "")
./chroma_inspect_venv/lib64/python3.12/site-packages/pip/_vendor/pkg_resources/__init__.py:448:    return {'PowerPC': 'ppc', 'Power_Macintosh': 'ppc'}.get(machine, machine)
./chroma_inspect_venv/lib64/python3.12/site-packages/pip/_vendor/pkg_resources/__init__.py:928:                    requirers = required_by.get(req, None)
./chroma_inspect_venv/lib64/python3.12/site-packages/pip/_vendor/pkg_resources/__init__.py:1121:            for extra in self.get(req, ()) + (extras or (None,))
./chroma_inspect_venv/lib64/python3.12/site-packages/pip/_vendor/pkg_resources/__init__.py:1198:        return self._distmap.get(distribution_key, [])
./chroma_inspect_venv/lib64/python3.12/site-packages/pip/_vendor/pkg_resources/__init__.py:2554:        for package in _namespace_packages.get(parent, ()):
./chroma_inspect_venv/lib64/python3.12/site-packages/pip/_vendor/pkg_resources/__init__.py:3072:        deps.extend(dm.get(None, ()))
./chroma_inspect_venv/lib64/python3.12/site-packages/pip/_vendor/pkg_resources/__init__.py:3194:            return self._ep_map.get(group, {})
./chroma_inspect_venv/lib64/python3.12/site-packages/pip/_vendor/dependency_groups/_implementation.py:175:                if include_group in self._include_graph_ancestors.get(group, ()):
./chroma_inspect_venv/lib64/python3.12/site-packages/pip/_vendor/dependency_groups/_implementation.py:180:                    *self._include_graph_ancestors.get(group, ()),
./chroma_inspect_venv/lib64/python3.12/site-packages/pip/_vendor/pygments/style.py:88:                styledefs = obj.styles.get(token, '').split()
./chroma_inspect_venv/lib64/python3.12/site-packages/pip/_vendor/pygments/style.py:96:                for styledef in obj.styles.get(token, '').split():
./chroma_inspect_venv/lib64/python3.12/site-packages/pip/_vendor/pygments/util.py:45:    string = options.get(optname, default)
./chroma_inspect_venv/lib64/python3.12/site-packages/pip/_vendor/pygments/util.py:55:    Intuitively, this is `options.get(optname, default)`, but restricted to
./chroma_inspect_venv/lib64/python3.12/site-packages/pip/_vendor/pygments/util.py:65:    string = options.get(optname, default)
./chroma_inspect_venv/lib64/python3.12/site-packages/pip/_vendor/pygments/util.py:84:    string = options.get(optname, default)
./chroma_inspect_venv/lib64/python3.12/site-packages/pip/_vendor/pygments/util.py:100:    val = options.get(optname, default)
./chroma_inspect_venv/lib64/python3.12/site-packages/pip/_vendor/pygments/filters/__init__.py:824:            opt = options.get(name, False)
./chroma_inspect_venv/lib64/python3.12/site-packages/pip/_vendor/pygments/plugin.py:52:        return groups.get(group_name, [])
./chroma_inspect_venv/lib64/python3.12/site-packages/pip/_vendor/resolvelib/structs.py:140:        return itertools.chain(self._accessor(v), self._appends.get(k, ()))
./chroma_inspect_venv/lib64/python3.12/site-packages/pip/_vendor/distlib/util.py:1052:        return iter(self._subscribers.get(event, ()))
./chroma_inspect_venv/lib64/python3.12/site-packages/pip/_vendor/distlib/util.py:1094:            for p in set(self._preds.get(node, ())):
./chroma_inspect_venv/lib64/python3.12/site-packages/pip/_vendor/distlib/util.py:1096:            for s in set(self._succs.get(node, ())):
./chroma_inspect_venv/lib64/python3.12/site-packages/pip/_vendor/distlib/util.py:1148:                preds = self._preds.get(step, ())
./chroma_inspect_venv/lib64/python3.12/site-packages/pip/_vendor/distlib/util.py:1825:                        result['username'] = config.get(server, 'username')
./chroma_inspect_venv/lib64/python3.12/site-packages/pip/_vendor/distlib/util.py:1831:                                result[key] = config.get(server, key)
./chroma_inspect_venv/lib64/python3.12/site-packages/pip/_vendor/distlib/util.py:1846:                    repository = config.get(server, 'repository')
./chroma_inspect_venv/lib64/python3.12/site-packages/pip/_vendor/distlib/util.py:1850:                    'username': config.get(server, 'username'),
./chroma_inspect_venv/lib64/python3.12/site-packages/pip/_vendor/distlib/util.py:1851:                    'password': config.get(server, 'password'),
./chroma_inspect_venv/lib64/python3.12/site-packages/pip/_vendor/distlib/compat.py:836:            'od.setdefault(k[,d]) -> od.get(k,d), also set od[k]=d if k not in od'
./chroma_inspect_venv/lib64/python3.12/site-packages/pip/_vendor/distlib/compat.py:946:            value = dict.get(self, key, default)
./chroma_inspect_venv/lib64/python3.12/site-packages/pip/_vendor/distlib/compat.py:1112:                    converter = self.value_converters.get(prefix, None)
./chroma_inspect_venv/lib64/python3.12/site-packages/pip/_vendor/platformdirs/unix.py:238:        media_dir = os.environ.get(env_var, "").strip()
./chroma_inspect_venv/lib64/python3.12/site-packages/pip/_internal/cli/spinners.py:179:        return Measurement.get(console, options, text)
./chroma_inspect_venv/lib64/python3.12/site-packages/pip/_internal/network/download.py:333:            resp = self._session.get(target_url, headers=headers, stream=True)
./chroma_inspect_venv/lib64/python3.12/site-packages/pip/_internal/utils/hashes.py:67:        return hex_digest in self._allowed.get(hash_name, [])
./chroma_inspect_venv/lib64/python3.12/site-packages/pip/_internal/utils/temp_dir.py:64:        return self._should_delete.get(kind, True)
./chroma_inspect_venv/lib64/python3.12/site-packages/pip/_internal/build_env.py:497:            name: os.environ.get(name, None)
./chroma_inspect_venv/lib64/python3.12/site-packages/pip/_internal/resolution/resolvelib/provider.py:224:        requested_order = self._user_requested.get(identifier, math.inf)
./chroma_inspect_venv/lib64/python3.12/site-packages/pip/_internal/resolution/resolvelib/factory.py:445:        incompat_ids = {id(c) for c in incompatibilities.get(identifier, ())}
./chroma_inspect_venv/lib64/python3.12/site-packages/pip/_internal/resolution/resolvelib/resolver.py:261:        cur_weights = weights.get(node, [])
./chroma_inspect_venv/lib64/python3.12/site-packages/pypika/terms.py:1746:        return self.templates.get(dialect, "INTERVAL '{expr} {unit}'").format(expr=expr, unit=unit)
./chroma_inspect_venv/lib64/python3.12/site-packages/requests/utils.py:874:        proxy = environ_proxies.get(scheme, environ_proxies.get("all"))
./chroma_inspect_venv/lib64/python3.12/site-packages/requests/structures.py:96:        return self.__dict__.get(key, None)
./chroma_inspect_venv/lib64/python3.12/site-packages/requests/structures.py:99:        return self.__dict__.get(key, default)
./chroma_inspect_venv/lib64/python3.12/site-packages/requests/cookies.py:76:        return self._r.headers.get(name, self._new_headers.get(name, default))
./chroma_inspect_venv/lib64/python3.12/site-packages/urllib3/response.py:679:        return self.headers.get(name, default)
./chroma_inspect_venv/lib64/python3.12/site-packages/urllib3/connectionpool.py:1130:    port = port or port_by_scheme.get(scheme, 80)
./chroma_inspect_venv/lib64/python3.12/site-packages/urllib3/fields.py:299:            if self.headers.get(sort_key, False):
./chroma_inspect_venv/lib64/python3.12/site-packages/pydantic/_internal/_model_construction.py:57:        existing: Any = self.get(k, None)
./chroma_inspect_venv/lib64/python3.12/site-packages/pydantic/_internal/_generate_schema.py:1551:                        default=namedtuple_cls._field_defaults.get(field_name, Parameter.empty),
./chroma_inspect_venv/lib64/python3.12/site-packages/pydantic/_internal/_generics.py:339:    return type_map.get(type_, type_)
./chroma_inspect_venv/lib64/python3.12/site-packages/pydantic/_internal/_utils.py:394:        return self.wrapped.get(key, _SENTINEL)
./chroma_inspect_venv/lib64/python3.12/site-packages/pydantic/_internal/_decorators.py:379:            attribute = base.__dict__.get(name, _sentinel)
./chroma_inspect_venv/lib64/python3.12/site-packages/pydantic/mypy.py:208:                setting = config.get(key, False)
./chroma_inspect_venv/lib64/python3.12/site-packages/pydantic/v1/class_validators.py:168:        validators = self.validators.get(name, [])
./chroma_inspect_venv/lib64/python3.12/site-packages/pydantic/v1/generics.py:242:                        key: typevars_map.get(value, value) for key, value in _assigned_parameters[cls].items()
./chroma_inspect_venv/lib64/python3.12/site-packages/pydantic/v1/generics.py:274:        return type_map.get(type_, type_)
./chroma_inspect_venv/lib64/python3.12/site-packages/pydantic/v1/generics.py:325:    new_type = type_map.get(type_, type_)
./chroma_inspect_venv/lib64/python3.12/site-packages/pydantic/v1/main.py:183:                elif is_finalvar_with_default_val(ann_type, namespace.get(ann_name, Undefined)):
./chroma_inspect_venv/lib64/python3.12/site-packages/pydantic/v1/main.py:187:                    value = namespace.get(ann_name, Undefined)
./chroma_inspect_venv/lib64/python3.12/site-packages/pydantic/v1/main.py:224:                        annotation=annotations.get(var_name, Undefined),
./chroma_inspect_venv/lib64/python3.12/site-packages/pydantic/v1/main.py:379:            known_field = self.__fields__.get(name, None)
./chroma_inspect_venv/lib64/python3.12/site-packages/pydantic/v1/mypy.py:247:                setting = config.get(key, False)
./chroma_inspect_venv/lib64/python3.12/site-packages/pydantic/v1/dataclasses.py:456:        known_field = self.__pydantic_model__.__fields__.get(name, None)
./chroma_inspect_venv/lib64/python3.12/site-packages/pydantic/v1/fields.py:187:        return [(a, v) for a, v in attrs if v != field_defaults_to_hide.get(a, None)]
./chroma_inspect_venv/lib64/python3.12/site-packages/pydantic/v1/fields.py:209:                if current_value is self.__field_constraints__.get(attr_name, None):
./chroma_inspect_venv/lib64/python3.12/site-packages/pydantic/json_schema.py:190:        return self.defs_remapping.get(ref, ref)
./chroma_inspect_venv/lib64/python3.12/site-packages/pydantic/json_schema.py:193:        return self.json_remapping.get(ref, ref)
./chroma_inspect_venv/lib64/python3.12/site-packages/pydantic/json_schema.py:2311:            return self.definitions.get(def_ref, None)
./chroma_inspect_venv/lib64/python3.12/site-packages/mpmath/functions/bessel.py:390:        p,v = cache.get(name, (-1,0))
./chroma_inspect_venv/lib64/python3.12/site-packages/mpmath/ctx_mp_python.py:1010:        f.__doc__ = function_docs.__dict__.get(name, "Computes the %s of x" % doc)
./chroma_inspect_venv/lib64/python3.12/site-packages/mpmath/ctx_mp_python.py:1029:        f_wrapped.__doc__ = function_docs.__dict__.get(name, f.__doc__)
./chroma_inspect_venv/lib64/python3.12/site-packages/mpmath/ctx_fp.py:60:        f_wrapped.__doc__ = function_docs.__dict__.get(name, f.__doc__)
./chroma_inspect_venv/lib64/python3.12/site-packages/google/protobuf/json_format.py:296:      enum_value = field.enum_type.values_by_number.get(value, None)
./chroma_inspect_venv/lib64/python3.12/site-packages/google/protobuf/json_format.py:590:        field = fields_by_json_name.get(name, None)
./chroma_inspect_venv/lib64/python3.12/site-packages/google/protobuf/json_format.py:592:          field = message_descriptor.fields_by_name.get(name, None)
./chroma_inspect_venv/lib64/python3.12/site-packages/google/protobuf/json_format.py:954:      enum_value = field.enum_type.values_by_name.get(value, None)
./chroma_inspect_venv/lib64/python3.12/site-packages/google/protobuf/json_format.py:958:          enum_value = field.enum_type.values_by_number.get(number, None)
./chroma_inspect_venv/lib64/python3.12/site-packages/google/protobuf/text_format.py:635:      enum_value = field.enum_type.values_by_number.get(value, None)
./chroma_inspect_venv/lib64/python3.12/site-packages/google/protobuf/text_format.py:967:        field = message_descriptor.fields_by_number.get(number, None)
./chroma_inspect_venv/lib64/python3.12/site-packages/google/protobuf/text_format.py:971:        field = message_descriptor.fields_by_name.get(name, None)
./chroma_inspect_venv/lib64/python3.12/site-packages/google/protobuf/text_format.py:1873:    enum_value = enum_descriptor.values_by_name.get(value, None)
./chroma_inspect_venv/lib64/python3.12/site-packages/google/protobuf/text_format.py:1880:    enum_value = enum_descriptor.values_by_number.get(number, None)
./chroma_inspect_venv/lib64/python3.12/site-packages/google/protobuf/internal/extension_dict.py:160:    return extensions.get(name, None)
./chroma_inspect_venv/lib64/python3.12/site-packages/google/protobuf/internal/extension_dict.py:173:    return extensions.get(number, None)
./chroma_inspect_venv/lib64/python3.12/site-packages/google/protobuf/internal/python_message.py:728:    return self._fields.get(field, default_value)
./chroma_inspect_venv/lib64/python3.12/site-packages/google/protobuf/internal/python_message.py:1245:      field_des, is_packed = fields_by_tag.get(tag_bytes, (None, None))
./chroma_inspect_venv/lib64/python3.12/site-packages/google/protobuf/internal/python_message.py:1429:    nested_field = self._oneofs.get(field, None)
./chroma_inspect_venv/lib64/python3.12/site-packages/uvicorn/logging.py:49:        func = self.level_name_colors.get(level_no, default)
./chroma_inspect_venv/lib64/python3.12/site-packages/markdown_it/rules_inline/backticks.py:26:    if state.backticksScanned and state.backticks.get(openerLength, 0) <= start:
./chroma_inspect_venv/lib64/python3.12/site-packages/markdown_it/rules_inline/link.py:115:        ref = state.env["references"].get(label, None)
./chroma_inspect_venv/lib64/python3.12/site-packages/markdown_it/rules_inline/image.py:116:        ref = state.env["references"].get(label, None)
./chroma_inspect_venv/lib64/python3.12/site-packages/markdown_it/ruler.py:267:        return self.__cache__.get(chainName, []) or []
./chroma_inspect_venv/lib64/python3.12/site-packages/markdown_it/token.py:104:        return self.attrs.get(name, None)
./chroma_inspect_venv/lib64/python3.12/site-packages/h11/_state.py:349:            changes = STATE_TRIGGERED_TRANSITIONS.get(joint_state, {})
./chroma_inspect_venv/lib64/python3.12/site-packages/rich/_emoji_replace.py:21:    default_variant_code = variants.get(default_variant, "") if default_variant else ""
./chroma_inspect_venv/lib64/python3.12/site-packages/rich/emoji.py:50:            self._char += self.VARIANTS.get(variant, "")
./chroma_inspect_venv/lib64/python3.12/site-packages/rich/padding.py:87:                Measurement.get(console, options, self.renderable).maximum
./chroma_inspect_venv/lib64/python3.12/site-packages/rich/padding.py:132:        measure_min, measure_max = Measurement.get(console, options, self.renderable)
./chroma_inspect_venv/lib64/python3.12/site-packages/rich/styled.py:34:        return Measurement.get(console, options, self.renderable)
./chroma_inspect_venv/lib64/python3.12/site-packages/rich/align.py:238:        measurement = Measurement.get(console, options, self.renderable)
./chroma_inspect_venv/lib64/python3.12/site-packages/rich/align.py:295:        measurement = Measurement.get(console, options, self.renderable)
./chroma_inspect_venv/lib64/python3.12/site-packages/rich/spinner.py:59:        return Measurement.get(console, options, text)
./chroma_inspect_venv/lib64/python3.12/site-packages/rich/console.py:816:            color_system = _TERM_COLORS.get(colors, ColorSystem.STANDARD)
./chroma_inspect_venv/lib64/python3.12/site-packages/rich/console.py:1297:        measurement = Measurement.get(self, options or self.options, renderable)
./chroma_inspect_venv/lib64/python3.12/site-packages/rich/containers.py:50:            Measurement.get(console, options, renderable)
./chroma_inspect_venv/lib64/python3.12/site-packages/rich/box.py:80:            box = LEGACY_WINDOWS_SUBSTITUTIONS.get(box, box)
./chroma_inspect_venv/lib64/python3.12/site-packages/rich/box.py:93:        return PLAIN_HEADED_SUBSTITUTIONS.get(self, self)
./chroma_inspect_venv/lib64/python3.12/site-packages/rich/constrain.py:36:        measurement = Measurement.get(console, options, self.renderable)
./chroma_inspect_venv/lib64/python3.12/site-packages/grpc/_simple_stubs.py:191:            channel_data = self._mapping.get(key, None)
./chroma_inspect_venv/lib64/python3.12/site-packages/grpc/aio/_metadata.py:114:        return self._metadata.get(key, [])
./chroma_inspect_venv/lib64/python3.12/site-packages/typer/rich_utils.py:586:    default_arguments = panel_to_arguments.get(ARGUMENTS_PANEL_TITLE, [])
./chroma_inspect_venv/lib64/python3.12/site-packages/typer/rich_utils.py:605:    default_options = panel_to_options.get(OPTIONS_PANEL_TITLE, [])
./chroma_inspect_venv/lib64/python3.12/site-packages/typer/rich_utils.py:647:        default_commands = panel_to_commands.get(COMMANDS_PANEL_TITLE, [])
./chroma_inspect_venv/lib64/python3.12/site-packages/typer/core.py:372:                rich_markup_mode = ctx.obj.get(MARKUP_MODE_KEY, None)
./chroma_inspect_venv/lib64/python3.12/site-packages/typer/core.py:594:                rich_markup_mode = ctx.obj.get(MARKUP_MODE_KEY, None)
./chroma_inspect_venv/lib64/python3.12/site-packages/typer/cli.py:204:        rich_markup_mode = ctx.obj.get(MARKUP_MODE_KEY, None)
./chroma_inspect_venv/lib64/python3.12/site-packages/httpx/_models.py:827:        error_type = error_types.get(status_class, "Invalid status code")
./chroma_inspect_venv/lib64/python3.12/site-packages/dateutil/zoneinfo/__init__.py:68:        return self.zones.get(name, default)
./chroma_inspect_venv/lib64/python3.12/site-packages/dateutil/tz/_factories.py:39:        instance = cls.__instances.get(key, None)
./chroma_inspect_venv/lib64/python3.12/site-packages/dateutil/tz/_factories.py:65:        instance = cls.__instances.get(key, None)
./chroma_inspect_venv/lib64/python3.12/site-packages/dateutil/tz/tz.py:383:            setattr(self, attr, kwargs.get(attr, None))
./chroma_inspect_venv/lib64/python3.12/site-packages/dateutil/tz/tz.py:1554:                rv = self.__instances.get(name, None)
./chroma_inspect_venv/lib64/python3.12/site-packages/click/core.py:555:                return get_current_context().meta.get(LANG_KEY, 'en_US')
./chroma_inspect_venv/lib64/python3.12/site-packages/click/core.py:709:            value = self.default_map.get(name, UNSET)
./chroma_inspect_venv/lib64/python3.12/site-packages/click/formatting.py:19:            widths[idx] = max(widths.get(idx, 0), term_len(col))
./chroma_inspect_venv/lib64/python3.12/site-packages/jsonschema/_utils.py:329:        for subschema in schema.get(keyword, []):
./chroma_inspect_venv/lib64/python3.12/site-packages/distro/distro.py:841:            return table.get(distro_id, distro_id)
./chroma_inspect_venv/lib64/python3.12/site-packages/distro/distro.py:1061:        return self._os_release_info.get(attribute, "")
./chroma_inspect_venv/lib64/python3.12/site-packages/distro/distro.py:1070:        return self._lsb_release_info.get(attribute, "")
./chroma_inspect_venv/lib64/python3.12/site-packages/distro/distro.py:1079:        return self._distro_release_info.get(attribute, "")
./chroma_inspect_venv/lib64/python3.12/site-packages/distro/distro.py:1088:        return self._uname_info.get(attribute, "")
./chroma_inspect_venv/lib64/python3.12/site-packages/humanfriendly/deprecation.py:97:    return REGISTRY.get(module_name, {})
./chroma_inspect_venv/lib64/python3.12/site-packages/websockets/sync/connection.py:319:            return self.recv_messages.get(timeout, decode)
./chroma_inspect_venv/lib64/python3.12/site-packages/huggingface_hub/cli/cache.py:237:            refs = revision.refs if revision is not None else repo_refs_map.get(repo, frozenset())
./chroma_inspect_venv/lib64/python3.12/site-packages/huggingface_hub/cli/cache.py:269:                "refs": sorted(repo_refs_map.get(repo, frozenset())),
./chroma_inspect_venv/lib64/python3.12/site-packages/huggingface_hub/cli/cache.py:305:                " ".join(sorted(repo_refs_map.get(repo, frozenset()))),
./chroma_inspect_venv/lib64/python3.12/site-packages/huggingface_hub/_commit_api.py:855:                    response = get_session().get(url, headers=headers)
./chroma_inspect_venv/lib64/python3.12/site-packages/huggingface_hub/inference/_generated/_async_client.py:3387:        response = await client.get(url, headers=build_hf_headers(token=self.token))
./chroma_inspect_venv/lib64/python3.12/site-packages/huggingface_hub/inference/_generated/_async_client.py:3424:        response = await client.get(url, headers=build_hf_headers(token=self.token))
./chroma_inspect_venv/lib64/python3.12/site-packages/huggingface_hub/inference/_common.py:386:    return _UNSUPPORTED_TEXT_GENERATION_KWARGS.get(model, [])
./chroma_inspect_venv/lib64/python3.12/site-packages/huggingface_hub/inference/_providers/fal_ai.py:82:            status_response = get_session().get(status_url, headers=request_params.headers)
./chroma_inspect_venv/lib64/python3.12/site-packages/huggingface_hub/inference/_providers/fal_ai.py:86:        return get_session().get(result_url, headers=request_params.headers).json()
./chroma_inspect_venv/lib64/python3.12/site-packages/huggingface_hub/inference/_providers/black_forest_labs.py:51:            response = session.get(url, headers={"Content-Type": "application/json"})  # type: ignore
./chroma_inspect_venv/lib64/python3.12/site-packages/huggingface_hub/inference/_providers/zai_org.py:98:            poll_response = session.get(poll_url, headers=request_params.headers)
./chroma_inspect_venv/lib64/python3.12/site-packages/huggingface_hub/inference/_providers/wavespeed.py:62:            result_response = get_session().get(result_url, headers=request_params.headers)
./chroma_inspect_venv/lib64/python3.12/site-packages/huggingface_hub/inference/_client.py:3334:        response = get_session().get(url, headers=build_hf_headers(token=self.token))
./chroma_inspect_venv/lib64/python3.12/site-packages/huggingface_hub/inference/_client.py:3369:        response = get_session().get(url, headers=build_hf_headers(token=self.token))
./chroma_inspect_venv/lib64/python3.12/site-packages/huggingface_hub/utils/_auth.py:143:        stored_tokens = {token_name: config.get(token_name, "hf_token") for token_name in config.sections()}
./chroma_inspect_venv/lib64/python3.12/site-packages/huggingface_hub/utils/_runtime.py:76:    return _package_versions.get(package_name, "N/A")
./chroma_inspect_venv/lib64/python3.12/site-packages/huggingface_hub/utils/_pagination.py:36:    r = session.get(path, params=params, headers=headers)
./chroma_inspect_venv/lib64/python3.12/site-packages/huggingface_hub/_login.py:214:        token = tokens.get(token_name, "<not set>")
./chroma_inspect_venv/lib64/python3.12/site-packages/huggingface_hub/_inference_endpoints.py:230:                response = get_session().get(_health_url, headers=self._api._build_hf_headers(token=self._token))
./chroma_inspect_venv/lib64/python3.12/site-packages/huggingface_hub/hf_api.py:2790:        r = get_session().get(path, headers=headers, timeout=timeout, params=params)
./chroma_inspect_venv/lib64/python3.12/site-packages/huggingface_hub/hf_api.py:2860:        r = get_session().get(path, headers=headers, timeout=timeout, params=params)
./chroma_inspect_venv/lib64/python3.12/site-packages/huggingface_hub/hf_api.py:2930:        r = get_session().get(path, headers=headers, timeout=timeout, params=params)
./chroma_inspect_venv/lib64/python3.12/site-packages/huggingface_hub/hf_api.py:5947:        response = get_session().get(url, headers={**_headers, "range": "bytes=0-100000"})
./chroma_inspect_venv/lib64/python3.12/site-packages/huggingface_hub/hf_api.py:5957:            response = get_session().get(url, headers={**_headers, "range": f"bytes=8-{metadata_size + 7}"})
./chroma_inspect_venv/lib64/python3.12/site-packages/huggingface_hub/hf_api.py:6338:            resp = get_session().get(path, headers=headers, params=params)
./chroma_inspect_venv/lib64/python3.12/site-packages/huggingface_hub/hf_api.py:6414:        resp = get_session().get(path, params={"diff": "1"}, headers=headers)
./chroma_inspect_venv/lib64/python3.12/site-packages/huggingface_hub/hf_api.py:10097:        r = get_session().get(path, params=params, headers=self._build_hf_headers(token=token))
./chroma_inspect_venv/lib64/python3.12/site-packages/huggingface_hub/hf_api.py:10163:        r = get_session().get(path, headers=headers)
./chroma_inspect_venv/lib64/python3.12/site-packages/huggingface_hub/dataclasses.py:145:            for validator in self.__validators__.get(name, []):
./chroma_inspect_venv/lib64/python3.12/site-packages/posthog/types.py:240:                key, value, featureFlagPayloads.get(key, None)
./chroma_inspect_venv/lib64/python3.12/site-packages/posthog/client.py:1329:            payload = flag_payloads.get(lookup_value, None)
./chroma_inspect_venv/lib64/python3.12/site-packages/numpy/f2py/use_rules.py:68:            varsmap[v] = revmap.get(v, v)
./chroma_inspect_venv/lib64/python3.12/site-packages/numpy/f2py/auxfuncs.py:303:        for d in rout['vars'].get(a, {}).get('dimension', []):
./chroma_inspect_venv/lib64/python3.12/site-packages/numpy/f2py/auxfuncs.py:789:    return rout['f2pymultilines'].get(k, None)
./chroma_inspect_venv/lib64/python3.12/site-packages/numpy/f2py/crackfortran.py:2362:            for w in deps.get(word, []) \
./chroma_inspect_venv/lib64/python3.12/site-packages/numpy/f2py/crackfortran.py:2589:                        vars[n] = setattrspec(vars.get(n, {}), k)
./chroma_inspect_venv/lib64/python3.12/site-packages/numpy/f2py/crackfortran.py:2789:                                for v1 in coeffs_and_deps.get(v, [None, []])[1]:
./chroma_inspect_venv/lib64/python3.12/site-packages/numpy/f2py/crackfortran.py:3134:            block['vars'][a] = block['vars'].get(orig_a, {})
./chroma_inspect_venv/lib64/python3.12/site-packages/numpy/f2py/tests/test_character.py:20:        clength = {'star': '(*)'}.get(length, length)
./chroma_inspect_venv/lib64/python3.12/site-packages/numpy/f2py/tests/test_character.py:81:        fsuffix = {'(*)': 'star'}.get(length, length)
./chroma_inspect_venv/lib64/python3.12/site-packages/numpy/f2py/_src_pyf.py:157:            thelist = lnames.get(r, names.get(r, None))
./chroma_inspect_venv/lib64/python3.12/site-packages/numpy/f2py/_src_pyf.py:181:        return rules.get(name, (k + 1) * [name])[k]
./chroma_inspect_venv/lib64/python3.12/site-packages/numpy/lib/_iotools.py:374:            cnt = seen.get(item, 0)
./chroma_inspect_venv/lib64/python3.12/site-packages/numpy/lib/recfunctions.py:265:            lastparent = list(parents.get(lastname, []) or [])
./chroma_inspect_venv/lib64/python3.12/site-packages/numpy/lib/recfunctions.py:635:            newname = namemapper.get(name, name)
./chroma_inspect_venv/lib64/python3.12/site-packages/numpy/lib/_npyio_impl.py:288:        D.get(k,[,d]) returns D[k] if k in D, else d.  d defaults to None.
./chroma_inspect_venv/lib64/python3.12/site-packages/numpy/lib/_npyio_impl.py:290:        return Mapping.get(self, key, default)
./chroma_inspect_venv/lib64/python3.12/site-packages/numpy/_utils/_pep440.py:208:        part = _legacy_version_replacement_map.get(part, part)
./chroma_inspect_venv/lib64/python3.12/site-packages/numpy/linalg/_linalg.py:184:    return _real_types_map.get(t, default)
./chroma_inspect_venv/lib64/python3.12/site-packages/numpy/linalg/_linalg.py:187:    return _complex_types_map.get(t, default)
./chroma_inspect_venv/lib64/python3.12/site-packages/numpy/testing/print_coercion_tables.py:158:            row = table.get(from_dt, {})
./chroma_inspect_venv/lib64/python3.12/site-packages/numpy/testing/print_coercion_tables.py:160:                print(getattr(row.get(to_dt, no_cast_info), field), end=' ')
./chroma_inspect_venv/lib64/python3.12/site-packages/numpy/matrixlib/tests/test_defmatrix.py:304:                args = methodargs.get(attrib, ())
./chroma_inspect_venv/lib64/python3.12/site-packages/numpy/_core/records.py:223:        res = fielddict.get(attr, None)
./chroma_inspect_venv/lib64/python3.12/site-packages/numpy/_core/records.py:243:        res = fielddict.get(attr, None)
./chroma_inspect_venv/lib64/python3.12/site-packages/numpy/_core/getlimits.py:221:                obj = cls._finfo_cache.get(dtype, None)
./chroma_inspect_venv/lib64/python3.12/site-packages/numpy/_core/tests/test_regression.py:2345:            item = sctype(values.get(sctype, 1))
./chroma_inspect_venv/lib64/python3.12/site-packages/numpy/_core/tests/test_regression.py:2383:            scvalue = sctype(values.get(ch, 3))
./chroma_inspect_venv/lib64/python3.12/site-packages/numpy/_core/tests/test_cpu_features.py:90:        map_names = self.features_map.get(feature_name, feature_name)
./chroma_inspect_venv/lib64/python3.12/site-packages/numpy/_core/tests/test_umath.py:4338:            cname = name_map.get(fname, fname)
./chroma_inspect_venv/lib64/python3.12/site-packages/numpy/_core/tests/test_simd.py:1337:            skip_m = skip_sfx.get(sfx, skip)
./chroma_inspect_venv/lib64/python3.12/site-packages/numpy/_core/_internal.py:184:            order1 = _convorder.get(order1, order1)
./chroma_inspect_venv/lib64/python3.12/site-packages/numpy/_core/_internal.py:185:            order2 = _convorder.get(order2, order2)
./chroma_inspect_venv/lib64/python3.12/site-packages/yaml/resolver.py:149:            wildcard_resolvers = self.yaml_implicit_resolvers.get(None, [])
./chroma_inspect_venv/lib64/python3.12/site-packages/pygments/style.py:88:                styledefs = obj.styles.get(token, '').split()
./chroma_inspect_venv/lib64/python3.12/site-packages/pygments/style.py:96:                for styledef in obj.styles.get(token, '').split():
./chroma_inspect_venv/lib64/python3.12/site-packages/pygments/util.py:45:    string = options.get(optname, default)
./chroma_inspect_venv/lib64/python3.12/site-packages/pygments/util.py:55:    Intuitively, this is `options.get(optname, default)`, but restricted to
./chroma_inspect_venv/lib64/python3.12/site-packages/pygments/util.py:65:    string = options.get(optname, default)
./chroma_inspect_venv/lib64/python3.12/site-packages/pygments/util.py:84:    string = options.get(optname, default)
./chroma_inspect_venv/lib64/python3.12/site-packages/pygments/util.py:100:    val = options.get(optname, default)
./chroma_inspect_venv/lib64/python3.12/site-packages/pygments/lexers/lisp.py:2415:                token = self.MAPPINGS.get(value, Name.Function)
./chroma_inspect_venv/lib64/python3.12/site-packages/pygments/lexers/robotframework.py:143:        return self._tables.get(name, UnknownTable())
./chroma_inspect_venv/lib64/python3.12/site-packages/pygments/formatters/terminal256.py:206:        index = self.best_match.get(color, None)
./chroma_inspect_venv/lib64/python3.12/site-packages/pygments/filters/__init__.py:824:            opt = options.get(name, False)
./chroma_inspect_venv/lib64/python3.12/site-packages/pygments/plugin.py:52:        return groups.get(group_name, [])
./chroma_inspect_venv/lib64/python3.12/site-packages/httpcore/_async/socks_proxy.py:66:        requested = AUTH_METHODS.get(auth_method, "UNKNOWN")
./chroma_inspect_venv/lib64/python3.12/site-packages/httpcore/_sync/socks_proxy.py:66:        requested = AUTH_METHODS.get(auth_method, "UNKNOWN")
./chroma_inspect_venv/lib64/python3.12/site-packages/websocket/_url.py:177:    value = os.environ.get(env_key, os.environ.get(env_key.upper(), "")).replace(
./chroma_inspect_venv/lib64/python3.12/site-packages/websocket/_handshake.py:177:        r = headers.get(k, None)
./chroma_inspect_venv/lib64/python3.12/site-packages/attr/_make.py:414:            a = cd.get(attr_name, NOTHING)
./chroma_inspect_venv/lib64/python3.12/site-packages/flatbuffers/table.py:110:    return self.Get(validator_flags, self.Pos + off)
./chroma_inspect_venv/lib64/python3.12/site-packages/oauthlib/oauth1/rfc5849/request_validator.py:284:            return ClientSecret.get(client_key, 'dummy')
./chroma_inspect_venv/lib64/python3.12/site-packages/oauthlib/oauth1/rfc5849/request_validator.py:698:            request_token = RequestToken.get(token, None)
./chroma_inspect_venv/lib64/python3.12/site-packages/oauthlib/oauth1/rfc5849/request_validator.py:732:            correct_verifier = Verifier.get(client_key, request_token)
./chroma_inspect_venv/lib64/python3.12/site-packages/chromadb/test/utils/test_embedding_function_schemas.py:122:        return type_map.get(field_type, "dummy")
./chroma_inspect_venv/lib64/python3.12/site-packages/chromadb/execution/executor/local.py:170:                    [_doc(metadata_by_id.get(id, None)) for id in result]
./chroma_inspect_venv/lib64/python3.12/site-packages/chromadb/execution/executor/local.py:177:                    [_uri(metadata_by_id.get(id, None)) for id in result]
./chroma_inspect_venv/lib64/python3.12/site-packages/chromadb/execution/executor/local.py:184:                    [_clean_metadata(metadata_by_id.get(id, None)) for id in result]
./chroma_inspect_venv/lib64/python3.12/site-packages/chromadb/segment/impl/vector/local_persistent_hnsw.py:312:                exists_in_persisted_index = self._id_to_label.get(id, None) is not None
./chroma_inspect_venv/lib64/python3.12/site-packages/chromadb/segment/impl/vector/local_hnsw.py:304:                label = self._id_to_label.get(id, None)
./chroma_inspect_venv/lib64/python3.12/site-packages/sympy/multipledispatch/utils.py:51:        for m in edges.get(n, ()):
./chroma_inspect_venv/lib64/python3.12/site-packages/sympy/multipledispatch/utils.py:56:    if any(incoming_edges.get(v, None) for v in edges):
./chroma_inspect_venv/lib64/python3.12/site-packages/sympy/multipledispatch/utils.py:77:            result[val] = result.get(val, ()) + (key, )
./chroma_inspect_venv/lib64/python3.12/site-packages/sympy/integrals/rationaltools.py:385:    a, b = H_map.get(S.One, S.Zero), H_map.get(I, S.Zero)
./chroma_inspect_venv/lib64/python3.12/site-packages/sympy/integrals/rationaltools.py:386:    c, d = Q_map.get(S.One, S.Zero), Q_map.get(I, S.Zero)
./chroma_inspect_venv/lib64/python3.12/site-packages/sympy/integrals/manualintegrate.py:993:            var_index = orthogonal_poly_var_index.get(klass, 1)
./chroma_inspect_venv/lib64/python3.12/site-packages/sympy/integrals/manualintegrate.py:1149:    a, b, c = [match.get(i, S.Zero) for i in (a, b, c)]
./chroma_inspect_venv/lib64/python3.12/site-packages/sympy/integrals/manualintegrate.py:1734:            [match.get(i, S.Zero) for i in (a, b, m, n)] +
./chroma_inspect_venv/lib64/python3.12/site-packages/sympy/integrals/manualintegrate.py:1755:            [match.get(i, S.Zero) for i in (a, b, m, n)] +
./chroma_inspect_venv/lib64/python3.12/site-packages/sympy/integrals/manualintegrate.py:1776:            [match.get(i, S.Zero) for i in (a, b, m, n)] +
./chroma_inspect_venv/lib64/python3.12/site-packages/sympy/integrals/manualintegrate.py:1803:        a = match.get(A, S.Zero)
./chroma_inspect_venv/lib64/python3.12/site-packages/sympy/integrals/manualintegrate.py:1804:        b = match.get(B, S.Zero)
./chroma_inspect_venv/lib64/python3.12/site-packages/sympy/integrals/heurisch.py:665:            y = m.get(I, S.Zero)
./chroma_inspect_venv/lib64/python3.12/site-packages/sympy/integrals/intpoly.py:304:                value = result.get(m, None)
./chroma_inspect_venv/lib64/python3.12/site-packages/sympy/printing/pytorch.py:156:                    var_groups[base_var] = var_groups.get(base_var, 0) + order
./chroma_inspect_venv/lib64/python3.12/site-packages/sympy/printing/pytorch.py:158:                    var_groups[var] = var_groups.get(var, 0) + 1
./chroma_inspect_venv/lib64/python3.12/site-packages/sympy/printing/llvmjitcode.py:131:        array, idx = self.func_arg_map.get(s, [None, 0])
./chroma_inspect_venv/lib64/python3.12/site-packages/sympy/printing/tableform.py:166:                return {'left': 'l', 'right': 'r', 'center': 'c'}.get(a, a)
./chroma_inspect_venv/lib64/python3.12/site-packages/sympy/printing/tableform.py:168:                return {'<': 'l', '>': 'r', '^': 'c'}.get(a, a)
./chroma_inspect_venv/lib64/python3.12/site-packages/sympy/printing/fortran.py:432:        type_ = self.type_aliases.get(type_, type_)
./chroma_inspect_venv/lib64/python3.12/site-packages/sympy/printing/fortran.py:433:        type_str = self.type_mappings.get(type_, type_.name)
./chroma_inspect_venv/lib64/python3.12/site-packages/sympy/printing/latex.py:224:        self._settings['imaginary_unit_latex'] = imaginary_unit_table.get(imag_unit, imag_unit)
./chroma_inspect_venv/lib64/python3.12/site-packages/sympy/printing/latex.py:233:        self._settings["diff_operator_latex"] = diff_operator_table.get(diff_operator, diff_operator)
./chroma_inspect_venv/lib64/python3.12/site-packages/sympy/printing/c.py:466:        return self.type_func_suffixes[self.type_aliases.get(type_, type_)]
./chroma_inspect_venv/lib64/python3.12/site-packages/sympy/printing/c.py:469:        return self.type_literal_suffixes[self.type_aliases.get(type_, type_)]
./chroma_inspect_venv/lib64/python3.12/site-packages/sympy/printing/c.py:472:        alias = self.type_aliases.get(type_, type_)
./chroma_inspect_venv/lib64/python3.12/site-packages/sympy/printing/c.py:473:        dflt = self.type_math_macro_suffixes.get(alias, '')
./chroma_inspect_venv/lib64/python3.12/site-packages/sympy/printing/c.py:474:        return self.type_math_macro_suffixes.get(type_, dflt)
./chroma_inspect_venv/lib64/python3.12/site-packages/sympy/printing/c.py:482:        self.headers.update(self.type_headers.get(type_, set()))
./chroma_inspect_venv/lib64/python3.12/site-packages/sympy/printing/c.py:483:        self.macros.update(self.type_macros.get(type_, set()))
./chroma_inspect_venv/lib64/python3.12/site-packages/sympy/printing/c.py:484:        return self._print(self.type_mappings.get(type_, type_.name))
./chroma_inspect_venv/lib64/python3.12/site-packages/sympy/printing/c.py:514:        type_ = self.type_aliases.get(real, real)
./chroma_inspect_venv/lib64/python3.12/site-packages/sympy/printing/c.py:515:        self.macros.update(self.type_macros.get(type_, set()))
./chroma_inspect_venv/lib64/python3.12/site-packages/sympy/printing/preview.py:275:        for candidate in candidates.get(output, []):
./chroma_inspect_venv/lib64/python3.12/site-packages/sympy/printing/preview.py:365:                cmd.extend(defaultoptions.get(cmd_variant, []))
./chroma_inspect_venv/lib64/python3.12/site-packages/sympy/printing/pycode.py:274:        func = self.known_functions.get(name, name)
./chroma_inspect_venv/lib64/python3.12/site-packages/sympy/printing/lambdarepr.py:123:        nstr = self._numexpr_functions.get(func_name, None)
./chroma_inspect_venv/lib64/python3.12/site-packages/sympy/tensor/array/sparse_ndim_array.py:62:            return self._sparse_array.get(index, S.Zero)
./chroma_inspect_venv/lib64/python3.12/site-packages/sympy/tensor/array/expressions/array_expressions.py:1714:            arg_with_ind.indices = [updates.get(i, None) for i in arg_with_ind.indices]
./chroma_inspect_venv/lib64/python3.12/site-packages/sympy/tensor/array/expressions/from_indexed_to_array.py:83:    first_indices = [repl.get(i, i) for i in first_indices]
./chroma_inspect_venv/lib64/python3.12/site-packages/sympy/tensor/array/expressions/from_indexed_to_array.py:112:        summation_indices = sorted({subindicessets.get(i, i) for i in summation_indices}, key=default_sort_key)
./chroma_inspect_venv/lib64/python3.12/site-packages/sympy/tensor/array/expressions/from_indexed_to_array.py:194:        flattened_indices = [kronecker_delta_repl.get(j, j) for i in newindices for j in i]
./chroma_inspect_venv/lib64/python3.12/site-packages/sympy/tensor/tensor.py:956:        return self._comm[i].get(j, 0 if i == 0 or j == 0 else None)
./chroma_inspect_venv/lib64/python3.12/site-packages/sympy/tensor/tensor.py:4524:        index_map = {name_translation.get(index, index): value for index, value in index_map.items()}
./chroma_inspect_venv/lib64/python3.12/site-packages/sympy/tensor/tensor.py:4572:        slice_tuple = tuple(index_map.get(i, slice(None)) for i in ret_indices)
./chroma_inspect_venv/lib64/python3.12/site-packages/sympy/simplify/radsimp.py:181:        syms = [reps.get(s, s) for s in syms]
./chroma_inspect_venv/lib64/python3.12/site-packages/sympy/simplify/radsimp.py:189:            return {urep.get(k, k).xreplace(urep): v.xreplace(urep)
./chroma_inspect_venv/lib64/python3.12/site-packages/sympy/simplify/trigsimp.py:1026:                if res and res.get(c, 0):
./chroma_inspect_venv/lib64/python3.12/site-packages/sympy/concrete/expr_with_limits.py:341:        return {reps.get(_, _) for _ in isyms}
./chroma_inspect_venv/lib64/python3.12/site-packages/sympy/concrete/summations.py:1652:        assum_true = x._assumptions.get(assum, None)
./chroma_inspect_venv/lib64/python3.12/site-packages/sympy/functions/elementary/exponential.py:1027:                    res[ex] = res.get(ex, S.Zero) + d1[e1]*d2[e2]
./chroma_inspect_venv/lib64/python3.12/site-packages/sympy/functions/elementary/exponential.py:1034:            pterms[e1] = pterms.get(e1, S.Zero) + co1
./chroma_inspect_venv/lib64/python3.12/site-packages/sympy/functions/elementary/exponential.py:1043:                terms[ex] = terms.get(ex, S.Zero) + coeff*pk[ex]
./chroma_inspect_venv/lib64/python3.12/site-packages/sympy/functions/special/bsplines.py:345:            [c * d.get(i, S.Zero) for (c, d) in zip(coeff, basis_dicts)], S.Zero
./chroma_inspect_venv/lib64/python3.12/site-packages/sympy/series/fourier.py:597:        _term = self.an.get(pt, S.Zero) * cos(pt * (pi / self.L) * self.x) \
./chroma_inspect_venv/lib64/python3.12/site-packages/sympy/series/fourier.py:598:                + self.bn.get(pt, S.Zero) * sin(pt * (pi / self.L) * self.x)
./chroma_inspect_venv/lib64/python3.12/site-packages/sympy/matrices/eigen.py:250:            all_eigs[val] = all_eigs.get(val, 0) + 1
./chroma_inspect_venv/lib64/python3.12/site-packages/sympy/physics/units/util.py:41:    camat = Matrix([[dimension_system.get_dimensional_dependencies(i, mark_dimensionless=True).get(j, 0) for i in target_dims] for j in canon_dim_units])
./chroma_inspect_venv/lib64/python3.12/site-packages/sympy/physics/units/util.py:42:    exprmat = Matrix([dim_dependencies.get(k, 0) for k in canon_dim_units])
./chroma_inspect_venv/lib64/python3.12/site-packages/sympy/physics/units/dimensions.py:321:                dimensional_dependencies[dim].get(dim, None) != 1)):
./chroma_inspect_venv/lib64/python3.12/site-packages/sympy/physics/units/dimensions.py:384:            return dict(self.dimensional_dependencies.get(dimension, {dimension: 1}))
./chroma_inspect_venv/lib64/python3.12/site-packages/sympy/physics/units/dimensions.py:539:            vec.append(self.get_dimensional_dependencies(dim).get(d, 0))
./chroma_inspect_venv/lib64/python3.12/site-packages/sympy/assumptions/cnf.py:238:        newpred = composite_map.get(pred, None)
./chroma_inspect_venv/lib64/python3.12/site-packages/sympy/assumptions/cnf.py:243:        newpred = composite_map.get(expr, None)
./chroma_inspect_venv/lib64/python3.12/site-packages/sympy/assumptions/cnf.py:434:        value = self.encoding.get(literal, None)
./chroma_inspect_venv/lib64/python3.12/site-packages/sympy/assumptions/refine.py:60:    handler = handlers_dict.get(name, None)
./chroma_inspect_venv/lib64/python3.12/site-packages/sympy/assumptions/ask.py:577:                prop_facts = known_facts_dict.get(key, None)
./chroma_inspect_venv/lib64/python3.12/site-packages/sympy/stats/frv.py:255:            return density.get(elem, S.Zero)
./chroma_inspect_venv/lib64/python3.12/site-packages/sympy/stats/frv.py:268:            d[val] = d.get(val, S.Zero) + prob
./chroma_inspect_venv/lib64/python3.12/site-packages/sympy/stats/frv.py:500:            d[elem] = d.get(elem, S.Zero) + prob
./chroma_inspect_venv/lib64/python3.12/site-packages/sympy/stats/stochastic_process_types.py:527:            condition = type(condition)(self.index_of.get(lhs, lhs),
./chroma_inspect_venv/lib64/python3.12/site-packages/sympy/stats/stochastic_process_types.py:528:                                        self.index_of.get(rhs, rhs))
./chroma_inspect_venv/lib64/python3.12/site-packages/sympy/stats/stochastic_process_types.py:695:                    if state2cond.get(ris, None) is None:
./chroma_inspect_venv/lib64/python3.12/site-packages/sympy/stats/rv.py:1477:        results[result] = results.get(result, 0) + 1
./chroma_inspect_venv/lib64/python3.12/site-packages/sympy/utilities/_compilation/compilation.py:92:        file_kwargs.update(_per_file_kwargs.get(f, {}))
./chroma_inspect_venv/lib64/python3.12/site-packages/sympy/utilities/misc.py:339:        rv = alias.get(rv, rv)
./chroma_inspect_venv/lib64/python3.12/site-packages/sympy/parsing/mathematica.py:1076:                return self._atom_conversions.get(expr, sympify(expr))
./chroma_inspect_venv/lib64/python3.12/site-packages/sympy/parsing/latex/_antlr/latexparser.py:3614:        pred = self._predicates.get(ruleIndex, None)
./chroma_inspect_venv/lib64/python3.12/site-packages/sympy/parsing/autolev/_antlr/autolevparser.py:3034:        pred = self._predicates.get(ruleIndex, None)
./chroma_inspect_venv/lib64/python3.12/site-packages/sympy/ntheory/factor_.py:719:        self._cache[n] = max(self._cache.get(n, 0), factor)
./chroma_inspect_venv/lib64/python3.12/site-packages/sympy/ntheory/factor_.py:1538:                    factors[k] = factors.get(k, 0) + v
./chroma_inspect_venv/lib64/python3.12/site-packages/sympy/unify/rewrite.py:47:                not condition(*[match.get(var, var) for var in variables])):
./chroma_inspect_venv/lib64/python3.12/site-packages/sympy/core/assumptions.py:624:        v = cls.__dict__.get(attrname, '')
./chroma_inspect_venv/lib64/python3.12/site-packages/sympy/core/power.py:1575:                    res[ex] = res.get(ex, S.Zero) + d1[e1]*d2[e2]
./chroma_inspect_venv/lib64/python3.12/site-packages/sympy/core/power.py:1609:            gterms[e1] = gterms.get(e1, S.Zero) + co1
./chroma_inspect_venv/lib64/python3.12/site-packages/sympy/core/power.py:1620:                terms[ex] = terms.get(ex, S.Zero) + coeff*tk[ex]
./chroma_inspect_venv/lib64/python3.12/site-packages/sympy/core/evalf.py:1385:        cached, cached_prec = cache.get(x, (None, MINUS_INF))
./chroma_inspect_venv/lib64/python3.12/site-packages/sympy/core/basic.py:142:        f = mapping.get(clsname, None)
./chroma_inspect_venv/lib64/python3.12/site-packages/sympy/core/basic.py:2255:        return rule.get(self, self)
./chroma_inspect_venv/lib64/python3.12/site-packages/sympy/core/relational.py:166:        cls = cls.ValidRelationOperator.get(rop, None)
./chroma_inspect_venv/lib64/python3.12/site-packages/sympy/core/exprtools.py:366:                factors[I] = factors.get(I, S.Zero) + i
./chroma_inspect_venv/lib64/python3.12/site-packages/sympy/core/function.py:224:        return lambda rule, **_: rule.get(self, self)
./chroma_inspect_venv/lib64/python3.12/site-packages/sympy/core/function.py:543:                fname = MPMATH_TRANSLATIONS.get(fname, None)
./chroma_inspect_venv/lib64/python3.12/site-packages/sympy/core/function.py:1759:            wrt = {syms.get(vi, vi) for vi in self._wrt_variables}
./chroma_inspect_venv/lib64/python3.12/site-packages/sympy/core/containers.py:312:        return self._dict.get(key, default)
./chroma_inspect_venv/lib64/python3.12/site-packages/sympy/vector/basisdependent.py:207:                components[x] = components.get(x, 0) + arg.components[x]
./chroma_inspect_venv/lib64/python3.12/site-packages/sympy/polys/domains/algebraicfield.py:626:    matrix = [[todom(t.get(a, S.Zero)) for t in terms] for a in algebraics]
./chroma_inspect_venv/lib64/python3.12/site-packages/sympy/polys/galoistools.py:301:            h.append(f.get(k, K.zero) % p)
./chroma_inspect_venv/lib64/python3.12/site-packages/sympy/polys/matrices/sdm.py:112:            rowi = self.get(i, None)
./chroma_inspect_venv/lib64/python3.12/site-packages/sympy/polys/matrices/sdm.py:969:        Emap = {v: list(A.get(v, [])) for v in V}
./chroma_inspect_venv/lib64/python3.12/site-packages/sympy/polys/matrices/sdm.py:1273:                Ai = Anew.get(i, None)
./chroma_inspect_venv/lib64/python3.12/site-packages/sympy/polys/matrices/sdm.py:1385:        return [row.get(i, zero) for i, row in self.items() if i < n]
./chroma_inspect_venv/lib64/python3.12/site-packages/sympy/polys/matrices/sdm.py:1512:                Cij = Ci.get(j, None)
./chroma_inspect_venv/lib64/python3.12/site-packages/sympy/polys/matrices/sdm.py:1551:                    Ci_list[j].append(Aik * B[k].get(j, zero))
./chroma_inspect_venv/lib64/python3.12/site-packages/sympy/polys/matrices/sdm.py:1574:                    Aik = A.get(i, {}).get(k, zero)
./chroma_inspect_venv/lib64/python3.12/site-packages/sympy/polys/matrices/sdm.py:1577:                        Ci = C.get(i, {})
./chroma_inspect_venv/lib64/python3.12/site-packages/sympy/polys/matrices/sdm.py:1578:                        Cij = Ci.get(j, zero) + Aik * Bkj
./chroma_inspect_venv/lib64/python3.12/site-packages/sympy/polys/matrices/sdm.py:2066:        for i in nonzero_cols.get(j, ()):
./chroma_inspect_venv/lib64/python3.12/site-packages/sympy/polys/densebasic.py:943:            h.append(f.get(k, K.zero))
./chroma_inspect_venv/lib64/python3.12/site-packages/sympy/polys/densebasic.py:973:        h.append(f.get(k, K.zero))
./chroma_inspect_venv/lib64/python3.12/site-packages/sympy/polys/numberfields/galoisgroups.py:100:        gen = coeff_generators.get(degree, coeff_search(degree, 1))
./chroma_inspect_venv/lib64/python3.12/site-packages/sympy/polys/rings.py:1292:            coeff = poly.get(monom, zero) + coeff
./chroma_inspect_venv/lib64/python3.12/site-packages/sympy/polys/rings.py:1785:        return self.get(expv, self.ring.domain.zero)
./chroma_inspect_venv/lib64/python3.12/site-packages/sympy/codegen/ast.py:206:            return cls.defaults.get(attr, none)
./chroma_inspect_venv/lib64/python3.12/site-packages/sympy/solvers/ode/single.py:306:        return [match.get(w, S.Zero) for w in self.wilds()]
./chroma_inspect_venv/lib64/python3.12/site-packages/sympy/solvers/ode/single.py:427:        diffcls = NthAlgebraic._diffx_stored.get(var, None)
./chroma_inspect_venv/lib64/python3.12/site-packages/sympy/solvers/ode/ode.py:629:                if retdict['best'] == retdict.get(i, None):
./chroma_inspect_venv/lib64/python3.12/site-packages/sympy/solvers/ode/ode.py:1244:        if not order.get(func, False):
./chroma_inspect_venv/lib64/python3.12/site-packages/sympy/solvers/solvers.py:91:    >>> assert [d.get(i, i) for i in s] == syms
./chroma_inspect_venv/lib64/python3.12/site-packages/sympy/solvers/solvers.py:112:    return new_f, [swap_sym.get(i, i) for i in orig], restore
./chroma_inspect_venv/lib64/python3.12/site-packages/sympy/solvers/solvers.py:836:        default = flags.setdefault(k, bool(flags.get(k, default)))
./chroma_inspect_venv/lib64/python3.12/site-packages/sympy/solvers/solvers.py:1180:    tuple_format = lambda s: [tuple([i.get(x, x) for x in symbols]) for i in s]
./chroma_inspect_venv/lib64/python3.12/site-packages/sympy/solvers/solvers.py:1221:        symbols = [swap_sym.get(k, k) for k in symbols]
./chroma_inspect_venv/lib64/python3.12/site-packages/sympy/solvers/solvers.py:1223:            solution[i] = {swap_sym.get(k, k): v.subs(swap_sym)
./chroma_inspect_venv/lib64/python3.12/site-packages/sympy/solvers/solvers.py:1290:    return k, {tuple([s.get(ki, ki) for ki in k]) for s in solution}
./chroma_inspect_venv/lib64/python3.12/site-packages/sympy/solvers/solveset.py:1150:    f_p, f_q, f_r = [pattern_match.get(i, S.Zero) for i in (p, q, r)]
./chroma_inspect_venv/lib64/python3.12/site-packages/sympy/solvers/solveset.py:3116:            sol = FiniteSet(Tuple(*(sol.get(sym, sym) for sym in symbols)))
./chroma_inspect_venv/lib64/python3.12/site-packages/sympy/solvers/solveset.py:3161:    sol = FiniteSet(Tuple(*(sol.get(sym, sym) for sym in symbols)))
./chroma_inspect_venv/lib64/python3.12/site-packages/sympy/solvers/simplex.py:664:        i = univariate.get(x, True)
./chroma_inspect_venv/lib64/python3.12/site-packages/sympy/solvers/tests/test_solvers.py:1521:        tuple([a.get(i, i) for i in v]) for a in ans]
./chroma_inspect_venv/lib64/python3.12/site-packages/kubernetes/config/kube_config.py:746:            self._merge(item, config.get(item, []) or [], path)
./chroma_inspect_venv/lib64/python3.12/site-packages/kubernetes/dynamic/discovery.py:127:                    resource_group = self._cache.get('resources', {}).get(DISCOVERY_PREFIX, {}).get(group['name'], {}).get(version)
./chroma_inspect_venv/lib64/python3.12/site-packages/kubernetes/dynamic/resource.py:383:        return self.__dict__.get(name, getattr(self.__dict__, name, None))
./chroma_inspect_venv/lib64/python3.12/site-packages/kubernetes/client/api_client.py:373:            return self.rest_client.GET(url,
./chroma_inspect_venv/lib64/python3.12/site-packages/kubernetes/stream/ws_client_test.py:58:    return dict_obj.get(key, default)
./msjarvis_semaphore.py:62:                    resp = await client.get(url, params=body)
./webhook_notifications.py:23:        webhooks = self.webhooks.get(event_type, [])
./main_brain_legacy_backup.py:79:    return endpoints.get(service_name, "/process")
./ms_jarvis_facebook_rag.py:318:        response = requests.get(url, params=params)
./woah_policy_update.py:13:        b = best.get(k, 0.0)
./woah_policy_update.py:23:        b = best.get(k, 0.0)
./consciousness_coordinator.py:183:            resp = await client.get(url, params=params)
./dgm_worker.py:43:KEYWORDS = SPECIALTY_KEYWORDS.get(SPECIALTY, ["community","purpose","serve","mount hope","west virginia","values"])
./ms_jarvis_main_gateway_8000.py:23:            r = await client.get(url, timeout=5.0)
./implement_safe_optimizations.py:114:                response = requests.get(url, timeout=5)
./implement_safe_optimizations.py:211:        return self.session.get(url, **kwargs)
./implement_safe_optimizations.py:223:        return optimized_session.get(url, **kwargs)
./quick_optimizations.py:35:            response = requests.get(service_url, timeout=3)
./facebook_poster.py:74:            resp = await client.get(CONSCIOUS_TICK_URL, timeout=360.0)
./dgm_supervisor_woah.psychology_patched.py:211:                    "woah_weight": WOAH_WEIGHTS.get(service_name, 1.0),
./process_gis_shapefiles.py:158:        categories[cat] = categories.get(cat, 0) + 1
./ms_jarvis_alerting_manager.py:176:                    "color": colors.get(severity, "#ffc107"),
./substack_rss_reader.py:22:            response = await client.get(url, timeout=10)
(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:/mnt/nvme1/msjarvis-rebuild/services$ 

