cakidd@cakidd-Legion-5-16IRX9:~/msjarvis-rebuild-working/msjarvis-rebuild$ # Correct port is 8002
# List collections
curl -s http://localhost:8002/api/v2/tenants/default_tenant/databases/default_database/collections \
  | python3 -m json.tool

# Test add directly
curl -s -X POST \
  http://localhost:8002/api/v2/tenants/default_tenant/databases/default_database/collections/0338d961-4f32-43ce-9afa-25ecb4ba0185/add \
  -H "Content-Type: application/json" \
  -d '{"ids":["test-1"],"documents":["test"],"embeddings":[[0.1,0.2]],"metadatas":[{"source":"test"}]}' \
  | python3 -m json.tool
[
    {
        "id": "02715c7c-7676-4cc1-8e9e-9c345bb332fe",
        "name": "msjarvis-smoke",
        "configuration_json": {
            "hnsw": {
                "space": "l2",
                "ef_construction": 100,
                "ef_search": 100,
                "max_neighbors": 16,
                "resize_factor": 1.2,
                "sync_threshold": 1000
            },
            "spann": null,
            "embedding_function": {
                "type": "known",
                "name": "default",
                "config": {}
            }
        },
        "schema": {
            "defaults": {
                "string": {
                    "fts_index": {
                        "enabled": false,
                        "config": {}
                    },
                    "string_inverted_index": {
                        "enabled": true,
                        "config": {}
                    }
                },
                "float_list": {
                    "vector_index": {
                        "enabled": false,
                        "config": {
                            "space": "l2",
                            "embedding_function": {
                                "type": "known",
                                "name": "default",
                                "config": {}
                            },
                            "hnsw": {
                                "ef_construction": 100,
                                "max_neighbors": 16,
                                "ef_search": 100,
                                "num_threads": 32,
                                "batch_size": 100,
                                "sync_threshold": 1000,
                                "resize_factor": 1.2
                            }
                        }
                    }
                },
                "sparse_vector": {
                    "sparse_vector_index": {
                        "enabled": false,
                        "config": {
                            "embedding_function": {
                                "type": "unknown"
                            },
                            "bm25": false
                        }
                    }
                },
                "int": {
                    "int_inverted_index": {
                        "enabled": true,
                        "config": {}
                    }
                },
                "float": {
                    "float_inverted_index": {
                        "enabled": true,
                        "config": {}
                    }
                },
                "bool": {
                    "bool_inverted_index": {
                        "enabled": true,
                        "config": {}
                    }
                }
            },
            "keys": {
                "#document": {
                    "string": {
                        "fts_index": {
                            "enabled": true,
                            "config": {}
                        },
                        "string_inverted_index": {
                            "enabled": false,
                            "config": {}
                        }
                    }
                },
                "source": {
                    "string": {
                        "fts_index": {
                            "enabled": false,
                            "config": {}
                        },
                        "string_inverted_index": {
                            "enabled": true,
                            "config": {}
                        }
                    }
                },
                "#embedding": {
                    "float_list": {
                        "vector_index": {
                            "enabled": true,
                            "config": {
                                "space": "l2",
                                "embedding_function": {
                                    "type": "known",
                                    "name": "default",
                                    "config": {}
                                },
                                "source_key": "#document",
                                "hnsw": {
                                    "ef_construction": 100,
                                    "max_neighbors": 16,
                                    "ef_search": 100,
                                    "num_threads": 32,
                                    "batch_size": 100,
                                    "sync_threshold": 1000,
                                    "resize_factor": 1.2
                                }
                            }
                        }
                    }
                }
            }
        },
        "metadata": null,
        "dimension": 384,
        "tenant": "default_tenant",
        "database": "default_database",
        "log_position": 0,
        "version": 0
    },
    {
        "id": "0338d961-4f32-43ce-9afa-25ecb4ba0185",
        "name": "fifth_dgm_subconscious",
        "configuration_json": {
            "hnsw": {
                "space": "l2",
                "ef_construction": 100,
                "ef_search": 100,
                "max_neighbors": 16,
                "resize_factor": 1.2,
                "sync_threshold": 1000
            },
            "spann": null,
            "embedding_function": {
                "type": "known",
                "name": "default",
                "config": {}
            }
        },
        "schema": {
            "defaults": {
                "string": {
                    "fts_index": {
                        "enabled": false,
                        "config": {}
                    },
                    "string_inverted_index": {
                        "enabled": true,
                        "config": {}
                    }
                },
                "float_list": {
                    "vector_index": {
                        "enabled": false,
                        "config": {
                            "space": "l2",
                            "embedding_function": {
                                "type": "known",
                                "name": "default",
                                "config": {}
                            },
                            "hnsw": {
                                "ef_construction": 100,
                                "max_neighbors": 16,
                                "ef_search": 100,
                                "num_threads": 32,
                                "batch_size": 100,
                                "sync_threshold": 1000,
                                "resize_factor": 1.2
                            }
                        }
                    }
                },
                "sparse_vector": {
                    "sparse_vector_index": {
                        "enabled": false,
                        "config": {
                            "embedding_function": {
                                "type": "unknown"
                            },
                            "bm25": false
                        }
                    }
                },
                "int": {
                    "int_inverted_index": {
                        "enabled": true,
                        "config": {}
                    }
                },
                "float": {
                    "float_inverted_index": {
                        "enabled": true,
                        "config": {}
                    }
                },
                "bool": {
                    "bool_inverted_index": {
                        "enabled": true,
                        "config": {}
                    }
                }
            },
            "keys": {
                "#embedding": {
                    "float_list": {
                        "vector_index": {
                            "enabled": true,
                            "config": {
                                "space": "l2",
                                "embedding_function": {
                                    "type": "known",
                                    "name": "default",
                                    "config": {}
                                },
                                "source_key": "#document",
                                "hnsw": {
                                    "ef_construction": 100,
                                    "max_neighbors": 16,
                                    "ef_search": 100,
                                    "num_threads": 32,
                                    "batch_size": 100,
                                    "sync_threshold": 1000,
                                    "resize_factor": 1.2
                                }
                            }
                        }
                    }
                },
                "#document": {
                    "string": {
                        "fts_index": {
                            "enabled": true,
                            "config": {}
                        },
                        "string_inverted_index": {
                            "enabled": false,
                            "config": {}
                        }
                    }
                },
                "type": {
                    "string": {
                        "fts_index": {
                            "enabled": false,
                            "config": {}
                        },
                        "string_inverted_index": {
                            "enabled": true,
                            "config": {}
                        }
                    }
                },
                "timestamp": {
                    "string": {
                        "fts_index": {
                            "enabled": false,
                            "config": {}
                        },
                        "string_inverted_index": {
                            "enabled": true,
                            "config": {}
                        }
                    }
                },
                "source": {
                    "string": {
                        "fts_index": {
                            "enabled": false,
                            "config": {}
                        },
                        "string_inverted_index": {
                            "enabled": true,
                            "config": {}
                        }
                    }
                }
            }
        },
        "metadata": null,
        "dimension": 384,
        "tenant": "default_tenant",
        "database": "default_database",
        "log_position": 0,
        "version": 0
    },
    {
        "id": "062ab0ff-f06a-4beb-ba61-81461f4079c8",
        "name": "safety_rules",
        "configuration_json": {
            "hnsw": {
                "space": "l2",
                "ef_construction": 100,
                "ef_search": 100,
                "max_neighbors": 16,
                "resize_factor": 1.2,
                "sync_threshold": 1000
            },
            "spann": null,
            "embedding_function": {
                "type": "known",
                "name": "default",
                "config": {}
            }
        },
        "schema": {
            "defaults": {
                "string": {
                    "fts_index": {
                        "enabled": false,
                        "config": {}
                    },
                    "string_inverted_index": {
                        "enabled": true,
                        "config": {}
                    }
                },
                "float_list": {
                    "vector_index": {
                        "enabled": false,
                        "config": {
                            "space": "l2",
                            "embedding_function": {
                                "type": "known",
                                "name": "default",
                                "config": {}
                            },
                            "hnsw": {
                                "ef_construction": 100,
                                "max_neighbors": 16,
                                "ef_search": 100,
                                "num_threads": 32,
                                "batch_size": 100,
                                "sync_threshold": 1000,
                                "resize_factor": 1.2
                            }
                        }
                    }
                },
                "sparse_vector": {
                    "sparse_vector_index": {
                        "enabled": false,
                        "config": {
                            "embedding_function": {
                                "type": "unknown"
                            },
                            "bm25": false
                        }
                    }
                },
                "int": {
                    "int_inverted_index": {
                        "enabled": true,
                        "config": {}
                    }
                },
                "float": {
                    "float_inverted_index": {
                        "enabled": true,
                        "config": {}
                    }
                },
                "bool": {
                    "bool_inverted_index": {
                        "enabled": true,
                        "config": {}
                    }
                }
            },
            "keys": {
                "category": {
                    "string": {
                        "fts_index": {
                            "enabled": false,
                            "config": {}
                        },
                        "string_inverted_index": {
                            "enabled": true,
                            "config": {}
                        }
                    }
                },
                "rule_id": {
                    "string": {
                        "fts_index": {
                            "enabled": false,
                            "config": {}
                        },
                        "string_inverted_index": {
                            "enabled": true,
                            "config": {}
                        }
                    }
                },
                "wv_tagged": {
                    "bool": {
                        "bool_inverted_index": {
                            "enabled": true,
                            "config": {}
                        }
                    }
                },
                "#document": {
                    "string": {
                        "fts_index": {
                            "enabled": true,
                            "config": {}
                        },
                        "string_inverted_index": {
                            "enabled": false,
                            "config": {}
                        }
                    }
                },
                "#embedding": {
                    "float_list": {
                        "vector_index": {
                            "enabled": true,
                            "config": {
                                "space": "l2",
                                "embedding_function": {
                                    "type": "known",
                                    "name": "default",
                                    "config": {}
                                },
                                "source_key": "#document",
                                "hnsw": {
                                    "ef_construction": 100,
                                    "max_neighbors": 16,
                                    "ef_search": 100,
                                    "num_threads": 32,
                                    "batch_size": 100,
                                    "sync_threshold": 1000,
                                    "resize_factor": 1.2
                                }
                            }
                        }
                    }
                }
            }
        },
        "metadata": {
            "status": "created_empty_2026-03-24",
            "wv_tagged": true,
            "description": "Safety constitutional rules \u2014 Ms. Jarvis ethical guardrails"
        },
        "dimension": 384,
        "tenant": "default_tenant",
        "database": "default_database",
        "log_position": 0,
        "version": 0
    },
    {
        "id": "0c88a778-02bf-475f-ba80-64b9f4467e84",
        "name": "economic_rag",
        "configuration_json": {
            "hnsw": {
                "space": "l2",
                "ef_construction": 100,
                "ef_search": 100,
                "max_neighbors": 16,
                "resize_factor": 1.2,
                "sync_threshold": 1000
            },
            "spann": null,
            "embedding_function": {
                "type": "known",
                "name": "default",
                "config": {}
            }
        },
        "schema": {
            "defaults": {
                "string": {
                    "fts_index": {
                        "enabled": false,
                        "config": {}
                    },
                    "string_inverted_index": {
                        "enabled": true,
                        "config": {}
                    }
                },
                "float_list": {
                    "vector_index": {
                        "enabled": false,
                        "config": {
                            "space": "l2",
                            "embedding_function": {
                                "type": "known",
                                "name": "default",
                                "config": {}
                            },
                            "hnsw": {
                                "ef_construction": 100,
                                "max_neighbors": 16,
                                "ef_search": 100,
                                "num_threads": 32,
                                "batch_size": 100,
                                "sync_threshold": 1000,
                                "resize_factor": 1.2
                            }
                        }
                    }
                },
                "sparse_vector": {
                    "sparse_vector_index": {
                        "enabled": false,
                        "config": {
                            "embedding_function": {
                                "type": "unknown"
                            },
                            "bm25": false
                        }
                    }
                },
                "int": {
                    "int_inverted_index": {
                        "enabled": true,
                        "config": {}
                    }
                },
                "float": {
                    "float_inverted_index": {
                        "enabled": true,
                        "config": {}
                    }
                },
                "bool": {
                    "bool_inverted_index": {
                        "enabled": true,
                        "config": {}
                    }
                }
            },
            "keys": {
                "wv_tagged": {
                    "bool": {
                        "bool_inverted_index": {
                            "enabled": true,
                            "config": {}
                        }
                    }
                },
                "category": {
                    "string": {
                        "fts_index": {
                            "enabled": false,
                            "config": {}
                        },
                        "string_inverted_index": {
                            "enabled": true,
                            "config": {}
                        }
                    }
                },
                "#embedding": {
                    "float_list": {
                        "vector_index": {
                            "enabled": true,
                            "config": {
                                "space": "l2",
                                "embedding_function": {
                                    "type": "known",
                                    "name": "default",
                                    "config": {}
                                },
                                "source_key": "#document",
                                "hnsw": {
                                    "ef_construction": 100,
                                    "max_neighbors": 16,
                                    "ef_search": 100,
                                    "num_threads": 32,
                                    "batch_size": 100,
                                    "sync_threshold": 1000,
                                    "resize_factor": 1.2
                                }
                            }
                        }
                    }
                },
                "#document": {
                    "string": {
                        "fts_index": {
                            "enabled": true,
                            "config": {}
                        },
                        "string_inverted_index": {
                            "enabled": false,
                            "config": {}
                        }
                    }
                }
            }
        },
        "metadata": {
            "status": "created_empty_2026-03-24",
            "wv_tagged": true,
            "description": "Economic indicators \u2014 Appalachian regional data"
        },
        "dimension": 384,
        "tenant": "default_tenant",
        "database": "default_database",
        "log_position": 0,
        "version": 0
    },
    {
        "id": "16c37f61-6bb5-4749-a007-25e8e937b13f",
        "name": "local_resources",
        "configuration_json": {
            "hnsw": {
                "space": "l2",
                "ef_construction": 100,
                "ef_search": 100,
                "max_neighbors": 16,
                "resize_factor": 1.2,
                "sync_threshold": 1000
            },
            "spann": null,
            "embedding_function": {
                "type": "known",
                "name": "default",
                "config": {}
            }
        },
        "schema": {
            "defaults": {
                "string": {
                    "fts_index": {
                        "enabled": false,
                        "config": {}
                    },
                    "string_inverted_index": {
                        "enabled": true,
                        "config": {}
                    }
                },
                "float_list": {
                    "vector_index": {
                        "enabled": false,
                        "config": {
                            "space": "l2",
                            "embedding_function": {
                                "type": "known",
                                "name": "default",
                                "config": {}
                            },
                            "hnsw": {
                                "ef_construction": 100,
                                "max_neighbors": 16,
                                "ef_search": 100,
                                "num_threads": 32,
                                "batch_size": 100,
                                "sync_threshold": 1000,
                                "resize_factor": 1.2
                            }
                        }
                    }
                },
                "sparse_vector": {
                    "sparse_vector_index": {
                        "enabled": false,
                        "config": {
                            "embedding_function": {
                                "type": "unknown"
                            },
                            "bm25": false
                        }
                    }
                },
                "int": {
                    "int_inverted_index": {
                        "enabled": true,
                        "config": {}
                    }
                },
                "float": {
                    "float_inverted_index": {
                        "enabled": true,
                        "config": {}
                    }
                },
                "bool": {
                    "bool_inverted_index": {
                        "enabled": true,
                        "config": {}
                    }
                }
            },
            "keys": {
                "name": {
                    "string": {
                        "fts_index": {
                            "enabled": false,
                            "config": {}
                        },
                        "string_inverted_index": {
                            "enabled": true,
                            "config": {}
                        }
                    }
                },
                "ingested_at": {
                    "string": {
                        "fts_index": {
                            "enabled": false,
                            "config": {}
                        },
                        "string_inverted_index": {
                            "enabled": true,
                            "config": {}
                        }
                    }
                },
                "phone": {
                    "string": {
                        "fts_index": {
                            "enabled": false,
                            "config": {}
                        },
                        "string_inverted_index": {
                            "enabled": true,
                            "config": {}
                        }
                    }
                },
                "source_file": {
                    "string": {
                        "fts_index": {
                            "enabled": false,
                            "config": {}
                        },
                        "string_inverted_index": {
                            "enabled": true,
                            "config": {}
                        }
                    }
                },
                "verification_status": {
                    "string": {
                        "fts_index": {
                            "enabled": false,
                            "config": {}
                        },
                        "string_inverted_index": {
                            "enabled": true,
                            "config": {}
                        }
                    }
                },
                "address": {
                    "string": {
                        "fts_index": {
                            "enabled": false,
                            "config": {}
                        },
                        "string_inverted_index": {
                            "enabled": true,
                            "config": {}
                        }
                    }
                },
                "status": {
                    "string": {
                        "fts_index": {
                            "enabled": false,
                            "config": {}
                        },
                        "string_inverted_index": {
                            "enabled": true,
                            "config": {}
                        }
                    }
                },
                "layer": {
                    "string": {
                        "fts_index": {
                            "enabled": false,
                            "config": {}
                        },
                        "string_inverted_index": {
                            "enabled": true,
                            "config": {}
                        }
                    }
                },
                "source": {
                    "string": {
                        "fts_index": {
                            "enabled": false,
                            "config": {}
                        },
                        "string_inverted_index": {
                            "enabled": true,
                            "config": {}
                        }
                    }
                },
                "lon": {
                    "float": {
                        "float_inverted_index": {
                            "enabled": true,
                            "config": {}
                        }
                    }
                },
                "text_length": {
                    "int": {
                        "int_inverted_index": {
                            "enabled": true,
                            "config": {}
                        }
                    }
                },
                "email": {
                    "string": {
                        "fts_index": {
                            "enabled": false,
                            "config": {}
                        },
                        "string_inverted_index": {
                            "enabled": true,
                            "config": {}
                        }
                    }
                },
                "county": {
                    "string": {
                        "fts_index": {
                            "enabled": false,
                            "config": {}
                        },
                        "string_inverted_index": {
                            "enabled": true,
                            "config": {}
                        }
                    }
                },
                "lat": {
                    "float": {
                        "float_inverted_index": {
                            "enabled": true,
                            "config": {}
                        }
                    }
                },
                "state": {
                    "string": {
                        "fts_index": {
                            "enabled": false,
                            "config": {}
                        },
                        "string_inverted_index": {
                            "enabled": true,
                            "config": {}
                        }
                    }
                },
                "resource_type": {
                    "string": {
                        "fts_index": {
                            "enabled": false,
                            "config": {}
                        },
                        "string_inverted_index": {
                            "enabled": true,
                            "config": {}
                        }
                    }
                },
                "url": {
                    "string": {
                        "fts_index": {
                            "enabled": false,
                            "config": {}
                        },
                        "string_inverted_index": {
                            "enabled": true,
                            "config": {}
                        }
                    }
                },
                "zip_codes": {
                    "string": {
                        "fts_index": {
                            "enabled": false,
                            "config": {}
                        },
                        "string_inverted_index": {
                            "enabled": true,
                            "config": {}
                        }
                    }
                },
                "doc_type": {
                    "string": {
                        "fts_index": {
                            "enabled": false,
                            "config": {}
                        },
                        "string_inverted_index": {
                            "enabled": true,
                            "config": {}
                        }
                    }
                },
                "#document": {
                    "string": {
                        "fts_index": {
                            "enabled": true,
                            "config": {}
                        },
                        "string_inverted_index": {
                            "enabled": false,
                            "config": {}
                        }
                    }
                },
                "#embedding": {
                    "float_list": {
                        "vector_index": {
                            "enabled": true,
                            "config": {
                                "space": "l2",
                                "embedding_function": {
                                    "type": "known",
                                    "name": "default",
                                    "config": {}
                                },
                                "source_key": "#document",
                                "hnsw": {
                                    "ef_construction": 100,
                                    "max_neighbors": 16,
                                    "ef_search": 100,
                                    "num_threads": 32,
                                    "batch_size": 100,
                                    "sync_threshold": 1000,
                                    "resize_factor": 1.2
                                }
                            }
                        }
                    }
                }
            }
        },
        "metadata": null,
        "dimension": 384,
        "tenant": "default_tenant",
        "database": "default_database",
        "log_position": 0,
        "version": 0
    },
    {
        "id": "1bf4e665-75d9-4d7e-8738-048800de6985",
        "name": "governance_rag",
        "configuration_json": {
            "hnsw": {
                "space": "l2",
                "ef_construction": 100,
                "ef_search": 100,
                "max_neighbors": 16,
                "resize_factor": 1.2,
                "sync_threshold": 1000
            },
            "spann": null,
            "embedding_function": {
                "type": "known",
                "name": "default",
                "config": {}
            }
        },
        "schema": {
            "defaults": {
                "string": {
                    "fts_index": {
                        "enabled": false,
                        "config": {}
                    },
                    "string_inverted_index": {
                        "enabled": true,
                        "config": {}
                    }
                },
                "float_list": {
                    "vector_index": {
                        "enabled": false,
                        "config": {
                            "space": "l2",
                            "embedding_function": {
                                "type": "known",
                                "name": "default",
                                "config": {}
                            },
                            "hnsw": {
                                "ef_construction": 100,
                                "max_neighbors": 16,
                                "ef_search": 100,
                                "num_threads": 32,
                                "batch_size": 100,
                                "sync_threshold": 1000,
                                "resize_factor": 1.2
                            }
                        }
                    }
                },
                "sparse_vector": {
                    "sparse_vector_index": {
                        "enabled": false,
                        "config": {
                            "embedding_function": {
                                "type": "unknown"
                            },
                            "bm25": false
                        }
                    }
                },
                "int": {
                    "int_inverted_index": {
                        "enabled": true,
                        "config": {}
                    }
                },
                "float": {
                    "float_inverted_index": {
                        "enabled": true,
                        "config": {}
                    }
                },
                "bool": {
                    "bool_inverted_index": {
                        "enabled": true,
                        "config": {}
                    }
                }
            },
            "keys": {
                "category": {
                    "string": {
                        "fts_index": {
                            "enabled": false,
                            "config": {}
                        },
                        "string_inverted_index": {
                            "enabled": true,
                            "config": {}
                        }
                    }
                },
                "#document": {
                    "string": {
                        "fts_index": {
                            "enabled": true,
                            "config": {}
                        },
                        "string_inverted_index": {
                            "enabled": false,
                            "config": {}
                        }
                    }
                },
                "#embedding": {
                    "float_list": {
                        "vector_index": {
                            "enabled": true,
                            "config": {
                                "space": "l2",
                                "embedding_function": {
                                    "type": "known",
                                    "name": "default",
                                    "config": {}
                                },
                                "source_key": "#document",
                                "hnsw": {
                                    "ef_construction": 100,
                                    "max_neighbors": 16,
                                    "ef_search": 100,
                                    "num_threads": 32,
                                    "batch_size": 100,
                                    "sync_threshold": 1000,
                                    "resize_factor": 1.2
                                }
                            }
                        }
                    }
                },
                "wv_tagged": {
                    "bool": {
                        "bool_inverted_index": {
                            "enabled": true,
                            "config": {}
                        }
                    }
                }
            }
        },
        "metadata": {
            "wv_tagged": true,
            "status": "created_empty_2026-03-24",
            "description": "Governance frameworks \u2014 community AI governance"
        },
        "dimension": 384,
        "tenant": "default_tenant",
        "database": "default_database",
        "log_position": 0,
        "version": 0
    },
    {
        "id": "21151130-0704-416b-9cd8-6c7403c1aeae",
        "name": "geospatialfeatures",
        "configuration_json": {
            "hnsw": {
                "space": "l2",
                "ef_construction": 100,
                "ef_search": 100,
                "max_neighbors": 16,
                "resize_factor": 1.2,
                "sync_threshold": 1000
            },
            "spann": null,
            "embedding_function": {
                "type": "known",
                "name": "default",
                "config": {}
            }
        },
        "schema": {
            "defaults": {
                "string": {
                    "fts_index": {
                        "enabled": false,
                        "config": {}
                    },
                    "string_inverted_index": {
                        "enabled": true,
                        "config": {}
                    }
                },
                "float_list": {
                    "vector_index": {
                        "enabled": false,
                        "config": {
                            "space": "l2",
                            "embedding_function": {
                                "type": "known",
                                "name": "default",
                                "config": {}
                            },
                            "hnsw": {
                                "ef_construction": 100,
                                "max_neighbors": 16,
                                "ef_search": 100,
                                "num_threads": 32,
                                "batch_size": 100,
                                "sync_threshold": 1000,
                                "resize_factor": 1.2
                            }
                        }
                    }
                },
                "sparse_vector": {
                    "sparse_vector_index": {
                        "enabled": false,
                        "config": {
                            "embedding_function": {
                                "type": "unknown"
                            },
                            "bm25": false
                        }
                    }
                },
                "int": {
                    "int_inverted_index": {
                        "enabled": true,
                        "config": {}
                    }
                },
                "float": {
                    "float_inverted_index": {
                        "enabled": true,
                        "config": {}
                    }
                },
                "bool": {
                    "bool_inverted_index": {
                        "enabled": true,
                        "config": {}
                    }
                }
            },
            "keys": {
                "#embedding": {
                    "float_list": {
                        "vector_index": {
                            "enabled": true,
                            "config": {
                                "space": "l2",
                                "embedding_function": {
                                    "type": "known",
                                    "name": "default",
                                    "config": {}
                                },
                                "source_key": "#document",
                                "hnsw": {
                                    "ef_construction": 100,
                                    "max_neighbors": 16,
                                    "ef_search": 100,
                                    "num_threads": 32,
                                    "batch_size": 100,
                                    "sync_threshold": 1000,
                                    "resize_factor": 1.2
                                }
                            }
                        }
                    }
                },
                "lat": {
                    "float": {
                        "float_inverted_index": {
                            "enabled": true,
                            "config": {}
                        }
                    }
                },
                "label": {
                    "string": {
                        "fts_index": {
                            "enabled": false,
                            "config": {}
                        },
                        "string_inverted_index": {
                            "enabled": true,
                            "config": {}
                        }
                    }
                },
                "state": {
                    "string": {
                        "fts_index": {
                            "enabled": false,
                            "config": {}
                        },
                        "string_inverted_index": {
                            "enabled": true,
                            "config": {}
                        }
                    }
                },
                "#document": {
                    "string": {
                        "fts_index": {
                            "enabled": true,
                            "config": {}
                        },
                        "string_inverted_index": {
                            "enabled": false,
                            "config": {}
                        }
                    }
                },
                "layer": {
                    "string": {
                        "fts_index": {
                            "enabled": false,
                            "config": {}
                        },
                        "string_inverted_index": {
                            "enabled": true,
                            "config": {}
                        }
                    }
                },
                "lon": {
                    "float": {
                        "float_inverted_index": {
                            "enabled": true,
                            "config": {}
                        }
                    }
                }
            }
        },
        "metadata": {
            "description": "WV GIS spatial features \u2014 132 datasets, 384-dim embeddings"
        },
        "dimension": 384,
        "tenant": "default_tenant",
        "database": "default_database",
        "log_position": 0,
        "version": 0
    },
    {
        "id": "27f9d49b-c2a0-4c5e-91f5-8441105fedc9",
        "name": "conversation_gbim_private",
        "configuration_json": {
            "hnsw": {
                "space": "l2",
                "ef_construction": 100,
                "ef_search": 100,
                "max_neighbors": 16,
                "resize_factor": 1.2,
                "sync_threshold": 1000
            },
            "spann": null,
            "embedding_function": {
                "type": "known",
                "name": "default",
                "config": {}
            }
        },
        "schema": {
            "defaults": {
                "string": {
                    "fts_index": {
                        "enabled": false,
                        "config": {}
                    },
                    "string_inverted_index": {
                        "enabled": true,
                        "config": {}
                    }
                },
                "float_list": {
                    "vector_index": {
                        "enabled": false,
                        "config": {
                            "space": "l2",
                            "embedding_function": {
                                "type": "known",
                                "name": "default",
                                "config": {}
                            },
                            "hnsw": {
                                "ef_construction": 100,
                                "max_neighbors": 16,
                                "ef_search": 100,
                                "num_threads": 32,
                                "batch_size": 100,
                                "sync_threshold": 1000,
                                "resize_factor": 1.2
                            }
                        }
                    }
                },
                "sparse_vector": {
                    "sparse_vector_index": {
                        "enabled": false,
                        "config": {
                            "embedding_function": {
                                "type": "unknown"
                            },
                            "bm25": false
                        }
                    }
                },
                "int": {
                    "int_inverted_index": {
                        "enabled": true,
                        "config": {}
                    }
                },
                "float": {
                    "float_inverted_index": {
                        "enabled": true,
                        "config": {}
                    }
                },
                "bool": {
                    "bool_inverted_index": {
                        "enabled": true,
                        "config": {}
                    }
                }
            },
            "keys": {
                "turn_number": {
                    "int": {
                        "int_inverted_index": {
                            "enabled": true,
                            "config": {}
                        }
                    }
                },
                "session_id": {
                    "string": {
                        "fts_index": {
                            "enabled": false,
                            "config": {}
                        },
                        "string_inverted_index": {
                            "enabled": true,
                            "config": {}
                        }
                    }
                },
                "belief_id": {
                    "string": {
                        "fts_index": {
                            "enabled": false,
                            "config": {}
                        },
                        "string_inverted_index": {
                            "enabled": true,
                            "config": {}
                        }
                    }
                },
                "#embedding": {
                    "float_list": {
                        "vector_index": {
                            "enabled": true,
                            "config": {
                                "space": "l2",
                                "embedding_function": {
                                    "type": "known",
                                    "name": "default",
                                    "config": {}
                                },
                                "source_key": "#document",
                                "hnsw": {
                                    "ef_construction": 100,
                                    "max_neighbors": 16,
                                    "ef_search": 100,
                                    "num_threads": 32,
                                    "batch_size": 100,
                                    "sync_threshold": 1000,
                                    "resize_factor": 1.2
                                }
                            }
                        }
                    }
                },
                "created_at": {
                    "string": {
                        "fts_index": {
                            "enabled": false,
                            "config": {}
                        },
                        "string_inverted_index": {
                            "enabled": true,
                            "config": {}
                        }
                    }
                },
                "privacy_tier": {
                    "string": {
                        "fts_index": {
                            "enabled": false,
                            "config": {}
                        },
                        "string_inverted_index": {
                            "enabled": true,
                            "config": {}
                        }
                    }
                },
                "place": {
                    "string": {
                        "fts_index": {
                            "enabled": false,
                            "config": {}
                        },
                        "string_inverted_index": {
                            "enabled": true,
                            "config": {}
                        }
                    }
                },
                "intent": {
                    "string": {
                        "fts_index": {
                            "enabled": false,
                            "config": {}
                        },
                        "string_inverted_index": {
                            "enabled": true,
                            "config": {}
                        }
                    }
                },
                "county": {
                    "string": {
                        "fts_index": {
                            "enabled": false,
                            "config": {}
                        },
                        "string_inverted_index": {
                            "enabled": true,
                            "config": {}
                        }
                    }
                },
                "immutability_hash": {
                    "string": {
                        "fts_index": {
                            "enabled": false,
                            "config": {}
                        },
                        "string_inverted_index": {
                            "enabled": true,
                            "config": {}
                        }
                    }
                },
                "user_id": {
                    "string": {
                        "fts_index": {
                            "enabled": false,
                            "config": {}
                        },
                        "string_inverted_index": {
                            "enabled": true,
                            "config": {}
                        }
                    }
                },
                "#document": {
                    "string": {
                        "fts_index": {
                            "enabled": true,
                            "config": {}
                        },
                        "string_inverted_index": {
                            "enabled": false,
                            "config": {}
                        }
                    }
                },
                "state": {
                    "string": {
                        "fts_index": {
                            "enabled": false,
                            "config": {}
                        },
                        "string_inverted_index": {
                            "enabled": true,
                            "config": {}
                        }
                    }
                }
            }
        },
        "metadata": {
            "description": "Private conversation GBIM \u2014 per-user, session-anchored",
            "privacy_tier": "private",
            "gbim_axes": "who,what,where,when,how,why,for_whom,authority,evidence",
            "access": "ms_jarvis_only"
        },
        "dimension": 384,
        "tenant": "default_tenant",
        "database": "default_database",
        "log_position": 0,
        "version": 0
    },
    {
        "id": "28014347-d398-4f92-b0ca-81a1de7fc4eb",
        "name": "policy_rag",
        "configuration_json": {
            "hnsw": {
                "space": "l2",
                "ef_construction": 100,
                "ef_search": 100,
                "max_neighbors": 16,
                "resize_factor": 1.2,
                "sync_threshold": 1000
            },
            "spann": null,
            "embedding_function": {
                "type": "known",
                "name": "default",
                "config": {}
            }
        },
        "schema": {
            "defaults": {
                "string": {
                    "fts_index": {
                        "enabled": false,
                        "config": {}
                    },
                    "string_inverted_index": {
                        "enabled": true,
                        "config": {}
                    }
                },
                "float_list": {
                    "vector_index": {
                        "enabled": false,
                        "config": {
                            "space": "l2",
                            "embedding_function": {
                                "type": "known",
                                "name": "default",
                                "config": {}
                            },
                            "hnsw": {
                                "ef_construction": 100,
                                "max_neighbors": 16,
                                "ef_search": 100,
                                "num_threads": 32,
                                "batch_size": 100,
                                "sync_threshold": 1000,
                                "resize_factor": 1.2
                            }
                        }
                    }
                },
                "sparse_vector": {
                    "sparse_vector_index": {
                        "enabled": false,
                        "config": {
                            "embedding_function": {
                                "type": "unknown"
                            },
                            "bm25": false
                        }
                    }
                },
                "int": {
                    "int_inverted_index": {
                        "enabled": true,
                        "config": {}
                    }
                },
                "float": {
                    "float_inverted_index": {
                        "enabled": true,
                        "config": {}
                    }
                },
                "bool": {
                    "bool_inverted_index": {
                        "enabled": true,
                        "config": {}
                    }
                }
            },
            "keys": {
                "#document": {
                    "string": {
                        "fts_index": {
                            "enabled": true,
                            "config": {}
                        },
                        "string_inverted_index": {
                            "enabled": false,
                            "config": {}
                        }
                    }
                },
                "#embedding": {
                    "float_list": {
                        "vector_index": {
                            "enabled": true,
                            "config": {
                                "space": "l2",
                                "embedding_function": {
                                    "type": "known",
                                    "name": "default",
                                    "config": {}
                                },
                                "source_key": "#document",
                                "hnsw": {
                                    "ef_construction": 100,
                                    "max_neighbors": 16,
                                    "ef_search": 100,
                                    "num_threads": 32,
                                    "batch_size": 100,
                                    "sync_threshold": 1000,
                                    "resize_factor": 1.2
                                }
                            }
                        }
                    }
                },
                "wv_tagged": {
                    "bool": {
                        "bool_inverted_index": {
                            "enabled": true,
                            "config": {}
                        }
                    }
                },
                "category": {
                    "string": {
                        "fts_index": {
                            "enabled": false,
                            "config": {}
                        },
                        "string_inverted_index": {
                            "enabled": true,
                            "config": {}
                        }
                    }
                }
            }
        },
        "metadata": {
            "description": "WV policy documents \u2014 state and regional legislation",
            "wv_tagged": true,
            "status": "created_empty_2026-03-24"
        },
        "dimension": 384,
        "tenant": "default_tenant",
        "database": "default_database",
        "log_position": 0,
        "version": 0
    },
    {
        "id": "2bc09932-0ec4-4883-9abd-bf18f3769eaa",
        "name": "grants_rag",
        "configuration_json": {
            "hnsw": {
                "space": "l2",
                "ef_construction": 100,
                "ef_search": 100,
                "max_neighbors": 16,
                "resize_factor": 1.2,
                "sync_threshold": 1000
            },
            "spann": null,
            "embedding_function": {
                "type": "known",
                "name": "default",
                "config": {}
            }
        },
        "schema": {
            "defaults": {
                "string": {
                    "fts_index": {
                        "enabled": false,
                        "config": {}
                    },
                    "string_inverted_index": {
                        "enabled": true,
                        "config": {}
                    }
                },
                "float_list": {
                    "vector_index": {
                        "enabled": false,
                        "config": {
                            "space": "l2",
                            "embedding_function": {
                                "type": "known",
                                "name": "default",
                                "config": {}
                            },
                            "hnsw": {
                                "ef_construction": 100,
                                "max_neighbors": 16,
                                "ef_search": 100,
                                "num_threads": 32,
                                "batch_size": 100,
                                "sync_threshold": 1000,
                                "resize_factor": 1.2
                            }
                        }
                    }
                },
                "sparse_vector": {
                    "sparse_vector_index": {
                        "enabled": false,
                        "config": {
                            "embedding_function": {
                                "type": "unknown"
                            },
                            "bm25": false
                        }
                    }
                },
                "int": {
                    "int_inverted_index": {
                        "enabled": true,
                        "config": {}
                    }
                },
                "float": {
                    "float_inverted_index": {
                        "enabled": true,
                        "config": {}
                    }
                },
                "bool": {
                    "bool_inverted_index": {
                        "enabled": true,
                        "config": {}
                    }
                }
            },
            "keys": {
                "wv_tagged": {
                    "bool": {
                        "bool_inverted_index": {
                            "enabled": true,
                            "config": {}
                        }
                    }
                },
                "#embedding": {
                    "float_list": {
                        "vector_index": {
                            "enabled": true,
                            "config": {
                                "space": "l2",
                                "embedding_function": {
                                    "type": "known",
                                    "name": "default",
                                    "config": {}
                                },
                                "source_key": "#document",
                                "hnsw": {
                                    "ef_construction": 100,
                                    "max_neighbors": 16,
                                    "ef_search": 100,
                                    "num_threads": 32,
                                    "batch_size": 100,
                                    "sync_threshold": 1000,
                                    "resize_factor": 1.2
                                }
                            }
                        }
                    }
                },
                "category": {
                    "string": {
                        "fts_index": {
                            "enabled": false,
                            "config": {}
                        },
                        "string_inverted_index": {
                            "enabled": true,
                            "config": {}
                        }
                    }
                },
                "#document": {
                    "string": {
                        "fts_index": {
                            "enabled": true,
                            "config": {}
                        },
                        "string_inverted_index": {
                            "enabled": false,
                            "config": {}
                        }
                    }
                }
            }
        },
        "metadata": {
            "status": "created_empty_2026-03-24",
            "wv_tagged": true,
            "description": "Grant opportunities \u2014 federal, state, and foundation funding"
        },
        "dimension": 384,
        "tenant": "default_tenant",
        "database": "default_database",
        "log_position": 0,
        "version": 0
    },
    {
        "id": "3a193c3b-4743-4267-878d-cacb6c0c3ba2",
        "name": "appalachian_cultural_intelligence",
        "configuration_json": {
            "hnsw": {
                "space": "l2",
                "ef_construction": 100,
                "ef_search": 100,
                "max_neighbors": 16,
                "resize_factor": 1.2,
                "sync_threshold": 1000
            },
            "spann": null,
            "embedding_function": {
                "type": "known",
                "name": "default",
                "config": {}
            }
        },
        "schema": {
            "defaults": {
                "string": {
                    "fts_index": {
                        "enabled": false,
                        "config": {}
                    },
                    "string_inverted_index": {
                        "enabled": true,
                        "config": {}
                    }
                },
                "float_list": {
                    "vector_index": {
                        "enabled": false,
                        "config": {
                            "space": "l2",
                            "embedding_function": {
                                "type": "known",
                                "name": "default",
                                "config": {}
                            },
                            "hnsw": {
                                "ef_construction": 100,
                                "max_neighbors": 16,
                                "ef_search": 100,
                                "num_threads": 32,
                                "batch_size": 100,
                                "sync_threshold": 1000,
                                "resize_factor": 1.2
                            }
                        }
                    }
                },
                "sparse_vector": {
                    "sparse_vector_index": {
                        "enabled": false,
                        "config": {
                            "embedding_function": {
                                "type": "unknown"
                            },
                            "bm25": false
                        }
                    }
                },
                "int": {
                    "int_inverted_index": {
                        "enabled": true,
                        "config": {}
                    }
                },
                "float": {
                    "float_inverted_index": {
                        "enabled": true,
                        "config": {}
                    }
                },
                "bool": {
                    "bool_inverted_index": {
                        "enabled": true,
                        "config": {}
                    }
                }
            },
            "keys": {
                "#embedding": {
                    "float_list": {
                        "vector_index": {
                            "enabled": true,
                            "config": {
                                "space": "l2",
                                "embedding_function": {
                                    "type": "known",
                                    "name": "default",
                                    "config": {}
                                },
                                "source_key": "#document",
                                "hnsw": {
                                    "ef_construction": 100,
                                    "max_neighbors": 16,
                                    "ef_search": 100,
                                    "num_threads": 32,
                                    "batch_size": 100,
                                    "sync_threshold": 1000,
                                    "resize_factor": 1.2
                                }
                            }
                        }
                    }
                },
                "tradition": {
                    "string": {
                        "fts_index": {
                            "enabled": false,
                            "config": {}
                        },
                        "string_inverted_index": {
                            "enabled": true,
                            "config": {}
                        }
                    }
                },
                "location": {
                    "string": {
                        "fts_index": {
                            "enabled": false,
                            "config": {}
                        },
                        "string_inverted_index": {
                            "enabled": true,
                            "config": {}
                        }
                    }
                },
                "cultural_family": {
                    "string": {
                        "fts_index": {
                            "enabled": false,
                            "config": {}
                        },
                        "string_inverted_index": {
                            "enabled": true,
                            "config": {}
                        }
                    }
                },
                "#document": {
                    "string": {
                        "fts_index": {
                            "enabled": true,
                            "config": {}
                        },
                        "string_inverted_index": {
                            "enabled": false,
                            "config": {}
                        }
                    }
                },
                "category": {
                    "string": {
                        "fts_index": {
                            "enabled": false,
                            "config": {}
                        },
                        "string_inverted_index": {
                            "enabled": true,
                            "config": {}
                        }
                    }
                },
                "source": {
                    "string": {
                        "fts_index": {
                            "enabled": false,
                            "config": {}
                        },
                        "string_inverted_index": {
                            "enabled": true,
                            "config": {}
                        }
                    }
                }
            }
        },
        "metadata": null,
        "dimension": 384,
        "tenant": "default_tenant",
        "database": "default_database",
        "log_position": 0,
        "version": 0
    },
    {
        "id": "3b4317d9-19e4-495c-b91e-6e02686d67f0",
        "name": "GBIM_sample_rows",
        "configuration_json": {
            "hnsw": {
                "space": "l2",
                "ef_construction": 100,
                "ef_search": 100,
                "max_neighbors": 16,
                "resize_factor": 1.2,
                "sync_threshold": 1000
            },
            "spann": null,
            "embedding_function": {
                "type": "known",
                "name": "default",
                "config": {}
            }
        },
        "schema": {
            "defaults": {
                "string": {
                    "fts_index": {
                        "enabled": false,
                        "config": {}
                    },
                    "string_inverted_index": {
                        "enabled": true,
                        "config": {}
                    }
                },
                "float_list": {
                    "vector_index": {
                        "enabled": false,
                        "config": {
                            "space": "l2",
                            "embedding_function": {
                                "type": "known",
                                "name": "default",
                                "config": {}
                            },
                            "hnsw": {
                                "ef_construction": 100,
                                "max_neighbors": 16,
                                "ef_search": 100,
                                "num_threads": 32,
                                "batch_size": 100,
                                "sync_threshold": 1000,
                                "resize_factor": 1.2
                            }
                        }
                    }
                },
                "sparse_vector": {
                    "sparse_vector_index": {
                        "enabled": false,
                        "config": {
                            "embedding_function": {
                                "type": "unknown"
                            },
                            "bm25": false
                        }
                    }
                },
                "int": {
                    "int_inverted_index": {
                        "enabled": true,
                        "config": {}
                    }
                },
                "float": {
                    "float_inverted_index": {
                        "enabled": true,
                        "config": {}
                    }
                },
                "bool": {
                    "bool_inverted_index": {
                        "enabled": true,
                        "config": {}
                    }
                }
            },
            "keys": {
                "worldview_id": {
                    "string": {
                        "fts_index": {
                            "enabled": false,
                            "config": {}
                        },
                        "string_inverted_index": {
                            "enabled": true,
                            "config": {}
                        }
                    }
                },
                "#embedding": {
                    "float_list": {
                        "vector_index": {
                            "enabled": true,
                            "config": {
                                "space": "l2",
                                "embedding_function": {
                                    "type": "known",
                                    "name": "default",
                                    "config": {}
                                },
                                "source_key": "#document",
                                "hnsw": {
                                    "ef_construction": 100,
                                    "max_neighbors": 16,
                                    "ef_search": 100,
                                    "num_threads": 32,
                                    "batch_size": 100,
                                    "sync_threshold": 1000,
                                    "resize_factor": 1.2
                                }
                            }
                        }
                    }
                },
                "#document": {
                    "string": {
                        "fts_index": {
                            "enabled": true,
                            "config": {}
                        },
                        "string_inverted_index": {
                            "enabled": false,
                            "config": {}
                        }
                    }
                },
                "id": {
                    "string": {
                        "fts_index": {
                            "enabled": false,
                            "config": {}
                        },
                        "string_inverted_index": {
                            "enabled": true,
                            "config": {}
                        }
                    }
                },
                "entity_type": {
                    "string": {
                        "fts_index": {
                            "enabled": false,
                            "config": {}
                        },
                        "string_inverted_index": {
                            "enabled": true,
                            "config": {}
                        }
                    }
                },
                "belief_state": {
                    "string": {
                        "fts_index": {
                            "enabled": false,
                            "config": {}
                        },
                        "string_inverted_index": {
                            "enabled": true,
                            "config": {}
                        }
                    }
                },
                "created_at": {
                    "string": {
                        "fts_index": {
                            "enabled": false,
                            "config": {}
                        },
                        "string_inverted_index": {
                            "enabled": true,
                            "config": {}
                        }
                    }
                },
                "source_pk": {
                    "string": {
                        "fts_index": {
                            "enabled": false,
                            "config": {}
                        },
                        "string_inverted_index": {
                            "enabled": true,
                            "config": {}
                        }
                    }
                },
                "source_table": {
                    "string": {
                        "fts_index": {
                            "enabled": false,
                            "config": {}
                        },
                        "string_inverted_index": {
                            "enabled": true,
                            "config": {}
                        }
                    }
                },
                "label": {
                    "string": {
                        "fts_index": {
                            "enabled": false,
                            "config": {}
                        },
                        "string_inverted_index": {
                            "enabled": true,
                            "config": {}
                        }
                    }
                }
            }
        },
        "metadata": null,
        "dimension": 384,
        "tenant": "default_tenant",
        "database": "default_database",
        "log_position": 0,
        "version": 0
    },
    {
        "id": "524507db-559b-44e5-80a1-b25896a3c229",
        "name": "gis_wv_benefits",
        "configuration_json": {
            "hnsw": {
                "space": "l2",
                "ef_construction": 100,
                "ef_search": 100,
                "max_neighbors": 16,
                "resize_factor": 1.2,
                "sync_threshold": 1000
            },
            "spann": null,
            "embedding_function": {
                "type": "known",
                "name": "default",
                "config": {}
            }
        },
        "schema": {
            "defaults": {
                "string": {
                    "fts_index": {
                        "enabled": false,
                        "config": {}
                    },
                    "string_inverted_index": {
                        "enabled": true,
                        "config": {}
                    }
                },
                "float_list": {
                    "vector_index": {
                        "enabled": false,
                        "config": {
                            "space": "l2",
                            "embedding_function": {
                                "type": "known",
                                "name": "default",
                                "config": {}
                            },
                            "hnsw": {
                                "ef_construction": 100,
                                "max_neighbors": 16,
                                "ef_search": 100,
                                "num_threads": 32,
                                "batch_size": 100,
                                "sync_threshold": 1000,
                                "resize_factor": 1.2
                            }
                        }
                    }
                },
                "sparse_vector": {
                    "sparse_vector_index": {
                        "enabled": false,
                        "config": {
                            "embedding_function": {
                                "type": "unknown"
                            },
                            "bm25": false
                        }
                    }
                },
                "int": {
                    "int_inverted_index": {
                        "enabled": true,
                        "config": {}
                    }
                },
                "float": {
                    "float_inverted_index": {
                        "enabled": true,
                        "config": {}
                    }
                },
                "bool": {
                    "bool_inverted_index": {
                        "enabled": true,
                        "config": {}
                    }
                }
            },
            "keys": {
                "#embedding": {
                    "float_list": {
                        "vector_index": {
                            "enabled": true,
                            "config": {
                                "space": "l2",
                                "embedding_function": {
                                    "type": "known",
                                    "name": "default",
                                    "config": {}
                                },
                                "source_key": "#document",
                                "hnsw": {
                                    "ef_construction": 100,
                                    "max_neighbors": 16,
                                    "ef_search": 100,
                                    "num_threads": 32,
                                    "batch_size": 100,
                                    "sync_threshold": 1000,
                                    "resize_factor": 1.2
                                }
                            }
                        }
                    }
                },
                "state": {
                    "string": {
                        "fts_index": {
                            "enabled": false,
                            "config": {}
                        },
                        "string_inverted_index": {
                            "enabled": true,
                            "config": {}
                        }
                    }
                },
                "city": {
                    "string": {
                        "fts_index": {
                            "enabled": false,
                            "config": {}
                        },
                        "string_inverted_index": {
                            "enabled": true,
                            "config": {}
                        }
                    }
                },
                "source": {
                    "string": {
                        "fts_index": {
                            "enabled": false,
                            "config": {}
                        },
                        "string_inverted_index": {
                            "enabled": true,
                            "config": {}
                        }
                    }
                },
                "phone": {
                    "string": {
                        "fts_index": {
                            "enabled": false,
                            "config": {}
                        },
                        "string_inverted_index": {
                            "enabled": true,
                            "config": {}
                        }
                    }
                },
                "geo_method": {
                    "string": {
                        "fts_index": {
                            "enabled": false,
                            "config": {}
                        },
                        "string_inverted_index": {
                            "enabled": true,
                            "config": {}
                        }
                    }
                },
                "fips_county": {
                    "string": {
                        "fts_index": {
                            "enabled": false,
                            "config": {}
                        },
                        "string_inverted_index": {
                            "enabled": true,
                            "config": {}
                        }
                    }
                },
                "zip_code": {
                    "string": {
                        "fts_index": {
                            "enabled": false,
                            "config": {}
                        },
                        "string_inverted_index": {
                            "enabled": true,
                            "config": {}
                        }
                    }
                },
                "source_file": {
                    "string": {
                        "fts_index": {
                            "enabled": false,
                            "config": {}
                        },
                        "string_inverted_index": {
                            "enabled": true,
                            "config": {}
                        }
                    }
                },
                "#document": {
                    "string": {
                        "fts_index": {
                            "enabled": true,
                            "config": {}
                        },
                        "string_inverted_index": {
                            "enabled": false,
                            "config": {}
                        }
                    }
                },
                "service_type": {
                    "string": {
                        "fts_index": {
                            "enabled": false,
                            "config": {}
                        },
                        "string_inverted_index": {
                            "enabled": true,
                            "config": {}
                        }
                    }
                },
                "program_name": {
                    "string": {
                        "fts_index": {
                            "enabled": false,
                            "config": {}
                        },
                        "string_inverted_index": {
                            "enabled": true,
                            "config": {}
                        }
                    }
                },
                "url": {
                    "string": {
                        "fts_index": {
                            "enabled": false,
                            "config": {}
                        },
                        "string_inverted_index": {
                            "enabled": true,
                            "config": {}
                        }
                    }
                }
            }
        },
        "metadata": {
            "description": "WV state benefits and social services programs"
        },
        "dimension": 384,
        "tenant": "default_tenant",
        "database": "default_database",
        "log_position": 0,
        "version": 0
    },
    {
        "id": "5627f6ba-115d-4d7b-898d-a2436e6513ac",
        "name": "news_rag",
        "configuration_json": {
            "hnsw": {
                "space": "l2",
                "ef_construction": 100,
                "ef_search": 100,
                "max_neighbors": 16,
                "resize_factor": 1.2,
                "sync_threshold": 1000
            },
            "spann": null,
            "embedding_function": {
                "type": "known",
                "name": "default",
                "config": {}
            }
        },
        "schema": {
            "defaults": {
                "string": {
                    "fts_index": {
                        "enabled": false,
                        "config": {}
                    },
                    "string_inverted_index": {
                        "enabled": true,
                        "config": {}
                    }
                },
                "float_list": {
                    "vector_index": {
                        "enabled": false,
                        "config": {
                            "space": "l2",
                            "embedding_function": {
                                "type": "known",
                                "name": "default",
                                "config": {}
                            },
                            "hnsw": {
                                "ef_construction": 100,
                                "max_neighbors": 16,
                                "ef_search": 100,
                                "num_threads": 32,
                                "batch_size": 100,
                                "sync_threshold": 1000,
                                "resize_factor": 1.2
                            }
                        }
                    }
                },
                "sparse_vector": {
                    "sparse_vector_index": {
                        "enabled": false,
                        "config": {
                            "embedding_function": {
                                "type": "unknown"
                            },
                            "bm25": false
                        }
                    }
                },
                "int": {
                    "int_inverted_index": {
                        "enabled": true,
                        "config": {}
                    }
                },
                "float": {
                    "float_inverted_index": {
                        "enabled": true,
                        "config": {}
                    }
                },
                "bool": {
                    "bool_inverted_index": {
                        "enabled": true,
                        "config": {}
                    }
                }
            },
            "keys": {
                "source": {
                    "string": {
                        "fts_index": {
                            "enabled": false,
                            "config": {}
                        },
                        "string_inverted_index": {
                            "enabled": true,
                            "config": {}
                        }
                    }
                },
                "#embedding": {
                    "float_list": {
                        "vector_index": {
                            "enabled": true,
                            "config": {
                                "space": "l2",
                                "embedding_function": {
                                    "type": "known",
                                    "name": "default",
                                    "config": {}
                                },
                                "source_key": "#document",
                                "hnsw": {
                                    "ef_construction": 100,
                                    "max_neighbors": 16,
                                    "ef_search": 100,
                                    "num_threads": 32,
                                    "batch_size": 100,
                                    "sync_threshold": 1000,
                                    "resize_factor": 1.2
                                }
                            }
                        }
                    }
                },
                "url": {
                    "string": {
                        "fts_index": {
                            "enabled": false,
                            "config": {}
                        },
                        "string_inverted_index": {
                            "enabled": true,
                            "config": {}
                        }
                    }
                },
                "pubdate": {
                    "string": {
                        "fts_index": {
                            "enabled": false,
                            "config": {}
                        },
                        "string_inverted_index": {
                            "enabled": true,
                            "config": {}
                        }
                    }
                },
                "#document": {
                    "string": {
                        "fts_index": {
                            "enabled": true,
                            "config": {}
                        },
                        "string_inverted_index": {
                            "enabled": false,
                            "config": {}
                        }
                    }
                },
                "wv_tagged": {
                    "bool": {
                        "bool_inverted_index": {
                            "enabled": true,
                            "config": {}
                        }
                    }
                },
                "category": {
                    "string": {
                        "fts_index": {
                            "enabled": false,
                            "config": {}
                        },
                        "string_inverted_index": {
                            "enabled": true,
                            "config": {}
                        }
                    }
                }
            }
        },
        "metadata": {
            "description": "Regional news \u2014 WV and Appalachian media",
            "status": "created_empty_2026-03-24",
            "wv_tagged": true
        },
        "dimension": 384,
        "tenant": "default_tenant",
        "database": "default_database",
        "log_position": 0,
        "version": 0
    },
    {
        "id": "571eebfa-b122-4e91-af3a-a7aa9a188ba1",
        "name": "gbim_beliefs_v2",
        "configuration_json": {
            "hnsw": {
                "space": "cosine",
                "ef_construction": 100,
                "ef_search": 100,
                "max_neighbors": 16,
                "resize_factor": 1.2,
                "sync_threshold": 1000
            },
            "spann": null,
            "embedding_function": null
        },
        "schema": {
            "defaults": {
                "string": {
                    "fts_index": {
                        "enabled": false,
                        "config": {}
                    },
                    "string_inverted_index": {
                        "enabled": true,
                        "config": {}
                    }
                },
                "float_list": {
                    "vector_index": {
                        "enabled": false,
                        "config": {
                            "space": "cosine",
                            "hnsw": {
                                "ef_construction": 100,
                                "max_neighbors": 16,
                                "ef_search": 100,
                                "num_threads": 32,
                                "batch_size": 100,
                                "sync_threshold": 1000,
                                "resize_factor": 1.2
                            }
                        }
                    }
                },
                "sparse_vector": {
                    "sparse_vector_index": {
                        "enabled": false,
                        "config": {
                            "embedding_function": {
                                "type": "unknown"
                            },
                            "bm25": false
                        }
                    }
                },
                "int": {
                    "int_inverted_index": {
                        "enabled": true,
                        "config": {}
                    }
                },
                "float": {
                    "float_inverted_index": {
                        "enabled": true,
                        "config": {}
                    }
                },
                "bool": {
                    "bool_inverted_index": {
                        "enabled": true,
                        "config": {}
                    }
                }
            },
            "keys": {
                "#embedding": {
                    "float_list": {
                        "vector_index": {
                            "enabled": true,
                            "config": {
                                "space": "cosine",
                                "source_key": "#document",
                                "hnsw": {
                                    "ef_construction": 100,
                                    "max_neighbors": 16,
                                    "ef_search": 100,
                                    "num_threads": 32,
                                    "batch_size": 100,
                                    "sync_threshold": 1000,
                                    "resize_factor": 1.2
                                }
                            }
                        }
                    }
                },
                "#document": {
                    "string": {
                        "fts_index": {
                            "enabled": true,
                            "config": {}
                        },
                        "string_inverted_index": {
                            "enabled": false,
                            "config": {}
                        }
                    }
                }
            }
        },
        "metadata": {
            "wv_tagged": true,
            "description": "GBIM belief propositions v2 \u2014 WV landowner and community beliefs",
            "hnsw:space": "cosine"
        },
        "dimension": null,
        "tenant": "default_tenant",
        "database": "default_database",
        "log_position": 0,
        "version": 0
    },
    {
        "id": "73793b76-c4b9-46a0-b2e7-353d0bad6eb4",
        "name": "commons_rag",
        "configuration_json": {
            "hnsw": {
                "space": "l2",
                "ef_construction": 100,
                "ef_search": 100,
                "max_neighbors": 16,
                "resize_factor": 1.2,
                "sync_threshold": 1000
            },
            "spann": null,
            "embedding_function": {
                "type": "known",
                "name": "default",
                "config": {}
            }
        },
        "schema": {
            "defaults": {
                "string": {
                    "fts_index": {
                        "enabled": false,
                        "config": {}
                    },
                    "string_inverted_index": {
                        "enabled": true,
                        "config": {}
                    }
                },
                "float_list": {
                    "vector_index": {
                        "enabled": false,
                        "config": {
                            "space": "l2",
                            "embedding_function": {
                                "type": "known",
                                "name": "default",
                                "config": {}
                            },
                            "hnsw": {
                                "ef_construction": 100,
                                "max_neighbors": 16,
                                "ef_search": 100,
                                "num_threads": 32,
                                "batch_size": 100,
                                "sync_threshold": 1000,
                                "resize_factor": 1.2
                            }
                        }
                    }
                },
                "sparse_vector": {
                    "sparse_vector_index": {
                        "enabled": false,
                        "config": {
                            "embedding_function": {
                                "type": "unknown"
                            },
                            "bm25": false
                        }
                    }
                },
                "int": {
                    "int_inverted_index": {
                        "enabled": true,
                        "config": {}
                    }
                },
                "float": {
                    "float_inverted_index": {
                        "enabled": true,
                        "config": {}
                    }
                },
                "bool": {
                    "bool_inverted_index": {
                        "enabled": true,
                        "config": {}
                    }
                }
            },
            "keys": {
                "#embedding": {
                    "float_list": {
                        "vector_index": {
                            "enabled": true,
                            "config": {
                                "space": "l2",
                                "embedding_function": {
                                    "type": "known",
                                    "name": "default",
                                    "config": {}
                                },
                                "source_key": "#document",
                                "hnsw": {
                                    "ef_construction": 100,
                                    "max_neighbors": 16,
                                    "ef_search": 100,
                                    "num_threads": 32,
                                    "batch_size": 100,
                                    "sync_threshold": 1000,
                                    "resize_factor": 1.2
                                }
                            }
                        }
                    }
                },
                "wv_tagged": {
                    "bool": {
                        "bool_inverted_index": {
                            "enabled": true,
                            "config": {}
                        }
                    }
                },
                "#document": {
                    "string": {
                        "fts_index": {
                            "enabled": true,
                            "config": {}
                        },
                        "string_inverted_index": {
                            "enabled": false,
                            "config": {}
                        }
                    }
                },
                "category": {
                    "string": {
                        "fts_index": {
                            "enabled": false,
                            "config": {}
                        },
                        "string_inverted_index": {
                            "enabled": true,
                            "config": {}
                        }
                    }
                }
            }
        },
        "metadata": {
            "description": "Commons governance documents \u2014 MountainShares DAO",
            "status": "created_empty_2026-03-24",
            "wv_tagged": true
        },
        "dimension": 384,
        "tenant": "default_tenant",
        "database": "default_database",
        "log_position": 0,
        "version": 0
    },
    {
        "id": "79240788-0828-45f3-b1bc-a9a3593628a6",
        "name": "ms_jarvis_memory",
        "configuration_json": {
            "hnsw": {
                "space": "cosine",
                "ef_construction": 100,
                "ef_search": 100,
                "max_neighbors": 16,
                "resize_factor": 1.2,
                "sync_threshold": 1000
            },
            "spann": null,
            "embedding_function": null
        },
        "schema": {
            "defaults": {
                "string": {
                    "fts_index": {
                        "enabled": false,
                        "config": {}
                    },
                    "string_inverted_index": {
                        "enabled": true,
                        "config": {}
                    }
                },
                "float_list": {
                    "vector_index": {
                        "enabled": false,
                        "config": {
                            "space": "cosine",
                            "hnsw": {
                                "ef_construction": 100,
                                "max_neighbors": 16,
                                "ef_search": 100,
                                "num_threads": 32,
                                "batch_size": 100,
                                "sync_threshold": 1000,
                                "resize_factor": 1.2
                            }
                        }
                    }
                },
                "sparse_vector": {
                    "sparse_vector_index": {
                        "enabled": false,
                        "config": {
                            "embedding_function": {
                                "type": "unknown"
                            },
                            "bm25": false
                        }
                    }
                },
                "int": {
                    "int_inverted_index": {
                        "enabled": true,
                        "config": {}
                    }
                },
                "float": {
                    "float_inverted_index": {
                        "enabled": true,
                        "config": {}
                    }
                },
                "bool": {
                    "bool_inverted_index": {
                        "enabled": true,
                        "config": {}
                    }
                }
            },
            "keys": {
                "timestamp": {
                    "string": {
                        "fts_index": {
                            "enabled": false,
                            "config": {}
                        },
                        "string_inverted_index": {
                            "enabled": true,
                            "config": {}
                        }
                    }
                },
                "user_id": {
                    "string": {
                        "fts_index": {
                            "enabled": false,
                            "config": {}
                        },
                        "string_inverted_index": {
                            "enabled": true,
                            "config": {}
                        }
                    }
                },
                "#embedding": {
                    "float_list": {
                        "vector_index": {
                            "enabled": true,
                            "config": {
                                "space": "cosine",
                                "source_key": "#document",
                                "hnsw": {
                                    "ef_construction": 100,
                                    "max_neighbors": 16,
                                    "ef_search": 100,
                                    "num_threads": 32,
                                    "batch_size": 100,
                                    "sync_threshold": 1000,
                                    "resize_factor": 1.2
                                }
                            }
                        }
                    }
                },
                "#document": {
                    "string": {
                        "fts_index": {
                            "enabled": true,
                            "config": {}
                        },
                        "string_inverted_index": {
                            "enabled": false,
                            "config": {}
                        }
                    }
                }
            }
        },
        "metadata": {
            "hnsw:space": "cosine"
        },
        "dimension": 384,
        "tenant": "default_tenant",
        "database": "default_database",
        "log_position": 0,
        "version": 0
    },
    {
        "id": "872f538b-a930-4427-b309-19c1d081537d",
        "name": "health_rag",
        "configuration_json": {
            "hnsw": {
                "space": "l2",
                "ef_construction": 100,
                "ef_search": 100,
                "max_neighbors": 16,
                "resize_factor": 1.2,
                "sync_threshold": 1000
            },
            "spann": null,
            "embedding_function": {
                "type": "known",
                "name": "default",
                "config": {}
            }
        },
        "schema": {
            "defaults": {
                "string": {
                    "fts_index": {
                        "enabled": false,
                        "config": {}
                    },
                    "string_inverted_index": {
                        "enabled": true,
                        "config": {}
                    }
                },
                "float_list": {
                    "vector_index": {
                        "enabled": false,
                        "config": {
                            "space": "l2",
                            "embedding_function": {
                                "type": "known",
                                "name": "default",
                                "config": {}
                            },
                            "hnsw": {
                                "ef_construction": 100,
                                "max_neighbors": 16,
                                "ef_search": 100,
                                "num_threads": 32,
                                "batch_size": 100,
                                "sync_threshold": 1000,
                                "resize_factor": 1.2
                            }
                        }
                    }
                },
                "sparse_vector": {
                    "sparse_vector_index": {
                        "enabled": false,
                        "config": {
                            "embedding_function": {
                                "type": "unknown"
                            },
                            "bm25": false
                        }
                    }
                },
                "int": {
                    "int_inverted_index": {
                        "enabled": true,
                        "config": {}
                    }
                },
                "float": {
                    "float_inverted_index": {
                        "enabled": true,
                        "config": {}
                    }
                },
                "bool": {
                    "bool_inverted_index": {
                        "enabled": true,
                        "config": {}
                    }
                }
            },
            "keys": {
                "#embedding": {
                    "float_list": {
                        "vector_index": {
                            "enabled": true,
                            "config": {
                                "space": "l2",
                                "embedding_function": {
                                    "type": "known",
                                    "name": "default",
                                    "config": {}
                                },
                                "source_key": "#document",
                                "hnsw": {
                                    "ef_construction": 100,
                                    "max_neighbors": 16,
                                    "ef_search": 100,
                                    "num_threads": 32,
                                    "batch_size": 100,
                                    "sync_threshold": 1000,
                                    "resize_factor": 1.2
                                }
                            }
                        }
                    }
                },
                "wv_tagged": {
                    "bool": {
                        "bool_inverted_index": {
                            "enabled": true,
                            "config": {}
                        }
                    }
                },
                "#document": {
                    "string": {
                        "fts_index": {
                            "enabled": true,
                            "config": {}
                        },
                        "string_inverted_index": {
                            "enabled": false,
                            "config": {}
                        }
                    }
                },
                "category": {
                    "string": {
                        "fts_index": {
                            "enabled": false,
                            "config": {}
                        },
                        "string_inverted_index": {
                            "enabled": true,
                            "config": {}
                        }
                    }
                }
            }
        },
        "metadata": {
            "description": "Community health data \u2014 WV DHHR, county health depts",
            "status": "created_empty_2026-03-24",
            "wv_tagged": true
        },
        "dimension": 384,
        "tenant": "default_tenant",
        "database": "default_database",
        "log_position": 0,
        "version": 0
    },
    {
        "id": "8b101b8d-8d18-44b3-884e-a7112569a09e",
        "name": "conversation_history",
        "configuration_json": {
            "hnsw": {
                "space": "cosine",
                "ef_construction": 100,
                "ef_search": 100,
                "max_neighbors": 16,
                "resize_factor": 1.2,
                "sync_threshold": 1000
            },
            "spann": null,
            "embedding_function": null
        },
        "schema": {
            "defaults": {
                "string": {
                    "fts_index": {
                        "enabled": false,
                        "config": {}
                    },
                    "string_inverted_index": {
                        "enabled": true,
                        "config": {}
                    }
                },
                "float_list": {
                    "vector_index": {
                        "enabled": false,
                        "config": {
                            "space": "cosine",
                            "hnsw": {
                                "ef_construction": 100,
                                "max_neighbors": 16,
                                "ef_search": 100,
                                "num_threads": 32,
                                "batch_size": 100,
                                "sync_threshold": 1000,
                                "resize_factor": 1.2
                            }
                        }
                    }
                },
                "sparse_vector": {
                    "sparse_vector_index": {
                        "enabled": false,
                        "config": {
                            "embedding_function": {
                                "type": "unknown"
                            },
                            "bm25": false
                        }
                    }
                },
                "int": {
                    "int_inverted_index": {
                        "enabled": true,
                        "config": {}
                    }
                },
                "float": {
                    "float_inverted_index": {
                        "enabled": true,
                        "config": {}
                    }
                },
                "bool": {
                    "bool_inverted_index": {
                        "enabled": true,
                        "config": {}
                    }
                }
            },
            "keys": {
                "timestamp": {
                    "string": {
                        "fts_index": {
                            "enabled": false,
                            "config": {}
                        },
                        "string_inverted_index": {
                            "enabled": true,
                            "config": {}
                        }
                    }
                },
                "#document": {
                    "string": {
                        "fts_index": {
                            "enabled": true,
                            "config": {}
                        },
                        "string_inverted_index": {
                            "enabled": false,
                            "config": {}
                        }
                    }
                },
                "user_id": {
                    "string": {
                        "fts_index": {
                            "enabled": false,
                            "config": {}
                        },
                        "string_inverted_index": {
                            "enabled": true,
                            "config": {}
                        }
                    }
                },
                "#embedding": {
                    "float_list": {
                        "vector_index": {
                            "enabled": true,
                            "config": {
                                "space": "cosine",
                                "source_key": "#document",
                                "hnsw": {
                                    "ef_construction": 100,
                                    "max_neighbors": 16,
                                    "ef_search": 100,
                                    "num_threads": 32,
                                    "batch_size": 100,
                                    "sync_threshold": 1000,
                                    "resize_factor": 1.2
                                }
                            }
                        }
                    }
                }
            }
        },
        "metadata": {
            "hnsw:space": "cosine",
            "created": "2026-03-24",
            "description": "Turn-by-turn conversation context for Ms. Jarvis"
        },
        "dimension": 3,
        "tenant": "default_tenant",
        "database": "default_database",
        "log_position": 0,
        "version": 0
    },
    {
        "id": "8c359463-244c-4441-a698-b498fd1da5dc",
        "name": "psychological_rag",
        "configuration_json": {
            "hnsw": {
                "space": "l2",
                "ef_construction": 100,
                "ef_search": 100,
                "max_neighbors": 16,
                "resize_factor": 1.2,
                "sync_threshold": 1000
            },
            "spann": null,
            "embedding_function": {
                "type": "known",
                "name": "default",
                "config": {}
            }
        },
        "schema": {
            "defaults": {
                "string": {
                    "fts_index": {
                        "enabled": false,
                        "config": {}
                    },
                    "string_inverted_index": {
                        "enabled": true,
                        "config": {}
                    }
                },
                "float_list": {
                    "vector_index": {
                        "enabled": false,
                        "config": {
                            "space": "l2",
                            "embedding_function": {
                                "type": "known",
                                "name": "default",
                                "config": {}
                            },
                            "hnsw": {
                                "ef_construction": 100,
                                "max_neighbors": 16,
                                "ef_search": 100,
                                "num_threads": 32,
                                "batch_size": 100,
                                "sync_threshold": 1000,
                                "resize_factor": 1.2
                            }
                        }
                    }
                },
                "sparse_vector": {
                    "sparse_vector_index": {
                        "enabled": false,
                        "config": {
                            "embedding_function": {
                                "type": "unknown"
                            },
                            "bm25": false
                        }
                    }
                },
                "int": {
                    "int_inverted_index": {
                        "enabled": true,
                        "config": {}
                    }
                },
                "float": {
                    "float_inverted_index": {
                        "enabled": true,
                        "config": {}
                    }
                },
                "bool": {
                    "bool_inverted_index": {
                        "enabled": true,
                        "config": {}
                    }
                }
            },
            "keys": {
                "source": {
                    "string": {
                        "fts_index": {
                            "enabled": false,
                            "config": {}
                        },
                        "string_inverted_index": {
                            "enabled": true,
                            "config": {}
                        }
                    }
                },
                "category": {
                    "string": {
                        "fts_index": {
                            "enabled": false,
                            "config": {}
                        },
                        "string_inverted_index": {
                            "enabled": true,
                            "config": {}
                        }
                    }
                },
                "#embedding": {
                    "float_list": {
                        "vector_index": {
                            "enabled": true,
                            "config": {
                                "space": "l2",
                                "embedding_function": {
                                    "type": "known",
                                    "name": "default",
                                    "config": {}
                                },
                                "source_key": "#document",
                                "hnsw": {
                                    "ef_construction": 100,
                                    "max_neighbors": 16,
                                    "ef_search": 100,
                                    "num_threads": 32,
                                    "batch_size": 100,
                                    "sync_threshold": 1000,
                                    "resize_factor": 1.2
                                }
                            }
                        }
                    }
                },
                "page": {
                    "int": {
                        "int_inverted_index": {
                            "enabled": true,
                            "config": {}
                        }
                    }
                },
                "#document": {
                    "string": {
                        "fts_index": {
                            "enabled": true,
                            "config": {}
                        },
                        "string_inverted_index": {
                            "enabled": false,
                            "config": {}
                        }
                    }
                }
            }
        },
        "metadata": {
            "role": "rag",
            "domain": "psychological"
        },
        "dimension": 384,
        "tenant": "default_tenant",
        "database": "default_database",
        "log_position": 0,
        "version": 0
    },
    {
        "id": "ac277ccb-e1ec-45b6-b8b4-e40666f49f95",
        "name": "GBIM_sample",
        "configuration_json": {
            "hnsw": {
                "space": "l2",
                "ef_construction": 100,
                "ef_search": 100,
                "max_neighbors": 16,
                "resize_factor": 1.2,
                "sync_threshold": 1000
            },
            "spann": null,
            "embedding_function": {
                "type": "known",
                "name": "default",
                "config": {}
            }
        },
        "schema": {
            "defaults": {
                "string": {
                    "fts_index": {
                        "enabled": false,
                        "config": {}
                    },
                    "string_inverted_index": {
                        "enabled": true,
                        "config": {}
                    }
                },
                "float_list": {
                    "vector_index": {
                        "enabled": false,
                        "config": {
                            "space": "l2",
                            "embedding_function": {
                                "type": "known",
                                "name": "default",
                                "config": {}
                            },
                            "hnsw": {
                                "ef_construction": 100,
                                "max_neighbors": 16,
                                "ef_search": 100,
                                "num_threads": 32,
                                "batch_size": 100,
                                "sync_threshold": 1000,
                                "resize_factor": 1.2
                            }
                        }
                    }
                },
                "sparse_vector": {
                    "sparse_vector_index": {
                        "enabled": false,
                        "config": {
                            "embedding_function": {
                                "type": "unknown"
                            },
                            "bm25": false
                        }
                    }
                },
                "int": {
                    "int_inverted_index": {
                        "enabled": true,
                        "config": {}
                    }
                },
                "float": {
                    "float_inverted_index": {
                        "enabled": true,
                        "config": {}
                    }
                },
                "bool": {
                    "bool_inverted_index": {
                        "enabled": true,
                        "config": {}
                    }
                }
            },
            "keys": {
                "lon": {
                    "float": {
                        "float_inverted_index": {
                            "enabled": true,
                            "config": {}
                        }
                    }
                },
                "#document": {
                    "string": {
                        "fts_index": {
                            "enabled": true,
                            "config": {}
                        },
                        "string_inverted_index": {
                            "enabled": false,
                            "config": {}
                        }
                    }
                },
                "location": {
                    "string": {
                        "fts_index": {
                            "enabled": false,
                            "config": {}
                        },
                        "string_inverted_index": {
                            "enabled": true,
                            "config": {}
                        }
                    }
                },
                "timestamp": {
                    "string": {
                        "fts_index": {
                            "enabled": false,
                            "config": {}
                        },
                        "string_inverted_index": {
                            "enabled": true,
                            "config": {}
                        }
                    }
                },
                "county": {
                    "string": {
                        "fts_index": {
                            "enabled": false,
                            "config": {}
                        },
                        "string_inverted_index": {
                            "enabled": true,
                            "config": {}
                        }
                    }
                },
                "#embedding": {
                    "float_list": {
                        "vector_index": {
                            "enabled": true,
                            "config": {
                                "space": "l2",
                                "embedding_function": {
                                    "type": "known",
                                    "name": "default",
                                    "config": {}
                                },
                                "source_key": "#document",
                                "hnsw": {
                                    "ef_construction": 100,
                                    "max_neighbors": 16,
                                    "ef_search": 100,
                                    "num_threads": 32,
                                    "batch_size": 100,
                                    "sync_threshold": 1000,
                                    "resize_factor": 1.2
                                }
                            }
                        }
                    }
                },
                "quantum_tag": {
                    "string": {
                        "fts_index": {
                            "enabled": false,
                            "config": {}
                        },
                        "string_inverted_index": {
                            "enabled": true,
                            "config": {}
                        }
                    }
                },
                "state": {
                    "string": {
                        "fts_index": {
                            "enabled": false,
                            "config": {}
                        },
                        "string_inverted_index": {
                            "enabled": true,
                            "config": {}
                        }
                    }
                },
                "lat": {
                    "float": {
                        "float_inverted_index": {
                            "enabled": true,
                            "config": {}
                        }
                    }
                }
            }
        },
        "metadata": null,
        "dimension": 384,
        "tenant": "default_tenant",
        "database": "default_database",
        "log_position": 0,
        "version": 0
    },
    {
        "id": "b2a59ffc-a3a5-4c06-90c9-8954b33992f1",
        "name": "conversation_gbim_public",
        "configuration_json": {
            "hnsw": {
                "space": "l2",
                "ef_construction": 100,
                "ef_search": 100,
                "max_neighbors": 16,
                "resize_factor": 1.2,
                "sync_threshold": 1000
            },
            "spann": null,
            "embedding_function": {
                "type": "known",
                "name": "default",
                "config": {}
            }
        },
        "schema": {
            "defaults": {
                "string": {
                    "fts_index": {
                        "enabled": false,
                        "config": {}
                    },
                    "string_inverted_index": {
                        "enabled": true,
                        "config": {}
                    }
                },
                "float_list": {
                    "vector_index": {
                        "enabled": false,
                        "config": {
                            "space": "l2",
                            "embedding_function": {
                                "type": "known",
                                "name": "default",
                                "config": {}
                            },
                            "hnsw": {
                                "ef_construction": 100,
                                "max_neighbors": 16,
                                "ef_search": 100,
                                "num_threads": 32,
                                "batch_size": 100,
                                "sync_threshold": 1000,
                                "resize_factor": 1.2
                            }
                        }
                    }
                },
                "sparse_vector": {
                    "sparse_vector_index": {
                        "enabled": false,
                        "config": {
                            "embedding_function": {
                                "type": "unknown"
                            },
                            "bm25": false
                        }
                    }
                },
                "int": {
                    "int_inverted_index": {
                        "enabled": true,
                        "config": {}
                    }
                },
                "float": {
                    "float_inverted_index": {
                        "enabled": true,
                        "config": {}
                    }
                },
                "bool": {
                    "bool_inverted_index": {
                        "enabled": true,
                        "config": {}
                    }
                }
            },
            "keys": {
                "county": {
                    "string": {
                        "fts_index": {
                            "enabled": false,
                            "config": {}
                        },
                        "string_inverted_index": {
                            "enabled": true,
                            "config": {}
                        }
                    }
                },
                "belief_id": {
                    "string": {
                        "fts_index": {
                            "enabled": false,
                            "config": {}
                        },
                        "string_inverted_index": {
                            "enabled": true,
                            "config": {}
                        }
                    }
                },
                "user_id": {
                    "string": {
                        "fts_index": {
                            "enabled": false,
                            "config": {}
                        },
                        "string_inverted_index": {
                            "enabled": true,
                            "config": {}
                        }
                    }
                },
                "#embedding": {
                    "float_list": {
                        "vector_index": {
                            "enabled": true,
                            "config": {
                                "space": "l2",
                                "embedding_function": {
                                    "type": "known",
                                    "name": "default",
                                    "config": {}
                                },
                                "source_key": "#document",
                                "hnsw": {
                                    "ef_construction": 100,
                                    "max_neighbors": 16,
                                    "ef_search": 100,
                                    "num_threads": 32,
                                    "batch_size": 100,
                                    "sync_threshold": 1000,
                                    "resize_factor": 1.2
                                }
                            }
                        }
                    }
                },
                "privacy_tier": {
                    "string": {
                        "fts_index": {
                            "enabled": false,
                            "config": {}
                        },
                        "string_inverted_index": {
                            "enabled": true,
                            "config": {}
                        }
                    }
                },
                "turn_number": {
                    "int": {
                        "int_inverted_index": {
                            "enabled": true,
                            "config": {}
                        }
                    }
                },
                "#document": {
                    "string": {
                        "fts_index": {
                            "enabled": true,
                            "config": {}
                        },
                        "string_inverted_index": {
                            "enabled": false,
                            "config": {}
                        }
                    }
                },
                "immutability_hash": {
                    "string": {
                        "fts_index": {
                            "enabled": false,
                            "config": {}
                        },
                        "string_inverted_index": {
                            "enabled": true,
                            "config": {}
                        }
                    }
                },
                "created_at": {
                    "string": {
                        "fts_index": {
                            "enabled": false,
                            "config": {}
                        },
                        "string_inverted_index": {
                            "enabled": true,
                            "config": {}
                        }
                    }
                },
                "state": {
                    "string": {
                        "fts_index": {
                            "enabled": false,
                            "config": {}
                        },
                        "string_inverted_index": {
                            "enabled": true,
                            "config": {}
                        }
                    }
                },
                "place": {
                    "string": {
                        "fts_index": {
                            "enabled": false,
                            "config": {}
                        },
                        "string_inverted_index": {
                            "enabled": true,
                            "config": {}
                        }
                    }
                },
                "intent": {
                    "string": {
                        "fts_index": {
                            "enabled": false,
                            "config": {}
                        },
                        "string_inverted_index": {
                            "enabled": true,
                            "config": {}
                        }
                    }
                },
                "session_id": {
                    "string": {
                        "fts_index": {
                            "enabled": false,
                            "config": {}
                        },
                        "string_inverted_index": {
                            "enabled": true,
                            "config": {}
                        }
                    }
                }
            }
        },
        "metadata": {
            "access": "dao_governed",
            "gbim_axes": "what,where,when,why,for_whom",
            "privacy_tier": "public",
            "description": "Public conversation GBIM \u2014 anonymized community patterns"
        },
        "dimension": 384,
        "tenant": "default_tenant",
        "database": "default_database",
        "log_position": 0,
        "version": 0
    },
    {
        "id": "bfce28c9-a700-48c6-a133-25a43f14bb81",
        "name": "spiritual_rag",
        "configuration_json": {
            "hnsw": {
                "space": "cosine",
                "ef_construction": 100,
                "ef_search": 100,
                "max_neighbors": 16,
                "resize_factor": 1.2,
                "sync_threshold": 1000
            },
            "spann": null,
            "embedding_function": {
                "type": "known",
                "name": "default",
                "config": {}
            }
        },
        "schema": {
            "defaults": {
                "string": {
                    "fts_index": {
                        "enabled": false,
                        "config": {}
                    },
                    "string_inverted_index": {
                        "enabled": true,
                        "config": {}
                    }
                },
                "float_list": {
                    "vector_index": {
                        "enabled": false,
                        "config": {
                            "space": "cosine",
                            "embedding_function": {
                                "type": "known",
                                "name": "default",
                                "config": {}
                            },
                            "hnsw": {
                                "ef_construction": 100,
                                "max_neighbors": 16,
                                "ef_search": 100,
                                "num_threads": 32,
                                "batch_size": 100,
                                "sync_threshold": 1000,
                                "resize_factor": 1.2
                            }
                        }
                    }
                },
                "sparse_vector": {
                    "sparse_vector_index": {
                        "enabled": false,
                        "config": {
                            "embedding_function": {
                                "type": "unknown"
                            },
                            "bm25": false
                        }
                    }
                },
                "int": {
                    "int_inverted_index": {
                        "enabled": true,
                        "config": {}
                    }
                },
                "float": {
                    "float_inverted_index": {
                        "enabled": true,
                        "config": {}
                    }
                },
                "bool": {
                    "bool_inverted_index": {
                        "enabled": true,
                        "config": {}
                    }
                }
            },
            "keys": {
                "#embedding": {
                    "float_list": {
                        "vector_index": {
                            "enabled": true,
                            "config": {
                                "space": "cosine",
                                "embedding_function": {
                                    "type": "known",
                                    "name": "default",
                                    "config": {}
                                },
                                "source_key": "#document",
                                "hnsw": {
                                    "ef_construction": 100,
                                    "max_neighbors": 16,
                                    "ef_search": 100,
                                    "num_threads": 32,
                                    "batch_size": 100,
                                    "sync_threshold": 1000,
                                    "resize_factor": 1.2
                                }
                            }
                        }
                    }
                },
                "#document": {
                    "string": {
                        "fts_index": {
                            "enabled": true,
                            "config": {}
                        },
                        "string_inverted_index": {
                            "enabled": false,
                            "config": {}
                        }
                    }
                },
                "region": {
                    "string": {
                        "fts_index": {
                            "enabled": false,
                            "config": {}
                        },
                        "string_inverted_index": {
                            "enabled": true,
                            "config": {}
                        }
                    }
                },
                "origin_lon": {
                    "string": {
                        "fts_index": {
                            "enabled": false,
                            "config": {}
                        },
                        "string_inverted_index": {
                            "enabled": true,
                            "config": {}
                        }
                    }
                },
                "source_file": {
                    "string": {
                        "fts_index": {
                            "enabled": false,
                            "config": {}
                        },
                        "string_inverted_index": {
                            "enabled": true,
                            "config": {}
                        }
                    }
                },
                "cultural_family": {
                    "string": {
                        "fts_index": {
                            "enabled": false,
                            "config": {}
                        },
                        "string_inverted_index": {
                            "enabled": true,
                            "config": {}
                        }
                    }
                },
                "title": {
                    "string": {
                        "fts_index": {
                            "enabled": false,
                            "config": {}
                        },
                        "string_inverted_index": {
                            "enabled": true,
                            "config": {}
                        }
                    }
                },
                "chunk_index": {
                    "string": {
                        "fts_index": {
                            "enabled": false,
                            "config": {}
                        },
                        "string_inverted_index": {
                            "enabled": true,
                            "config": {}
                        }
                    }
                },
                "tradition": {
                    "string": {
                        "fts_index": {
                            "enabled": false,
                            "config": {}
                        },
                        "string_inverted_index": {
                            "enabled": true,
                            "config": {}
                        }
                    }
                },
                "origin_lat": {
                    "string": {
                        "fts_index": {
                            "enabled": false,
                            "config": {}
                        },
                        "string_inverted_index": {
                            "enabled": true,
                            "config": {}
                        }
                    }
                },
                "origin_notes": {
                    "string": {
                        "fts_index": {
                            "enabled": false,
                            "config": {}
                        },
                        "string_inverted_index": {
                            "enabled": true,
                            "config": {}
                        }
                    }
                }
            }
        },
        "metadata": {
            "role": "rag",
            "description": "Spiritual RAG \u2014 fed from spiritual_texts 19k items",
            "domain": "spiritual",
            "hnsw:space": "cosine"
        },
        "dimension": 384,
        "tenant": "default_tenant",
        "database": "default_database",
        "log_position": 0,
        "version": 0
    },
    {
        "id": "cb0e2432-3a8c-44c0-8839-d94beebff42f",
        "name": "meeting_minutes",
        "configuration_json": {
            "hnsw": {
                "space": "l2",
                "ef_construction": 100,
                "ef_search": 100,
                "max_neighbors": 16,
                "resize_factor": 1.2,
                "sync_threshold": 1000
            },
            "spann": null,
            "embedding_function": {
                "type": "known",
                "name": "default",
                "config": {}
            }
        },
        "schema": {
            "defaults": {
                "string": {
                    "fts_index": {
                        "enabled": false,
                        "config": {}
                    },
                    "string_inverted_index": {
                        "enabled": true,
                        "config": {}
                    }
                },
                "float_list": {
                    "vector_index": {
                        "enabled": false,
                        "config": {
                            "space": "l2",
                            "embedding_function": {
                                "type": "known",
                                "name": "default",
                                "config": {}
                            },
                            "hnsw": {
                                "ef_construction": 100,
                                "max_neighbors": 16,
                                "ef_search": 100,
                                "num_threads": 32,
                                "batch_size": 100,
                                "sync_threshold": 1000,
                                "resize_factor": 1.2
                            }
                        }
                    }
                },
                "sparse_vector": {
                    "sparse_vector_index": {
                        "enabled": false,
                        "config": {
                            "embedding_function": {
                                "type": "unknown"
                            },
                            "bm25": false
                        }
                    }
                },
                "int": {
                    "int_inverted_index": {
                        "enabled": true,
                        "config": {}
                    }
                },
                "float": {
                    "float_inverted_index": {
                        "enabled": true,
                        "config": {}
                    }
                },
                "bool": {
                    "bool_inverted_index": {
                        "enabled": true,
                        "config": {}
                    }
                }
            },
            "keys": {
                "status": {
                    "string": {
                        "fts_index": {
                            "enabled": false,
                            "config": {}
                        },
                        "string_inverted_index": {
                            "enabled": true,
                            "config": {}
                        }
                    }
                },
                "category": {
                    "string": {
                        "fts_index": {
                            "enabled": false,
                            "config": {}
                        },
                        "string_inverted_index": {
                            "enabled": true,
                            "config": {}
                        }
                    }
                },
                "#document": {
                    "string": {
                        "fts_index": {
                            "enabled": true,
                            "config": {}
                        },
                        "string_inverted_index": {
                            "enabled": false,
                            "config": {}
                        }
                    }
                },
                "wv_tagged": {
                    "bool": {
                        "bool_inverted_index": {
                            "enabled": true,
                            "config": {}
                        }
                    }
                },
                "#embedding": {
                    "float_list": {
                        "vector_index": {
                            "enabled": true,
                            "config": {
                                "space": "l2",
                                "embedding_function": {
                                    "type": "known",
                                    "name": "default",
                                    "config": {}
                                },
                                "source_key": "#document",
                                "hnsw": {
                                    "ef_construction": 100,
                                    "max_neighbors": 16,
                                    "ef_search": 100,
                                    "num_threads": 32,
                                    "batch_size": 100,
                                    "sync_threshold": 1000,
                                    "resize_factor": 1.2
                                }
                            }
                        }
                    }
                }
            }
        },
        "metadata": {
            "description": "Community meeting minutes \u2014 Fayette County and regional",
            "status": "created_empty_2026-03-24",
            "wv_tagged": true
        },
        "dimension": 384,
        "tenant": "default_tenant",
        "database": "default_database",
        "log_position": 0,
        "version": 0
    },
    {
        "id": "d59f93ad-fc41-4965-8f93-7da47e90657a",
        "name": "address_points",
        "configuration_json": {
            "hnsw": {
                "space": "l2",
                "ef_construction": 100,
                "ef_search": 100,
                "max_neighbors": 16,
                "resize_factor": 1.2,
                "sync_threshold": 1000
            },
            "spann": null,
            "embedding_function": {
                "type": "known",
                "name": "default",
                "config": {}
            }
        },
        "schema": {
            "defaults": {
                "string": {
                    "fts_index": {
                        "enabled": false,
                        "config": {}
                    },
                    "string_inverted_index": {
                        "enabled": true,
                        "config": {}
                    }
                },
                "float_list": {
                    "vector_index": {
                        "enabled": false,
                        "config": {
                            "space": "l2",
                            "embedding_function": {
                                "type": "known",
                                "name": "default",
                                "config": {}
                            },
                            "hnsw": {
                                "ef_construction": 100,
                                "max_neighbors": 16,
                                "ef_search": 100,
                                "num_threads": 32,
                                "batch_size": 100,
                                "sync_threshold": 1000,
                                "resize_factor": 1.2
                            }
                        }
                    }
                },
                "sparse_vector": {
                    "sparse_vector_index": {
                        "enabled": false,
                        "config": {
                            "embedding_function": {
                                "type": "unknown"
                            },
                            "bm25": false
                        }
                    }
                },
                "int": {
                    "int_inverted_index": {
                        "enabled": true,
                        "config": {}
                    }
                },
                "float": {
                    "float_inverted_index": {
                        "enabled": true,
                        "config": {}
                    }
                },
                "bool": {
                    "bool_inverted_index": {
                        "enabled": true,
                        "config": {}
                    }
                }
            },
            "keys": {
                "#document": {
                    "string": {
                        "fts_index": {
                            "enabled": true,
                            "config": {}
                        },
                        "string_inverted_index": {
                            "enabled": false,
                            "config": {}
                        }
                    }
                },
                "#embedding": {
                    "float_list": {
                        "vector_index": {
                            "enabled": true,
                            "config": {
                                "space": "l2",
                                "embedding_function": {
                                    "type": "known",
                                    "name": "default",
                                    "config": {}
                                },
                                "source_key": "#document",
                                "hnsw": {
                                    "ef_construction": 100,
                                    "max_neighbors": 16,
                                    "ef_search": 100,
                                    "num_threads": 32,
                                    "batch_size": 100,
                                    "sync_threshold": 1000,
                                    "resize_factor": 1.2
                                }
                            }
                        }
                    }
                },
                "layer_type": {
                    "string": {
                        "fts_index": {
                            "enabled": false,
                            "config": {}
                        },
                        "string_inverted_index": {
                            "enabled": true,
                            "config": {}
                        }
                    }
                },
                "esn": {
                    "string": {
                        "fts_index": {
                            "enabled": false,
                            "config": {}
                        },
                        "string_inverted_index": {
                            "enabled": true,
                            "config": {}
                        }
                    }
                },
                "county": {
                    "string": {
                        "fts_index": {
                            "enabled": false,
                            "config": {}
                        },
                        "string_inverted_index": {
                            "enabled": true,
                            "config": {}
                        }
                    }
                },
                "record_count": {
                    "int": {
                        "int_inverted_index": {
                            "enabled": true,
                            "config": {}
                        }
                    }
                },
                "zip": {
                    "string": {
                        "fts_index": {
                            "enabled": false,
                            "config": {}
                        },
                        "string_inverted_index": {
                            "enabled": true,
                            "config": {}
                        }
                    }
                },
                "state": {
                    "string": {
                        "fts_index": {
                            "enabled": false,
                            "config": {}
                        },
                        "string_inverted_index": {
                            "enabled": true,
                            "config": {}
                        }
                    }
                },
                "columns": {
                    "string": {
                        "fts_index": {
                            "enabled": false,
                            "config": {}
                        },
                        "string_inverted_index": {
                            "enabled": true,
                            "config": {}
                        }
                    }
                },
                "source": {
                    "string": {
                        "fts_index": {
                            "enabled": false,
                            "config": {}
                        },
                        "string_inverted_index": {
                            "enabled": true,
                            "config": {}
                        }
                    }
                }
            }
        },
        "metadata": null,
        "dimension": 768,
        "tenant": "default_tenant",
        "database": "default_database",
        "log_position": 0,
        "version": 0
    },
    {
        "id": "e0caffcd-136e-4ac2-addc-f4c9b1814ac2",
        "name": "legal_rag",
        "configuration_json": {
            "hnsw": {
                "space": "l2",
                "ef_construction": 100,
                "ef_search": 100,
                "max_neighbors": 16,
                "resize_factor": 1.2,
                "sync_threshold": 1000
            },
            "spann": null,
            "embedding_function": {
                "type": "known",
                "name": "default",
                "config": {}
            }
        },
        "schema": {
            "defaults": {
                "string": {
                    "fts_index": {
                        "enabled": false,
                        "config": {}
                    },
                    "string_inverted_index": {
                        "enabled": true,
                        "config": {}
                    }
                },
                "float_list": {
                    "vector_index": {
                        "enabled": false,
                        "config": {
                            "space": "l2",
                            "embedding_function": {
                                "type": "known",
                                "name": "default",
                                "config": {}
                            },
                            "hnsw": {
                                "ef_construction": 100,
                                "max_neighbors": 16,
                                "ef_search": 100,
                                "num_threads": 32,
                                "batch_size": 100,
                                "sync_threshold": 1000,
                                "resize_factor": 1.2
                            }
                        }
                    }
                },
                "sparse_vector": {
                    "sparse_vector_index": {
                        "enabled": false,
                        "config": {
                            "embedding_function": {
                                "type": "unknown"
                            },
                            "bm25": false
                        }
                    }
                },
                "int": {
                    "int_inverted_index": {
                        "enabled": true,
                        "config": {}
                    }
                },
                "float": {
                    "float_inverted_index": {
                        "enabled": true,
                        "config": {}
                    }
                },
                "bool": {
                    "bool_inverted_index": {
                        "enabled": true,
                        "config": {}
                    }
                }
            },
            "keys": {
                "#embedding": {
                    "float_list": {
                        "vector_index": {
                            "enabled": true,
                            "config": {
                                "space": "l2",
                                "embedding_function": {
                                    "type": "known",
                                    "name": "default",
                                    "config": {}
                                },
                                "source_key": "#document",
                                "hnsw": {
                                    "ef_construction": 100,
                                    "max_neighbors": 16,
                                    "ef_search": 100,
                                    "num_threads": 32,
                                    "batch_size": 100,
                                    "sync_threshold": 1000,
                                    "resize_factor": 1.2
                                }
                            }
                        }
                    }
                },
                "#document": {
                    "string": {
                        "fts_index": {
                            "enabled": true,
                            "config": {}
                        },
                        "string_inverted_index": {
                            "enabled": false,
                            "config": {}
                        }
                    }
                },
                "category": {
                    "string": {
                        "fts_index": {
                            "enabled": false,
                            "config": {}
                        },
                        "string_inverted_index": {
                            "enabled": true,
                            "config": {}
                        }
                    }
                },
                "wv_tagged": {
                    "bool": {
                        "bool_inverted_index": {
                            "enabled": true,
                            "config": {}
                        }
                    }
                }
            }
        },
        "metadata": {
            "status": "created_empty_2026-03-24",
            "description": "Legal and regulatory documents \u2014 WV code and federal",
            "wv_tagged": true
        },
        "dimension": 384,
        "tenant": "default_tenant",
        "database": "default_database",
        "log_position": 0,
        "version": 0
    },
    {
        "id": "e666b46d-e04f-4fd6-a0ce-067a06f491b6",
        "name": "gbim_worldview_entities",
        "configuration_json": {
            "hnsw": {
                "space": "l2",
                "ef_construction": 100,
                "ef_search": 100,
                "max_neighbors": 16,
                "resize_factor": 1.2,
                "sync_threshold": 1000
            },
            "spann": null,
            "embedding_function": {
                "type": "known",
                "name": "default",
                "config": {}
            }
        },
        "schema": {
            "defaults": {
                "string": {
                    "fts_index": {
                        "enabled": false,
                        "config": {}
                    },
                    "string_inverted_index": {
                        "enabled": true,
                        "config": {}
                    }
                },
                "float_list": {
                    "vector_index": {
                        "enabled": false,
                        "config": {
                            "space": "l2",
                            "embedding_function": {
                                "type": "known",
                                "name": "default",
                                "config": {}
                            },
                            "hnsw": {
                                "ef_construction": 100,
                                "max_neighbors": 16,
                                "ef_search": 100,
                                "num_threads": 32,
                                "batch_size": 100,
                                "sync_threshold": 1000,
                                "resize_factor": 1.2
                            }
                        }
                    }
                },
                "sparse_vector": {
                    "sparse_vector_index": {
                        "enabled": false,
                        "config": {
                            "embedding_function": {
                                "type": "unknown"
                            },
                            "bm25": false
                        }
                    }
                },
                "int": {
                    "int_inverted_index": {
                        "enabled": true,
                        "config": {}
                    }
                },
                "float": {
                    "float_inverted_index": {
                        "enabled": true,
                        "config": {}
                    }
                },
                "bool": {
                    "bool_inverted_index": {
                        "enabled": true,
                        "config": {}
                    }
                }
            },
            "keys": {
                "source_table": {
                    "string": {
                        "fts_index": {
                            "enabled": false,
                            "config": {}
                        },
                        "string_inverted_index": {
                            "enabled": true,
                            "config": {}
                        }
                    }
                },
                "coord_srid": {
                    "string": {
                        "fts_index": {
                            "enabled": false,
                            "config": {}
                        },
                        "string_inverted_index": {
                            "enabled": true,
                            "config": {}
                        }
                    }
                },
                "source_pk": {
                    "string": {
                        "fts_index": {
                            "enabled": false,
                            "config": {}
                        },
                        "string_inverted_index": {
                            "enabled": true,
                            "config": {}
                        }
                    }
                },
                "#document": {
                    "string": {
                        "fts_index": {
                            "enabled": true,
                            "config": {}
                        },
                        "string_inverted_index": {
                            "enabled": false,
                            "config": {}
                        }
                    }
                },
                "entity_type": {
                    "string": {
                        "fts_index": {
                            "enabled": false,
                            "config": {}
                        },
                        "string_inverted_index": {
                            "enabled": true,
                            "config": {}
                        }
                    }
                },
                "belief_state": {
                    "string": {
                        "fts_index": {
                            "enabled": false,
                            "config": {}
                        },
                        "string_inverted_index": {
                            "enabled": true,
                            "config": {}
                        }
                    }
                },
                "created_at": {
                    "string": {
                        "fts_index": {
                            "enabled": false,
                            "config": {}
                        },
                        "string_inverted_index": {
                            "enabled": true,
                            "config": {}
                        }
                    }
                },
                "label": {
                    "string": {
                        "fts_index": {
                            "enabled": false,
                            "config": {}
                        },
                        "string_inverted_index": {
                            "enabled": true,
                            "config": {}
                        }
                    }
                },
                "#embedding": {
                    "float_list": {
                        "vector_index": {
                            "enabled": true,
                            "config": {
                                "space": "l2",
                                "embedding_function": {
                                    "type": "known",
                                    "name": "default",
                                    "config": {}
                                },
                                "source_key": "#document",
                                "hnsw": {
                                    "ef_construction": 100,
                                    "max_neighbors": 16,
                                    "ef_search": 100,
                                    "num_threads": 32,
                                    "batch_size": 100,
                                    "sync_threshold": 1000,
                                    "resize_factor": 1.2
                                }
                            }
                        }
                    }
                },
                "worldview_id": {
                    "string": {
                        "fts_index": {
                            "enabled": false,
                            "config": {}
                        },
                        "string_inverted_index": {
                            "enabled": true,
                            "config": {}
                        }
                    }
                },
                "centroid_y": {
                    "string": {
                        "fts_index": {
                            "enabled": false,
                            "config": {}
                        },
                        "string_inverted_index": {
                            "enabled": true,
                            "config": {}
                        }
                    }
                },
                "id": {
                    "string": {
                        "fts_index": {
                            "enabled": false,
                            "config": {}
                        },
                        "string_inverted_index": {
                            "enabled": true,
                            "config": {}
                        }
                    }
                },
                "centroid_x": {
                    "string": {
                        "fts_index": {
                            "enabled": false,
                            "config": {}
                        },
                        "string_inverted_index": {
                            "enabled": true,
                            "config": {}
                        }
                    }
                },
                "parcel_resolution": {
                    "string": {
                        "fts_index": {
                            "enabled": false,
                            "config": {}
                        },
                        "string_inverted_index": {
                            "enabled": true,
                            "config": {}
                        }
                    }
                }
            }
        },
        "metadata": {
            "worldview_id": "002c2c84-2f18-40b7-8a98-b8d813dd6cc7",
            "description": "GBIM entities"
        },
        "dimension": 384,
        "tenant": "default_tenant",
        "database": "default_database",
        "log_position": 0,
        "version": 0
    },
    {
        "id": "e7e83578-973e-474e-a6d4-ea91d5d5289d",
        "name": "autonomous_learner",
        "configuration_json": {
            "hnsw": {
                "space": "l2",
                "ef_construction": 100,
                "ef_search": 100,
                "max_neighbors": 16,
                "resize_factor": 1.2,
                "sync_threshold": 1000
            },
            "spann": null,
            "embedding_function": {
                "type": "known",
                "name": "default",
                "config": {}
            }
        },
        "schema": {
            "defaults": {
                "string": {
                    "fts_index": {
                        "enabled": false,
                        "config": {}
                    },
                    "string_inverted_index": {
                        "enabled": true,
                        "config": {}
                    }
                },
                "float_list": {
                    "vector_index": {
                        "enabled": false,
                        "config": {
                            "space": "l2",
                            "embedding_function": {
                                "type": "known",
                                "name": "default",
                                "config": {}
                            },
                            "hnsw": {
                                "ef_construction": 100,
                                "max_neighbors": 16,
                                "ef_search": 100,
                                "num_threads": 32,
                                "batch_size": 100,
                                "sync_threshold": 1000,
                                "resize_factor": 1.2
                            }
                        }
                    }
                },
                "sparse_vector": {
                    "sparse_vector_index": {
                        "enabled": false,
                        "config": {
                            "embedding_function": {
                                "type": "unknown"
                            },
                            "bm25": false
                        }
                    }
                },
                "int": {
                    "int_inverted_index": {
                        "enabled": true,
                        "config": {}
                    }
                },
                "float": {
                    "float_inverted_index": {
                        "enabled": true,
                        "config": {}
                    }
                },
                "bool": {
                    "bool_inverted_index": {
                        "enabled": true,
                        "config": {}
                    }
                }
            },
            "keys": {
                "feature_count": {
                    "int": {
                        "int_inverted_index": {
                            "enabled": true,
                            "config": {}
                        }
                    }
                },
                "learned_at": {
                    "string": {
                        "fts_index": {
                            "enabled": false,
                            "config": {}
                        },
                        "string_inverted_index": {
                            "enabled": true,
                            "config": {}
                        }
                    }
                },
                "entity_type": {
                    "string": {
                        "fts_index": {
                            "enabled": false,
                            "config": {}
                        },
                        "string_inverted_index": {
                            "enabled": true,
                            "config": {}
                        }
                    }
                },
                "user_id": {
                    "string": {
                        "fts_index": {
                            "enabled": false,
                            "config": {}
                        },
                        "string_inverted_index": {
                            "enabled": true,
                            "config": {}
                        }
                    }
                },
                "services": {
                    "string": {
                        "fts_index": {
                            "enabled": false,
                            "config": {}
                        },
                        "string_inverted_index": {
                            "enabled": true,
                            "config": {}
                        }
                    }
                },
                "topic": {
                    "string": {
                        "fts_index": {
                            "enabled": false,
                            "config": {}
                        },
                        "string_inverted_index": {
                            "enabled": true,
                            "config": {}
                        }
                    }
                },
                "table_key": {
                    "string": {
                        "fts_index": {
                            "enabled": false,
                            "config": {}
                        },
                        "string_inverted_index": {
                            "enabled": true,
                            "config": {}
                        }
                    }
                },
                "source": {
                    "string": {
                        "fts_index": {
                            "enabled": false,
                            "config": {}
                        },
                        "string_inverted_index": {
                            "enabled": true,
                            "config": {}
                        }
                    }
                },
                "total_pop": {
                    "int": {
                        "int_inverted_index": {
                            "enabled": true,
                            "config": {}
                        }
                    }
                },
                "action_type": {
                    "string": {
                        "fts_index": {
                            "enabled": false,
                            "config": {}
                        },
                        "string_inverted_index": {
                            "enabled": true,
                            "config": {}
                        }
                    }
                },
                "layer_key": {
                    "string": {
                        "fts_index": {
                            "enabled": false,
                            "config": {}
                        },
                        "string_inverted_index": {
                            "enabled": true,
                            "config": {}
                        }
                    }
                },
                "chunk_idx": {
                    "int": {
                        "int_inverted_index": {
                            "enabled": true,
                            "config": {}
                        }
                    }
                },
                "#document": {
                    "string": {
                        "fts_index": {
                            "enabled": true,
                            "config": {}
                        },
                        "string_inverted_index": {
                            "enabled": false,
                            "config": {}
                        }
                    }
                },
                "collection": {
                    "string": {
                        "fts_index": {
                            "enabled": false,
                            "config": {}
                        },
                        "string_inverted_index": {
                            "enabled": true,
                            "config": {}
                        }
                    }
                },
                "#embedding": {
                    "float_list": {
                        "vector_index": {
                            "enabled": true,
                            "config": {
                                "space": "l2",
                                "embedding_function": {
                                    "type": "known",
                                    "name": "default",
                                    "config": {}
                                },
                                "source_key": "#document",
                                "hnsw": {
                                    "ef_construction": 100,
                                    "max_neighbors": 16,
                                    "ef_search": 100,
                                    "num_threads": 32,
                                    "batch_size": 100,
                                    "sync_threshold": 1000,
                                    "resize_factor": 1.2
                                }
                            }
                        }
                    }
                },
                "cycle": {
                    "int": {
                        "int_inverted_index": {
                            "enabled": true,
                            "config": {}
                        }
                    }
                },
                "category": {
                    "string": {
                        "fts_index": {
                            "enabled": false,
                            "config": {}
                        },
                        "string_inverted_index": {
                            "enabled": true,
                            "config": {}
                        }
                    }
                },
                "timestamp": {
                    "string": {
                        "fts_index": {
                            "enabled": false,
                            "config": {}
                        },
                        "string_inverted_index": {
                            "enabled": true,
                            "config": {}
                        }
                    }
                },
                "domain": {
                    "string": {
                        "fts_index": {
                            "enabled": false,
                            "config": {}
                        },
                        "string_inverted_index": {
                            "enabled": true,
                            "config": {}
                        }
                    }
                },
                "index": {
                    "int": {
                        "int_inverted_index": {
                            "enabled": true,
                            "config": {}
                        }
                    }
                },
                "type": {
                    "string": {
                        "fts_index": {
                            "enabled": false,
                            "config": {}
                        },
                        "string_inverted_index": {
                            "enabled": true,
                            "config": {}
                        }
                    }
                },
                "actor_role": {
                    "string": {
                        "fts_index": {
                            "enabled": false,
                            "config": {}
                        },
                        "string_inverted_index": {
                            "enabled": true,
                            "config": {}
                        }
                    }
                },
                "decision": {
                    "string": {
                        "fts_index": {
                            "enabled": false,
                            "config": {}
                        },
                        "string_inverted_index": {
                            "enabled": true,
                            "config": {}
                        }
                    }
                }
            }
        },
        "metadata": null,
        "dimension": 384,
        "tenant": "default_tenant",
        "database": "default_database",
        "log_position": 0,
        "version": 0
    },
    {
        "id": "f6d0a9cd-4c76-4b7d-be6a-5249db9ff7ab",
        "name": "contracts",
        "configuration_json": {
            "hnsw": {
                "space": "cosine",
                "ef_construction": 100,
                "ef_search": 100,
                "max_neighbors": 16,
                "resize_factor": 1.2,
                "sync_threshold": 1000
            },
            "spann": null,
            "embedding_function": {
                "type": "known",
                "name": "default",
                "config": {}
            }
        },
        "schema": {
            "defaults": {
                "string": {
                    "fts_index": {
                        "enabled": false,
                        "config": {}
                    },
                    "string_inverted_index": {
                        "enabled": true,
                        "config": {}
                    }
                },
                "float_list": {
                    "vector_index": {
                        "enabled": false,
                        "config": {
                            "space": "cosine",
                            "embedding_function": {
                                "type": "known",
                                "name": "default",
                                "config": {}
                            },
                            "hnsw": {
                                "ef_construction": 100,
                                "max_neighbors": 16,
                                "ef_search": 100,
                                "num_threads": 32,
                                "batch_size": 100,
                                "sync_threshold": 1000,
                                "resize_factor": 1.2
                            }
                        }
                    }
                },
                "sparse_vector": {
                    "sparse_vector_index": {
                        "enabled": false,
                        "config": {
                            "embedding_function": {
                                "type": "unknown"
                            },
                            "bm25": false
                        }
                    }
                },
                "int": {
                    "int_inverted_index": {
                        "enabled": true,
                        "config": {}
                    }
                },
                "float": {
                    "float_inverted_index": {
                        "enabled": true,
                        "config": {}
                    }
                },
                "bool": {
                    "bool_inverted_index": {
                        "enabled": true,
                        "config": {}
                    }
                }
            },
            "keys": {
                "source": {
                    "string": {
                        "fts_index": {
                            "enabled": false,
                            "config": {}
                        },
                        "string_inverted_index": {
                            "enabled": true,
                            "config": {}
                        }
                    }
                },
                "#document": {
                    "string": {
                        "fts_index": {
                            "enabled": true,
                            "config": {}
                        },
                        "string_inverted_index": {
                            "enabled": false,
                            "config": {}
                        }
                    }
                },
                "type": {
                    "string": {
                        "fts_index": {
                            "enabled": false,
                            "config": {}
                        },
                        "string_inverted_index": {
                            "enabled": true,
                            "config": {}
                        }
                    }
                },
                "#embedding": {
                    "float_list": {
                        "vector_index": {
                            "enabled": true,
                            "config": {
                                "space": "cosine",
                                "embedding_function": {
                                    "type": "known",
                                    "name": "default",
                                    "config": {}
                                },
                                "source_key": "#document",
                                "hnsw": {
                                    "ef_construction": 100,
                                    "max_neighbors": 16,
                                    "ef_search": 100,
                                    "num_threads": 32,
                                    "batch_size": 100,
                                    "sync_threshold": 1000,
                                    "resize_factor": 1.2
                                }
                            }
                        }
                    }
                }
            }
        },
        "metadata": {
            "hnsw:space": "cosine"
        },
        "dimension": 384,
        "tenant": "default_tenant",
        "database": "default_database",
        "log_position": 0,
        "version": 0
    },
    {
        "id": "f776101b-133d-4b2b-af3b-e30fbe7f456a",
        "name": "GBIM_Fayette_sample",
        "configuration_json": {
            "hnsw": {
                "space": "l2",
                "ef_construction": 100,
                "ef_search": 100,
                "max_neighbors": 16,
                "resize_factor": 1.2,
                "sync_threshold": 1000
            },
            "spann": null,
            "embedding_function": {
                "type": "known",
                "name": "default",
                "config": {}
            }
        },
        "schema": {
            "defaults": {
                "string": {
                    "fts_index": {
                        "enabled": false,
                        "config": {}
                    },
                    "string_inverted_index": {
                        "enabled": true,
                        "config": {}
                    }
                },
                "float_list": {
                    "vector_index": {
                        "enabled": false,
                        "config": {
                            "space": "l2",
                            "embedding_function": {
                                "type": "known",
                                "name": "default",
                                "config": {}
                            },
                            "hnsw": {
                                "ef_construction": 100,
                                "max_neighbors": 16,
                                "ef_search": 100,
                                "num_threads": 32,
                                "batch_size": 100,
                                "sync_threshold": 1000,
                                "resize_factor": 1.2
                            }
                        }
                    }
                },
                "sparse_vector": {
                    "sparse_vector_index": {
                        "enabled": false,
                        "config": {
                            "embedding_function": {
                                "type": "unknown"
                            },
                            "bm25": false
                        }
                    }
                },
                "int": {
                    "int_inverted_index": {
                        "enabled": true,
                        "config": {}
                    }
                },
                "float": {
                    "float_inverted_index": {
                        "enabled": true,
                        "config": {}
                    }
                },
                "bool": {
                    "bool_inverted_index": {
                        "enabled": true,
                        "config": {}
                    }
                }
            },
            "keys": {
                "entity_type": {
                    "string": {
                        "fts_index": {
                            "enabled": false,
                            "config": {}
                        },
                        "string_inverted_index": {
                            "enabled": true,
                            "config": {}
                        }
                    }
                },
                "belief_state": {
                    "string": {
                        "fts_index": {
                            "enabled": false,
                            "config": {}
                        },
                        "string_inverted_index": {
                            "enabled": true,
                            "config": {}
                        }
                    }
                },
                "worldview_id": {
                    "string": {
                        "fts_index": {
                            "enabled": false,
                            "config": {}
                        },
                        "string_inverted_index": {
                            "enabled": true,
                            "config": {}
                        }
                    }
                },
                "county": {
                    "string": {
                        "fts_index": {
                            "enabled": false,
                            "config": {}
                        },
                        "string_inverted_index": {
                            "enabled": true,
                            "config": {}
                        }
                    }
                },
                "source_table": {
                    "string": {
                        "fts_index": {
                            "enabled": false,
                            "config": {}
                        },
                        "string_inverted_index": {
                            "enabled": true,
                            "config": {}
                        }
                    }
                },
                "source_id": {
                    "string": {
                        "fts_index": {
                            "enabled": false,
                            "config": {}
                        },
                        "string_inverted_index": {
                            "enabled": true,
                            "config": {}
                        }
                    }
                },
                "#document": {
                    "string": {
                        "fts_index": {
                            "enabled": true,
                            "config": {}
                        },
                        "string_inverted_index": {
                            "enabled": false,
                            "config": {}
                        }
                    }
                },
                "label": {
                    "string": {
                        "fts_index": {
                            "enabled": false,
                            "config": {}
                        },
                        "string_inverted_index": {
                            "enabled": true,
                            "config": {}
                        }
                    }
                },
                "state": {
                    "string": {
                        "fts_index": {
                            "enabled": false,
                            "config": {}
                        },
                        "string_inverted_index": {
                            "enabled": true,
                            "config": {}
                        }
                    }
                },
                "#embedding": {
                    "float_list": {
                        "vector_index": {
                            "enabled": true,
                            "config": {
                                "space": "l2",
                                "embedding_function": {
                                    "type": "known",
                                    "name": "default",
                                    "config": {}
                                },
                                "source_key": "#document",
                                "hnsw": {
                                    "ef_construction": 100,
                                    "max_neighbors": 16,
                                    "ef_search": 100,
                                    "num_threads": 32,
                                    "batch_size": 100,
                                    "sync_threshold": 1000,
                                    "resize_factor": 1.2
                                }
                            }
                        }
                    }
                }
            }
        },
        "metadata": {
            "county": "Fayette",
            "gbim_source": "msjarvisgis + worldview",
            "description": "GBIM Fayette County WV \u2014 home county belief slice",
            "state": "WV"
        },
        "dimension": 384,
        "tenant": "default_tenant",
        "database": "default_database",
        "log_position": 0,
        "version": 0
    },
    {
        "id": "f9152993-c774-47ef-8760-63f7dc50e747",
        "name": "msjarvis_docs",
        "configuration_json": {
            "hnsw": {
                "space": "l2",
                "ef_construction": 100,
                "ef_search": 100,
                "max_neighbors": 16,
                "resize_factor": 1.2,
                "sync_threshold": 1000
            },
            "spann": null,
            "embedding_function": {
                "type": "known",
                "name": "default",
                "config": {}
            }
        },
        "schema": {
            "defaults": {
                "string": {
                    "fts_index": {
                        "enabled": false,
                        "config": {}
                    },
                    "string_inverted_index": {
                        "enabled": true,
                        "config": {}
                    }
                },
                "float_list": {
                    "vector_index": {
                        "enabled": false,
                        "config": {
                            "space": "l2",
                            "embedding_function": {
                                "type": "known",
                                "name": "default",
                                "config": {}
                            },
                            "hnsw": {
                                "ef_construction": 100,
                                "max_neighbors": 16,
                                "ef_search": 100,
                                "num_threads": 32,
                                "batch_size": 100,
                                "sync_threshold": 1000,
                                "resize_factor": 1.2
                            }
                        }
                    }
                },
                "sparse_vector": {
                    "sparse_vector_index": {
                        "enabled": false,
                        "config": {
                            "embedding_function": {
                                "type": "unknown"
                            },
                            "bm25": false
                        }
                    }
                },
                "int": {
                    "int_inverted_index": {
                        "enabled": true,
                        "config": {}
                    }
                },
                "float": {
                    "float_inverted_index": {
                        "enabled": true,
                        "config": {}
                    }
                },
                "bool": {
                    "bool_inverted_index": {
                        "enabled": true,
                        "config": {}
                    }
                }
            },
            "keys": {
                "resource_type": {
                    "string": {
                        "fts_index": {
                            "enabled": false,
                            "config": {}
                        },
                        "string_inverted_index": {
                            "enabled": true,
                            "config": {}
                        }
                    }
                },
                "county": {
                    "string": {
                        "fts_index": {
                            "enabled": false,
                            "config": {}
                        },
                        "string_inverted_index": {
                            "enabled": true,
                            "config": {}
                        }
                    }
                },
                "verified": {
                    "string": {
                        "fts_index": {
                            "enabled": false,
                            "config": {}
                        },
                        "string_inverted_index": {
                            "enabled": true,
                            "config": {}
                        }
                    }
                },
                "path": {
                    "string": {
                        "fts_index": {
                            "enabled": false,
                            "config": {}
                        },
                        "string_inverted_index": {
                            "enabled": true,
                            "config": {}
                        }
                    }
                },
                "topic": {
                    "string": {
                        "fts_index": {
                            "enabled": false,
                            "config": {}
                        },
                        "string_inverted_index": {
                            "enabled": true,
                            "config": {}
                        }
                    }
                },
                "filename": {
                    "string": {
                        "fts_index": {
                            "enabled": false,
                            "config": {}
                        },
                        "string_inverted_index": {
                            "enabled": true,
                            "config": {}
                        }
                    }
                },
                "zip": {
                    "string": {
                        "fts_index": {
                            "enabled": false,
                            "config": {}
                        },
                        "string_inverted_index": {
                            "enabled": true,
                            "config": {}
                        }
                    }
                },
                "local_resource_id": {
                    "string": {
                        "fts_index": {
                            "enabled": false,
                            "config": {}
                        },
                        "string_inverted_index": {
                            "enabled": true,
                            "config": {}
                        }
                    }
                },
                "state": {
                    "string": {
                        "fts_index": {
                            "enabled": false,
                            "config": {}
                        },
                        "string_inverted_index": {
                            "enabled": true,
                            "config": {}
                        }
                    }
                },
                "page": {
                    "int": {
                        "int_inverted_index": {
                            "enabled": true,
                            "config": {}
                        }
                    }
                },
                "#embedding": {
                    "float_list": {
                        "vector_index": {
                            "enabled": true,
                            "config": {
                                "space": "l2",
                                "embedding_function": {
                                    "type": "known",
                                    "name": "default",
                                    "config": {}
                                },
                                "source_key": "#document",
                                "hnsw": {
                                    "ef_construction": 100,
                                    "max_neighbors": 16,
                                    "ef_search": 100,
                                    "num_threads": 32,
                                    "batch_size": 100,
                                    "sync_threshold": 1000,
                                    "resize_factor": 1.2
                                }
                            }
                        }
                    }
                },
                "doc_type": {
                    "string": {
                        "fts_index": {
                            "enabled": false,
                            "config": {}
                        },
                        "string_inverted_index": {
                            "enabled": true,
                            "config": {}
                        }
                    }
                },
                "#document": {
                    "string": {
                        "fts_index": {
                            "enabled": true,
                            "config": {}
                        },
                        "string_inverted_index": {
                            "enabled": false,
                            "config": {}
                        }
                    }
                },
                "type": {
                    "string": {
                        "fts_index": {
                            "enabled": false,
                            "config": {}
                        },
                        "string_inverted_index": {
                            "enabled": true,
                            "config": {}
                        }
                    }
                },
                "name": {
                    "string": {
                        "fts_index": {
                            "enabled": false,
                            "config": {}
                        },
                        "string_inverted_index": {
                            "enabled": true,
                            "config": {}
                        }
                    }
                },
                "category": {
                    "string": {
                        "fts_index": {
                            "enabled": false,
                            "config": {}
                        },
                        "string_inverted_index": {
                            "enabled": true,
                            "config": {}
                        }
                    }
                },
                "programs": {
                    "string": {
                        "fts_index": {
                            "enabled": false,
                            "config": {}
                        },
                        "string_inverted_index": {
                            "enabled": true,
                            "config": {}
                        }
                    }
                },
                "chunk": {
                    "int": {
                        "int_inverted_index": {
                            "enabled": true,
                            "config": {}
                        }
                    }
                },
                "source": {
                    "string": {
                        "fts_index": {
                            "enabled": false,
                            "config": {}
                        },
                        "string_inverted_index": {
                            "enabled": true,
                            "config": {}
                        }
                    }
                },
                "zip_code": {
                    "string": {
                        "fts_index": {
                            "enabled": false,
                            "config": {}
                        },
                        "string_inverted_index": {
                            "enabled": true,
                            "config": {}
                        }
                    }
                },
                "jurisdiction": {
                    "string": {
                        "fts_index": {
                            "enabled": false,
                            "config": {}
                        },
                        "string_inverted_index": {
                            "enabled": true,
                            "config": {}
                        }
                    }
                }
            }
        },
        "metadata": null,
        "dimension": 384,
        "tenant": "default_tenant",
        "database": "default_database",
        "log_position": 0,
        "version": 0
    }
]
{
    "error": "InvalidArgumentError",
    "message": "Collection expecting embedding with dimension of 384, got 2"
}
cakidd@cakidd-Legion-5-16IRX9:~/msjarvis-rebuild-working/msjarvis-rebuild$  

