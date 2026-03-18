(ingest-venv) cakidd@cakidd-Legion-5-16IRX9:~/msjarvis-rebuild-working/msjarvis-rebuild$ echo "=== Container ChromaDB version ==="
docker exec jarvis-chroma pip show chromadb 2>/dev/null | grep -E "^Version|^Name"

echo "=== Venv ChromaDB version ==="
pip show chromadb | grep -E "^Version|^Name"

echo "=== ChromaDB v2 collections ==="
curl -s "http://127.0.0.1:8002/api/v2/tenants/default_tenant/databases/default_database/collections" \
  | python3 -m json.tool 2>/dev/null \
  || curl -s "http://127.0.0.1:8002/api/v2/collections" | python3 -m json.tool 2>/dev/null

echo "=== ZCTA table columns ==="
sudo -u postgres psql -d msjarvisgis -c "
SELECT column_name, data_type
FROM information_schema.columns
WHERE table_name = 'zipcodetabulationarea_census_2020_wma84'
ORDER BY ordinal_position;" | head -25

echo "=== ingest_runner.py integrity ==="
wc -l ~/msjarvis-rebuild-working/ingest/ingest_runner.py
tail -5 ~/msjarvis-rebuild-working/ingest/ingest_runner.py
=== Container ChromaDB version ===
=== Venv ChromaDB version ===
Name: chromadb
Version: 1.5.5
=== ChromaDB v2 collections ===
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
        "id": "44420f2a-9daf-4807-8f03-c6b42aa39ae9",
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
        "metadata": null,
        "dimension": null,
        "tenant": "default_tenant",
        "database": "default_database",
        "log_position": 0,
        "version": 0
    },
    {
        "id": "5749f8b5-ba48-4b4b-a76d-b8f2c9bbd776",
        "name": "spiritual_texts",
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
                            "space": "l2",
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
                "ingestion_date": {
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
            "type": "spiritual_rag",
            "source": "heritage_recovery"
        },
        "dimension": 384,
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
                "page": {
                    "int": {
                        "int_inverted_index": {
                            "enabled": true,
                            "config": {}
                        }
                    }
                }
            }
        },
        "metadata": {
            "domain": "psychological",
            "role": "rag"
        },
        "dimension": 384,
        "tenant": "default_tenant",
        "database": "default_database",
        "log_position": 0,
        "version": 0
    },
    {
        "id": "9e292b1a-a5b3-4db0-a394-15fb8923b75e",
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
        "metadata": null,
        "dimension": null,
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
                "lon": {
                    "float": {
                        "float_inverted_index": {
                            "enabled": true,
                            "config": {}
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
                }
            }
        },
        "metadata": {
            "description": "GBIM entities",
            "worldview_id": "002c2c84-2f18-40b7-8a98-b8d813dd6cc7"
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
                "total_pop": {
                    "int": {
                        "int_inverted_index": {
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
                },
                "cycle": {
                    "int": {
                        "int_inverted_index": {
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
                "index": {
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
                "feature_count": {
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
                "page": {
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
        "metadata": null,
        "dimension": 384,
        "tenant": "default_tenant",
        "database": "default_database",
        "log_position": 0,
        "version": 0
    }
]
=== ZCTA table columns ===
Password for user postgres: 
 column_name |  data_type   
-------------+--------------
 geodbid     | integer
 geom        | USER-DEFINED
 label       | text
 sourcetable | text
 country     | text
(5 rows)

=== ingest_runner.py integrity ===
268 /home/cakidd/msjarvis-rebuild-working/ingest/ingest_runner.py
        files = sorted(INCOMING.glob("*.*"))
        if not files:
            print("No files in incoming/")
        for f in files:
            process_file(f)
(ingest-venv) cakidd@cakidd-Legion-5-16IRX9:~/msjarvis-rebuild-working/msjarvis-rebuild$ 

