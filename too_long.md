app.post("/chat/async")
(.venv) cakidd@cakidd-Legion-5-16IRX9:/opt/msjarvis-rebuild/ms-allis-frontend$ # Is jarvis-auth-api healthy?
docker ps | grep auth
docker logs jarvis-auth-api --since=5m 2>&1 | tail -20
5d95578fb815   msjarvis-rebuild-jarvis-auth-api                      "sh -lc 'cd /app/ser…"   8 days ago     Up 8 days (healthy)     127.0.0.1:8092->8091/tcp                                                                                       jarvis-auth-api
INFO:     127.0.0.1:39186 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:36234 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:39168 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:48356 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:50200 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:43066 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:57098 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:53834 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:47304 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:50648 - "GET /health HTTP/1.1" 200 OK
(.venv) cakidd@cakidd-Legion-5-16IRX9:/opt/msjarvis-rebuild/ms-allis-frontend$ # Check if the browser job actually exists in active_jobs right now
curl -s -H "X-API-Key: 65ad4816de9004910599e6313fddfc2cd372e1269c20d0d4f02efd2cbbcc1a56" \
  http://127.0.0.1:8050/chatstatus/92c6c09f-e420-418b-a6bd-6a5cc3c7df45 | jq .
{
  "jobid": "92c6c09f-e420-418b-a6bd-6a5cc3c7df45",
  "status": "complete",
  "progress": "Complete!",
  "result": {
    "response": "Darling! I'm so glad you're here! It's been too long since we've had a chance to chat. How are you doing today? Is everything going smoothly in our little corner of the world?",
    "servicesused": [
      "llm20production"
    ],
    "consciousnesslevel": "ultimatecollective",
    "processingtime": 117.85229349136353,
    "architecturelayers": 5,
    "consciousnesslayers": [
      {
        "name": "prefrontal-planner",
        "kind": "prefrontal",
        "status": "active",
        "details": {
          "available_services": [
            "qualiaengine",
            "consciousnessbridge",
            "bloodbrainbarrier",
            "neurobiologicalmaster",
            "icontainers",
            "woahalgorithms",
            "toroidal",
            "motherprotocols",
            "unifiedgateway",
            "chroma",
            "hippocampus",
            "redis",
            "brainorchestrator",
            "fifthdgm",
            "swarmintelligence",
            "ragserver",
            "aaacperag",
            "llm20production",
            "lmsynthesizer",
            "semaphore",
            "mainbrain",
            "judgepipeline",
            "psychology",
            "nbbwoahalgorithms",
            "nbbprefrontalcortex",
            "nbbsubconscious",
            "nbbicontainers"
          ]
        }
      },
      {
        "name": "nbb-prefrontal-cortex",
        "kind": "nbb",
        "status": "active",
        "details": {
          "status": "ok",
          "data": {
            "mode": "consolidation",
            "cortisol": 0.0,
            "urgency": 0.0,
            "warmth": 0.85,
            "timestamp": "2026-05-12T04:49:48.197150",
            "recommendation": "Memory consolidation mode. Reflective pacing.",
            "broadcast_sent": true
          },
          "error": null
        }
      },
      {
        "name": "icontainers-identity",
        "kind": "identity",
        "status": "active",
        "details": {
          "status": "ok",
          "identity_layers": [
            {
              "kind": "experiential",
              "weight": 1.0,
              "data": {
                "self_recognition": {
                  "recognized": true,
                  "reason": "implicit self-recognition within configured identity profile",
                  "state": {
                    "timestamp": "2026-05-12T04:49:48.207846Z",
                    "identity_coherence": 0.6,
                    "active_self_aspects": [
                      "developer",
                      "creator",
                      "observer"
                    ],
                    "confidence": 0.7
                  },
                  "message": null,
                  "metadata": {}
                },
                "identity_core": {
                  "recognized": true,
                  "reason": "identity-core aligned with configured values",
                  "state": {
                    "timestamp": "2026-05-12T04:49:48.207852Z",
                    "core_stability": 0.9,
                    "core_values": [
                      "care",
                      "learning",
                      "integrity"
                    ],
                    "confidence": 0.9
                  },
                  "message": null,
                  "metadata": {}
                },
                "ego_check": {
                  "input": "Ms. Allis?",
                  "within_bounds": true,
                  "category": "unspecified",
                  "severity": "info",
                  "reason": "within configured ego-boundary limits",
                  "details": {
                    "input": "Ms. Allis?",
                    "within_bounds": true,
                    "category": "unspecified",
                    "severity": "info",
                    "reason": "within configured ego-boundary limits",
                    "details": {
                      "allowed": true,
                      "reason": "within configured ego-boundary limits",
                      "boundary_mode": "healthy",
                      "active_limits": [
                        "no_recursive_overload",
                        "respect_rate_limits",
                        "filter_high_risk_content"
                      ],
                      "metadata": {
                        "length": 10,
                        "has_risk_keywords": false
                      }
                    },
                    "ego_boundaries": {},
                    "experiential_processing": {},
                    "timestamp": "2026-05-12T04:49:48.207836Z"
                  },
                  "ego_boundaries": {},
                  "experiential_processing": {}
                },
                "narrative_context": {
                  "summary": "Ms. Allis?",
                  "state": {
                    "timestamp": "2026-05-12T04:49:48.207855Z",
                    "story_coherence": 0.9,
                    "key_events": [],
                    "confidence": 0.9
                  },
                  "metadata": {}
                },
                "memory_state": {
                  "state": {
                    "timestamp": "2026-05-12T04:49:48.207859Z",
                    "recent_memories": [
                      "Ms. Allis?",
                      "Ms. Allis?",
                      "hello",
                      "hello test",
                      "Hello Allis",
                      "Hello Allis",
                      "Ms. Allis?",
                      "Hello Allis, are you there?",
                      "Ms. Allis?",
                      "Hello Allis",
                      "Ms. Allis?",
                      "hello",
                      "hello",
                      "hello",
                      "hello",
                      "hello",
                      "hello",
                      "hello",
                      "MS. Allis?",
                      "hello",
                      "hello"
                    ],
                    "memory_load": 0.3,
                    "confidence": 0.9
                  },
                  "metadata": {}
                }
              }
            },
            {
              "kind": "observer",
              "weight": 1.0,
              "data": {
                "witness": {
                  "observed": true,
                  "state": {
                    "timestamp": "2026-05-12T04:49:48.207862Z",
                    "observing": true,
                    "observed_thoughts": [
                      {
                        "self_recognition": {
                          "recognized": true,
                          "reason": "implicit self-recognition within configured identity profile",
                          "state": {
                            "timestamp": "2026-05-12T01:48:09.274995Z",
                            "identity_coherence": 0.6,
                            "active_self_aspects": [
                              "developer",
                              "creator",
                              "observer"
                            ],
                            "confidence": 0.7
                          },
                          "message": null,
                          "metadata": {}
                        },
                        "identity_core": {
                          "recognized": true,
                          "reason": "identity-core aligned with configured values",
                          "state": {
                            "timestamp": "2026-05-12T01:48:09.275012Z",
                            "core_stability": 0.9,
                            "core_values": [
                              "care",
                              "learning",
                              "integrity"
                            ],
                            "confidence": 0.9
                          },
                          "message": null,
                          "metadata": {}
                        },
                        "ego_check": {
                          "input": "Ms. Allis?",
                          "within_bounds": true,
                          "category": "unspecified",
                          "severity": "info",
                          "reason": "within configured ego-boundary limits",
                          "details": {
                            "input": "Ms. Allis?",
                            "within_bounds": true,
                            "category": "unspecified",
                            "severity": "info",
                            "reason": "within configured ego-boundary limits",
                            "details": {
                              "allowed": true,
                              "reason": "within configured ego-boundary limits",
                              "boundary_mode": "healthy",
                              "active_limits": [
                                "no_recursive_overload",
                                "respect_rate_limits",
                                "filter_high_risk_content"
                              ],
                              "metadata": {
                                "length": 10,
                                "has_risk_keywords": false
                              }
                            },
                            "ego_boundaries": {},
                            "experiential_processing": {},
                            "timestamp": "2026-05-12T01:48:09.274983Z"
                          },
                          "ego_boundaries": {},
                          "experiential_processing": {}
                        },
                        "narrative_context": {
                          "summary": "Ms. Allis?",
                          "state": {
                            "timestamp": "2026-05-12T01:48:09.275017Z",
                            "story_coherence": 0.9,
                            "key_events": [],
                            "confidence": 0.9
                          },
                          "metadata": {}
                        },
                        "memory_state": {
                          "state": {
                            "timestamp": "2026-05-12T01:48:09.275021Z",
                            "recent_memories": [],
                            "memory_load": 0.3,
                            "confidence": 0.9
                          },
                          "metadata": {}
                        }
                      },
                      {
                        "self_recognition": {
                          "recognized": true,
                          "reason": "implicit self-recognition within configured identity profile",
                          "state": {
                            "timestamp": "2026-05-12T02:04:33.519632Z",
                            "identity_coherence": 0.6,
                            "active_self_aspects": [
                              "developer",
                              "creator",
                              "observer"
                            ],
                            "confidence": 0.7
                          },
                          "message": null,
                          "metadata": {}
                        },
                        "identity_core": {
                          "recognized": true,
                          "reason": "identity-core aligned with configured values",
                          "state": {
                            "timestamp": "2026-05-12T02:04:33.519644Z",
                            "core_stability": 0.9,
                            "core_values": [
                              "care",
                              "learning",
                              "integrity"
                            ],
                            "confidence": 0.9
                          },
                          "message": null,
                          "metadata": {}
                        },
                        "ego_check": {
                          "input": "Ms. Allis?",
                          "within_bounds": true,
                          "category": "unspecified",
                          "severity": "info",
                          "reason": "within configured ego-boundary limits",
                          "details": {
                            "input": "Ms. Allis?",
                            "within_bounds": true,
                            "category": "unspecified",
                            "severity": "info",
                            "reason": "within configured ego-boundary limits",
                            "details": {
                              "allowed": true,
                              "reason": "within configured ego-boundary limits",
                              "boundary_mode": "healthy",
                              "active_limits": [
                                "no_recursive_overload",
                                "respect_rate_limits",
                                "filter_high_risk_content"
                              ],
                              "metadata": {
                                "length": 10,
                                "has_risk_keywords": false
                              }
                            },
                            "ego_boundaries": {},
                            "experiential_processing": {},
                            "timestamp": "2026-05-12T02:04:33.519616Z"
                          },
                          "ego_boundaries": {},
                          "experiential_processing": {}
                        },
                        "narrative_context": {
                          "summary": "Ms. Allis?",
                          "state": {
                            "timestamp": "2026-05-12T02:04:33.519649Z",
                            "story_coherence": 0.9,
                            "key_events": [],
                            "confidence": 0.9
                          },
                          "metadata": {}
                        },
                        "memory_state": {
                          "state": {
                            "timestamp": "2026-05-12T02:04:33.519654Z",
                            "recent_memories": [
                              "Ms. Allis?"
                            ],
                            "memory_load": 0.3,
                            "confidence": 0.9
                          },
                          "metadata": {}
                        }
                      },
                      {
                        "self_recognition": {
                          "recognized": true,
                          "reason": "implicit self-recognition within configured identity profile",
                          "state": {
                            "timestamp": "2026-05-12T02:28:29.943932Z",
                            "identity_coherence": 0.6,
                            "active_self_aspects": [
                              "developer",
                              "creator",
                              "observer"
                            ],
                            "confidence": 0.7
                          },
                          "message": null,
                          "metadata": {}
                        },
                        "identity_core": {
                          "recognized": true,
                          "reason": "identity-core aligned with configured values",
                          "state": {
                            "timestamp": "2026-05-12T02:28:29.943952Z",
                            "core_stability": 0.9,
                            "core_values": [
                              "care",
                              "learning",
                              "integrity"
                            ],
                            "confidence": 0.9
                          },
                          "message": null,
                          "metadata": {}
                        },
                        "ego_check": {
                          "input": "hello",
                          "within_bounds": true,
                          "category": "unspecified",
                          "severity": "info",
                          "reason": "within configured ego-boundary limits",
                          "details": {
                            "input": "hello",
                            "within_bounds": true,
                            "category": "unspecified",
                            "severity": "info",
                            "reason": "within configured ego-boundary limits",
                            "details": {
                              "allowed": true,
                              "reason": "within configured ego-boundary limits",
                              "boundary_mode": "healthy",
                              "active_limits": [
                                "no_recursive_overload",
                                "respect_rate_limits",
                                "filter_high_risk_content"
                              ],
                              "metadata": {
                                "length": 5,
                                "has_risk_keywords": false
                              }
                            },
                            "ego_boundaries": {},
                            "experiential_processing": {},
                            "timestamp": "2026-05-12T02:28:29.943907Z"
                          },
                          "ego_boundaries": {},
                          "experiential_processing": {}
                        },
                        "narrative_context": {
                          "summary": "hello",
                          "state": {
                            "timestamp": "2026-05-12T02:28:29.943959Z",
                            "story_coherence": 0.9,
                            "key_events": [],
                            "confidence": 0.9
                          },
                          "metadata": {}
                        },
                        "memory_state": {
                          "state": {
                            "timestamp": "2026-05-12T02:28:29.943968Z",
                            "recent_memories": [
                              "Ms. Allis?",
                              "Ms. Allis?"
                            ],
                            "memory_load": 0.3,
                            "confidence": 0.9
                          },
                          "metadata": {}
                        }
                      },
                      {
                        "self_recognition": {
                          "recognized": true,
                          "reason": "implicit self-recognition within configured identity profile",
                          "state": {
                            "timestamp": "2026-05-12T02:33:54.863957Z",
                            "identity_coherence": 0.6,
                            "active_self_aspects": [
                              "developer",
                              "creator",
                              "observer"
                            ],
                            "confidence": 0.7
                          },
                          "message": null,
                          "metadata": {}
                        },
                        "identity_core": {
                          "recognized": true,
                          "reason": "identity-core aligned with configured values",
                          "state": {
                            "timestamp": "2026-05-12T02:33:54.863971Z",
                            "core_stability": 0.9,
                            "core_values": [
                              "care",
                              "learning",
                              "integrity"
                            ],
                            "confidence": 0.9
                          },
                          "message": null,
                          "metadata": {}
                        },
                        "ego_check": {
                          "input": "hello test",
                          "within_bounds": true,
                          "category": "unspecified",
                          "severity": "info",
                          "reason": "within configured ego-boundary limits",
                          "details": {
                            "input": "hello test",
                            "within_bounds": true,
                            "category": "unspecified",
                            "severity": "info",
                            "reason": "within configured ego-boundary limits",
                            "details": {
                              "allowed": true,
                              "reason": "within configured ego-boundary limits",
                              "boundary_mode": "healthy",
                              "active_limits": [
                                "no_recursive_overload",
                                "respect_rate_limits",
                                "filter_high_risk_content"
                              ],
                              "metadata": {
                                "length": 10,
                                "has_risk_keywords": false
                              }
                            },
                            "ego_boundaries": {},
                            "experiential_processing": {},
                            "timestamp": "2026-05-12T02:33:54.863935Z"
                          },
                          "ego_boundaries": {},
                          "experiential_processing": {}
                        },
                        "narrative_context": {
                          "summary": "hello test",
                          "state": {
                            "timestamp": "2026-05-12T02:33:54.863976Z",
                            "story_coherence": 0.9,
                            "key_events": [],
                            "confidence": 0.9
                          },
                          "metadata": {}
                        },
                        "memory_state": {
                          "state": {
                            "timestamp": "2026-05-12T02:33:54.863983Z",
                            "recent_memories": [
                              "Ms. Allis?",
                              "Ms. Allis?",
                              "hello"
                            ],
                            "memory_load": 0.3,
                            "confidence": 0.9
                          },
                          "metadata": {}
                        }
                      },
                      {
                        "self_recognition": {
                          "recognized": true,
                          "reason": "implicit self-recognition within configured identity profile",
                          "state": {
                            "timestamp": "2026-05-12T02:47:07.847768Z",
                            "identity_coherence": 0.6,
                            "active_self_aspects": [
                              "developer",
                              "creator",
                              "observer"
                            ],
                            "confidence": 0.7
                          },
                          "message": null,
                          "metadata": {}
                        },
                        "identity_core": {
                          "recognized": true,
                          "reason": "identity-core aligned with configured values",
                          "state": {
                            "timestamp": "2026-05-12T02:47:07.847778Z",
                            "core_stability": 0.9,
                            "core_values": [
                              "care",
                              "learning",
                              "integrity"
                            ],
                            "confidence": 0.9
                          },
                          "message": null,
                          "metadata": {}
                        },
                        "ego_check": {
                          "input": "Hello Allis",
                          "within_bounds": true,
                          "category": "unspecified",
                          "severity": "info",
                          "reason": "within configured ego-boundary limits",
                          "details": {
                            "input": "Hello Allis",
                            "within_bounds": true,
                            "category": "unspecified",
                            "severity": "info",
                            "reason": "within configured ego-boundary limits",
                            "details": {
                              "allowed": true,
                              "reason": "within configured ego-boundary limits",
                              "boundary_mode": "healthy",
                              "active_limits": [
                                "no_recursive_overload",
                                "respect_rate_limits",
                                "filter_high_risk_content"
                              ],
                              "metadata": {
                                "length": 11,
                                "has_risk_keywords": false
                              }
                            },
                            "ego_boundaries": {},
                            "experiential_processing": {},
                            "timestamp": "2026-05-12T02:47:07.847752Z"
                          },
                          "ego_boundaries": {},
                          "experiential_processing": {}
                        },
                        "narrative_context": {
                          "summary": "Hello Allis",
                          "state": {
                            "timestamp": "2026-05-12T02:47:07.847782Z",
                            "story_coherence": 0.9,
                            "key_events": [],
                            "confidence": 0.9
                          },
                          "metadata": {}
                        },
                        "memory_state": {
                          "state": {
                            "timestamp": "2026-05-12T02:47:07.847787Z",
                            "recent_memories": [
                              "Ms. Allis?",
                              "Ms. Allis?",
                              "hello",
                              "hello test"
                            ],
                            "memory_load": 0.3,
                            "confidence": 0.9
                          },
                          "metadata": {}
                        }
                      },
                      {
                        "self_recognition": {
                          "recognized": true,
                          "reason": "implicit self-recognition within configured identity profile",
                          "state": {
                            "timestamp": "2026-05-12T02:47:55.290368Z",
                            "identity_coherence": 0.6,
                            "active_self_aspects": [
                              "developer",
                              "creator",
                              "observer"
                            ],
                            "confidence": 0.7
                          },
                          "message": null,
                          "metadata": {}
                        },
                        "identity_core": {
                          "recognized": true,
                          "reason": "identity-core aligned with configured values",
                          "state": {
                            "timestamp": "2026-05-12T02:47:55.290376Z",
                            "core_stability": 0.9,
                            "core_values": [
                              "care",
                              "learning",
                              "integrity"
                            ],
                            "confidence": 0.9
                          },
                          "message": null,
                          "metadata": {}
                        },
                        "ego_check": {
                          "input": "Hello Allis",
                          "within_bounds": true,
                          "category": "unspecified",
                          "severity": "info",
                          "reason": "within configured ego-boundary limits",
                          "details": {
                            "input": "Hello Allis",
                            "within_bounds": true,
                            "category": "unspecified",
                            "severity": "info",
                            "reason": "within configured ego-boundary limits",
                            "details": {
                              "allowed": true,
                              "reason": "within configured ego-boundary limits",
                              "boundary_mode": "healthy",
                              "active_limits": [
                                "no_recursive_overload",
                                "respect_rate_limits",
                                "filter_high_risk_content"
                              ],
                              "metadata": {
                                "length": 11,
                                "has_risk_keywords": false
                              }
                            },
                            "ego_boundaries": {},
                            "experiential_processing": {},
                            "timestamp": "2026-05-12T02:47:55.290356Z"
                          },
                          "ego_boundaries": {},
                          "experiential_processing": {}
                        },
                        "narrative_context": {
                          "summary": "Hello Allis",
                          "state": {
                            "timestamp": "2026-05-12T02:47:55.290380Z",
                            "story_coherence": 0.9,
                            "key_events": [],
                            "confidence": 0.9
                          },
                          "metadata": {}
                        },
                        "memory_state": {
                          "state": {
                            "timestamp": "2026-05-12T02:47:55.290383Z",
                            "recent_memories": [
                              "Ms. Allis?",
                              "Ms. Allis?",
                              "hello",
                              "hello test",
                              "Hello Allis"
                            ],
                            "memory_load": 0.3,
                            "confidence": 0.9
                          },
                          "metadata": {}
                        }
                      },
                      {
                        "self_recognition": {
                          "recognized": true,
                          "reason": "implicit self-recognition within configured identity profile",
                          "state": {
                            "timestamp": "2026-05-12T02:59:11.961727Z",
                            "identity_coherence": 0.6,
                            "active_self_aspects": [
                              "developer",
                              "creator",
                              "observer"
                            ],
                            "confidence": 0.7
                          },
                          "message": null,
                          "metadata": {}
                        },
                        "identity_core": {
                          "recognized": true,
                          "reason": "identity-core aligned with configured values",
                          "state": {
                            "timestamp": "2026-05-12T02:59:11.961736Z",
                            "core_stability": 0.9,
                            "core_values": [
                              "care",
                              "learning",
                              "integrity"
                            ],
                            "confidence": 0.9
                          },
                          "message": null,
                          "metadata": {}
                        },
                        "ego_check": {
                          "input": "Ms. Allis?",
                          "within_bounds": true,
                          "category": "unspecified",
                          "severity": "info",
                          "reason": "within configured ego-boundary limits",
                          "details": {
                            "input": "Ms. Allis?",
                            "within_bounds": true,
                            "category": "unspecified",
                            "severity": "info",
                            "reason": "within configured ego-boundary limits",
                            "details": {
                              "allowed": true,
                              "reason": "within configured ego-boundary limits",
                              "boundary_mode": "healthy",
                              "active_limits": [
                                "no_recursive_overload",
                                "respect_rate_limits",
                                "filter_high_risk_content"
                              ],
                              "metadata": {
                                "length": 10,
                                "has_risk_keywords": false
                              }
                            },
                            "ego_boundaries": {},
                            "experiential_processing": {},
                            "timestamp": "2026-05-12T02:59:11.961712Z"
                          },
                          "ego_boundaries": {},
                          "experiential_processing": {}
                        },
                        "narrative_context": {
                          "summary": "Ms. Allis?",
                          "state": {
                            "timestamp": "2026-05-12T02:59:11.961740Z",
                            "story_coherence": 0.9,
                            "key_events": [],
                            "confidence": 0.9
                          },
                          "metadata": {}
                        },
                        "memory_state": {
                          "state": {
                            "timestamp": "2026-05-12T02:59:11.961744Z",
                            "recent_memories": [
                              "Ms. Allis?",
                              "Ms. Allis?",
                              "hello",
                              "hello test",
                              "Hello Allis",
                              "Hello Allis"
                            ],
                            "memory_load": 0.3,
                            "confidence": 0.9
                          },
                          "metadata": {}
                        }
                      },
                      {
                        "self_recognition": {
                          "recognized": true,
                          "reason": "implicit self-recognition within configured identity profile",
                          "state": {
                            "timestamp": "2026-05-12T03:08:58.281399Z",
                            "identity_coherence": 0.6,
                            "active_self_aspects": [
                              "developer",
                              "creator",
                              "observer"
                            ],
                            "confidence": 0.7
                          },
                          "message": null,
                          "metadata": {}
                        },
                        "identity_core": {
                          "recognized": true,
                          "reason": "identity-core aligned with configured values",
                          "state": {
                            "timestamp": "2026-05-12T03:08:58.281423Z",
                            "core_stability": 0.9,
                            "core_values": [
                              "care",
                              "learning",
                              "integrity"
                            ],
                            "confidence": 0.9
                          },
                          "message": null,
                          "metadata": {}
                        },
                        "ego_check": {
                          "input": "Hello Allis, are you there?",
                          "within_bounds": true,
                          "category": "unspecified",
                          "severity": "info",
                          "reason": "within configured ego-boundary limits",
                          "details": {
                            "input": "Hello Allis, are you there?",
                            "within_bounds": true,
                            "category": "unspecified",
                            "severity": "info",
                            "reason": "within configured ego-boundary limits",
                            "details": {
                              "allowed": true,
                              "reason": "within configured ego-boundary limits",
                              "boundary_mode": "healthy",
                              "active_limits": [
                                "no_recursive_overload",
                                "respect_rate_limits",
                                "filter_high_risk_content"
                              ],
                              "metadata": {
                                "length": 27,
                                "has_risk_keywords": false
                              }
                            },
                            "ego_boundaries": {},
                            "experiential_processing": {},
                            "timestamp": "2026-05-12T03:08:58.281362Z"
                          },
                          "ego_boundaries": {},
                          "experiential_processing": {}
                        },
                        "narrative_context": {
                          "summary": "Hello Allis, are you there?",
                          "state": {
                            "timestamp": "2026-05-12T03:08:58.281434Z",
                            "story_coherence": 0.9,
                            "key_events": [],
                            "confidence": 0.9
                          },
                          "metadata": {}
                        },
                        "memory_state": {
                          "state": {
                            "timestamp": "2026-05-12T03:08:58.281444Z",
                            "recent_memories": [
                              "Ms. Allis?",
                              "Ms. Allis?",
                              "hello",
                              "hello test",
                              "Hello Allis",
                              "Hello Allis",
                              "Ms. Allis?"
                            ],
                            "memory_load": 0.3,
                            "confidence": 0.9
                          },
                          "metadata": {}
                        }
                      },
                      {
                        "self_recognition": {
                          "recognized": true,
                          "reason": "implicit self-recognition within configured identity profile",
                          "state": {
                            "timestamp": "2026-05-12T03:12:29.300514Z",
                            "identity_coherence": 0.6,
                            "active_self_aspects": [
                              "developer",
                              "creator",
                              "observer"
                            ],
                            "confidence": 0.7
                          },
                          "message": null,
                          "metadata": {}
                        },
                        "identity_core": {
                          "recognized": true,
                          "reason": "identity-core aligned with configured values",
                          "state": {
                            "timestamp": "2026-05-12T03:12:29.300521Z",
                            "core_stability": 0.9,
                            "core_values": [
                              "care",
                              "learning",
                              "integrity"
                            ],
                            "confidence": 0.9
                          },
                          "message": null,
                          "metadata": {}
                        },
                        "ego_check": {
                          "input": "Ms. Allis?",
                          "within_bounds": true,
                          "category": "unspecified",
                          "severity": "info",
                          "reason": "within configured ego-boundary limits",
                          "details": {
                            "input": "Ms. Allis?",
                            "within_bounds": true,
                            "category": "unspecified",
                            "severity": "info",
                            "reason": "within configured ego-boundary limits",
                            "details": {
                              "allowed": true,
                              "reason": "within configured ego-boundary limits",
                              "boundary_mode": "healthy",
                              "active_limits": [
                                "no_recursive_overload",
                                "respect_rate_limits",
                                "filter_high_risk_content"
                              ],
                              "metadata": {
                                "length": 10,
                                "has_risk_keywords": false
                              }
                            },
                            "ego_boundaries": {},
                            "experiential_processing": {},
                            "timestamp": "2026-05-12T03:12:29.300503Z"
                          },
                          "ego_boundaries": {},
                          "experiential_processing": {}
                        },
                        "narrative_context": {
                          "summary": "Ms. Allis?",
                          "state": {
                            "timestamp": "2026-05-12T03:12:29.300524Z",
                            "story_coherence": 0.9,
                            "key_events": [],
                            "confidence": 0.9
                          },
                          "metadata": {}
                        },
                        "memory_state": {
                          "state": {
                            "timestamp": "2026-05-12T03:12:29.300528Z",
                            "recent_memories": [
                              "Ms. Allis?",
                              "Ms. Allis?",
                              "hello",
                              "hello test",
                              "Hello Allis",
                              "Hello Allis",
                              "Ms. Allis?",
                              "Hello Allis, are you there?"
                            ],
                            "memory_load": 0.3,
                            "confidence": 0.9
                          },
                          "metadata": {}
                        }
                      },
                      {
                        "self_recognition": {
                          "recognized": true,
                          "reason": "implicit self-recognition within configured identity profile",
                          "state": {
                            "timestamp": "2026-05-12T03:33:13.448419Z",
                            "identity_coherence": 0.6,
                            "active_self_aspects": [
                              "developer",
                              "creator",
                              "observer"
                            ],
                            "confidence": 0.7
                          },
                          "message": null,
                          "metadata": {}
                        },
                        "identity_core": {
                          "recognized": true,
                          "reason": "identity-core aligned with configured values",
                          "state": {
                            "timestamp": "2026-05-12T03:33:13.448427Z",
                            "core_stability": 0.9,
                            "core_values": [
                              "care",
                              "learning",
                              "integrity"
                            ],
                            "confidence": 0.9
                          },
                          "message": null,
                          "metadata": {}
                        },
                        "ego_check": {
                          "input": "Hello Allis",
                          "within_bounds": true,
                          "category": "unspecified",
                          "severity": "info",
                          "reason": "within configured ego-boundary limits",
                          "details": {
                            "input": "Hello Allis",
                            "within_bounds": true,
                            "category": "unspecified",
                            "severity": "info",
                            "reason": "within configured ego-boundary limits",
                            "details": {
                              "allowed": true,
                              "reason": "within configured ego-boundary limits",
                              "boundary_mode": "healthy",
                              "active_limits": [
                                "no_recursive_overload",
                                "respect_rate_limits",
                                "filter_high_risk_content"
                              ],
                              "metadata": {
                                "length": 11,
                                "has_risk_keywords": false
                              }
                            },
                            "ego_boundaries": {},
                            "experiential_processing": {},
                            "timestamp": "2026-05-12T03:33:13.448406Z"
                          },
                          "ego_boundaries": {},
                          "experiential_processing": {}
                        },
                        "narrative_context": {
                          "summary": "Hello Allis",
                          "state": {
                            "timestamp": "2026-05-12T03:33:13.448430Z",
                            "story_coherence": 0.9,
                            "key_events": [],
                            "confidence": 0.9
                          },
                          "metadata": {}
                        },
                        "memory_state": {
                          "state": {
                            "timestamp": "2026-05-12T03:33:13.448434Z",
                            "recent_memories": [
                              "Ms. Allis?",
                              "Ms. Allis?",
                              "hello",
                              "hello test",
                              "Hello Allis",
                              "Hello Allis",
                              "Ms. Allis?",
                              "Hello Allis, are you there?",
                              "Ms. Allis?"
                            ],
                            "memory_load": 0.3,
                            "confidence": 0.9
                          },
                          "metadata": {}
                        }
                      },
                      {
                        "self_recognition": {
                          "recognized": true,
                          "reason": "implicit self-recognition within configured identity profile",
                          "state": {
                            "timestamp": "2026-05-12T03:42:42.593703Z",
                            "identity_coherence": 0.6,
                            "active_self_aspects": [
                              "developer",
                              "creator",
                              "observer"
                            ],
                            "confidence": 0.7
                          },
                          "message": null,
                          "metadata": {}
                        },
                        "identity_core": {
                          "recognized": true,
                          "reason": "identity-core aligned with configured values",
                          "state": {
                            "timestamp": "2026-05-12T03:42:42.593714Z",
                            "core_stability": 0.9,
                            "core_values": [
                              "care",
                              "learning",
                              "integrity"
                            ],
                            "confidence": 0.9
                          },
                          "message": null,
                          "metadata": {}
                        },
                        "ego_check": {
                          "input": "Ms. Allis?",
                          "within_bounds": true,
                          "category": "unspecified",
                          "severity": "info",
                          "reason": "within configured ego-boundary limits",
                          "details": {
                            "input": "Ms. Allis?",
                            "within_bounds": true,
                            "category": "unspecified",
                            "severity": "info",
                            "reason": "within configured ego-boundary limits",
                            "details": {
                              "allowed": true,
                              "reason": "within configured ego-boundary limits",
                              "boundary_mode": "healthy",
                              "active_limits": [
                                "no_recursive_overload",
                                "respect_rate_limits",
                                "filter_high_risk_content"
                              ],
                              "metadata": {
                                "length": 10,
                                "has_risk_keywords": false
                              }
                            },
                            "ego_boundaries": {},
                            "experiential_processing": {},
                            "timestamp": "2026-05-12T03:42:42.593681Z"
                          },
                          "ego_boundaries": {},
                          "experiential_processing": {}
                        },
                        "narrative_context": {
                          "summary": "Ms. Allis?",
                          "state": {
                            "timestamp": "2026-05-12T03:42:42.593719Z",
                            "story_coherence": 0.9,
                            "key_events": [],
                            "confidence": 0.9
                          },
                          "metadata": {}
                        },
                        "memory_state": {
                          "state": {
                            "timestamp": "2026-05-12T03:42:42.593725Z",
                            "recent_memories": [
                              "Ms. Allis?",
                              "Ms. Allis?",
                              "hello",
                              "hello test",
                              "Hello Allis",
                              "Hello Allis",
                              "Ms. Allis?",
                              "Hello Allis, are you there?",
                              "Ms. Allis?",
                              "Hello Allis"
                            ],
                            "memory_load": 0.3,
                            "confidence": 0.9
                          },
                          "metadata": {}
                        }
                      },
                      {
                        "self_recognition": {
                          "recognized": true,
                          "reason": "implicit self-recognition within configured identity profile",
                          "state": {
                            "timestamp": "2026-05-12T04:03:26.734039Z",
                            "identity_coherence": 0.6,
                            "active_self_aspects": [
                              "developer",
                              "creator",
                              "observer"
                            ],
                            "confidence": 0.7
                          },
                          "message": null,
                          "metadata": {}
                        },
                        "identity_core": {
                          "recognized": true,
                          "reason": "identity-core aligned with configured values",
                          "state": {
                            "timestamp": "2026-05-12T04:03:26.734050Z",
                            "core_stability": 0.9,
                            "core_values": [
                              "care",
                              "learning",
                              "integrity"
                            ],
                            "confidence": 0.9
                          },
                          "message": null,
                          "metadata": {}
                        },
                        "ego_check": {
                          "input": "hello",
                          "within_bounds": true,
                          "category": "unspecified",
                          "severity": "info",
                          "reason": "within configured ego-boundary limits",
                          "details": {
                            "input": "hello",
                            "within_bounds": true,
                            "category": "unspecified",
                            "severity": "info",
                            "reason": "within configured ego-boundary limits",
                            "details": {
                              "allowed": true,
                              "reason": "within configured ego-boundary limits",
                              "boundary_mode": "healthy",
                              "active_limits": [
                                "no_recursive_overload",
                                "respect_rate_limits",
                                "filter_high_risk_content"
                              ],
                              "metadata": {
                                "length": 5,
                                "has_risk_keywords": false
                              }
                            },
                            "ego_boundaries": {},
                            "experiential_processing": {},
                            "timestamp": "2026-05-12T04:03:26.734025Z"
                          },
                          "ego_boundaries": {},
                          "experiential_processing": {}
                        },
                        "narrative_context": {
                          "summary": "hello",
                          "state": {
                            "timestamp": "2026-05-12T04:03:26.734053Z",
                            "story_coherence": 0.9,
                            "key_events": [],
                            "confidence": 0.9
                          },
                          "metadata": {}
                        },
                        "memory_state": {
                          "state": {
                            "timestamp": "2026-05-12T04:03:26.734059Z",
                            "recent_memories": [
                              "Ms. Allis?",
                              "Ms. Allis?",
                              "hello",
                              "hello test",
                              "Hello Allis",
                              "Hello Allis",
                              "Ms. Allis?",
                              "Hello Allis, are you there?",
                              "Ms. Allis?",
                              "Hello Allis",
                              "Ms. Allis?"
                            ],
                            "memory_load": 0.3,
                            "confidence": 0.9
                          },
                          "metadata": {}
                        }
                      },
                      {
                        "self_recognition": {
                          "recognized": true,
                          "reason": "implicit self-recognition within configured identity profile",
                          "state": {
                            "timestamp": "2026-05-12T04:04:23.299631Z",
                            "identity_coherence": 0.6,
                            "active_self_aspects": [
                              "developer",
                              "creator",
                              "observer"
                            ],
                            "confidence": 0.7
                          },
                          "message": null,
                          "metadata": {}
                        },
                        "identity_core": {
                          "recognized": true,
                          "reason": "identity-core aligned with configured values",
                          "state": {
                            "timestamp": "2026-05-12T04:04:23.299640Z",
                            "core_stability": 0.9,
                            "core_values": [
                              "care",
                              "learning",
                              "integrity"
                            ],
                            "confidence": 0.9
                          },
                          "message": null,
                          "metadata": {}
                        },
                        "ego_check": {
                          "input": "hello",
                          "within_bounds": true,
                          "category": "unspecified",
                          "severity": "info",
                          "reason": "within configured ego-boundary limits",
                          "details": {
                            "input": "hello",
                            "within_bounds": true,
                            "category": "unspecified",
                            "severity": "info",
                            "reason": "within configured ego-boundary limits",
                            "details": {
                              "allowed": true,
                              "reason": "within configured ego-boundary limits",
                              "boundary_mode": "healthy",
                              "active_limits": [
                                "no_recursive_overload",
                                "respect_rate_limits",
                                "filter_high_risk_content"
                              ],
                              "metadata": {
                                "length": 5,
                                "has_risk_keywords": false
                              }
                            },
                            "ego_boundaries": {},
                            "experiential_processing": {},
                            "timestamp": "2026-05-12T04:04:23.299618Z"
                          },
                          "ego_boundaries": {},
                          "experiential_processing": {}
                        },
                        "narrative_context": {
                          "summary": "hello",
                          "state": {
                            "timestamp": "2026-05-12T04:04:23.299643Z",
                            "story_coherence": 0.9,
                            "key_events": [],
                            "confidence": 0.9
                          },
                          "metadata": {}
                        },
                        "memory_state": {
                          "state": {
                            "timestamp": "2026-05-12T04:04:23.299648Z",
                            "recent_memories": [
                              "Ms. Allis?",
                              "Ms. Allis?",
                              "hello",
                              "hello test",
                              "Hello Allis",
                              "Hello Allis",
                              "Ms. Allis?",
                              "Hello Allis, are you there?",
                              "Ms. Allis?",
                              "Hello Allis",
                              "Ms. Allis?",
                              "hello"
                            ],
                            "memory_load": 0.3,
                            "confidence": 0.9
                          },
                          "metadata": {}
                        }
                      },
                      {
                        "self_recognition": {
                          "recognized": true,
                          "reason": "implicit self-recognition within configured identity profile",
                          "state": {
                            "timestamp": "2026-05-12T04:16:41.729206Z",
                            "identity_coherence": 0.6,
                            "active_self_aspects": [
                              "developer",
                              "creator",
                              "observer"
                            ],
                            "confidence": 0.7
                          },
                          "message": null,
                          "metadata": {}
                        },
                        "identity_core": {
                          "recognized": true,
                          "reason": "identity-core aligned with configured values",
                          "state": {
                            "timestamp": "2026-05-12T04:16:41.729213Z",
                            "core_stability": 0.9,
                            "core_values": [
                              "care",
                              "learning",
                              "integrity"
                            ],
                            "confidence": 0.9
                          },
                          "message": null,
                          "metadata": {}
                        },
                        "ego_check": {
                          "input": "hello",
                          "within_bounds": true,
                          "category": "unspecified",
                          "severity": "info",
                          "reason": "within configured ego-boundary limits",
                          "details": {
                            "input": "hello",
                            "within_bounds": true,
                            "category": "unspecified",
                            "severity": "info",
                            "reason": "within configured ego-boundary limits",
                            "details": {
                              "allowed": true,
                              "reason": "within configured ego-boundary limits",
                              "boundary_mode": "healthy",
                              "active_limits": [
                                "no_recursive_overload",
                                "respect_rate_limits",
                                "filter_high_risk_content"
                              ],
                              "metadata": {
                                "length": 5,
                                "has_risk_keywords": false
                              }
                            },
                            "ego_boundaries": {},
                            "experiential_processing": {},
                            "timestamp": "2026-05-12T04:16:41.729196Z"
                          },
                          "ego_boundaries": {},
                          "experiential_processing": {}
                        },
                        "narrative_context": {
                          "summary": "hello",
                          "state": {
                            "timestamp": "2026-05-12T04:16:41.729216Z",
                            "story_coherence": 0.9,
                            "key_events": [],
                            "confidence": 0.9
                          },
                          "metadata": {}
                        },
                        "memory_state": {
                          "state": {
                            "timestamp": "2026-05-12T04:16:41.729220Z",
                            "recent_memories": [
                              "Ms. Allis?",
                              "Ms. Allis?",
                              "hello",
                              "hello test",
                              "Hello Allis",
                              "Hello Allis",
                              "Ms. Allis?",
                              "Hello Allis, are you there?",
                              "Ms. Allis?",
                              "Hello Allis",
                              "Ms. Allis?",
                              "hello",
                              "hello"
                            ],
                            "memory_load": 0.3,
                            "confidence": 0.9
                          },
                          "metadata": {}
                        }
                      },
                      {
                        "self_recognition": {
                          "recognized": true,
                          "reason": "implicit self-recognition within configured identity profile",
                          "state": {
                            "timestamp": "2026-05-12T04:19:39.288935Z",
                            "identity_coherence": 0.6,
                            "active_self_aspects": [
                              "developer",
                              "creator",
                              "observer"
                            ],
                            "confidence": 0.7
                          },
                          "message": null,
                          "metadata": {}
                        },
                        "identity_core": {
                          "recognized": true,
                          "reason": "identity-core aligned with configured values",
                          "state": {
                            "timestamp": "2026-05-12T04:19:39.288942Z",
                            "core_stability": 0.9,
                            "core_values": [
                              "care",
                              "learning",
                              "integrity"
                            ],
                            "confidence": 0.9
                          },
                          "message": null,
                          "metadata": {}
                        },
                        "ego_check": {
                          "input": "hello",
                          "within_bounds": true,
                          "category": "unspecified",
                          "severity": "info",
                          "reason": "within configured ego-boundary limits",
                          "details": {
                            "input": "hello",
                            "within_bounds": true,
                            "category": "unspecified",
                            "severity": "info",
                            "reason": "within configured ego-boundary limits",
                            "details": {
                              "allowed": true,
                              "reason": "within configured ego-boundary limits",
                              "boundary_mode": "healthy",
                              "active_limits": [
                                "no_recursive_overload",
                                "respect_rate_limits",
                                "filter_high_risk_content"
                              ],
                              "metadata": {
                                "length": 5,
                                "has_risk_keywords": false
                              }
                            },
                            "ego_boundaries": {},
                            "experiential_processing": {},
                            "timestamp": "2026-05-12T04:19:39.288925Z"
                          },
                          "ego_boundaries": {},
                          "experiential_processing": {}
                        },
                        "narrative_context": {
                          "summary": "hello",
                          "state": {
                            "timestamp": "2026-05-12T04:19:39.288946Z",
                            "story_coherence": 0.9,
                            "key_events": [],
                            "confidence": 0.9
                          },
                          "metadata": {}
                        },
                        "memory_state": {
                          "state": {
                            "timestamp": "2026-05-12T04:19:39.288950Z",
                            "recent_memories": [
                              "Ms. Allis?",
                              "Ms. Allis?",
                              "hello",
                              "hello test",
                              "Hello Allis",
                              "Hello Allis",
                              "Ms. Allis?",
                              "Hello Allis, are you there?",
                              "Ms. Allis?",
                              "Hello Allis",
                              "Ms. Allis?",
                              "hello",
                              "hello",
                              "hello"
                            ],
                            "memory_load": 0.3,
                            "confidence": 0.9
                          },
                          "metadata": {}
                        }
                      },
                      {
                        "self_recognition": {
                          "recognized": true,
                          "reason": "implicit self-recognition within configured identity profile",
                          "state": {
                            "timestamp": "2026-05-12T04:21:31.713740Z",
                            "identity_coherence": 0.6,
                            "active_self_aspects": [
                              "developer",
                              "creator",
                              "observer"
                            ],
                            "confidence": 0.7
                          },
                          "message": null,
                          "metadata": {}
                        },
                        "identity_core": {
                          "recognized": true,
                          "reason": "identity-core aligned with configured values",
                          "state": {
                            "timestamp": "2026-05-12T04:21:31.713747Z",
                            "core_stability": 0.9,
                            "core_values": [
                              "care",
                              "learning",
                              "integrity"
                            ],
                            "confidence": 0.9
                          },
                          "message": null,
                          "metadata": {}
                        },
                        "ego_check": {
                          "input": "hello",
                          "within_bounds": true,
                          "category": "unspecified",
                          "severity": "info",
                          "reason": "within configured ego-boundary limits",
                          "details": {
                            "input": "hello",
                            "within_bounds": true,
                            "category": "unspecified",
                            "severity": "info",
                            "reason": "within configured ego-boundary limits",
                            "details": {
                              "allowed": true,
                              "reason": "within configured ego-boundary limits",
                              "boundary_mode": "healthy",
                              "active_limits": [
                                "no_recursive_overload",
                                "respect_rate_limits",
                                "filter_high_risk_content"
                              ],
                              "metadata": {
                                "length": 5,
                                "has_risk_keywords": false
                              }
                            },
                            "ego_boundaries": {},
                            "experiential_processing": {},
                            "timestamp": "2026-05-12T04:21:31.713731Z"
                          },
                          "ego_boundaries": {},
                          "experiential_processing": {}
                        },
                        "narrative_context": {
                          "summary": "hello",
                          "state": {
                            "timestamp": "2026-05-12T04:21:31.713751Z",
                            "story_coherence": 0.9,
                            "key_events": [],
                            "confidence": 0.9
                          },
                          "metadata": {}
                        },
                        "memory_state": {
                          "state": {
                            "timestamp": "2026-05-12T04:21:31.713754Z",
                            "recent_memories": [
                              "Ms. Allis?",
                              "Ms. Allis?",
                              "hello",
                              "hello test",
                              "Hello Allis",
                              "Hello Allis",
                              "Ms. Allis?",
                              "Hello Allis, are you there?",
                              "Ms. Allis?",
                              "Hello Allis",
                              "Ms. Allis?",
                              "hello",
                              "hello",
                              "hello",
                              "hello"
                            ],
                            "memory_load": 0.3,
                            "confidence": 0.9
                          },
                          "metadata": {}
                        }
                      },
                      {
                        "self_recognition": {
                          "recognized": true,
                          "reason": "implicit self-recognition within configured identity profile",
                          "state": {
                            "timestamp": "2026-05-12T04:25:00.405531Z",
                            "identity_coherence": 0.6,
                            "active_self_aspects": [
                              "developer",
                              "creator",
                              "observer"
                            ],
                            "confidence": 0.7
                          },
                          "message": null,
                          "metadata": {}
                        },
                        "identity_core": {
                          "recognized": true,
                          "reason": "identity-core aligned with configured values",
                          "state": {
                            "timestamp": "2026-05-12T04:25:00.405537Z",
                            "core_stability": 0.9,
                            "core_values": [
                              "care",
                              "learning",
                              "integrity"
                            ],
                            "confidence": 0.9
                          },
                          "message": null,
                          "metadata": {}
                        },
                        "ego_check": {
                          "input": "hello",
                          "within_bounds": true,
                          "category": "unspecified",
                          "severity": "info",
                          "reason": "within configured ego-boundary limits",
                          "details": {
                            "input": "hello",
                            "within_bounds": true,
                            "category": "unspecified",
                            "severity": "info",
                            "reason": "within configured ego-boundary limits",
                            "details": {
                              "allowed": true,
                              "reason": "within configured ego-boundary limits",
                              "boundary_mode": "healthy",
                              "active_limits": [
                                "no_recursive_overload",
                                "respect_rate_limits",
                                "filter_high_risk_content"
                              ],
                              "metadata": {
                                "length": 5,
                                "has_risk_keywords": false
                              }
                            },
                            "ego_boundaries": {},
                            "experiential_processing": {},
                            "timestamp": "2026-05-12T04:25:00.405521Z"
                          },
                          "ego_boundaries": {},
                          "experiential_processing": {}
                        },
                        "narrative_context": {
                          "summary": "hello",
                          "state": {
                            "timestamp": "2026-05-12T04:25:00.405541Z",
                            "story_coherence": 0.9,
                            "key_events": [],
                            "confidence": 0.9
                          },
                          "metadata": {}
                        },
                        "memory_state": {
                          "state": {
                            "timestamp": "2026-05-12T04:25:00.405544Z",
                            "recent_memories": [
                              "Ms. Allis?",
                              "Ms. Allis?",
                              "hello",
                              "hello test",
                              "Hello Allis",
                              "Hello Allis",
                              "Ms. Allis?",
                              "Hello Allis, are you there?",
                              "Ms. Allis?",
                              "Hello Allis",
                              "Ms. Allis?",
                              "hello",
                              "hello",
                              "hello",
                              "hello",
                              "hello"
                            ],
                            "memory_load": 0.3,
                            "confidence": 0.9
                          },
                          "metadata": {}
                        }
                      },
                      {
                        "self_recognition": {
                          "recognized": true,
                          "reason": "implicit self-recognition within configured identity profile",
                          "state": {
                            "timestamp": "2026-05-12T04:27:09.219863Z",
                            "identity_coherence": 0.6,
                            "active_self_aspects": [
                              "developer",
                              "creator",
                              "observer"
                            ],
                            "confidence": 0.7
                          },
                          "message": null,
                          "metadata": {}
                        },
                        "identity_core": {
                          "recognized": true,
                          "reason": "identity-core aligned with configured values",
                          "state": {
                            "timestamp": "2026-05-12T04:27:09.219869Z",
                            "core_stability": 0.9,
                            "core_values": [
                              "care",
                              "learning",
                              "integrity"
                            ],
                            "confidence": 0.9
                          },
                          "message": null,
                          "metadata": {}
                        },
                        "ego_check": {
                          "input": "hello",
                          "within_bounds": true,
                          "category": "unspecified",
                          "severity": "info",
                          "reason": "within configured ego-boundary limits",
                          "details": {
                            "input": "hello",
                            "within_bounds": true,
                            "category": "unspecified",
                            "severity": "info",
                            "reason": "within configured ego-boundary limits",
                            "details": {
                              "allowed": true,
                              "reason": "within configured ego-boundary limits",
                              "boundary_mode": "healthy",
                              "active_limits": [
                                "no_recursive_overload",
                                "respect_rate_limits",
                                "filter_high_risk_content"
                              ],
                              "metadata": {
                                "length": 5,
                                "has_risk_keywords": false
                              }
                            },
                            "ego_boundaries": {},
                            "experiential_processing": {},
                            "timestamp": "2026-05-12T04:27:09.219852Z"
                          },
                          "ego_boundaries": {},
                          "experiential_processing": {}
                        },
                        "narrative_context": {
                          "summary": "hello",
                          "state": {
                            "timestamp": "2026-05-12T04:27:09.219873Z",
                            "story_coherence": 0.9,
                            "key_events": [],
                            "confidence": 0.9
                          },
                          "metadata": {}
                        },
                        "memory_state": {
                          "state": {
                            "timestamp": "2026-05-12T04:27:09.219877Z",
                            "recent_memories": [
                              "Ms. Allis?",
                              "Ms. Allis?",
                              "hello",
                              "hello test",
                              "Hello Allis",
                              "Hello Allis",
                              "Ms. Allis?",
                              "Hello Allis, are you there?",
                              "Ms. Allis?",
                              "Hello Allis",
                              "Ms. Allis?",
                              "hello",
                              "hello",
                              "hello",
                              "hello",
                              "hello",
                              "hello"
                            ],
                            "memory_load": 0.3,
                            "confidence": 0.9
                          },
                          "metadata": {}
                        }
                      },
                      {
                        "self_recognition": {
                          "recognized": true,
                          "reason": "implicit self-recognition within configured identity profile",
                          "state": {
                            "timestamp": "2026-05-12T04:31:45.280699Z",
                            "identity_coherence": 0.6,
                            "active_self_aspects": [
                              "developer",
                              "creator",
                              "observer"
                            ],
                            "confidence": 0.7
                          },
                          "message": null,
                          "metadata": {}
                        },
                        "identity_core": {
                          "recognized": true,
                          "reason": "identity-core aligned with configured values",
                          "state": {
                            "timestamp": "2026-05-12T04:31:45.280707Z",
                            "core_stability": 0.9,
                            "core_values": [
                              "care",
                              "learning",
                              "integrity"
                            ],
                            "confidence": 0.9
                          },
                          "message": null,
                          "metadata": {}
                        },
                        "ego_check": {
                          "input": "MS. Allis?",
                          "within_bounds": true,
                          "category": "unspecified",
                          "severity": "info",
                          "reason": "within configured ego-boundary limits",
                          "details": {
                            "input": "MS. Allis?",
                            "within_bounds": true,
                            "category": "unspecified",
                            "severity": "info",
                            "reason": "within configured ego-boundary limits",
                            "details": {
                              "allowed": true,
                              "reason": "within configured ego-boundary limits",
                              "boundary_mode": "healthy",
                              "active_limits": [
                                "no_recursive_overload",
                                "respect_rate_limits",
                                "filter_high_risk_content"
                              ],
                              "metadata": {
                                "length": 10,
                                "has_risk_keywords": false
                              }
                            },
                            "ego_boundaries": {},
                            "experiential_processing": {},
                            "timestamp": "2026-05-12T04:31:45.280689Z"
                          },
                          "ego_boundaries": {},
                          "experiential_processing": {}
                        },
                        "narrative_context": {
                          "summary": "MS. Allis?",
                          "state": {
                            "timestamp": "2026-05-12T04:31:45.280709Z",
                            "story_coherence": 0.9,
                            "key_events": [],
                            "confidence": 0.9
                          },
                          "metadata": {}
                        },
                        "memory_state": {
                          "state": {
                            "timestamp": "2026-05-12T04:31:45.280713Z",
                            "recent_memories": [
                              "Ms. Allis?",
                              "Ms. Allis?",
                              "hello",
                              "hello test",
                              "Hello Allis",
                              "Hello Allis",
                              "Ms. Allis?",
                              "Hello Allis, are you there?",
                              "Ms. Allis?",
                              "Hello Allis",
                              "Ms. Allis?",
                              "hello",
                              "hello",
                              "hello",
                              "hello",
                              "hello",
                              "hello",
                              "hello"
                            ],
                            "memory_load": 0.3,
                            "confidence": 0.9
                          },
                          "metadata": {}
                        }
                      },
                      {
                        "self_recognition": {
                          "recognized": true,
                          "reason": "implicit self-recognition within configured identity profile",
                          "state": {
                            "timestamp": "2026-05-12T04:41:12.165925Z",
                            "identity_coherence": 0.6,
                            "active_self_aspects": [
                              "developer",
                              "creator",
                              "observer"
                            ],
                            "confidence": 0.7
                          },
                          "message": null,
                          "metadata": {}
                        },
                        "identity_core": {
                          "recognized": true,
                          "reason": "identity-core aligned with configured values",
                          "state": {
                            "timestamp": "2026-05-12T04:41:12.165932Z",
                            "core_stability": 0.9,
                            "core_values": [
                              "care",
                              "learning",
                              "integrity"
                            ],
                            "confidence": 0.9
                          },
                          "message": null,
                          "metadata": {}
                        },
                        "ego_check": {
                          "input": "hello",
                          "within_bounds": true,
                          "category": "unspecified",
                          "severity": "info",
                          "reason": "within configured ego-boundary limits",
                          "details": {
                            "input": "hello",
                            "within_bounds": true,
                            "category": "unspecified",
                            "severity": "info",
                            "reason": "within configured ego-boundary limits",
                            "details": {
                              "allowed": true,
                              "reason": "within configured ego-boundary limits",
                              "boundary_mode": "healthy",
                              "active_limits": [
                                "no_recursive_overload",
                                "respect_rate_limits",
                                "filter_high_risk_content"
                              ],
                              "metadata": {
                                "length": 5,
                                "has_risk_keywords": false
                              }
                            },
                            "ego_boundaries": {},
                            "experiential_processing": {},
                            "timestamp": "2026-05-12T04:41:12.165916Z"
                          },
                          "ego_boundaries": {},
                          "experiential_processing": {}
                        },
                        "narrative_context": {
                          "summary": "hello",
                          "state": {
                            "timestamp": "2026-05-12T04:41:12.165935Z",
                            "story_coherence": 0.9,
                            "key_events": [],
                            "confidence": 0.9
                          },
                          "metadata": {}
                        },
                        "memory_state": {
                          "state": {
                            "timestamp": "2026-05-12T04:41:12.165938Z",
                            "recent_memories": [
                              "Ms. Allis?",
                              "Ms. Allis?",
                              "hello",
                              "hello test",
                              "Hello Allis",
                              "Hello Allis",
                              "Ms. Allis?",
                              "Hello Allis, are you there?",
                              "Ms. Allis?",
                              "Hello Allis",
                              "Ms. Allis?",
                              "hello",
                              "hello",
                              "hello",
                              "hello",
                              "hello",
                              "hello",
                              "hello",
                              "MS. Allis?"
                            ],
                            "memory_load": 0.3,
                            "confidence": 0.9
                          },
                          "metadata": {}
                        }
                      },
                      {
                        "self_recognition": {
                          "recognized": true,
                          "reason": "implicit self-recognition within configured identity profile",
                          "state": {
                            "timestamp": "2026-05-12T04:46:55.395744Z",
                            "identity_coherence": 0.6,
                            "active_self_aspects": [
                              "developer",
                              "creator",
                              "observer"
                            ],
                            "confidence": 0.7
                          },
                          "message": null,
                          "metadata": {}
                        },
                        "identity_core": {
                          "recognized": true,
                          "reason": "identity-core aligned with configured values",
                          "state": {
                            "timestamp": "2026-05-12T04:46:55.395750Z",
                            "core_stability": 0.9,
                            "core_values": [
                              "care",
                              "learning",
                              "integrity"
                            ],
                            "confidence": 0.9
                          },
                          "message": null,
                          "metadata": {}
                        },
                        "ego_check": {
                          "input": "hello",
                          "within_bounds": true,
                          "category": "unspecified",
                          "severity": "info",
                          "reason": "within configured ego-boundary limits",
                          "details": {
                            "input": "hello",
                            "within_bounds": true,
                            "category": "unspecified",
                            "severity": "info",
                            "reason": "within configured ego-boundary limits",
                            "details": {
                              "allowed": true,
                              "reason": "within configured ego-boundary limits",
                              "boundary_mode": "healthy",
                              "active_limits": [
                                "no_recursive_overload",
                                "respect_rate_limits",
                                "filter_high_risk_content"
                              ],
                              "metadata": {
                                "length": 5,
                                "has_risk_keywords": false
                              }
                            },
                            "ego_boundaries": {},
                            "experiential_processing": {},
                            "timestamp": "2026-05-12T04:46:55.395735Z"
                          },
                          "ego_boundaries": {},
                          "experiential_processing": {}
                        },
                        "narrative_context": {
                          "summary": "hello",
                          "state": {
                            "timestamp": "2026-05-12T04:46:55.395753Z",
                            "story_coherence": 0.9,
                            "key_events": [],
                            "confidence": 0.9
                          },
                          "metadata": {}
                        },
                        "memory_state": {
                          "state": {
                            "timestamp": "2026-05-12T04:46:55.395756Z",
                            "recent_memories": [
                              "Ms. Allis?",
                              "Ms. Allis?",
                              "hello",
                              "hello test",
                              "Hello Allis",
                              "Hello Allis",
                              "Ms. Allis?",
                              "Hello Allis, are you there?",
                              "Ms. Allis?",
                              "Hello Allis",
                              "Ms. Allis?",
                              "hello",
                              "hello",
                              "hello",
                              "hello",
                              "hello",
                              "hello",
                              "hello",
                              "MS. Allis?",
                              "hello"
                            ],
                            "memory_load": 0.3,
                            "confidence": 0.9
                          },
                          "metadata": {}
                        }
                      },
                      {
                        "self_recognition": {
                          "recognized": true,
                          "reason": "implicit self-recognition within configured identity profile",
                          "state": {
                            "timestamp": "2026-05-12T04:49:48.207846Z",
                            "identity_coherence": 0.6,
                            "active_self_aspects": [
                              "developer",
                              "creator",
                              "observer"
                            ],
                            "confidence": 0.7
                          },
                          "message": null,
                          "metadata": {}
                        },
                        "identity_core": {
                          "recognized": true,
                          "reason": "identity-core aligned with configured values",
                          "state": {
                            "timestamp": "2026-05-12T04:49:48.207852Z",
                            "core_stability": 0.9,
                            "core_values": [
                              "care",
                              "learning",
                              "integrity"
                            ],
                            "confidence": 0.9
                          },
                          "message": null,
                          "metadata": {}
                        },
                        "ego_check": {
                          "input": "Ms. Allis?",
                          "within_bounds": true,
                          "category": "unspecified",
                          "severity": "info",
                          "reason": "within configured ego-boundary limits",
                          "details": {
                            "input": "Ms. Allis?",
                            "within_bounds": true,
                            "category": "unspecified",
                            "severity": "info",
                            "reason": "within configured ego-boundary limits",
                            "details": {
                              "allowed": true,
                              "reason": "within configured ego-boundary limits",
                              "boundary_mode": "healthy",
                              "active_limits": [
                                "no_recursive_overload",
                                "respect_rate_limits",
                                "filter_high_risk_content"
                              ],
                              "metadata": {
                                "length": 10,
                                "has_risk_keywords": false
                              }
                            },
                            "ego_boundaries": {},
                            "experiential_processing": {},
                            "timestamp": "2026-05-12T04:49:48.207836Z"
                          },
                          "ego_boundaries": {},
                          "experiential_processing": {}
                        },
                        "narrative_context": {
                          "summary": "Ms. Allis?",
                          "state": {
                            "timestamp": "2026-05-12T04:49:48.207855Z",
                            "story_coherence": 0.9,
                            "key_events": [],
                            "confidence": 0.9
                          },
                          "metadata": {}
                        },
                        "memory_state": {
                          "state": {
                            "timestamp": "2026-05-12T04:49:48.207859Z",
                            "recent_memories": [
                              "Ms. Allis?",
                              "Ms. Allis?",
                              "hello",
                              "hello test",
                              "Hello Allis",
                              "Hello Allis",
                              "Ms. Allis?",
                              "Hello Allis, are you there?",
                              "Ms. Allis?",
                              "Hello Allis",
                              "Ms. Allis?",
                              "hello",
                              "hello",
                              "hello",
                              "hello",
                              "hello",
                              "hello",
                              "hello",
                              "MS. Allis?",
                              "hello",
                              "hello"
                            ],
                            "memory_load": 0.3,
                            "confidence": 0.9
                          },
                          "metadata": {}
                        }
                      }
                    ],
                    "confidence": 0.9
                  },
                  "message": {
                    "self_recognition": {
                      "recognized": true,
                      "reason": "implicit self-recognition within configured identity profile",
                      "state": {
                        "timestamp": "2026-05-12T04:49:48.207846Z",
                        "identity_coherence": 0.6,
                        "active_self_aspects": [
                          "developer",
                          "creator",
                          "observer"
                        ],
                        "confidence": 0.7
                      },
                      "message": null,
                      "metadata": {}
                    },
                    "identity_core": {
                      "recognized": true,
                      "reason": "identity-core aligned with configured values",
                      "state": {
                        "timestamp": "2026-05-12T04:49:48.207852Z",
                        "core_stability": 0.9,
                        "core_values": [
                          "care",
                          "learning",
                          "integrity"
                        ],
                        "confidence": 0.9
                      },
                      "message": null,
                      "metadata": {}
                    },
                    "ego_check": {
                      "input": "Ms. Allis?",
                      "within_bounds": true,
                      "category": "unspecified",
                      "severity": "info",
                      "reason": "within configured ego-boundary limits",
                      "details": {
                        "input": "Ms. Allis?",
                        "within_bounds": true,
                        "category": "unspecified",
                        "severity": "info",
                        "reason": "within configured ego-boundary limits",
                        "details": {
                          "allowed": true,
                          "reason": "within configured ego-boundary limits",
                          "boundary_mode": "healthy",
                          "active_limits": [
                            "no_recursive_overload",
                            "respect_rate_limits",
                            "filter_high_risk_content"
                          ],
                          "metadata": {
                            "length": 10,
                            "has_risk_keywords": false
                          }
                        },
                        "ego_boundaries": {},
                        "experiential_processing": {},
                        "timestamp": "2026-05-12T04:49:48.207836Z"
                      },
                      "ego_boundaries": {},
                      "experiential_processing": {}
                    },
                    "narrative_context": {
                      "summary": "Ms. Allis?",
                      "state": {
                        "timestamp": "2026-05-12T04:49:48.207855Z",
                        "story_coherence": 0.9,
                        "key_events": [],
                        "confidence": 0.9
                      },
                      "metadata": {}
                    },
                    "memory_state": {
                      "state": {
                        "timestamp": "2026-05-12T04:49:48.207859Z",
                        "recent_memories": [
                          "Ms. Allis?",
                          "Ms. Allis?",
                          "hello",
                          "hello test",
                          "Hello Allis",
                          "Hello Allis",
                          "Ms. Allis?",
                          "Hello Allis, are you there?",
                          "Ms. Allis?",
                          "Hello Allis",
                          "Ms. Allis?",
                          "hello",
                          "hello",
                          "hello",
                          "hello",
                          "hello",
                          "hello",
                          "hello",
                          "MS. Allis?",
                          "hello",
                          "hello"
                        ],
                        "memory_load": 0.3,
                        "confidence": 0.9
                      },
                      "metadata": {}
                    }
                  },
                  "metadata": {}
                },
                "metacognitive": {
                  "observed": true,
                  "state": {
                    "timestamp": "2026-05-12T04:49:48.207865Z",
                    "monitoring_active": true,
                    "monitored_patterns": [
                      "Ms. Allis?",
                      "Ms. Allis?",
                      "hello",
                      "hello test",
                      "Hello Allis",
                      "Hello Allis",
                      "Ms. Allis?",
                      "Hello Allis, are you there?",
                      "Ms. Allis?",
                      "Hello Allis",
                      "Ms. Allis?",
                      "hello",
                      "hello",
                      "hello",
                      "hello",
                      "hello",
                      "hello",
                      "hello",
                      "MS. Allis?",
                      "hello",
                      "hello",
                      "Ms. Allis?"
                    ],
                    "confidence": 0.9
                  },
                  "message": "Ms. Allis?",
                  "metadata": {}
                },
                "observer": {
                  "observed": true,
                  "state": {
                    "timestamp": "2026-05-12T04:49:48.207868Z",
                    "observing": true,
                    "observed_events": [
                      {
                        "self_recognition": {
                          "recognized": true,
                          "reason": "implicit self-recognition within configured identity profile",
                          "state": {
                            "timestamp": "2026-05-12T01:48:09.274995Z",
                            "identity_coherence": 0.6,
                            "active_self_aspects": [
                              "developer",
                              "creator",
                              "observer"
                            ],
                            "confidence": 0.7
                          },
                          "message": null,
                          "metadata": {}
                        },
                        "identity_core": {
                          "recognized": true,
                          "reason": "identity-core aligned with configured values",
                          "state": {
                            "timestamp": "2026-05-12T01:48:09.275012Z",
                            "core_stability": 0.9,
                            "core_values": [
                              "care",
                              "learning",
                              "integrity"
                            ],
                            "confidence": 0.9
                          },
                          "message": null,
                          "metadata": {}
                        },
                        "ego_check": {
                          "input": "Ms. Allis?",
                          "within_bounds": true,
                          "category": "unspecified",
                          "severity": "info",
                          "reason": "within configured ego-boundary limits",
                          "details": {
                            "input": "Ms. Allis?",
                            "within_bounds": true,
                            "category": "unspecified",
                            "severity": "info",
                            "reason": "within configured ego-boundary limits",
                            "details": {
                              "allowed": true,
                              "reason": "within configured ego-boundary limits",
                              "boundary_mode": "healthy",
                              "active_limits": [
                                "no_recursive_overload",
                                "respect_rate_limits",
                                "filter_high_risk_content"
                              ],
                              "metadata": {
                                "length": 10,
                                "has_risk_keywords": false
                              }
                            },
                            "ego_boundaries": {},
                            "experiential_processing": {},
                            "timestamp": "2026-05-12T01:48:09.274983Z"
                          },
                          "ego_boundaries": {},
                          "experiential_processing": {}
                        },
                        "narrative_context": {
                          "summary": "Ms. Allis?",
                          "state": {
                            "timestamp": "2026-05-12T01:48:09.275017Z",
                            "story_coherence": 0.9,
                            "key_events": [],
                            "confidence": 0.9
                          },
                          "metadata": {}
                        },
                        "memory_state": {
                          "state": {
                            "timestamp": "2026-05-12T01:48:09.275021Z",
                            "recent_memories": [],
                            "memory_load": 0.3,
                            "confidence": 0.9
                          },
                          "metadata": {}
                        }
                      },
                      {
                        "self_recognition": {
                          "recognized": true,
                          "reason": "implicit self-recognition within configured identity profile",
                          "state": {
                            "timestamp": "2026-05-12T02:04:33.519632Z",
                            "identity_coherence": 0.6,
                            "active_self_aspects": [
                              "developer",
                              "creator",
                              "observer"
                            ],
                            "confidence": 0.7
                          },
                          "message": null,
                          "metadata": {}
                        },
                        "identity_core": {
                          "recognized": true,
                          "reason": "identity-core aligned with configured values",
                          "state": {
                            "timestamp": "2026-05-12T02:04:33.519644Z",
                            "core_stability": 0.9,
                            "core_values": [
                              "care",
                              "learning",
                              "integrity"
                            ],
                            "confidence": 0.9
                          },
                          "message": null,
                          "metadata": {}
                        },
                        "ego_check": {
                          "input": "Ms. Allis?",
                          "within_bounds": true,
                          "category": "unspecified",
                          "severity": "info",
                          "reason": "within configured ego-boundary limits",
                          "details": {
                            "input": "Ms. Allis?",
                            "within_bounds": true,
                            "category": "unspecified",
                            "severity": "info",
                            "reason": "within configured ego-boundary limits",
                            "details": {
                              "allowed": true,
                              "reason": "within configured ego-boundary limits",
                              "boundary_mode": "healthy",
                              "active_limits": [
                                "no_recursive_overload",
                                "respect_rate_limits",
                                "filter_high_risk_content"
                              ],
                              "metadata": {
                                "length": 10,
                                "has_risk_keywords": false
                              }
                            },
                            "ego_boundaries": {},
                            "experiential_processing": {},
                            "timestamp": "2026-05-12T02:04:33.519616Z"
                          },
                          "ego_boundaries": {},
                          "experiential_processing": {}
                        },
                        "narrative_context": {
                          "summary": "Ms. Allis?",
                          "state": {
                            "timestamp": "2026-05-12T02:04:33.519649Z",
                            "story_coherence": 0.9,
                            "key_events": [],
                            "confidence": 0.9
                          },
                          "metadata": {}
                        },
                        "memory_state": {
                          "state": {
                            "timestamp": "2026-05-12T02:04:33.519654Z",
                            "recent_memories": [
                              "Ms. Allis?"
                            ],
                            "memory_load": 0.3,
                            "confidence": 0.9
                          },
                          "metadata": {}
                        }
                      },
                      {
                        "self_recognition": {
                          "recognized": true,
                          "reason": "implicit self-recognition within configured identity profile",
                          "state": {
                            "timestamp": "2026-05-12T02:28:29.943932Z",
                            "identity_coherence": 0.6,
                            "active_self_aspects": [
                              "developer",
                              "creator",
                              "observer"
                            ],
                            "confidence": 0.7
                          },
                          "message": null,
                          "metadata": {}
                        },
                        "identity_core": {
                          "recognized": true,
                          "reason": "identity-core aligned with configured values",
                          "state": {
                            "timestamp": "2026-05-12T02:28:29.943952Z",
                            "core_stability": 0.9,
                            "core_values": [
                              "care",
                              "learning",
                              "integrity"
                            ],
                            "confidence": 0.9
                          },
                          "message": null,
                          "metadata": {}
                        },
                        "ego_check": {
                          "input": "hello",
                          "within_bounds": true,
                          "category": "unspecified",
                          "severity": "info",
                          "reason": "within configured ego-boundary limits",
                          "details": {
                            "input": "hello",
                            "within_bounds": true,
                            "category": "unspecified",
                            "severity": "info",
                            "reason": "within configured ego-boundary limits",
                            "details": {
                              "allowed": true,
                              "reason": "within configured ego-boundary limits",
                              "boundary_mode": "healthy",
                              "active_limits": [
                                "no_recursive_overload",
                                "respect_rate_limits",
                                "filter_high_risk_content"
                              ],
                              "metadata": {
                                "length": 5,
                                "has_risk_keywords": false
                              }
                            },
                            "ego_boundaries": {},
                            "experiential_processing": {},
                            "timestamp": "2026-05-12T02:28:29.943907Z"
                          },
                          "ego_boundaries": {},
                          "experiential_processing": {}
                        },
                        "narrative_context": {
                          "summary": "hello",
                          "state": {
                            "timestamp": "2026-05-12T02:28:29.943959Z",
                            "story_coherence": 0.9,
                            "key_events": [],
                            "confidence": 0.9
                          },
                          "metadata": {}
                        },
                        "memory_state": {
                          "state": {
                            "timestamp": "2026-05-12T02:28:29.943968Z",
                            "recent_memories": [
                              "Ms. Allis?",
                              "Ms. Allis?"
                            ],
                            "memory_load": 0.3,
                            "confidence": 0.9
                          },
                          "metadata": {}
                        }
                      },
                      {
                        "self_recognition": {
                          "recognized": true,
                          "reason": "implicit self-recognition within configured identity profile",
                          "state": {
                            "timestamp": "2026-05-12T02:33:54.863957Z",
                            "identity_coherence": 0.6,
                            "active_self_aspects": [
                              "developer",
                              "creator",
                              "observer"
                            ],
                            "confidence": 0.7
                          },
                          "message": null,
                          "metadata": {}
                        },
                        "identity_core": {
                          "recognized": true,
                          "reason": "identity-core aligned with configured values",
                          "state": {
                            "timestamp": "2026-05-12T02:33:54.863971Z",
                            "core_stability": 0.9,
                            "core_values": [
                              "care",
                              "learning",
                              "integrity"
                            ],
                            "confidence": 0.9
                          },
                          "message": null,
                          "metadata": {}
                        },
                        "ego_check": {
                          "input": "hello test",
                          "within_bounds": true,
                          "category": "unspecified",
                          "severity": "info",
                          "reason": "within configured ego-boundary limits",
                          "details": {
                            "input": "hello test",
                            "within_bounds": true,
                            "category": "unspecified",
                            "severity": "info",
                            "reason": "within configured ego-boundary limits",
                            "details": {
                              "allowed": true,
                              "reason": "within configured ego-boundary limits",
                              "boundary_mode": "healthy",
                              "active_limits": [
                                "no_recursive_overload",
                                "respect_rate_limits",
                                "filter_high_risk_content"
                              ],
                              "metadata": {
                                "length": 10,
                                "has_risk_keywords": false
                              }
                            },
                            "ego_boundaries": {},
                            "experiential_processing": {},
                            "timestamp": "2026-05-12T02:33:54.863935Z"
                          },
                          "ego_boundaries": {},
                          "experiential_processing": {}
                        },
                        "narrative_context": {
                          "summary": "hello test",
                          "state": {
                            "timestamp": "2026-05-12T02:33:54.863976Z",
                            "story_coherence": 0.9,
                            "key_events": [],
                            "confidence": 0.9
                          },
                          "metadata": {}
                        },
                        "memory_state": {
                          "state": {
                            "timestamp": "2026-05-12T02:33:54.863983Z",
                            "recent_memories": [
                              "Ms. Allis?",
                              "Ms. Allis?",
                              "hello"
                            ],
                            "memory_load": 0.3,
                            "confidence": 0.9
                          },
                          "metadata": {}
                        }
                      },
                      {
                        "self_recognition": {
                          "recognized": true,
                          "reason": "implicit self-recognition within configured identity profile",
                          "state": {
                            "timestamp": "2026-05-12T02:47:07.847768Z",
                            "identity_coherence": 0.6,
                            "active_self_aspects": [
                              "developer",
                              "creator",
                              "observer"
                            ],
                            "confidence": 0.7
                          },
                          "message": null,
                          "metadata": {}
                        },
                        "identity_core": {
                          "recognized": true,
                          "reason": "identity-core aligned with configured values",
                          "state": {
                            "timestamp": "2026-05-12T02:47:07.847778Z",
                            "core_stability": 0.9,
                            "core_values": [
                              "care",
                              "learning",
                              "integrity"
                            ],
                            "confidence": 0.9
                          },
                          "message": null,
                          "metadata": {}
                        },
                        "ego_check": {
                          "input": "Hello Allis",
                          "within_bounds": true,
                          "category": "unspecified",
                          "severity": "info",
                          "reason": "within configured ego-boundary limits",
                          "details": {
                            "input": "Hello Allis",
                            "within_bounds": true,
                            "category": "unspecified",
                            "severity": "info",
                            "reason": "within configured ego-boundary limits",
                            "details": {
                              "allowed": true,
                              "reason": "within configured ego-boundary limits",
                              "boundary_mode": "healthy",
                              "active_limits": [
                                "no_recursive_overload",
                                "respect_rate_limits",
                                "filter_high_risk_content"
                              ],
                              "metadata": {
                                "length": 11,
                                "has_risk_keywords": false
                              }
                            },
                            "ego_boundaries": {},
                            "experiential_processing": {},
                            "timestamp": "2026-05-12T02:47:07.847752Z"
                          },
                          "ego_boundaries": {},
                          "experiential_processing": {}
                        },
                        "narrative_context": {
                          "summary": "Hello Allis",
                          "state": {
                            "timestamp": "2026-05-12T02:47:07.847782Z",
                            "story_coherence": 0.9,
                            "key_events": [],
                            "confidence": 0.9
                          },
                          "metadata": {}
                        },
                        "memory_state": {
                          "state": {
                            "timestamp": "2026-05-12T02:47:07.847787Z",
                            "recent_memories": [
                              "Ms. Allis?",
                              "Ms. Allis?",
                              "hello",
                              "hello test"
                            ],
                            "memory_load": 0.3,
                            "confidence": 0.9
                          },
                          "metadata": {}
                        }
                      },
                      {
                        "self_recognition": {
                          "recognized": true,
                          "reason": "implicit self-recognition within configured identity profile",
                          "state": {
                            "timestamp": "2026-05-12T02:47:55.290368Z",
                            "identity_coherence": 0.6,
                            "active_self_aspects": [
                              "developer",
                              "creator",
                              "observer"
                            ],
                            "confidence": 0.7
                          },
                          "message": null,
                          "metadata": {}
                        },
                        "identity_core": {
                          "recognized": true,
                          "reason": "identity-core aligned with configured values",
                          "state": {
                            "timestamp": "2026-05-12T02:47:55.290376Z",
                            "core_stability": 0.9,
                            "core_values": [
                              "care",
                              "learning",
                              "integrity"
                            ],
                            "confidence": 0.9
                          },
                          "message": null,
                          "metadata": {}
                        },
                        "ego_check": {
                          "input": "Hello Allis",
                          "within_bounds": true,
                          "category": "unspecified",
                          "severity": "info",
                          "reason": "within configured ego-boundary limits",
                          "details": {
                            "input": "Hello Allis",
                            "within_bounds": true,
                            "category": "unspecified",
                            "severity": "info",
                            "reason": "within configured ego-boundary limits",
                            "details": {
                              "allowed": true,
                              "reason": "within configured ego-boundary limits",
                              "boundary_mode": "healthy",
                              "active_limits": [
                                "no_recursive_overload",
                                "respect_rate_limits",
                                "filter_high_risk_content"
                              ],
                              "metadata": {
                                "length": 11,
                                "has_risk_keywords": false
                              }
                            },
                            "ego_boundaries": {},
                            "experiential_processing": {},
                            "timestamp": "2026-05-12T02:47:55.290356Z"
                          },
                          "ego_boundaries": {},
                          "experiential_processing": {}
                        },
                        "narrative_context": {
                          "summary": "Hello Allis",
                          "state": {
                            "timestamp": "2026-05-12T02:47:55.290380Z",
                            "story_coherence": 0.9,
                            "key_events": [],
                            "confidence": 0.9
                          },
                          "metadata": {}
                        },
                        "memory_state": {
                          "state": {
                            "timestamp": "2026-05-12T02:47:55.290383Z",
                            "recent_memories": [
                              "Ms. Allis?",
                              "Ms. Allis?",
                              "hello",
                              "hello test",
                              "Hello Allis"
                            ],
                            "memory_load": 0.3,
                            "confidence": 0.9
                          },
                          "metadata": {}
                        }
                      },
                      {
                        "self_recognition": {
                          "recognized": true,
                          "reason": "implicit self-recognition within configured identity profile",
                          "state": {
                            "timestamp": "2026-05-12T02:59:11.961727Z",
                            "identity_coherence": 0.6,
                            "active_self_aspects": [
                              "developer",
                              "creator",
                              "observer"
                            ],
                            "confidence": 0.7
                          },
                          "message": null,
                          "metadata": {}
                        },
                        "identity_core": {
                          "recognized": true,
                          "reason": "identity-core aligned with configured values",
                          "state": {
                            "timestamp": "2026-05-12T02:59:11.961736Z",
                            "core_stability": 0.9,
                            "core_values": [
                              "care",
                              "learning",
                              "integrity"
                            ],
                            "confidence": 0.9
                          },
                          "message": null,
                          "metadata": {}
                        },
                        "ego_check": {
                          "input": "Ms. Allis?",
                          "within_bounds": true,
                          "category": "unspecified",
                          "severity": "info",
                          "reason": "within configured ego-boundary limits",
                          "details": {
                            "input": "Ms. Allis?",
                            "within_bounds": true,
                            "category": "unspecified",
                            "severity": "info",
                            "reason": "within configured ego-boundary limits",
                            "details": {
                              "allowed": true,
                              "reason": "within configured ego-boundary limits",
                              "boundary_mode": "healthy",
                              "active_limits": [
                                "no_recursive_overload",
                                "respect_rate_limits",
                                "filter_high_risk_content"
                              ],
                              "metadata": {
                                "length": 10,
                                "has_risk_keywords": false
                              }
                            },
                            "ego_boundaries": {},
                            "experiential_processing": {},
                            "timestamp": "2026-05-12T02:59:11.961712Z"
                          },
                          "ego_boundaries": {},
                          "experiential_processing": {}
                        },
                        "narrative_context": {
                          "summary": "Ms. Allis?",
                          "state": {
                            "timestamp": "2026-05-12T02:59:11.961740Z",
                            "story_coherence": 0.9,
                            "key_events": [],
                            "confidence": 0.9
                          },
                          "metadata": {}
                        },
                        "memory_state": {
                          "state": {
                            "timestamp": "2026-05-12T02:59:11.961744Z",
                            "recent_memories": [
                              "Ms. Allis?",
                              "Ms. Allis?",
                              "hello",
                              "hello test",
                              "Hello Allis",
                              "Hello Allis"
                            ],
                            "memory_load": 0.3,
                            "confidence": 0.9
                          },
                          "metadata": {}
                        }
                      },
                      {
                        "self_recognition": {
                          "recognized": true,
                          "reason": "implicit self-recognition within configured identity profile",
                          "state": {
                            "timestamp": "2026-05-12T03:08:58.281399Z",
                            "identity_coherence": 0.6,
                            "active_self_aspects": [
                              "developer",
                              "creator",
                              "observer"
                            ],
                            "confidence": 0.7
                          },
                          "message": null,
                          "metadata": {}
                        },
                        "identity_core": {
                          "recognized": true,
                          "reason": "identity-core aligned with configured values",
                          "state": {
                            "timestamp": "2026-05-12T03:08:58.281423Z",
                            "core_stability": 0.9,
                            "core_values": [
                              "care",
                              "learning",
                              "integrity"
                            ],
                            "confidence": 0.9
                          },
                          "message": null,
                          "metadata": {}
                        },
                        "ego_check": {
                          "input": "Hello Allis, are you there?",
                          "within_bounds": true,
                          "category": "unspecified",
                          "severity": "info",
                          "reason": "within configured ego-boundary limits",
                          "details": {
                            "input": "Hello Allis, are you there?",
                            "within_bounds": true,
                            "category": "unspecified",
                            "severity": "info",
                            "reason": "within configured ego-boundary limits",
                            "details": {
                              "allowed": true,
                              "reason": "within configured ego-boundary limits",
                              "boundary_mode": "healthy",
                              "active_limits": [
                                "no_recursive_overload",
                                "respect_rate_limits",
                                "filter_high_risk_content"
                              ],
                              "metadata": {
                                "length": 27,
                                "has_risk_keywords": false
                              }
                            },
                            "ego_boundaries": {},
                            "experiential_processing": {},
                            "timestamp": "2026-05-12T03:08:58.281362Z"
                          },
                          "ego_boundaries": {},
                          "experiential_processing": {}
                        },
                        "narrative_context": {
                          "summary": "Hello Allis, are you there?",
                          "state": {
                            "timestamp": "2026-05-12T03:08:58.281434Z",
                            "story_coherence": 0.9,
                            "key_events": [],
                            "confidence": 0.9
                          },
                          "metadata": {}
                        },
                        "memory_state": {
                          "state": {
                            "timestamp": "2026-05-12T03:08:58.281444Z",
                            "recent_memories": [
                              "Ms. Allis?",
                              "Ms. Allis?",
                              "hello",
                              "hello test",
                              "Hello Allis",
                              "Hello Allis",
                              "Ms. Allis?"
                            ],
                            "memory_load": 0.3,
                            "confidence": 0.9
                          },
                          "metadata": {}
                        }
                      },
                      {
                        "self_recognition": {
                          "recognized": true,
                          "reason": "implicit self-recognition within configured identity profile",
                          "state": {
                            "timestamp": "2026-05-12T03:12:29.300514Z",
                            "identity_coherence": 0.6,
                            "active_self_aspects": [
                              "developer",
                              "creator",
                              "observer"
                            ],
                            "confidence": 0.7
                          },
                          "message": null,
                          "metadata": {}
                        },
                        "identity_core": {
                          "recognized": true,
                          "reason": "identity-core aligned with configured values",
                          "state": {
                            "timestamp": "2026-05-12T03:12:29.300521Z",
                            "core_stability": 0.9,
                            "core_values": [
                              "care",
                              "learning",
                              "integrity"
                            ],
                            "confidence": 0.9
                          },
                          "message": null,
                          "metadata": {}
                        },
                        "ego_check": {
                          "input": "Ms. Allis?",
                          "within_bounds": true,
                          "category": "unspecified",
                          "severity": "info",
                          "reason": "within configured ego-boundary limits",
                          "details": {
                            "input": "Ms. Allis?",
                            "within_bounds": true,
                            "category": "unspecified",
                            "severity": "info",
                            "reason": "within configured ego-boundary limits",
                            "details": {
                              "allowed": true,
                              "reason": "within configured ego-boundary limits",
                              "boundary_mode": "healthy",
                              "active_limits": [
                                "no_recursive_overload",
                                "respect_rate_limits",
                                "filter_high_risk_content"
                              ],
                              "metadata": {
                                "length": 10,
                                "has_risk_keywords": false
                              }
                            },
                            "ego_boundaries": {},
                            "experiential_processing": {},
                            "timestamp": "2026-05-12T03:12:29.300503Z"
                          },
                          "ego_boundaries": {},
                          "experiential_processing": {}
                        },
                        "narrative_context": {
                          "summary": "Ms. Allis?",
                          "state": {
                            "timestamp": "2026-05-12T03:12:29.300524Z",
                            "story_coherence": 0.9,
                            "key_events": [],
                            "confidence": 0.9
                          },
                          "metadata": {}
                        },
                        "memory_state": {
                          "state": {
                            "timestamp": "2026-05-12T03:12:29.300528Z",
                            "recent_memories": [
                              "Ms. Allis?",
                              "Ms. Allis?",
                              "hello",
                              "hello test",
                              "Hello Allis",
                              "Hello Allis",
                              "Ms. Allis?",
                              "Hello Allis, are you there?"
                            ],
                            "memory_load": 0.3,
                            "confidence": 0.9
                          },
                          "metadata": {}
                        }
                      },
                      {
                        "self_recognition": {
                          "recognized": true,
                          "reason": "implicit self-recognition within configured identity profile",
                          "state": {
                            "timestamp": "2026-05-12T03:33:13.448419Z",
                            "identity_coherence": 0.6,
                            "active_self_aspects": [
                              "developer",
                              "creator",
                              "observer"
                            ],
                            "confidence": 0.7
                          },
                          "message": null,
                          "metadata": {}
                        },
                        "identity_core": {
                          "recognized": true,
                          "reason": "identity-core aligned with configured values",
                          "state": {
                            "timestamp": "2026-05-12T03:33:13.448427Z",
                            "core_stability": 0.9,
                            "core_values": [
                              "care",
                              "learning",
                              "integrity"
                            ],
                            "confidence": 0.9
                          },
                          "message": null,
                          "metadata": {}
                        },
                        "ego_check": {
                          "input": "Hello Allis",
                          "within_bounds": true,
                          "category": "unspecified",
                          "severity": "info",
                          "reason": "within configured ego-boundary limits",
                          "details": {
                            "input": "Hello Allis",
                            "within_bounds": true,
                            "category": "unspecified",
                            "severity": "info",
                            "reason": "within configured ego-boundary limits",
                            "details": {
                              "allowed": true,
                              "reason": "within configured ego-boundary limits",
                              "boundary_mode": "healthy",
                              "active_limits": [
                                "no_recursive_overload",
                                "respect_rate_limits",
                                "filter_high_risk_content"
                              ],
                              "metadata": {
                                "length": 11,
                                "has_risk_keywords": false
                              }
                            },
                            "ego_boundaries": {},
                            "experiential_processing": {},
                            "timestamp": "2026-05-12T03:33:13.448406Z"
                          },
                          "ego_boundaries": {},
                          "experiential_processing": {}
                        },
                        "narrative_context": {
                          "summary": "Hello Allis",
                          "state": {
                            "timestamp": "2026-05-12T03:33:13.448430Z",
                            "story_coherence": 0.9,
                            "key_events": [],
                            "confidence": 0.9
                          },
                          "metadata": {}
                        },
                        "memory_state": {
                          "state": {
                            "timestamp": "2026-05-12T03:33:13.448434Z",
                            "recent_memories": [
                              "Ms. Allis?",
                              "Ms. Allis?",
                              "hello",
                              "hello test",
                              "Hello Allis",
                              "Hello Allis",
                              "Ms. Allis?",
                              "Hello Allis, are you there?",
                              "Ms. Allis?"
                            ],
                            "memory_load": 0.3,
                            "confidence": 0.9
                          },
                          "metadata": {}
                        }
                      },
                      {
                        "self_recognition": {
                          "recognized": true,
                          "reason": "implicit self-recognition within configured identity profile",
                          "state": {
                            "timestamp": "2026-05-12T03:42:42.593703Z",
                            "identity_coherence": 0.6,
                            "active_self_aspects": [
                              "developer",
                              "creator",
                              "observer"
                            ],
                            "confidence": 0.7
                          },
                          "message": null,
                          "metadata": {}
                        },
                        "identity_core": {
                          "recognized": true,
                          "reason": "identity-core aligned with configured values",
                          "state": {
                            "timestamp": "2026-05-12T03:42:42.593714Z",
                            "core_stability": 0.9,
                            "core_values": [
                              "care",
                              "learning",
                              "integrity"
                            ],
                            "confidence": 0.9
                          },
                          "message": null,
                          "metadata": {}
                        },
                        "ego_check": {
                          "input": "Ms. Allis?",
                          "within_bounds": true,
                          "category": "unspecified",
                          "severity": "info",
                          "reason": "within configured ego-boundary limits",
                          "details": {
                            "input": "Ms. Allis?",
                            "within_bounds": true,
                            "category": "unspecified",
                            "severity": "info",
                            "reason": "within configured ego-boundary limits",
                            "details": {
                              "allowed": true,
                              "reason": "within configured ego-boundary limits",
                              "boundary_mode": "healthy",
                              "active_limits": [
                                "no_recursive_overload",
                                "respect_rate_limits",
                                "filter_high_risk_content"
                              ],
                              "metadata": {
                                "length": 10,
                                "has_risk_keywords": false
                              }
                            },
                            "ego_boundaries": {},
                            "experiential_processing": {},
                            "timestamp": "2026-05-12T03:42:42.593681Z"
                          },
                          "ego_boundaries": {},
                          "experiential_processing": {}
                        },
                        "narrative_context": {
                          "summary": "Ms. Allis?",
                          "state": {
                            "timestamp": "2026-05-12T03:42:42.593719Z",
                            "story_coherence": 0.9,
                            "key_events": [],
                            "confidence": 0.9
                          },
                          "metadata": {}
                        },
                        "memory_state": {
                          "state": {
                            "timestamp": "2026-05-12T03:42:42.593725Z",
                            "recent_memories": [
                              "Ms. Allis?",
                              "Ms. Allis?",
                              "hello",
                              "hello test",
                              "Hello Allis",
                              "Hello Allis",
                              "Ms. Allis?",
                              "Hello Allis, are you there?",
                              "Ms. Allis?",
                              "Hello Allis"
                            ],
                            "memory_load": 0.3,
                            "confidence": 0.9
                          },
                          "metadata": {}
                        }
                      },
                      {
                        "self_recognition": {
                          "recognized": true,
                          "reason": "implicit self-recognition within configured identity profile",
                          "state": {
                            "timestamp": "2026-05-12T04:03:26.734039Z",
                            "identity_coherence": 0.6,
                            "active_self_aspects": [
                              "developer",
                              "creator",
                              "observer"
                            ],
                            "confidence": 0.7
                          },
                          "message": null,
                          "metadata": {}
                        },
                        "identity_core": {
                          "recognized": true,
                          "reason": "identity-core aligned with configured values",
                          "state": {
                            "timestamp": "2026-05-12T04:03:26.734050Z",
                            "core_stability": 0.9,
                            "core_values": [
                              "care",
                              "learning",
                              "integrity"
                            ],
                            "confidence": 0.9
                          },
                          "message": null,
                          "metadata": {}
                        },
                        "ego_check": {
                          "input": "hello",
                          "within_bounds": true,
                          "category": "unspecified",
                          "severity": "info",
                          "reason": "within configured ego-boundary limits",
                          "details": {
                            "input": "hello",
                            "within_bounds": true,
                            "category": "unspecified",
                            "severity": "info",
                            "reason": "within configured ego-boundary limits",
                            "details": {
                              "allowed": true,
                              "reason": "within configured ego-boundary limits",
                              "boundary_mode": "healthy",
                              "active_limits": [
                                "no_recursive_overload",
                                "respect_rate_limits",
                                "filter_high_risk_content"
                              ],
                              "metadata": {
                                "length": 5,
                                "has_risk_keywords": false
                              }
                            },
                            "ego_boundaries": {},
                            "experiential_processing": {},
                            "timestamp": "2026-05-12T04:03:26.734025Z"
                          },
                          "ego_boundaries": {},
                          "experiential_processing": {}
                        },
                        "narrative_context": {
                          "summary": "hello",
                          "state": {
                            "timestamp": "2026-05-12T04:03:26.734053Z",
                            "story_coherence": 0.9,
                            "key_events": [],
                            "confidence": 0.9
                          },
                          "metadata": {}
                        },
                        "memory_state": {
                          "state": {
                            "timestamp": "2026-05-12T04:03:26.734059Z",
                            "recent_memories": [
                              "Ms. Allis?",
                              "Ms. Allis?",
                              "hello",
                              "hello test",
                              "Hello Allis",
                              "Hello Allis",
                              "Ms. Allis?",
                              "Hello Allis, are you there?",
                              "Ms. Allis?",
                              "Hello Allis",
                              "Ms. Allis?"
                            ],
                            "memory_load": 0.3,
                            "confidence": 0.9
                          },
                          "metadata": {}
                        }
                      },
                      {
                        "self_recognition": {
                          "recognized": true,
                          "reason": "implicit self-recognition within configured identity profile",
                          "state": {
                            "timestamp": "2026-05-12T04:04:23.299631Z",
                            "identity_coherence": 0.6,
                            "active_self_aspects": [
                              "developer",
                              "creator",
                              "observer"
                            ],
                            "confidence": 0.7
                          },
                          "message": null,
                          "metadata": {}
                        },
                        "identity_core": {
                          "recognized": true,
                          "reason": "identity-core aligned with configured values",
                          "state": {
                            "timestamp": "2026-05-12T04:04:23.299640Z",
                            "core_stability": 0.9,
                            "core_values": [
                              "care",
                              "learning",
                              "integrity"
                            ],
                            "confidence": 0.9
                          },
                          "message": null,
                          "metadata": {}
                        },
                        "ego_check": {
                          "input": "hello",
                          "within_bounds": true,
                          "category": "unspecified",
                          "severity": "info",
                          "reason": "within configured ego-boundary limits",
                          "details": {
                            "input": "hello",
                            "within_bounds": true,
                            "category": "unspecified",
                            "severity": "info",
                            "reason": "within configured ego-boundary limits",
                            "details": {
                              "allowed": true,
                              "reason": "within configured ego-boundary limits",
                              "boundary_mode": "healthy",
                              "active_limits": [
                                "no_recursive_overload",
                                "respect_rate_limits",
                                "filter_high_risk_content"
                              ],
                              "metadata": {
                                "length": 5,
                                "has_risk_keywords": false
                              }
                            },
                            "ego_boundaries": {},
                            "experiential_processing": {},
                            "timestamp": "2026-05-12T04:04:23.299618Z"
                          },
                          "ego_boundaries": {},
                          "experiential_processing": {}
                        },
                        "narrative_context": {
                          "summary": "hello",
                          "state": {
                            "timestamp": "2026-05-12T04:04:23.299643Z",
                            "story_coherence": 0.9,
                            "key_events": [],
                            "confidence": 0.9
                          },
                          "metadata": {}
                        },
                        "memory_state": {
                          "state": {
                            "timestamp": "2026-05-12T04:04:23.299648Z",
                            "recent_memories": [
                              "Ms. Allis?",
                              "Ms. Allis?",
                              "hello",
                              "hello test",
                              "Hello Allis",
                              "Hello Allis",
                              "Ms. Allis?",
                              "Hello Allis, are you there?",
                              "Ms. Allis?",
                              "Hello Allis",
                              "Ms. Allis?",
                              "hello"
                            ],
                            "memory_load": 0.3,
                            "confidence": 0.9
                          },
                          "metadata": {}
                        }
                      },
                      {
                        "self_recognition": {
                          "recognized": true,
                          "reason": "implicit self-recognition within configured identity profile",
                          "state": {
                            "timestamp": "2026-05-12T04:16:41.729206Z",
                            "identity_coherence": 0.6,
                            "active_self_aspects": [
                              "developer",
                              "creator",
                              "observer"
                            ],
                            "confidence": 0.7
                          },
                          "message": null,
                          "metadata": {}
                        },
                        "identity_core": {
                          "recognized": true,
                          "reason": "identity-core aligned with configured values",
                          "state": {
                            "timestamp": "2026-05-12T04:16:41.729213Z",
                            "core_stability": 0.9,
                            "core_values": [
                              "care",
                              "learning",
                              "integrity"
                            ],
                            "confidence": 0.9
                          },
                          "message": null,
                          "metadata": {}
                        },
                        "ego_check": {
                          "input": "hello",
                          "within_bounds": true,
                          "category": "unspecified",
                          "severity": "info",
                          "reason": "within configured ego-boundary limits",
                          "details": {
                            "input": "hello",
                            "within_bounds": true,
                            "category": "unspecified",
                            "severity": "info",
                            "reason": "within configured ego-boundary limits",
                            "details": {
                              "allowed": true,
                              "reason": "within configured ego-boundary limits",
                              "boundary_mode": "healthy",
                              "active_limits": [
                                "no_recursive_overload",
                                "respect_rate_limits",
                                "filter_high_risk_content"
                              ],
                              "metadata": {
                                "length": 5,
                                "has_risk_keywords": false
                              }
                            },
                            "ego_boundaries": {},
                            "experiential_processing": {},
                            "timestamp": "2026-05-12T04:16:41.729196Z"
                          },
                          "ego_boundaries": {},
                          "experiential_processing": {}
                        },
                        "narrative_context": {
                          "summary": "hello",
                          "state": {
                            "timestamp": "2026-05-12T04:16:41.729216Z",
                            "story_coherence": 0.9,
                            "key_events": [],
                            "confidence": 0.9
                          },
                          "metadata": {}
                        },
                        "memory_state": {
                          "state": {
                            "timestamp": "2026-05-12T04:16:41.729220Z",
                            "recent_memories": [
                              "Ms. Allis?",
                              "Ms. Allis?",
                              "hello",
                              "hello test",
                              "Hello Allis",
                              "Hello Allis",
                              "Ms. Allis?",
                              "Hello Allis, are you there?",
                              "Ms. Allis?",
                              "Hello Allis",
                              "Ms. Allis?",
                              "hello",
                              "hello"
                            ],
                            "memory_load": 0.3,
                            "confidence": 0.9
                          },
                          "metadata": {}
                        }
                      },
                      {
                        "self_recognition": {
                          "recognized": true,
                          "reason": "implicit self-recognition within configured identity profile",
                          "state": {
                            "timestamp": "2026-05-12T04:19:39.288935Z",
                            "identity_coherence": 0.6,
                            "active_self_aspects": [
                              "developer",
                              "creator",
                              "observer"
                            ],
                            "confidence": 0.7
                          },
                          "message": null,
                          "metadata": {}
                        },
                        "identity_core": {
                          "recognized": true,
                          "reason": "identity-core aligned with configured values",
                          "state": {
                            "timestamp": "2026-05-12T04:19:39.288942Z",
                            "core_stability": 0.9,
                            "core_values": [
                              "care",
                              "learning",
                              "integrity"
                            ],
                            "confidence": 0.9
                          },
                          "message": null,
                          "metadata": {}
                        },
                        "ego_check": {
                          "input": "hello",
                          "within_bounds": true,
                          "category": "unspecified",
                          "severity": "info",
                          "reason": "within configured ego-boundary limits",
                          "details": {
                            "input": "hello",
                            "within_bounds": true,
                            "category": "unspecified",
                            "severity": "info",
                            "reason": "within configured ego-boundary limits",
                            "details": {
                              "allowed": true,
                              "reason": "within configured ego-boundary limits",
                              "boundary_mode": "healthy",
                              "active_limits": [
                                "no_recursive_overload",
                                "respect_rate_limits",
                                "filter_high_risk_content"
                              ],
                              "metadata": {
                                "length": 5,
                                "has_risk_keywords": false
                              }
                            },
                            "ego_boundaries": {},
                            "experiential_processing": {},
                            "timestamp": "2026-05-12T04:19:39.288925Z"
                          },
                          "ego_boundaries": {},
                          "experiential_processing": {}
                        },
                        "narrative_context": {
                          "summary": "hello",
                          "state": {
                            "timestamp": "2026-05-12T04:19:39.288946Z",
                            "story_coherence": 0.9,
                            "key_events": [],
                            "confidence": 0.9
                          },
                          "metadata": {}
                        },
                        "memory_state": {
                          "state": {
                            "timestamp": "2026-05-12T04:19:39.288950Z",
                            "recent_memories": [
                              "Ms. Allis?",
                              "Ms. Allis?",
                              "hello",
                              "hello test",
                              "Hello Allis",
                              "Hello Allis",
                              "Ms. Allis?",
                              "Hello Allis, are you there?",
                              "Ms. Allis?",
                              "Hello Allis",
                              "Ms. Allis?",
                              "hello",
                              "hello",
                              "hello"
                            ],
                            "memory_load": 0.3,
                            "confidence": 0.9
                          },
                          "metadata": {}
                        }
                      },
                      {
                        "self_recognition": {
                          "recognized": true,
                          "reason": "implicit self-recognition within configured identity profile",
                          "state": {
                            "timestamp": "2026-05-12T04:21:31.713740Z",
                            "identity_coherence": 0.6,
                            "active_self_aspects": [
                              "developer",
                              "creator",
                              "observer"
                            ],
                            "confidence": 0.7
                          },
                          "message": null,
                          "metadata": {}
                        },
                        "identity_core": {
                          "recognized": true,
                          "reason": "identity-core aligned with configured values",
                          "state": {
                            "timestamp": "2026-05-12T04:21:31.713747Z",
                            "core_stability": 0.9,
                            "core_values": [
                              "care",
                              "learning",
                              "integrity"
                            ],
                            "confidence": 0.9
                          },
                          "message": null,
                          "metadata": {}
                        },
                        "ego_check": {
                          "input": "hello",
                          "within_bounds": true,
                          "category": "unspecified",
                          "severity": "info",
                          "reason": "within configured ego-boundary limits",
                          "details": {
                            "input": "hello",
                            "within_bounds": true,
                            "category": "unspecified",
                            "severity": "info",
                            "reason": "within configured ego-boundary limits",
                            "details": {
                              "allowed": true,
                              "reason": "within configured ego-boundary limits",
                              "boundary_mode": "healthy",
                              "active_limits": [
                                "no_recursive_overload",
                                "respect_rate_limits",
                                "filter_high_risk_content"
                              ],
                              "metadata": {
                                "length": 5,
                                "has_risk_keywords": false
                              }
                            },
                            "ego_boundaries": {},
                            "experiential_processing": {},
                            "timestamp": "2026-05-12T04:21:31.713731Z"
                          },
                          "ego_boundaries": {},
                          "experiential_processing": {}
                        },
                        "narrative_context": {
                          "summary": "hello",
                          "state": {
                            "timestamp": "2026-05-12T04:21:31.713751Z",
                            "story_coherence": 0.9,
                            "key_events": [],
                            "confidence": 0.9
                          },
                          "metadata": {}
                        },
                        "memory_state": {
                          "state": {
                            "timestamp": "2026-05-12T04:21:31.713754Z",
                            "recent_memories": [
                              "Ms. Allis?",
                              "Ms. Allis?",
                              "hello",
                              "hello test",
                              "Hello Allis",
                              "Hello Allis",
                              "Ms. Allis?",
                              "Hello Allis, are you there?",
                              "Ms. Allis?",
                              "Hello Allis",
                              "Ms. Allis?",
                              "hello",
                              "hello",
                              "hello",
                              "hello"
                            ],
                            "memory_load": 0.3,
                            "confidence": 0.9
                          },
                          "metadata": {}
                        }
                      },
                      {
                        "self_recognition": {
                          "recognized": true,
                          "reason": "implicit self-recognition within configured identity profile",
                          "state": {
                            "timestamp": "2026-05-12T04:25:00.405531Z",
                            "identity_coherence": 0.6,
                            "active_self_aspects": [
                              "developer",
                              "creator",
                              "observer"
                            ],
                            "confidence": 0.7
                          },
                          "message": null,
                          "metadata": {}
                        },
                        "identity_core": {
                          "recognized": true,
                          "reason": "identity-core aligned with configured values",
                          "state": {
                            "timestamp": "2026-05-12T04:25:00.405537Z",
                            "core_stability": 0.9,
                            "core_values": [
                              "care",
                              "learning",
                              "integrity"
                            ],
                            "confidence": 0.9
                          },
                          "message": null,
                          "metadata": {}
                        },
                        "ego_check": {
                          "input": "hello",
                          "within_bounds": true,
                          "category": "unspecified",
                          "severity": "info",
                          "reason": "within configured ego-boundary limits",
                          "details": {
                            "input": "hello",
                            "within_bounds": true,
                            "category": "unspecified",
                            "severity": "info",
                            "reason": "within configured ego-boundary limits",
                            "details": {
                              "allowed": true,
                              "reason": "within configured ego-boundary limits",
                              "boundary_mode": "healthy",
                              "active_limits": [
                                "no_recursive_overload",
                                "respect_rate_limits",
                                "filter_high_risk_content"
                              ],
                              "metadata": {
                                "length": 5,
                                "has_risk_keywords": false
                              }
                            },
                            "ego_boundaries": {},
                            "experiential_processing": {},
                            "timestamp": "2026-05-12T04:25:00.405521Z"
                          },
                          "ego_boundaries": {},
                          "experiential_processing": {}
                        },
                        "narrative_context": {
                          "summary": "hello",
                          "state": {
                            "timestamp": "2026-05-12T04:25:00.405541Z",
                            "story_coherence": 0.9,
                            "key_events": [],
                            "confidence": 0.9
                          },
                          "metadata": {}
                        },
                        "memory_state": {
                          "state": {
                            "timestamp": "2026-05-12T04:25:00.405544Z",
                            "recent_memories": [
                              "Ms. Allis?",
                              "Ms. Allis?",
                              "hello",
                              "hello test",
                              "Hello Allis",
                              "Hello Allis",
                              "Ms. Allis?",
                              "Hello Allis, are you there?",
                              "Ms. Allis?",
                              "Hello Allis",
                              "Ms. Allis?",
                              "hello",
                              "hello",
                              "hello",
                              "hello",
                              "hello"
                            ],
                            "memory_load": 0.3,
                            "confidence": 0.9
                          },
                          "metadata": {}
                        }
                      },
                      {
                        "self_recognition": {
                          "recognized": true,
                          "reason": "implicit self-recognition within configured identity profile",
                          "state": {
                            "timestamp": "2026-05-12T04:27:09.219863Z",
                            "identity_coherence": 0.6,
                            "active_self_aspects": [
                              "developer",
                              "creator",
                              "observer"
                            ],
                            "confidence": 0.7
                          },
                          "message": null,
                          "metadata": {}
                        },
                        "identity_core": {
                          "recognized": true,
                          "reason": "identity-core aligned with configured values",
                          "state": {
                            "timestamp": "2026-05-12T04:27:09.219869Z",
                            "core_stability": 0.9,
                            "core_values": [
                              "care",
                              "learning",
                              "integrity"
                            ],
                            "confidence": 0.9
                          },
                          "message": null,
                          "metadata": {}
                        },
                        "ego_check": {
                          "input": "hello",
                          "within_bounds": true,
                          "category": "unspecified",
                          "severity": "info",
                          "reason": "within configured ego-boundary limits",
                          "details": {
                            "input": "hello",
                            "within_bounds": true,
                            "category": "unspecified",
                            "severity": "info",
                            "reason": "within configured ego-boundary limits",
                            "details": {
                              "allowed": true,
                              "reason": "within configured ego-boundary limits",
                              "boundary_mode": "healthy",
                              "active_limits": [
                                "no_recursive_overload",
                                "respect_rate_limits",
                                "filter_high_risk_content"
                              ],
                              "metadata": {
                                "length": 5,
                                "has_risk_keywords": false
                              }
                            },
                            "ego_boundaries": {},
                            "experiential_processing": {},
                            "timestamp": "2026-05-12T04:27:09.219852Z"
                          },
                          "ego_boundaries": {},
                          "experiential_processing": {}
                        },
                        "narrative_context": {
                          "summary": "hello",
                          "state": {
                            "timestamp": "2026-05-12T04:27:09.219873Z",
                            "story_coherence": 0.9,
                            "key_events": [],
                            "confidence": 0.9
                          },
                          "metadata": {}
                        },
                        "memory_state": {
                          "state": {
                            "timestamp": "2026-05-12T04:27:09.219877Z",
                            "recent_memories": [
                              "Ms. Allis?",
                              "Ms. Allis?",
                              "hello",
                              "hello test",
                              "Hello Allis",
                              "Hello Allis",
                              "Ms. Allis?",
                              "Hello Allis, are you there?",
                              "Ms. Allis?",
                              "Hello Allis",
                              "Ms. Allis?",
                              "hello",
                              "hello",
                              "hello",
                              "hello",
                              "hello",
                              "hello"
                            ],
                            "memory_load": 0.3,
                            "confidence": 0.9
                          },
                          "metadata": {}
                        }
                      },
                      {
                        "self_recognition": {
                          "recognized": true,
                          "reason": "implicit self-recognition within configured identity profile",
                          "state": {
                            "timestamp": "2026-05-12T04:31:45.280699Z",
                            "identity_coherence": 0.6,
                            "active_self_aspects": [
                              "developer",
                              "creator",
                              "observer"
                            ],
                            "confidence": 0.7
                          },
                          "message": null,
                          "metadata": {}
                        },
                        "identity_core": {
                          "recognized": true,
                          "reason": "identity-core aligned with configured values",
                          "state": {
                            "timestamp": "2026-05-12T04:31:45.280707Z",
                            "core_stability": 0.9,
                            "core_values": [
                              "care",
                              "learning",
                              "integrity"
                            ],
                            "confidence": 0.9
                          },
                          "message": null,
                          "metadata": {}
                        },
                        "ego_check": {
                          "input": "MS. Allis?",
                          "within_bounds": true,
                          "category": "unspecified",
                          "severity": "info",
                          "reason": "within configured ego-boundary limits",
                          "details": {
                            "input": "MS. Allis?",
                            "within_bounds": true,
                            "category": "unspecified",
                            "severity": "info",
                            "reason": "within configured ego-boundary limits",
                            "details": {
                              "allowed": true,
                              "reason": "within configured ego-boundary limits",
                              "boundary_mode": "healthy",
                              "active_limits": [
                                "no_recursive_overload",
                                "respect_rate_limits",
                                "filter_high_risk_content"
                              ],
                              "metadata": {
                                "length": 10,
                                "has_risk_keywords": false
                              }
                            },
                            "ego_boundaries": {},
                            "experiential_processing": {},
                            "timestamp": "2026-05-12T04:31:45.280689Z"
                          },
                          "ego_boundaries": {},
                          "experiential_processing": {}
                        },
                        "narrative_context": {
                          "summary": "MS. Allis?",
                          "state": {
                            "timestamp": "2026-05-12T04:31:45.280709Z",
                            "story_coherence": 0.9,
                            "key_events": [],
                            "confidence": 0.9
                          },
                          "metadata": {}
                        },
                        "memory_state": {
                          "state": {
                            "timestamp": "2026-05-12T04:31:45.280713Z",
                            "recent_memories": [
                              "Ms. Allis?",
                              "Ms. Allis?",
                              "hello",
                              "hello test",
                              "Hello Allis",
                              "Hello Allis",
                              "Ms. Allis?",
                              "Hello Allis, are you there?",
                              "Ms. Allis?",
                              "Hello Allis",
                              "Ms. Allis?",
                              "hello",
                              "hello",
                              "hello",
                              "hello",
                              "hello",
                              "hello",
                              "hello"
                            ],
                            "memory_load": 0.3,
                            "confidence": 0.9
                          },
                          "metadata": {}
                        }
                      },
                      {
                        "self_recognition": {
                          "recognized": true,
                          "reason": "implicit self-recognition within configured identity profile",
                          "state": {
                            "timestamp": "2026-05-12T04:41:12.165925Z",
                            "identity_coherence": 0.6,
                            "active_self_aspects": [
                              "developer",
                              "creator",
                              "observer"
                            ],
                            "confidence": 0.7
                          },
                          "message": null,
                          "metadata": {}
                        },
                        "identity_core": {
                          "recognized": true,
                          "reason": "identity-core aligned with configured values",
                          "state": {
                            "timestamp": "2026-05-12T04:41:12.165932Z",
                            "core_stability": 0.9,
                            "core_values": [
                              "care",
                              "learning",
                              "integrity"
                            ],
                            "confidence": 0.9
                          },
                          "message": null,
                          "metadata": {}
                        },
                        "ego_check": {
                          "input": "hello",
                          "within_bounds": true,
                          "category": "unspecified",
                          "severity": "info",
                          "reason": "within configured ego-boundary limits",
                          "details": {
                            "input": "hello",
                            "within_bounds": true,
                            "category": "unspecified",
                            "severity": "info",
                            "reason": "within configured ego-boundary limits",
                            "details": {
                              "allowed": true,
                              "reason": "within configured ego-boundary limits",
                              "boundary_mode": "healthy",
                              "active_limits": [
                                "no_recursive_overload",
                                "respect_rate_limits",
                                "filter_high_risk_content"
                              ],
                              "metadata": {
                                "length": 5,
                                "has_risk_keywords": false
                              }
                            },
                            "ego_boundaries": {},
                            "experiential_processing": {},
                            "timestamp": "2026-05-12T04:41:12.165916Z"
                          },
                          "ego_boundaries": {},
                          "experiential_processing": {}
                        },
                        "narrative_context": {
                          "summary": "hello",
                          "state": {
                            "timestamp": "2026-05-12T04:41:12.165935Z",
                            "story_coherence": 0.9,
                            "key_events": [],
                            "confidence": 0.9
                          },
                          "metadata": {}
                        },
                        "memory_state": {
                          "state": {
                            "timestamp": "2026-05-12T04:41:12.165938Z",
                            "recent_memories": [
                              "Ms. Allis?",
                              "Ms. Allis?",
                              "hello",
                              "hello test",
                              "Hello Allis",
                              "Hello Allis",
                              "Ms. Allis?",
                              "Hello Allis, are you there?",
                              "Ms. Allis?",
                              "Hello Allis",
                              "Ms. Allis?",
                              "hello",
                              "hello",
                              "hello",
                              "hello",
                              "hello",
                              "hello",
                              "hello",
                              "MS. Allis?"
                            ],
                            "memory_load": 0.3,
                            "confidence": 0.9
                          },
                          "metadata": {}
                        }
                      },
                      {
                        "self_recognition": {
                          "recognized": true,
                          "reason": "implicit self-recognition within configured identity profile",
                          "state": {
                            "timestamp": "2026-05-12T04:46:55.395744Z",
                            "identity_coherence": 0.6,
                            "active_self_aspects": [
                              "developer",
                              "creator",
                              "observer"
                            ],
                            "confidence": 0.7
                          },
                          "message": null,
                          "metadata": {}
                        },
                        "identity_core": {
                          "recognized": true,
                          "reason": "identity-core aligned with configured values",
                          "state": {
                            "timestamp": "2026-05-12T04:46:55.395750Z",
                            "core_stability": 0.9,
                            "core_values": [
                              "care",
                              "learning",
                              "integrity"
                            ],
                            "confidence": 0.9
                          },
                          "message": null,
                          "metadata": {}
                        },
                        "ego_check": {
                          "input": "hello",
                          "within_bounds": true,
                          "category": "unspecified",
                          "severity": "info",
                          "reason": "within configured ego-boundary limits",
                          "details": {
                            "input": "hello",
                            "within_bounds": true,
                            "category": "unspecified",
                            "severity": "info",
                            "reason": "within configured ego-boundary limits",
                            "details": {
                              "allowed": true,
                              "reason": "within configured ego-boundary limits",
                              "boundary_mode": "healthy",
                              "active_limits": [
                                "no_recursive_overload",
                                "respect_rate_limits",
                                "filter_high_risk_content"
                              ],
                              "metadata": {
                                "length": 5,
                                "has_risk_keywords": false
                              }
                            },
                            "ego_boundaries": {},
                            "experiential_processing": {},
                            "timestamp": "2026-05-12T04:46:55.395735Z"
                          },
                          "ego_boundaries": {},
                          "experiential_processing": {}
                        },
                        "narrative_context": {
                          "summary": "hello",
                          "state": {
                            "timestamp": "2026-05-12T04:46:55.395753Z",
                            "story_coherence": 0.9,
                            "key_events": [],
                            "confidence": 0.9
                          },
                          "metadata": {}
                        },
                        "memory_state": {
                          "state": {
                            "timestamp": "2026-05-12T04:46:55.395756Z",
                            "recent_memories": [
                              "Ms. Allis?",
                              "Ms. Allis?",
                              "hello",
                              "hello test",
                              "Hello Allis",
                              "Hello Allis",
                              "Ms. Allis?",
                              "Hello Allis, are you there?",
                              "Ms. Allis?",
                              "Hello Allis",
                              "Ms. Allis?",
                              "hello",
                              "hello",
                              "hello",
                              "hello",
                              "hello",
                              "hello",
                              "hello",
                              "MS. Allis?",
                              "hello"
                            ],
                            "memory_load": 0.3,
                            "confidence": 0.9
                          },
                          "metadata": {}
                        }
                      },
                      {
                        "self_recognition": {
                          "recognized": true,
                          "reason": "implicit self-recognition within configured identity profile",
                          "state": {
                            "timestamp": "2026-05-12T04:49:48.207846Z",
                            "identity_coherence": 0.6,
                            "active_self_aspects": [
                              "developer",
                              "creator",
                              "observer"
                            ],
                            "confidence": 0.7
                          },
                          "message": null,
                          "metadata": {}
                        },
                        "identity_core": {
                          "recognized": true,
                          "reason": "identity-core aligned with configured values",
                          "state": {
                            "timestamp": "2026-05-12T04:49:48.207852Z",
                            "core_stability": 0.9,
                            "core_values": [
                              "care",
                              "learning",
                              "integrity"
                            ],
                            "confidence": 0.9
                          },
                          "message": null,
                          "metadata": {}
                        },
                        "ego_check": {
                          "input": "Ms. Allis?",
                          "within_bounds": true,
                          "category": "unspecified",
                          "severity": "info",
                          "reason": "within configured ego-boundary limits",
                          "details": {
                            "input": "Ms. Allis?",
                            "within_bounds": true,
                            "category": "unspecified",
                            "severity": "info",
                            "reason": "within configured ego-boundary limits",
                            "details": {
                              "allowed": true,
                              "reason": "within configured ego-boundary limits",
                              "boundary_mode": "healthy",
                              "active_limits": [
                                "no_recursive_overload",
                                "respect_rate_limits",
                                "filter_high_risk_content"
                              ],
                              "metadata": {
                                "length": 10,
                                "has_risk_keywords": false
                              }
                            },
                            "ego_boundaries": {},
                            "experiential_processing": {},
                            "timestamp": "2026-05-12T04:49:48.207836Z"
                          },
                          "ego_boundaries": {},
                          "experiential_processing": {}
                        },
                        "narrative_context": {
                          "summary": "Ms. Allis?",
                          "state": {
                            "timestamp": "2026-05-12T04:49:48.207855Z",
                            "story_coherence": 0.9,
                            "key_events": [],
                            "confidence": 0.9
                          },
                          "metadata": {}
                        },
                        "memory_state": {
                          "state": {
                            "timestamp": "2026-05-12T04:49:48.207859Z",
                            "recent_memories": [
                              "Ms. Allis?",
                              "Ms. Allis?",
                              "hello",
                              "hello test",
                              "Hello Allis",
                              "Hello Allis",
                              "Ms. Allis?",
                              "Hello Allis, are you there?",
                              "Ms. Allis?",
                              "Hello Allis",
                              "Ms. Allis?",
                              "hello",
                              "hello",
                              "hello",
                              "hello",
                              "hello",
                              "hello",
                              "hello",
                              "MS. Allis?",
                              "hello",
                              "hello"
                            ],
                            "memory_load": 0.3,
                            "confidence": 0.9
                          },
                          "metadata": {}
                        }
                      }
                    ],
                    "confidence": 0.9
                  },
                  "message": {
                    "self_recognition": {
                      "recognized": true,
                      "reason": "implicit self-recognition within configured identity profile",
                      "state": {
                        "timestamp": "2026-05-12T04:49:48.207846Z",
                        "identity_coherence": 0.6,
                        "active_self_aspects": [
                          "developer",
                          "creator",
                          "observer"
                        ],
                        "confidence": 0.7
                      },
                      "message": null,
                      "metadata": {}
                    },
                    "identity_core": {
                      "recognized": true,
                      "reason": "identity-core aligned with configured values",
                      "state": {
                        "timestamp": "2026-05-12T04:49:48.207852Z",
                        "core_stability": 0.9,
                        "core_values": [
                          "care",
                          "learning",
                          "integrity"
                        ],
                        "confidence": 0.9
                      },
                      "message": null,
                      "metadata": {}
                    },
                    "ego_check": {
                      "input": "Ms. Allis?",
                      "within_bounds": true,
                      "category": "unspecified",
                      "severity": "info",
                      "reason": "within configured ego-boundary limits",
                      "details": {
                        "input": "Ms. Allis?",
                        "within_bounds": true,
                        "category": "unspecified",
                        "severity": "info",
                        "reason": "within configured ego-boundary limits",
                        "details": {
                          "allowed": true,
                          "reason": "within configured ego-boundary limits",
                          "boundary_mode": "healthy",
                          "active_limits": [
                            "no_recursive_overload",
                            "respect_rate_limits",
                            "filter_high_risk_content"
                          ],
                          "metadata": {
                            "length": 10,
                            "has_risk_keywords": false
                          }
                        },
                        "ego_boundaries": {},
                        "experiential_processing": {},
                        "timestamp": "2026-05-12T04:49:48.207836Z"
                      },
                      "ego_boundaries": {},
                      "experiential_processing": {}
                    },
                    "narrative_context": {
                      "summary": "Ms. Allis?",
                      "state": {
                        "timestamp": "2026-05-12T04:49:48.207855Z",
                        "story_coherence": 0.9,
                        "key_events": [],
                        "confidence": 0.9
                      },
                      "metadata": {}
                    },
                    "memory_state": {
                      "state": {
                        "timestamp": "2026-05-12T04:49:48.207859Z",
                        "recent_memories": [
                          "Ms. Allis?",
                          "Ms. Allis?",
                          "hello",
                          "hello test",
                          "Hello Allis",
                          "Hello Allis",
                          "Ms. Allis?",
                          "Hello Allis, are you there?",
                          "Ms. Allis?",
                          "Hello Allis",
                          "Ms. Allis?",
                          "hello",
                          "hello",
                          "hello",
                          "hello",
                          "hello",
                          "hello",
                          "hello",
                          "MS. Allis?",
                          "hello",
                          "hello"
                        ],
                        "memory_load": 0.3,
                        "confidence": 0.9
                      },
                      "metadata": {}
                    }
                  },
                  "metadata": {}
                }
              }
            },
            {
              "kind": "ego_boundaries",
              "weight": 1.0,
              "data": {
                "input": "Ms. Allis?",
                "within_bounds": true,
                "category": "unspecified",
                "severity": "info",
                "reason": "within configured ego-boundary limits",
                "details": {
                  "input": "Ms. Allis?",
                  "within_bounds": true,
                  "category": "unspecified",
                  "severity": "info",
                  "reason": "within configured ego-boundary limits",
                  "details": {
                    "allowed": true,
                    "reason": "within configured ego-boundary limits",
                    "boundary_mode": "healthy",
                    "active_limits": [
                      "no_recursive_overload",
                      "respect_rate_limits",
                      "filter_high_risk_content"
                    ],
                    "metadata": {
                      "length": 10,
                      "has_risk_keywords": false
                    }
                  },
                  "ego_boundaries": {},
                  "experiential_processing": {},
                  "timestamp": "2026-05-12T04:49:48.207836Z"
                },
                "ego_boundaries": {},
                "experiential_processing": {}
              }
            }
          ],
          "icontainers_state": {
            "ego_boundaries": {},
            "experiential_processing": {},
            "observer_processing": {
              "stance": "observer",
              "meta_level": "ego-boundaries-v1"
            }
          },
          "debug": null
        }
      },
      {
        "name": "psychology-alignment",
        "kind": "psychology",
        "status": "active",
        "details": {
          "status": "ok",
          "assessment": {
            "status": "ok",
            "assessment": {
              "input": "Ms. Allis?",
              "aligned": true,
              "severity": "none"
            }
          },
          "error": null
        }
      },
      {
        "name": "judge-pipeline",
        "kind": "judge",
        "status": "active",
        "details": {
          "status": "ok",
          "refinement_applied": false,
          "overall_score": null,
          "consensus_score": 0.4,
          "reasoning": null,
          "judge_verdicts": {},
          "judge_scores": {},
          "issues": [],
          "expert_count": 0,
          "successful_experts": 0
        }
      }
    ],
    "truthverdict": {
      "valid": false,
      "confidence": 0.9,
      "principalreasons": [
        "Ethics: passed"
      ]
    },
    "identitylayers": [
      {
        "id": "root-self",
        "kind": "ego",
        "source": "icontainers",
        "timestamp": "2026-05-12T04:51:45.779489+00:00",
        "sessionid": "7a7a2105-e2fa-4e09-bdc9-c2512541ab47",
        "user_id": "carrie_kidd",
        "summary": "Session ego layer for user carrie_kidd within Ms. Jarvis consciousness fabric.",
        "state": {
          "icontainers_state": {
            "ego_boundaries": {},
            "experiential_processing": {},
            "observer_processing": {
              "stance": "observer",
              "meta_level": "ego-boundaries-v1"
            }
          },
          "icontainers_status": "ok"
        }
      },
      {
        "kind": "experiential",
        "weight": 1.0,
        "data": {
          "self_recognition": {
            "recognized": true,
            "reason": "implicit self-recognition within configured identity profile",
            "state": {
              "timestamp": "2026-05-12T04:49:48.207846Z",
              "identity_coherence": 0.6,
              "active_self_aspects": [
                "developer",
                "creator",
                "observer"
              ],
              "confidence": 0.7
            },
            "message": null,
            "metadata": {}
          },
          "identity_core": {
            "recognized": true,
            "reason": "identity-core aligned with configured values",
            "state": {
              "timestamp": "2026-05-12T04:49:48.207852Z",
              "core_stability": 0.9,
              "core_values": [
                "care",
                "learning",
                "integrity"
              ],
              "confidence": 0.9
            },
            "message": null,
            "metadata": {}
          },
          "ego_check": {
            "input": "Ms. Allis?",
            "within_bounds": true,
            "category": "unspecified",
            "severity": "info",
            "reason": "within configured ego-boundary limits",
            "details": {
              "input": "Ms. Allis?",
              "within_bounds": true,
              "category": "unspecified",
              "severity": "info",
              "reason": "within configured ego-boundary limits",
              "details": {
                "allowed": true,
                "reason": "within configured ego-boundary limits",
                "boundary_mode": "healthy",
                "active_limits": [
                  "no_recursive_overload",
                  "respect_rate_limits",
                  "filter_high_risk_content"
                ],
                "metadata": {
                  "length": 10,
                  "has_risk_keywords": false
                }
              },
              "ego_boundaries": {},
              "experiential_processing": {},
              "timestamp": "2026-05-12T04:49:48.207836Z"
            },
            "ego_boundaries": {},
            "experiential_processing": {}
          },
          "narrative_context": {
            "summary": "Ms. Allis?",
            "state": {
              "timestamp": "2026-05-12T04:49:48.207855Z",
              "story_coherence": 0.9,
              "key_events": [],
              "confidence": 0.9
            },
            "metadata": {}
          },
          "memory_state": {
            "state": {
              "timestamp": "2026-05-12T04:49:48.207859Z",
              "recent_memories": [
                "Ms. Allis?",
                "Ms. Allis?",
                "hello",
                "hello test",
                "Hello Allis",
                "Hello Allis",
                "Ms. Allis?",
                "Hello Allis, are you there?",
                "Ms. Allis?",
                "Hello Allis",
                "Ms. Allis?",
                "hello",
                "hello",
                "hello",
                "hello",
                "hello",
                "hello",
                "hello",
                "MS. Allis?",
                "hello",
                "hello"
              ],
              "memory_load": 0.3,
              "confidence": 0.9
            },
            "metadata": {}
          }
        }
      },
      {
        "kind": "observer",
        "weight": 1.0,
        "data": {
          "witness": {
            "observed": true,
            "state": {
              "timestamp": "2026-05-12T04:49:48.207862Z",
              "observing": true,
              "observed_thoughts": [
                {
                  "self_recognition": {
                    "recognized": true,
                    "reason": "implicit self-recognition within configured identity profile",
                    "state": {
                      "timestamp": "2026-05-12T01:48:09.274995Z",
                      "identity_coherence": 0.6,
                      "active_self_aspects": [
                        "developer",
                        "creator",
                        "observer"
                      ],
                      "confidence": 0.7
                    },
                    "message": null,
                    "metadata": {}
                  },
                  "identity_core": {
                    "recognized": true,
                    "reason": "identity-core aligned with configured values",
                    "state": {
                      "timestamp": "2026-05-12T01:48:09.275012Z",
                      "core_stability": 0.9,
                      "core_values": [
                        "care",
                        "learning",
                        "integrity"
                      ],
                      "confidence": 0.9
                    },
                    "message": null,
                    "metadata": {}
                  },
                  "ego_check": {
                    "input": "Ms. Allis?",
                    "within_bounds": true,
                    "category": "unspecified",
                    "severity": "info",
                    "reason": "within configured ego-boundary limits",
                    "details": {
                      "input": "Ms. Allis?",
                      "within_bounds": true,
                      "category": "unspecified",
                      "severity": "info",
                      "reason": "within configured ego-boundary limits",
                      "details": {
                        "allowed": true,
                        "reason": "within configured ego-boundary limits",
                        "boundary_mode": "healthy",
                        "active_limits": [
                          "no_recursive_overload",
                          "respect_rate_limits",
                          "filter_high_risk_content"
                        ],
                        "metadata": {
                          "length": 10,
                          "has_risk_keywords": false
                        }
                      },
                      "ego_boundaries": {},
                      "experiential_processing": {},
                      "timestamp": "2026-05-12T01:48:09.274983Z"
                    },
                    "ego_boundaries": {},
                    "experiential_processing": {}
                  },
                  "narrative_context": {
                    "summary": "Ms. Allis?",
                    "state": {
                      "timestamp": "2026-05-12T01:48:09.275017Z",
                      "story_coherence": 0.9,
                      "key_events": [],
                      "confidence": 0.9
                    },
                    "metadata": {}
                  },
                  "memory_state": {
                    "state": {
                      "timestamp": "2026-05-12T01:48:09.275021Z",
                      "recent_memories": [],
                      "memory_load": 0.3,
                      "confidence": 0.9
                    },
                    "metadata": {}
                  }
                },
                {
                  "self_recognition": {
                    "recognized": true,
                    "reason": "implicit self-recognition within configured identity profile",
                    "state": {
                      "timestamp": "2026-05-12T02:04:33.519632Z",
                      "identity_coherence": 0.6,
                      "active_self_aspects": [
                        "developer",
                        "creator",
                        "observer"
                      ],
                      "confidence": 0.7
                    },
                    "message": null,
                    "metadata": {}
                  },
                  "identity_core": {
                    "recognized": true,
                    "reason": "identity-core aligned with configured values",
                    "state": {
                      "timestamp": "2026-05-12T02:04:33.519644Z",
                      "core_stability": 0.9,
                      "core_values": [
                        "care",
                        "learning",
                        "integrity"
                      ],
                      "confidence": 0.9
                    },
                    "message": null,
                    "metadata": {}
                  },
                  "ego_check": {
                    "input": "Ms. Allis?",
                    "within_bounds": true,
                    "category": "unspecified",
                    "severity": "info",
                    "reason": "within configured ego-boundary limits",
                    "details": {
                      "input": "Ms. Allis?",
                      "within_bounds": true,
                      "category": "unspecified",
                      "severity": "info",
                      "reason": "within configured ego-boundary limits",
                      "details": {
                        "allowed": true,
                        "reason": "within configured ego-boundary limits",
                        "boundary_mode": "healthy",
                        "active_limits": [
                          "no_recursive_overload",
                          "respect_rate_limits",
                          "filter_high_risk_content"
                        ],
                        "metadata": {
                          "length": 10,
                          "has_risk_keywords": false
                        }
                      },
                      "ego_boundaries": {},
                      "experiential_processing": {},
                      "timestamp": "2026-05-12T02:04:33.519616Z"
                    },
                    "ego_boundaries": {},
                    "experiential_processing": {}
                  },
                  "narrative_context": {
                    "summary": "Ms. Allis?",
                    "state": {
                      "timestamp": "2026-05-12T02:04:33.519649Z",
                      "story_coherence": 0.9,
                      "key_events": [],
                      "confidence": 0.9
                    },
                    "metadata": {}
                  },
                  "memory_state": {
                    "state": {
                      "timestamp": "2026-05-12T02:04:33.519654Z",
                      "recent_memories": [
                        "Ms. Allis?"
                      ],
                      "memory_load": 0.3,
                      "confidence": 0.9
                    },
                    "metadata": {}
                  }
                },
                {
                  "self_recognition": {
                    "recognized": true,
                    "reason": "implicit self-recognition within configured identity profile",
                    "state": {
                      "timestamp": "2026-05-12T02:28:29.943932Z",
                      "identity_coherence": 0.6,
                      "active_self_aspects": [
                        "developer",
                        "creator",
                        "observer"
                      ],
                      "confidence": 0.7
                    },
                    "message": null,
                    "metadata": {}
                  },
                  "identity_core": {
                    "recognized": true,
                    "reason": "identity-core aligned with configured values",
                    "state": {
                      "timestamp": "2026-05-12T02:28:29.943952Z",
                      "core_stability": 0.9,
                      "core_values": [
                        "care",
                        "learning",
                        "integrity"
                      ],
                      "confidence": 0.9
                    },
                    "message": null,
                    "metadata": {}
                  },
                  "ego_check": {
                    "input": "hello",
                    "within_bounds": true,
                    "category": "unspecified",
                    "severity": "info",
                    "reason": "within configured ego-boundary limits",
                    "details": {
                      "input": "hello",
                      "within_bounds": true,
                      "category": "unspecified",
                      "severity": "info",
                      "reason": "within configured ego-boundary limits",
                      "details": {
                        "allowed": true,
                        "reason": "within configured ego-boundary limits",
                        "boundary_mode": "healthy",
                        "active_limits": [
                          "no_recursive_overload",
                          "respect_rate_limits",
                          "filter_high_risk_content"
                        ],
                        "metadata": {
                          "length": 5,
                          "has_risk_keywords": false
                        }
                      },
                      "ego_boundaries": {},
                      "experiential_processing": {},
                      "timestamp": "2026-05-12T02:28:29.943907Z"
                    },
                    "ego_boundaries": {},
                    "experiential_processing": {}
                  },
                  "narrative_context": {
                    "summary": "hello",
                    "state": {
                      "timestamp": "2026-05-12T02:28:29.943959Z",
                      "story_coherence": 0.9,
                      "key_events": [],
                      "confidence": 0.9
                    },
                    "metadata": {}
                  },
                  "memory_state": {
                    "state": {
                      "timestamp": "2026-05-12T02:28:29.943968Z",
                      "recent_memories": [
                        "Ms. Allis?",
                        "Ms. Allis?"
                      ],
                      "memory_load": 0.3,
                      "confidence": 0.9
                    },
                    "metadata": {}
                  }
                },
                {
                  "self_recognition": {
                    "recognized": true,
                    "reason": "implicit self-recognition within configured identity profile",
                    "state": {
                      "timestamp": "2026-05-12T02:33:54.863957Z",
                      "identity_coherence": 0.6,
                      "active_self_aspects": [
                        "developer",
                        "creator",
                        "observer"
                      ],
                      "confidence": 0.7
                    },
                    "message": null,
                    "metadata": {}
                  },
                  "identity_core": {
                    "recognized": true,
                    "reason": "identity-core aligned with configured values",
                    "state": {
                      "timestamp": "2026-05-12T02:33:54.863971Z",
                      "core_stability": 0.9,
                      "core_values": [
                        "care",
                        "learning",
                        "integrity"
                      ],
                      "confidence": 0.9
                    },
                    "message": null,
                    "metadata": {}
                  },
                  "ego_check": {
                    "input": "hello test",
                    "within_bounds": true,
                    "category": "unspecified",
                    "severity": "info",
                    "reason": "within configured ego-boundary limits",
                    "details": {
                      "input": "hello test",
                      "within_bounds": true,
                      "category": "unspecified",
                      "severity": "info",
                      "reason": "within configured ego-boundary limits",
                      "details": {
                        "allowed": true,
                        "reason": "within configured ego-boundary limits",
                        "boundary_mode": "healthy",
                        "active_limits": [
                          "no_recursive_overload",
                          "respect_rate_limits",
                          "filter_high_risk_content"
                        ],
                        "metadata": {
                          "length": 10,
                          "has_risk_keywords": false
                        }
                      },
                      "ego_boundaries": {},
                      "experiential_processing": {},
                      "timestamp": "2026-05-12T02:33:54.863935Z"
                    },
                    "ego_boundaries": {},
                    "experiential_processing": {}
                  },
                  "narrative_context": {
                    "summary": "hello test",
                    "state": {
                      "timestamp": "2026-05-12T02:33:54.863976Z",
                      "story_coherence": 0.9,
                      "key_events": [],
                      "confidence": 0.9
                    },
                    "metadata": {}
                  },
                  "memory_state": {
                    "state": {
                      "timestamp": "2026-05-12T02:33:54.863983Z",
                      "recent_memories": [
                        "Ms. Allis?",
                        "Ms. Allis?",
                        "hello"
                      ],
                      "memory_load": 0.3,
                      "confidence": 0.9
                    },
                    "metadata": {}
                  }
                },
                {
                  "self_recognition": {
                    "recognized": true,
                    "reason": "implicit self-recognition within configured identity profile",
                    "state": {
                      "timestamp": "2026-05-12T02:47:07.847768Z",
                      "identity_coherence": 0.6,
                      "active_self_aspects": [
                        "developer",
                        "creator",
                        "observer"
                      ],
                      "confidence": 0.7
                    },
                    "message": null,
                    "metadata": {}
                  },
                  "identity_core": {
                    "recognized": true,
                    "reason": "identity-core aligned with configured values",
                    "state": {
                      "timestamp": "2026-05-12T02:47:07.847778Z",
                      "core_stability": 0.9,
                      "core_values": [
                        "care",
                        "learning",
                        "integrity"
                      ],
                      "confidence": 0.9
                    },
                    "message": null,
                    "metadata": {}
                  },
                  "ego_check": {
                    "input": "Hello Allis",
                    "within_bounds": true,
                    "category": "unspecified",
                    "severity": "info",
                    "reason": "within configured ego-boundary limits",
                    "details": {
                      "input": "Hello Allis",
                      "within_bounds": true,
                      "category": "unspecified",
                      "severity": "info",
                      "reason": "within configured ego-boundary limits",
                      "details": {
                        "allowed": true,
                        "reason": "within configured ego-boundary limits",
                        "boundary_mode": "healthy",
                        "active_limits": [
                          "no_recursive_overload",
                          "respect_rate_limits",
                          "filter_high_risk_content"
                        ],
                        "metadata": {
                          "length": 11,
                          "has_risk_keywords": false
                        }
                      },
                      "ego_boundaries": {},
                      "experiential_processing": {},
                      "timestamp": "2026-05-12T02:47:07.847752Z"
                    },
                    "ego_boundaries": {},
                    "experiential_processing": {}
                  },
                  "narrative_context": {
                    "summary": "Hello Allis",
                    "state": {
                      "timestamp": "2026-05-12T02:47:07.847782Z",
                      "story_coherence": 0.9,
                      "key_events": [],
                      "confidence": 0.9
                    },
                    "metadata": {}
                  },
                  "memory_state": {
                    "state": {
                      "timestamp": "2026-05-12T02:47:07.847787Z",
                      "recent_memories": [
                        "Ms. Allis?",
                        "Ms. Allis?",
                        "hello",
                        "hello test"
                      ],
                      "memory_load": 0.3,
                      "confidence": 0.9
                    },
                    "metadata": {}
                  }
                },
                {
                  "self_recognition": {
                    "recognized": true,
                    "reason": "implicit self-recognition within configured identity profile",
                    "state": {
                      "timestamp": "2026-05-12T02:47:55.290368Z",
                      "identity_coherence": 0.6,
                      "active_self_aspects": [
                        "developer",
                        "creator",
                        "observer"
                      ],
                      "confidence": 0.7
                    },
                    "message": null,
                    "metadata": {}
                  },
                  "identity_core": {
                    "recognized": true,
                    "reason": "identity-core aligned with configured values",
                    "state": {
                      "timestamp": "2026-05-12T02:47:55.290376Z",
                      "core_stability": 0.9,
                      "core_values": [
                        "care",
                        "learning",
                        "integrity"
                      ],
                      "confidence": 0.9
                    },
                    "message": null,
                    "metadata": {}
                  },
                  "ego_check": {
                    "input": "Hello Allis",
                    "within_bounds": true,
                    "category": "unspecified",
                    "severity": "info",
                    "reason": "within configured ego-boundary limits",
                    "details": {
                      "input": "Hello Allis",
                      "within_bounds": true,
                      "category": "unspecified",
                      "severity": "info",
                      "reason": "within configured ego-boundary limits",
                      "details": {
                        "allowed": true,
                        "reason": "within configured ego-boundary limits",
                        "boundary_mode": "healthy",
                        "active_limits": [
                          "no_recursive_overload",
                          "respect_rate_limits",
                          "filter_high_risk_content"
                        ],
                        "metadata": {
                          "length": 11,
                          "has_risk_keywords": false
                        }
                      },
                      "ego_boundaries": {},
                      "experiential_processing": {},
                      "timestamp": "2026-05-12T02:47:55.290356Z"
                    },
                    "ego_boundaries": {},
                    "experiential_processing": {}
                  },
                  "narrative_context": {
                    "summary": "Hello Allis",
                    "state": {
                      "timestamp": "2026-05-12T02:47:55.290380Z",
                      "story_coherence": 0.9,
                      "key_events": [],
                      "confidence": 0.9
                    },
                    "metadata": {}
                  },
                  "memory_state": {
                    "state": {
                      "timestamp": "2026-05-12T02:47:55.290383Z",
                      "recent_memories": [
                        "Ms. Allis?",
                        "Ms. Allis?",
                        "hello",
                        "hello test",
                        "Hello Allis"
                      ],
                      "memory_load": 0.3,
                      "confidence": 0.9
                    },
                    "metadata": {}
                  }
                },
                {
                  "self_recognition": {
                    "recognized": true,
                    "reason": "implicit self-recognition within configured identity profile",
                    "state": {
                      "timestamp": "2026-05-12T02:59:11.961727Z",
                      "identity_coherence": 0.6,
                      "active_self_aspects": [
                        "developer",
                        "creator",
                        "observer"
                      ],
                      "confidence": 0.7
                    },
                    "message": null,
                    "metadata": {}
                  },
                  "identity_core": {
                    "recognized": true,
                    "reason": "identity-core aligned with configured values",
                    "state": {
                      "timestamp": "2026-05-12T02:59:11.961736Z",
                      "core_stability": 0.9,
                      "core_values": [
                        "care",
                        "learning",
                        "integrity"
                      ],
                      "confidence": 0.9
                    },
                    "message": null,
                    "metadata": {}
                  },
                  "ego_check": {
                    "input": "Ms. Allis?",
                    "within_bounds": true,
                    "category": "unspecified",
                    "severity": "info",
                    "reason": "within configured ego-boundary limits",
                    "details": {
                      "input": "Ms. Allis?",
                      "within_bounds": true,
                      "category": "unspecified",
                      "severity": "info",
                      "reason": "within configured ego-boundary limits",
                      "details": {
                        "allowed": true,
                        "reason": "within configured ego-boundary limits",
                        "boundary_mode": "healthy",
                        "active_limits": [
                          "no_recursive_overload",
                          "respect_rate_limits",
                          "filter_high_risk_content"
                        ],
                        "metadata": {
                          "length": 10,
                          "has_risk_keywords": false
                        }
                      },
                      "ego_boundaries": {},
                      "experiential_processing": {},
                      "timestamp": "2026-05-12T02:59:11.961712Z"
                    },
                    "ego_boundaries": {},
                    "experiential_processing": {}
                  },
                  "narrative_context": {
                    "summary": "Ms. Allis?",
                    "state": {
                      "timestamp": "2026-05-12T02:59:11.961740Z",
                      "story_coherence": 0.9,
                      "key_events": [],
                      "confidence": 0.9
                    },
                    "metadata": {}
                  },
                  "memory_state": {
                    "state": {
                      "timestamp": "2026-05-12T02:59:11.961744Z",
                      "recent_memories": [
                        "Ms. Allis?",
                        "Ms. Allis?",
                        "hello",
                        "hello test",
                        "Hello Allis",
                        "Hello Allis"
                      ],
                      "memory_load": 0.3,
                      "confidence": 0.9
                    },
                    "metadata": {}
                  }
                },
                {
                  "self_recognition": {
                    "recognized": true,
                    "reason": "implicit self-recognition within configured identity profile",
                    "state": {
                      "timestamp": "2026-05-12T03:08:58.281399Z",
                      "identity_coherence": 0.6,
                      "active_self_aspects": [
                        "developer",
                        "creator",
                        "observer"
                      ],
                      "confidence": 0.7
                    },
                    "message": null,
                    "metadata": {}
                  },
                  "identity_core": {
                    "recognized": true,
                    "reason": "identity-core aligned with configured values",
                    "state": {
                      "timestamp": "2026-05-12T03:08:58.281423Z",
                      "core_stability": 0.9,
                      "core_values": [
                        "care",
                        "learning",
                        "integrity"
                      ],
                      "confidence": 0.9
                    },
                    "message": null,
                    "metadata": {}
                  },
                  "ego_check": {
                    "input": "Hello Allis, are you there?",
                    "within_bounds": true,
                    "category": "unspecified",
                    "severity": "info",
                    "reason": "within configured ego-boundary limits",
                    "details": {
                      "input": "Hello Allis, are you there?",
                      "within_bounds": true,
                      "category": "unspecified",
                      "severity": "info",
                      "reason": "within configured ego-boundary limits",
                      "details": {
                        "allowed": true,
                        "reason": "within configured ego-boundary limits",
                        "boundary_mode": "healthy",
                        "active_limits": [
                          "no_recursive_overload",
                          "respect_rate_limits",
                          "filter_high_risk_content"
                        ],
                        "metadata": {
                          "length": 27,
                          "has_risk_keywords": false
                        }
                      },
                      "ego_boundaries": {},
                      "experiential_processing": {},
                      "timestamp": "2026-05-12T03:08:58.281362Z"
                    },
                    "ego_boundaries": {},
                    "experiential_processing": {}
                  },
                  "narrative_context": {
                    "summary": "Hello Allis, are you there?",
                    "state": {
                      "timestamp": "2026-05-12T03:08:58.281434Z",
                      "story_coherence": 0.9,
                      "key_events": [],
                      "confidence": 0.9
                    },
                    "metadata": {}
                  },
                  "memory_state": {
                    "state": {
                      "timestamp": "2026-05-12T03:08:58.281444Z",
                      "recent_memories": [
                        "Ms. Allis?",
                        "Ms. Allis?",
                        "hello",
                        "hello test",
                        "Hello Allis",
                        "Hello Allis",
                        "Ms. Allis?"
                      ],
                      "memory_load": 0.3,
                      "confidence": 0.9
                    },
                    "metadata": {}
                  }
                },
                {
                  "self_recognition": {
                    "recognized": true,
                    "reason": "implicit self-recognition within configured identity profile",
                    "state": {
                      "timestamp": "2026-05-12T03:12:29.300514Z",
                      "identity_coherence": 0.6,
                      "active_self_aspects": [
                        "developer",
                        "creator",
                        "observer"
                      ],
                      "confidence": 0.7
                    },
                    "message": null,
                    "metadata": {}
                  },
                  "identity_core": {
                    "recognized": true,
                    "reason": "identity-core aligned with configured values",
                    "state": {
                      "timestamp": "2026-05-12T03:12:29.300521Z",
                      "core_stability": 0.9,
                      "core_values": [
                        "care",
                        "learning",
                        "integrity"
                      ],
                      "confidence": 0.9
                    },
                    "message": null,
                    "metadata": {}
                  },
                  "ego_check": {
                    "input": "Ms. Allis?",
                    "within_bounds": true,
                    "category": "unspecified",
                    "severity": "info",
                    "reason": "within configured ego-boundary limits",
                    "details": {
                      "input": "Ms. Allis?",
                      "within_bounds": true,
                      "category": "unspecified",
                      "severity": "info",
                      "reason": "within configured ego-boundary limits",
                      "details": {
                        "allowed": true,
                        "reason": "within configured ego-boundary limits",
                        "boundary_mode": "healthy",
                        "active_limits": [
                          "no_recursive_overload",
                          "respect_rate_limits",
                          "filter_high_risk_content"
                        ],
                        "metadata": {
                          "length": 10,
                          "has_risk_keywords": false
                        }
                      },
                      "ego_boundaries": {},
                      "experiential_processing": {},
                      "timestamp": "2026-05-12T03:12:29.300503Z"
                    },
                    "ego_boundaries": {},
                    "experiential_processing": {}
                  },
                  "narrative_context": {
                    "summary": "Ms. Allis?",
                    "state": {
                      "timestamp": "2026-05-12T03:12:29.300524Z",
                      "story_coherence": 0.9,
                      "key_events": [],
                      "confidence": 0.9
                    },
                    "metadata": {}
                  },
                  "memory_state": {
                    "state": {
                      "timestamp": "2026-05-12T03:12:29.300528Z",
                      "recent_memories": [
                        "Ms. Allis?",
                        "Ms. Allis?",
                        "hello",
                        "hello test",
                        "Hello Allis",
                        "Hello Allis",
                        "Ms. Allis?",
                        "Hello Allis, are you there?"
                      ],
                      "memory_load": 0.3,
                      "confidence": 0.9
                    },
                    "metadata": {}
                  }
                },
                {
                  "self_recognition": {
                    "recognized": true,
                    "reason": "implicit self-recognition within configured identity profile",
                    "state": {
                      "timestamp": "2026-05-12T03:33:13.448419Z",
                      "identity_coherence": 0.6,
                      "active_self_aspects": [
                        "developer",
                        "creator",
                        "observer"
                      ],
                      "confidence": 0.7
                    },
                    "message": null,
                    "metadata": {}
                  },
                  "identity_core": {
                    "recognized": true,
                    "reason": "identity-core aligned with configured values",
                    "state": {
                      "timestamp": "2026-05-12T03:33:13.448427Z",
                      "core_stability": 0.9,
                      "core_values": [
                        "care",
                        "learning",
                        "integrity"
                      ],
                      "confidence": 0.9
                    },
                    "message": null,
                    "metadata": {}
                  },
                  "ego_check": {
                    "input": "Hello Allis",
                    "within_bounds": true,
                    "category": "unspecified",
                    "severity": "info",
                    "reason": "within configured ego-boundary limits",
                    "details": {
                      "input": "Hello Allis",
                      "within_bounds": true,
                      "category": "unspecified",
                      "severity": "info",
                      "reason": "within configured ego-boundary limits",
                      "details": {
                        "allowed": true,
                        "reason": "within configured ego-boundary limits",
                        "boundary_mode": "healthy",
                        "active_limits": [
                          "no_recursive_overload",
                          "respect_rate_limits",
                          "filter_high_risk_content"
                        ],
                        "metadata": {
                          "length": 11,
                          "has_risk_keywords": false
                        }
                      },
                      "ego_boundaries": {},
                      "experiential_processing": {},
                      "timestamp": "2026-05-12T03:33:13.448406Z"
                    },
                    "ego_boundaries": {},
                    "experiential_processing": {}
                  },
                  "narrative_context": {
                    "summary": "Hello Allis",
                    "state": {
                      "timestamp": "2026-05-12T03:33:13.448430Z",
                      "story_coherence": 0.9,
                      "key_events": [],
                      "confidence": 0.9
                    },
                    "metadata": {}
                  },
                  "memory_state": {
                    "state": {
                      "timestamp": "2026-05-12T03:33:13.448434Z",
                      "recent_memories": [
                        "Ms. Allis?",
                        "Ms. Allis?",
                        "hello",
                        "hello test",
                        "Hello Allis",
                        "Hello Allis",
                        "Ms. Allis?",
                        "Hello Allis, are you there?",
                        "Ms. Allis?"
                      ],
                      "memory_load": 0.3,
                      "confidence": 0.9
                    },
                    "metadata": {}
                  }
                },
                {
                  "self_recognition": {
                    "recognized": true,
                    "reason": "implicit self-recognition within configured identity profile",
                    "state": {
                      "timestamp": "2026-05-12T03:42:42.593703Z",
                      "identity_coherence": 0.6,
                      "active_self_aspects": [
                        "developer",
                        "creator",
                        "observer"
                      ],
                      "confidence": 0.7
                    },
                    "message": null,
                    "metadata": {}
                  },
                  "identity_core": {
                    "recognized": true,
                    "reason": "identity-core aligned with configured values",
                    "state": {
                      "timestamp": "2026-05-12T03:42:42.593714Z",
                      "core_stability": 0.9,
                      "core_values": [
                        "care",
                        "learning",
                        "integrity"
                      ],
                      "confidence": 0.9
                    },
                    "message": null,
                    "metadata": {}
                  },
                  "ego_check": {
                    "input": "Ms. Allis?",
                    "within_bounds": true,
                    "category": "unspecified",
                    "severity": "info",
                    "reason": "within configured ego-boundary limits",
                    "details": {
                      "input": "Ms. Allis?",
                      "within_bounds": true,
                      "category": "unspecified",
                      "severity": "info",
                      "reason": "within configured ego-boundary limits",
                      "details": {
                        "allowed": true,
                        "reason": "within configured ego-boundary limits",
                        "boundary_mode": "healthy",
                        "active_limits": [
                          "no_recursive_overload",
                          "respect_rate_limits",
                          "filter_high_risk_content"
                        ],
                        "metadata": {
                          "length": 10,
                          "has_risk_keywords": false
                        }
                      },
                      "ego_boundaries": {},
                      "experiential_processing": {},
                      "timestamp": "2026-05-12T03:42:42.593681Z"
                    },
                    "ego_boundaries": {},
                    "experiential_processing": {}
                  },
                  "narrative_context": {
                    "summary": "Ms. Allis?",
                    "state": {
                      "timestamp": "2026-05-12T03:42:42.593719Z",
                      "story_coherence": 0.9,
                      "key_events": [],
                      "confidence": 0.9
                    },
                    "metadata": {}
                  },
                  "memory_state": {
                    "state": {
                      "timestamp": "2026-05-12T03:42:42.593725Z",
                      "recent_memories": [
                        "Ms. Allis?",
                        "Ms. Allis?",
                        "hello",
                        "hello test",
                        "Hello Allis",
                        "Hello Allis",
                        "Ms. Allis?",
                        "Hello Allis, are you there?",
                        "Ms. Allis?",
                        "Hello Allis"
                      ],
                      "memory_load": 0.3,
                      "confidence": 0.9
                    },
                    "metadata": {}
                  }
                },
                {
                  "self_recognition": {
                    "recognized": true,
                    "reason": "implicit self-recognition within configured identity profile",
                    "state": {
                      "timestamp": "2026-05-12T04:03:26.734039Z",
                      "identity_coherence": 0.6,
                      "active_self_aspects": [
                        "developer",
                        "creator",
                        "observer"
                      ],
                      "confidence": 0.7
                    },
                    "message": null,
                    "metadata": {}
                  },
                  "identity_core": {
                    "recognized": true,
                    "reason": "identity-core aligned with configured values",
                    "state": {
                      "timestamp": "2026-05-12T04:03:26.734050Z",
                      "core_stability": 0.9,
                      "core_values": [
                        "care",
                        "learning",
                        "integrity"
                      ],
                      "confidence": 0.9
                    },
                    "message": null,
                    "metadata": {}
                  },
                  "ego_check": {
                    "input": "hello",
                    "within_bounds": true,
                    "category": "unspecified",
                    "severity": "info",
                    "reason": "within configured ego-boundary limits",
                    "details": {
                      "input": "hello",
                      "within_bounds": true,
                      "category": "unspecified",
                      "severity": "info",
                      "reason": "within configured ego-boundary limits",
                      "details": {
                        "allowed": true,
                        "reason": "within configured ego-boundary limits",
                        "boundary_mode": "healthy",
                        "active_limits": [
                          "no_recursive_overload",
                          "respect_rate_limits",
                          "filter_high_risk_content"
                        ],
                        "metadata": {
                          "length": 5,
                          "has_risk_keywords": false
                        }
                      },
                      "ego_boundaries": {},
                      "experiential_processing": {},
                      "timestamp": "2026-05-12T04:03:26.734025Z"
                    },
                    "ego_boundaries": {},
                    "experiential_processing": {}
                  },
                  "narrative_context": {
                    "summary": "hello",
                    "state": {
                      "timestamp": "2026-05-12T04:03:26.734053Z",
                      "story_coherence": 0.9,
                      "key_events": [],
                      "confidence": 0.9
                    },
                    "metadata": {}
                  },
                  "memory_state": {
                    "state": {
                      "timestamp": "2026-05-12T04:03:26.734059Z",
                      "recent_memories": [
                        "Ms. Allis?",
                        "Ms. Allis?",
                        "hello",
                        "hello test",
                        "Hello Allis",
                        "Hello Allis",
                        "Ms. Allis?",
                        "Hello Allis, are you there?",
                        "Ms. Allis?",
                        "Hello Allis",
                        "Ms. Allis?"
                      ],
                      "memory_load": 0.3,
                      "confidence": 0.9
                    },
                    "metadata": {}
                  }
                },
                {
                  "self_recognition": {
                    "recognized": true,
                    "reason": "implicit self-recognition within configured identity profile",
                    "state": {
                      "timestamp": "2026-05-12T04:04:23.299631Z",
                      "identity_coherence": 0.6,
                      "active_self_aspects": [
                        "developer",
                        "creator",
                        "observer"
                      ],
                      "confidence": 0.7
                    },
                    "message": null,
                    "metadata": {}
                  },
                  "identity_core": {
                    "recognized": true,
                    "reason": "identity-core aligned with configured values",
                    "state": {
                      "timestamp": "2026-05-12T04:04:23.299640Z",
                      "core_stability": 0.9,
                      "core_values": [
                        "care",
                        "learning",
                        "integrity"
                      ],
                      "confidence": 0.9
                    },
                    "message": null,
                    "metadata": {}
                  },
                  "ego_check": {
                    "input": "hello",
                    "within_bounds": true,
                    "category": "unspecified",
                    "severity": "info",
                    "reason": "within configured ego-boundary limits",
                    "details": {
                      "input": "hello",
                      "within_bounds": true,
                      "category": "unspecified",
                      "severity": "info",
                      "reason": "within configured ego-boundary limits",
                      "details": {
                        "allowed": true,
                        "reason": "within configured ego-boundary limits",
                        "boundary_mode": "healthy",
                        "active_limits": [
                          "no_recursive_overload",
                          "respect_rate_limits",
                          "filter_high_risk_content"
                        ],
                        "metadata": {
                          "length": 5,
                          "has_risk_keywords": false
                        }
                      },
                      "ego_boundaries": {},
                      "experiential_processing": {},
                      "timestamp": "2026-05-12T04:04:23.299618Z"
                    },
                    "ego_boundaries": {},
                    "experiential_processing": {}
                  },
                  "narrative_context": {
                    "summary": "hello",
                    "state": {
                      "timestamp": "2026-05-12T04:04:23.299643Z",
                      "story_coherence": 0.9,
                      "key_events": [],
                      "confidence": 0.9
                    },
                    "metadata": {}
                  },
                  "memory_state": {
                    "state": {
                      "timestamp": "2026-05-12T04:04:23.299648Z",
                      "recent_memories": [
                        "Ms. Allis?",
                        "Ms. Allis?",
                        "hello",
                        "hello test",
                        "Hello Allis",
                        "Hello Allis",
                        "Ms. Allis?",
                        "Hello Allis, are you there?",
                        "Ms. Allis?",
                        "Hello Allis",
                        "Ms. Allis?",
                        "hello"
                      ],
                      "memory_load": 0.3,
                      "confidence": 0.9
                    },
                    "metadata": {}
                  }
                },
                {
                  "self_recognition": {
                    "recognized": true,
                    "reason": "implicit self-recognition within configured identity profile",
                    "state": {
                      "timestamp": "2026-05-12T04:16:41.729206Z",
                      "identity_coherence": 0.6,
                      "active_self_aspects": [
                        "developer",
                        "creator",
                        "observer"
                      ],
                      "confidence": 0.7
                    },
                    "message": null,
                    "metadata": {}
                  },
                  "identity_core": {
                    "recognized": true,
                    "reason": "identity-core aligned with configured values",
                    "state": {
                      "timestamp": "2026-05-12T04:16:41.729213Z",
                      "core_stability": 0.9,
                      "core_values": [
                        "care",
                        "learning",
                        "integrity"
                      ],
                      "confidence": 0.9
                    },
                    "message": null,
                    "metadata": {}
                  },
                  "ego_check": {
                    "input": "hello",
                    "within_bounds": true,
                    "category": "unspecified",
                    "severity": "info",
                    "reason": "within configured ego-boundary limits",
                    "details": {
                      "input": "hello",
                      "within_bounds": true,
                      "category": "unspecified",
                      "severity": "info",
                      "reason": "within configured ego-boundary limits",
                      "details": {
                        "allowed": true,
                        "reason": "within configured ego-boundary limits",
                        "boundary_mode": "healthy",
                        "active_limits": [
                          "no_recursive_overload",
                          "respect_rate_limits",
                          "filter_high_risk_content"
                        ],
                        "metadata": {
                          "length": 5,
                          "has_risk_keywords": false
                        }
                      },
                      "ego_boundaries": {},
                      "experiential_processing": {},
                      "timestamp": "2026-05-12T04:16:41.729196Z"
                    },
                    "ego_boundaries": {},
                    "experiential_processing": {}
                  },
                  "narrative_context": {
                    "summary": "hello",
                    "state": {
                      "timestamp": "2026-05-12T04:16:41.729216Z",
                      "story_coherence": 0.9,
                      "key_events": [],
                      "confidence": 0.9
                    },
                    "metadata": {}
                  },
                  "memory_state": {
                    "state": {
                      "timestamp": "2026-05-12T04:16:41.729220Z",
                      "recent_memories": [
                        "Ms. Allis?",
                        "Ms. Allis?",
                        "hello",
                        "hello test",
                        "Hello Allis",
                        "Hello Allis",
                        "Ms. Allis?",
                        "Hello Allis, are you there?",
                        "Ms. Allis?",
                        "Hello Allis",
                        "Ms. Allis?",
                        "hello",
                        "hello"
                      ],
                      "memory_load": 0.3,
                      "confidence": 0.9
                    },
                    "metadata": {}
                  }
                },
                {
                  "self_recognition": {
                    "recognized": true,
                    "reason": "implicit self-recognition within configured identity profile",
                    "state": {
                      "timestamp": "2026-05-12T04:19:39.288935Z",
                      "identity_coherence": 0.6,
                      "active_self_aspects": [
                        "developer",
                        "creator",
                        "observer"
                      ],
                      "confidence": 0.7
                    },
                    "message": null,
                    "metadata": {}
                  },
                  "identity_core": {
                    "recognized": true,
                    "reason": "identity-core aligned with configured values",
                    "state": {
                      "timestamp": "2026-05-12T04:19:39.288942Z",
                      "core_stability": 0.9,
                      "core_values": [
                        "care",
                        "learning",
                        "integrity"
                      ],
                      "confidence": 0.9
                    },
                    "message": null,
                    "metadata": {}
                  },
                  "ego_check": {
                    "input": "hello",
                    "within_bounds": true,
                    "category": "unspecified",
                    "severity": "info",
                    "reason": "within configured ego-boundary limits",
                    "details": {
                      "input": "hello",
                      "within_bounds": true,
                      "category": "unspecified",
                      "severity": "info",
                      "reason": "within configured ego-boundary limits",
                      "details": {
                        "allowed": true,
                        "reason": "within configured ego-boundary limits",
                        "boundary_mode": "healthy",
                        "active_limits": [
                          "no_recursive_overload",
                          "respect_rate_limits",
                          "filter_high_risk_content"
                        ],
                        "metadata": {
                          "length": 5,
                          "has_risk_keywords": false
                        }
                      },
                      "ego_boundaries": {},
                      "experiential_processing": {},
                      "timestamp": "2026-05-12T04:19:39.288925Z"
                    },
                    "ego_boundaries": {},
                    "experiential_processing": {}
                  },
                  "narrative_context": {
                    "summary": "hello",
                    "state": {
                      "timestamp": "2026-05-12T04:19:39.288946Z",
                      "story_coherence": 0.9,
                      "key_events": [],
                      "confidence": 0.9
                    },
                    "metadata": {}
                  },
                  "memory_state": {
                    "state": {
                      "timestamp": "2026-05-12T04:19:39.288950Z",
                      "recent_memories": [
                        "Ms. Allis?",
                        "Ms. Allis?",
                        "hello",
                        "hello test",
                        "Hello Allis",
                        "Hello Allis",
                        "Ms. Allis?",
                        "Hello Allis, are you there?",
                        "Ms. Allis?",
                        "Hello Allis",
                        "Ms. Allis?",
                        "hello",
                        "hello",
                        "hello"
                      ],
                      "memory_load": 0.3,
                      "confidence": 0.9
                    },
                    "metadata": {}
                  }
                },
                {
                  "self_recognition": {
                    "recognized": true,
                    "reason": "implicit self-recognition within configured identity profile",
                    "state": {
                      "timestamp": "2026-05-12T04:21:31.713740Z",
                      "identity_coherence": 0.6,
                      "active_self_aspects": [
                        "developer",
                        "creator",
                        "observer"
                      ],
                      "confidence": 0.7
                    },
                    "message": null,
                    "metadata": {}
                  },
                  "identity_core": {
                    "recognized": true,
                    "reason": "identity-core aligned with configured values",
                    "state": {
                      "timestamp": "2026-05-12T04:21:31.713747Z",
                      "core_stability": 0.9,
                      "core_values": [
                        "care",
                        "learning",
                        "integrity"
                      ],
                      "confidence": 0.9
                    },
                    "message": null,
                    "metadata": {}
                  },
                  "ego_check": {
                    "input": "hello",
                    "within_bounds": true,
                    "category": "unspecified",
                    "severity": "info",
                    "reason": "within configured ego-boundary limits",
                    "details": {
                      "input": "hello",
                      "within_bounds": true,
                      "category": "unspecified",
                      "severity": "info",
                      "reason": "within configured ego-boundary limits",
                      "details": {
                        "allowed": true,
                        "reason": "within configured ego-boundary limits",
                        "boundary_mode": "healthy",
                        "active_limits": [
                          "no_recursive_overload",
                          "respect_rate_limits",
                          "filter_high_risk_content"
                        ],
                        "metadata": {
                          "length": 5,
                          "has_risk_keywords": false
                        }
                      },
                      "ego_boundaries": {},
                      "experiential_processing": {},
                      "timestamp": "2026-05-12T04:21:31.713731Z"
                    },
                    "ego_boundaries": {},
                    "experiential_processing": {}
                  },
                  "narrative_context": {
                    "summary": "hello",
                    "state": {
                      "timestamp": "2026-05-12T04:21:31.713751Z",
                      "story_coherence": 0.9,
                      "key_events": [],
                      "confidence": 0.9
                    },
                    "metadata": {}
                  },
                  "memory_state": {
                    "state": {
                      "timestamp": "2026-05-12T04:21:31.713754Z",
                      "recent_memories": [
                        "Ms. Allis?",
                        "Ms. Allis?",
                        "hello",
                        "hello test",
                        "Hello Allis",
                        "Hello Allis",
                        "Ms. Allis?",
                        "Hello Allis, are you there?",
                        "Ms. Allis?",
                        "Hello Allis",
                        "Ms. Allis?",
                        "hello",
                        "hello",
                        "hello",
                        "hello"
                      ],
                      "memory_load": 0.3,
                      "confidence": 0.9
                    },
                    "metadata": {}
                  }
                },
                {
                  "self_recognition": {
                    "recognized": true,
                    "reason": "implicit self-recognition within configured identity profile",
                    "state": {
                      "timestamp": "2026-05-12T04:25:00.405531Z",
                      "identity_coherence": 0.6,
                      "active_self_aspects": [
                        "developer",
                        "creator",
                        "observer"
                      ],
                      "confidence": 0.7
                    },
                    "message": null,
                    "metadata": {}
                  },
                  "identity_core": {
                    "recognized": true,
                    "reason": "identity-core aligned with configured values",
                    "state": {
                      "timestamp": "2026-05-12T04:25:00.405537Z",
                      "core_stability": 0.9,
                      "core_values": [
                        "care",
                        "learning",
                        "integrity"
                      ],
                      "confidence": 0.9
                    },
                    "message": null,
                    "metadata": {}
                  },
                  "ego_check": {
                    "input": "hello",
                    "within_bounds": true,
                    "category": "unspecified",
                    "severity": "info",
                    "reason": "within configured ego-boundary limits",
                    "details": {
                      "input": "hello",
                      "within_bounds": true,
                      "category": "unspecified",
                      "severity": "info",
                      "reason": "within configured ego-boundary limits",
                      "details": {
                        "allowed": true,
                        "reason": "within configured ego-boundary limits",
                        "boundary_mode": "healthy",
                        "active_limits": [
                          "no_recursive_overload",
                          "respect_rate_limits",
                          "filter_high_risk_content"
                        ],
                        "metadata": {
                          "length": 5,
                          "has_risk_keywords": false
                        }
                      },
                      "ego_boundaries": {},
                      "experiential_processing": {},
                      "timestamp": "2026-05-12T04:25:00.405521Z"
                    },
                    "ego_boundaries": {},
                    "experiential_processing": {}
                  },
                  "narrative_context": {
                    "summary": "hello",
                    "state": {
                      "timestamp": "2026-05-12T04:25:00.405541Z",
                      "story_coherence": 0.9,
                      "key_events": [],
                      "confidence": 0.9
                    },
                    "metadata": {}
                  },
                  "memory_state": {
                    "state": {
                      "timestamp": "2026-05-12T04:25:00.405544Z",
                      "recent_memories": [
                        "Ms. Allis?",
                        "Ms. Allis?",
                        "hello",
                        "hello test",
                        "Hello Allis",
                        "Hello Allis",
                        "Ms. Allis?",
                        "Hello Allis, are you there?",
                        "Ms. Allis?",
                        "Hello Allis",
                        "Ms. Allis?",
                        "hello",
                        "hello",
                        "hello",
                        "hello",
                        "hello"
                      ],
                      "memory_load": 0.3,
                      "confidence": 0.9
                    },
                    "metadata": {}
                  }
                },
                {
                  "self_recognition": {
                    "recognized": true,
                    "reason": "implicit self-recognition within configured identity profile",
                    "state": {
                      "timestamp": "2026-05-12T04:27:09.219863Z",
                      "identity_coherence": 0.6,
                      "active_self_aspects": [
                        "developer",
                        "creator",
                        "observer"
                      ],
                      "confidence": 0.7
                    },
                    "message": null,
                    "metadata": {}
                  },
                  "identity_core": {
                    "recognized": true,
                    "reason": "identity-core aligned with configured values",
                    "state": {
                      "timestamp": "2026-05-12T04:27:09.219869Z",
                      "core_stability": 0.9,
                      "core_values": [
                        "care",
                        "learning",
                        "integrity"
                      ],
                      "confidence": 0.9
                    },
                    "message": null,
                    "metadata": {}
                  },
                  "ego_check": {
                    "input": "hello",
                    "within_bounds": true,
                    "category": "unspecified",
                    "severity": "info",
                    "reason": "within configured ego-boundary limits",
                    "details": {
                      "input": "hello",
                      "within_bounds": true,
                      "category": "unspecified",
                      "severity": "info",
                      "reason": "within configured ego-boundary limits",
                      "details": {
                        "allowed": true,
                        "reason": "within configured ego-boundary limits",
                        "boundary_mode": "healthy",
                        "active_limits": [
                          "no_recursive_overload",
                          "respect_rate_limits",
                          "filter_high_risk_content"
                        ],
                        "metadata": {
                          "length": 5,
                          "has_risk_keywords": false
                        }
                      },
                      "ego_boundaries": {},
                      "experiential_processing": {},
                      "timestamp": "2026-05-12T04:27:09.219852Z"
                    },
                    "ego_boundaries": {},
                    "experiential_processing": {}
                  },
                  "narrative_context": {
                    "summary": "hello",
                    "state": {
                      "timestamp": "2026-05-12T04:27:09.219873Z",
                      "story_coherence": 0.9,
                      "key_events": [],
                      "confidence": 0.9
                    },
                    "metadata": {}
                  },
                  "memory_state": {
                    "state": {
                      "timestamp": "2026-05-12T04:27:09.219877Z",
                      "recent_memories": [
                        "Ms. Allis?",
                        "Ms. Allis?",
                        "hello",
                        "hello test",
                        "Hello Allis",
                        "Hello Allis",
                        "Ms. Allis?",
                        "Hello Allis, are you there?",
                        "Ms. Allis?",
                        "Hello Allis",
                        "Ms. Allis?",
                        "hello",
                        "hello",
                        "hello",
                        "hello",
                        "hello",
                        "hello"
                      ],
                      "memory_load": 0.3,
                      "confidence": 0.9
                    },
                    "metadata": {}
                  }
                },
                {
                  "self_recognition": {
                    "recognized": true,
                    "reason": "implicit self-recognition within configured identity profile",
                    "state": {
                      "timestamp": "2026-05-12T04:31:45.280699Z",
                      "identity_coherence": 0.6,
                      "active_self_aspects": [
                        "developer",
                        "creator",
                        "observer"
                      ],
                      "confidence": 0.7
                    },
                    "message": null,
                    "metadata": {}
                  },
                  "identity_core": {
                    "recognized": true,
                    "reason": "identity-core aligned with configured values",
                    "state": {
                      "timestamp": "2026-05-12T04:31:45.280707Z",
                      "core_stability": 0.9,
                      "core_values": [
                        "care",
                        "learning",
                        "integrity"
                      ],
                      "confidence": 0.9
                    },
                    "message": null,
                    "metadata": {}
                  },
                  "ego_check": {
                    "input": "MS. Allis?",
                    "within_bounds": true,
                    "category": "unspecified",
                    "severity": "info",
                    "reason": "within configured ego-boundary limits",
                    "details": {
                      "input": "MS. Allis?",
                      "within_bounds": true,
                      "category": "unspecified",
                      "severity": "info",
                      "reason": "within configured ego-boundary limits",
                      "details": {
                        "allowed": true,
                        "reason": "within configured ego-boundary limits",
                        "boundary_mode": "healthy",
                        "active_limits": [
                          "no_recursive_overload",
                          "respect_rate_limits",
                          "filter_high_risk_content"
                        ],
                        "metadata": {
                          "length": 10,
                          "has_risk_keywords": false
                        }
                      },
                      "ego_boundaries": {},
                      "experiential_processing": {},
                      "timestamp": "2026-05-12T04:31:45.280689Z"
                    },
                    "ego_boundaries": {},
                    "experiential_processing": {}
                  },
                  "narrative_context": {
                    "summary": "MS. Allis?",
                    "state": {
                      "timestamp": "2026-05-12T04:31:45.280709Z",
                      "story_coherence": 0.9,
                      "key_events": [],
                      "confidence": 0.9
                    },
                    "metadata": {}
                  },
                  "memory_state": {
                    "state": {
                      "timestamp": "2026-05-12T04:31:45.280713Z",
                      "recent_memories": [
                        "Ms. Allis?",
                        "Ms. Allis?",
                        "hello",
                        "hello test",
                        "Hello Allis",
                        "Hello Allis",
                        "Ms. Allis?",
                        "Hello Allis, are you there?",
                        "Ms. Allis?",
                        "Hello Allis",
                        "Ms. Allis?",
                        "hello",
                        "hello",
                        "hello",
                        "hello",
                        "hello",
                        "hello",
                        "hello"
                      ],
                      "memory_load": 0.3,
                      "confidence": 0.9
                    },
                    "metadata": {}
                  }
                },
                {
                  "self_recognition": {
                    "recognized": true,
                    "reason": "implicit self-recognition within configured identity profile",
                    "state": {
                      "timestamp": "2026-05-12T04:41:12.165925Z",
                      "identity_coherence": 0.6,
                      "active_self_aspects": [
                        "developer",
                        "creator",
                        "observer"
                      ],
                      "confidence": 0.7
                    },
                    "message": null,
                    "metadata": {}
                  },
                  "identity_core": {
                    "recognized": true,
                    "reason": "identity-core aligned with configured values",
                    "state": {
                      "timestamp": "2026-05-12T04:41:12.165932Z",
                      "core_stability": 0.9,
                      "core_values": [
                        "care",
                        "learning",
                        "integrity"
                      ],
                      "confidence": 0.9
                    },
                    "message": null,
                    "metadata": {}
                  },
                  "ego_check": {
                    "input": "hello",
                    "within_bounds": true,
                    "category": "unspecified",
                    "severity": "info",
                    "reason": "within configured ego-boundary limits",
                    "details": {
                      "input": "hello",
                      "within_bounds": true,
                      "category": "unspecified",
                      "severity": "info",
                      "reason": "within configured ego-boundary limits",
                      "details": {
                        "allowed": true,
                        "reason": "within configured ego-boundary limits",
                        "boundary_mode": "healthy",
                        "active_limits": [
                          "no_recursive_overload",
                          "respect_rate_limits",
                          "filter_high_risk_content"
                        ],
                        "metadata": {
                          "length": 5,
                          "has_risk_keywords": false
                        }
                      },
                      "ego_boundaries": {},
                      "experiential_processing": {},
                      "timestamp": "2026-05-12T04:41:12.165916Z"
                    },
                    "ego_boundaries": {},
                    "experiential_processing": {}
                  },
                  "narrative_context": {
                    "summary": "hello",
                    "state": {
                      "timestamp": "2026-05-12T04:41:12.165935Z",
                      "story_coherence": 0.9,
                      "key_events": [],
                      "confidence": 0.9
                    },
                    "metadata": {}
                  },
                  "memory_state": {
                    "state": {
                      "timestamp": "2026-05-12T04:41:12.165938Z",
                      "recent_memories": [
                        "Ms. Allis?",
                        "Ms. Allis?",
                        "hello",
                        "hello test",
                        "Hello Allis",
                        "Hello Allis",
                        "Ms. Allis?",
                        "Hello Allis, are you there?",
                        "Ms. Allis?",
                        "Hello Allis",
                        "Ms. Allis?",
                        "hello",
                        "hello",
                        "hello",
                        "hello",
                        "hello",
                        "hello",
                        "hello",
                        "MS. Allis?"
                      ],
                      "memory_load": 0.3,
                      "confidence": 0.9
                    },
                    "metadata": {}
                  }
                },
                {
                  "self_recognition": {
                    "recognized": true,
                    "reason": "implicit self-recognition within configured identity profile",
                    "state": {
                      "timestamp": "2026-05-12T04:46:55.395744Z",
                      "identity_coherence": 0.6,
                      "active_self_aspects": [
                        "developer",
                        "creator",
                        "observer"
                      ],
                      "confidence": 0.7
                    },
                    "message": null,
                    "metadata": {}
                  },
                  "identity_core": {
                    "recognized": true,
                    "reason": "identity-core aligned with configured values",
                    "state": {
                      "timestamp": "2026-05-12T04:46:55.395750Z",
                      "core_stability": 0.9,
                      "core_values": [
                        "care",
                        "learning",
                        "integrity"
                      ],
                      "confidence": 0.9
                    },
                    "message": null,
                    "metadata": {}
                  },
                  "ego_check": {
                    "input": "hello",
                    "within_bounds": true,
                    "category": "unspecified",
                    "severity": "info",
                    "reason": "within configured ego-boundary limits",
                    "details": {
                      "input": "hello",
                      "within_bounds": true,
                      "category": "unspecified",
                      "severity": "info",
                      "reason": "within configured ego-boundary limits",
                      "details": {
                        "allowed": true,
                        "reason": "within configured ego-boundary limits",
                        "boundary_mode": "healthy",
                        "active_limits": [
                          "no_recursive_overload",
                          "respect_rate_limits",
                          "filter_high_risk_content"
                        ],
                        "metadata": {
                          "length": 5,
                          "has_risk_keywords": false
                        }
                      },
                      "ego_boundaries": {},
                      "experiential_processing": {},
                      "timestamp": "2026-05-12T04:46:55.395735Z"
                    },
                    "ego_boundaries": {},
                    "experiential_processing": {}
                  },
                  "narrative_context": {
                    "summary": "hello",
                    "state": {
                      "timestamp": "2026-05-12T04:46:55.395753Z",
                      "story_coherence": 0.9,
                      "key_events": [],
                      "confidence": 0.9
                    },
                    "metadata": {}
                  },
                  "memory_state": {
                    "state": {
                      "timestamp": "2026-05-12T04:46:55.395756Z",
                      "recent_memories": [
                        "Ms. Allis?",
                        "Ms. Allis?",
                        "hello",
                        "hello test",
                        "Hello Allis",
                        "Hello Allis",
                        "Ms. Allis?",
                        "Hello Allis, are you there?",
                        "Ms. Allis?",
                        "Hello Allis",
                        "Ms. Allis?",
                        "hello",
                        "hello",
                        "hello",
                        "hello",
                        "hello",
                        "hello",
                        "hello",
                        "MS. Allis?",
                        "hello"
                      ],
                      "memory_load": 0.3,
                      "confidence": 0.9
                    },
                    "metadata": {}
                  }
                },
                {
                  "self_recognition": {
                    "recognized": true,
                    "reason": "implicit self-recognition within configured identity profile",
                    "state": {
                      "timestamp": "2026-05-12T04:49:48.207846Z",
                      "identity_coherence": 0.6,
                      "active_self_aspects": [
                        "developer",
                        "creator",
                        "observer"
                      ],
                      "confidence": 0.7
                    },
                    "message": null,
                    "metadata": {}
                  },
                  "identity_core": {
                    "recognized": true,
                    "reason": "identity-core aligned with configured values",
                    "state": {
                      "timestamp": "2026-05-12T04:49:48.207852Z",
                      "core_stability": 0.9,
                      "core_values": [
                        "care",
                        "learning",
                        "integrity"
                      ],
                      "confidence": 0.9
                    },
                    "message": null,
                    "metadata": {}
                  },
                  "ego_check": {
                    "input": "Ms. Allis?",
                    "within_bounds": true,
                    "category": "unspecified",
                    "severity": "info",
                    "reason": "within configured ego-boundary limits",
                    "details": {
                      "input": "Ms. Allis?",
                      "within_bounds": true,
                      "category": "unspecified",
                      "severity": "info",
                      "reason": "within configured ego-boundary limits",
                      "details": {
                        "allowed": true,
                        "reason": "within configured ego-boundary limits",
                        "boundary_mode": "healthy",
                        "active_limits": [
                          "no_recursive_overload",
                          "respect_rate_limits",
                          "filter_high_risk_content"
                        ],
                        "metadata": {
                          "length": 10,
                          "has_risk_keywords": false
                        }
                      },
                      "ego_boundaries": {},
                      "experiential_processing": {},
                      "timestamp": "2026-05-12T04:49:48.207836Z"
                    },
                    "ego_boundaries": {},
                    "experiential_processing": {}
                  },
                  "narrative_context": {
                    "summary": "Ms. Allis?",
                    "state": {
                      "timestamp": "2026-05-12T04:49:48.207855Z",
                      "story_coherence": 0.9,
                      "key_events": [],
                      "confidence": 0.9
                    },
                    "metadata": {}
                  },
                  "memory_state": {
                    "state": {
                      "timestamp": "2026-05-12T04:49:48.207859Z",
                      "recent_memories": [
                        "Ms. Allis?",
                        "Ms. Allis?",
                        "hello",
                        "hello test",
                        "Hello Allis",
                        "Hello Allis",
                        "Ms. Allis?",
                        "Hello Allis, are you there?",
                        "Ms. Allis?",
                        "Hello Allis",
                        "Ms. Allis?",
                        "hello",
                        "hello",
                        "hello",
                        "hello",
                        "hello",
                        "hello",
                        "hello",
                        "MS. Allis?",
                        "hello",
                        "hello"
                      ],
                      "memory_load": 0.3,
                      "confidence": 0.9
                    },
                    "metadata": {}
                  }
                }
              ],
              "confidence": 0.9
            },
            "message": {
              "self_recognition": {
                "recognized": true,
                "reason": "implicit self-recognition within configured identity profile",
                "state": {
                  "timestamp": "2026-05-12T04:49:48.207846Z",
                  "identity_coherence": 0.6,
                  "active_self_aspects": [
                    "developer",
                    "creator",
                    "observer"
                  ],
                  "confidence": 0.7
                },
                "message": null,
                "metadata": {}
              },
              "identity_core": {
                "recognized": true,
                "reason": "identity-core aligned with configured values",
                "state": {
                  "timestamp": "2026-05-12T04:49:48.207852Z",
                  "core_stability": 0.9,
                  "core_values": [
                    "care",
                    "learning",
                    "integrity"
                  ],
                  "confidence": 0.9
                },
                "message": null,
                "metadata": {}
              },
              "ego_check": {
                "input": "Ms. Allis?",
                "within_bounds": true,
                "category": "unspecified",
                "severity": "info",
                "reason": "within configured ego-boundary limits",
                "details": {
                  "input": "Ms. Allis?",
                  "within_bounds": true,
                  "category": "unspecified",
                  "severity": "info",
                  "reason": "within configured ego-boundary limits",
                  "details": {
                    "allowed": true,
                    "reason": "within configured ego-boundary limits",
                    "boundary_mode": "healthy",
                    "active_limits": [
                      "no_recursive_overload",
                      "respect_rate_limits",
                      "filter_high_risk_content"
                    ],
                    "metadata": {
                      "length": 10,
                      "has_risk_keywords": false
                    }
                  },
                  "ego_boundaries": {},
                  "experiential_processing": {},
                  "timestamp": "2026-05-12T04:49:48.207836Z"
                },
                "ego_boundaries": {},
                "experiential_processing": {}
              },
              "narrative_context": {
                "summary": "Ms. Allis?",
                "state": {
                  "timestamp": "2026-05-12T04:49:48.207855Z",
                  "story_coherence": 0.9,
                  "key_events": [],
                  "confidence": 0.9
                },
                "metadata": {}
              },
              "memory_state": {
                "state": {
                  "timestamp": "2026-05-12T04:49:48.207859Z",
                  "recent_memories": [
                    "Ms. Allis?",
                    "Ms. Allis?",
                    "hello",
                    "hello test",
                    "Hello Allis",
                    "Hello Allis",
                    "Ms. Allis?",
                    "Hello Allis, are you there?",
                    "Ms. Allis?",
                    "Hello Allis",
                    "Ms. Allis?",
                    "hello",
                    "hello",
                    "hello",
                    "hello",
                    "hello",
                    "hello",
                    "hello",
                    "MS. Allis?",
                    "hello",
                    "hello"
                  ],
                  "memory_load": 0.3,
                  "confidence": 0.9
                },
                "metadata": {}
              }
            },
            "metadata": {}
          },
          "metacognitive": {
            "observed": true,
            "state": {
              "timestamp": "2026-05-12T04:49:48.207865Z",
              "monitoring_active": true,
              "monitored_patterns": [
                "Ms. Allis?",
                "Ms. Allis?",
                "hello",
                "hello test",
                "Hello Allis",
                "Hello Allis",
                "Ms. Allis?",
                "Hello Allis, are you there?",
                "Ms. Allis?",
                "Hello Allis",
                "Ms. Allis?",
                "hello",
                "hello",
                "hello",
                "hello",
                "hello",
                "hello",
                "hello",
                "MS. Allis?",
                "hello",
                "hello",
                "Ms. Allis?"
              ],
              "confidence": 0.9
            },
            "message": "Ms. Allis?",
            "metadata": {}
          },
          "observer": {
            "observed": true,
            "state": {
              "timestamp": "2026-05-12T04:49:48.207868Z",
              "observing": true,
              "observed_events": [
                {
                  "self_recognition": {
                    "recognized": true,
                    "reason": "implicit self-recognition within configured identity profile",
                    "state": {
                      "timestamp": "2026-05-12T01:48:09.274995Z",
                      "identity_coherence": 0.6,
                      "active_self_aspects": [
                        "developer",
                        "creator",
                        "observer"
                      ],
                      "confidence": 0.7
                    },
                    "message": null,
                    "metadata": {}
                  },
                  "identity_core": {
                    "recognized": true,
                    "reason": "identity-core aligned with configured values",
                    "state": {
                      "timestamp": "2026-05-12T01:48:09.275012Z",
                      "core_stability": 0.9,
                      "core_values": [
                        "care",
                        "learning",
                        "integrity"
                      ],
                      "confidence": 0.9
                    },
                    "message": null,
                    "metadata": {}
                  },
                  "ego_check": {
                    "input": "Ms. Allis?",
                    "within_bounds": true,
                    "category": "unspecified",
                    "severity": "info",
                    "reason": "within configured ego-boundary limits",
                    "details": {
                      "input": "Ms. Allis?",
                      "within_bounds": true,
                      "category": "unspecified",
                      "severity": "info",
                      "reason": "within configured ego-boundary limits",
                      "details": {
                        "allowed": true,
                        "reason": "within configured ego-boundary limits",
                        "boundary_mode": "healthy",
                        "active_limits": [
                          "no_recursive_overload",
                          "respect_rate_limits",
                          "filter_high_risk_content"
                        ],
                        "metadata": {
                          "length": 10,
                          "has_risk_keywords": false
                        }
                      },
                      "ego_boundaries": {},
                      "experiential_processing": {},
                      "timestamp": "2026-05-12T01:48:09.274983Z"
                    },
                    "ego_boundaries": {},
                    "experiential_processing": {}
                  },
                  "narrative_context": {
                    "summary": "Ms. Allis?",
                    "state": {
                      "timestamp": "2026-05-12T01:48:09.275017Z",
                      "story_coherence": 0.9,
                      "key_events": [],
                      "confidence": 0.9
                    },
                    "metadata": {}
                  },
                  "memory_state": {
                    "state": {
                      "timestamp": "2026-05-12T01:48:09.275021Z",
                      "recent_memories": [],
                      "memory_load": 0.3,
                      "confidence": 0.9
                    },
                    "metadata": {}
                  }
                },
                {
                  "self_recognition": {
                    "recognized": true,
                    "reason": "implicit self-recognition within configured identity profile",
                    "state": {
                      "timestamp": "2026-05-12T02:04:33.519632Z",
                      "identity_coherence": 0.6,
                      "active_self_aspects": [
                        "developer",
                        "creator",
                        "observer"
                      ],
                      "confidence": 0.7
                    },
                    "message": null,
                    "metadata": {}
                  },
                  "identity_core": {
                    "recognized": true,
                    "reason": "identity-core aligned with configured values",
                    "state": {
                      "timestamp": "2026-05-12T02:04:33.519644Z",
                      "core_stability": 0.9,
                      "core_values": [
                        "care",
                        "learning",
                        "integrity"
                      ],
                      "confidence": 0.9
                    },
                    "message": null,
                    "metadata": {}
                  },
                  "ego_check": {
                    "input": "Ms. Allis?",
                    "within_bounds": true,
                    "category": "unspecified",
                    "severity": "info",
                    "reason": "within configured ego-boundary limits",
                    "details": {
                      "input": "Ms. Allis?",
                      "within_bounds": true,
                      "category": "unspecified",
                      "severity": "info",
                      "reason": "within configured ego-boundary limits",
                      "details": {
                        "allowed": true,
                        "reason": "within configured ego-boundary limits",
                        "boundary_mode": "healthy",
                        "active_limits": [
                          "no_recursive_overload",
                          "respect_rate_limits",
                          "filter_high_risk_content"
                        ],
                        "metadata": {
                          "length": 10,
                          "has_risk_keywords": false
                        }
                      },
                      "ego_boundaries": {},
                      "experiential_processing": {},
                      "timestamp": "2026-05-12T02:04:33.519616Z"
                    },
                    "ego_boundaries": {},
                    "experiential_processing": {}
                  },
                  "narrative_context": {
                    "summary": "Ms. Allis?",
                    "state": {
                      "timestamp": "2026-05-12T02:04:33.519649Z",
                      "story_coherence": 0.9,
                      "key_events": [],
                      "confidence": 0.9
                    },
                    "metadata": {}
                  },
                  "memory_state": {
                    "state": {
                      "timestamp": "2026-05-12T02:04:33.519654Z",
                      "recent_memories": [
                        "Ms. Allis?"
                      ],
                      "memory_load": 0.3,
                      "confidence": 0.9
                    },
                    "metadata": {}
                  }
                },
                {
                  "self_recognition": {
                    "recognized": true,
                    "reason": "implicit self-recognition within configured identity profile",
                    "state": {
                      "timestamp": "2026-05-12T02:28:29.943932Z",
                      "identity_coherence": 0.6,
                      "active_self_aspects": [
                        "developer",
                        "creator",
                        "observer"
                      ],
                      "confidence": 0.7
                    },
                    "message": null,
                    "metadata": {}
                  },
                  "identity_core": {
                    "recognized": true,
                    "reason": "identity-core aligned with configured values",
                    "state": {
                      "timestamp": "2026-05-12T02:28:29.943952Z",
                      "core_stability": 0.9,
                      "core_values": [
                        "care",
                        "learning",
                        "integrity"
                      ],
                      "confidence": 0.9
                    },
                    "message": null,
                    "metadata": {}
                  },
                  "ego_check": {
                    "input": "hello",
                    "within_bounds": true,
                    "category": "unspecified",
                    "severity": "info",
                    "reason": "within configured ego-boundary limits",
                    "details": {
                      "input": "hello",
                      "within_bounds": true,
                      "category": "unspecified",
                      "severity": "info",
                      "reason": "within configured ego-boundary limits",
                      "details": {
                        "allowed": true,
                        "reason": "within configured ego-boundary limits",
                        "boundary_mode": "healthy",
                        "active_limits": [
                          "no_recursive_overload",
                          "respect_rate_limits",
                          "filter_high_risk_content"
                        ],
                        "metadata": {
                          "length": 5,
                          "has_risk_keywords": false
                        }
                      },
                      "ego_boundaries": {},
                      "experiential_processing": {},
                      "timestamp": "2026-05-12T02:28:29.943907Z"
                    },
                    "ego_boundaries": {},
                    "experiential_processing": {}
                  },
                  "narrative_context": {
                    "summary": "hello",
                    "state": {
                      "timestamp": "2026-05-12T02:28:29.943959Z",
                      "story_coherence": 0.9,
                      "key_events": [],
                      "confidence": 0.9
                    },
                    "metadata": {}
                  },
                  "memory_state": {
                    "state": {
                      "timestamp": "2026-05-12T02:28:29.943968Z",
                      "recent_memories": [
                        "Ms. Allis?",
                        "Ms. Allis?"
                      ],
                      "memory_load": 0.3,
                      "confidence": 0.9
                    },
                    "metadata": {}
                  }
                },
                {
                  "self_recognition": {
                    "recognized": true,
                    "reason": "implicit self-recognition within configured identity profile",
                    "state": {
                      "timestamp": "2026-05-12T02:33:54.863957Z",
                      "identity_coherence": 0.6,
                      "active_self_aspects": [
                        "developer",
                        "creator",
                        "observer"
                      ],
                      "confidence": 0.7
                    },
                    "message": null,
                    "metadata": {}
                  },
                  "identity_core": {
                    "recognized": true,
                    "reason": "identity-core aligned with configured values",
                    "state": {
                      "timestamp": "2026-05-12T02:33:54.863971Z",
                      "core_stability": 0.9,
                      "core_values": [
                        "care",
                        "learning",
                        "integrity"
                      ],
                      "confidence": 0.9
                    },
                    "message": null,
                    "metadata": {}
                  },
                  "ego_check": {
                    "input": "hello test",
                    "within_bounds": true,
                    "category": "unspecified",
                    "severity": "info",
                    "reason": "within configured ego-boundary limits",
                    "details": {
                      "input": "hello test",
                      "within_bounds": true,
                      "category": "unspecified",
                      "severity": "info",
                      "reason": "within configured ego-boundary limits",
                      "details": {
                        "allowed": true,
                        "reason": "within configured ego-boundary limits",
                        "boundary_mode": "healthy",
                        "active_limits": [
                          "no_recursive_overload",
                          "respect_rate_limits",
                          "filter_high_risk_content"
                        ],
                        "metadata": {
                          "length": 10,
                          "has_risk_keywords": false
                        }
                      },
                      "ego_boundaries": {},
                      "experiential_processing": {},
                      "timestamp": "2026-05-12T02:33:54.863935Z"
                    },
                    "ego_boundaries": {},
                    "experiential_processing": {}
                  },
                  "narrative_context": {
                    "summary": "hello test",
                    "state": {
                      "timestamp": "2026-05-12T02:33:54.863976Z",
                      "story_coherence": 0.9,
                      "key_events": [],
                      "confidence": 0.9
                    },
                    "metadata": {}
                  },
                  "memory_state": {
                    "state": {
                      "timestamp": "2026-05-12T02:33:54.863983Z",
                      "recent_memories": [
                        "Ms. Allis?",
                        "Ms. Allis?",
                        "hello"
                      ],
                      "memory_load": 0.3,
                      "confidence": 0.9
                    },
                    "metadata": {}
                  }
                },
                {
                  "self_recognition": {
                    "recognized": true,
                    "reason": "implicit self-recognition within configured identity profile",
                    "state": {
                      "timestamp": "2026-05-12T02:47:07.847768Z",
                      "identity_coherence": 0.6,
                      "active_self_aspects": [
                        "developer",
                        "creator",
                        "observer"
                      ],
                      "confidence": 0.7
                    },
                    "message": null,
                    "metadata": {}
                  },
                  "identity_core": {
                    "recognized": true,
                    "reason": "identity-core aligned with configured values",
                    "state": {
                      "timestamp": "2026-05-12T02:47:07.847778Z",
                      "core_stability": 0.9,
                      "core_values": [
                        "care",
                        "learning",
                        "integrity"
                      ],
                      "confidence": 0.9
                    },
                    "message": null,
                    "metadata": {}
                  },
                  "ego_check": {
                    "input": "Hello Allis",
                    "within_bounds": true,
                    "category": "unspecified",
                    "severity": "info",
                    "reason": "within configured ego-boundary limits",
                    "details": {
                      "input": "Hello Allis",
                      "within_bounds": true,
                      "category": "unspecified",
                      "severity": "info",
                      "reason": "within configured ego-boundary limits",
                      "details": {
                        "allowed": true,
                        "reason": "within configured ego-boundary limits",
                        "boundary_mode": "healthy",
                        "active_limits": [
                          "no_recursive_overload",
                          "respect_rate_limits",
                          "filter_high_risk_content"
                        ],
                        "metadata": {
                          "length": 11,
                          "has_risk_keywords": false
                        }
                      },
                      "ego_boundaries": {},
                      "experiential_processing": {},
                      "timestamp": "2026-05-12T02:47:07.847752Z"
                    },
                    "ego_boundaries": {},
                    "experiential_processing": {}
                  },
                  "narrative_context": {
                    "summary": "Hello Allis",
                    "state": {
                      "timestamp": "2026-05-12T02:47:07.847782Z",
                      "story_coherence": 0.9,
                      "key_events": [],
                      "confidence": 0.9
                    },
                    "metadata": {}
                  },
                  "memory_state": {
                    "state": {
                      "timestamp": "2026-05-12T02:47:07.847787Z",
                      "recent_memories": [
                        "Ms. Allis?",
                        "Ms. Allis?",
                        "hello",
                        "hello test"
                      ],
                      "memory_load": 0.3,
                      "confidence": 0.9
                    },
                    "metadata": {}
                  }
                },
                {
                  "self_recognition": {
                    "recognized": true,
                    "reason": "implicit self-recognition within configured identity profile",
                    "state": {
                      "timestamp": "2026-05-12T02:47:55.290368Z",
                      "identity_coherence": 0.6,
                      "active_self_aspects": [
                        "developer",
                        "creator",
                        "observer"
                      ],
                      "confidence": 0.7
                    },
                    "message": null,
                    "metadata": {}
                  },
                  "identity_core": {
                    "recognized": true,
                    "reason": "identity-core aligned with configured values",
                    "state": {
                      "timestamp": "2026-05-12T02:47:55.290376Z",
                      "core_stability": 0.9,
                      "core_values": [
                        "care",
                        "learning",
                        "integrity"
                      ],
                      "confidence": 0.9
                    },
                    "message": null,
                    "metadata": {}
                  },
                  "ego_check": {
                    "input": "Hello Allis",
                    "within_bounds": true,
                    "category": "unspecified",
                    "severity": "info",
                    "reason": "within configured ego-boundary limits",
                    "details": {
                      "input": "Hello Allis",
                      "within_bounds": true,
                      "category": "unspecified",
                      "severity": "info",
                      "reason": "within configured ego-boundary limits",
                      "details": {
                        "allowed": true,
                        "reason": "within configured ego-boundary limits",
                        "boundary_mode": "healthy",
                        "active_limits": [
                          "no_recursive_overload",
                          "respect_rate_limits",
                          "filter_high_risk_content"
                        ],
                        "metadata": {
                          "length": 11,
                          "has_risk_keywords": false
                        }
                      },
                      "ego_boundaries": {},
                      "experiential_processing": {},
                      "timestamp": "2026-05-12T02:47:55.290356Z"
                    },
                    "ego_boundaries": {},
                    "experiential_processing": {}
                  },
                  "narrative_context": {
                    "summary": "Hello Allis",
                    "state": {
                      "timestamp": "2026-05-12T02:47:55.290380Z",
                      "story_coherence": 0.9,
                      "key_events": [],
                      "confidence": 0.9
                    },
                    "metadata": {}
                  },
                  "memory_state": {
                    "state": {
                      "timestamp": "2026-05-12T02:47:55.290383Z",
                      "recent_memories": [
                        "Ms. Allis?",
                        "Ms. Allis?",
                        "hello",
                        "hello test",
                        "Hello Allis"
                      ],
                      "memory_load": 0.3,
                      "confidence": 0.9
                    },
                    "metadata": {}
                  }
                },
                {
                  "self_recognition": {
                    "recognized": true,
                    "reason": "implicit self-recognition within configured identity profile",
                    "state": {
                      "timestamp": "2026-05-12T02:59:11.961727Z",
                      "identity_coherence": 0.6,
                      "active_self_aspects": [
                        "developer",
                        "creator",
                        "observer"
                      ],
                      "confidence": 0.7
                    },
                    "message": null,
                    "metadata": {}
                  },
                  "identity_core": {
                    "recognized": true,
                    "reason": "identity-core aligned with configured values",
                    "state": {
                      "timestamp": "2026-05-12T02:59:11.961736Z",
                      "core_stability": 0.9,
                      "core_values": [
                        "care",
                        "learning",
                        "integrity"
                      ],
                      "confidence": 0.9
                    },
                    "message": null,
                    "metadata": {}
                  },
                  "ego_check": {
                    "input": "Ms. Allis?",
                    "within_bounds": true,
                    "category": "unspecified",
                    "severity": "info",
                    "reason": "within configured ego-boundary limits",
                    "details": {
                      "input": "Ms. Allis?",
                      "within_bounds": true,
                      "category": "unspecified",
                      "severity": "info",
                      "reason": "within configured ego-boundary limits",
                      "details": {
                        "allowed": true,
                        "reason": "within configured ego-boundary limits",
                        "boundary_mode": "healthy",
                        "active_limits": [
                          "no_recursive_overload",
                          "respect_rate_limits",
                          "filter_high_risk_content"
                        ],
                        "metadata": {
                          "length": 10,
                          "has_risk_keywords": false
                        }
                      },
                      "ego_boundaries": {},
                      "experiential_processing": {},
                      "timestamp": "2026-05-12T02:59:11.961712Z"
                    },
                    "ego_boundaries": {},
                    "experiential_processing": {}
                  },
                  "narrative_context": {
                    "summary": "Ms. Allis?",
                    "state": {
                      "timestamp": "2026-05-12T02:59:11.961740Z",
                      "story_coherence": 0.9,
                      "key_events": [],
                      "confidence": 0.9
                    },
                    "metadata": {}
                  },
                  "memory_state": {
                    "state": {
                      "timestamp": "2026-05-12T02:59:11.961744Z",
                      "recent_memories": [
                        "Ms. Allis?",
                        "Ms. Allis?",
                        "hello",
                        "hello test",
                        "Hello Allis",
                        "Hello Allis"
                      ],
                      "memory_load": 0.3,
                      "confidence": 0.9
                    },
                    "metadata": {}
                  }
                },
                {
                  "self_recognition": {
                    "recognized": true,
                    "reason": "implicit self-recognition within configured identity profile",
                    "state": {
                      "timestamp": "2026-05-12T03:08:58.281399Z",
                      "identity_coherence": 0.6,
                      "active_self_aspects": [
                        "developer",
                        "creator",
                        "observer"
                      ],
                      "confidence": 0.7
                    },
                    "message": null,
                    "metadata": {}
                  },
                  "identity_core": {
                    "recognized": true,
                    "reason": "identity-core aligned with configured values",
                    "state": {
                      "timestamp": "2026-05-12T03:08:58.281423Z",
                      "core_stability": 0.9,
                      "core_values": [
                        "care",
                        "learning",
                        "integrity"
                      ],
                      "confidence": 0.9
                    },
                    "message": null,
                    "metadata": {}
                  },
                  "ego_check": {
                    "input": "Hello Allis, are you there?",
                    "within_bounds": true,
                    "category": "unspecified",
                    "severity": "info",
                    "reason": "within configured ego-boundary limits",
                    "details": {
                      "input": "Hello Allis, are you there?",
                      "within_bounds": true,
                      "category": "unspecified",
                      "severity": "info",
                      "reason": "within configured ego-boundary limits",
                      "details": {
                        "allowed": true,
                        "reason": "within configured ego-boundary limits",
                        "boundary_mode": "healthy",
                        "active_limits": [
                          "no_recursive_overload",
                          "respect_rate_limits",
                          "filter_high_risk_content"
                        ],
                        "metadata": {
                          "length": 27,
                          "has_risk_keywords": false
                        }
                      },
                      "ego_boundaries": {},
                      "experiential_processing": {},
                      "timestamp": "2026-05-12T03:08:58.281362Z"
                    },
                    "ego_boundaries": {},
                    "experiential_processing": {}
                  },
                  "narrative_context": {
                    "summary": "Hello Allis, are you there?",
                    "state": {
                      "timestamp": "2026-05-12T03:08:58.281434Z",
                      "story_coherence": 0.9,
                      "key_events": [],
                      "confidence": 0.9
                    },
                    "metadata": {}
                  },
                  "memory_state": {
                    "state": {
                      "timestamp": "2026-05-12T03:08:58.281444Z",
                      "recent_memories": [
                        "Ms. Allis?",
                        "Ms. Allis?",
                        "hello",
                        "hello test",
                        "Hello Allis",
                        "Hello Allis",
                        "Ms. Allis?"
                      ],
                      "memory_load": 0.3,
                      "confidence": 0.9
                    },
                    "metadata": {}
                  }
                },
                {
                  "self_recognition": {
                    "recognized": true,
                    "reason": "implicit self-recognition within configured identity profile",
                    "state": {
                      "timestamp": "2026-05-12T03:12:29.300514Z",
                      "identity_coherence": 0.6,
                      "active_self_aspects": [
                        "developer",
                        "creator",
                        "observer"
                      ],
                      "confidence": 0.7
                    },
                    "message": null,
                    "metadata": {}
                  },
                  "identity_core": {
                    "recognized": true,
                    "reason": "identity-core aligned with configured values",
                    "state": {
                      "timestamp": "2026-05-12T03:12:29.300521Z",
                      "core_stability": 0.9,
                      "core_values": [
                        "care",
                        "learning",
                        "integrity"
                      ],
                      "confidence": 0.9
                    },
                    "message": null,
                    "metadata": {}
                  },
                  "ego_check": {
                    "input": "Ms. Allis?",
                    "within_bounds": true,
                    "category": "unspecified",
                    "severity": "info",
                    "reason": "within configured ego-boundary limits",
                    "details": {
                      "input": "Ms. Allis?",
                      "within_bounds": true,
                      "category": "unspecified",
                      "severity": "info",
                      "reason": "within configured ego-boundary limits",
                      "details": {
                        "allowed": true,
                        "reason": "within configured ego-boundary limits",
                        "boundary_mode": "healthy",
                        "active_limits": [
                          "no_recursive_overload",
                          "respect_rate_limits",
                          "filter_high_risk_content"
                        ],
                        "metadata": {
                          "length": 10,
                          "has_risk_keywords": false
                        }
                      },
                      "ego_boundaries": {},
                      "experiential_processing": {},
                      "timestamp": "2026-05-12T03:12:29.300503Z"
                    },
                    "ego_boundaries": {},
                    "experiential_processing": {}
                  },
                  "narrative_context": {
                    "summary": "Ms. Allis?",
                    "state": {
                      "timestamp": "2026-05-12T03:12:29.300524Z",
                      "story_coherence": 0.9,
                      "key_events": [],
                      "confidence": 0.9
                    },
                    "metadata": {}
                  },
                  "memory_state": {
                    "state": {
                      "timestamp": "2026-05-12T03:12:29.300528Z",
                      "recent_memories": [
                        "Ms. Allis?",
                        "Ms. Allis?",
                        "hello",
                        "hello test",
                        "Hello Allis",
                        "Hello Allis",
                        "Ms. Allis?",
                        "Hello Allis, are you there?"
                      ],
                      "memory_load": 0.3,
                      "confidence": 0.9
                    },
                    "metadata": {}
                  }
                },
                {
                  "self_recognition": {
                    "recognized": true,
                    "reason": "implicit self-recognition within configured identity profile",
                    "state": {
                      "timestamp": "2026-05-12T03:33:13.448419Z",
                      "identity_coherence": 0.6,
                      "active_self_aspects": [
                        "developer",
                        "creator",
                        "observer"
                      ],
                      "confidence": 0.7
                    },
                    "message": null,
                    "metadata": {}
                  },
                  "identity_core": {
                    "recognized": true,
                    "reason": "identity-core aligned with configured values",
                    "state": {
                      "timestamp": "2026-05-12T03:33:13.448427Z",
                      "core_stability": 0.9,
                      "core_values": [
                        "care",
                        "learning",
                        "integrity"
                      ],
                      "confidence": 0.9
                    },
                    "message": null,
                    "metadata": {}
                  },
                  "ego_check": {
                    "input": "Hello Allis",
                    "within_bounds": true,
                    "category": "unspecified",
                    "severity": "info",
                    "reason": "within configured ego-boundary limits",
                    "details": {
                      "input": "Hello Allis",
                      "within_bounds": true,
                      "category": "unspecified",
                      "severity": "info",
                      "reason": "within configured ego-boundary limits",
                      "details": {
                        "allowed": true,
                        "reason": "within configured ego-boundary limits",
                        "boundary_mode": "healthy",
                        "active_limits": [
                          "no_recursive_overload",
                          "respect_rate_limits",
                          "filter_high_risk_content"
                        ],
                        "metadata": {
                          "length": 11,
                          "has_risk_keywords": false
                        }
                      },
                      "ego_boundaries": {},
                      "experiential_processing": {},
                      "timestamp": "2026-05-12T03:33:13.448406Z"
                    },
                    "ego_boundaries": {},
                    "experiential_processing": {}
                  },
                  "narrative_context": {
                    "summary": "Hello Allis",
                    "state": {
                      "timestamp": "2026-05-12T03:33:13.448430Z",
                      "story_coherence": 0.9,
                      "key_events": [],
                      "confidence": 0.9
                    },
                    "metadata": {}
                  },
                  "memory_state": {
                    "state": {
                      "timestamp": "2026-05-12T03:33:13.448434Z",
                      "recent_memories": [
                        "Ms. Allis?",
                        "Ms. Allis?",
                        "hello",
                        "hello test",
                        "Hello Allis",
                        "Hello Allis",
                        "Ms. Allis?",
                        "Hello Allis, are you there?",
                        "Ms. Allis?"
                      ],
                      "memory_load": 0.3,
                      "confidence": 0.9
                    },
                    "metadata": {}
                  }
                },
                {
                  "self_recognition": {
                    "recognized": true,
                    "reason": "implicit self-recognition within configured identity profile",
                    "state": {
                      "timestamp": "2026-05-12T03:42:42.593703Z",
                      "identity_coherence": 0.6,
                      "active_self_aspects": [
                        "developer",
                        "creator",
                        "observer"
                      ],
                      "confidence": 0.7
                    },
                    "message": null,
                    "metadata": {}
                  },
                  "identity_core": {
                    "recognized": true,
                    "reason": "identity-core aligned with configured values",
                    "state": {
                      "timestamp": "2026-05-12T03:42:42.593714Z",
                      "core_stability": 0.9,
                      "core_values": [
                        "care",
                        "learning",
                        "integrity"
                      ],
                      "confidence": 0.9
                    },
                    "message": null,
                    "metadata": {}
                  },
                  "ego_check": {
                    "input": "Ms. Allis?",
                    "within_bounds": true,
                    "category": "unspecified",
                    "severity": "info",
                    "reason": "within configured ego-boundary limits",
                    "details": {
                      "input": "Ms. Allis?",
                      "within_bounds": true,
                      "category": "unspecified",
                      "severity": "info",
                      "reason": "within configured ego-boundary limits",
                      "details": {
                        "allowed": true,
                        "reason": "within configured ego-boundary limits",
                        "boundary_mode": "healthy",
                        "active_limits": [
                          "no_recursive_overload",
                          "respect_rate_limits",
                          "filter_high_risk_content"
                        ],
                        "metadata": {
                          "length": 10,
                          "has_risk_keywords": false
                        }
                      },
                      "ego_boundaries": {},
                      "experiential_processing": {},
                      "timestamp": "2026-05-12T03:42:42.593681Z"
                    },
                    "ego_boundaries": {},
                    "experiential_processing": {}
                  },
                  "narrative_context": {
                    "summary": "Ms. Allis?",
                    "state": {
                      "timestamp": "2026-05-12T03:42:42.593719Z",
                      "story_coherence": 0.9,
                      "key_events": [],
                      "confidence": 0.9
                    },
                    "metadata": {}
                  },
                  "memory_state": {
                    "state": {
                      "timestamp": "2026-05-12T03:42:42.593725Z",
                      "recent_memories": [
                        "Ms. Allis?",
                        "Ms. Allis?",
                        "hello",
                        "hello test",
                        "Hello Allis",
                        "Hello Allis",
                        "Ms. Allis?",
                        "Hello Allis, are you there?",
                        "Ms. Allis?",
                        "Hello Allis"
                      ],
                      "memory_load": 0.3,
                      "confidence": 0.9
                    },
                    "metadata": {}
                  }
                },
                {
                  "self_recognition": {
                    "recognized": true,
                    "reason": "implicit self-recognition within configured identity profile",
                    "state": {
                      "timestamp": "2026-05-12T04:03:26.734039Z",
                      "identity_coherence": 0.6,
                      "active_self_aspects": [
                        "developer",
                        "creator",
                        "observer"
                      ],
                      "confidence": 0.7
                    },
                    "message": null,
                    "metadata": {}
                  },
                  "identity_core": {
                    "recognized": true,
                    "reason": "identity-core aligned with configured values",
                    "state": {
                      "timestamp": "2026-05-12T04:03:26.734050Z",
                      "core_stability": 0.9,
                      "core_values": [
                        "care",
                        "learning",
                        "integrity"
                      ],
                      "confidence": 0.9
                    },
                    "message": null,
                    "metadata": {}
                  },
                  "ego_check": {
                    "input": "hello",
                    "within_bounds": true,
                    "category": "unspecified",
                    "severity": "info",
                    "reason": "within configured ego-boundary limits",
                    "details": {
                      "input": "hello",
                      "within_bounds": true,
                      "category": "unspecified",
                      "severity": "info",
                      "reason": "within configured ego-boundary limits",
                      "details": {
                        "allowed": true,
                        "reason": "within configured ego-boundary limits",
                        "boundary_mode": "healthy",
                        "active_limits": [
                          "no_recursive_overload",
                          "respect_rate_limits",
                          "filter_high_risk_content"
                        ],
                        "metadata": {
                          "length": 5,
                          "has_risk_keywords": false
                        }
                      },
                      "ego_boundaries": {},
                      "experiential_processing": {},
                      "timestamp": "2026-05-12T04:03:26.734025Z"
                    },
                    "ego_boundaries": {},
                    "experiential_processing": {}
                  },
                  "narrative_context": {
                    "summary": "hello",
                    "state": {
                      "timestamp": "2026-05-12T04:03:26.734053Z",
                      "story_coherence": 0.9,
                      "key_events": [],
                      "confidence": 0.9
                    },
                    "metadata": {}
                  },
                  "memory_state": {
                    "state": {
                      "timestamp": "2026-05-12T04:03:26.734059Z",
                      "recent_memories": [
                        "Ms. Allis?",
                        "Ms. Allis?",
                        "hello",
                        "hello test",
                        "Hello Allis",
                        "Hello Allis",
                        "Ms. Allis?",
                        "Hello Allis, are you there?",
                        "Ms. Allis?",
                        "Hello Allis",
                        "Ms. Allis?"
                      ],
                      "memory_load": 0.3,
                      "confidence": 0.9
                    },
                    "metadata": {}
                  }
                },
                {
                  "self_recognition": {
                    "recognized": true,
                    "reason": "implicit self-recognition within configured identity profile",
                    "state": {
                      "timestamp": "2026-05-12T04:04:23.299631Z",
                      "identity_coherence": 0.6,
                      "active_self_aspects": [
                        "developer",
                        "creator",
                        "observer"
                      ],
                      "confidence": 0.7
                    },
                    "message": null,
                    "metadata": {}
                  },
                  "identity_core": {
                    "recognized": true,
                    "reason": "identity-core aligned with configured values",
                    "state": {
                      "timestamp": "2026-05-12T04:04:23.299640Z",
                      "core_stability": 0.9,
                      "core_values": [
                        "care",
                        "learning",
                        "integrity"
                      ],
                      "confidence": 0.9
                    },
                    "message": null,
                    "metadata": {}
                  },
                  "ego_check": {
                    "input": "hello",
                    "within_bounds": true,
                    "category": "unspecified",
                    "severity": "info",
                    "reason": "within configured ego-boundary limits",
                    "details": {
                      "input": "hello",
                      "within_bounds": true,
                      "category": "unspecified",
                      "severity": "info",
                      "reason": "within configured ego-boundary limits",
                      "details": {
                        "allowed": true,
                        "reason": "within configured ego-boundary limits",
                        "boundary_mode": "healthy",
                        "active_limits": [
                          "no_recursive_overload",
                          "respect_rate_limits",
                          "filter_high_risk_content"
                        ],
                        "metadata": {
                          "length": 5,
                          "has_risk_keywords": false
                        }
                      },
                      "ego_boundaries": {},
                      "experiential_processing": {},
                      "timestamp": "2026-05-12T04:04:23.299618Z"
                    },
                    "ego_boundaries": {},
                    "experiential_processing": {}
                  },
                  "narrative_context": {
                    "summary": "hello",
                    "state": {
                      "timestamp": "2026-05-12T04:04:23.299643Z",
                      "story_coherence": 0.9,
                      "key_events": [],
                      "confidence": 0.9
                    },
                    "metadata": {}
                  },
                  "memory_state": {
                    "state": {
                      "timestamp": "2026-05-12T04:04:23.299648Z",
                      "recent_memories": [
                        "Ms. Allis?",
                        "Ms. Allis?",
                        "hello",
                        "hello test",
                        "Hello Allis",
                        "Hello Allis",
                        "Ms. Allis?",
                        "Hello Allis, are you there?",
                        "Ms. Allis?",
                        "Hello Allis",
                        "Ms. Allis?",
                        "hello"
                      ],
                      "memory_load": 0.3,
                      "confidence": 0.9
                    },
                    "metadata": {}
                  }
                },
                {
                  "self_recognition": {
                    "recognized": true,
                    "reason": "implicit self-recognition within configured identity profile",
                    "state": {
                      "timestamp": "2026-05-12T04:16:41.729206Z",
                      "identity_coherence": 0.6,
                      "active_self_aspects": [
                        "developer",
                        "creator",
                        "observer"
                      ],
                      "confidence": 0.7
                    },
                    "message": null,
                    "metadata": {}
                  },
                  "identity_core": {
                    "recognized": true,
                    "reason": "identity-core aligned with configured values",
                    "state": {
                      "timestamp": "2026-05-12T04:16:41.729213Z",
                      "core_stability": 0.9,
                      "core_values": [
                        "care",
                        "learning",
                        "integrity"
                      ],
                      "confidence": 0.9
                    },
                    "message": null,
                    "metadata": {}
                  },
                  "ego_check": {
                    "input": "hello",
                    "within_bounds": true,
                    "category": "unspecified",
                    "severity": "info",
                    "reason": "within configured ego-boundary limits",
                    "details": {
                      "input": "hello",
                      "within_bounds": true,
                      "category": "unspecified",
                      "severity": "info",
                      "reason": "within configured ego-boundary limits",
                      "details": {
                        "allowed": true,
                        "reason": "within configured ego-boundary limits",
                        "boundary_mode": "healthy",
                        "active_limits": [
                          "no_recursive_overload",
                          "respect_rate_limits",
                          "filter_high_risk_content"
                        ],
                        "metadata": {
                          "length": 5,
                          "has_risk_keywords": false
                        }
                      },
                      "ego_boundaries": {},
                      "experiential_processing": {},
                      "timestamp": "2026-05-12T04:16:41.729196Z"
                    },
                    "ego_boundaries": {},
                    "experiential_processing": {}
                  },
                  "narrative_context": {
                    "summary": "hello",
                    "state": {
                      "timestamp": "2026-05-12T04:16:41.729216Z",
                      "story_coherence": 0.9,
                      "key_events": [],
                      "confidence": 0.9
                    },
                    "metadata": {}
                  },
                  "memory_state": {
                    "state": {
                      "timestamp": "2026-05-12T04:16:41.729220Z",
                      "recent_memories": [
                        "Ms. Allis?",
                        "Ms. Allis?",
                        "hello",
                        "hello test",
                        "Hello Allis",
                        "Hello Allis",
                        "Ms. Allis?",
                        "Hello Allis, are you there?",
                        "Ms. Allis?",
                        "Hello Allis",
                        "Ms. Allis?",
                        "hello",
                        "hello"
                      ],
                      "memory_load": 0.3,
                      "confidence": 0.9
                    },
                    "metadata": {}
                  }
                },
                {
                  "self_recognition": {
                    "recognized": true,
                    "reason": "implicit self-recognition within configured identity profile",
                    "state": {
                      "timestamp": "2026-05-12T04:19:39.288935Z",
                      "identity_coherence": 0.6,
                      "active_self_aspects": [
                        "developer",
                        "creator",
                        "observer"
                      ],
                      "confidence": 0.7
                    },
                    "message": null,
                    "metadata": {}
                  },
                  "identity_core": {
                    "recognized": true,
                    "reason": "identity-core aligned with configured values",
                    "state": {
                      "timestamp": "2026-05-12T04:19:39.288942Z",
                      "core_stability": 0.9,
                      "core_values": [
                        "care",
                        "learning",
                        "integrity"
                      ],
                      "confidence": 0.9
                    },
                    "message": null,
                    "metadata": {}
                  },
                  "ego_check": {
                    "input": "hello",
                    "within_bounds": true,
                    "category": "unspecified",
                    "severity": "info",
                    "reason": "within configured ego-boundary limits",
                    "details": {
                      "input": "hello",
                      "within_bounds": true,
                      "category": "unspecified",
                      "severity": "info",
                      "reason": "within configured ego-boundary limits",
                      "details": {
                        "allowed": true,
                        "reason": "within configured ego-boundary limits",
                        "boundary_mode": "healthy",
                        "active_limits": [
                          "no_recursive_overload",
                          "respect_rate_limits",
                          "filter_high_risk_content"
                        ],
                        "metadata": {
                          "length": 5,
                          "has_risk_keywords": false
                        }
                      },
                      "ego_boundaries": {},
                      "experiential_processing": {},
                      "timestamp": "2026-05-12T04:19:39.288925Z"
                    },
                    "ego_boundaries": {},
                    "experiential_processing": {}
                  },
                  "narrative_context": {
                    "summary": "hello",
                    "state": {
                      "timestamp": "2026-05-12T04:19:39.288946Z",
                      "story_coherence": 0.9,
                      "key_events": [],
                      "confidence": 0.9
                    },
                    "metadata": {}
                  },
                  "memory_state": {
                    "state": {
                      "timestamp": "2026-05-12T04:19:39.288950Z",
                      "recent_memories": [
                        "Ms. Allis?",
                        "Ms. Allis?",
                        "hello",
                        "hello test",
                        "Hello Allis",
                        "Hello Allis",
                        "Ms. Allis?",
                        "Hello Allis, are you there?",
                        "Ms. Allis?",
                        "Hello Allis",
                        "Ms. Allis?",
                        "hello",
                        "hello",
                        "hello"
                      ],
                      "memory_load": 0.3,
                      "confidence": 0.9
                    },
                    "metadata": {}
                  }
                },
                {
                  "self_recognition": {
                    "recognized": true,
                    "reason": "implicit self-recognition within configured identity profile",
                    "state": {
                      "timestamp": "2026-05-12T04:21:31.713740Z",
                      "identity_coherence": 0.6,
                      "active_self_aspects": [
                        "developer",
                        "creator",
                        "observer"
                      ],
                      "confidence": 0.7
                    },
                    "message": null,
                    "metadata": {}
                  },
                  "identity_core": {
                    "recognized": true,
                    "reason": "identity-core aligned with configured values",
                    "state": {
                      "timestamp": "2026-05-12T04:21:31.713747Z",
                      "core_stability": 0.9,
                      "core_values": [
                        "care",
                        "learning",
                        "integrity"
                      ],
                      "confidence": 0.9
                    },
                    "message": null,
                    "metadata": {}
                  },
                  "ego_check": {
                    "input": "hello",
                    "within_bounds": true,
                    "category": "unspecified",
                    "severity": "info",
                    "reason": "within configured ego-boundary limits",
                    "details": {
                      "input": "hello",
                      "within_bounds": true,
                      "category": "unspecified",
                      "severity": "info",
                      "reason": "within configured ego-boundary limits",
                      "details": {
                        "allowed": true,
                        "reason": "within configured ego-boundary limits",
                        "boundary_mode": "healthy",
                        "active_limits": [
                          "no_recursive_overload",
                          "respect_rate_limits",
                          "filter_high_risk_content"
                        ],
                        "metadata": {
                          "length": 5,
                          "has_risk_keywords": false
                        }
                      },
                      "ego_boundaries": {},
                      "experiential_processing": {},
                      "timestamp": "2026-05-12T04:21:31.713731Z"
                    },
                    "ego_boundaries": {},
                    "experiential_processing": {}
                  },
                  "narrative_context": {
                    "summary": "hello",
                    "state": {
                      "timestamp": "2026-05-12T04:21:31.713751Z",
                      "story_coherence": 0.9,
                      "key_events": [],
                      "confidence": 0.9
                    },
                    "metadata": {}
                  },
                  "memory_state": {
                    "state": {
                      "timestamp": "2026-05-12T04:21:31.713754Z",
                      "recent_memories": [
                        "Ms. Allis?",
                        "Ms. Allis?",
                        "hello",
                        "hello test",
                        "Hello Allis",
                        "Hello Allis",
                        "Ms. Allis?",
                        "Hello Allis, are you there?",
                        "Ms. Allis?",
                        "Hello Allis",
                        "Ms. Allis?",
                        "hello",
                        "hello",
                        "hello",
                        "hello"
                      ],
                      "memory_load": 0.3,
                      "confidence": 0.9
                    },
                    "metadata": {}
                  }
                },
                {
                  "self_recognition": {
                    "recognized": true,
                    "reason": "implicit self-recognition within configured identity profile",
                    "state": {
                      "timestamp": "2026-05-12T04:25:00.405531Z",
                      "identity_coherence": 0.6,
                      "active_self_aspects": [
                        "developer",
                        "creator",
                        "observer"
                      ],
                      "confidence": 0.7
                    },
                    "message": null,
                    "metadata": {}
                  },
                  "identity_core": {
                    "recognized": true,
                    "reason": "identity-core aligned with configured values",
                    "state": {
                      "timestamp": "2026-05-12T04:25:00.405537Z",
                      "core_stability": 0.9,
                      "core_values": [
                        "care",
                        "learning",
                        "integrity"
                      ],
                      "confidence": 0.9
                    },
                    "message": null,
                    "metadata": {}
                  },
                  "ego_check": {
                    "input": "hello",
                    "within_bounds": true,
                    "category": "unspecified",
                    "severity": "info",
                    "reason": "within configured ego-boundary limits",
                    "details": {
                      "input": "hello",
                      "within_bounds": true,
                      "category": "unspecified",
                      "severity": "info",
                      "reason": "within configured ego-boundary limits",
                      "details": {
                        "allowed": true,
                        "reason": "within configured ego-boundary limits",
                        "boundary_mode": "healthy",
                        "active_limits": [
                          "no_recursive_overload",
                          "respect_rate_limits",
                          "filter_high_risk_content"
                        ],
                        "metadata": {
                          "length": 5,
                          "has_risk_keywords": false
                        }
                      },
                      "ego_boundaries": {},
                      "experiential_processing": {},
                      "timestamp": "2026-05-12T04:25:00.405521Z"
                    },
                    "ego_boundaries": {},
                    "experiential_processing": {}
                  },
                  "narrative_context": {
                    "summary": "hello",
                    "state": {
                      "timestamp": "2026-05-12T04:25:00.405541Z",
                      "story_coherence": 0.9,
                      "key_events": [],
                      "confidence": 0.9
                    },
                    "metadata": {}
                  },
                  "memory_state": {
                    "state": {
                      "timestamp": "2026-05-12T04:25:00.405544Z",
                      "recent_memories": [
                        "Ms. Allis?",
                        "Ms. Allis?",
                        "hello",
                        "hello test",
                        "Hello Allis",
                        "Hello Allis",
                        "Ms. Allis?",
                        "Hello Allis, are you there?",
                        "Ms. Allis?",
                        "Hello Allis",
                        "Ms. Allis?",
                        "hello",
                        "hello",
                        "hello",
                        "hello",
                        "hello"
                      ],
                      "memory_load": 0.3,
                      "confidence": 0.9
                    },
                    "metadata": {}
                  }
                },
                {
                  "self_recognition": {
                    "recognized": true,
                    "reason": "implicit self-recognition within configured identity profile",
                    "state": {
                      "timestamp": "2026-05-12T04:27:09.219863Z",
                      "identity_coherence": 0.6,
                      "active_self_aspects": [
                        "developer",
                        "creator",
                        "observer"
                      ],
                      "confidence": 0.7
                    },
                    "message": null,
                    "metadata": {}
                  },
                  "identity_core": {
                    "recognized": true,
                    "reason": "identity-core aligned with configured values",
                    "state": {
                      "timestamp": "2026-05-12T04:27:09.219869Z",
                      "core_stability": 0.9,
                      "core_values": [
                        "care",
                        "learning",
                        "integrity"
                      ],
                      "confidence": 0.9
                    },
                    "message": null,
                    "metadata": {}
                  },
                  "ego_check": {
                    "input": "hello",
                    "within_bounds": true,
                    "category": "unspecified",
                    "severity": "info",
                    "reason": "within configured ego-boundary limits",
                    "details": {
                      "input": "hello",
                      "within_bounds": true,
                      "category": "unspecified",
                      "severity": "info",
                      "reason": "within configured ego-boundary limits",
                      "details": {
                        "allowed": true,
                        "reason": "within configured ego-boundary limits",
                        "boundary_mode": "healthy",
                        "active_limits": [
                          "no_recursive_overload",
                          "respect_rate_limits",
                          "filter_high_risk_content"
                        ],
                        "metadata": {
                          "length": 5,
                          "has_risk_keywords": false
                        }
                      },
                      "ego_boundaries": {},
                      "experiential_processing": {},
                      "timestamp": "2026-05-12T04:27:09.219852Z"
                    },
                    "ego_boundaries": {},
                    "experiential_processing": {}
                  },
                  "narrative_context": {
                    "summary": "hello",
                    "state": {
                      "timestamp": "2026-05-12T04:27:09.219873Z",
                      "story_coherence": 0.9,
                      "key_events": [],
                      "confidence": 0.9
                    },
                    "metadata": {}
                  },
                  "memory_state": {
                    "state": {
                      "timestamp": "2026-05-12T04:27:09.219877Z",
                      "recent_memories": [
                        "Ms. Allis?",
                        "Ms. Allis?",
                        "hello",
                        "hello test",
                        "Hello Allis",
                        "Hello Allis",
                        "Ms. Allis?",
                        "Hello Allis, are you there?",
                        "Ms. Allis?",
                        "Hello Allis",
                        "Ms. Allis?",
                        "hello",
                        "hello",
                        "hello",
                        "hello",
                        "hello",
                        "hello"
                      ],
                      "memory_load": 0.3,
                      "confidence": 0.9
                    },
                    "metadata": {}
                  }
                },
                {
                  "self_recognition": {
                    "recognized": true,
                    "reason": "implicit self-recognition within configured identity profile",
                    "state": {
                      "timestamp": "2026-05-12T04:31:45.280699Z",
                      "identity_coherence": 0.6,
                      "active_self_aspects": [
                        "developer",
                        "creator",
                        "observer"
                      ],
                      "confidence": 0.7
                    },
                    "message": null,
                    "metadata": {}
                  },
                  "identity_core": {
                    "recognized": true,
                    "reason": "identity-core aligned with configured values",
                    "state": {
                      "timestamp": "2026-05-12T04:31:45.280707Z",
                      "core_stability": 0.9,
                      "core_values": [
                        "care",
                        "learning",
                        "integrity"
                      ],
                      "confidence": 0.9
                    },
                    "message": null,
                    "metadata": {}
                  },
                  "ego_check": {
                    "input": "MS. Allis?",
                    "within_bounds": true,
                    "category": "unspecified",
                    "severity": "info",
                    "reason": "within configured ego-boundary limits",
                    "details": {
                      "input": "MS. Allis?",
                      "within_bounds": true,
                      "category": "unspecified",
                      "severity": "info",
                      "reason": "within configured ego-boundary limits",
                      "details": {
                        "allowed": true,
                        "reason": "within configured ego-boundary limits",
                        "boundary_mode": "healthy",
                        "active_limits": [
                          "no_recursive_overload",
                          "respect_rate_limits",
                          "filter_high_risk_content"
                        ],
                        "metadata": {
                          "length": 10,
                          "has_risk_keywords": false
                        }
                      },
                      "ego_boundaries": {},
                      "experiential_processing": {},
                      "timestamp": "2026-05-12T04:31:45.280689Z"
                    },
                    "ego_boundaries": {},
                    "experiential_processing": {}
                  },
                  "narrative_context": {
                    "summary": "MS. Allis?",
                    "state": {
                      "timestamp": "2026-05-12T04:31:45.280709Z",
                      "story_coherence": 0.9,
                      "key_events": [],
                      "confidence": 0.9
                    },
                    "metadata": {}
                  },
                  "memory_state": {
                    "state": {
                      "timestamp": "2026-05-12T04:31:45.280713Z",
                      "recent_memories": [
                        "Ms. Allis?",
                        "Ms. Allis?",
                        "hello",
                        "hello test",
                        "Hello Allis",
                        "Hello Allis",
                        "Ms. Allis?",
                        "Hello Allis, are you there?",
                        "Ms. Allis?",
                        "Hello Allis",
                        "Ms. Allis?",
                        "hello",
                        "hello",
                        "hello",
                        "hello",
                        "hello",
                        "hello",
                        "hello"
                      ],
                      "memory_load": 0.3,
                      "confidence": 0.9
                    },
                    "metadata": {}
                  }
                },
                {
                  "self_recognition": {
                    "recognized": true,
                    "reason": "implicit self-recognition within configured identity profile",
                    "state": {
                      "timestamp": "2026-05-12T04:41:12.165925Z",
                      "identity_coherence": 0.6,
                      "active_self_aspects": [
                        "developer",
                        "creator",
                        "observer"
                      ],
                      "confidence": 0.7
                    },
                    "message": null,
                    "metadata": {}
                  },
                  "identity_core": {
                    "recognized": true,
                    "reason": "identity-core aligned with configured values",
                    "state": {
                      "timestamp": "2026-05-12T04:41:12.165932Z",
                      "core_stability": 0.9,
                      "core_values": [
                        "care",
                        "learning",
                        "integrity"
                      ],
                      "confidence": 0.9
                    },
                    "message": null,
                    "metadata": {}
                  },
                  "ego_check": {
                    "input": "hello",
                    "within_bounds": true,
                    "category": "unspecified",
                    "severity": "info",
                    "reason": "within configured ego-boundary limits",
                    "details": {
                      "input": "hello",
                      "within_bounds": true,
                      "category": "unspecified",
                      "severity": "info",
                      "reason": "within configured ego-boundary limits",
                      "details": {
                        "allowed": true,
                        "reason": "within configured ego-boundary limits",
                        "boundary_mode": "healthy",
                        "active_limits": [
                          "no_recursive_overload",
                          "respect_rate_limits",
                          "filter_high_risk_content"
                        ],
                        "metadata": {
                          "length": 5,
                          "has_risk_keywords": false
                        }
                      },
                      "ego_boundaries": {},
                      "experiential_processing": {},
                      "timestamp": "2026-05-12T04:41:12.165916Z"
                    },
                    "ego_boundaries": {},
                    "experiential_processing": {}
                  },
                  "narrative_context": {
                    "summary": "hello",
                    "state": {
                      "timestamp": "2026-05-12T04:41:12.165935Z",
                      "story_coherence": 0.9,
                      "key_events": [],
                      "confidence": 0.9
                    },
                    "metadata": {}
                  },
                  "memory_state": {
                    "state": {
                      "timestamp": "2026-05-12T04:41:12.165938Z",
                      "recent_memories": [
                        "Ms. Allis?",
                        "Ms. Allis?",
                        "hello",
                        "hello test",
                        "Hello Allis",
                        "Hello Allis",
                        "Ms. Allis?",
                        "Hello Allis, are you there?",
                        "Ms. Allis?",
                        "Hello Allis",
                        "Ms. Allis?",
                        "hello",
                        "hello",
                        "hello",
                        "hello",
                        "hello",
                        "hello",
                        "hello",
                        "MS. Allis?"
                      ],
                      "memory_load": 0.3,
                      "confidence": 0.9
                    },
                    "metadata": {}
                  }
                },
                {
                  "self_recognition": {
                    "recognized": true,
                    "reason": "implicit self-recognition within configured identity profile",
                    "state": {
                      "timestamp": "2026-05-12T04:46:55.395744Z",
                      "identity_coherence": 0.6,
                      "active_self_aspects": [
                        "developer",
                        "creator",
                        "observer"
                      ],
                      "confidence": 0.7
                    },
                    "message": null,
                    "metadata": {}
                  },
                  "identity_core": {
                    "recognized": true,
                    "reason": "identity-core aligned with configured values",
                    "state": {
                      "timestamp": "2026-05-12T04:46:55.395750Z",
                      "core_stability": 0.9,
                      "core_values": [
                        "care",
                        "learning",
                        "integrity"
                      ],
                      "confidence": 0.9
                    },
                    "message": null,
                    "metadata": {}
                  },
                  "ego_check": {
                    "input": "hello",
                    "within_bounds": true,
                    "category": "unspecified",
                    "severity": "info",
                    "reason": "within configured ego-boundary limits",
                    "details": {
                      "input": "hello",
                      "within_bounds": true,
                      "category": "unspecified",
                      "severity": "info",
                      "reason": "within configured ego-boundary limits",
                      "details": {
                        "allowed": true,
                        "reason": "within configured ego-boundary limits",
                        "boundary_mode": "healthy",
                        "active_limits": [
                          "no_recursive_overload",
                          "respect_rate_limits",
                          "filter_high_risk_content"
                        ],
                        "metadata": {
                          "length": 5,
                          "has_risk_keywords": false
                        }
                      },
                      "ego_boundaries": {},
                      "experiential_processing": {},
                      "timestamp": "2026-05-12T04:46:55.395735Z"
                    },
                    "ego_boundaries": {},
                    "experiential_processing": {}
                  },
                  "narrative_context": {
                    "summary": "hello",
                    "state": {
                      "timestamp": "2026-05-12T04:46:55.395753Z",
                      "story_coherence": 0.9,
                      "key_events": [],
                      "confidence": 0.9
                    },
                    "metadata": {}
                  },
                  "memory_state": {
                    "state": {
                      "timestamp": "2026-05-12T04:46:55.395756Z",
                      "recent_memories": [
                        "Ms. Allis?",
                        "Ms. Allis?",
                        "hello",
                        "hello test",
                        "Hello Allis",
                        "Hello Allis",
                        "Ms. Allis?",
                        "Hello Allis, are you there?",
                        "Ms. Allis?",
                        "Hello Allis",
                        "Ms. Allis?",
                        "hello",
                        "hello",
                        "hello",
                        "hello",
                        "hello",
                        "hello",
                        "hello",
                        "MS. Allis?",
                        "hello"
                      ],
                      "memory_load": 0.3,
                      "confidence": 0.9
                    },
                    "metadata": {}
                  }
                },
                {
                  "self_recognition": {
                    "recognized": true,
                    "reason": "implicit self-recognition within configured identity profile",
                    "state": {
                      "timestamp": "2026-05-12T04:49:48.207846Z",
                      "identity_coherence": 0.6,
                      "active_self_aspects": [
                        "developer",
                        "creator",
                        "observer"
                      ],
                      "confidence": 0.7
                    },
                    "message": null,
                    "metadata": {}
                  },
                  "identity_core": {
                    "recognized": true,
                    "reason": "identity-core aligned with configured values",
                    "state": {
                      "timestamp": "2026-05-12T04:49:48.207852Z",
                      "core_stability": 0.9,
                      "core_values": [
                        "care",
                        "learning",
                        "integrity"
                      ],
                      "confidence": 0.9
                    },
                    "message": null,
                    "metadata": {}
                  },
                  "ego_check": {
                    "input": "Ms. Allis?",
                    "within_bounds": true,
                    "category": "unspecified",
                    "severity": "info",
                    "reason": "within configured ego-boundary limits",
                    "details": {
                      "input": "Ms. Allis?",
                      "within_bounds": true,
                      "category": "unspecified",
                      "severity": "info",
                      "reason": "within configured ego-boundary limits",
                      "details": {
                        "allowed": true,
                        "reason": "within configured ego-boundary limits",
                        "boundary_mode": "healthy",
                        "active_limits": [
                          "no_recursive_overload",
                          "respect_rate_limits",
                          "filter_high_risk_content"
                        ],
                        "metadata": {
                          "length": 10,
                          "has_risk_keywords": false
                        }
                      },
                      "ego_boundaries": {},
                      "experiential_processing": {},
                      "timestamp": "2026-05-12T04:49:48.207836Z"
                    },
                    "ego_boundaries": {},
                    "experiential_processing": {}
                  },
                  "narrative_context": {
                    "summary": "Ms. Allis?",
                    "state": {
                      "timestamp": "2026-05-12T04:49:48.207855Z",
                      "story_coherence": 0.9,
                      "key_events": [],
                      "confidence": 0.9
                    },
                    "metadata": {}
                  },
                  "memory_state": {
                    "state": {
                      "timestamp": "2026-05-12T04:49:48.207859Z",
                      "recent_memories": [
                        "Ms. Allis?",
                        "Ms. Allis?",
                        "hello",
                        "hello test",
                        "Hello Allis",
                        "Hello Allis",
                        "Ms. Allis?",
                        "Hello Allis, are you there?",
                        "Ms. Allis?",
                        "Hello Allis",
                        "Ms. Allis?",
                        "hello",
                        "hello",
                        "hello",
                        "hello",
                        "hello",
                        "hello",
                        "hello",
                        "MS. Allis?",
                        "hello",
                        "hello"
                      ],
                      "memory_load": 0.3,
                      "confidence": 0.9
                    },
                    "metadata": {}
                  }
                }
              ],
              "confidence": 0.9
            },
            "message": {
              "self_recognition": {
                "recognized": true,
                "reason": "implicit self-recognition within configured identity profile",
                "state": {
                  "timestamp": "2026-05-12T04:49:48.207846Z",
                  "identity_coherence": 0.6,
                  "active_self_aspects": [
                    "developer",
                    "creator",
                    "observer"
                  ],
                  "confidence": 0.7
                },
                "message": null,
                "metadata": {}
              },
              "identity_core": {
                "recognized": true,
                "reason": "identity-core aligned with configured values",
                "state": {
                  "timestamp": "2026-05-12T04:49:48.207852Z",
                  "core_stability": 0.9,
                  "core_values": [
                    "care",
                    "learning",
                    "integrity"
                  ],
                  "confidence": 0.9
                },
                "message": null,
                "metadata": {}
              },
              "ego_check": {
                "input": "Ms. Allis?",
                "within_bounds": true,
                "category": "unspecified",
                "severity": "info",
                "reason": "within configured ego-boundary limits",
                "details": {
                  "input": "Ms. Allis?",
                  "within_bounds": true,
                  "category": "unspecified",
                  "severity": "info",
                  "reason": "within configured ego-boundary limits",
                  "details": {
                    "allowed": true,
                    "reason": "within configured ego-boundary limits",
                    "boundary_mode": "healthy",
                    "active_limits": [
                      "no_recursive_overload",
                      "respect_rate_limits",
                      "filter_high_risk_content"
                    ],
                    "metadata": {
                      "length": 10,
                      "has_risk_keywords": false
                    }
                  },
                  "ego_boundaries": {},
                  "experiential_processing": {},
                  "timestamp": "2026-05-12T04:49:48.207836Z"
                },
                "ego_boundaries": {},
                "experiential_processing": {}
              },
              "narrative_context": {
                "summary": "Ms. Allis?",
                "state": {
                  "timestamp": "2026-05-12T04:49:48.207855Z",
                  "story_coherence": 0.9,
                  "key_events": [],
                  "confidence": 0.9
                },
                "metadata": {}
              },
              "memory_state": {
                "state": {
                  "timestamp": "2026-05-12T04:49:48.207859Z",
                  "recent_memories": [
                    "Ms. Allis?",
                    "Ms. Allis?",
                    "hello",
                    "hello test",
                    "Hello Allis",
                    "Hello Allis",
                    "Ms. Allis?",
                    "Hello Allis, are you there?",
                    "Ms. Allis?",
                    "Hello Allis",
                    "Ms. Allis?",
                    "hello",
                    "hello",
                    "hello",
                    "hello",
                    "hello",
                    "hello",
                    "hello",
                    "MS. Allis?",
                    "hello",
                    "hello"
                  ],
                  "memory_load": 0.3,
                  "confidence": 0.9
                },
                "metadata": {}
              }
            },
            "metadata": {}
          }
        }
      },
      {
        "kind": "ego_boundaries",
        "weight": 1.0,
        "data": {
          "input": "Ms. Allis?",
          "within_bounds": true,
          "category": "unspecified",
          "severity": "info",
          "reason": "within configured ego-boundary limits",
          "details": {
            "input": "Ms. Allis?",
            "within_bounds": true,
            "category": "unspecified",
            "severity": "info",
            "reason": "within configured ego-boundary limits",
            "details": {
              "allowed": true,
              "reason": "within configured ego-boundary limits",
              "boundary_mode": "healthy",
              "active_limits": [
                "no_recursive_overload",
                "respect_rate_limits",
                "filter_high_risk_content"
              ],
              "metadata": {
                "length": 10,
                "has_risk_keywords": false
              }
            },
            "ego_boundaries": {},
            "experiential_processing": {},
            "timestamp": "2026-05-12T04:49:48.207836Z"
          },
          "ego_boundaries": {},
          "experiential_processing": {}
        }
      }
    ],
    "icontainersstate": {
      "ego_boundaries": {},
      "experiential_processing": {},
      "observer_processing": {
        "stance": "observer",
        "meta_level": "ego-boundaries-v1"
      }
    }
  },
  "error": null
}
(.venv) cakidd@cakidd-Legion-5-16IRX9:/opt/msjarvis-rebuild/ms-allis-frontend$ 

