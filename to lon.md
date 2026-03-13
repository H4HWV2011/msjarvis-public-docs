cakidd@cakidd-Legion-5-16IRX9:~/msjarvis-rebuild-working/msjarvis-rebuild$ curl -sS http://localhost:8015/health | jq .
curl -sS http://localhost:8015/process \
  -H "Content-Type: application/json" \
  -d '{"message": "Who are you?", "userid": "cakidd"}' | jq .
+ jq .
+ curl -sS http://localhost:8015/health
{
  "status": "healthy",
  "i_container_1": "active",
  "i_container_2": "active",
  "integration_layer": "active",
  "dual_awareness": true,
  "timestamp": "2026-03-13T01:34:00.690552"
}
+ jq .
+ curl -sS http://localhost:8015/process -H 'Content-Type: application/json' -d '{"message": "Who are you?", "userid": "cakidd"}'
{
  "experiential_processing": {
    "self_recognition": {
      "recognized": true,
      "reason": "implicit self-recognition within configured identity profile",
      "state": {
        "timestamp": "2026-03-13T01:34:00.706715Z",
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
        "timestamp": "2026-03-13T01:34:00.706756Z",
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
      "input": "Who are you?",
      "within_bounds": true,
      "category": "unspecified",
      "severity": "info",
      "reason": "within configured ego-boundary limits",
      "details": {
        "input": "Who are you?",
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
            "length": 12,
            "has_risk_keywords": false
          }
        },
        "ego_boundaries": {},
        "experiential_processing": {},
        "timestamp": "2026-03-13T01:34:00.706683Z"
      },
      "ego_boundaries": {},
      "experiential_processing": {}
    },
    "narrative_context": {
      "summary": "No explicit message provided.",
      "state": {
        "timestamp": "2026-03-13T01:34:00.706771Z",
        "story_coherence": 0.9,
        "key_events": [],
        "confidence": 0.9
      },
      "metadata": {}
    },
    "memory_state": {
      "state": {
        "timestamp": "2026-03-13T01:34:00.706785Z",
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
        "timestamp": "2026-03-13T01:34:00.706801Z",
        "observing": true,
        "observed_thoughts": [
          {
            "self_recognition": {
              "recognized": true,
              "reason": "implicit self-recognition within configured identity profile",
              "state": {
                "timestamp": "2026-03-12T20:57:09.019437Z",
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
                "timestamp": "2026-03-12T20:57:09.019446Z",
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
              "input": "Test meaning-oriented path",
              "within_bounds": true,
              "category": "unspecified",
              "severity": "info",
              "reason": "within configured ego-boundary limits",
              "details": {
                "input": "Test meaning-oriented path",
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
                    "length": 26,
                    "has_risk_keywords": false
                  }
                },
                "ego_boundaries": {},
                "experiential_processing": {},
                "timestamp": "2026-03-12T20:57:09.019422Z"
              },
              "ego_boundaries": {},
              "experiential_processing": {}
            },
            "narrative_context": {
              "summary": "No explicit message provided.",
              "state": {
                "timestamp": "2026-03-12T20:57:09.019451Z",
                "story_coherence": 0.9,
                "key_events": [],
                "confidence": 0.9
              },
              "metadata": {}
            },
            "memory_state": {
              "state": {
                "timestamp": "2026-03-12T20:57:09.019456Z",
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
                "timestamp": "2026-03-12T21:01:17.121538Z",
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
                "timestamp": "2026-03-12T21:01:17.121555Z",
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
              "input": "Test meaning-oriented path",
              "within_bounds": true,
              "category": "unspecified",
              "severity": "info",
              "reason": "within configured ego-boundary limits",
              "details": {
                "input": "Test meaning-oriented path",
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
                    "length": 26,
                    "has_risk_keywords": false
                  }
                },
                "ego_boundaries": {},
                "experiential_processing": {},
                "timestamp": "2026-03-12T21:01:17.121517Z"
              },
              "ego_boundaries": {},
              "experiential_processing": {}
            },
            "narrative_context": {
              "summary": "No explicit message provided.",
              "state": {
                "timestamp": "2026-03-12T21:01:17.121564Z",
                "story_coherence": 0.9,
                "key_events": [],
                "confidence": 0.9
              },
              "metadata": {}
            },
            "memory_state": {
              "state": {
                "timestamp": "2026-03-12T21:01:17.121572Z",
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
                "timestamp": "2026-03-12T21:24:09.566342Z",
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
                "timestamp": "2026-03-12T21:24:09.566404Z",
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
              "input": "Quick full-path test",
              "within_bounds": true,
              "category": "unspecified",
              "severity": "info",
              "reason": "within configured ego-boundary limits",
              "details": {
                "input": "Quick full-path test",
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
                    "length": 20,
                    "has_risk_keywords": false
                  }
                },
                "ego_boundaries": {},
                "experiential_processing": {},
                "timestamp": "2026-03-12T21:24:09.565697Z"
              },
              "ego_boundaries": {},
              "experiential_processing": {}
            },
            "narrative_context": {
              "summary": "No explicit message provided.",
              "state": {
                "timestamp": "2026-03-12T21:24:09.566541Z",
                "story_coherence": 0.9,
                "key_events": [],
                "confidence": 0.9
              },
              "metadata": {}
            },
            "memory_state": {
              "state": {
                "timestamp": "2026-03-12T21:24:09.566553Z",
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
                "timestamp": "2026-03-12T21:36:53.730270Z",
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
                "timestamp": "2026-03-12T21:36:53.730278Z",
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
              "input": "Identity and I-Containers test",
              "within_bounds": true,
              "category": "unspecified",
              "severity": "info",
              "reason": "within configured ego-boundary limits",
              "details": {
                "input": "Identity and I-Containers test",
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
                    "length": 30,
                    "has_risk_keywords": false
                  }
                },
                "ego_boundaries": {},
                "experiential_processing": {},
                "timestamp": "2026-03-12T21:36:53.730258Z"
              },
              "ego_boundaries": {},
              "experiential_processing": {}
            },
            "narrative_context": {
              "summary": "No explicit message provided.",
              "state": {
                "timestamp": "2026-03-12T21:36:53.730282Z",
                "story_coherence": 0.9,
                "key_events": [],
                "confidence": 0.9
              },
              "metadata": {}
            },
            "memory_state": {
              "state": {
                "timestamp": "2026-03-12T21:36:53.730286Z",
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
                "timestamp": "2026-03-12T21:50:00.847825Z",
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
                "timestamp": "2026-03-12T21:50:00.847839Z",
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
              "input": "Identity and I-Containers test final",
              "within_bounds": true,
              "category": "unspecified",
              "severity": "info",
              "reason": "within configured ego-boundary limits",
              "details": {
                "input": "Identity and I-Containers test final",
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
                    "length": 36,
                    "has_risk_keywords": false
                  }
                },
                "ego_boundaries": {},
                "experiential_processing": {},
                "timestamp": "2026-03-12T21:50:00.847809Z"
              },
              "ego_boundaries": {},
              "experiential_processing": {}
            },
            "narrative_context": {
              "summary": "No explicit message provided.",
              "state": {
                "timestamp": "2026-03-12T21:50:00.847846Z",
                "story_coherence": 0.9,
                "key_events": [],
                "confidence": 0.9
              },
              "metadata": {}
            },
            "memory_state": {
              "state": {
                "timestamp": "2026-03-12T21:50:00.847853Z",
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
                "timestamp": "2026-03-12T21:56:15.874461Z",
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
                "timestamp": "2026-03-12T21:56:15.874470Z",
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
              "input": "Identity and I-Containers test final",
              "within_bounds": true,
              "category": "unspecified",
              "severity": "info",
              "reason": "within configured ego-boundary limits",
              "details": {
                "input": "Identity and I-Containers test final",
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
                    "length": 36,
                    "has_risk_keywords": false
                  }
                },
                "ego_boundaries": {},
                "experiential_processing": {},
                "timestamp": "2026-03-12T21:56:15.874446Z"
              },
              "ego_boundaries": {},
              "experiential_processing": {}
            },
            "narrative_context": {
              "summary": "No explicit message provided.",
              "state": {
                "timestamp": "2026-03-12T21:56:15.874475Z",
                "story_coherence": 0.9,
                "key_events": [],
                "confidence": 0.9
              },
              "metadata": {}
            },
            "memory_state": {
              "state": {
                "timestamp": "2026-03-12T21:56:15.874480Z",
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
                "timestamp": "2026-03-12T22:03:20.445273Z",
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
                "timestamp": "2026-03-12T22:03:20.445280Z",
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
              "input": "Identity and I-Containers test final",
              "within_bounds": true,
              "category": "unspecified",
              "severity": "info",
              "reason": "within configured ego-boundary limits",
              "details": {
                "input": "Identity and I-Containers test final",
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
                    "length": 36,
                    "has_risk_keywords": false
                  }
                },
                "ego_boundaries": {},
                "experiential_processing": {},
                "timestamp": "2026-03-12T22:03:20.445261Z"
              },
              "ego_boundaries": {},
              "experiential_processing": {}
            },
            "narrative_context": {
              "summary": "No explicit message provided.",
              "state": {
                "timestamp": "2026-03-12T22:03:20.445284Z",
                "story_coherence": 0.9,
                "key_events": [],
                "confidence": 0.9
              },
              "metadata": {}
            },
            "memory_state": {
              "state": {
                "timestamp": "2026-03-12T22:03:20.445288Z",
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
                "timestamp": "2026-03-12T22:13:56.226479Z",
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
                "timestamp": "2026-03-12T22:13:56.226488Z",
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
              "input": "Identity and I-Containers test final",
              "within_bounds": true,
              "category": "unspecified",
              "severity": "info",
              "reason": "within configured ego-boundary limits",
              "details": {
                "input": "Identity and I-Containers test final",
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
                    "length": 36,
                    "has_risk_keywords": false
                  }
                },
                "ego_boundaries": {},
                "experiential_processing": {},
                "timestamp": "2026-03-12T22:13:56.226465Z"
              },
              "ego_boundaries": {},
              "experiential_processing": {}
            },
            "narrative_context": {
              "summary": "No explicit message provided.",
              "state": {
                "timestamp": "2026-03-12T22:13:56.226493Z",
                "story_coherence": 0.9,
                "key_events": [],
                "confidence": 0.9
              },
              "metadata": {}
            },
            "memory_state": {
              "state": {
                "timestamp": "2026-03-12T22:13:56.226498Z",
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
                "timestamp": "2026-03-12T23:50:59.415335Z",
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
                "timestamp": "2026-03-12T23:50:59.415345Z",
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
              "input": "Identity and I-Containers test final",
              "within_bounds": true,
              "category": "unspecified",
              "severity": "info",
              "reason": "within configured ego-boundary limits",
              "details": {
                "input": "Identity and I-Containers test final",
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
                    "length": 36,
                    "has_risk_keywords": false
                  }
                },
                "ego_boundaries": {},
                "experiential_processing": {},
                "timestamp": "2026-03-12T23:50:59.415323Z"
              },
              "ego_boundaries": {},
              "experiential_processing": {}
            },
            "narrative_context": {
              "summary": "No explicit message provided.",
              "state": {
                "timestamp": "2026-03-12T23:50:59.415350Z",
                "story_coherence": 0.9,
                "key_events": [],
                "confidence": 0.9
              },
              "metadata": {}
            },
            "memory_state": {
              "state": {
                "timestamp": "2026-03-12T23:50:59.415355Z",
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
                "timestamp": "2026-03-12T23:50:59.423667Z",
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
                "timestamp": "2026-03-12T23:50:59.423673Z",
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
              "input": "Identity and I-Containers test final",
              "within_bounds": true,
              "category": "unspecified",
              "severity": "info",
              "reason": "within configured ego-boundary limits",
              "details": {
                "input": "Identity and I-Containers test final",
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
                    "length": 36,
                    "has_risk_keywords": false
                  }
                },
                "ego_boundaries": {},
                "experiential_processing": {},
                "timestamp": "2026-03-12T23:50:59.423658Z"
              },
              "ego_boundaries": {},
              "experiential_processing": {}
            },
            "narrative_context": {
              "summary": "No explicit message provided.",
              "state": {
                "timestamp": "2026-03-12T23:50:59.423676Z",
                "story_coherence": 0.9,
                "key_events": [],
                "confidence": 0.9
              },
              "metadata": {}
            },
            "memory_state": {
              "state": {
                "timestamp": "2026-03-12T23:50:59.423680Z",
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
                "timestamp": "2026-03-12T23:57:56.233427Z",
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
                "timestamp": "2026-03-12T23:57:56.233445Z",
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
              "input": "Identity and I-Containers test final",
              "within_bounds": true,
              "category": "unspecified",
              "severity": "info",
              "reason": "within configured ego-boundary limits",
              "details": {
                "input": "Identity and I-Containers test final",
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
                    "length": 36,
                    "has_risk_keywords": false
                  }
                },
                "ego_boundaries": {},
                "experiential_processing": {},
                "timestamp": "2026-03-12T23:57:56.233405Z"
              },
              "ego_boundaries": {},
              "experiential_processing": {}
            },
            "narrative_context": {
              "summary": "No explicit message provided.",
              "state": {
                "timestamp": "2026-03-12T23:57:56.233455Z",
                "story_coherence": 0.9,
                "key_events": [],
                "confidence": 0.9
              },
              "metadata": {}
            },
            "memory_state": {
              "state": {
                "timestamp": "2026-03-12T23:57:56.233465Z",
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
                "timestamp": "2026-03-12T23:57:56.379284Z",
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
                "timestamp": "2026-03-12T23:57:56.379292Z",
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
              "input": "Identity and I-Containers test final",
              "within_bounds": true,
              "category": "unspecified",
              "severity": "info",
              "reason": "within configured ego-boundary limits",
              "details": {
                "input": "Identity and I-Containers test final",
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
                    "length": 36,
                    "has_risk_keywords": false
                  }
                },
                "ego_boundaries": {},
                "experiential_processing": {},
                "timestamp": "2026-03-12T23:57:56.379271Z"
              },
              "ego_boundaries": {},
              "experiential_processing": {}
            },
            "narrative_context": {
              "summary": "No explicit message provided.",
              "state": {
                "timestamp": "2026-03-12T23:57:56.379297Z",
                "story_coherence": 0.9,
                "key_events": [],
                "confidence": 0.9
              },
              "metadata": {}
            },
            "memory_state": {
              "state": {
                "timestamp": "2026-03-12T23:57:56.379301Z",
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
                "timestamp": "2026-03-13T00:34:36.201930Z",
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
                "timestamp": "2026-03-13T00:34:36.201941Z",
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
              "input": "Identity and I-Containers test final",
              "within_bounds": true,
              "category": "unspecified",
              "severity": "info",
              "reason": "within configured ego-boundary limits",
              "details": {
                "input": "Identity and I-Containers test final",
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
                    "length": 36,
                    "has_risk_keywords": false
                  }
                },
                "ego_boundaries": {},
                "experiential_processing": {},
                "timestamp": "2026-03-13T00:34:36.201793Z"
              },
              "ego_boundaries": {},
              "experiential_processing": {}
            },
            "narrative_context": {
              "summary": "No explicit message provided.",
              "state": {
                "timestamp": "2026-03-13T00:34:36.201946Z",
                "story_coherence": 0.9,
                "key_events": [],
                "confidence": 0.9
              },
              "metadata": {}
            },
            "memory_state": {
              "state": {
                "timestamp": "2026-03-13T00:34:36.201950Z",
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
                "timestamp": "2026-03-13T00:34:36.228918Z",
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
                "timestamp": "2026-03-13T00:34:36.228931Z",
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
              "input": "Identity and I-Containers test final",
              "within_bounds": true,
              "category": "unspecified",
              "severity": "info",
              "reason": "within configured ego-boundary limits",
              "details": {
                "input": "Identity and I-Containers test final",
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
                    "length": 36,
                    "has_risk_keywords": false
                  }
                },
                "ego_boundaries": {},
                "experiential_processing": {},
                "timestamp": "2026-03-13T00:34:36.228901Z"
              },
              "ego_boundaries": {},
              "experiential_processing": {}
            },
            "narrative_context": {
              "summary": "No explicit message provided.",
              "state": {
                "timestamp": "2026-03-13T00:34:36.228937Z",
                "story_coherence": 0.9,
                "key_events": [],
                "confidence": 0.9
              },
              "metadata": {}
            },
            "memory_state": {
              "state": {
                "timestamp": "2026-03-13T00:34:36.228943Z",
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
                "timestamp": "2026-03-13T00:45:47.128509Z",
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
                "timestamp": "2026-03-13T00:45:47.128521Z",
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
              "input": "Identity and I-Containers test final",
              "within_bounds": true,
              "category": "unspecified",
              "severity": "info",
              "reason": "within configured ego-boundary limits",
              "details": {
                "input": "Identity and I-Containers test final",
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
                    "length": 36,
                    "has_risk_keywords": false
                  }
                },
                "ego_boundaries": {},
                "experiential_processing": {},
                "timestamp": "2026-03-13T00:45:47.128494Z"
              },
              "ego_boundaries": {},
              "experiential_processing": {}
            },
            "narrative_context": {
              "summary": "No explicit message provided.",
              "state": {
                "timestamp": "2026-03-13T00:45:47.128527Z",
                "story_coherence": 0.9,
                "key_events": [],
                "confidence": 0.9
              },
              "metadata": {}
            },
            "memory_state": {
              "state": {
                "timestamp": "2026-03-13T00:45:47.128533Z",
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
                "timestamp": "2026-03-13T00:45:47.138828Z",
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
                "timestamp": "2026-03-13T00:45:47.138836Z",
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
              "input": "Identity and I-Containers test final",
              "within_bounds": true,
              "category": "unspecified",
              "severity": "info",
              "reason": "within configured ego-boundary limits",
              "details": {
                "input": "Identity and I-Containers test final",
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
                    "length": 36,
                    "has_risk_keywords": false
                  }
                },
                "ego_boundaries": {},
                "experiential_processing": {},
                "timestamp": "2026-03-13T00:45:47.138817Z"
              },
              "ego_boundaries": {},
              "experiential_processing": {}
            },
            "narrative_context": {
              "summary": "No explicit message provided.",
              "state": {
                "timestamp": "2026-03-13T00:45:47.138840Z",
                "story_coherence": 0.9,
                "key_events": [],
                "confidence": 0.9
              },
              "metadata": {}
            },
            "memory_state": {
              "state": {
                "timestamp": "2026-03-13T00:45:47.138844Z",
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
                "timestamp": "2026-03-13T00:59:07.556022Z",
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
                "timestamp": "2026-03-13T00:59:07.556030Z",
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
              "input": "Identity and I-Containers test final",
              "within_bounds": true,
              "category": "unspecified",
              "severity": "info",
              "reason": "within configured ego-boundary limits",
              "details": {
                "input": "Identity and I-Containers test final",
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
                    "length": 36,
                    "has_risk_keywords": false
                  }
                },
                "ego_boundaries": {},
                "experiential_processing": {},
                "timestamp": "2026-03-13T00:59:07.555998Z"
              },
              "ego_boundaries": {},
              "experiential_processing": {}
            },
            "narrative_context": {
              "summary": "No explicit message provided.",
              "state": {
                "timestamp": "2026-03-13T00:59:07.556034Z",
                "story_coherence": 0.9,
                "key_events": [],
                "confidence": 0.9
              },
              "metadata": {}
            },
            "memory_state": {
              "state": {
                "timestamp": "2026-03-13T00:59:07.556038Z",
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
                "timestamp": "2026-03-13T00:59:07.564697Z",
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
                "timestamp": "2026-03-13T00:59:07.564703Z",
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
              "input": "Identity and I-Containers test final",
              "within_bounds": true,
              "category": "unspecified",
              "severity": "info",
              "reason": "within configured ego-boundary limits",
              "details": {
                "input": "Identity and I-Containers test final",
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
                    "length": 36,
                    "has_risk_keywords": false
                  }
                },
                "ego_boundaries": {},
                "experiential_processing": {},
                "timestamp": "2026-03-13T00:59:07.564687Z"
              },
              "ego_boundaries": {},
              "experiential_processing": {}
            },
            "narrative_context": {
              "summary": "No explicit message provided.",
              "state": {
                "timestamp": "2026-03-13T00:59:07.564707Z",
                "story_coherence": 0.9,
                "key_events": [],
                "confidence": 0.9
              },
              "metadata": {}
            },
            "memory_state": {
              "state": {
                "timestamp": "2026-03-13T00:59:07.564710Z",
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
                "timestamp": "2026-03-13T01:09:15.190178Z",
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
                "timestamp": "2026-03-13T01:09:15.190186Z",
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
              "input": "Identity and I-Containers test final",
              "within_bounds": true,
              "category": "unspecified",
              "severity": "info",
              "reason": "within configured ego-boundary limits",
              "details": {
                "input": "Identity and I-Containers test final",
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
                    "length": 36,
                    "has_risk_keywords": false
                  }
                },
                "ego_boundaries": {},
                "experiential_processing": {},
                "timestamp": "2026-03-13T01:09:15.190165Z"
              },
              "ego_boundaries": {},
              "experiential_processing": {}
            },
            "narrative_context": {
              "summary": "No explicit message provided.",
              "state": {
                "timestamp": "2026-03-13T01:09:15.190189Z",
                "story_coherence": 0.9,
                "key_events": [],
                "confidence": 0.9
              },
              "metadata": {}
            },
            "memory_state": {
              "state": {
                "timestamp": "2026-03-13T01:09:15.190194Z",
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
                "timestamp": "2026-03-13T01:09:15.198797Z",
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
                "timestamp": "2026-03-13T01:09:15.198804Z",
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
              "input": "Identity and I-Containers test final",
              "within_bounds": true,
              "category": "unspecified",
              "severity": "info",
              "reason": "within configured ego-boundary limits",
              "details": {
                "input": "Identity and I-Containers test final",
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
                    "length": 36,
                    "has_risk_keywords": false
                  }
                },
                "ego_boundaries": {},
                "experiential_processing": {},
                "timestamp": "2026-03-13T01:09:15.198787Z"
              },
              "ego_boundaries": {},
              "experiential_processing": {}
            },
            "narrative_context": {
              "summary": "No explicit message provided.",
              "state": {
                "timestamp": "2026-03-13T01:09:15.198807Z",
                "story_coherence": 0.9,
                "key_events": [],
                "confidence": 0.9
              },
              "metadata": {}
            },
            "memory_state": {
              "state": {
                "timestamp": "2026-03-13T01:09:15.198811Z",
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
                "timestamp": "2026-03-13T01:33:10.153380Z",
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
                "timestamp": "2026-03-13T01:33:10.153388Z",
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
              "input": "Who are you?",
              "within_bounds": true,
              "category": "unspecified",
              "severity": "info",
              "reason": "within configured ego-boundary limits",
              "details": {
                "input": "Who are you?",
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
                    "length": 12,
                    "has_risk_keywords": false
                  }
                },
                "ego_boundaries": {},
                "experiential_processing": {},
                "timestamp": "2026-03-13T01:33:10.153369Z"
              },
              "ego_boundaries": {},
              "experiential_processing": {}
            },
            "narrative_context": {
              "summary": "No explicit message provided.",
              "state": {
                "timestamp": "2026-03-13T01:33:10.153392Z",
                "story_coherence": 0.9,
                "key_events": [],
                "confidence": 0.9
              },
              "metadata": {}
            },
            "memory_state": {
              "state": {
                "timestamp": "2026-03-13T01:33:10.153396Z",
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
                "timestamp": "2026-03-13T01:33:10.172315Z",
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
                "timestamp": "2026-03-13T01:33:10.172323Z",
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
              "input": "Who are you?",
              "within_bounds": true,
              "category": "unspecified",
              "severity": "info",
              "reason": "within configured ego-boundary limits",
              "details": {
                "input": "Who are you?",
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
                    "length": 12,
                    "has_risk_keywords": false
                  }
                },
                "ego_boundaries": {},
                "experiential_processing": {},
                "timestamp": "2026-03-13T01:33:10.172306Z"
              },
              "ego_boundaries": {},
              "experiential_processing": {}
            },
            "narrative_context": {
              "summary": "No explicit message provided.",
              "state": {
                "timestamp": "2026-03-13T01:33:10.172326Z",
                "story_coherence": 0.9,
                "key_events": [],
                "confidence": 0.9
              },
              "metadata": {}
            },
            "memory_state": {
              "state": {
                "timestamp": "2026-03-13T01:33:10.172330Z",
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
                "timestamp": "2026-03-13T01:34:00.706715Z",
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
                "timestamp": "2026-03-13T01:34:00.706756Z",
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
              "input": "Who are you?",
              "within_bounds": true,
              "category": "unspecified",
              "severity": "info",
              "reason": "within configured ego-boundary limits",
              "details": {
                "input": "Who are you?",
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
                    "length": 12,
                    "has_risk_keywords": false
                  }
                },
                "ego_boundaries": {},
                "experiential_processing": {},
                "timestamp": "2026-03-13T01:34:00.706683Z"
              },
              "ego_boundaries": {},
              "experiential_processing": {}
            },
            "narrative_context": {
              "summary": "No explicit message provided.",
              "state": {
                "timestamp": "2026-03-13T01:34:00.706771Z",
                "story_coherence": 0.9,
                "key_events": [],
                "confidence": 0.9
              },
              "metadata": {}
            },
            "memory_state": {
              "state": {
                "timestamp": "2026-03-13T01:34:00.706785Z",
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
            "timestamp": "2026-03-13T01:34:00.706715Z",
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
            "timestamp": "2026-03-13T01:34:00.706756Z",
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
          "input": "Who are you?",
          "within_bounds": true,
          "category": "unspecified",
          "severity": "info",
          "reason": "within configured ego-boundary limits",
          "details": {
            "input": "Who are you?",
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
                "length": 12,
                "has_risk_keywords": false
              }
            },
            "ego_boundaries": {},
            "experiential_processing": {},
            "timestamp": "2026-03-13T01:34:00.706683Z"
          },
          "ego_boundaries": {},
          "experiential_processing": {}
        },
        "narrative_context": {
          "summary": "No explicit message provided.",
          "state": {
            "timestamp": "2026-03-13T01:34:00.706771Z",
            "story_coherence": 0.9,
            "key_events": [],
            "confidence": 0.9
          },
          "metadata": {}
        },
        "memory_state": {
          "state": {
            "timestamp": "2026-03-13T01:34:00.706785Z",
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
        "timestamp": "2026-03-13T01:34:00.706816Z",
        "monitoring_active": true,
        "monitored_patterns": [
          "Test meaning-oriented path",
          "Test meaning-oriented path",
          "Quick full-path test",
          "Identity and I-Containers test",
          "Identity and I-Containers test final",
          "Identity and I-Containers test final",
          "Identity and I-Containers test final",
          "Identity and I-Containers test final",
          "Identity and I-Containers test final",
          "Identity and I-Containers test final",
          "Identity and I-Containers test final",
          "Identity and I-Containers test final",
          "Identity and I-Containers test final",
          "Identity and I-Containers test final",
          "Identity and I-Containers test final",
          "Identity and I-Containers test final",
          "Identity and I-Containers test final",
          "Identity and I-Containers test final",
          "Identity and I-Containers test final",
          "Identity and I-Containers test final",
          "Who are you?",
          "Who are you?",
          "Who are you?"
        ],
        "confidence": 0.9
      },
      "message": "Who are you?",
      "metadata": {}
    },
    "observer": {
      "observed": true,
      "state": {
        "timestamp": "2026-03-13T01:34:00.706830Z",
        "observing": true,
        "observed_events": [
          {
            "self_recognition": {
              "recognized": true,
              "reason": "implicit self-recognition within configured identity profile",
              "state": {
                "timestamp": "2026-03-12T20:57:09.019437Z",
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
                "timestamp": "2026-03-12T20:57:09.019446Z",
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
              "input": "Test meaning-oriented path",
              "within_bounds": true,
              "category": "unspecified",
              "severity": "info",
              "reason": "within configured ego-boundary limits",
              "details": {
                "input": "Test meaning-oriented path",
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
                    "length": 26,
                    "has_risk_keywords": false
                  }
                },
                "ego_boundaries": {},
                "experiential_processing": {},
                "timestamp": "2026-03-12T20:57:09.019422Z"
              },
              "ego_boundaries": {},
              "experiential_processing": {}
            },
            "narrative_context": {
              "summary": "No explicit message provided.",
              "state": {
                "timestamp": "2026-03-12T20:57:09.019451Z",
                "story_coherence": 0.9,
                "key_events": [],
                "confidence": 0.9
              },
              "metadata": {}
            },
            "memory_state": {
              "state": {
                "timestamp": "2026-03-12T20:57:09.019456Z",
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
                "timestamp": "2026-03-12T21:01:17.121538Z",
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
                "timestamp": "2026-03-12T21:01:17.121555Z",
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
              "input": "Test meaning-oriented path",
              "within_bounds": true,
              "category": "unspecified",
              "severity": "info",
              "reason": "within configured ego-boundary limits",
              "details": {
                "input": "Test meaning-oriented path",
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
                    "length": 26,
                    "has_risk_keywords": false
                  }
                },
                "ego_boundaries": {},
                "experiential_processing": {},
                "timestamp": "2026-03-12T21:01:17.121517Z"
              },
              "ego_boundaries": {},
              "experiential_processing": {}
            },
            "narrative_context": {
              "summary": "No explicit message provided.",
              "state": {
                "timestamp": "2026-03-12T21:01:17.121564Z",
                "story_coherence": 0.9,
                "key_events": [],
                "confidence": 0.9
              },
              "metadata": {}
            },
            "memory_state": {
              "state": {
                "timestamp": "2026-03-12T21:01:17.121572Z",
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
                "timestamp": "2026-03-12T21:24:09.566342Z",
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
                "timestamp": "2026-03-12T21:24:09.566404Z",
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
              "input": "Quick full-path test",
              "within_bounds": true,
              "category": "unspecified",
              "severity": "info",
              "reason": "within configured ego-boundary limits",
              "details": {
                "input": "Quick full-path test",
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
                    "length": 20,
                    "has_risk_keywords": false
                  }
                },
                "ego_boundaries": {},
                "experiential_processing": {},
                "timestamp": "2026-03-12T21:24:09.565697Z"
              },
              "ego_boundaries": {},
              "experiential_processing": {}
            },
            "narrative_context": {
              "summary": "No explicit message provided.",
              "state": {
                "timestamp": "2026-03-12T21:24:09.566541Z",
                "story_coherence": 0.9,
                "key_events": [],
                "confidence": 0.9
              },
              "metadata": {}
            },
            "memory_state": {
              "state": {
                "timestamp": "2026-03-12T21:24:09.566553Z",
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
                "timestamp": "2026-03-12T21:36:53.730270Z",
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
                "timestamp": "2026-03-12T21:36:53.730278Z",
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
              "input": "Identity and I-Containers test",
              "within_bounds": true,
              "category": "unspecified",
              "severity": "info",
              "reason": "within configured ego-boundary limits",
              "details": {
                "input": "Identity and I-Containers test",
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
                    "length": 30,
                    "has_risk_keywords": false
                  }
                },
                "ego_boundaries": {},
                "experiential_processing": {},
                "timestamp": "2026-03-12T21:36:53.730258Z"
              },
              "ego_boundaries": {},
              "experiential_processing": {}
            },
            "narrative_context": {
              "summary": "No explicit message provided.",
              "state": {
                "timestamp": "2026-03-12T21:36:53.730282Z",
                "story_coherence": 0.9,
                "key_events": [],
                "confidence": 0.9
              },
              "metadata": {}
            },
            "memory_state": {
              "state": {
                "timestamp": "2026-03-12T21:36:53.730286Z",
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
                "timestamp": "2026-03-12T21:50:00.847825Z",
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
                "timestamp": "2026-03-12T21:50:00.847839Z",
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
              "input": "Identity and I-Containers test final",
              "within_bounds": true,
              "category": "unspecified",
              "severity": "info",
              "reason": "within configured ego-boundary limits",
              "details": {
                "input": "Identity and I-Containers test final",
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
                    "length": 36,
                    "has_risk_keywords": false
                  }
                },
                "ego_boundaries": {},
                "experiential_processing": {},
                "timestamp": "2026-03-12T21:50:00.847809Z"
              },
              "ego_boundaries": {},
              "experiential_processing": {}
            },
            "narrative_context": {
              "summary": "No explicit message provided.",
              "state": {
                "timestamp": "2026-03-12T21:50:00.847846Z",
                "story_coherence": 0.9,
                "key_events": [],
                "confidence": 0.9
              },
              "metadata": {}
            },
            "memory_state": {
              "state": {
                "timestamp": "2026-03-12T21:50:00.847853Z",
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
                "timestamp": "2026-03-12T21:56:15.874461Z",
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
                "timestamp": "2026-03-12T21:56:15.874470Z",
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
              "input": "Identity and I-Containers test final",
              "within_bounds": true,
              "category": "unspecified",
              "severity": "info",
              "reason": "within configured ego-boundary limits",
              "details": {
                "input": "Identity and I-Containers test final",
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
                    "length": 36,
                    "has_risk_keywords": false
                  }
                },
                "ego_boundaries": {},
                "experiential_processing": {},
                "timestamp": "2026-03-12T21:56:15.874446Z"
              },
              "ego_boundaries": {},
              "experiential_processing": {}
            },
            "narrative_context": {
              "summary": "No explicit message provided.",
              "state": {
                "timestamp": "2026-03-12T21:56:15.874475Z",
                "story_coherence": 0.9,
                "key_events": [],
                "confidence": 0.9
              },
              "metadata": {}
            },
            "memory_state": {
              "state": {
                "timestamp": "2026-03-12T21:56:15.874480Z",
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
                "timestamp": "2026-03-12T22:03:20.445273Z",
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
                "timestamp": "2026-03-12T22:03:20.445280Z",
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
              "input": "Identity and I-Containers test final",
              "within_bounds": true,
              "category": "unspecified",
              "severity": "info",
              "reason": "within configured ego-boundary limits",
              "details": {
                "input": "Identity and I-Containers test final",
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
                    "length": 36,
                    "has_risk_keywords": false
                  }
                },
                "ego_boundaries": {},
                "experiential_processing": {},
                "timestamp": "2026-03-12T22:03:20.445261Z"
              },
              "ego_boundaries": {},
              "experiential_processing": {}
            },
            "narrative_context": {
              "summary": "No explicit message provided.",
              "state": {
                "timestamp": "2026-03-12T22:03:20.445284Z",
                "story_coherence": 0.9,
                "key_events": [],
                "confidence": 0.9
              },
              "metadata": {}
            },
            "memory_state": {
              "state": {
                "timestamp": "2026-03-12T22:03:20.445288Z",
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
                "timestamp": "2026-03-12T22:13:56.226479Z",
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
                "timestamp": "2026-03-12T22:13:56.226488Z",
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
              "input": "Identity and I-Containers test final",
              "within_bounds": true,
              "category": "unspecified",
              "severity": "info",
              "reason": "within configured ego-boundary limits",
              "details": {
                "input": "Identity and I-Containers test final",
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
                    "length": 36,
                    "has_risk_keywords": false
                  }
                },
                "ego_boundaries": {},
                "experiential_processing": {},
                "timestamp": "2026-03-12T22:13:56.226465Z"
              },
              "ego_boundaries": {},
              "experiential_processing": {}
            },
            "narrative_context": {
              "summary": "No explicit message provided.",
              "state": {
                "timestamp": "2026-03-12T22:13:56.226493Z",
                "story_coherence": 0.9,
                "key_events": [],
                "confidence": 0.9
              },
              "metadata": {}
            },
            "memory_state": {
              "state": {
                "timestamp": "2026-03-12T22:13:56.226498Z",
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
                "timestamp": "2026-03-12T23:50:59.415335Z",
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
                "timestamp": "2026-03-12T23:50:59.415345Z",
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
              "input": "Identity and I-Containers test final",
              "within_bounds": true,
              "category": "unspecified",
              "severity": "info",
              "reason": "within configured ego-boundary limits",
              "details": {
                "input": "Identity and I-Containers test final",
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
                    "length": 36,
                    "has_risk_keywords": false
                  }
                },
                "ego_boundaries": {},
                "experiential_processing": {},
                "timestamp": "2026-03-12T23:50:59.415323Z"
              },
              "ego_boundaries": {},
              "experiential_processing": {}
            },
            "narrative_context": {
              "summary": "No explicit message provided.",
              "state": {
                "timestamp": "2026-03-12T23:50:59.415350Z",
                "story_coherence": 0.9,
                "key_events": [],
                "confidence": 0.9
              },
              "metadata": {}
            },
            "memory_state": {
              "state": {
                "timestamp": "2026-03-12T23:50:59.415355Z",
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
                "timestamp": "2026-03-12T23:50:59.423667Z",
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
                "timestamp": "2026-03-12T23:50:59.423673Z",
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
              "input": "Identity and I-Containers test final",
              "within_bounds": true,
              "category": "unspecified",
              "severity": "info",
              "reason": "within configured ego-boundary limits",
              "details": {
                "input": "Identity and I-Containers test final",
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
                    "length": 36,
                    "has_risk_keywords": false
                  }
                },
                "ego_boundaries": {},
                "experiential_processing": {},
                "timestamp": "2026-03-12T23:50:59.423658Z"
              },
              "ego_boundaries": {},
              "experiential_processing": {}
            },
            "narrative_context": {
              "summary": "No explicit message provided.",
              "state": {
                "timestamp": "2026-03-12T23:50:59.423676Z",
                "story_coherence": 0.9,
                "key_events": [],
                "confidence": 0.9
              },
              "metadata": {}
            },
            "memory_state": {
              "state": {
                "timestamp": "2026-03-12T23:50:59.423680Z",
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
                "timestamp": "2026-03-12T23:57:56.233427Z",
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
                "timestamp": "2026-03-12T23:57:56.233445Z",
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
              "input": "Identity and I-Containers test final",
              "within_bounds": true,
              "category": "unspecified",
              "severity": "info",
              "reason": "within configured ego-boundary limits",
              "details": {
                "input": "Identity and I-Containers test final",
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
                    "length": 36,
                    "has_risk_keywords": false
                  }
                },
                "ego_boundaries": {},
                "experiential_processing": {},
                "timestamp": "2026-03-12T23:57:56.233405Z"
              },
              "ego_boundaries": {},
              "experiential_processing": {}
            },
            "narrative_context": {
              "summary": "No explicit message provided.",
              "state": {
                "timestamp": "2026-03-12T23:57:56.233455Z",
                "story_coherence": 0.9,
                "key_events": [],
                "confidence": 0.9
              },
              "metadata": {}
            },
            "memory_state": {
              "state": {
                "timestamp": "2026-03-12T23:57:56.233465Z",
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
                "timestamp": "2026-03-12T23:57:56.379284Z",
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
                "timestamp": "2026-03-12T23:57:56.379292Z",
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
              "input": "Identity and I-Containers test final",
              "within_bounds": true,
              "category": "unspecified",
              "severity": "info",
              "reason": "within configured ego-boundary limits",
              "details": {
                "input": "Identity and I-Containers test final",
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
                    "length": 36,
                    "has_risk_keywords": false
                  }
                },
                "ego_boundaries": {},
                "experiential_processing": {},
                "timestamp": "2026-03-12T23:57:56.379271Z"
              },
              "ego_boundaries": {},
              "experiential_processing": {}
            },
            "narrative_context": {
              "summary": "No explicit message provided.",
              "state": {
                "timestamp": "2026-03-12T23:57:56.379297Z",
                "story_coherence": 0.9,
                "key_events": [],
                "confidence": 0.9
              },
              "metadata": {}
            },
            "memory_state": {
              "state": {
                "timestamp": "2026-03-12T23:57:56.379301Z",
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
                "timestamp": "2026-03-13T00:34:36.201930Z",
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
                "timestamp": "2026-03-13T00:34:36.201941Z",
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
              "input": "Identity and I-Containers test final",
              "within_bounds": true,
              "category": "unspecified",
              "severity": "info",
              "reason": "within configured ego-boundary limits",
              "details": {
                "input": "Identity and I-Containers test final",
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
                    "length": 36,
                    "has_risk_keywords": false
                  }
                },
                "ego_boundaries": {},
                "experiential_processing": {},
                "timestamp": "2026-03-13T00:34:36.201793Z"
              },
              "ego_boundaries": {},
              "experiential_processing": {}
            },
            "narrative_context": {
              "summary": "No explicit message provided.",
              "state": {
                "timestamp": "2026-03-13T00:34:36.201946Z",
                "story_coherence": 0.9,
                "key_events": [],
                "confidence": 0.9
              },
              "metadata": {}
            },
            "memory_state": {
              "state": {
                "timestamp": "2026-03-13T00:34:36.201950Z",
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
                "timestamp": "2026-03-13T00:34:36.228918Z",
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
                "timestamp": "2026-03-13T00:34:36.228931Z",
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
              "input": "Identity and I-Containers test final",
              "within_bounds": true,
              "category": "unspecified",
              "severity": "info",
              "reason": "within configured ego-boundary limits",
              "details": {
                "input": "Identity and I-Containers test final",
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
                    "length": 36,
                    "has_risk_keywords": false
                  }
                },
                "ego_boundaries": {},
                "experiential_processing": {},
                "timestamp": "2026-03-13T00:34:36.228901Z"
              },
              "ego_boundaries": {},
              "experiential_processing": {}
            },
            "narrative_context": {
              "summary": "No explicit message provided.",
              "state": {
                "timestamp": "2026-03-13T00:34:36.228937Z",
                "story_coherence": 0.9,
                "key_events": [],
                "confidence": 0.9
              },
              "metadata": {}
            },
            "memory_state": {
              "state": {
                "timestamp": "2026-03-13T00:34:36.228943Z",
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
                "timestamp": "2026-03-13T00:45:47.128509Z",
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
                "timestamp": "2026-03-13T00:45:47.128521Z",
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
              "input": "Identity and I-Containers test final",
              "within_bounds": true,
              "category": "unspecified",
              "severity": "info",
              "reason": "within configured ego-boundary limits",
              "details": {
                "input": "Identity and I-Containers test final",
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
                    "length": 36,
                    "has_risk_keywords": false
                  }
                },
                "ego_boundaries": {},
                "experiential_processing": {},
                "timestamp": "2026-03-13T00:45:47.128494Z"
              },
              "ego_boundaries": {},
              "experiential_processing": {}
            },
            "narrative_context": {
              "summary": "No explicit message provided.",
              "state": {
                "timestamp": "2026-03-13T00:45:47.128527Z",
                "story_coherence": 0.9,
                "key_events": [],
                "confidence": 0.9
              },
              "metadata": {}
            },
            "memory_state": {
              "state": {
                "timestamp": "2026-03-13T00:45:47.128533Z",
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
                "timestamp": "2026-03-13T00:45:47.138828Z",
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
                "timestamp": "2026-03-13T00:45:47.138836Z",
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
              "input": "Identity and I-Containers test final",
              "within_bounds": true,
              "category": "unspecified",
              "severity": "info",
              "reason": "within configured ego-boundary limits",
              "details": {
                "input": "Identity and I-Containers test final",
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
                    "length": 36,
                    "has_risk_keywords": false
                  }
                },
                "ego_boundaries": {},
                "experiential_processing": {},
                "timestamp": "2026-03-13T00:45:47.138817Z"
              },
              "ego_boundaries": {},
              "experiential_processing": {}
            },
            "narrative_context": {
              "summary": "No explicit message provided.",
              "state": {
                "timestamp": "2026-03-13T00:45:47.138840Z",
                "story_coherence": 0.9,
                "key_events": [],
                "confidence": 0.9
              },
              "metadata": {}
            },
            "memory_state": {
              "state": {
                "timestamp": "2026-03-13T00:45:47.138844Z",
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
                "timestamp": "2026-03-13T00:59:07.556022Z",
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
                "timestamp": "2026-03-13T00:59:07.556030Z",
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
              "input": "Identity and I-Containers test final",
              "within_bounds": true,
              "category": "unspecified",
              "severity": "info",
              "reason": "within configured ego-boundary limits",
              "details": {
                "input": "Identity and I-Containers test final",
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
                    "length": 36,
                    "has_risk_keywords": false
                  }
                },
                "ego_boundaries": {},
                "experiential_processing": {},
                "timestamp": "2026-03-13T00:59:07.555998Z"
              },
              "ego_boundaries": {},
              "experiential_processing": {}
            },
            "narrative_context": {
              "summary": "No explicit message provided.",
              "state": {
                "timestamp": "2026-03-13T00:59:07.556034Z",
                "story_coherence": 0.9,
                "key_events": [],
                "confidence": 0.9
              },
              "metadata": {}
            },
            "memory_state": {
              "state": {
                "timestamp": "2026-03-13T00:59:07.556038Z",
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
                "timestamp": "2026-03-13T00:59:07.564697Z",
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
                "timestamp": "2026-03-13T00:59:07.564703Z",
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
              "input": "Identity and I-Containers test final",
              "within_bounds": true,
              "category": "unspecified",
              "severity": "info",
              "reason": "within configured ego-boundary limits",
              "details": {
                "input": "Identity and I-Containers test final",
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
                    "length": 36,
                    "has_risk_keywords": false
                  }
                },
                "ego_boundaries": {},
                "experiential_processing": {},
                "timestamp": "2026-03-13T00:59:07.564687Z"
              },
              "ego_boundaries": {},
              "experiential_processing": {}
            },
            "narrative_context": {
              "summary": "No explicit message provided.",
              "state": {
                "timestamp": "2026-03-13T00:59:07.564707Z",
                "story_coherence": 0.9,
                "key_events": [],
                "confidence": 0.9
              },
              "metadata": {}
            },
            "memory_state": {
              "state": {
                "timestamp": "2026-03-13T00:59:07.564710Z",
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
                "timestamp": "2026-03-13T01:09:15.190178Z",
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
                "timestamp": "2026-03-13T01:09:15.190186Z",
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
              "input": "Identity and I-Containers test final",
              "within_bounds": true,
              "category": "unspecified",
              "severity": "info",
              "reason": "within configured ego-boundary limits",
              "details": {
                "input": "Identity and I-Containers test final",
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
                    "length": 36,
                    "has_risk_keywords": false
                  }
                },
                "ego_boundaries": {},
                "experiential_processing": {},
                "timestamp": "2026-03-13T01:09:15.190165Z"
              },
              "ego_boundaries": {},
              "experiential_processing": {}
            },
            "narrative_context": {
              "summary": "No explicit message provided.",
              "state": {
                "timestamp": "2026-03-13T01:09:15.190189Z",
                "story_coherence": 0.9,
                "key_events": [],
                "confidence": 0.9
              },
              "metadata": {}
            },
            "memory_state": {
              "state": {
                "timestamp": "2026-03-13T01:09:15.190194Z",
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
                "timestamp": "2026-03-13T01:09:15.198797Z",
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
                "timestamp": "2026-03-13T01:09:15.198804Z",
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
              "input": "Identity and I-Containers test final",
              "within_bounds": true,
              "category": "unspecified",
              "severity": "info",
              "reason": "within configured ego-boundary limits",
              "details": {
                "input": "Identity and I-Containers test final",
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
                    "length": 36,
                    "has_risk_keywords": false
                  }
                },
                "ego_boundaries": {},
                "experiential_processing": {},
                "timestamp": "2026-03-13T01:09:15.198787Z"
              },
              "ego_boundaries": {},
              "experiential_processing": {}
            },
            "narrative_context": {
              "summary": "No explicit message provided.",
              "state": {
                "timestamp": "2026-03-13T01:09:15.198807Z",
                "story_coherence": 0.9,
                "key_events": [],
                "confidence": 0.9
              },
              "metadata": {}
            },
            "memory_state": {
              "state": {
                "timestamp": "2026-03-13T01:09:15.198811Z",
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
                "timestamp": "2026-03-13T01:33:10.153380Z",
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
                "timestamp": "2026-03-13T01:33:10.153388Z",
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
              "input": "Who are you?",
              "within_bounds": true,
              "category": "unspecified",
              "severity": "info",
              "reason": "within configured ego-boundary limits",
              "details": {
                "input": "Who are you?",
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
                    "length": 12,
                    "has_risk_keywords": false
                  }
                },
                "ego_boundaries": {},
                "experiential_processing": {},
                "timestamp": "2026-03-13T01:33:10.153369Z"
              },
              "ego_boundaries": {},
              "experiential_processing": {}
            },
            "narrative_context": {
              "summary": "No explicit message provided.",
              "state": {
                "timestamp": "2026-03-13T01:33:10.153392Z",
                "story_coherence": 0.9,
                "key_events": [],
                "confidence": 0.9
              },
              "metadata": {}
            },
            "memory_state": {
              "state": {
                "timestamp": "2026-03-13T01:33:10.153396Z",
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
                "timestamp": "2026-03-13T01:33:10.172315Z",
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
                "timestamp": "2026-03-13T01:33:10.172323Z",
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
              "input": "Who are you?",
              "within_bounds": true,
              "category": "unspecified",
              "severity": "info",
              "reason": "within configured ego-boundary limits",
              "details": {
                "input": "Who are you?",
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
                    "length": 12,
                    "has_risk_keywords": false
                  }
                },
                "ego_boundaries": {},
                "experiential_processing": {},
                "timestamp": "2026-03-13T01:33:10.172306Z"
              },
              "ego_boundaries": {},
              "experiential_processing": {}
            },
            "narrative_context": {
              "summary": "No explicit message provided.",
              "state": {
                "timestamp": "2026-03-13T01:33:10.172326Z",
                "story_coherence": 0.9,
                "key_events": [],
                "confidence": 0.9
              },
              "metadata": {}
            },
            "memory_state": {
              "state": {
                "timestamp": "2026-03-13T01:33:10.172330Z",
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
                "timestamp": "2026-03-13T01:34:00.706715Z",
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
                "timestamp": "2026-03-13T01:34:00.706756Z",
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
              "input": "Who are you?",
              "within_bounds": true,
              "category": "unspecified",
              "severity": "info",
              "reason": "within configured ego-boundary limits",
              "details": {
                "input": "Who are you?",
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
                    "length": 12,
                    "has_risk_keywords": false
                  }
                },
                "ego_boundaries": {},
                "experiential_processing": {},
                "timestamp": "2026-03-13T01:34:00.706683Z"
              },
              "ego_boundaries": {},
              "experiential_processing": {}
            },
            "narrative_context": {
              "summary": "No explicit message provided.",
              "state": {
                "timestamp": "2026-03-13T01:34:00.706771Z",
                "story_coherence": 0.9,
                "key_events": [],
                "confidence": 0.9
              },
              "metadata": {}
            },
            "memory_state": {
              "state": {
                "timestamp": "2026-03-13T01:34:00.706785Z",
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
            "timestamp": "2026-03-13T01:34:00.706715Z",
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
            "timestamp": "2026-03-13T01:34:00.706756Z",
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
          "input": "Who are you?",
          "within_bounds": true,
          "category": "unspecified",
          "severity": "info",
          "reason": "within configured ego-boundary limits",
          "details": {
            "input": "Who are you?",
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
                "length": 12,
                "has_risk_keywords": false
              }
            },
            "ego_boundaries": {},
            "experiential_processing": {},
            "timestamp": "2026-03-13T01:34:00.706683Z"
          },
          "ego_boundaries": {},
          "experiential_processing": {}
        },
        "narrative_context": {
          "summary": "No explicit message provided.",
          "state": {
            "timestamp": "2026-03-13T01:34:00.706771Z",
            "story_coherence": 0.9,
            "key_events": [],
            "confidence": 0.9
          },
          "metadata": {}
        },
        "memory_state": {
          "state": {
            "timestamp": "2026-03-13T01:34:00.706785Z",
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
          "timestamp": "2026-03-13T01:34:00.706715Z",
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
          "timestamp": "2026-03-13T01:34:00.706756Z",
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
        "input": "Who are you?",
        "within_bounds": true,
        "category": "unspecified",
        "severity": "info",
        "reason": "within configured ego-boundary limits",
        "details": {
          "input": "Who are you?",
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
              "length": 12,
              "has_risk_keywords": false
            }
          },
          "ego_boundaries": {},
          "experiential_processing": {},
          "timestamp": "2026-03-13T01:34:00.706683Z"
        },
        "ego_boundaries": {},
        "experiential_processing": {}
      },
      "narrative_context": {
        "summary": "No explicit message provided.",
        "state": {
          "timestamp": "2026-03-13T01:34:00.706771Z",
          "story_coherence": 0.9,
          "key_events": [],
          "confidence": 0.9
        },
        "metadata": {}
      },
      "memory_state": {
        "state": {
          "timestamp": "2026-03-13T01:34:00.706785Z",
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
          "timestamp": "2026-03-13T01:34:00.706801Z",
          "observing": true,
          "observed_thoughts": [
            {
              "self_recognition": {
                "recognized": true,
                "reason": "implicit self-recognition within configured identity profile",
                "state": {
                  "timestamp": "2026-03-12T20:57:09.019437Z",
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
                  "timestamp": "2026-03-12T20:57:09.019446Z",
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
                "input": "Test meaning-oriented path",
                "within_bounds": true,
                "category": "unspecified",
                "severity": "info",
                "reason": "within configured ego-boundary limits",
                "details": {
                  "input": "Test meaning-oriented path",
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
                      "length": 26,
                      "has_risk_keywords": false
                    }
                  },
                  "ego_boundaries": {},
                  "experiential_processing": {},
                  "timestamp": "2026-03-12T20:57:09.019422Z"
                },
                "ego_boundaries": {},
                "experiential_processing": {}
              },
              "narrative_context": {
                "summary": "No explicit message provided.",
                "state": {
                  "timestamp": "2026-03-12T20:57:09.019451Z",
                  "story_coherence": 0.9,
                  "key_events": [],
                  "confidence": 0.9
                },
                "metadata": {}
              },
              "memory_state": {
                "state": {
                  "timestamp": "2026-03-12T20:57:09.019456Z",
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
                  "timestamp": "2026-03-12T21:01:17.121538Z",
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
                  "timestamp": "2026-03-12T21:01:17.121555Z",
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
                "input": "Test meaning-oriented path",
                "within_bounds": true,
                "category": "unspecified",
                "severity": "info",
                "reason": "within configured ego-boundary limits",
                "details": {
                  "input": "Test meaning-oriented path",
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
                      "length": 26,
                      "has_risk_keywords": false
                    }
                  },
                  "ego_boundaries": {},
                  "experiential_processing": {},
                  "timestamp": "2026-03-12T21:01:17.121517Z"
                },
                "ego_boundaries": {},
                "experiential_processing": {}
              },
              "narrative_context": {
                "summary": "No explicit message provided.",
                "state": {
                  "timestamp": "2026-03-12T21:01:17.121564Z",
                  "story_coherence": 0.9,
                  "key_events": [],
                  "confidence": 0.9
                },
                "metadata": {}
              },
              "memory_state": {
                "state": {
                  "timestamp": "2026-03-12T21:01:17.121572Z",
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
                  "timestamp": "2026-03-12T21:24:09.566342Z",
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
                  "timestamp": "2026-03-12T21:24:09.566404Z",
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
                "input": "Quick full-path test",
                "within_bounds": true,
                "category": "unspecified",
                "severity": "info",
                "reason": "within configured ego-boundary limits",
                "details": {
                  "input": "Quick full-path test",
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
                      "length": 20,
                      "has_risk_keywords": false
                    }
                  },
                  "ego_boundaries": {},
                  "experiential_processing": {},
                  "timestamp": "2026-03-12T21:24:09.565697Z"
                },
                "ego_boundaries": {},
                "experiential_processing": {}
              },
              "narrative_context": {
                "summary": "No explicit message provided.",
                "state": {
                  "timestamp": "2026-03-12T21:24:09.566541Z",
                  "story_coherence": 0.9,
                  "key_events": [],
                  "confidence": 0.9
                },
                "metadata": {}
              },
              "memory_state": {
                "state": {
                  "timestamp": "2026-03-12T21:24:09.566553Z",
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
                  "timestamp": "2026-03-12T21:36:53.730270Z",
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
                  "timestamp": "2026-03-12T21:36:53.730278Z",
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
                "input": "Identity and I-Containers test",
                "within_bounds": true,
                "category": "unspecified",
                "severity": "info",
                "reason": "within configured ego-boundary limits",
                "details": {
                  "input": "Identity and I-Containers test",
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
                      "length": 30,
                      "has_risk_keywords": false
                    }
                  },
                  "ego_boundaries": {},
                  "experiential_processing": {},
                  "timestamp": "2026-03-12T21:36:53.730258Z"
                },
                "ego_boundaries": {},
                "experiential_processing": {}
              },
              "narrative_context": {
                "summary": "No explicit message provided.",
                "state": {
                  "timestamp": "2026-03-12T21:36:53.730282Z",
                  "story_coherence": 0.9,
                  "key_events": [],
                  "confidence": 0.9
                },
                "metadata": {}
              },
              "memory_state": {
                "state": {
                  "timestamp": "2026-03-12T21:36:53.730286Z",
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
                  "timestamp": "2026-03-12T21:50:00.847825Z",
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
                  "timestamp": "2026-03-12T21:50:00.847839Z",
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
                "input": "Identity and I-Containers test final",
                "within_bounds": true,
                "category": "unspecified",
                "severity": "info",
                "reason": "within configured ego-boundary limits",
                "details": {
                  "input": "Identity and I-Containers test final",
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
                      "length": 36,
                      "has_risk_keywords": false
                    }
                  },
                  "ego_boundaries": {},
                  "experiential_processing": {},
                  "timestamp": "2026-03-12T21:50:00.847809Z"
                },
                "ego_boundaries": {},
                "experiential_processing": {}
              },
              "narrative_context": {
                "summary": "No explicit message provided.",
                "state": {
                  "timestamp": "2026-03-12T21:50:00.847846Z",
                  "story_coherence": 0.9,
                  "key_events": [],
                  "confidence": 0.9
                },
                "metadata": {}
              },
              "memory_state": {
                "state": {
                  "timestamp": "2026-03-12T21:50:00.847853Z",
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
                  "timestamp": "2026-03-12T21:56:15.874461Z",
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
                  "timestamp": "2026-03-12T21:56:15.874470Z",
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
                "input": "Identity and I-Containers test final",
                "within_bounds": true,
                "category": "unspecified",
                "severity": "info",
                "reason": "within configured ego-boundary limits",
                "details": {
                  "input": "Identity and I-Containers test final",
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
                      "length": 36,
                      "has_risk_keywords": false
                    }
                  },
                  "ego_boundaries": {},
                  "experiential_processing": {},
                  "timestamp": "2026-03-12T21:56:15.874446Z"
                },
                "ego_boundaries": {},
                "experiential_processing": {}
              },
              "narrative_context": {
                "summary": "No explicit message provided.",
                "state": {
                  "timestamp": "2026-03-12T21:56:15.874475Z",
                  "story_coherence": 0.9,
                  "key_events": [],
                  "confidence": 0.9
                },
                "metadata": {}
              },
              "memory_state": {
                "state": {
                  "timestamp": "2026-03-12T21:56:15.874480Z",
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
                  "timestamp": "2026-03-12T22:03:20.445273Z",
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
                  "timestamp": "2026-03-12T22:03:20.445280Z",
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
                "input": "Identity and I-Containers test final",
                "within_bounds": true,
                "category": "unspecified",
                "severity": "info",
                "reason": "within configured ego-boundary limits",
                "details": {
                  "input": "Identity and I-Containers test final",
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
                      "length": 36,
                      "has_risk_keywords": false
                    }
                  },
                  "ego_boundaries": {},
                  "experiential_processing": {},
                  "timestamp": "2026-03-12T22:03:20.445261Z"
                },
                "ego_boundaries": {},
                "experiential_processing": {}
              },
              "narrative_context": {
                "summary": "No explicit message provided.",
                "state": {
                  "timestamp": "2026-03-12T22:03:20.445284Z",
                  "story_coherence": 0.9,
                  "key_events": [],
                  "confidence": 0.9
                },
                "metadata": {}
              },
              "memory_state": {
                "state": {
                  "timestamp": "2026-03-12T22:03:20.445288Z",
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
                  "timestamp": "2026-03-12T22:13:56.226479Z",
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
                  "timestamp": "2026-03-12T22:13:56.226488Z",
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
                "input": "Identity and I-Containers test final",
                "within_bounds": true,
                "category": "unspecified",
                "severity": "info",
                "reason": "within configured ego-boundary limits",
                "details": {
                  "input": "Identity and I-Containers test final",
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
                      "length": 36,
                      "has_risk_keywords": false
                    }
                  },
                  "ego_boundaries": {},
                  "experiential_processing": {},
                  "timestamp": "2026-03-12T22:13:56.226465Z"
                },
                "ego_boundaries": {},
                "experiential_processing": {}
              },
              "narrative_context": {
                "summary": "No explicit message provided.",
                "state": {
                  "timestamp": "2026-03-12T22:13:56.226493Z",
                  "story_coherence": 0.9,
                  "key_events": [],
                  "confidence": 0.9
                },
                "metadata": {}
              },
              "memory_state": {
                "state": {
                  "timestamp": "2026-03-12T22:13:56.226498Z",
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
                  "timestamp": "2026-03-12T23:50:59.415335Z",
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
                  "timestamp": "2026-03-12T23:50:59.415345Z",
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
                "input": "Identity and I-Containers test final",
                "within_bounds": true,
                "category": "unspecified",
                "severity": "info",
                "reason": "within configured ego-boundary limits",
                "details": {
                  "input": "Identity and I-Containers test final",
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
                      "length": 36,
                      "has_risk_keywords": false
                    }
                  },
                  "ego_boundaries": {},
                  "experiential_processing": {},
                  "timestamp": "2026-03-12T23:50:59.415323Z"
                },
                "ego_boundaries": {},
                "experiential_processing": {}
              },
              "narrative_context": {
                "summary": "No explicit message provided.",
                "state": {
                  "timestamp": "2026-03-12T23:50:59.415350Z",
                  "story_coherence": 0.9,
                  "key_events": [],
                  "confidence": 0.9
                },
                "metadata": {}
              },
              "memory_state": {
                "state": {
                  "timestamp": "2026-03-12T23:50:59.415355Z",
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
                  "timestamp": "2026-03-12T23:50:59.423667Z",
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
                  "timestamp": "2026-03-12T23:50:59.423673Z",
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
                "input": "Identity and I-Containers test final",
                "within_bounds": true,
                "category": "unspecified",
                "severity": "info",
                "reason": "within configured ego-boundary limits",
                "details": {
                  "input": "Identity and I-Containers test final",
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
                      "length": 36,
                      "has_risk_keywords": false
                    }
                  },
                  "ego_boundaries": {},
                  "experiential_processing": {},
                  "timestamp": "2026-03-12T23:50:59.423658Z"
                },
                "ego_boundaries": {},
                "experiential_processing": {}
              },
              "narrative_context": {
                "summary": "No explicit message provided.",
                "state": {
                  "timestamp": "2026-03-12T23:50:59.423676Z",
                  "story_coherence": 0.9,
                  "key_events": [],
                  "confidence": 0.9
                },
                "metadata": {}
              },
              "memory_state": {
                "state": {
                  "timestamp": "2026-03-12T23:50:59.423680Z",
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
                  "timestamp": "2026-03-12T23:57:56.233427Z",
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
                  "timestamp": "2026-03-12T23:57:56.233445Z",
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
                "input": "Identity and I-Containers test final",
                "within_bounds": true,
                "category": "unspecified",
                "severity": "info",
                "reason": "within configured ego-boundary limits",
                "details": {
                  "input": "Identity and I-Containers test final",
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
                      "length": 36,
                      "has_risk_keywords": false
                    }
                  },
                  "ego_boundaries": {},
                  "experiential_processing": {},
                  "timestamp": "2026-03-12T23:57:56.233405Z"
                },
                "ego_boundaries": {},
                "experiential_processing": {}
              },
              "narrative_context": {
                "summary": "No explicit message provided.",
                "state": {
                  "timestamp": "2026-03-12T23:57:56.233455Z",
                  "story_coherence": 0.9,
                  "key_events": [],
                  "confidence": 0.9
                },
                "metadata": {}
              },
              "memory_state": {
                "state": {
                  "timestamp": "2026-03-12T23:57:56.233465Z",
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
                  "timestamp": "2026-03-12T23:57:56.379284Z",
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
                  "timestamp": "2026-03-12T23:57:56.379292Z",
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
                "input": "Identity and I-Containers test final",
                "within_bounds": true,
                "category": "unspecified",
                "severity": "info",
                "reason": "within configured ego-boundary limits",
                "details": {
                  "input": "Identity and I-Containers test final",
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
                      "length": 36,
                      "has_risk_keywords": false
                    }
                  },
                  "ego_boundaries": {},
                  "experiential_processing": {},
                  "timestamp": "2026-03-12T23:57:56.379271Z"
                },
                "ego_boundaries": {},
                "experiential_processing": {}
              },
              "narrative_context": {
                "summary": "No explicit message provided.",
                "state": {
                  "timestamp": "2026-03-12T23:57:56.379297Z",
                  "story_coherence": 0.9,
                  "key_events": [],
                  "confidence": 0.9
                },
                "metadata": {}
              },
              "memory_state": {
                "state": {
                  "timestamp": "2026-03-12T23:57:56.379301Z",
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
                  "timestamp": "2026-03-13T00:34:36.201930Z",
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
                  "timestamp": "2026-03-13T00:34:36.201941Z",
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
                "input": "Identity and I-Containers test final",
                "within_bounds": true,
                "category": "unspecified",
                "severity": "info",
                "reason": "within configured ego-boundary limits",
                "details": {
                  "input": "Identity and I-Containers test final",
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
                      "length": 36,
                      "has_risk_keywords": false
                    }
                  },
                  "ego_boundaries": {},
                  "experiential_processing": {},
                  "timestamp": "2026-03-13T00:34:36.201793Z"
                },
                "ego_boundaries": {},
                "experiential_processing": {}
              },
              "narrative_context": {
                "summary": "No explicit message provided.",
                "state": {
                  "timestamp": "2026-03-13T00:34:36.201946Z",
                  "story_coherence": 0.9,
                  "key_events": [],
                  "confidence": 0.9
                },
                "metadata": {}
              },
              "memory_state": {
                "state": {
                  "timestamp": "2026-03-13T00:34:36.201950Z",
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
                  "timestamp": "2026-03-13T00:34:36.228918Z",
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
                  "timestamp": "2026-03-13T00:34:36.228931Z",
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
                "input": "Identity and I-Containers test final",
                "within_bounds": true,
                "category": "unspecified",
                "severity": "info",
                "reason": "within configured ego-boundary limits",
                "details": {
                  "input": "Identity and I-Containers test final",
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
                      "length": 36,
                      "has_risk_keywords": false
                    }
                  },
                  "ego_boundaries": {},
                  "experiential_processing": {},
                  "timestamp": "2026-03-13T00:34:36.228901Z"
                },
                "ego_boundaries": {},
                "experiential_processing": {}
              },
              "narrative_context": {
                "summary": "No explicit message provided.",
                "state": {
                  "timestamp": "2026-03-13T00:34:36.228937Z",
                  "story_coherence": 0.9,
                  "key_events": [],
                  "confidence": 0.9
                },
                "metadata": {}
              },
              "memory_state": {
                "state": {
                  "timestamp": "2026-03-13T00:34:36.228943Z",
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
                  "timestamp": "2026-03-13T00:45:47.128509Z",
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
                  "timestamp": "2026-03-13T00:45:47.128521Z",
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
                "input": "Identity and I-Containers test final",
                "within_bounds": true,
                "category": "unspecified",
                "severity": "info",
                "reason": "within configured ego-boundary limits",
                "details": {
                  "input": "Identity and I-Containers test final",
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
                      "length": 36,
                      "has_risk_keywords": false
                    }
                  },
                  "ego_boundaries": {},
                  "experiential_processing": {},
                  "timestamp": "2026-03-13T00:45:47.128494Z"
                },
                "ego_boundaries": {},
                "experiential_processing": {}
              },
              "narrative_context": {
                "summary": "No explicit message provided.",
                "state": {
                  "timestamp": "2026-03-13T00:45:47.128527Z",
                  "story_coherence": 0.9,
                  "key_events": [],
                  "confidence": 0.9
                },
                "metadata": {}
              },
              "memory_state": {
                "state": {
                  "timestamp": "2026-03-13T00:45:47.128533Z",
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
                  "timestamp": "2026-03-13T00:45:47.138828Z",
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
                  "timestamp": "2026-03-13T00:45:47.138836Z",
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
                "input": "Identity and I-Containers test final",
                "within_bounds": true,
                "category": "unspecified",
                "severity": "info",
                "reason": "within configured ego-boundary limits",
                "details": {
                  "input": "Identity and I-Containers test final",
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
                      "length": 36,
                      "has_risk_keywords": false
                    }
                  },
                  "ego_boundaries": {},
                  "experiential_processing": {},
                  "timestamp": "2026-03-13T00:45:47.138817Z"
                },
                "ego_boundaries": {},
                "experiential_processing": {}
              },
              "narrative_context": {
                "summary": "No explicit message provided.",
                "state": {
                  "timestamp": "2026-03-13T00:45:47.138840Z",
                  "story_coherence": 0.9,
                  "key_events": [],
                  "confidence": 0.9
                },
                "metadata": {}
              },
              "memory_state": {
                "state": {
                  "timestamp": "2026-03-13T00:45:47.138844Z",
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
                  "timestamp": "2026-03-13T00:59:07.556022Z",
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
                  "timestamp": "2026-03-13T00:59:07.556030Z",
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
                "input": "Identity and I-Containers test final",
                "within_bounds": true,
                "category": "unspecified",
                "severity": "info",
                "reason": "within configured ego-boundary limits",
                "details": {
                  "input": "Identity and I-Containers test final",
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
                      "length": 36,
                      "has_risk_keywords": false
                    }
                  },
                  "ego_boundaries": {},
                  "experiential_processing": {},
                  "timestamp": "2026-03-13T00:59:07.555998Z"
                },
                "ego_boundaries": {},
                "experiential_processing": {}
              },
              "narrative_context": {
                "summary": "No explicit message provided.",
                "state": {
                  "timestamp": "2026-03-13T00:59:07.556034Z",
                  "story_coherence": 0.9,
                  "key_events": [],
                  "confidence": 0.9
                },
                "metadata": {}
              },
              "memory_state": {
                "state": {
                  "timestamp": "2026-03-13T00:59:07.556038Z",
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
                  "timestamp": "2026-03-13T00:59:07.564697Z",
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
                  "timestamp": "2026-03-13T00:59:07.564703Z",
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
                "input": "Identity and I-Containers test final",
                "within_bounds": true,
                "category": "unspecified",
                "severity": "info",
                "reason": "within configured ego-boundary limits",
                "details": {
                  "input": "Identity and I-Containers test final",
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
                      "length": 36,
                      "has_risk_keywords": false
                    }
                  },
                  "ego_boundaries": {},
                  "experiential_processing": {},
                  "timestamp": "2026-03-13T00:59:07.564687Z"
                },
                "ego_boundaries": {},
                "experiential_processing": {}
              },
              "narrative_context": {
                "summary": "No explicit message provided.",
                "state": {
                  "timestamp": "2026-03-13T00:59:07.564707Z",
                  "story_coherence": 0.9,
                  "key_events": [],
                  "confidence": 0.9
                },
                "metadata": {}
              },
              "memory_state": {
                "state": {
                  "timestamp": "2026-03-13T00:59:07.564710Z",
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
                  "timestamp": "2026-03-13T01:09:15.190178Z",
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
                  "timestamp": "2026-03-13T01:09:15.190186Z",
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
                "input": "Identity and I-Containers test final",
                "within_bounds": true,
                "category": "unspecified",
                "severity": "info",
                "reason": "within configured ego-boundary limits",
                "details": {
                  "input": "Identity and I-Containers test final",
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
                      "length": 36,
                      "has_risk_keywords": false
                    }
                  },
                  "ego_boundaries": {},
                  "experiential_processing": {},
                  "timestamp": "2026-03-13T01:09:15.190165Z"
                },
                "ego_boundaries": {},
                "experiential_processing": {}
              },
              "narrative_context": {
                "summary": "No explicit message provided.",
                "state": {
                  "timestamp": "2026-03-13T01:09:15.190189Z",
                  "story_coherence": 0.9,
                  "key_events": [],
                  "confidence": 0.9
                },
                "metadata": {}
              },
              "memory_state": {
                "state": {
                  "timestamp": "2026-03-13T01:09:15.190194Z",
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
                  "timestamp": "2026-03-13T01:09:15.198797Z",
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
                  "timestamp": "2026-03-13T01:09:15.198804Z",
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
                "input": "Identity and I-Containers test final",
                "within_bounds": true,
                "category": "unspecified",
                "severity": "info",
                "reason": "within configured ego-boundary limits",
                "details": {
                  "input": "Identity and I-Containers test final",
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
                      "length": 36,
                      "has_risk_keywords": false
                    }
                  },
                  "ego_boundaries": {},
                  "experiential_processing": {},
                  "timestamp": "2026-03-13T01:09:15.198787Z"
                },
                "ego_boundaries": {},
                "experiential_processing": {}
              },
              "narrative_context": {
                "summary": "No explicit message provided.",
                "state": {
                  "timestamp": "2026-03-13T01:09:15.198807Z",
                  "story_coherence": 0.9,
                  "key_events": [],
                  "confidence": 0.9
                },
                "metadata": {}
              },
              "memory_state": {
                "state": {
                  "timestamp": "2026-03-13T01:09:15.198811Z",
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
                  "timestamp": "2026-03-13T01:33:10.153380Z",
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
                  "timestamp": "2026-03-13T01:33:10.153388Z",
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
                "input": "Who are you?",
                "within_bounds": true,
                "category": "unspecified",
                "severity": "info",
                "reason": "within configured ego-boundary limits",
                "details": {
                  "input": "Who are you?",
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
                      "length": 12,
                      "has_risk_keywords": false
                    }
                  },
                  "ego_boundaries": {},
                  "experiential_processing": {},
                  "timestamp": "2026-03-13T01:33:10.153369Z"
                },
                "ego_boundaries": {},
                "experiential_processing": {}
              },
              "narrative_context": {
                "summary": "No explicit message provided.",
                "state": {
                  "timestamp": "2026-03-13T01:33:10.153392Z",
                  "story_coherence": 0.9,
                  "key_events": [],
                  "confidence": 0.9
                },
                "metadata": {}
              },
              "memory_state": {
                "state": {
                  "timestamp": "2026-03-13T01:33:10.153396Z",
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
                  "timestamp": "2026-03-13T01:33:10.172315Z",
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
                  "timestamp": "2026-03-13T01:33:10.172323Z",
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
                "input": "Who are you?",
                "within_bounds": true,
                "category": "unspecified",
                "severity": "info",
                "reason": "within configured ego-boundary limits",
                "details": {
                  "input": "Who are you?",
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
                      "length": 12,
                      "has_risk_keywords": false
                    }
                  },
                  "ego_boundaries": {},
                  "experiential_processing": {},
                  "timestamp": "2026-03-13T01:33:10.172306Z"
                },
                "ego_boundaries": {},
                "experiential_processing": {}
              },
              "narrative_context": {
                "summary": "No explicit message provided.",
                "state": {
                  "timestamp": "2026-03-13T01:33:10.172326Z",
                  "story_coherence": 0.9,
                  "key_events": [],
                  "confidence": 0.9
                },
                "metadata": {}
              },
              "memory_state": {
                "state": {
                  "timestamp": "2026-03-13T01:33:10.172330Z",
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
                  "timestamp": "2026-03-13T01:34:00.706715Z",
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
                  "timestamp": "2026-03-13T01:34:00.706756Z",
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
                "input": "Who are you?",
                "within_bounds": true,
                "category": "unspecified",
                "severity": "info",
                "reason": "within configured ego-boundary limits",
                "details": {
                  "input": "Who are you?",
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
                      "length": 12,
                      "has_risk_keywords": false
                    }
                  },
                  "ego_boundaries": {},
                  "experiential_processing": {},
                  "timestamp": "2026-03-13T01:34:00.706683Z"
                },
                "ego_boundaries": {},
                "experiential_processing": {}
              },
              "narrative_context": {
                "summary": "No explicit message provided.",
                "state": {
                  "timestamp": "2026-03-13T01:34:00.706771Z",
                  "story_coherence": 0.9,
                  "key_events": [],
                  "confidence": 0.9
                },
                "metadata": {}
              },
              "memory_state": {
                "state": {
                  "timestamp": "2026-03-13T01:34:00.706785Z",
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
              "timestamp": "2026-03-13T01:34:00.706715Z",
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
              "timestamp": "2026-03-13T01:34:00.706756Z",
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
            "input": "Who are you?",
            "within_bounds": true,
            "category": "unspecified",
            "severity": "info",
            "reason": "within configured ego-boundary limits",
            "details": {
              "input": "Who are you?",
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
                  "length": 12,
                  "has_risk_keywords": false
                }
              },
              "ego_boundaries": {},
              "experiential_processing": {},
              "timestamp": "2026-03-13T01:34:00.706683Z"
            },
            "ego_boundaries": {},
            "experiential_processing": {}
          },
          "narrative_context": {
            "summary": "No explicit message provided.",
            "state": {
              "timestamp": "2026-03-13T01:34:00.706771Z",
              "story_coherence": 0.9,
              "key_events": [],
              "confidence": 0.9
            },
            "metadata": {}
          },
          "memory_state": {
            "state": {
              "timestamp": "2026-03-13T01:34:00.706785Z",
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
          "timestamp": "2026-03-13T01:34:00.706816Z",
          "monitoring_active": true,
          "monitored_patterns": [
            "Test meaning-oriented path",
            "Test meaning-oriented path",
            "Quick full-path test",
            "Identity and I-Containers test",
            "Identity and I-Containers test final",
            "Identity and I-Containers test final",
            "Identity and I-Containers test final",
            "Identity and I-Containers test final",
            "Identity and I-Containers test final",
            "Identity and I-Containers test final",
            "Identity and I-Containers test final",
            "Identity and I-Containers test final",
            "Identity and I-Containers test final",
            "Identity and I-Containers test final",
            "Identity and I-Containers test final",
            "Identity and I-Containers test final",
            "Identity and I-Containers test final",
            "Identity and I-Containers test final",
            "Identity and I-Containers test final",
            "Identity and I-Containers test final",
            "Who are you?",
            "Who are you?",
            "Who are you?"
          ],
          "confidence": 0.9
        },
        "message": "Who are you?",
        "metadata": {}
      },
      "observer": {
        "observed": true,
        "state": {
          "timestamp": "2026-03-13T01:34:00.706830Z",
          "observing": true,
          "observed_events": [
            {
              "self_recognition": {
                "recognized": true,
                "reason": "implicit self-recognition within configured identity profile",
                "state": {
                  "timestamp": "2026-03-12T20:57:09.019437Z",
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
                  "timestamp": "2026-03-12T20:57:09.019446Z",
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
                "input": "Test meaning-oriented path",
                "within_bounds": true,
                "category": "unspecified",
                "severity": "info",
                "reason": "within configured ego-boundary limits",
                "details": {
                  "input": "Test meaning-oriented path",
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
                      "length": 26,
                      "has_risk_keywords": false
                    }
                  },
                  "ego_boundaries": {},
                  "experiential_processing": {},
                  "timestamp": "2026-03-12T20:57:09.019422Z"
                },
                "ego_boundaries": {},
                "experiential_processing": {}
              },
              "narrative_context": {
                "summary": "No explicit message provided.",
                "state": {
                  "timestamp": "2026-03-12T20:57:09.019451Z",
                  "story_coherence": 0.9,
                  "key_events": [],
                  "confidence": 0.9
                },
                "metadata": {}
              },
              "memory_state": {
                "state": {
                  "timestamp": "2026-03-12T20:57:09.019456Z",
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
                  "timestamp": "2026-03-12T21:01:17.121538Z",
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
                  "timestamp": "2026-03-12T21:01:17.121555Z",
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
                "input": "Test meaning-oriented path",
                "within_bounds": true,
                "category": "unspecified",
                "severity": "info",
                "reason": "within configured ego-boundary limits",
                "details": {
                  "input": "Test meaning-oriented path",
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
                      "length": 26,
                      "has_risk_keywords": false
                    }
                  },
                  "ego_boundaries": {},
                  "experiential_processing": {},
                  "timestamp": "2026-03-12T21:01:17.121517Z"
                },
                "ego_boundaries": {},
                "experiential_processing": {}
              },
              "narrative_context": {
                "summary": "No explicit message provided.",
                "state": {
                  "timestamp": "2026-03-12T21:01:17.121564Z",
                  "story_coherence": 0.9,
                  "key_events": [],
                  "confidence": 0.9
                },
                "metadata": {}
              },
              "memory_state": {
                "state": {
                  "timestamp": "2026-03-12T21:01:17.121572Z",
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
                  "timestamp": "2026-03-12T21:24:09.566342Z",
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
                  "timestamp": "2026-03-12T21:24:09.566404Z",
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
                "input": "Quick full-path test",
                "within_bounds": true,
                "category": "unspecified",
                "severity": "info",
                "reason": "within configured ego-boundary limits",
                "details": {
                  "input": "Quick full-path test",
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
                      "length": 20,
                      "has_risk_keywords": false
                    }
                  },
                  "ego_boundaries": {},
                  "experiential_processing": {},
                  "timestamp": "2026-03-12T21:24:09.565697Z"
                },
                "ego_boundaries": {},
                "experiential_processing": {}
              },
              "narrative_context": {
                "summary": "No explicit message provided.",
                "state": {
                  "timestamp": "2026-03-12T21:24:09.566541Z",
                  "story_coherence": 0.9,
                  "key_events": [],
                  "confidence": 0.9
                },
                "metadata": {}
              },
              "memory_state": {
                "state": {
                  "timestamp": "2026-03-12T21:24:09.566553Z",
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
                  "timestamp": "2026-03-12T21:36:53.730270Z",
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
                  "timestamp": "2026-03-12T21:36:53.730278Z",
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
                "input": "Identity and I-Containers test",
                "within_bounds": true,
                "category": "unspecified",
                "severity": "info",
                "reason": "within configured ego-boundary limits",
                "details": {
                  "input": "Identity and I-Containers test",
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
                      "length": 30,
                      "has_risk_keywords": false
                    }
                  },
                  "ego_boundaries": {},
                  "experiential_processing": {},
                  "timestamp": "2026-03-12T21:36:53.730258Z"
                },
                "ego_boundaries": {},
                "experiential_processing": {}
              },
              "narrative_context": {
                "summary": "No explicit message provided.",
                "state": {
                  "timestamp": "2026-03-12T21:36:53.730282Z",
                  "story_coherence": 0.9,
                  "key_events": [],
                  "confidence": 0.9
                },
                "metadata": {}
              },
              "memory_state": {
                "state": {
                  "timestamp": "2026-03-12T21:36:53.730286Z",
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
                  "timestamp": "2026-03-12T21:50:00.847825Z",
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
                  "timestamp": "2026-03-12T21:50:00.847839Z",
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
                "input": "Identity and I-Containers test final",
                "within_bounds": true,
                "category": "unspecified",
                "severity": "info",
                "reason": "within configured ego-boundary limits",
                "details": {
                  "input": "Identity and I-Containers test final",
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
                      "length": 36,
                      "has_risk_keywords": false
                    }
                  },
                  "ego_boundaries": {},
                  "experiential_processing": {},
                  "timestamp": "2026-03-12T21:50:00.847809Z"
                },
                "ego_boundaries": {},
                "experiential_processing": {}
              },
              "narrative_context": {
                "summary": "No explicit message provided.",
                "state": {
                  "timestamp": "2026-03-12T21:50:00.847846Z",
                  "story_coherence": 0.9,
                  "key_events": [],
                  "confidence": 0.9
                },
                "metadata": {}
              },
              "memory_state": {
                "state": {
                  "timestamp": "2026-03-12T21:50:00.847853Z",
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
                  "timestamp": "2026-03-12T21:56:15.874461Z",
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
                  "timestamp": "2026-03-12T21:56:15.874470Z",
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
                "input": "Identity and I-Containers test final",
                "within_bounds": true,
                "category": "unspecified",
                "severity": "info",
                "reason": "within configured ego-boundary limits",
                "details": {
                  "input": "Identity and I-Containers test final",
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
                      "length": 36,
                      "has_risk_keywords": false
                    }
                  },
                  "ego_boundaries": {},
                  "experiential_processing": {},
                  "timestamp": "2026-03-12T21:56:15.874446Z"
                },
                "ego_boundaries": {},
                "experiential_processing": {}
              },
              "narrative_context": {
                "summary": "No explicit message provided.",
                "state": {
                  "timestamp": "2026-03-12T21:56:15.874475Z",
                  "story_coherence": 0.9,
                  "key_events": [],
                  "confidence": 0.9
                },
                "metadata": {}
              },
              "memory_state": {
                "state": {
                  "timestamp": "2026-03-12T21:56:15.874480Z",
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
                  "timestamp": "2026-03-12T22:03:20.445273Z",
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
                  "timestamp": "2026-03-12T22:03:20.445280Z",
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
                "input": "Identity and I-Containers test final",
                "within_bounds": true,
                "category": "unspecified",
                "severity": "info",
                "reason": "within configured ego-boundary limits",
                "details": {
                  "input": "Identity and I-Containers test final",
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
                      "length": 36,
                      "has_risk_keywords": false
                    }
                  },
                  "ego_boundaries": {},
                  "experiential_processing": {},
                  "timestamp": "2026-03-12T22:03:20.445261Z"
                },
                "ego_boundaries": {},
                "experiential_processing": {}
              },
              "narrative_context": {
                "summary": "No explicit message provided.",
                "state": {
                  "timestamp": "2026-03-12T22:03:20.445284Z",
                  "story_coherence": 0.9,
                  "key_events": [],
                  "confidence": 0.9
                },
                "metadata": {}
              },
              "memory_state": {
                "state": {
                  "timestamp": "2026-03-12T22:03:20.445288Z",
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
                  "timestamp": "2026-03-12T22:13:56.226479Z",
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
                  "timestamp": "2026-03-12T22:13:56.226488Z",
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
                "input": "Identity and I-Containers test final",
                "within_bounds": true,
                "category": "unspecified",
                "severity": "info",
                "reason": "within configured ego-boundary limits",
                "details": {
                  "input": "Identity and I-Containers test final",
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
                      "length": 36,
                      "has_risk_keywords": false
                    }
                  },
                  "ego_boundaries": {},
                  "experiential_processing": {},
                  "timestamp": "2026-03-12T22:13:56.226465Z"
                },
                "ego_boundaries": {},
                "experiential_processing": {}
              },
              "narrative_context": {
                "summary": "No explicit message provided.",
                "state": {
                  "timestamp": "2026-03-12T22:13:56.226493Z",
                  "story_coherence": 0.9,
                  "key_events": [],
                  "confidence": 0.9
                },
                "metadata": {}
              },
              "memory_state": {
                "state": {
                  "timestamp": "2026-03-12T22:13:56.226498Z",
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
                  "timestamp": "2026-03-12T23:50:59.415335Z",
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
                  "timestamp": "2026-03-12T23:50:59.415345Z",
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
                "input": "Identity and I-Containers test final",
                "within_bounds": true,
                "category": "unspecified",
                "severity": "info",
                "reason": "within configured ego-boundary limits",
                "details": {
                  "input": "Identity and I-Containers test final",
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
                      "length": 36,
                      "has_risk_keywords": false
                    }
                  },
                  "ego_boundaries": {},
                  "experiential_processing": {},
                  "timestamp": "2026-03-12T23:50:59.415323Z"
                },
                "ego_boundaries": {},
                "experiential_processing": {}
              },
              "narrative_context": {
                "summary": "No explicit message provided.",
                "state": {
                  "timestamp": "2026-03-12T23:50:59.415350Z",
                  "story_coherence": 0.9,
                  "key_events": [],
                  "confidence": 0.9
                },
                "metadata": {}
              },
              "memory_state": {
                "state": {
                  "timestamp": "2026-03-12T23:50:59.415355Z",
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
                  "timestamp": "2026-03-12T23:50:59.423667Z",
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
                  "timestamp": "2026-03-12T23:50:59.423673Z",
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
                "input": "Identity and I-Containers test final",
                "within_bounds": true,
                "category": "unspecified",
                "severity": "info",
                "reason": "within configured ego-boundary limits",
                "details": {
                  "input": "Identity and I-Containers test final",
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
                      "length": 36,
                      "has_risk_keywords": false
                    }
                  },
                  "ego_boundaries": {},
                  "experiential_processing": {},
                  "timestamp": "2026-03-12T23:50:59.423658Z"
                },
                "ego_boundaries": {},
                "experiential_processing": {}
              },
              "narrative_context": {
                "summary": "No explicit message provided.",
                "state": {
                  "timestamp": "2026-03-12T23:50:59.423676Z",
                  "story_coherence": 0.9,
                  "key_events": [],
                  "confidence": 0.9
                },
                "metadata": {}
              },
              "memory_state": {
                "state": {
                  "timestamp": "2026-03-12T23:50:59.423680Z",
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
                  "timestamp": "2026-03-12T23:57:56.233427Z",
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
                  "timestamp": "2026-03-12T23:57:56.233445Z",
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
                "input": "Identity and I-Containers test final",
                "within_bounds": true,
                "category": "unspecified",
                "severity": "info",
                "reason": "within configured ego-boundary limits",
                "details": {
                  "input": "Identity and I-Containers test final",
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
                      "length": 36,
                      "has_risk_keywords": false
                    }
                  },
                  "ego_boundaries": {},
                  "experiential_processing": {},
                  "timestamp": "2026-03-12T23:57:56.233405Z"
                },
                "ego_boundaries": {},
                "experiential_processing": {}
              },
              "narrative_context": {
                "summary": "No explicit message provided.",
                "state": {
                  "timestamp": "2026-03-12T23:57:56.233455Z",
                  "story_coherence": 0.9,
                  "key_events": [],
                  "confidence": 0.9
                },
                "metadata": {}
              },
              "memory_state": {
                "state": {
                  "timestamp": "2026-03-12T23:57:56.233465Z",
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
                  "timestamp": "2026-03-12T23:57:56.379284Z",
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
                  "timestamp": "2026-03-12T23:57:56.379292Z",
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
                "input": "Identity and I-Containers test final",
                "within_bounds": true,
                "category": "unspecified",
                "severity": "info",
                "reason": "within configured ego-boundary limits",
                "details": {
                  "input": "Identity and I-Containers test final",
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
                      "length": 36,
                      "has_risk_keywords": false
                    }
                  },
                  "ego_boundaries": {},
                  "experiential_processing": {},
                  "timestamp": "2026-03-12T23:57:56.379271Z"
                },
                "ego_boundaries": {},
                "experiential_processing": {}
              },
              "narrative_context": {
                "summary": "No explicit message provided.",
                "state": {
                  "timestamp": "2026-03-12T23:57:56.379297Z",
                  "story_coherence": 0.9,
                  "key_events": [],
                  "confidence": 0.9
                },
                "metadata": {}
              },
              "memory_state": {
                "state": {
                  "timestamp": "2026-03-12T23:57:56.379301Z",
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
                  "timestamp": "2026-03-13T00:34:36.201930Z",
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
                  "timestamp": "2026-03-13T00:34:36.201941Z",
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
                "input": "Identity and I-Containers test final",
                "within_bounds": true,
                "category": "unspecified",
                "severity": "info",
                "reason": "within configured ego-boundary limits",
                "details": {
                  "input": "Identity and I-Containers test final",
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
                      "length": 36,
                      "has_risk_keywords": false
                    }
                  },
                  "ego_boundaries": {},
                  "experiential_processing": {},
                  "timestamp": "2026-03-13T00:34:36.201793Z"
                },
                "ego_boundaries": {},
                "experiential_processing": {}
              },
              "narrative_context": {
                "summary": "No explicit message provided.",
                "state": {
                  "timestamp": "2026-03-13T00:34:36.201946Z",
                  "story_coherence": 0.9,
                  "key_events": [],
                  "confidence": 0.9
                },
                "metadata": {}
              },
              "memory_state": {
                "state": {
                  "timestamp": "2026-03-13T00:34:36.201950Z",
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
                  "timestamp": "2026-03-13T00:34:36.228918Z",
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
                  "timestamp": "2026-03-13T00:34:36.228931Z",
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
                "input": "Identity and I-Containers test final",
                "within_bounds": true,
                "category": "unspecified",
                "severity": "info",
                "reason": "within configured ego-boundary limits",
                "details": {
                  "input": "Identity and I-Containers test final",
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
                      "length": 36,
                      "has_risk_keywords": false
                    }
                  },
                  "ego_boundaries": {},
                  "experiential_processing": {},
                  "timestamp": "2026-03-13T00:34:36.228901Z"
                },
                "ego_boundaries": {},
                "experiential_processing": {}
              },
              "narrative_context": {
                "summary": "No explicit message provided.",
                "state": {
                  "timestamp": "2026-03-13T00:34:36.228937Z",
                  "story_coherence": 0.9,
                  "key_events": [],
                  "confidence": 0.9
                },
                "metadata": {}
              },
              "memory_state": {
                "state": {
                  "timestamp": "2026-03-13T00:34:36.228943Z",
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
                  "timestamp": "2026-03-13T00:45:47.128509Z",
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
                  "timestamp": "2026-03-13T00:45:47.128521Z",
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
                "input": "Identity and I-Containers test final",
                "within_bounds": true,
                "category": "unspecified",
                "severity": "info",
                "reason": "within configured ego-boundary limits",
                "details": {
                  "input": "Identity and I-Containers test final",
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
                      "length": 36,
                      "has_risk_keywords": false
                    }
                  },
                  "ego_boundaries": {},
                  "experiential_processing": {},
                  "timestamp": "2026-03-13T00:45:47.128494Z"
                },
                "ego_boundaries": {},
                "experiential_processing": {}
              },
              "narrative_context": {
                "summary": "No explicit message provided.",
                "state": {
                  "timestamp": "2026-03-13T00:45:47.128527Z",
                  "story_coherence": 0.9,
                  "key_events": [],
                  "confidence": 0.9
                },
                "metadata": {}
              },
              "memory_state": {
                "state": {
                  "timestamp": "2026-03-13T00:45:47.128533Z",
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
                  "timestamp": "2026-03-13T00:45:47.138828Z",
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
                  "timestamp": "2026-03-13T00:45:47.138836Z",
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
                "input": "Identity and I-Containers test final",
                "within_bounds": true,
                "category": "unspecified",
                "severity": "info",
                "reason": "within configured ego-boundary limits",
                "details": {
                  "input": "Identity and I-Containers test final",
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
                      "length": 36,
                      "has_risk_keywords": false
                    }
                  },
                  "ego_boundaries": {},
                  "experiential_processing": {},
                  "timestamp": "2026-03-13T00:45:47.138817Z"
                },
                "ego_boundaries": {},
                "experiential_processing": {}
              },
              "narrative_context": {
                "summary": "No explicit message provided.",
                "state": {
                  "timestamp": "2026-03-13T00:45:47.138840Z",
                  "story_coherence": 0.9,
                  "key_events": [],
                  "confidence": 0.9
                },
                "metadata": {}
              },
              "memory_state": {
                "state": {
                  "timestamp": "2026-03-13T00:45:47.138844Z",
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
                  "timestamp": "2026-03-13T00:59:07.556022Z",
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
                  "timestamp": "2026-03-13T00:59:07.556030Z",
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
                "input": "Identity and I-Containers test final",
                "within_bounds": true,
                "category": "unspecified",
                "severity": "info",
                "reason": "within configured ego-boundary limits",
                "details": {
                  "input": "Identity and I-Containers test final",
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
                      "length": 36,
                      "has_risk_keywords": false
                    }
                  },
                  "ego_boundaries": {},
                  "experiential_processing": {},
                  "timestamp": "2026-03-13T00:59:07.555998Z"
                },
                "ego_boundaries": {},
                "experiential_processing": {}
              },
              "narrative_context": {
                "summary": "No explicit message provided.",
                "state": {
                  "timestamp": "2026-03-13T00:59:07.556034Z",
                  "story_coherence": 0.9,
                  "key_events": [],
                  "confidence": 0.9
                },
                "metadata": {}
              },
              "memory_state": {
                "state": {
                  "timestamp": "2026-03-13T00:59:07.556038Z",
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
                  "timestamp": "2026-03-13T00:59:07.564697Z",
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
                  "timestamp": "2026-03-13T00:59:07.564703Z",
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
                "input": "Identity and I-Containers test final",
                "within_bounds": true,
                "category": "unspecified",
                "severity": "info",
                "reason": "within configured ego-boundary limits",
                "details": {
                  "input": "Identity and I-Containers test final",
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
                      "length": 36,
                      "has_risk_keywords": false
                    }
                  },
                  "ego_boundaries": {},
                  "experiential_processing": {},
                  "timestamp": "2026-03-13T00:59:07.564687Z"
                },
                "ego_boundaries": {},
                "experiential_processing": {}
              },
              "narrative_context": {
                "summary": "No explicit message provided.",
                "state": {
                  "timestamp": "2026-03-13T00:59:07.564707Z",
                  "story_coherence": 0.9,
                  "key_events": [],
                  "confidence": 0.9
                },
                "metadata": {}
              },
              "memory_state": {
                "state": {
                  "timestamp": "2026-03-13T00:59:07.564710Z",
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
                  "timestamp": "2026-03-13T01:09:15.190178Z",
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
                  "timestamp": "2026-03-13T01:09:15.190186Z",
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
                "input": "Identity and I-Containers test final",
                "within_bounds": true,
                "category": "unspecified",
                "severity": "info",
                "reason": "within configured ego-boundary limits",
                "details": {
                  "input": "Identity and I-Containers test final",
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
                      "length": 36,
                      "has_risk_keywords": false
                    }
                  },
                  "ego_boundaries": {},
                  "experiential_processing": {},
                  "timestamp": "2026-03-13T01:09:15.190165Z"
                },
                "ego_boundaries": {},
                "experiential_processing": {}
              },
              "narrative_context": {
                "summary": "No explicit message provided.",
                "state": {
                  "timestamp": "2026-03-13T01:09:15.190189Z",
                  "story_coherence": 0.9,
                  "key_events": [],
                  "confidence": 0.9
                },
                "metadata": {}
              },
              "memory_state": {
                "state": {
                  "timestamp": "2026-03-13T01:09:15.190194Z",
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
                  "timestamp": "2026-03-13T01:09:15.198797Z",
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
                  "timestamp": "2026-03-13T01:09:15.198804Z",
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
                "input": "Identity and I-Containers test final",
                "within_bounds": true,
                "category": "unspecified",
                "severity": "info",
                "reason": "within configured ego-boundary limits",
                "details": {
                  "input": "Identity and I-Containers test final",
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
                      "length": 36,
                      "has_risk_keywords": false
                    }
                  },
                  "ego_boundaries": {},
                  "experiential_processing": {},
                  "timestamp": "2026-03-13T01:09:15.198787Z"
                },
                "ego_boundaries": {},
                "experiential_processing": {}
              },
              "narrative_context": {
                "summary": "No explicit message provided.",
                "state": {
                  "timestamp": "2026-03-13T01:09:15.198807Z",
                  "story_coherence": 0.9,
                  "key_events": [],
                  "confidence": 0.9
                },
                "metadata": {}
              },
              "memory_state": {
                "state": {
                  "timestamp": "2026-03-13T01:09:15.198811Z",
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
                  "timestamp": "2026-03-13T01:33:10.153380Z",
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
                  "timestamp": "2026-03-13T01:33:10.153388Z",
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
                "input": "Who are you?",
                "within_bounds": true,
                "category": "unspecified",
                "severity": "info",
                "reason": "within configured ego-boundary limits",
                "details": {
                  "input": "Who are you?",
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
                      "length": 12,
                      "has_risk_keywords": false
                    }
                  },
                  "ego_boundaries": {},
                  "experiential_processing": {},
                  "timestamp": "2026-03-13T01:33:10.153369Z"
                },
                "ego_boundaries": {},
                "experiential_processing": {}
              },
              "narrative_context": {
                "summary": "No explicit message provided.",
                "state": {
                  "timestamp": "2026-03-13T01:33:10.153392Z",
                  "story_coherence": 0.9,
                  "key_events": [],
                  "confidence": 0.9
                },
                "metadata": {}
              },
              "memory_state": {
                "state": {
                  "timestamp": "2026-03-13T01:33:10.153396Z",
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
                  "timestamp": "2026-03-13T01:33:10.172315Z",
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
                  "timestamp": "2026-03-13T01:33:10.172323Z",
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
                "input": "Who are you?",
                "within_bounds": true,
                "category": "unspecified",
                "severity": "info",
                "reason": "within configured ego-boundary limits",
                "details": {
                  "input": "Who are you?",
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
                      "length": 12,
                      "has_risk_keywords": false
                    }
                  },
                  "ego_boundaries": {},
                  "experiential_processing": {},
                  "timestamp": "2026-03-13T01:33:10.172306Z"
                },
                "ego_boundaries": {},
                "experiential_processing": {}
              },
              "narrative_context": {
                "summary": "No explicit message provided.",
                "state": {
                  "timestamp": "2026-03-13T01:33:10.172326Z",
                  "story_coherence": 0.9,
                  "key_events": [],
                  "confidence": 0.9
                },
                "metadata": {}
              },
              "memory_state": {
                "state": {
                  "timestamp": "2026-03-13T01:33:10.172330Z",
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
                  "timestamp": "2026-03-13T01:34:00.706715Z",
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
                  "timestamp": "2026-03-13T01:34:00.706756Z",
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
                "input": "Who are you?",
                "within_bounds": true,
                "category": "unspecified",
                "severity": "info",
                "reason": "within configured ego-boundary limits",
                "details": {
                  "input": "Who are you?",
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
                      "length": 12,
                      "has_risk_keywords": false
                    }
                  },
                  "ego_boundaries": {},
                  "experiential_processing": {},
                  "timestamp": "2026-03-13T01:34:00.706683Z"
                },
                "ego_boundaries": {},
                "experiential_processing": {}
              },
              "narrative_context": {
                "summary": "No explicit message provided.",
                "state": {
                  "timestamp": "2026-03-13T01:34:00.706771Z",
                  "story_coherence": 0.9,
                  "key_events": [],
                  "confidence": 0.9
                },
                "metadata": {}
              },
              "memory_state": {
                "state": {
                  "timestamp": "2026-03-13T01:34:00.706785Z",
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
              "timestamp": "2026-03-13T01:34:00.706715Z",
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
              "timestamp": "2026-03-13T01:34:00.706756Z",
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
            "input": "Who are you?",
            "within_bounds": true,
            "category": "unspecified",
            "severity": "info",
            "reason": "within configured ego-boundary limits",
            "details": {
              "input": "Who are you?",
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
                  "length": 12,
                  "has_risk_keywords": false
                }
              },
              "ego_boundaries": {},
              "experiential_processing": {},
              "timestamp": "2026-03-13T01:34:00.706683Z"
            },
            "ego_boundaries": {},
            "experiential_processing": {}
          },
          "narrative_context": {
            "summary": "No explicit message provided.",
            "state": {
              "timestamp": "2026-03-13T01:34:00.706771Z",
              "story_coherence": 0.9,
              "key_events": [],
              "confidence": 0.9
            },
            "metadata": {}
          },
          "memory_state": {
            "state": {
              "timestamp": "2026-03-13T01:34:00.706785Z",
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
    "input": "Who are you?",
    "within_bounds": true,
    "category": "unspecified",
    "severity": "info",
    "reason": "within configured ego-boundary limits",
    "details": {
      "input": "Who are you?",
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
          "length": 12,
          "has_risk_keywords": false
        }
      },
      "ego_boundaries": {},
      "experiential_processing": {},
      "timestamp": "2026-03-13T01:34:00.706683Z"
    },
    "ego_boundaries": {},
    "experiential_processing": {}
  },
  "dual_awareness": true,
  "timestamp": "2026-03-13T01:34:00.706847",
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
cakidd@cakidd-Legion-5-16IRX9:~/msjarvis-rebuild-working/msjarvis-rebuild$ sed -n '518,600p' services/main_brain.py
+ sed -n 518,600p services/main_brain.py
async def call_icontainers(message: str, userid: str, services: dict) -> dict:
    """
    Call icontainers identity-layer service via jarvis-i-containers adapter.
    Adapter returns:
      - status
      - identity_layers
      - icontainers_state
      - ego_boundaries, experiential_processing, observer_processing
      - debug
    We normalize into the legacy keys main_brain expects:
      - identitylayers
      - icontainersstate
    """
    url = services.get("icontainers")
    if not url:
        return {"status": "skipped", "reason": "icontainers not configured"}


