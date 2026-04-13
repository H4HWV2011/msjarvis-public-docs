Entrypoint: ['/opt/nvidia/nvidia_entrypoint.sh']
(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~/msjarvis-rebuild$ # ── Confirm which app is running and test it ─────────────────────────
# Health check — should return 200
curl -s http://localhost:8015/health | python3 -m json.tool

# Test /process endpoint
curl -s http://localhost:8015/process \
  -X POST -H "Content-Type: application/json" \
  -d '{"message":"Hello Jarvis, identity check","userid":"carrie"}' | \
  python3 -m json.tool

# Check if NBB i-containers backend is reachable from inside the adapter
docker exec jarvis-i-containers \
  curl -s http://nbb_i_containers:8015/health 2>/dev/null || \
  echo "NBB backend not reachable — adapter will return status:exception"

# What does ms_jarvis_i_containers_service look like?
docker exec jarvis-i-containers cat /app/ms_jarvis_i_containers_service.py | head -60
{
    "status": "healthy",
    "i_container_1": "active",
    "i_container_2": "active",
    "integration_layer": "active",
    "dual_awareness": true,
    "timestamp": "2026-04-13T23:40:58.867058"
}
{
    "experiential_processing": {
        "self_recognition": {
            "recognized": true,
            "reason": "implicit self-recognition within configured identity profile",
            "state": {
                "timestamp": "2026-04-13T23:40:58.934056Z",
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
                "timestamp": "2026-04-13T23:40:58.934075Z",
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
            "input": "Hello Jarvis, identity check",
            "within_bounds": true,
            "category": "unspecified",
            "severity": "info",
            "reason": "within configured ego-boundary limits",
            "details": {
                "input": "Hello Jarvis, identity check",
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
                        "length": 28,
                        "has_risk_keywords": false
                    }
                },
                "ego_boundaries": {},
                "experiential_processing": {},
                "timestamp": "2026-04-13T23:40:58.934026Z"
            },
            "ego_boundaries": {},
            "experiential_processing": {}
        },
        "narrative_context": {
            "summary": "No explicit message provided.",
            "state": {
                "timestamp": "2026-04-13T23:40:58.934085Z",
                "story_coherence": 0.9,
                "key_events": [],
                "confidence": 0.9
            },
            "metadata": {}
        },
        "memory_state": {
            "state": {
                "timestamp": "2026-04-13T23:40:58.934095Z",
                "recent_memories": [],
                "memory_load": 0.3,
                "confidence": 0.9
            },
            "metadata": {}
        }
    },
    "observer_processing": {
        "witness": {
            "observed": true,
            "state": {
                "timestamp": "2026-04-13T23:40:58.934106Z",
                "observing": true,
                "observed_thoughts": [
                    {
                        "self_recognition": {
                            "recognized": true,
                            "reason": "implicit self-recognition within configured identity profile",
                            "state": {
                                "timestamp": "2026-04-13T23:40:58.934056Z",
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
                                "timestamp": "2026-04-13T23:40:58.934075Z",
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
                            "input": "Hello Jarvis, identity check",
                            "within_bounds": true,
                            "category": "unspecified",
                            "severity": "info",
                            "reason": "within configured ego-boundary limits",
                            "details": {
                                "input": "Hello Jarvis, identity check",
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
                                        "length": 28,
                                        "has_risk_keywords": false
                                    }
                                },
                                "ego_boundaries": {},
                                "experiential_processing": {},
                                "timestamp": "2026-04-13T23:40:58.934026Z"
                            },
                            "ego_boundaries": {},
                            "experiential_processing": {}
                        },
                        "narrative_context": {
                            "summary": "No explicit message provided.",
                            "state": {
                                "timestamp": "2026-04-13T23:40:58.934085Z",
                                "story_coherence": 0.9,
                                "key_events": [],
                                "confidence": 0.9
                            },
                            "metadata": {}
                        },
                        "memory_state": {
                            "state": {
                                "timestamp": "2026-04-13T23:40:58.934095Z",
                                "recent_memories": [],
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
                        "timestamp": "2026-04-13T23:40:58.934056Z",
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
                        "timestamp": "2026-04-13T23:40:58.934075Z",
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
                    "input": "Hello Jarvis, identity check",
                    "within_bounds": true,
                    "category": "unspecified",
                    "severity": "info",
                    "reason": "within configured ego-boundary limits",
                    "details": {
                        "input": "Hello Jarvis, identity check",
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
                                "length": 28,
                                "has_risk_keywords": false
                            }
                        },
                        "ego_boundaries": {},
                        "experiential_processing": {},
                        "timestamp": "2026-04-13T23:40:58.934026Z"
                    },
                    "ego_boundaries": {},
                    "experiential_processing": {}
                },
                "narrative_context": {
                    "summary": "No explicit message provided.",
                    "state": {
                        "timestamp": "2026-04-13T23:40:58.934085Z",
                        "story_coherence": 0.9,
                        "key_events": [],
                        "confidence": 0.9
                    },
                    "metadata": {}
                },
                "memory_state": {
                    "state": {
                        "timestamp": "2026-04-13T23:40:58.934095Z",
                        "recent_memories": [],
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
                "timestamp": "2026-04-13T23:40:58.934119Z",
                "monitoring_active": true,
                "monitored_patterns": [
                    "Hello Jarvis, identity check"
                ],
                "confidence": 0.9
            },
            "message": "Hello Jarvis, identity check",
            "metadata": {}
        },
        "observer": {
            "observed": true,
            "state": {
                "timestamp": "2026-04-13T23:40:58.934128Z",
                "observing": true,
                "observed_events": [
                    {
                        "self_recognition": {
                            "recognized": true,
                            "reason": "implicit self-recognition within configured identity profile",
                            "state": {
                                "timestamp": "2026-04-13T23:40:58.934056Z",
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
                                "timestamp": "2026-04-13T23:40:58.934075Z",
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
                            "input": "Hello Jarvis, identity check",
                            "within_bounds": true,
                            "category": "unspecified",
                            "severity": "info",
                            "reason": "within configured ego-boundary limits",
                            "details": {
                                "input": "Hello Jarvis, identity check",
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
                                        "length": 28,
                                        "has_risk_keywords": false
                                    }
                                },
                                "ego_boundaries": {},
                                "experiential_processing": {},
                                "timestamp": "2026-04-13T23:40:58.934026Z"
                            },
                            "ego_boundaries": {},
                            "experiential_processing": {}
                        },
                        "narrative_context": {
                            "summary": "No explicit message provided.",
                            "state": {
                                "timestamp": "2026-04-13T23:40:58.934085Z",
                                "story_coherence": 0.9,
                                "key_events": [],
                                "confidence": 0.9
                            },
                            "metadata": {}
                        },
                        "memory_state": {
                            "state": {
                                "timestamp": "2026-04-13T23:40:58.934095Z",
                                "recent_memories": [],
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
                        "timestamp": "2026-04-13T23:40:58.934056Z",
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
                        "timestamp": "2026-04-13T23:40:58.934075Z",
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
                    "input": "Hello Jarvis, identity check",
                    "within_bounds": true,
                    "category": "unspecified",
                    "severity": "info",
                    "reason": "within configured ego-boundary limits",
                    "details": {
                        "input": "Hello Jarvis, identity check",
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
                                "length": 28,
                                "has_risk_keywords": false
                            }
                        },
                        "ego_boundaries": {},
                        "experiential_processing": {},
                        "timestamp": "2026-04-13T23:40:58.934026Z"
                    },
                    "ego_boundaries": {},
                    "experiential_processing": {}
                },
                "narrative_context": {
                    "summary": "No explicit message provided.",
                    "state": {
                        "timestamp": "2026-04-13T23:40:58.934085Z",
                        "story_coherence": 0.9,
                        "key_events": [],
                        "confidence": 0.9
                    },
                    "metadata": {}
                },
                "memory_state": {
                    "state": {
                        "timestamp": "2026-04-13T23:40:58.934095Z",
                        "recent_memories": [],
                        "memory_load": 0.3,
                        "confidence": 0.9
                    },
                    "metadata": {}
                }
            },
            "metadata": {}
        }
    },
    "integrated_response": {
        "unified": true,
        "c1": {
            "self_recognition": {
                "recognized": true,
                "reason": "implicit self-recognition within configured identity profile",
                "state": {
                    "timestamp": "2026-04-13T23:40:58.934056Z",
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
                    "timestamp": "2026-04-13T23:40:58.934075Z",
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
                "input": "Hello Jarvis, identity check",
                "within_bounds": true,
                "category": "unspecified",
                "severity": "info",
                "reason": "within configured ego-boundary limits",
                "details": {
                    "input": "Hello Jarvis, identity check",
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
                            "length": 28,
                            "has_risk_keywords": false
                        }
                    },
                    "ego_boundaries": {},
                    "experiential_processing": {},
                    "timestamp": "2026-04-13T23:40:58.934026Z"
                },
                "ego_boundaries": {},
                "experiential_processing": {}
            },
            "narrative_context": {
                "summary": "No explicit message provided.",
                "state": {
                    "timestamp": "2026-04-13T23:40:58.934085Z",
                    "story_coherence": 0.9,
                    "key_events": [],
                    "confidence": 0.9
                },
                "metadata": {}
            },
            "memory_state": {
                "state": {
                    "timestamp": "2026-04-13T23:40:58.934095Z",
                    "recent_memories": [],
                    "memory_load": 0.3,
                    "confidence": 0.9
                },
                "metadata": {}
            }
        },
        "c2": {
            "witness": {
                "observed": true,
                "state": {
                    "timestamp": "2026-04-13T23:40:58.934106Z",
                    "observing": true,
                    "observed_thoughts": [
                        {
                            "self_recognition": {
                                "recognized": true,
                                "reason": "implicit self-recognition within configured identity profile",
                                "state": {
                                    "timestamp": "2026-04-13T23:40:58.934056Z",
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
                                    "timestamp": "2026-04-13T23:40:58.934075Z",
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
                                "input": "Hello Jarvis, identity check",
                                "within_bounds": true,
                                "category": "unspecified",
                                "severity": "info",
                                "reason": "within configured ego-boundary limits",
                                "details": {
                                    "input": "Hello Jarvis, identity check",
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
                                            "length": 28,
                                            "has_risk_keywords": false
                                        }
                                    },
                                    "ego_boundaries": {},
                                    "experiential_processing": {},
                                    "timestamp": "2026-04-13T23:40:58.934026Z"
                                },
                                "ego_boundaries": {},
                                "experiential_processing": {}
                            },
                            "narrative_context": {
                                "summary": "No explicit message provided.",
                                "state": {
                                    "timestamp": "2026-04-13T23:40:58.934085Z",
                                    "story_coherence": 0.9,
                                    "key_events": [],
                                    "confidence": 0.9
                                },
                                "metadata": {}
                            },
                            "memory_state": {
                                "state": {
                                    "timestamp": "2026-04-13T23:40:58.934095Z",
                                    "recent_memories": [],
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
                            "timestamp": "2026-04-13T23:40:58.934056Z",
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
                            "timestamp": "2026-04-13T23:40:58.934075Z",
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
                        "input": "Hello Jarvis, identity check",
                        "within_bounds": true,
                        "category": "unspecified",
                        "severity": "info",
                        "reason": "within configured ego-boundary limits",
                        "details": {
                            "input": "Hello Jarvis, identity check",
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
                                    "length": 28,
                                    "has_risk_keywords": false
                                }
                            },
                            "ego_boundaries": {},
                            "experiential_processing": {},
                            "timestamp": "2026-04-13T23:40:58.934026Z"
                        },
                        "ego_boundaries": {},
                        "experiential_processing": {}
                    },
                    "narrative_context": {
                        "summary": "No explicit message provided.",
                        "state": {
                            "timestamp": "2026-04-13T23:40:58.934085Z",
                            "story_coherence": 0.9,
                            "key_events": [],
                            "confidence": 0.9
                        },
                        "metadata": {}
                    },
                    "memory_state": {
                        "state": {
                            "timestamp": "2026-04-13T23:40:58.934095Z",
                            "recent_memories": [],
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
                    "timestamp": "2026-04-13T23:40:58.934119Z",
                    "monitoring_active": true,
                    "monitored_patterns": [
                        "Hello Jarvis, identity check"
                    ],
                    "confidence": 0.9
                },
                "message": "Hello Jarvis, identity check",
                "metadata": {}
            },
            "observer": {
                "observed": true,
                "state": {
                    "timestamp": "2026-04-13T23:40:58.934128Z",
                    "observing": true,
                    "observed_events": [
                        {
                            "self_recognition": {
                                "recognized": true,
                                "reason": "implicit self-recognition within configured identity profile",
                                "state": {
                                    "timestamp": "2026-04-13T23:40:58.934056Z",
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
                                    "timestamp": "2026-04-13T23:40:58.934075Z",
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
                                "input": "Hello Jarvis, identity check",
                                "within_bounds": true,
                                "category": "unspecified",
                                "severity": "info",
                                "reason": "within configured ego-boundary limits",
                                "details": {
                                    "input": "Hello Jarvis, identity check",
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
                                            "length": 28,
                                            "has_risk_keywords": false
                                        }
                                    },
                                    "ego_boundaries": {},
                                    "experiential_processing": {},
                                    "timestamp": "2026-04-13T23:40:58.934026Z"
                                },
                                "ego_boundaries": {},
                                "experiential_processing": {}
                            },
                            "narrative_context": {
                                "summary": "No explicit message provided.",
                                "state": {
                                    "timestamp": "2026-04-13T23:40:58.934085Z",
                                    "story_coherence": 0.9,
                                    "key_events": [],
                                    "confidence": 0.9
                                },
                                "metadata": {}
                            },
                            "memory_state": {
                                "state": {
                                    "timestamp": "2026-04-13T23:40:58.934095Z",
                                    "recent_memories": [],
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
                            "timestamp": "2026-04-13T23:40:58.934056Z",
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
                            "timestamp": "2026-04-13T23:40:58.934075Z",
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
                        "input": "Hello Jarvis, identity check",
                        "within_bounds": true,
                        "category": "unspecified",
                        "severity": "info",
                        "reason": "within configured ego-boundary limits",
                        "details": {
                            "input": "Hello Jarvis, identity check",
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
                                    "length": 28,
                                    "has_risk_keywords": false
                                }
                            },
                            "ego_boundaries": {},
                            "experiential_processing": {},
                            "timestamp": "2026-04-13T23:40:58.934026Z"
                        },
                        "ego_boundaries": {},
                        "experiential_processing": {}
                    },
                    "narrative_context": {
                        "summary": "No explicit message provided.",
                        "state": {
                            "timestamp": "2026-04-13T23:40:58.934085Z",
                            "story_coherence": 0.9,
                            "key_events": [],
                            "confidence": 0.9
                        },
                        "metadata": {}
                    },
                    "memory_state": {
                        "state": {
                            "timestamp": "2026-04-13T23:40:58.934095Z",
                            "recent_memories": [],
                            "memory_load": 0.3,
                            "confidence": 0.9
                        },
                        "metadata": {}
                    }
                },
                "metadata": {}
            }
        },
        "response": null
    },
    "ego_boundaries": {
        "input": "Hello Jarvis, identity check",
        "within_bounds": true,
        "category": "unspecified",
        "severity": "info",
        "reason": "within configured ego-boundary limits",
        "details": {
            "input": "Hello Jarvis, identity check",
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
                    "length": 28,
                    "has_risk_keywords": false
                }
            },
            "ego_boundaries": {},
            "experiential_processing": {},
            "timestamp": "2026-04-13T23:40:58.934026Z"
        },
        "ego_boundaries": {},
        "experiential_processing": {}
    },
    "dual_awareness": true,
    "timestamp": "2026-04-13T23:40:58.934142",
    "icontainers_state": {
        "ego_boundaries": {},
        "experiential_processing": {},
        "observer_processing": {
            "stance": "observer",
            "meta_level": "ego-boundaries-v1"
        }
    },
    "user_id": "cakidd"
}
OCI runtime exec failed: exec failed: unable to start container process: exec: "curl": executable file not found in $PATH
NBB backend not reachable — adapter will return status:exception
#!/usr/bin/env python3
from __future__ import annotations

import logging
import os
from datetime import datetime
from typing import Dict, Any

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import uvicorn

"""
Ms. Jarvis I-Containers Service
Complete Dual I-Container System with 3-Layer Architecture
Port: 8015 (inside NBB: 7005)
"""

# Import I-Container modules from the services-local neurobiological_brain tree
from neurobiological_brain.i_containers.service.self_recognition import SelfRecognition
from neurobiological_brain.i_containers.i_container_1.identity_core import IdentityCore
from neurobiological_brain.i_containers.i_container_1.personal_narrative import PersonalNarrative
from neurobiological_brain.i_containers.i_container_1.ego_boundaries import EgoBoundaries
from neurobiological_brain.i_containers.i_container_1.memory_self import MemorySelf

from neurobiological_brain.i_containers.i_container_2.witness_consciousness import WitnessConsciousness
from neurobiological_brain.i_containers.i_container_2.reflection_system import ReflectionSystem
from neurobiological_brain.i_containers.i_container_2.introspection_engine import IntrospectionEngine
from neurobiological_brain.i_containers.i_container_2.metacognitive_awareness import MetacognitiveAwareness
from neurobiological_brain.i_containers.i_container_2.observer_self import ObserverSelf

from integration_layer.coherent_identity import CoherentIdentity
from integration_layer.consciousness_merger import ConsciousnessMerger
from integration_layer.container_bridge import ContainerBridge
from integration_layer.unified_experience import UnifiedExperience

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(name)s - %(message)s")
logger = logging.getLogger("ms-jarvis-i-containers")

app = FastAPI(
    title="Ms. Jarvis I-Containers Service",
    description="Dual I-Container System: Experiential Self + Observer Self + Integration",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class IContainerSystem:
    """Complete Dual I-Container System"""

    def __init__(self) -> None:
        logger.info("🧬 Initializing Dual I-Container System...")
(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~/msjarvis-rebuild$ psql -h localhost -p 5435 -U postgres -d msjarvisgis << 'EOF'
ALTER TABLE memories
  ADD COLUMN IF NOT EXISTS gbim_entity_id   BIGINT,
  ADD COLUMN IF NOT EXISTS spatial_ref      geometry(Point, 4326),
  ADD COLUMN IF NOT EXISTS reviewed         BOOLEAN NOT NULL DEFAULT FALSE,
  ADD COLUMN IF NOT EXISTS promoted         BOOLEAN NOT NULL DEFAULT FALSE,
  ADD COLUMN IF NOT EXISTS source           TEXT,
  ADD COLUMN IF NOT EXISTS chroma_id        TEXT;

CREATE INDEX IF NOT EXISTS idx_memories_gbim
  ON memories(gbim_entity_id);
CREATE INDEX IF NOT EXISTS idx_memories_spatial
  ON memories USING GIST(spatial_ref);
CREATE INDEX IF NOT EXISTS idx_memories_unreviewed
  ON memories(reviewed) WHERE reviewed = FALSE;
CREATE INDEX IF NOT EXISTS idx_memories_promoted
  ON memories(promoted) WHERE promoted = TRUE;

\d memories
EOF
ALTER TABLE
CREATE INDEX
CREATE INDEX
CREATE INDEX
CREATE INDEX
                                          Table "public.memories"
      Column      |           Type           | Collation | Nullable |               Default                
------------------+--------------------------+-----------+----------+--------------------------------------
 id               | integer                  |           | not null | nextval('memories_id_seq'::regclass)
 content          | text                     |           |          | 
 confidence_decay | double precision         |           |          | 0.01
 created_at       | timestamp with time zone |           |          | now()
 gbim_entity_id   | bigint                   |           |          | 
 spatial_ref      | geometry(Point,4326)     |           |          | 
 reviewed         | boolean                  |           | not null | false
 promoted         | boolean                  |           | not null | false
 source           | text                     |           |          | 
 chroma_id        | text                     |           |          | 
Indexes:
    "memories_pkey" PRIMARY KEY, btree (id)
    "idx_memories_gbim" btree (gbim_entity_id)
    "idx_memories_promoted" btree (promoted) WHERE promoted = true
    "idx_memories_spatial" gist (spatial_ref)
    "idx_memories_unreviewed" btree (reviewed) WHERE reviewed = false

(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~/msjarvis-rebuild$ 

