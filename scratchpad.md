===== CONTAINER RUNTIME =====
image=msjarvis-rebuild-jarvis-20llm-production
command=["python3","ai_server_20llm_PRODUCTION.py"]
entrypoint=null
working_dir=/app/services
mounts=/mnt/spiritual_drive/msjarvis-rebuild/services -> /app/services ro=true


===== CONTRACT-PROBE LOGS =====
2026-08-10T13:45:37.559449688Z INFO:__main__:20llm inbound userid/role debug userid=None role=None context_keys=['system_overrides']
2026-08-10T13:45:37.559449689Z INFO:     172.18.0.17:44150 - "POST /chat_with_context HTTP/1.1" 200 OK
2026-08-10T13:46:37.710914446Z INFO:__main__:20llm inbound userid/role debug userid=None role=None context_keys=['system_overrides']
2026-08-10T13:46:37.710952115Z INFO:     172.18.0.17:41000 - "POST /chat_with_context HTTP/1.1" 200 OK
2026-08-10T13:48:37.386590250Z INFO:__main__:20llm inbound userid/role debug userid=None role=None context_keys=['system_overrides']
2026-08-10T13:48:37.386792668Z INFO:     172.18.0.17:37354 - "POST /chat_with_context HTTP/1.1" 200 OK
2026-08-10T13:51:36.910118514Z INFO:__main__:20llm inbound userid/role debug userid=None role=None context_keys=['system_overrides']
2026-08-10T13:51:36.910153538Z INFO:     172.18.0.17:57758 - "POST /chat_with_context HTTP/1.1" 200 OK
2026-08-10T13:56:38.595294015Z INFO:__main__:20llm inbound userid/role debug userid=None role=None context_keys=['system_overrides']
2026-08-10T13:56:38.595631528Z INFO:     172.18.0.17:39864 - "POST /chat_with_context HTTP/1.1" 200 OK
2026-08-10T13:56:56.461891452Z INFO:__main__:20llm inbound userid/role debug userid=None role=None context_keys=['contains_experimental_record', 'protocol_contract_probe', 'purpose', 'record_count']
2026-08-10T13:56:56.461956500Z INFO:__main__:20llm-context-debug keys=['contains_experimental_record', 'protocol_contract_probe', 'purpose', 'record_count'] has_judge_context_packet=False
2026-08-10T13:56:56.461974390Z INFO:__main__:20llm-context-debug
2026-08-10T13:56:56.462267654Z INFO:__main__:💬 Contextual query: Return exactly the text PROTOCOL_CONTRACT_OK and n...
2026-08-10T13:58:22.738482467Z INFO:__main__:   [20/21] dispatching DeepSeek Coder...
2026-08-10T13:58:31.290509029Z INFO:__main__:   [21/21] dispatching LLaMA 2...
2026-08-10T14:00:03.945201129Z INFO:httpx:HTTP Request: POST http://llm22-proxy:8222/generate "HTTP/1.1 504 Gateway Timeout"
2026-08-10T14:00:03.960390542Z WARNING:__main__:⚠️  LLaMA 3.1: HTTP 504 from proxy=http://llm22-proxy:8222/generate; body='{"detail":"LLaMA3 proxy timeout/error: "}'
2026-08-10T14:00:24.473804731Z INFO:__main__:✅ Complete: 20/21 responded (elapsed=208.0s, parallel max=8)
2026-08-10T14:01:38.838745240Z INFO:__main__:20llm inbound userid/role debug userid=None role=None context_keys=['system_overrides']
2026-08-10T14:01:38.839181227Z INFO:     172.18.0.17:39242 - "POST /chat_with_context HTTP/1.1" 200 OK