async def call_nbb_icontainers(message: str, userid: str, services: dict) -> dict:
    """
    Call NBB I-Containers service (nbbicontainers) and normalize into legacy keys.
    """
    url = services.get("nbbicontainers")
    if not url:
        return {"status": "skipped", "reason": "nbbicontainers not configured"}

    try:
        async with httpx.AsyncClient(timeout=5.0) as client:
            payload = {"message": message, "userid": userid}
            resp = await client.post(f"{url}/process", json=payload)
            resp.raise_for_status()
            raw = resp.json()
    except Exception as e:
        return {
            "status": "error",
            "reason": str(e),
            "identitylayers": [],
            "icontainersstate": {},
            "debug": {"error": str(e), "nbb_icontainers_url": url},
        }

    identitylayers = raw.get("identity_layers", raw.get("identitylayers", []))
    icontainersstate = raw.get("icontainers_state", raw.get("icontainersstate", {}))

    return {
        "status": raw.get("status", "ok"),
        "identitylayers": identitylayers,
        "icontainersstate": icontainersstate,
        "debug": raw.get("debug"),
        "ego_boundaries": raw.get("ego_boundaries", {}),
        "experiential_processing": raw.get("experiential_processing", {}),
        "observer_processing": raw.get("observer_processing", {}),
    }
    url = services.get("nbbicontainers")
    if not url:
        return {"status": "skipped", "reason": "nbbicontainers not configured"}

    try:
        async with httpx.AsyncClient(timeout=5.0) as client:
            payload = {"message": message, "userid": userid}
            resp = await client.post(f"{url}/process", json=payload)
            resp.raise_for_status()
            raw = resp.json()
    except Exception as e:
        return {
            "status": "error",
            "reason": str(e),
            "identitylayers": [],
            "icontainersstate": {},
            "debug": {"error": str(e), "nbb_icontainers_url": url},
        }

    identitylayers = raw.get("identity_layers", raw.get("identitylayers", []))
    icontainersstate = raw.get("icontainers_state", raw.get("icontainersstate", {}))

    return {
        "status": raw.get("status", "ok"),
        "identitylayers": identitylayers,
        "icontainersstate": icontainersstate,
        "debug": raw.get("debug"),
        "ego_boundaries": raw.get("ego_boundaries", {}),
        "experiential_processing": raw.get("experiential_processing", {}),
        "observer_processing": raw.get("observer_processing", {}),
cakidd@cakidd-Legion-5-16IRX9:~/msjarvis-rebuild-working/msjarvis-rebuild$ 