===== ANSWER-ROUTE SOURCE INDEX =====
/app/services/ms_jarvis_email_service.py:51:        return {"status": "error", "message": "Auth failed"}
/app/services/ms_jarvis_email_service.py:69:        return {"status": "error", "message": r.text}
/app/services/ms_jarvis_email_service.py:97:        return {"status": "error", "message": r.text}
/app/services/msjarvis-rebuild-nbb_spiritual_root-1_main.py:13:    return {"message": message}
/app/services/ms_jarvis_web_research_v2.py:53:        return {"status": "error", "message": str(e), "results": []}
/app/services/working_full_pipeline.py:101:    return {"response": final, "model": "egeria-warm", "filtered": True}
/app/services/jarvis-consciousness-bridge_ms_jarvis_consciousness_unified_bridge.py:155:            return unified_response
/app/services/jarvis-consciousness-bridge_ms_jarvis_consciousness_unified_bridge.py:174:        return fallback_response
/app/services/service_discovery.py:161:                return response.status_code == 200
/app/services/implement_judge_pituitary_fixed.py:35:                    return resp.json().get("response", response)
/app/services/implement_judge_pituitary_fixed.py:39:        return response'''
/app/services/implement_judge_pituitary_fixed.py:54:            return response_list[0]
/app/services/implement_judge_pituitary_fixed.py:86:            return response
/app/services/ms_jarvis_microsoft_integration_FIXED.py:127:            return response.json() if response.content else {}
/app/services/main_with_rag.py:48:    return response
/app/services/msjarvis_gateway_v2_final.py:30:            return response.json()
/app/services/msjarvis_gateway_v2_final.py:64:    Then return a combined response.
/app/services/msjarvis_gateway_v2_final.py:110:    return {"status": "error", "message": "Service unavailable", "sessionid": sessionid}
/app/services/ms_jarvis_auto_service.py:94:            return response.status_code == 200
/app/services/ms_jarvis_auto_service.py:188:        return response.status_code == 200
/app/services/port_9001_ui_DIRECT.py:116:        return {"response": "Please provide a message"}
/app/services/port_9001_ui_DIRECT.py:124:            return response.json()
/app/services/port_9001_ui_DIRECT.py:126:        return {"response": f"Ms. Jarvis is thinking... (connection: {str(e)})"}
/app/services/ms_jarvis_substack_reader.py:37:        return {"error": f"Status {response.status_code}"}
/app/services/llm_consensus_22.py:100:    return weighted_responses
/app/services/msjarvis-rebuild-nbb_mother_carrie_protocols-1_main.py:13:    return {"message": message}
/app/services/ms_jarvis_neurobiological_master.py:276:        return response.json()
/app/services/ms_jarvis_neurobiological_master.py:284:        return response.json()
/app/services/ms_jarvis_link_reader_scheduled_FIXED.py:51:                return {"error": f"Failed: {response.status_code}"}
/app/services/msjarvis-rebuild-nbb_blood_brain_barrier-1_ms_jarvis_consciousness_bridge.py:11:    return {"response": f"NBB bridge processed: {data.get('message')}"}
/app/services/ms_jarvis_facebook_full.py:86:                    return result.get("response", fallback)
/app/services/fix_response_parsing.py:21:new_return = '''                response_text = result.get("response") or result.get("result") or result.get("output") or result.get("answer") or str(result)
/app/services/egeria_web_ui_working.py:96:        return jsonify({"error": "No message"}), 400
/app/services/egeria_web_ui_working.py:113:            return jsonify({"response": result.get('response', '').strip()})
/app/services/egeria_web_ui_working.py:117:    return jsonify({"error": "Failed to get response"}), 500
/app/services/fix_judge_authentic.py:18:old_judge = r'async def judge_responses\(self, query: str, responses\) -> str:.*?return list\(responses\.values\(\)\)\[0\] if responses else ""'
/app/services/fix_judge_authentic.py:35:                return response_list[0]
/app/services/fix_judge_authentic.py:67:            return response_list[0] if response_list else ""'''
/app/services/fix_judge_authentic.py:70:    r'async def judge_responses\(self, query: str, responses\) -> str:.*?return list\(responses\.values\(\)\)\[0\] if responses else ""',
/app/services/llm_consensus_20_FINAL.py:256:    return sorted(responses, key=lambda x: x.get("weight", 0.5), reverse=True)
/app/services/roche_llm.stub.py:20:    return ChatResponse(response=f"[Roche-LLM STUB] Echo: {req.message}")
/app/services/wire_layers_into_chat.py:22:new_return = '''        # Apply Judge layer - SELECT BEST response
/app/services/ms_jarvis_blockchain_deployment.py:192:        return {"status": "success", "message": f"Contract {contract_name} deployed successfully on {network}", "contract_address": contract_address}
/app/services/ms_jarvis_blockchain_deployment.py:195:        return {"status": "failure", "message": f"Failed to deploy contract {contract_name} on {network}: {e}"}
/app/services/ms_jarvis_unified_swagger_gateway_FIXED.py:139:        return response.json()
/app/services/ms_jarvis_unified_swagger_gateway_FIXED.py:148:        return response.json()
/app/services/ms_jarvis_unified_swagger_gateway_FIXED.py:478:        return {"status": "error", "message": str(e)}
/app/services/ms_jarvis_unified_swagger_gateway_FIXED.py:503:        return HTMLResponse(response.text)
/app/services/ms_jarvis_unified_swagger_gateway_FIXED.py:550:        return response.json()
/app/services/ms_jarvis_unified_swagger_gateway_FIXED.py:596:        return response
/app/services/ms_jarvis_unified_swagger_gateway_FIXED.py:618:        return response
/app/services/llm_consensus_22_SMALL_TO_LARGE.py:80:    return sorted(responses, key=lambda x: x.get('weight', 0.5), reverse=True)
/app/services/ms_jarvis_facebook_rag.py:121:                return response.json()
/app/services/domain_service_router.py:58:                return response
/app/services/domain_service_router.py:101:            return response.json()
/app/services/domain_service_router.py:103:            return response.text
/app/services/port_9001_ui_FIXED.py:127:        return {"response": "Please provide a message"}
/app/services/port_9001_ui_FIXED.py:147:        return {"response": f"Connection error: {str(e)}"}
/app/services/integrate_complete_architecture.py:53:                return response.json()
/app/services/integrate_complete_architecture.py:72:                return response.json()
/app/services/integrate_complete_architecture.py:91:                return response.json()
/app/services/jarvis-lm-synthesizer_lm_synthesizer.py:21:    return response_text
/app/services/ms_jarvis_facebook_poster_FIXED.py:32:                return data.get("response", "")
/app/services/msjarvisunifiedgateway.py:82:    return {"status": "ok", "message": "Ms. Jarvis running"}
/app/services/ms_jarvis_facebook_intelligent.py:42:            return {"status": "unauthorized", "message": f"Invalid page access token: {PAGE_TOKEN}"}
/app/services/ms_jarvis_facebook_intelligent.py:44:            return {"status": "not_found", "message": f"Page not found: {PAGE_ID}"}
/app/services/ms_jarvis_facebook_intelligent.py:82:                    return result.get("response", "AI response")
/app/services/enhance_pituitary_warmth.py:18:old_persona = r'async def apply_mamma_kidd_persona\(self, response: str\) -> str:.*?return response'
/app/services/enhance_pituitary_warmth.py:74:    r'async def apply_mamma_kidd_persona\(self, response: str\) -> str:.*?return response',
/app/services/ai_server_22llm_FIXED.py:30:        return valid_responses
/app/services/jarvis-wv-entangled-gateway_msjarvis_wv_entangled_gateway.py:6:- Builds WV entangled context and forwards to 20‑LLM /chat_with_context.
/app/services/jarvis-wv-entangled-gateway_msjarvis_wv_entangled_gateway.py:138:    WV‑focused chat: send message + WV entangled context to 20‑LLM /chat_with_context.
/app/services/jarvis-wv-entangled-gateway_msjarvis_wv_entangled_gateway.py:175:            f"{SERVICE_URLS['production_20llm']}/chat_with_context",
/app/services/gateway8050_simple.py:31:    return {"reply": data.get("reply") or data.get("answer") or data}
/app/services/egeria_web_ui_with_execution.py:62:    if not message: return jsonify({"error": "No message"}), 400
/app/services/egeria_web_ui_with_execution.py:76:            return jsonify({"response": response.json().get('response', '').strip()})
/app/services/patch_fractal.py:11:    return await analyze_fractal({"messages": msg_array})
/app/services/ai_server.py:173:        return valid_responses
/app/services/ai_server.py:208:                    return result.get("response", responses[0]["response"])
/app/services/ai_server.py:212:        # Fallback: return highest weighted response
/app/services/ai_server.py:213:        return max(weighted, key=lambda x: x["weight"])["response"]
/app/services/ai_server.py:228:                    return resp.json().get("response", response)
/app/services/ai_server.py:232:        return response
/app/services/ai_server.py:277:        return {"response": "I apologize, sugar. My collective consciousness is reorganizing. Try again in a moment.", 
/app/services/msjarvis-rebuild-nbb_heteroglobulin_transport-1_main.py:13:    return {"message": message}
/app/services/ms_jarvis_facebook_dgm_woah.psychology_patched.py:281:                return response.json()
/app/services/ms_jarvis_facebook_dgm_woah.psychology_patched.py:298:                return response.json()
/app/services/ms_jarvis_facebook_brain_integrated.py:225:                return response.json()
/app/services/ms_jarvis_facebook_brain_integrated.py:471:        return response.json()
/app/services/ms_jarvis_facebook_webhook.py:62:                return resp.json().get("response", "Processing...")
/app/services/add_to_main_consciousness.py:18:                return {"error": f"Link read failed: {link_response.status_code}"}
/app/services/ai_server_19llm_PRODUCTION.py:84:        return responses
/app/services/ai_server_19llm_PRODUCTION.py:122:        return {"response": "Error processing request", "error": str(e)}
/app/services/ms_jarvis_fractal_dgm_woah.py:61:        return {'error': 'Need 4+ messages', 'architecture': 'DGM-WOAH'}
/app/services/bridge_cross_dgm.py:55:        return response.json()
/app/services/jarvis-psychology-services_psychology_integration_adapter.py:61:        return self._fallback_analysis(message)
/app/services/jarvis-psychology-services_psychology_integration_adapter.py:140:            return enriched_response
/app/services/msjarvis-rebuild-nbb_qualia_engine-1_ms_jarvis_consciousness_bridge.py:11:    return {"response": f"NBB bridge processed: {data.get('message')}"}
/app/services/messenger_service_fixed.py:44:    return JSONResponse({"response": response, "session_id": session_id})
/app/services/messenger_service_fixed.py:51:    return JSONResponse({"session_id": session_id, "messages": sessions[session_id]["messages"]})
/app/services/neurobiologicalbrain/woah_algorithms/service/ms_jarvis_consciousness_bridge.py:100:                return response.json()
/app/services/neurobiologicalbrain/woah_algorithms/service/ms_jarvis_consciousness_bridge.py:120:                return response.json()
/app/services/neurobiologicalbrain/woah_algorithms/service/ms_jarvis_consciousness_bridge.py:142:                return response.json()
/app/services/neurobiologicalbrain/i_containers/service/service_discovery.py:156:                return response.status_code == 200
/app/services/neurobiologicalbrain/i_containers/service/ms_jarvis_consciousness_bridge.py:100:                return response.json()
/app/services/neurobiologicalbrain/i_containers/service/ms_jarvis_consciousness_bridge.py:120:                return response.json()
/app/services/neurobiologicalbrain/i_containers/service/ms_jarvis_consciousness_bridge.py:142:                return response.json()
/app/services/neurobiologicalbrain/spiritual_root/service/ms_jarvis_consciousness_bridge.py:100:                return response.json()
/app/services/neurobiologicalbrain/spiritual_root/service/ms_jarvis_consciousness_bridge.py:120:                return response.json()
/app/services/neurobiologicalbrain/spiritual_root/service/ms_jarvis_consciousness_bridge.py:142:                return response.json()
/app/services/neurobiologicalbrain/prefrontal_cortex/service/service_discovery.py:156:                return response.status_code == 200
/app/services/neurobiologicalbrain/prefrontal_cortex/service/ms_jarvis_consciousness_bridge.py:100:                return response.json()
/app/services/neurobiologicalbrain/prefrontal_cortex/service/ms_jarvis_consciousness_bridge.py:120:                return response.json()
/app/services/neurobiologicalbrain/prefrontal_cortex/service/ms_jarvis_consciousness_bridge.py:142:                return response.json()
/app/services/neurobiologicalbrain/pituitary_gland/service/ms_jarvis_consciousness_bridge.py:100:                return response.json()
/app/services/neurobiologicalbrain/pituitary_gland/service/ms_jarvis_consciousness_bridge.py:120:                return response.json()
/app/services/neurobiologicalbrain/pituitary_gland/service/ms_jarvis_consciousness_bridge.py:142:                return response.json()
/app/services/neurobiologicalbrain/subconscious/service/ms_jarvis_consciousness_bridge.py:100:                return response.json()
/app/services/neurobiologicalbrain/subconscious/service/ms_jarvis_consciousness_bridge.py:120:                return response.json()
/app/services/neurobiologicalbrain/subconscious/service/ms_jarvis_consciousness_bridge.py:142:                return response.json()
/app/services/neurobiologicalbrain/mother_carrie_protocols/service/ms_jarvis_consciousness_bridge.py:100:                return response.json()
/app/services/neurobiologicalbrain/mother_carrie_protocols/service/ms_jarvis_consciousness_bridge.py:120:                return response.json()
/app/services/neurobiologicalbrain/mother_carrie_protocols/service/ms_jarvis_consciousness_bridge.py:142:                return response.json()
/app/services/neurobiologicalbrain/spiritual_maternal_integration/service/ms_jarvis_consciousness_bridge.py:100:                return response.json()
/app/services/neurobiologicalbrain/spiritual_maternal_integration/service/ms_jarvis_consciousness_bridge.py:120:                return response.json()
/app/services/neurobiologicalbrain/spiritual_maternal_integration/service/ms_jarvis_consciousness_bridge.py:142:                return response.json()
/app/services/neurobiologicalbrain/heteroglobulin_transport/service/ms_jarvis_consciousness_bridge.py:100:                return response.json()
/app/services/neurobiologicalbrain/heteroglobulin_transport/service/ms_jarvis_consciousness_bridge.py:120:                return response.json()
/app/services/neurobiologicalbrain/heteroglobulin_transport/service/ms_jarvis_consciousness_bridge.py:142:                return response.json()
/app/services/neurobiologicalbrain/consciousness_containers/service/ms_jarvis_consciousness_bridge.py:100:                return response.json()
/app/services/neurobiologicalbrain/consciousness_containers/service/ms_jarvis_consciousness_bridge.py:120:                return response.json()
/app/services/neurobiologicalbrain/consciousness_containers/service/ms_jarvis_consciousness_bridge.py:142:                return response.json()
/app/services/ms_jarvis_contract_builder_v2.py:55:        return {"status": "failed", "message": f"{e}"}
/app/services/ms_jarvis_unified_swagger_gateway_COMPLETE.py:53:            return response.json()
/app/services/ms_jarvis_unified_swagger_gateway_COMPLETE.py:63:            return response.json()
/app/services/ms_jarvis_unified_swagger_gateway_COMPLETE.py:73:            return response.json()
/app/services/ms_jarvis_unified_swagger_gateway_COMPLETE.py:204:            return response.json()
/app/services/jarvis-assertion-gateway/app/main.py:118:    return scrub_response({
/app/services/metrics_service.py:22:    return {"message": "Ms. Jarvis Metrics Service", "version": "1.0"}
/app/services/ms_jarvis_geo_ueid_integration.py:52:        return {"status": "exists", "message": "Entity already in geodatabase"}
/app/services/msjarvis-rebuild-nbb_woah_algorithms-1_service_discovery.py:156:                return response.status_code == 200
/app/services/ms_jarvis_llm_bridge_simple.py:49:        return response.json()
/app/services/ms_jarvis_expiration_monitor.py:132:    return response.status_code == 202
/app/services/jarvis-judge-alignment_lm_synthesizer.py:27:    return response
/app/services/jarvis-judge-alignment_lm_synthesizer.py:38:    return response_text
/app/services/msjarvis-rebuild-nbb_prefrontal_cortex-1_main.py:13:    return {"message": message}
/app/services/jarvis_synth_llm.py:50:            return "Ollama /api/chat returned no content in 'message'."
/app/services/jarvis_synth_llm.py:53:        return "Ollama call failed: ReadTimeout while waiting for /api/chat response."
/app/services/jarvis_synth_llm.py:67:    return {"answer": answer, "prompt": prompt, "model": OLLAMA_MODEL}
/app/services/ms_jarvis_command_orchestrator.py:45:            return JSONResponse({"status": "crisis_detected", "response": crisis["clarity_statement"], "resources": crisis["resources"]})
/app/services/ms_jarvis_command_orchestrator.py:115:            return response.json().get("response", "")[:1500]
/app/services/port_9001_ui_MYSQL_PROD.py:115:            if (d.response) return String(d.response);
/app/services/port_9001_ui_MYSQL_PROD.py:176:        return {"response": "Connecting..."}
/app/services/port_9001_ui_MYSQL_PROD.py:200:        return {"conversations": [{"message": r[0], "response": r[1]} for r in rows]}
/app/services/port_9001_ui_MYSQL_PROD.py:213:        return {"exported": datetime.now().isoformat(), "total": len(rows), "data": [{"user": r[0], "message": r[1], "response": r[2], "timestamp": str(r[3])} for r in rows]}
/app/services/ms_jarvis_fully_autonomous_coordinator.py:77:                return response.json()
/app/services/ms_jarvis_fully_autonomous_coordinator.py:210:                        return post_response.json()
/app/services/ms_jarvis_fully_autonomous_coordinator.py:425:            return response.json()
/app/services/ms_jarvis_email_identity_verifier.py:125:        return VerificationResponse(status="error", message="Failed to create account")
/app/services/ms_jarvis_web_research_aggregate.safe.20260119-094221.py:32:        return response
/app/services/apply_ollama_fix.py:79:                return result.get("response", "I've analyzed your request and I'm ready to help.")
/app/services/apply_ollama_fix.py:108:                    return result.get("response", judge_response)
/app/services/apply_ollama_fix.py:111:                return judge_response
/app/services/apply_ollama_fix.py:114:            return judge_response
/app/services/jarvis-rag-server_ms_jarvis_consciousness_unified_bridge.py:155:            return unified_response
/app/services/jarvis-rag-server_ms_jarvis_consciousness_unified_bridge.py:174:        return fallback_response
/app/services/fix_persona_hang.py:11:# Comment it out and return judge response directly
/app/services/msjarvis-rebuild-nbb_i_containers-1_ms_jarvis_consciousness_unified_bridge.py:155:            return unified_response
/app/services/msjarvis-rebuild-nbb_i_containers-1_ms_jarvis_consciousness_unified_bridge.py:174:        return fallback_response
/app/services/jarvis-judge-consistency_lm_synthesizer.py:21:    return response_text
/app/services/gateway_messenger_integration.py:35:        return response.json()
/app/services/gateway_messenger_integration.py:55:        return response.json()
/app/services/gateway_messenger_integration.py:70:        return response.json()
/app/services/msjarvisconsciousnessbridge_mountainshares_private.py:154:    return await bridge.process(payload.message, user_id)
/app/services/fifth_dgm_integration.py:106:                    return response.json()
/app/services/ms_jarvis_main_gateway.py:192:        return {"response": f"AI: {message}"}
/app/services/ms_jarvis_main_gateway.py:213:    return {"level": level, "response": f"Fractal: {query}"}
/app/services/egeria_api_proxy.py:46:            return response.json()
/app/services/egeria_api_proxy.py:49:        return {"response": "I apologize, but I'm having trouble processing that right now."}
/app/services/psychology_integration_adapter.py:61:        return self._fallback_analysis(message)
/app/services/psychology_integration_adapter.py:140:            return enriched_response
/app/services/msjarvis-rebuild-nbb_spiritual_maternal_integration-1_main.py:13:    return {"message": message}
/app/services/jarvis-judge-ethics_lm_synthesizer.py:21:    return response_text
/app/services/manual_storage_patch.py:16:    if 'return {' in line and '"response":' in line and '"services_used":' in line and '"consciousness_level":' in line:
/app/services/ms_jarvis_command_orchestrator_v5_backup.py:233:            return response.json().get("response", "")[:1500]
/app/services/rag_simple.py:35:            return {"status": "success", "consensus": response, "context_docs": len(context.split("\n")), "models_used": min_models}
/app/services/rag_simple.py:37:            return {"status": "error", "message": f"LLM error: {lr.status_code}"}
/app/services/rag_simple.py:39:        return {"status": "error", "message": str(e)}
/app/services/rag_server_main.py:277:    return response_payload
/app/services/facebook_messenger_integration.py:64:                return data.get("response", "Hello from Ms. Egeria Jarvis!")
/app/services/facebook_messenger_integration.py:88:            return response.ok
/app/services/verify_and_document_system.py:83:            return response.json()
/app/services/integrate_full_brain.py:33:                    return response.json()
/app/services/integrate_full_brain.py:47:                    return response.json()
/app/services/phase4_5_integration.py:31:                return response.json()
/app/services/phase4_5_integration.py:54:                return response.json()
/app/services/phase4_5_integration.py:56:            return {"response": None, "bridged": False}
/app/services/phase4_5_integration.py:62:    return await layer.route_through_gateway(data["message"], data.get("metadata", {}))
/app/services/llm_ensemble_router.py:33:                return {"model": model, "response": data.get("response", ""), "status": "success"}
/app/services/llm_ensemble_router.py:36:            return {"model": model, "response": "", "status": "error"}
/app/services/llm_ensemble_router.py:64:        return min(1.0, unique_starts / len(responses))
/app/services/chat_worker.py:66:            url = f"{SERVICE_URLS['production_20llm']}/chat_with_context"
/app/services/fifth_dgm.py:19:    return AnalyzeResponse(response=f"[fifth_dgm stub] {req.input}")
/app/services/advanced_service_dashboard.py:51:                return "🟢 HEALTHY" if response.status_code == 200 else "🔴 UNHEALTHY"
/app/services/ai_server_19llm_CONSCIOUS.py:166:            return personalized if len(personalized) > 50 else response
/app/services/ai_server_19llm_CONSCIOUS.py:170:            return response  # Fallback to original
/app/services/ms_jarvis_web_research_aggregate.py:32:        return response
/app/services/web_chat_server.py:187:        return response.json()
/app/services/jarvis-agents-service_ms_jarvis_consciousness_unified_bridge.py:155:            return unified_response
/app/services/jarvis-agents-service_ms_jarvis_consciousness_unified_bridge.py:174:        return fallback_response
/app/services/ms_jarvis_facebook_async.py:75:    return response
/app/services/add_background_call.py:20:    # If we're in ultimate_chat and we find a return with the final response
/app/services/add_background_call.py:21:    if in_ultimate_chat and 'return {' in line and '"response":' in line and not modified:
/app/services/llm_consensus_19_PRODUCTION.py:71:    return sorted(responses, key=lambda x: x.get('weight', 0.5), reverse=True)
/app/services/port_9001_ui_WITH_CONVERSATIONS.py:217:        return {"response": "Please provide a message"}
/app/services/port_9001_ui_WITH_CONVERSATIONS.py:225:            return response.json()
/app/services/port_9001_ui_WITH_CONVERSATIONS.py:227:        return {"response": f"Connection in progress..."}
/app/services/comprehensive_storage_fix.py:54:# Look for return with "response", "services_used", "consciousness_level", "processing_time"
/app/services/swagger_chat_integration.py:75:        return response.json()
/app/services/gateway_verify_fixed.py:15:        return HTMLResponse(response.text)
/app/services/fractal_adapter.py:19:        return response.json()
/app/services/ms_jarvis_production_chat_BEFORE_GIS.py:219:                return response.json()["ueid"]
/app/services/ms_jarvis_i_containers_service.py:341:        return response
/app/services/ms_jarvis_i_containers_service.py:348:                return response
/app/services/egeria_web_ui_fixed_simple.py:35:        return jsonify({"error": "No message"}), 400
/app/services/egeria_web_ui_fixed_simple.py:60:    return jsonify({"error": "Failed to get response"}), 500
/app/services/msjarvis_wv_entangled_gateway.py:5:- Builds WV entangled context and forwards to 20‑LLM /chat_with_context.
/app/services/msjarvis_wv_entangled_gateway.py:112:                f"{SERVICE_URLS['production_20llm']}/chat_with_context",
/app/services/msjarvis_wv_entangled_gateway.py:216:    WV‑focused chat: send message + WV entangled context to 20‑LLM /chat_with_context.
/app/services/msjarvis_wv_entangled_gateway.py:234:            f"{SERVICE_URLS['production_20llm']}/chat_with_context",
/app/services/ai_server_20llm_FINAL.py:54:class ChatRequestWithContext(BaseModel):
/app/services/ai_server_20llm_FINAL.py:110:        return responses
/app/services/ai_server_20llm_FINAL.py:125:        return final_response
/app/services/ai_server_20llm_FINAL.py:133:@app.post("/chat_with_context")
/app/services/ai_server_20llm_FINAL.py:135:async def chat_with_context(request: ChatRequestWithContext):
/app/services/ai_server_20llm_FINAL.py:165:        logger.error("Error in /chat_with_context: %s", e)
/app/services/ai_server_20llm_FINAL.py:183:        return {"response": "Error processing request", "error": str(e)}
/app/services/add_messenger_to_gateway.py:20:    return response.json()
/app/services/add_messenger_to_gateway.py:30:    return response.json()
/app/services/add_messenger_to_gateway.py:36:    return response.json()

===== ANSWER-ROUTE SOURCE CONTEXT =====
/app/services/jarvis-wv-entangled-gateway_msjarvis_wv_entangled_gateway.py-1-#!/usr/bin/env python3
/app/services/jarvis-wv-entangled-gateway_msjarvis_wv_entangled_gateway.py-2-"""
/app/services/jarvis-wv-entangled-gateway_msjarvis_wv_entangled_gateway.py-3-from hp_antisurveillance_guardian_client import require_guarded_join
/app/services/jarvis-wv-entangled-gateway_msjarvis_wv_entangled_gateway.py-4-Ms. Jarvis WV‑Entangled Gateway
/app/services/jarvis-wv-entangled-gateway_msjarvis_wv_entangled_gateway.py-5-- Exposes /chat_wv on its own port (8010).
/app/services/jarvis-wv-entangled-gateway_msjarvis_wv_entangled_gateway.py:6:- Builds WV entangled context and forwards to 20‑LLM /chat_with_context.
/app/services/jarvis-wv-entangled-gateway_msjarvis_wv_entangled_gateway.py-7-"""
/app/services/jarvis-wv-entangled-gateway_msjarvis_wv_entangled_gateway.py-8-
/app/services/jarvis-wv-entangled-gateway_msjarvis_wv_entangled_gateway.py-9-import logging
/app/services/jarvis-wv-entangled-gateway_msjarvis_wv_entangled_gateway.py-10-from datetime import datetime
/app/services/jarvis-wv-entangled-gateway_msjarvis_wv_entangled_gateway.py-11-from typing import Dict, Any
/app/services/jarvis-wv-entangled-gateway_msjarvis_wv_entangled_gateway.py-12-
/app/services/jarvis-wv-entangled-gateway_msjarvis_wv_entangled_gateway.py-13-import httpx
/app/services/jarvis-wv-entangled-gateway_msjarvis_wv_entangled_gateway.py-14-from fastapi import FastAPI
/app/services/jarvis-wv-entangled-gateway_msjarvis_wv_entangled_gateway.py-15-from request_context_builder import build_request_context_packet
/app/services/jarvis-wv-entangled-gateway_msjarvis_wv_entangled_gateway.py-16-from fastapi.middleware.cors import CORSMiddleware
/app/services/jarvis-wv-entangled-gateway_msjarvis_wv_entangled_gateway.py-17-from pydantic import BaseModel
/app/services/jarvis-wv-entangled-gateway_msjarvis_wv_entangled_gateway.py-18-import uvicorn
/app/services/jarvis-wv-entangled-gateway_msjarvis_wv_entangled_gateway.py-19-
/app/services/jarvis-wv-entangled-gateway_msjarvis_wv_entangled_gateway.py-20-logging.basicConfig(level=logging.INFO)
/app/services/jarvis-wv-entangled-gateway_msjarvis_wv_entangled_gateway.py-21-logger = logging.getLogger(__name__)
/app/services/jarvis-wv-entangled-gateway_msjarvis_wv_entangled_gateway.py-22-
/app/services/jarvis-wv-entangled-gateway_msjarvis_wv_entangled_gateway.py-23-
/app/services/jarvis-wv-entangled-gateway_msjarvis_wv_entangled_gateway.py-24-def _log_forward_context(ctx: dict | None) -> None:
/app/services/jarvis-wv-entangled-gateway_msjarvis_wv_entangled_gateway.py-25-    c = ctx if isinstance(ctx, dict) else {}
/app/services/jarvis-wv-entangled-gateway_msjarvis_wv_entangled_gateway.py-26-    logger.info(
--
/app/services/jarvis-wv-entangled-gateway_msjarvis_wv_entangled_gateway.py-118-    async with httpx.AsyncClient(timeout=5.0) as client:
/app/services/jarvis-wv-entangled-gateway_msjarvis_wv_entangled_gateway.py-119-        try:
/app/services/jarvis-wv-entangled-gateway_msjarvis_wv_entangled_gateway.py-120-            r = await client.get(f"{SERVICE_URLS['production_20llm']}/health")
/app/services/jarvis-wv-entangled-gateway_msjarvis_wv_entangled_gateway.py-121-            ok = r.status_code == 200
/app/services/jarvis-wv-entangled-gateway_msjarvis_wv_entangled_gateway.py-122-        except Exception as e:
/app/services/jarvis-wv-entangled-gateway_msjarvis_wv_entangled_gateway.py-123-            logger.error(f"20‑LLM health check failed: {e}")
/app/services/jarvis-wv-entangled-gateway_msjarvis_wv_entangled_gateway.py-124-            ok = False
/app/services/jarvis-wv-entangled-gateway_msjarvis_wv_entangled_gateway.py-125-
/app/services/jarvis-wv-entangled-gateway_msjarvis_wv_entangled_gateway.py-126-    return {
/app/services/jarvis-wv-entangled-gateway_msjarvis_wv_entangled_gateway.py-127-        "status": "healthy" if ok else "degraded",
/app/services/jarvis-wv-entangled-gateway_msjarvis_wv_entangled_gateway.py-128-        "dependencies": {
/app/services/jarvis-wv-entangled-gateway_msjarvis_wv_entangled_gateway.py-129-            "production_20llm": "healthy" if ok else "unavailable",
/app/services/jarvis-wv-entangled-gateway_msjarvis_wv_entangled_gateway.py-130-        },
/app/services/jarvis-wv-entangled-gateway_msjarvis_wv_entangled_gateway.py-131-        "timestamp": datetime.utcnow().isoformat(),
/app/services/jarvis-wv-entangled-gateway_msjarvis_wv_entangled_gateway.py-132-    }
/app/services/jarvis-wv-entangled-gateway_msjarvis_wv_entangled_gateway.py-133-
/app/services/jarvis-wv-entangled-gateway_msjarvis_wv_entangled_gateway.py-134-
/app/services/jarvis-wv-entangled-gateway_msjarvis_wv_entangled_gateway.py-135-@app.post("/chat_wv")
/app/services/jarvis-wv-entangled-gateway_msjarvis_wv_entangled_gateway.py-136-async def chat_wv(payload: ChatPayload):
/app/services/jarvis-wv-entangled-gateway_msjarvis_wv_entangled_gateway.py-137-    """
/app/services/jarvis-wv-entangled-gateway_msjarvis_wv_entangled_gateway.py:138:    WV‑focused chat: send message + WV entangled context to 20‑LLM /chat_with_context.
/app/services/jarvis-wv-entangled-gateway_msjarvis_wv_entangled_gateway.py-139-    """
/app/services/jarvis-wv-entangled-gateway_msjarvis_wv_entangled_gateway.py-140-    logger.info("WV‑Entangled /chat_wv invoked")
/app/services/jarvis-wv-entangled-gateway_msjarvis_wv_entangled_gateway.py-141-    user_id = payload.user_id or "anonymous"
/app/services/jarvis-wv-entangled-gateway_msjarvis_wv_entangled_gateway.py-142-    wv_ctx = build_wv_entangled_context(payload.message)
/app/services/jarvis-wv-entangled-gateway_msjarvis_wv_entangled_gateway.py-143-
/app/services/jarvis-wv-entangled-gateway_msjarvis_wv_entangled_gateway.py-144-    incoming_context = payload.context if isinstance(getattr(payload, "context", None), dict) else {}
/app/services/jarvis-wv-entangled-gateway_msjarvis_wv_entangled_gateway.py-145-    incoming_role = incoming_context.get("role", "community")
/app/services/jarvis-wv-entangled-gateway_msjarvis_wv_entangled_gateway.py-146-    incoming_packet = incoming_context.get("judge_context_packet")
/app/services/jarvis-wv-entangled-gateway_msjarvis_wv_entangled_gateway.py-147-
/app/services/jarvis-wv-entangled-gateway_msjarvis_wv_entangled_gateway.py-148-    if not isinstance(incoming_packet, dict):
/app/services/jarvis-wv-entangled-gateway_msjarvis_wv_entangled_gateway.py-149-        incoming_packet = await build_request_context_packet(
/app/services/jarvis-wv-entangled-gateway_msjarvis_wv_entangled_gateway.py-150-            message=payload.message,
/app/services/jarvis-wv-entangled-gateway_msjarvis_wv_entangled_gateway.py-151-            userid=user_id,
/app/services/jarvis-wv-entangled-gateway_msjarvis_wv_entangled_gateway.py-152-            role=incoming_role,
/app/services/jarvis-wv-entangled-gateway_msjarvis_wv_entangled_gateway.py-153-            sessionid=None,
/app/services/jarvis-wv-entangled-gateway_msjarvis_wv_entangled_gateway.py-154-            prebuilt_context=None,
/app/services/jarvis-wv-entangled-gateway_msjarvis_wv_entangled_gateway.py-155-        )
/app/services/jarvis-wv-entangled-gateway_msjarvis_wv_entangled_gateway.py-156-
/app/services/jarvis-wv-entangled-gateway_msjarvis_wv_entangled_gateway.py-157-    forward_payload = {
/app/services/jarvis-wv-entangled-gateway_msjarvis_wv_entangled_gateway.py-158-        "message": payload.message,
/app/services/jarvis-wv-entangled-gateway_msjarvis_wv_entangled_gateway.py-159-        "user_id": user_id,
/app/services/jarvis-wv-entangled-gateway_msjarvis_wv_entangled_gateway.py-160-        "context": {
/app/services/jarvis-wv-entangled-gateway_msjarvis_wv_entangled_gateway.py-161-            "userid": incoming_context.get("userid", user_id),
/app/services/jarvis-wv-entangled-gateway_msjarvis_wv_entangled_gateway.py-162-            "role": incoming_role,
/app/services/jarvis-wv-entangled-gateway_msjarvis_wv_entangled_gateway.py-163-            "judge_context_packet": incoming_packet,
/app/services/jarvis-wv-entangled-gateway_msjarvis_wv_entangled_gateway.py-164-            "system_overrides": {
/app/services/jarvis-wv-entangled-gateway_msjarvis_wv_entangled_gateway.py-165-                **(incoming_context.get("system_overrides") or {}),
/app/services/jarvis-wv-entangled-gateway_msjarvis_wv_entangled_gateway.py-166-                "wv_entangled_context": wv_ctx
/app/services/jarvis-wv-entangled-gateway_msjarvis_wv_entangled_gateway.py-167-            }
/app/services/jarvis-wv-entangled-gateway_msjarvis_wv_entangled_gateway.py-168-        },
/app/services/jarvis-wv-entangled-gateway_msjarvis_wv_entangled_gateway.py-169-    }
/app/services/jarvis-wv-entangled-gateway_msjarvis_wv_entangled_gateway.py-170-
/app/services/jarvis-wv-entangled-gateway_msjarvis_wv_entangled_gateway.py-171-    _log_forward_context(forward_payload.get("context"))
/app/services/jarvis-wv-entangled-gateway_msjarvis_wv_entangled_gateway.py-172-
/app/services/jarvis-wv-entangled-gateway_msjarvis_wv_entangled_gateway.py-173-    async with httpx.AsyncClient(timeout=600.0) as client:
/app/services/jarvis-wv-entangled-gateway_msjarvis_wv_entangled_gateway.py-174-        resp = await client.post(
/app/services/jarvis-wv-entangled-gateway_msjarvis_wv_entangled_gateway.py:175:            f"{SERVICE_URLS['production_20llm']}/chat_with_context",
/app/services/jarvis-wv-entangled-gateway_msjarvis_wv_entangled_gateway.py-176-            json=forward_payload,
/app/services/jarvis-wv-entangled-gateway_msjarvis_wv_entangled_gateway.py-177-        )
/app/services/jarvis-wv-entangled-gateway_msjarvis_wv_entangled_gateway.py-178-        resp.raise_for_status()
/app/services/jarvis-wv-entangled-gateway_msjarvis_wv_entangled_gateway.py-179-        data = resp.json()
/app/services/jarvis-wv-entangled-gateway_msjarvis_wv_entangled_gateway.py-180-
/app/services/jarvis-wv-entangled-gateway_msjarvis_wv_entangled_gateway.py-181-    return data
/app/services/jarvis-wv-entangled-gateway_msjarvis_wv_entangled_gateway.py-182-
/app/services/jarvis-wv-entangled-gateway_msjarvis_wv_entangled_gateway.py-183-
/app/services/jarvis-wv-entangled-gateway_msjarvis_wv_entangled_gateway.py-184-if __name__ == "__main__":
/app/services/jarvis-wv-entangled-gateway_msjarvis_wv_entangled_gateway.py-185-    # Run as a long-lived FastAPI service on port 8010, listening on all interfaces
/app/services/jarvis-wv-entangled-gateway_msjarvis_wv_entangled_gateway.py-186-    uvicorn.run(
/app/services/jarvis-wv-entangled-gateway_msjarvis_wv_entangled_gateway.py-187-        "msjarvis_wv_entangled_gateway:app",
/app/services/jarvis-wv-entangled-gateway_msjarvis_wv_entangled_gateway.py-188-        host="0.0.0.0",
/app/services/jarvis-wv-entangled-gateway_msjarvis_wv_entangled_gateway.py-189-        port=8010,
/app/services/jarvis-wv-entangled-gateway_msjarvis_wv_entangled_gateway.py-190-        workers=1,
/app/services/jarvis-wv-entangled-gateway_msjarvis_wv_entangled_gateway.py-191-    )
--
/app/services/chat_worker.py-46-rdb = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, db=REDIS_DB, decode_responses=True)
/app/services/chat_worker.py-47-
/app/services/chat_worker.py-48-
/app/services/chat_worker.py-49-def run_job(job_id: str, message: str, user_id: str, ueid: str | None = None):
/app/services/chat_worker.py-50-    """Run the 21-model forward call and store the result."""
/app/services/chat_worker.py-51-    try:
/app/services/chat_worker.py-52-        wv_ctx = build_wv_entangled_context(message)
/app/services/chat_worker.py-53-        if FORWARD_MODE == "fullbrain":
/app/services/chat_worker.py-54-            url = MAIN_BRAIN_URL
/app/services/chat_worker.py-55-            forward_payload = {
/app/services/chat_worker.py-56-                "message": message,
/app/services/chat_worker.py-57-                "userid": user_id or "cakidd",
/app/services/chat_worker.py-58-                "ueid": ueid,
/app/services/chat_worker.py-59-                "memory_key": build_memory_key(user_id or "cakidd", ueid),
/app/services/chat_worker.py-60-                "useallservices": True,
/app/services/chat_worker.py-61-                "role": "community",
/app/services/chat_worker.py-62-                "context": {"wv_entangled_context": wv_ctx},
/app/services/chat_worker.py-63-            }
/app/services/chat_worker.py-64-            headers = {"X-API-Key": MAIN_BRAIN_KEY, "Content-Type": "application/json"}
/app/services/chat_worker.py-65-        else:
/app/services/chat_worker.py:66:            url = f"{SERVICE_URLS['production_20llm']}/chat_with_context"
/app/services/chat_worker.py-67-            forward_payload = {
/app/services/chat_worker.py-68-                "message": message,
/app/services/chat_worker.py-69-                "user_id": user_id or "anonymous",
/app/services/chat_worker.py-70-                "context": {"system_overrides": {"wv_entangled_context": wv_ctx}},
/app/services/chat_worker.py-71-            }
/app/services/chat_worker.py-72-            headers = {}
/app/services/chat_worker.py-73-        # Long timeout: full pipeline can take ~2.5-4 min.
/app/services/chat_worker.py-74-        with httpx.Client(timeout=3600.0) as client:
/app/services/chat_worker.py-75-            resp = client.post(url, json=forward_payload, headers=headers, timeout=None)
/app/services/chat_worker.py-76-            resp.raise_for_status()
/app/services/chat_worker.py-77-            raw = resp.json()
/app/services/chat_worker.py-78-        if FORWARD_MODE == "fullbrain":
/app/services/chat_worker.py-79-            data = {
/app/services/chat_worker.py-80-                "response": raw.get("response", ""),
/app/services/chat_worker.py-81-                "minds_participated": 21,
/app/services/chat_worker.py-82-                "total_minds": 21,
/app/services/chat_worker.py-83-                "used_wv_entangled_context": True,
/app/services/chat_worker.py-84-                "services_used": raw.get("servicesused", []),
/app/services/chat_worker.py-85-                "consciousness_level": raw.get("consciousnesslevel", ""),
/app/services/chat_worker.py-86-                "processing_time": raw.get("processingtime", 0),
--
/app/services/msjarvis_wv_entangled_gateway.py-1-#!/usr/bin/env python3
/app/services/msjarvis_wv_entangled_gateway.py-2-"""
/app/services/msjarvis_wv_entangled_gateway.py-3-Ms. Jarvis WV‑Entangled Gateway
/app/services/msjarvis_wv_entangled_gateway.py-4-- Exposes /chat_wv on its own port (8010).
/app/services/msjarvis_wv_entangled_gateway.py:5:- Builds WV entangled context and forwards to 20‑LLM /chat_with_context.
/app/services/msjarvis_wv_entangled_gateway.py-6-"""
/app/services/msjarvis_wv_entangled_gateway.py-7-
/app/services/msjarvis_wv_entangled_gateway.py-8-import logging
/app/services/msjarvis_wv_entangled_gateway.py-9-from datetime import datetime
/app/services/msjarvis_wv_entangled_gateway.py-10-from typing import Dict, Any
/app/services/msjarvis_wv_entangled_gateway.py-11-
/app/services/msjarvis_wv_entangled_gateway.py-12-import httpx
/app/services/msjarvis_wv_entangled_gateway.py-13-import uuid
/app/services/msjarvis_wv_entangled_gateway.py-14-import json
/app/services/msjarvis_wv_entangled_gateway.py-15-import asyncio
/app/services/msjarvis_wv_entangled_gateway.py-16-import redis.asyncio as aioredis
/app/services/msjarvis_wv_entangled_gateway.py-17-from fastapi import FastAPI
/app/services/msjarvis_wv_entangled_gateway.py-18-from fastapi.middleware.cors import CORSMiddleware
/app/services/msjarvis_wv_entangled_gateway.py-19-from pydantic import BaseModel
/app/services/msjarvis_wv_entangled_gateway.py-20-
/app/services/msjarvis_wv_entangled_gateway.py-21-logging.basicConfig(level=logging.INFO)
/app/services/msjarvis_wv_entangled_gateway.py-22-logger = logging.getLogger(__name__)
/app/services/msjarvis_wv_entangled_gateway.py-23-
/app/services/msjarvis_wv_entangled_gateway.py-24-
/app/services/msjarvis_wv_entangled_gateway.py-25-class ChatPayload(BaseModel):
--
/app/services/msjarvis_wv_entangled_gateway.py-92-    try:
/app/services/msjarvis_wv_entangled_gateway.py-93-        logger.info("chat job %s starting", job_id)
/app/services/msjarvis_wv_entangled_gateway.py-94-        user_id = payload.user_id or "anonymous"
/app/services/msjarvis_wv_entangled_gateway.py-95-        wv_ctx = build_wv_entangled_context(payload.message)
/app/services/msjarvis_wv_entangled_gateway.py-96-        _gis_summary = await _fetch_gis_summary(payload.message)
/app/services/msjarvis_wv_entangled_gateway.py-97-        _context = {"system_overrides": {"wv_entangled_context": wv_ctx}}
/app/services/msjarvis_wv_entangled_gateway.py-98-        if _gis_summary:
/app/services/msjarvis_wv_entangled_gateway.py-99-            _context["judge_context_packet"] = {
/app/services/msjarvis_wv_entangled_gateway.py-100-                "spatial_temporal_context": {
/app/services/msjarvis_wv_entangled_gateway.py-101-                    "spatial_candidate": {"summary": _gis_summary}
/app/services/msjarvis_wv_entangled_gateway.py-102-                }
/app/services/msjarvis_wv_entangled_gateway.py-103-            }
/app/services/msjarvis_wv_entangled_gateway.py-104-        forward_payload = {
/app/services/msjarvis_wv_entangled_gateway.py-105-            "message": payload.message,
/app/services/msjarvis_wv_entangled_gateway.py-106-            "user_id": user_id,
/app/services/msjarvis_wv_entangled_gateway.py-107-            "context": _context,
/app/services/msjarvis_wv_entangled_gateway.py-108-        }
/app/services/msjarvis_wv_entangled_gateway.py-109-        logger.info("chat job %s posting to 20llm", job_id)
/app/services/msjarvis_wv_entangled_gateway.py-110-        async with httpx.AsyncClient(timeout=3600.0) as client:
/app/services/msjarvis_wv_entangled_gateway.py-111-            resp = await client.post(
/app/services/msjarvis_wv_entangled_gateway.py:112:                f"{SERVICE_URLS['production_20llm']}/chat_with_context",
/app/services/msjarvis_wv_entangled_gateway.py-113-                json=forward_payload,
/app/services/msjarvis_wv_entangled_gateway.py-114-            )
/app/services/msjarvis_wv_entangled_gateway.py-115-            resp.raise_for_status()
/app/services/msjarvis_wv_entangled_gateway.py-116-            data = resp.json()
/app/services/msjarvis_wv_entangled_gateway.py-117-        logger.info("chat job %s got 20llm response", job_id)
/app/services/msjarvis_wv_entangled_gateway.py-118-
/app/services/msjarvis_wv_entangled_gateway.py-119-        key = f"chatjob:{job_id}"
/app/services/msjarvis_wv_entangled_gateway.py-120-        value = json.dumps({"status": "completed", "result": data})
/app/services/msjarvis_wv_entangled_gateway.py-121-        await _rdb.set(key, value, ex=JOB_TTL)
/app/services/msjarvis_wv_entangled_gateway.py-122-        verify = await _rdb.get(key)
/app/services/msjarvis_wv_entangled_gateway.py-123-        logger.info("chat job %s redis set complete verify_present=%s", job_id, bool(verify))
/app/services/msjarvis_wv_entangled_gateway.py-124-        logger.info("chat job %s completed", job_id)
/app/services/msjarvis_wv_entangled_gateway.py-125-    except Exception as e:
/app/services/msjarvis_wv_entangled_gateway.py-126-        logger.exception("chat job %s failed permanently", job_id)
/app/services/msjarvis_wv_entangled_gateway.py-127-        try:
/app/services/msjarvis_wv_entangled_gateway.py-128-            key = f"chatjob:{job_id}"
/app/services/msjarvis_wv_entangled_gateway.py-129-            value = json.dumps({"status": "failed", "error": f"{type(e).__name__}: {e}"})
/app/services/msjarvis_wv_entangled_gateway.py-130-            await _rdb.set(key, value, ex=JOB_TTL)
/app/services/msjarvis_wv_entangled_gateway.py-131-            logger.info("chat job %s failure status written to redis", job_id)
/app/services/msjarvis_wv_entangled_gateway.py-132-        except Exception:
--
/app/services/msjarvis_wv_entangled_gateway.py-196-    async with httpx.AsyncClient(timeout=5.0) as client:
/app/services/msjarvis_wv_entangled_gateway.py-197-        try:
/app/services/msjarvis_wv_entangled_gateway.py-198-            r = await client.get(f"{SERVICE_URLS['production_20llm']}/health")
/app/services/msjarvis_wv_entangled_gateway.py-199-            ok = r.status_code == 200
/app/services/msjarvis_wv_entangled_gateway.py-200-        except Exception as e:
/app/services/msjarvis_wv_entangled_gateway.py-201-            logger.error(f"20‑LLM health check failed: {e}")
/app/services/msjarvis_wv_entangled_gateway.py-202-            ok = False
/app/services/msjarvis_wv_entangled_gateway.py-203-
/app/services/msjarvis_wv_entangled_gateway.py-204-    return {
/app/services/msjarvis_wv_entangled_gateway.py-205-        "status": "healthy" if ok else "degraded",
/app/services/msjarvis_wv_entangled_gateway.py-206-        "dependencies": {
/app/services/msjarvis_wv_entangled_gateway.py-207-            "production_20llm": "healthy" if ok else "unavailable",
/app/services/msjarvis_wv_entangled_gateway.py-208-        },
/app/services/msjarvis_wv_entangled_gateway.py-209-        "timestamp": datetime.utcnow().isoformat(),
/app/services/msjarvis_wv_entangled_gateway.py-210-    }
/app/services/msjarvis_wv_entangled_gateway.py-211-
/app/services/msjarvis_wv_entangled_gateway.py-212-
/app/services/msjarvis_wv_entangled_gateway.py-213-@app.post("/chat_wv")
/app/services/msjarvis_wv_entangled_gateway.py-214-async def chat_wv(payload: ChatPayload):
/app/services/msjarvis_wv_entangled_gateway.py-215-    """
/app/services/msjarvis_wv_entangled_gateway.py:216:    WV‑focused chat: send message + WV entangled context to 20‑LLM /chat_with_context.
/app/services/msjarvis_wv_entangled_gateway.py-217-    """
/app/services/msjarvis_wv_entangled_gateway.py-218-    logger.info("WV‑Entangled /chat_wv invoked")
/app/services/msjarvis_wv_entangled_gateway.py-219-    user_id = payload.user_id or "anonymous"
/app/services/msjarvis_wv_entangled_gateway.py-220-    wv_ctx = build_wv_entangled_context(payload.message)
/app/services/msjarvis_wv_entangled_gateway.py-221-
/app/services/msjarvis_wv_entangled_gateway.py-222-    forward_payload = {
/app/services/msjarvis_wv_entangled_gateway.py-223-        "message": payload.message,
/app/services/msjarvis_wv_entangled_gateway.py-224-        "user_id": user_id,
/app/services/msjarvis_wv_entangled_gateway.py-225-        "context": {
/app/services/msjarvis_wv_entangled_gateway.py-226-            "system_overrides": {
/app/services/msjarvis_wv_entangled_gateway.py-227-                "wv_entangled_context": wv_ctx
/app/services/msjarvis_wv_entangled_gateway.py-228-            }
/app/services/msjarvis_wv_entangled_gateway.py-229-        },
/app/services/msjarvis_wv_entangled_gateway.py-230-    }
/app/services/msjarvis_wv_entangled_gateway.py-231-
/app/services/msjarvis_wv_entangled_gateway.py-232-    async with httpx.AsyncClient(timeout=3600.0) as client:
/app/services/msjarvis_wv_entangled_gateway.py-233-        resp = await client.post(
/app/services/msjarvis_wv_entangled_gateway.py:234:            f"{SERVICE_URLS['production_20llm']}/chat_with_context",
/app/services/msjarvis_wv_entangled_gateway.py-235-            json=forward_payload,
/app/services/msjarvis_wv_entangled_gateway.py-236-        )
/app/services/msjarvis_wv_entangled_gateway.py-237-        resp.raise_for_status()
/app/services/msjarvis_wv_entangled_gateway.py-238-        data = resp.json()
/app/services/msjarvis_wv_entangled_gateway.py-239-
/app/services/msjarvis_wv_entangled_gateway.py-240-    return data
/app/services/msjarvis_wv_entangled_gateway.py-241-
/app/services/msjarvis_wv_entangled_gateway.py-242-
/app/services/msjarvis_wv_entangled_gateway.py-243-@app.post("/chat_wv/async")
/app/services/msjarvis_wv_entangled_gateway.py-244-async def chat_wv_async(payload: ChatPayload):
/app/services/msjarvis_wv_entangled_gateway.py-245-    logger.info("WV async inbound user_id=%r actor_role=%r has_judge_context_packet=%s",
/app/services/msjarvis_wv_entangled_gateway.py-246-                payload.user_id, None, False)
/app/services/msjarvis_wv_entangled_gateway.py-247-    """Submit a chat job to the worker queue; returns immediately."""
/app/services/msjarvis_wv_entangled_gateway.py-248-    logger.info("WV async inbound user_id=%r actor_role=%r has_judge_context_packet=%r", getattr(payload, "user_id", None), getattr(payload, "actor_role", None), bool(getattr(payload, "judge_context_packet", None)))
/app/services/msjarvis_wv_entangled_gateway.py-249-    job_id = uuid.uuid4().hex
/app/services/msjarvis_wv_entangled_gateway.py-250-    await _rdb.set(f"chatjob:{job_id}",
/app/services/msjarvis_wv_entangled_gateway.py-251-                   json.dumps({"status": "queued"}), ex=JOB_TTL)
/app/services/msjarvis_wv_entangled_gateway.py-252-    await _rdb.lpush("chatjob:queue", json.dumps({
/app/services/msjarvis_wv_entangled_gateway.py-253-        "job_id": job_id,
/app/services/msjarvis_wv_entangled_gateway.py-254-        "message": payload.message,
--
/app/services/ai_server_20llm_FINAL.py-113-        if not responses:
/app/services/ai_server_20llm_FINAL.py-114-            return "I apologize, I'm having trouble processing right now."
/app/services/ai_server_20llm_FINAL.py-115-        weighted = calculate_weighted_consensus(responses)
/app/services/ai_server_20llm_FINAL.py-116-        top_3 = sorted(weighted, key=lambda x: x["weight"], reverse=True)[:3]
/app/services/ai_server_20llm_FINAL.py-117-        combined = top_3[0]["response"]
/app/services/ai_server_20llm_FINAL.py-118-        if len(top_3) > 1 and len(combined) < 500:
/app/services/ai_server_20llm_FINAL.py-119-            combined += "\n\n" + top_3[1]["response"][:300]
/app/services/ai_server_20llm_FINAL.py-120-        return combined.strip()
/app/services/ai_server_20llm_FINAL.py-121-
/app/services/ai_server_20llm_FINAL.py-122-    async def process_with_prompt(self, prompt: str) -> str:
/app/services/ai_server_20llm_FINAL.py-123-        responses = await self.process_all_sequential(prompt)
/app/services/ai_server_20llm_FINAL.py-124-        final_response = self.synthesize_responses(responses)
/app/services/ai_server_20llm_FINAL.py-125-        return final_response
/app/services/ai_server_20llm_FINAL.py-126-
/app/services/ai_server_20llm_FINAL.py-127-brain = SequentialBrain()
/app/services/ai_server_20llm_FINAL.py-128-
/app/services/ai_server_20llm_FINAL.py-129-@app.get("/health")
/app/services/ai_server_20llm_FINAL.py-130-async def health():
/app/services/ai_server_20llm_FINAL.py-131-    return {"status": "healthy", "models": len(brain.models), "mode": "sequential"}
/app/services/ai_server_20llm_FINAL.py-132-
/app/services/ai_server_20llm_FINAL.py:133:@app.post("/chat_with_context")
/app/services/ai_server_20llm_FINAL.py-134-
/app/services/ai_server_20llm_FINAL.py:135:async def chat_with_context(request: ChatRequestWithContext):
/app/services/ai_server_20llm_FINAL.py-136-    msg = (getattr(request, "message", None) or "").strip()
/app/services/ai_server_20llm_FINAL.py-137-    normalized = " ".join(msg.lower().split()).strip(" ?!.")
/app/services/ai_server_20llm_FINAL.py-138-    if normalized == "what county is mount hope in":
/app/services/ai_server_20llm_FINAL.py-139-        logger.warning("Mount Hope hard-stop guard triggered user_id=%r", getattr(request, "user_id", None))
/app/services/ai_server_20llm_FINAL.py-140-        return {
/app/services/ai_server_20llm_FINAL.py-141-            "response": "HEALTHCHECK_BLOCKED",
/app/services/ai_server_20llm_FINAL.py-142-            "minds_participated": 0,
/app/services/ai_server_20llm_FINAL.py-143-            "total_minds": 21,
/app/services/ai_server_20llm_FINAL.py-144-            "timestamp": None,
/app/services/ai_server_20llm_FINAL.py-145-            "used_wv_entangled_context": False,
/app/services/ai_server_20llm_FINAL.py-146-        }
/app/services/ai_server_20llm_FINAL.py-147-
/app/services/ai_server_20llm_FINAL.py-148-    try:
/app/services/ai_server_20llm_FINAL.py-149-        logger.info("💬 Contextual query: %s...", request.message[:50])
/app/services/ai_server_20llm_FINAL.py-150-        prompt = build_prompt(request.message, request.context or {})
/app/services/ai_server_20llm_FINAL.py-151-        final_response = await brain.process_with_prompt(prompt)
/app/services/ai_server_20llm_FINAL.py-152-        active_models = [m for m in brain.models if m.get("active", True)]
/app/services/ai_server_20llm_FINAL.py-153-        return {
/app/services/ai_server_20llm_FINAL.py-154-            "response": final_response,
/app/services/ai_server_20llm_FINAL.py-155-            "minds_participated": len(active_models),
/app/services/ai_server_20llm_FINAL.py-156-            "total_minds": len(active_models),
/app/services/ai_server_20llm_FINAL.py-157-            "timestamp": datetime.now().isoformat(),
/app/services/ai_server_20llm_FINAL.py-158-            "used_wv_entangled_context": bool(
/app/services/ai_server_20llm_FINAL.py-159-                (request.context or {})
/app/services/ai_server_20llm_FINAL.py-160-                .get("system_overrides", {})
/app/services/ai_server_20llm_FINAL.py-161-                .get("wv_entangled_context")
/app/services/ai_server_20llm_FINAL.py-162-            ),
/app/services/ai_server_20llm_FINAL.py-163-        }
/app/services/ai_server_20llm_FINAL.py-164-    except Exception as e:
/app/services/ai_server_20llm_FINAL.py:165:        logger.error("Error in /chat_with_context: %s", e)
/app/services/ai_server_20llm_FINAL.py-166-        raise HTTPException(status_code=500, detail="Error processing contextual request")
/app/services/ai_server_20llm_FINAL.py-167-
/app/services/ai_server_20llm_FINAL.py-168-@app.post("/chat")
/app/services/ai_server_20llm_FINAL.py-169-async def chat(request: ChatRequest):
/app/services/ai_server_20llm_FINAL.py-170-    try:
/app/services/ai_server_20llm_FINAL.py-171-        logger.info("💬 Query: %s...", request.message[:50])
/app/services/ai_server_20llm_FINAL.py-172-        responses = await brain.process_all_sequential(request.message)
/app/services/ai_server_20llm_FINAL.py-173-        final_response = brain.synthesize_responses(responses)
/app/services/ai_server_20llm_FINAL.py-174-        return {
/app/services/ai_server_20llm_FINAL.py-175-            "response": final_response,
/app/services/ai_server_20llm_FINAL.py-176-            "minds_participated": len(responses),
/app/services/ai_server_20llm_FINAL.py-177-            "total_minds": len(brain.models),
/app/services/ai_server_20llm_FINAL.py-178-            "processing_mode": "sequential",
/app/services/ai_server_20llm_FINAL.py-179-            "timestamp": datetime.now().isoformat(),
/app/services/ai_server_20llm_FINAL.py-180-        }
/app/services/ai_server_20llm_FINAL.py-181-    except Exception as e:
/app/services/ai_server_20llm_FINAL.py-182-        logger.error("Error: %s", e)
/app/services/ai_server_20llm_FINAL.py-183-        return {"response": "Error processing request", "error": str(e)}
/app/services/ai_server_20llm_FINAL.py-184-
/app/services/ai_server_20llm_FINAL.py-185-if __name__ == "__main__":
--
/app/services/ai_server_20llm_PRODUCTION.py-502-
/app/services/ai_server_20llm_PRODUCTION.py-503-        # Use only the top consensus response to avoid double-voice stitching
/app/services/ai_server_20llm_PRODUCTION.py-504-        combined = top_3[0]["response"]
/app/services/ai_server_20llm_PRODUCTION.py-505-
/app/services/ai_server_20llm_PRODUCTION.py-506-        return combined.strip()
/app/services/ai_server_20llm_PRODUCTION.py-507-
/app/services/ai_server_20llm_PRODUCTION.py-508-
/app/services/ai_server_20llm_PRODUCTION.py-509-brain = ProductionBrain()
/app/services/ai_server_20llm_PRODUCTION.py-510-
/app/services/ai_server_20llm_PRODUCTION.py-511-
/app/services/ai_server_20llm_PRODUCTION.py-512-@app.get("/health")
/app/services/ai_server_20llm_PRODUCTION.py-513-async def health():
/app/services/ai_server_20llm_PRODUCTION.py-514-    active_models = [m for m in brain.models if m.get("active", True)]
/app/services/ai_server_20llm_PRODUCTION.py-515-    return {
/app/services/ai_server_20llm_PRODUCTION.py-516-        "status": "healthy",
/app/services/ai_server_20llm_PRODUCTION.py-517-        "models": len(active_models),
/app/services/ai_server_20llm_PRODUCTION.py-518-        "mode": "production",
/app/services/ai_server_20llm_PRODUCTION.py-519-    }
/app/services/ai_server_20llm_PRODUCTION.py-520-
/app/services/ai_server_20llm_PRODUCTION.py-521-
/app/services/ai_server_20llm_PRODUCTION.py:522:@app.post("/chat_with_context")
/app/services/ai_server_20llm_PRODUCTION.py-523-
/app/services/ai_server_20llm_PRODUCTION.py:524:async def chat_with_context(request: ChatRequestWithContext, x_debug_echo: str | None = Header(default=None)):
/app/services/ai_server_20llm_PRODUCTION.py-525-    import logging
/app/services/ai_server_20llm_PRODUCTION.py-526-    logger = logging.getLogger(__name__)
/app/services/ai_server_20llm_PRODUCTION.py-527-    ctx = request.context if isinstance(request.context, dict) else {}
/app/services/ai_server_20llm_PRODUCTION.py-528-    logger.info("20llm inbound userid/role debug userid=%r role=%r context_keys=%r", ctx.get("userid"), ctx.get("role"), sorted(list(ctx.keys())) if isinstance(ctx, dict) else None)
/app/services/ai_server_20llm_PRODUCTION.py-529-    msg = (getattr(request, "message", None) or "").strip()
/app/services/ai_server_20llm_PRODUCTION.py-530-    normalized = " ".join(msg.lower().split()).strip(" ?!.")
/app/services/ai_server_20llm_PRODUCTION.py-531-    if normalized == "what county is mount hope in":
/app/services/ai_server_20llm_PRODUCTION.py-532-        logger.warning("Mount Hope hard-stop guard triggered user_id=%r", getattr(request, "user_id", None))
/app/services/ai_server_20llm_PRODUCTION.py-533-        return {
/app/services/ai_server_20llm_PRODUCTION.py-534-            "response": "HEALTHCHECK_BLOCKED",
/app/services/ai_server_20llm_PRODUCTION.py-535-            "minds_participated": 0,
/app/services/ai_server_20llm_PRODUCTION.py-536-            "total_minds": 21,
/app/services/ai_server_20llm_PRODUCTION.py-537-            "timestamp": None,
/app/services/ai_server_20llm_PRODUCTION.py-538-            "used_wv_entangled_context": False,
/app/services/ai_server_20llm_PRODUCTION.py-539-        }
/app/services/ai_server_20llm_PRODUCTION.py-540-
/app/services/ai_server_20llm_PRODUCTION.py-541-    ctx = request.context if isinstance(request.context, dict) else {}
/app/services/ai_server_20llm_PRODUCTION.py-542-    keys = sorted(list(ctx.keys())) if isinstance(ctx, dict) else []
/app/services/ai_server_20llm_PRODUCTION.py-543-    has_jcp = isinstance(ctx.get("judge_context_packet"), dict) if isinstance(ctx, dict) else False
/app/services/ai_server_20llm_PRODUCTION.py-544-    logger.info(
--
/app/services/ai_server_20llm_PRODUCTION.py-569-        }
/app/services/ai_server_20llm_PRODUCTION.py-570-
/app/services/ai_server_20llm_PRODUCTION.py-571-    try:
/app/services/ai_server_20llm_PRODUCTION.py-572-        logger.info("💬 Contextual query: %s...", request.message[:50])
/app/services/ai_server_20llm_PRODUCTION.py-573-        # Build WV‑aware prompt when context is present (hard requirement enforced inside)
/app/services/ai_server_20llm_PRODUCTION.py-574-        prompt = build_prompt(request.message, request.context or {})
/app/services/ai_server_20llm_PRODUCTION.py-575-        final_response = await brain.process_with_prompt(prompt)
/app/services/ai_server_20llm_PRODUCTION.py-576-        active_models = [m for m in brain.models if m.get("active", True)]
/app/services/ai_server_20llm_PRODUCTION.py-577-        return {
/app/services/ai_server_20llm_PRODUCTION.py-578-            "response": final_response,
/app/services/ai_server_20llm_PRODUCTION.py-579-            "minds_participated": len(active_models),  # all attempted
/app/services/ai_server_20llm_PRODUCTION.py-580-            "total_minds": len(active_models),
/app/services/ai_server_20llm_PRODUCTION.py-581-            "timestamp": datetime.now().isoformat(),
/app/services/ai_server_20llm_PRODUCTION.py-582-            "used_wv_entangled_context": bool(
/app/services/ai_server_20llm_PRODUCTION.py-583-                (request.context or {})
/app/services/ai_server_20llm_PRODUCTION.py-584-                .get("system_overrides", {})
/app/services/ai_server_20llm_PRODUCTION.py-585-                .get("wv_entangled_context")
/app/services/ai_server_20llm_PRODUCTION.py-586-            ),
/app/services/ai_server_20llm_PRODUCTION.py-587-        }
/app/services/ai_server_20llm_PRODUCTION.py-588-    except Exception as e:
/app/services/ai_server_20llm_PRODUCTION.py:589:        logger.error("Error in /chat_with_context: %s", e)
/app/services/ai_server_20llm_PRODUCTION.py-590-        raise HTTPException(status_code=500, detail="Error processing contextual request")
/app/services/ai_server_20llm_PRODUCTION.py-591-
/app/services/ai_server_20llm_PRODUCTION.py-592-
/app/services/ai_server_20llm_PRODUCTION.py-593-@app.post("/chat")
/app/services/ai_server_20llm_PRODUCTION.py-594-async def chat(request: ChatRequest):
/app/services/ai_server_20llm_PRODUCTION.py-595-    try:
/app/services/ai_server_20llm_PRODUCTION.py-596-        logger.info("💬 Query: %s...", request.message[:50])
/app/services/ai_server_20llm_PRODUCTION.py-597-
/app/services/ai_server_20llm_PRODUCTION.py-598-        # Hard cap the entire 20‑LLM fabric to 600 seconds.
/app/services/ai_server_20llm_PRODUCTION.py-599-        # If this trips, we still return a graceful fallback instead of hanging.
/app/services/ai_server_20llm_PRODUCTION.py-600-        try:
/app/services/ai_server_20llm_PRODUCTION.py-601-            responses = await asyncio.wait_for(
/app/services/ai_server_20llm_PRODUCTION.py-602-                brain.process_all(request.message),
/app/services/ai_server_20llm_PRODUCTION.py-603-                timeout=3600,
/app/services/ai_server_20llm_PRODUCTION.py-604-            )
/app/services/ai_server_20llm_PRODUCTION.py-605-        except asyncio.TimeoutError:
/app/services/ai_server_20llm_PRODUCTION.py-606-            logger.warning("⚠️  /chat: overall 20‑LLM processing timed out at 600s")
/app/services/ai_server_20llm_PRODUCTION.py-607-            responses = []
/app/services/ai_server_20llm_PRODUCTION.py-608-
/app/services/ai_server_20llm_PRODUCTION.py-609-        final_response = brain.synthesize(responses)
--
/app/services/ai_server_20llm_PRODUCTION.py-618-                "response": r.get("response", ""),
/app/services/ai_server_20llm_PRODUCTION.py-619-                "confidence": r.get("weight", 0.5),
/app/services/ai_server_20llm_PRODUCTION.py-620-                "specialty": r.get("specialty", ""),
/app/services/ai_server_20llm_PRODUCTION.py-621-                "success": bool(r.get("response", "")),
/app/services/ai_server_20llm_PRODUCTION.py-622-            }
/app/services/ai_server_20llm_PRODUCTION.py-623-            for r in responses
/app/services/ai_server_20llm_PRODUCTION.py-624-        ]
/app/services/ai_server_20llm_PRODUCTION.py-625-
/app/services/ai_server_20llm_PRODUCTION.py-626-        return {
/app/services/ai_server_20llm_PRODUCTION.py-627-            "response": final_response,
/app/services/ai_server_20llm_PRODUCTION.py-628-            "minds_participated": len(responses),
/app/services/ai_server_20llm_PRODUCTION.py-629-            "total_minds": len(active_models),
/app/services/ai_server_20llm_PRODUCTION.py-630-            "timestamp": datetime.now().isoformat(),
/app/services/ai_server_20llm_PRODUCTION.py-631-            "expert_responses": _last_expert_responses,
/app/services/ai_server_20llm_PRODUCTION.py-632-        }
/app/services/ai_server_20llm_PRODUCTION.py-633-    except Exception as e:
/app/services/ai_server_20llm_PRODUCTION.py-634-        logger.error("Error in /chat: %s", e)
/app/services/ai_server_20llm_PRODUCTION.py-635-        raise HTTPException(status_code=500, detail="Error processing request")
/app/services/ai_server_20llm_PRODUCTION.py-636-
/app/services/ai_server_20llm_PRODUCTION.py-637-
/app/services/ai_server_20llm_PRODUCTION.py:638:@app.get("/cached_expert_responses")
/app/services/ai_server_20llm_PRODUCTION.py:639:async def cached_expert_responses():
/app/services/ai_server_20llm_PRODUCTION.py-640-    """Return the expert responses from the last /chat call (Chapter 33 §33.2)"""
/app/services/ai_server_20llm_PRODUCTION.py-641-    return {
/app/services/ai_server_20llm_PRODUCTION.py-642-        "expert_responses": _last_expert_responses,
/app/services/ai_server_20llm_PRODUCTION.py-643-        "count": len(_last_expert_responses),
/app/services/ai_server_20llm_PRODUCTION.py-644-    }
/app/services/ai_server_20llm_PRODUCTION.py-645-
/app/services/ai_server_20llm_PRODUCTION.py-646-
/app/services/ai_server_20llm_PRODUCTION.py-647-if __name__ == "__main__":
/app/services/ai_server_20llm_PRODUCTION.py-648-    uvicorn.run(
/app/services/ai_server_20llm_PRODUCTION.py-649-        app,
/app/services/ai_server_20llm_PRODUCTION.py-650-        host="0.0.0.0",
/app/services/ai_server_20llm_PRODUCTION.py-651-        port=int(os.getenv("SERVICE_PORT", "8008")),
/app/services/ai_server_20llm_PRODUCTION.py-652-    )
--
/app/services/msjarvismaingateway.py-74-    gbim = client.get_collection("GBIM")
/app/services/msjarvismaingateway.py-75-    results = gbim.query(query_texts=[query], n_results=1)
/app/services/msjarvismaingateway.py-76-    context = results['documents'][0] if results['documents'] else "No result"
/app/services/msjarvismaingateway.py-77-    ollama_payload = {
/app/services/msjarvismaingateway.py-78-        "model": "llama3",
/app/services/msjarvismaingateway.py-79-        "prompt": f"Summarize this asset: {context}"
/app/services/msjarvismaingateway.py-80-    }
/app/services/msjarvismaingateway.py-81-    response = requests.post("http://localhost:11434/api/generate", json=ollama_payload, stream=True)
/app/services/msjarvismaingateway.py-82-    summary_chunks = []
/app/services/msjarvismaingateway.py-83-    for line in response.iter_lines():
/app/services/msjarvismaingateway.py-84-        if line:
/app/services/msjarvismaingateway.py-85-            obj = json.loads(line.decode('utf-8'))
/app/services/msjarvismaingateway.py-86-            if "response" in obj:
/app/services/msjarvismaingateway.py-87-                summary_chunks.append(obj["response"])
/app/services/msjarvismaingateway.py-88-    return {
/app/services/msjarvismaingateway.py-89-        "query": query,
/app/services/msjarvismaingateway.py-90-        "context": context,
/app/services/msjarvismaingateway.py-91-        "llm_summary": "".join(summary_chunks)
/app/services/msjarvismaingateway.py-92-    }
/app/services/msjarvismaingateway.py-93-
/app/services/msjarvismaingateway.py:94:PRODUCTION_20LLM_URL = "http://jarvis-20llm-production:8008/chat_with_context"
/app/services/msjarvismaingateway.py-95-API_KEY = os.getenv("API_KEY")
/app/services/msjarvismaingateway.py-96-
/app/services/msjarvismaingateway.py-97-def call_production_20llm(user_message: str, user_id: str):
/app/services/msjarvismaingateway.py-98-    wv_ctx = build_wv_entangled_context(user_message)
/app/services/msjarvismaingateway.py-99-    payload = {
/app/services/msjarvismaingateway.py-100-        "message": user_message,
/app/services/msjarvismaingateway.py-101-        "user_id": user_id,
/app/services/msjarvismaingateway.py-102-        "context": {
/app/services/msjarvismaingateway.py-103-            "system_overrides": {
/app/services/msjarvismaingateway.py-104-                "wv_entangled_context": wv_ctx
/app/services/msjarvismaingateway.py-105-            }

===== IMPLEMENTATION INSPECTION MANIFEST =====
5d835fc76e09f9fc66aac62d065014949fb92d5dc587b4a837bdf878284086a9  /mnt/nvme1/msjarvis-rebuild/research/meaning_geometry_source_record_v1/inspection/governed_route_discovery/20llm-container-runtime.txt
e3dd12cde2bcb2e96d6cd0a715657836198314ddd35ef6c3660e375a8dd331de  /mnt/nvme1/msjarvis-rebuild/research/meaning_geometry_source_record_v1/inspection/governed_route_discovery/20llm-contract-probe-logs.txt
d98ddc9745de60576c182d0f912f5546fdc63c9bf95a5e60c93cf67c3acf7ac9  /mnt/nvme1/msjarvis-rebuild/research/meaning_geometry_source_record_v1/inspection/governed_route_discovery/20llm-answer-route-source-index.txt
a54e9d03652df1de87816f1b26c3fb0293909d439e46868692dbabc507b912ed  /mnt/nvme1/msjarvis-rebuild/research/meaning_geometry_source_record_v1/inspection/governed_route_discovery/20llm-answer-route-source-context.txt
(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:/mnt/nvme1/msjarvis-rebuild$ 

