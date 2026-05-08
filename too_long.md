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
        "cat": {
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
        "ref": {
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
      "created": "ms-jarvis"
    },
    "dimension": 384,
    "tenant": "default_tenant",
    "database": "default_database",
    "log_position": 0,
    "version": 0
  },
  {
    "id": "636dc443-1e42-43f6-aa85-78c8a4d7e8c5",
    "name": "geospatialfeatures",
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
        "feature_type": {
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
        "lat": {
          "float": {
            "float_inverted_index": {
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
    "id": "66856dfb-18f6-4dc8-9182-3d4f27ba800b",
    "name": "spiritual_texts",
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
        "wv_tagged": {
          "bool": {
            "bool_inverted_index": {
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
          },
          "int": {
            "int_inverted_index": {
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
      "hnsw:space": "cosine",
      "description": "Mother Carrie Protocol — 72 religious traditions corpus"
    },
    "dimension": 384,
    "tenant": "default_tenant",
    "database": "default_database",
    "log_position": 0,
    "version": 0
  },
  {
    "id": "6727fb3e-078f-49d5-9df8-e2c82ecf8cf2",
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
        "timestamp": {
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
        "role": {
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
      "hnsw:space": "cosine"
    },
    "dimension": 384,
    "tenant": "default_tenant",
    "database": "default_database",
    "log_position": 0,
    "version": 0
  },
  {
    "id": "6a39f36c-5da7-45b7-82f2-b2684415ebcd",
    "name": "appalachian_english_corpus",
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
        "published": {
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
        "subcategory": {
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
        "tier": {
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
    "id": "6acb5634-7ae4-41ae-b487-09da0be84f48",
    "name": "governance_rag",
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
        "ingested": {
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
        "chunk": {
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
      "hnsw:space": "cosine"
    },
    "dimension": 384,
    "tenant": "default_tenant",
    "database": "default_database",
    "log_position": 0,
    "version": 0
  },
  {
    "id": "7b85b2be-c1ae-4154-931a-af6a91119b7e",
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
          },
          "bool": {
            "bool_inverted_index": {
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
      "created": "ms-jarvis"
    },
    "dimension": 384,
    "tenant": "default_tenant",
    "database": "default_database",
    "log_position": 0,
    "version": 0
  },
  {
    "id": "84bfcc58-4c4a-43db-85d8-0eff476ae40a",
    "name": "fayette_county_resources_2026",
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
        "gbim_entity_id": {
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
        "address_count": {
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
        "year": {
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
        "contributor_role": {
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
        "geo_anchor_count": {
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
        "contributor": {
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
        "ingest_date": {
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
        "gbim_lon": {
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
        "doc_id": {
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
        "county_fips": {
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
        "gbim_lat": {
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
        "extraction_method": {
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
      "hnsw:space": "cosine"
    },
    "dimension": 384,
    "tenant": "default_tenant",
    "database": "default_database",
    "log_position": 0,
    "version": 0
  },
  {
    "id": "870f3910-c699-4d47-b616-e51f0fccac85",
    "name": "jarvis",
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
        }
      }
    },
    "metadata": {
      "wv_tagged": true,
      "description": "Community health data — WV DHHR, county health depts",
      "status": "created_empty_2026-03-24"
    },
    "dimension": 384,
    "tenant": "default_tenant",
    "database": "default_database",
    "log_position": 0,
    "version": 0
  },
  {
    "id": "9358928c-d503-47e5-b24d-78159edd53ab",
    "name": "appalachian_cultural_intelligence",
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
        "query": {
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
        "subcategory": {
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
        "tier": {
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
        "published": {
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
        "lat": {
          "float": {
            "float_inverted_index": {
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
        "turn_number": {
          "int": {
            "int_inverted_index": {
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
        }
      }
    },
    "metadata": {
      "gbim_axes": "what,where,when,why,for_whom",
      "privacy_tier": "public",
      "description": "Public conversation GBIM — anonymized community patterns",
      "access": "dao_governed"
    },
    "dimension": 384,
    "tenant": "default_tenant",
    "database": "default_database",
    "log_position": 0,
    "version": 0
  },
  {
    "id": "c0111c70-db44-4e0a-8a97-f6a7a5c59ec9",
    "name": "spiritual_wisdom",
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
    "id": "c303b088-d3c3-4569-9b7e-5053514c2b32",
    "name": "wv_resources",
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
        "cat": {
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
      "created": "ms-jarvis"
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
      "description": "Community meeting minutes — Fayette County and regional",
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
    "id": "ddb233d7-1642-4486-bde9-4cd4d96c3f43",
    "name": "commons_rag",
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
        "chunk": {
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
      "description": "Legal and regulatory documents — WV code and federal",
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
        "cycle": {
          "int": {
            "int_inverted_index": {
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
        "total_pop": {
          "int": {
            "int_inverted_index": {
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
        "chain": {
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
        "enriched": {
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
        "contract_name": {
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
        "phase": {
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
    "metadata": {
      "state": "WV",
      "county": "Fayette",
      "description": "GBIM Fayette County WV — home county belief slice",
      "gbim_source": "msjarvisgis + worldview"
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
        "page": {
          "int": {
            "int_inverted_index": {
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
        "pulse": {
          "int": {
            "int_inverted_index": {
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
        "chunk": {
          "int": {
            "int_inverted_index": {
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
    "id": "ff2f7717-3e21-4e6b-8244-e8da1aa2bb36",
    "name": "operations_history",
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
        "containers": {
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
        "result": {
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
        "logged_at": {
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
      "description": "VERIFYANDTEST.sh and preflight_gate.sh run logs"
    },
    "dimension": 384,
    "tenant": "default_tenant",
    "database": "default_database",
    "log_position": 0,
    "version": 0
  }
]
msjarvis-smoke	02715c7c-7676-4cc1-8e9e-9c345bb332fe
geospatial_features	02bb9e40-c68e-49e5-95f9-ec11186b4b7b
fifth_dgm_subconscious	0338d961-4f32-43ce-9afa-25ecb4ba0185
autonomous_learning	03627c99-c66a-4dbc-b42d-4e2052ff51ae
zcta_centroids	05c59b1f-d0c3-4cbd-bd60-ddf151307315
safety_rules	062ab0ff-f06a-4beb-ba61-81461f4079c8
economic_rag	0c88a778-02bf-475f-ba80-64b9f4467e84
psychological_rag	0ffa3033-630f-4abf-bf16-f6fd5e53dcb9
wv_facilities	13af61a6-2a62-47da-a14d-aa771bd4c1ef
jarvis_knowledge	15a7496c-dce4-4f57-a86f-2f6b97665d72
address_points	17f69cca-d74f-4f93-bb89-774dc339eeab
conversation_gbim_private	27f9d49b-c2a0-4c5e-91f5-8441105fedc9
policy_rag	28014347-d398-4f92-b0ca-81a1de7fc4eb
ms_jarvis_memory	2a8fd74d-5433-4ec9-8d2f-7d56d0843f4b
grants_rag	2bc09932-0ec4-4883-9abd-bf18f3769eaa
GBIM_sample_rows	3b4317d9-19e4-495c-b91e-6e02686d67f0
research_history	3f9c0200-ba98-4a38-8320-7abd2adf1b12
au02_threat_seeds	415fbdfe-b7e2-44ee-aba0-619566050bfc
gbim_entities	48a97656-e254-4e44-9294-bbfffd87bf07
pia_records	4a4ea5e5-cb8a-46dd-97c4-c8f23ce25958
ms_jarvis_identity	4b1af913-3248-425c-8af1-8ee08df8e226
gis_wv_benefits	524507db-559b-44e5-80a1-b25896a3c229
news_rag	5627f6ba-115d-4d7b-898d-a2436e6513ac
gbim_beliefs_v2	571eebfa-b122-4e91-af3a-a7aa9a188ba1
spiritual_knowledge	5a103162-2f32-4da5-9456-e0cffbe3d5f9
geospatialfeatures	636dc443-1e42-43f6-aa85-78c8a4d7e8c5
spiritual_texts	66856dfb-18f6-4dc8-9182-3d4f27ba800b
conversation_history	6727fb3e-078f-49d5-9df8-e2c82ecf8cf2
appalachian_english_corpus	6a39f36c-5da7-45b7-82f2-b2684415ebcd
governance_rag	6acb5634-7ae4-41ae-b487-09da0be84f48
local_resources	7b85b2be-c1ae-4154-931a-af6a91119b7e
fayette_county_resources_2026	84bfcc58-4c4a-43db-85d8-0eff476ae40a
jarvis	870f3910-c699-4d47-b616-e51f0fccac85
health_rag	872f538b-a930-4427-b309-19c1d081537d
appalachian_cultural_intelligence	9358928c-d503-47e5-b24d-78159edd53ab
GBIM_sample	ac277ccb-e1ec-45b6-b8b4-e40666f49f95
conversation_gbim_public	b2a59ffc-a3a5-4c06-90c9-8954b33992f1
spiritual_wisdom	c0111c70-db44-4e0a-8a97-f6a7a5c59ec9
wv_resources	c303b088-d3c3-4569-9b7e-5053514c2b32
meeting_minutes	cb0e2432-3a8c-44c0-8839-d94beebff42f
commons_rag	ddb233d7-1642-4486-bde9-4cd4d96c3f43
legal_rag	e0caffcd-136e-4ac2-addc-f4c9b1814ac2
gbim_worldview_entities	e666b46d-e04f-4fd6-a0ce-067a06f491b6
autonomous_learner	e7e83578-973e-474e-a6d4-ea91d5d5289d
contracts	f6d0a9cd-4c76-4b7d-be6a-5249db9ff7ab
GBIM_Fayette_sample	f776101b-133d-4b2b-af3b-e30fbe7f456a
msjarvis_docs	f9152993-c774-47ef-8760-63f7dc50e747
operations_history	ff2f7717-3e21-4e6b-8244-e8da1aa2bb36
===== msjarvis-smoke =====
{
  "error": "InvalidArgumentError",
  "message": "Collection ID is not a valid UUIDv4"
}
===== geospatial_features =====
{
  "error": "InvalidArgumentError",
  "message": "Collection ID is not a valid UUIDv4"
}
===== fifth_dgm_subconscious =====
{
  "error": "InvalidArgumentError",
  "message": "Collection ID is not a valid UUIDv4"
}
===== autonomous_learning =====
{
  "error": "InvalidArgumentError",
  "message": "Collection ID is not a valid UUIDv4"
}
===== zcta_centroids =====
{
  "error": "InvalidArgumentError",
  "message": "Collection ID is not a valid UUIDv4"
}
===== safety_rules =====
{
  "error": "InvalidArgumentError",
  "message": "Collection ID is not a valid UUIDv4"
}
===== economic_rag =====
{
  "error": "InvalidArgumentError",
  "message": "Collection ID is not a valid UUIDv4"
}
===== psychological_rag =====
{
  "error": "InvalidArgumentError",
  "message": "Collection ID is not a valid UUIDv4"
}
===== wv_facilities =====
{
  "error": "InvalidArgumentError",
  "message": "Collection ID is not a valid UUIDv4"
}
===== jarvis_knowledge =====
{
  "error": "InvalidArgumentError",
  "message": "Collection ID is not a valid UUIDv4"
}
===== address_points =====
{
  "error": "InvalidArgumentError",
  "message": "Collection ID is not a valid UUIDv4"
}
===== conversation_gbim_private =====
{
  "error": "InvalidArgumentError",
  "message": "Collection ID is not a valid UUIDv4"
}
===== policy_rag =====
{
  "error": "InvalidArgumentError",
  "message": "Collection ID is not a valid UUIDv4"
}
===== ms_jarvis_memory =====
{
  "error": "InvalidArgumentError",
  "message": "Collection ID is not a valid UUIDv4"
}
===== grants_rag =====
{
  "error": "InvalidArgumentError",
  "message": "Collection ID is not a valid UUIDv4"
}
===== GBIM_sample_rows =====
{
  "error": "InvalidArgumentError",
  "message": "Collection ID is not a valid UUIDv4"
}
===== research_history =====
{
  "error": "InvalidArgumentError",
  "message": "Collection ID is not a valid UUIDv4"
}
===== au02_threat_seeds =====
{
  "error": "InvalidArgumentError",
  "message": "Collection ID is not a valid UUIDv4"
}
===== gbim_entities =====
{
  "error": "InvalidArgumentError",
  "message": "Collection ID is not a valid UUIDv4"
}
===== pia_records =====
{
  "error": "InvalidArgumentError",
  "message": "Collection ID is not a valid UUIDv4"
}
===== ms_jarvis_identity =====
{
  "error": "InvalidArgumentError",
  "message": "Collection ID is not a valid UUIDv4"
}
===== gis_wv_benefits =====
{
  "error": "InvalidArgumentError",
  "message": "Collection ID is not a valid UUIDv4"
}
===== news_rag =====
{
  "error": "InvalidArgumentError",
  "message": "Collection ID is not a valid UUIDv4"
}
===== gbim_beliefs_v2 =====
{
  "error": "InvalidArgumentError",
  "message": "Collection ID is not a valid UUIDv4"
}
===== spiritual_knowledge =====
{
  "error": "InvalidArgumentError",
  "message": "Collection ID is not a valid UUIDv4"
}
===== geospatialfeatures =====
{
  "error": "InvalidArgumentError",
  "message": "Collection ID is not a valid UUIDv4"
}
===== spiritual_texts =====
{
  "error": "InvalidArgumentError",
  "message": "Collection ID is not a valid UUIDv4"
}
===== conversation_history =====
{
  "error": "InvalidArgumentError",
  "message": "Collection ID is not a valid UUIDv4"
}
===== appalachian_english_corpus =====
{
  "error": "InvalidArgumentError",
  "message": "Collection ID is not a valid UUIDv4"
}
===== governance_rag =====
{
  "error": "InvalidArgumentError",
  "message": "Collection ID is not a valid UUIDv4"
}
===== local_resources =====
{
  "error": "InvalidArgumentError",
  "message": "Collection ID is not a valid UUIDv4"
}
===== fayette_county_resources_2026 =====
{
  "error": "InvalidArgumentError",
  "message": "Collection ID is not a valid UUIDv4"
}
===== jarvis =====
{
  "error": "InvalidArgumentError",
  "message": "Collection ID is not a valid UUIDv4"
}
===== health_rag =====
{
  "error": "InvalidArgumentError",
  "message": "Collection ID is not a valid UUIDv4"
}
===== appalachian_cultural_intelligence =====
{
  "error": "InvalidArgumentError",
  "message": "Collection ID is not a valid UUIDv4"
}
===== GBIM_sample =====
{
  "error": "InvalidArgumentError",
  "message": "Collection ID is not a valid UUIDv4"
}
===== conversation_gbim_public =====
{
  "error": "InvalidArgumentError",
  "message": "Collection ID is not a valid UUIDv4"
}
===== spiritual_wisdom =====
{
  "error": "InvalidArgumentError",
  "message": "Collection ID is not a valid UUIDv4"
}
===== wv_resources =====
{
  "error": "InvalidArgumentError",
  "message": "Collection ID is not a valid UUIDv4"
}
===== meeting_minutes =====
{
  "error": "InvalidArgumentError",
  "message": "Collection ID is not a valid UUIDv4"
}
===== commons_rag =====
{
  "error": "InvalidArgumentError",
  "message": "Collection ID is not a valid UUIDv4"
}
===== legal_rag =====
{
  "error": "InvalidArgumentError",
  "message": "Collection ID is not a valid UUIDv4"
}
===== gbim_worldview_entities =====
{
  "error": "InvalidArgumentError",
  "message": "Collection ID is not a valid UUIDv4"
}
===== autonomous_learner =====
{
  "error": "InvalidArgumentError",
  "message": "Collection ID is not a valid UUIDv4"
}
===== contracts =====
{
  "error": "InvalidArgumentError",
  "message": "Collection ID is not a valid UUIDv4"
}
===== GBIM_Fayette_sample =====
{
  "error": "InvalidArgumentError",
  "message": "Collection ID is not a valid UUIDv4"
}
===== msjarvis_docs =====
{
  "error": "InvalidArgumentError",
  "message": "Collection ID is not a valid UUIDv4"
}
===== operations_history =====
{
  "error": "InvalidArgumentError",
  "message": "Collection ID is not a valid UUIDv4"
}
===== gbim_worldview_entities =====
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
    "description": "GBIM entities",
    "worldview_id": "002c2c84-2f18-40b7-8a98-b8d813dd6cc7"
  },
  "dimension": 384,
  "tenant": "default_tenant",
  "database": "default_database",
  "log_position": 0,
  "version": 0
}
{
  "error": "InvalidArgumentError",
  "message": "Collection ID is not a valid UUIDv4"
}
===== eq1_worldview.gbim_entities =====
{
  "error": "NotFoundError",
  "message": "Collection [eq1_worldview.gbim_entities] does not exist"
}
{
  "error": "InvalidArgumentError",
  "message": "Collection ID is not a valid UUIDv4"
}
===== address_points =====
{
  "id": "17f69cca-d74f-4f93-bb89-774dc339eeab",
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
      "backfill": {
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
      "evidence": {
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
      "where": {
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
      "who": {
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
      "why": {
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
      "how": {
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
      "for_whom": {
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
      "lon": {
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
      "what": {
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
      "when": {
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
      "authority": {
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
{
  "error": "InvalidArgumentError",
  "message": "Collection ID is not a valid UUIDv4"
}
===== spiritual_texts =====
{
  "id": "66856dfb-18f6-4dc8-9182-3d4f27ba800b",
  "name": "spiritual_texts",
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
        },
        "int": {
          "int_inverted_index": {
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
      "chunk": {
        "int": {
          "int_inverted_index": {
            "enabled": true,
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
      }
    }
  },
  "metadata": {
    "hnsw:space": "cosine",
    "description": "Mother Carrie Protocol — 72 religious traditions corpus"
  },
  "dimension": 384,
  "tenant": "default_tenant",
  "database": "default_database",
  "log_position": 0,
  "version": 0
}
{
  "error": "InvalidArgumentError",
  "message": "Collection ID is not a valid UUIDv4"
}
===== autonomous_learner =====
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
      "total_pop": {
        "int": {
          "int_inverted_index": {
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
      "index": {
        "int": {
          "int_inverted_index": {
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
      "chunk_idx": {
        "int": {
          "int_inverted_index": {
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
      "cycle": {
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
{
  "error": "InvalidArgumentError",
  "message": "Collection ID is not a valid UUIDv4"
}
===== autonomous_learning =====
{
  "id": "03627c99-c66a-4dbc-b42d-4e2052ff51ae",
  "name": "autonomous_learning",
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
      "content_hash": {
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
      "backfill": {
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
      "what": {
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
      "compressed": {
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
        "bool": {
          "bool_inverted_index": {
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
      "fallback": {
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
        "bool": {
          "bool_inverted_index": {
            "enabled": true,
            "config": {}
          }
        }
      },
      "why": {
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
      "for_whom": {
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
      "evidence": {
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
      "gbim_coordinate": {
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
      "when": {
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
      "cycle_number": {
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
        "int": {
          "int_inverted_index": {
            "enabled": true,
            "config": {}
          }
        }
      },
      "where": {
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
      "who": {
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
      "authority": {
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
    "description": "Autonomously acquired knowledge"
  },
  "dimension": 384,
  "tenant": "default_tenant",
  "database": "default_database",
  "log_position": 0,
  "version": 0
}
{
  "error": "InvalidArgumentError",
  "message": "Collection ID is not a valid UUIDv4"
}
===== fayettecounty_resources_2026 =====
{
  "error": "NotFoundError",
  "message": "Collection [fayettecounty_resources_2026] does not exist"
}
{
  "error": "InvalidArgumentError",
  "message": "Collection ID is not a valid UUIDv4"
}
{
  "models": [
    {
      "name": "egeria:latest",
      "model": "egeria:latest",
      "modified_at": "2026-05-04T15:42:11.519728366Z",
      "size": 4372824887,
      "digest": "06f147ff9e59378e9a68605458862b083473450bc2ee371da5f898d775650379",
      "details": {
        "parent_model": "",
        "format": "gguf",
        "family": "llama",
        "families": [
          "llama"
        ],
        "parameter_size": "7.2B",
        "quantization_level": "Q4_K_M"
      }
    },
    {
      "name": "phi3.5:latest",
      "model": "phi3.5:latest",
      "modified_at": "2026-04-12T20:35:47.354166236Z",
      "size": 2176178843,
      "digest": "61819fb370a3c1a9be6694869331e5f85f867a079e9271d66cb223acb81d04ba",
      "details": {
        "parent_model": "",
        "format": "gguf",
        "family": "phi3",
        "families": [
          "phi3"
        ],
        "parameter_size": "3.8B",
        "quantization_level": "Q4_0"
      }
    },
    {
      "name": "orca-mini:3b",
      "model": "orca-mini:3b",
      "modified_at": "2026-04-12T20:17:38.332112401Z",
      "size": 1979947443,
      "digest": "2dbd9f439647093cf773c325b0b3081a11f1b1426d61dee8b946f8f6555a1755",
      "details": {
        "parent_model": "",
        "format": "gguf",
        "family": "llama",
        "families": null,
        "parameter_size": "3B",
        "quantization_level": "Q4_0"
      }
    },
    {
      "name": "orca-mini:latest",
      "model": "orca-mini:latest",
      "modified_at": "2026-04-12T20:16:04.090263215Z",
      "size": 1979947443,
      "digest": "2dbd9f439647093cf773c325b0b3081a11f1b1426d61dee8b946f8f6555a1755",
      "details": {
        "parent_model": "",
        "format": "gguf",
        "family": "llama",
        "families": null,
        "parameter_size": "3B",
        "quantization_level": "Q4_0"
      }
    },
    {
      "name": "all-minilm:latest",
      "model": "all-minilm:latest",
      "modified_at": "2026-04-12T03:10:02.270756106Z",
      "size": 45960996,
      "digest": "1b226e2802dbb772b5fc32a58f103ca1804ef7501331012de126ab22f67475ef",
      "details": {
        "parent_model": "",
        "format": "gguf",
        "family": "bert",
        "families": [
          "bert"
        ],
        "parameter_size": "23M",
        "quantization_level": "F16"
      }
    },
    {
      "name": "nomic-embed-text:latest",
      "model": "nomic-embed-text:latest",
      "modified_at": "2026-04-11T04:15:03.46833539Z",
      "size": 274302450,
      "digest": "0a109f422b47e3a30ba2b10eca18548e944e8a23073ee3f3e947efcf3c45e59f",
      "details": {
        "parent_model": "",
        "format": "gguf",
        "family": "nomic-bert",
        "families": [
          "nomic-bert"
        ],
        "parameter_size": "137M",
        "quantization_level": "F16"
      }
    },
    {
      "name": "starcoder2:latest",
      "model": "starcoder2:latest",
      "modified_at": "2026-02-03T04:14:06.721592206Z",
      "size": 1709901728,
      "digest": "9f4ae0aff61ee24fe4b7d9714c9382b5172551fa8e95aa064452ec2e62610835",
      "details": {
        "parent_model": "",
        "format": "gguf",
        "family": "starcoder2",
        "families": [
          "starcoder2"
        ],
        "parameter_size": "3B",
        "quantization_level": "Q4_0"
      }
    },
    {
      "name": "medllama2:latest",
      "model": "medllama2:latest",
      "modified_at": "2026-02-03T04:08:58.668380862Z",
      "size": 3825807497,
      "digest": "a53737ec0c72e31e16968f232cad6a13d79b979d7c0cb13404dcd4405214c8f2",
      "details": {
        "parent_model": "",
        "format": "gguf",
        "family": "llama",
        "families": null,
        "parameter_size": "7B",
        "quantization_level": "Q4_0"
      }
    },
    {
      "name": "sqlcoder:latest",
      "model": "sqlcoder:latest",
      "modified_at": "2026-02-03T04:01:43.261978875Z",
      "size": 4108916695,
      "digest": "77ac143483877b043ed3da36ce3e00a8f707645a2f1b769e9827313e5f8f0015",
      "details": {
        "parent_model": "",
        "format": "gguf",
        "family": "llama",
        "families": null,
        "parameter_size": "7B",
        "quantization_level": "Q4_0"
      }
    },
    {
      "name": "dolphin-phi:latest",
      "model": "dolphin-phi:latest",
      "modified_at": "2026-02-03T03:52:52.031862946Z",
      "size": 1602473850,
      "digest": "c5761fc772409945787240af89a5cce01dd39dc52f1b7b80d080a1163e8dbe10",
      "details": {
        "parent_model": "",
        "format": "gguf",
        "family": "phi2",
        "families": [
          "phi2"
        ],
        "parameter_size": "3B",
        "quantization_level": "Q4_0"
      }
    },
    {
      "name": "llama2:latest",
      "model": "llama2:latest",
      "modified_at": "2026-02-03T02:49:20.676271273Z",
      "size": 3826793677,
      "digest": "78e26419b4469263f75331927a00a0284ef6544c1975b826b15abdaef17bb962",
      "details": {
        "parent_model": "",
        "format": "gguf",
        "family": "llama",
        "families": [
          "llama"
        ],
        "parameter_size": "7B",
        "quantization_level": "Q4_0"
      }
    },
    {
      "name": "deepseek-coder:latest",
      "model": "deepseek-coder:latest",
      "modified_at": "2026-02-03T02:40:12.60584115Z",
      "size": 776080839,
      "digest": "3ddd2d3fc8d2b5fe039d18f859271132fd9c7960ef0be1864984442dc2a915d3",
      "details": {
        "parent_model": "",
        "format": "gguf",
        "family": "llama",
        "families": [
          "llama"
        ],
        "parameter_size": "1B",
        "quantization_level": "Q4_0"
      }
    },
    {
      "name": "codellama:latest",
      "model": "codellama:latest",
      "modified_at": "2026-02-03T02:38:13.923973354Z",
      "size": 3825910662,
      "digest": "8fdf8f752f6e80de33e82f381aba784c025982752cd1ae9377add66449d2225f",
      "details": {
        "parent_model": "",
        "format": "gguf",
        "family": "llama",
        "families": null,
        "parameter_size": "7B",
        "quantization_level": "Q4_0"
      }
    },
    {
      "name": "qwen2:latest",
      "model": "qwen2:latest",
      "modified_at": "2026-02-03T02:27:01.016809737Z",
      "size": 4431401491,
      "digest": "dd314f039b9d54d5553002c906ce50c9fe7242f73f0680abd04f01c8ecbd2755",
      "details": {
        "parent_model": "",
        "format": "gguf",
        "family": "qwen2",
        "families": [
          "qwen2"
        ],
        "parameter_size": "7.6B",
        "quantization_level": "Q4_0"
      }
    },
    {
      "name": "llama3.1:latest",
      "model": "llama3.1:latest",
      "modified_at": "2026-02-03T02:27:00.360787079Z",
      "size": 4920753328,
      "digest": "46e0c10c039e019119339687c3c1757cc81b9da49709a3b3924863ba87ca666e",
      "details": {
        "parent_model": "",
        "format": "gguf",
        "family": "llama",
        "families": [
          "llama"
        ],
        "parameter_size": "8.0B",
        "quantization_level": "Q4_K_M"
      }
    },
    {
      "name": "mistral:latest",
      "model": "mistral:latest",
      "modified_at": "2026-02-03T02:14:36.779364334Z",
      "size": 4372824384,
      "digest": "6577803aa9a036369e481d648a2baebb381ebc6e897f2bb9a766a2aa7bfbc1cf",
      "details": {
        "parent_model": "",
        "format": "gguf",
        "family": "llama",
        "families": [
          "llama"
        ],
        "parameter_size": "7.2B",
        "quantization_level": "Q4_K_M"
      }
    },
    {
      "name": "starling-lm:latest",
      "model": "starling-lm:latest",
      "modified_at": "2026-01-22T15:06:56.13615103Z",
      "size": 4108940286,
      "digest": "39153f619be614bf1b8b91cf31afe53ec107d70b6b7bb4118aa52bccc107ca7e",
      "details": {
        "parent_model": "",
        "format": "gguf",
        "family": "llama",
        "families": [
          "llama"
        ],
        "parameter_size": "7B",
        "quantization_level": "Q4_0"
      }
    },
    {
      "name": "openchat:latest",
      "model": "openchat:latest",
      "modified_at": "2026-01-22T14:56:57.425457222Z",
      "size": 4109876386,
      "digest": "537a4e03b649d93bf57381199a85f412bfc35912e46db197407740230968e71f",
      "details": {
        "parent_model": "",
        "format": "gguf",
        "family": "llama",
        "families": [
          "llama"
        ],
        "parameter_size": "7B",
        "quantization_level": "Q4_0"
      }
    },
    {
      "name": "neural-chat:latest",
      "model": "neural-chat:latest",
      "modified_at": "2026-01-22T14:50:33.742259474Z",
      "size": 4109853239,
      "digest": "89fa737d3b85d5e037c2b699b2a735a365cf9e57fd01c62b3378ec1e95694694",
      "details": {
        "parent_model": "",
        "format": "gguf",
        "family": "llama",
        "families": [
          "llama"
        ],
        "parameter_size": "7B",
        "quantization_level": "Q4_0"
      }
    },
    {
      "name": "zephyr:latest",
      "model": "zephyr:latest",
      "modified_at": "2026-01-22T14:43:59.351422262Z",
      "size": 4109854934,
      "digest": "bbe38b81adec6be8ff951d148864ed15a368aa2e8534a5092d444f184a56e354",
      "details": {
        "parent_model": "",
        "format": "gguf",
        "family": "llama",
        "families": [
          "llama"
        ],
        "parameter_size": "7B",
        "quantization_level": "Q4_0"
      }
    },
    {
      "name": "vicuna:latest",
      "model": "vicuna:latest",
      "modified_at": "2026-01-22T14:28:31.831177247Z",
      "size": 3825807726,
      "digest": "370739dc897bba0188d390bb7659e48d926cacc320875136d0115228023b1590",
      "details": {
        "parent_model": "",
        "format": "gguf",
        "family": "llama",
        "families": null,
        "parameter_size": "7B",
        "quantization_level": "Q4_0"
      }
    },
    {
      "name": "qwen2:7b",
      "model": "qwen2:7b",
      "modified_at": "2026-01-22T13:57:15.682886171Z",
      "size": 4431401491,
      "digest": "dd314f039b9d54d5553002c906ce50c9fe7242f73f0680abd04f01c8ecbd2755",
      "details": {
        "parent_model": "",
        "format": "gguf",
        "family": "qwen2",
        "families": [
          "qwen2"
        ],
        "parameter_size": "7.6B",
        "quantization_level": "Q4_0"
      }
    },
    {
      "name": "gemma:2b",
      "model": "gemma:2b",
      "modified_at": "2026-01-22T13:41:23.721948307Z",
      "size": 1678456656,
      "digest": "b50d6c999e592ae4f79acae23b4feaefbdfceaa7cd366df2610e3072c052a160",
      "details": {
        "parent_model": "",
        "format": "gguf",
        "family": "gemma",
        "families": [
          "gemma"
        ],
        "parameter_size": "3B",
        "quantization_level": "Q4_0"
      }
    },
    {
      "name": "tinyllama:latest",
      "model": "tinyllama:latest",
      "modified_at": "2026-01-22T13:35:10.37070479Z",
      "size": 637700138,
      "digest": "2644915ede352ea7bdfaff0bfac0be74c719d5d5202acb63a6fb095b52f394a4",
      "details": {
        "parent_model": "",
        "format": "gguf",
        "family": "llama",
        "families": [
          "llama"
        ],
        "parameter_size": "1B",
        "quantization_level": "Q4_0"
      }
    },
    {
      "name": "phi3:mini",
      "model": "phi3:mini",
      "modified_at": "2026-01-22T13:32:33.451580236Z",
      "size": 2176178913,
      "digest": "4f222292793889a9a40a020799cfd28d53f3e01af25d48e06c5e708610fc47e9",
      "details": {
        "parent_model": "",
        "format": "gguf",
        "family": "phi3",
        "families": [
          "phi3"
        ],
        "parameter_size": "3.8B",
        "quantization_level": "Q4_0"
      }
    },
    {
      "name": "minicpm-v:latest",
      "model": "minicpm-v:latest",
      "modified_at": "2026-01-22T13:04:09.160951814Z",
      "size": 5473838466,
      "digest": "c92bfad0120556eda311984f1ac2f0d0a589b8d68c4053c13486b526276aa205",
      "details": {
        "parent_model": "",
        "format": "gguf",
        "family": "qwen2",
        "families": [
          "qwen2",
          "clip"
        ],
        "parameter_size": "7.6B",
        "quantization_level": "Q4_0"
      }
    },
    {
      "name": "llama3:latest",
      "model": "llama3:latest",
      "modified_at": "2026-01-22T03:28:01.402621937Z",
      "size": 4661224676,
      "digest": "365c0bd3c000a25d28ddbf732fe1c6add414de7275464c4e4d1c3b5fcb5d8ad1",
      "details": {
        "parent_model": "",
        "format": "gguf",
        "family": "llama",
        "families": [
          "llama"
        ],
        "parameter_size": "8.0B",
        "quantization_level": "Q4_0"
      }
    },
    {
      "name": "llava:latest",
      "model": "llava:latest",
      "modified_at": "2026-01-22T03:27:39.796602943Z",
      "size": 4733363377,
      "digest": "8dd30f6b0cb19f555f2c7a7ebda861449ea2cc76bf1f44e262931f45fc81d081",
      "details": {
        "parent_model": "",
        "format": "gguf",
        "family": "llama",
        "families": [
          "llama",
          "clip"
        ],
        "parameter_size": "7B",
        "quantization_level": "Q4_0"
      }
    },
    {
      "name": "stablelm-zephyr:latest",
      "model": "stablelm-zephyr:latest",
      "modified_at": "2026-01-22T03:25:13.525712124Z",
      "size": 1608579394,
      "digest": "0a108dbd846e2b0ee264a71a28e50ac18e7f1601eeb2d677217602d32644bf24",
      "details": {
        "parent_model": "",
        "format": "gguf",
        "family": "stablelm",
        "families": [
          "stablelm"
        ],
        "parameter_size": "3B",
        "quantization_level": "Q4_0"
      }
    },
    {
      "name": "qwen2.5:1.5b",
      "model": "qwen2.5:1.5b",
      "modified_at": "2026-01-22T03:00:19.182334501Z",
      "size": 986061892,
      "digest": "65ec06548149b04c096a120e4a6da9d4017ea809c91734ea5631e89f96ddc57b",
      "details": {
        "parent_model": "",
        "format": "gguf",
        "family": "qwen2",
        "families": [
          "qwen2"
        ],
        "parameter_size": "1.5B",
        "quantization_level": "Q4_K_M"
      }
    }
  ]
}
{
  "license": "                                 Apache License\n                           Version 2.0, January 2004\n                        http://www.apache.org/licenses/\n\n   TERMS AND CONDITIONS FOR USE, REPRODUCTION, AND DISTRIBUTION\n\n   1. Definitions.\n\n      \"License\" shall mean the terms and conditions for use, reproduction,\n      and distribution as defined by Sections 1 through 9 of this document.\n\n      \"Licensor\" shall mean the copyright owner or entity authorized by\n      the copyright owner that is granting the License.\n\n      \"Legal Entity\" shall mean the union of the acting entity and all\n      other entities that control, are controlled by, or are under common\n      control with that entity. For the purposes of this definition,\n      \"control\" means (i) the power, direct or indirect, to cause the\n      direction or management of such entity, whether by contract or\n      otherwise, or (ii) ownership of fifty percent (50%) or more of the\n      outstanding shares, or (iii) beneficial ownership of such entity.\n\n      \"You\" (or \"Your\") shall mean an individual or Legal Entity\n      exercising permissions granted by this License.\n\n      \"Source\" form shall mean the preferred form for making modifications,\n      including but not limited to software source code, documentation\n      source, and configuration files.\n\n      \"Object\" form shall mean any form resulting from mechanical\n      transformation or translation of a Source form, including but\n      not limited to compiled object code, generated documentation,\n      and conversions to other media types.\n\n      \"Work\" shall mean the work of authorship, whether in Source or\n      Object form, made available under the License, as indicated by a\n      copyright notice that is included in or attached to the work\n      (an example is provided in the Appendix below).\n\n      \"Derivative Works\" shall mean any work, whether in Source or Object\n      form, that is based on (or derived from) the Work and for which the\n      editorial revisions, annotations, elaborations, or other modifications\n      represent, as a whole, an original work of authorship. For the purposes\n      of this License, Derivative Works shall not include works that remain\n      separable from, or merely link (or bind by name) to the interfaces of,\n      the Work and Derivative Works thereof.\n\n      \"Contribution\" shall mean any work of authorship, including\n      the original version of the Work and any modifications or additions\n      to that Work or Derivative Works thereof, that is intentionally\n      submitted to Licensor for inclusion in the Work by the copyright owner\n      or by an individual or Legal Entity authorized to submit on behalf of\n      the copyright owner. For the purposes of this definition, \"submitted\"\n      means any form of electronic, verbal, or written communication sent\n      to the Licensor or its representatives, including but not limited to\n      communication on electronic mailing lists, source code control systems,\n      and issue tracking systems that are managed by, or on behalf of, the\n      Licensor for the purpose of discussing and improving the Work, but\n      excluding communication that is conspicuously marked or otherwise\n      designated in writing by the copyright owner as \"Not a Contribution.\"\n\n      \"Contributor\" shall mean Licensor and any individual or Legal Entity\n      on behalf of whom a Contribution has been received by Licensor and\n      subsequently incorporated within the Work.\n\n   2. Grant of Copyright License. Subject to the terms and conditions of\n      this License, each Contributor hereby grants to You a perpetual,\n      worldwide, non-exclusive, no-charge, royalty-free, irrevocable\n      copyright license to reproduce, prepare Derivative Works of,\n      publicly display, publicly perform, sublicense, and distribute the\n      Work and such Derivative Works in Source or Object form.\n\n   3. Grant of Patent License. Subject to the terms and conditions of\n      this License, each Contributor hereby grants to You a perpetual,\n      worldwide, non-exclusive, no-charge, royalty-free, irrevocable\n      (except as stated in this section) patent license to make, have made,\n      use, offer to sell, sell, import, and otherwise transfer the Work,\n      where such license applies only to those patent claims licensable\n      by such Contributor that are necessarily infringed by their\n      Contribution(s) alone or by combination of their Contribution(s)\n      with the Work to which such Contribution(s) was submitted. If You\n      institute patent litigation against any entity (including a\n      cross-claim or counterclaim in a lawsuit) alleging that the Work\n      or a Contribution incorporated within the Work constitutes direct\n      or contributory patent infringement, then any patent licenses\n      granted to You under this License for that Work shall terminate\n      as of the date such litigation is filed.\n\n   4. Redistribution. You may reproduce and distribute copies of the\n      Work or Derivative Works thereof in any medium, with or without\n      modifications, and in Source or Object form, provided that You\n      meet the following conditions:\n\n      (a) You must give any other recipients of the Work or\n          Derivative Works a copy of this License; and\n\n      (b) You must cause any modified files to carry prominent notices\n          stating that You changed the files; and\n\n      (c) You must retain, in the Source form of any Derivative Works\n          that You distribute, all copyright, patent, trademark, and\n          attribution notices from the Source form of the Work,\n          excluding those notices that do not pertain to any part of\n          the Derivative Works; and\n\n      (d) If the Work includes a \"NOTICE\" text file as part of its\n          distribution, then any Derivative Works that You distribute must\n          include a readable copy of the attribution notices contained\n          within such NOTICE file, excluding those notices that do not\n          pertain to any part of the Derivative Works, in at least one\n          of the following places: within a NOTICE text file distributed\n          as part of the Derivative Works; within the Source form or\n          documentation, if provided along with the Derivative Works; or,\n          within a display generated by the Derivative Works, if and\n          wherever such third-party notices normally appear. The contents\n          of the NOTICE file are for informational purposes only and\n          do not modify the License. You may add Your own attribution\n          notices within Derivative Works that You distribute, alongside\n          or as an addendum to the NOTICE text from the Work, provided\n          that such additional attribution notices cannot be construed\n          as modifying the License.\n\n      You may add Your own copyright statement to Your modifications and\n      may provide additional or different license terms and conditions\n      for use, reproduction, or distribution of Your modifications, or\n      for any such Derivative Works as a whole, provided Your use,\n      reproduction, and distribution of the Work otherwise complies with\n      the conditions stated in this License.\n\n   5. Submission of Contributions. Unless You explicitly state otherwise,\n      any Contribution intentionally submitted for inclusion in the Work\n      by You to the Licensor shall be under the terms and conditions of\n      this License, without any additional terms or conditions.\n      Notwithstanding the above, nothing herein shall supersede or modify\n      the terms of any separate license agreement you may have executed\n      with Licensor regarding such Contributions.\n\n   6. Trademarks. This License does not grant permission to use the trade\n      names, trademarks, service marks, or product names of the Licensor,\n      except as required for reasonable and customary use in describing the\n      origin of the Work and reproducing the content of the NOTICE file.\n\n   7. Disclaimer of Warranty. Unless required by applicable law or\n      agreed to in writing, Licensor provides the Work (and each\n      Contributor provides its Contributions) on an \"AS IS\" BASIS,\n      WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or\n      implied, including, without limitation, any warranties or conditions\n      of TITLE, NON-INFRINGEMENT, MERCHANTABILITY, or FITNESS FOR A\n      PARTICULAR PURPOSE. You are solely responsible for determining the\n      appropriateness of using or redistributing the Work and assume any\n      risks associated with Your exercise of permissions under this License.\n\n   8. Limitation of Liability. In no event and under no legal theory,\n      whether in tort (including negligence), contract, or otherwise,\n      unless required by applicable law (such as deliberate and grossly\n      negligent acts) or agreed to in writing, shall any Contributor be\n      liable to You for damages, including any direct, indirect, special,\n      incidental, or consequential damages of any character arising as a\n      result of this License or out of the use or inability to use the\n      Work (including but not limited to damages for loss of goodwill,\n      work stoppage, computer failure or malfunction, or any and all\n      other commercial damages or losses), even if such Contributor\n      has been advised of the possibility of such damages.\n\n   9. Accepting Warranty or Additional Liability. While redistributing\n      the Work or Derivative Works thereof, You may choose to offer,\n      and charge a fee for, acceptance of support, warranty, indemnity,\n      or other liability obligations and/or rights consistent with this\n      License. However, in accepting such obligations, You may act only\n      on Your own behalf and on Your sole responsibility, not on behalf\n      of any other Contributor, and only if You agree to indemnify,\n      defend, and hold each Contributor harmless for any liability\n      incurred by, or claims asserted against, such Contributor by reason\n      of your accepting any such warranty or additional liability.\n\n   END OF TERMS AND CONDITIONS\n\n   APPENDIX: How to apply the Apache License to your work.\n\n      To apply the Apache License to your work, attach the following\n      boilerplate notice, with the fields enclosed by brackets \"[]\"\n      replaced with your own identifying information. (Don't include\n      the brackets!)  The text should be enclosed in the appropriate\n      comment syntax for the file format. We also recommend that a\n      file or class name and description of purpose be included on the\n      same \"printed page\" as the copyright notice for easier\n      identification within third-party archives.\n\n   Copyright [yyyy] [name of copyright owner]\n\n   Licensed under the Apache License, Version 2.0 (the \"License\");\n   you may not use this file except in compliance with the License.\n   You may obtain a copy of the License at\n\n       http://www.apache.org/licenses/LICENSE-2.0\n\n   Unless required by applicable law or agreed to in writing, software\n   distributed under the License is distributed on an \"AS IS\" BASIS,\n   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\n   See the License for the specific language governing permissions and\n   limitations under the License.\n",
  "modelfile": "# Modelfile generated by \"ollama show\"\n# To build a new Modelfile based on this, replace FROM with:\n# FROM all-minilm:latest\n\nFROM /root/.ollama/models/blobs/sha256-797b70c4edf85907fe0a49eb85811256f65fa0f7bf52166b147fd16be2be4662\nTEMPLATE {{ .Prompt }}\nPARAMETER num_ctx 256\nLICENSE \"\"\"                                 Apache License\n                           Version 2.0, January 2004\n                        http://www.apache.org/licenses/\n\n   TERMS AND CONDITIONS FOR USE, REPRODUCTION, AND DISTRIBUTION\n\n   1. Definitions.\n\n      \"License\" shall mean the terms and conditions for use, reproduction,\n      and distribution as defined by Sections 1 through 9 of this document.\n\n      \"Licensor\" shall mean the copyright owner or entity authorized by\n      the copyright owner that is granting the License.\n\n      \"Legal Entity\" shall mean the union of the acting entity and all\n      other entities that control, are controlled by, or are under common\n      control with that entity. For the purposes of this definition,\n      \"control\" means (i) the power, direct or indirect, to cause the\n      direction or management of such entity, whether by contract or\n      otherwise, or (ii) ownership of fifty percent (50%) or more of the\n      outstanding shares, or (iii) beneficial ownership of such entity.\n\n      \"You\" (or \"Your\") shall mean an individual or Legal Entity\n      exercising permissions granted by this License.\n\n      \"Source\" form shall mean the preferred form for making modifications,\n      including but not limited to software source code, documentation\n      source, and configuration files.\n\n      \"Object\" form shall mean any form resulting from mechanical\n      transformation or translation of a Source form, including but\n      not limited to compiled object code, generated documentation,\n      and conversions to other media types.\n\n      \"Work\" shall mean the work of authorship, whether in Source or\n      Object form, made available under the License, as indicated by a\n      copyright notice that is included in or attached to the work\n      (an example is provided in the Appendix below).\n\n      \"Derivative Works\" shall mean any work, whether in Source or Object\n      form, that is based on (or derived from) the Work and for which the\n      editorial revisions, annotations, elaborations, or other modifications\n      represent, as a whole, an original work of authorship. For the purposes\n      of this License, Derivative Works shall not include works that remain\n      separable from, or merely link (or bind by name) to the interfaces of,\n      the Work and Derivative Works thereof.\n\n      \"Contribution\" shall mean any work of authorship, including\n      the original version of the Work and any modifications or additions\n      to that Work or Derivative Works thereof, that is intentionally\n      submitted to Licensor for inclusion in the Work by the copyright owner\n      or by an individual or Legal Entity authorized to submit on behalf of\n      the copyright owner. For the purposes of this definition, \"submitted\"\n      means any form of electronic, verbal, or written communication sent\n      to the Licensor or its representatives, including but not limited to\n      communication on electronic mailing lists, source code control systems,\n      and issue tracking systems that are managed by, or on behalf of, the\n      Licensor for the purpose of discussing and improving the Work, but\n      excluding communication that is conspicuously marked or otherwise\n      designated in writing by the copyright owner as \"Not a Contribution.\"\n\n      \"Contributor\" shall mean Licensor and any individual or Legal Entity\n      on behalf of whom a Contribution has been received by Licensor and\n      subsequently incorporated within the Work.\n\n   2. Grant of Copyright License. Subject to the terms and conditions of\n      this License, each Contributor hereby grants to You a perpetual,\n      worldwide, non-exclusive, no-charge, royalty-free, irrevocable\n      copyright license to reproduce, prepare Derivative Works of,\n      publicly display, publicly perform, sublicense, and distribute the\n      Work and such Derivative Works in Source or Object form.\n\n   3. Grant of Patent License. Subject to the terms and conditions of\n      this License, each Contributor hereby grants to You a perpetual,\n      worldwide, non-exclusive, no-charge, royalty-free, irrevocable\n      (except as stated in this section) patent license to make, have made,\n      use, offer to sell, sell, import, and otherwise transfer the Work,\n      where such license applies only to those patent claims licensable\n      by such Contributor that are necessarily infringed by their\n      Contribution(s) alone or by combination of their Contribution(s)\n      with the Work to which such Contribution(s) was submitted. If You\n      institute patent litigation against any entity (including a\n      cross-claim or counterclaim in a lawsuit) alleging that the Work\n      or a Contribution incorporated within the Work constitutes direct\n      or contributory patent infringement, then any patent licenses\n      granted to You under this License for that Work shall terminate\n      as of the date such litigation is filed.\n\n   4. Redistribution. You may reproduce and distribute copies of the\n      Work or Derivative Works thereof in any medium, with or without\n      modifications, and in Source or Object form, provided that You\n      meet the following conditions:\n\n      (a) You must give any other recipients of the Work or\n          Derivative Works a copy of this License; and\n\n      (b) You must cause any modified files to carry prominent notices\n          stating that You changed the files; and\n\n      (c) You must retain, in the Source form of any Derivative Works\n          that You distribute, all copyright, patent, trademark, and\n          attribution notices from the Source form of the Work,\n          excluding those notices that do not pertain to any part of\n          the Derivative Works; and\n\n      (d) If the Work includes a \"NOTICE\" text file as part of its\n          distribution, then any Derivative Works that You distribute must\n          include a readable copy of the attribution notices contained\n          within such NOTICE file, excluding those notices that do not\n          pertain to any part of the Derivative Works, in at least one\n          of the following places: within a NOTICE text file distributed\n          as part of the Derivative Works; within the Source form or\n          documentation, if provided along with the Derivative Works; or,\n          within a display generated by the Derivative Works, if and\n          wherever such third-party notices normally appear. The contents\n          of the NOTICE file are for informational purposes only and\n          do not modify the License. You may add Your own attribution\n          notices within Derivative Works that You distribute, alongside\n          or as an addendum to the NOTICE text from the Work, provided\n          that such additional attribution notices cannot be construed\n          as modifying the License.\n\n      You may add Your own copyright statement to Your modifications and\n      may provide additional or different license terms and conditions\n      for use, reproduction, or distribution of Your modifications, or\n      for any such Derivative Works as a whole, provided Your use,\n      reproduction, and distribution of the Work otherwise complies with\n      the conditions stated in this License.\n\n   5. Submission of Contributions. Unless You explicitly state otherwise,\n      any Contribution intentionally submitted for inclusion in the Work\n      by You to the Licensor shall be under the terms and conditions of\n      this License, without any additional terms or conditions.\n      Notwithstanding the above, nothing herein shall supersede or modify\n      the terms of any separate license agreement you may have executed\n      with Licensor regarding such Contributions.\n\n   6. Trademarks. This License does not grant permission to use the trade\n      names, trademarks, service marks, or product names of the Licensor,\n      except as required for reasonable and customary use in describing the\n      origin of the Work and reproducing the content of the NOTICE file.\n\n   7. Disclaimer of Warranty. Unless required by applicable law or\n      agreed to in writing, Licensor provides the Work (and each\n      Contributor provides its Contributions) on an \"AS IS\" BASIS,\n      WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or\n      implied, including, without limitation, any warranties or conditions\n      of TITLE, NON-INFRINGEMENT, MERCHANTABILITY, or FITNESS FOR A\n      PARTICULAR PURPOSE. You are solely responsible for determining the\n      appropriateness of using or redistributing the Work and assume any\n      risks associated with Your exercise of permissions under this License.\n\n   8. Limitation of Liability. In no event and under no legal theory,\n      whether in tort (including negligence), contract, or otherwise,\n      unless required by applicable law (such as deliberate and grossly\n      negligent acts) or agreed to in writing, shall any Contributor be\n      liable to You for damages, including any direct, indirect, special,\n      incidental, or consequential damages of any character arising as a\n      result of this License or out of the use or inability to use the\n      Work (including but not limited to damages for loss of goodwill,\n      work stoppage, computer failure or malfunction, or any and all\n      other commercial damages or losses), even if such Contributor\n      has been advised of the possibility of such damages.\n\n   9. Accepting Warranty or Additional Liability. While redistributing\n      the Work or Derivative Works thereof, You may choose to offer,\n      and charge a fee for, acceptance of support, warranty, indemnity,\n      or other liability obligations and/or rights consistent with this\n      License. However, in accepting such obligations, You may act only\n      on Your own behalf and on Your sole responsibility, not on behalf\n      of any other Contributor, and only if You agree to indemnify,\n      defend, and hold each Contributor harmless for any liability\n      incurred by, or claims asserted against, such Contributor by reason\n      of your accepting any such warranty or additional liability.\n\n   END OF TERMS AND CONDITIONS\n\n   APPENDIX: How to apply the Apache License to your work.\n\n      To apply the Apache License to your work, attach the following\n      boilerplate notice, with the fields enclosed by brackets \"[]\"\n      replaced with your own identifying information. (Don't include\n      the brackets!)  The text should be enclosed in the appropriate\n      comment syntax for the file format. We also recommend that a\n      file or class name and description of purpose be included on the\n      same \"printed page\" as the copyright notice for easier\n      identification within third-party archives.\n\n   Copyright [yyyy] [name of copyright owner]\n\n   Licensed under the Apache License, Version 2.0 (the \"License\");\n   you may not use this file except in compliance with the License.\n   You may obtain a copy of the License at\n\n       http://www.apache.org/licenses/LICENSE-2.0\n\n   Unless required by applicable law or agreed to in writing, software\n   distributed under the License is distributed on an \"AS IS\" BASIS,\n   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\n   See the License for the specific language governing permissions and\n   limitations under the License.\n\"\"\"\n",
  "parameters": "num_ctx                        256",
  "template": "{{ .Prompt }}",
  "details": {
    "parent_model": "",
    "format": "gguf",
    "family": "bert",
    "families": [
      "bert"
    ],
    "parameter_size": "23M",
    "quantization_level": "F16"
  },
  "model_info": {
    "bert.attention.causal": false,
    "bert.attention.head_count": 12,
    "bert.attention.layer_norm_epsilon": 1E-12,
    "bert.block_count": 6,
    "bert.context_length": 512,
    "bert.embedding_length": 384,
    "bert.feed_forward_length": 1536,
    "bert.pooling_type": 1,
    "general.architecture": "bert",
    "general.file_type": 1,
    "general.parameter_count": 22565376,
    "tokenizer.ggml.bos_token_id": 101,
    "tokenizer.ggml.cls_token_id": 101,
    "tokenizer.ggml.eos_token_id": 102,
    "tokenizer.ggml.mask_token_id": 103,
    "tokenizer.ggml.model": "bert",
    "tokenizer.ggml.padding_token_id": 0,
    "tokenizer.ggml.scores": null,
    "tokenizer.ggml.seperator_token_id": 102,
    "tokenizer.ggml.token_type": null,
    "tokenizer.ggml.token_type_count": 2,
    "tokenizer.ggml.tokens": null,
    "tokenizer.ggml.unknown_token_id": 100
  },
  "tensors": [
    {
      "name": "token_embd.weight",
      "type": "F16",
      "shape": [
        384,
        30522
      ]
    },
    {
      "name": "position_embd.weight",
      "type": "F16",
      "shape": [
        384,
        512
      ]
    },
    {
      "name": "token_types.weight",
      "type": "F32",
      "shape": [
        384,
        2
      ]
    },
    {
      "name": "token_embd_norm.weight",
      "type": "F32",
      "shape": [
        384
      ]
    },
    {
      "name": "token_embd_norm.bias",
      "type": "F32",
      "shape": [
        384
      ]
    },
    {
      "name": "blk.0.attn_q.weight",
      "type": "F16",
      "shape": [
        384,
        384
      ]
    },
    {
      "name": "blk.0.attn_q.bias",
      "type": "F32",
      "shape": [
        384
      ]
    },
    {
      "name": "blk.0.attn_k.weight",
      "type": "F16",
      "shape": [
        384,
        384
      ]
    },
    {
      "name": "blk.0.attn_k.bias",
      "type": "F32",
      "shape": [
        384
      ]
    },
    {
      "name": "blk.0.attn_v.weight",
      "type": "F16",
      "shape": [
        384,
        384
      ]
    },
    {
      "name": "blk.0.attn_v.bias",
      "type": "F32",
      "shape": [
        384
      ]
    },
    {
      "name": "blk.0.attn_output.weight",
      "type": "F16",
      "shape": [
        384,
        384
      ]
    },
    {
      "name": "blk.0.attn_output.bias",
      "type": "F32",
      "shape": [
        384
      ]
    },
    {
      "name": "blk.0.attn_output_norm.weight",
      "type": "F32",
      "shape": [
        384
      ]
    },
    {
      "name": "blk.0.attn_output_norm.bias",
      "type": "F32",
      "shape": [
        384
      ]
    },
    {
      "name": "blk.0.ffn_up.weight",
      "type": "F16",
      "shape": [
        384,
        1536
      ]
    },
    {
      "name": "blk.0.ffn_up.bias",
      "type": "F32",
      "shape": [
        1536
      ]
    },
    {
      "name": "blk.0.ffn_down.weight",
      "type": "F16",
      "shape": [
        1536,
        384
      ]
    },
    {
      "name": "blk.0.ffn_down.bias",
      "type": "F32",
      "shape": [
        384
      ]
    },
    {
      "name": "blk.0.layer_output_norm.weight",
      "type": "F32",
      "shape": [
        384
      ]
    },
    {
      "name": "blk.0.layer_output_norm.bias",
      "type": "F32",
      "shape": [
        384
      ]
    },
    {
      "name": "blk.1.attn_q.weight",
      "type": "F16",
      "shape": [
        384,
        384
      ]
    },
    {
      "name": "blk.1.attn_q.bias",
      "type": "F32",
      "shape": [
        384
      ]
    },
    {
      "name": "blk.1.attn_k.weight",
      "type": "F16",
      "shape": [
        384,
        384
      ]
    },
    {
      "name": "blk.1.attn_k.bias",
      "type": "F32",
      "shape": [
        384
      ]
    },
    {
      "name": "blk.1.attn_v.weight",
      "type": "F16",
      "shape": [
        384,
        384
      ]
    },
    {
      "name": "blk.1.attn_v.bias",
      "type": "F32",
      "shape": [
        384
      ]
    },
    {
      "name": "blk.1.attn_output.weight",
      "type": "F16",
      "shape": [
        384,
        384
      ]
    },
    {
      "name": "blk.1.attn_output.bias",
      "type": "F32",
      "shape": [
        384
      ]
    },
    {
      "name": "blk.1.attn_output_norm.weight",
      "type": "F32",
      "shape": [
        384
      ]
    },
    {
      "name": "blk.1.attn_output_norm.bias",
      "type": "F32",
      "shape": [
        384
      ]
    },
    {
      "name": "blk.1.ffn_up.weight",
      "type": "F16",
      "shape": [
        384,
        1536
      ]
    },
    {
      "name": "blk.1.ffn_up.bias",
      "type": "F32",
      "shape": [
        1536
      ]
    },
    {
      "name": "blk.1.ffn_down.weight",
      "type": "F16",
      "shape": [
        1536,
        384
      ]
    },
    {
      "name": "blk.1.ffn_down.bias",
      "type": "F32",
      "shape": [
        384
      ]
    },
    {
      "name": "blk.1.layer_output_norm.weight",
      "type": "F32",
      "shape": [
        384
      ]
    },
    {
      "name": "blk.1.layer_output_norm.bias",
      "type": "F32",
      "shape": [
        384
      ]
    },
    {
      "name": "blk.2.attn_q.weight",
      "type": "F16",
      "shape": [
        384,
        384
      ]
    },
    {
      "name": "blk.2.attn_q.bias",
      "type": "F32",
      "shape": [
        384
      ]
    },
    {
      "name": "blk.2.attn_k.weight",
      "type": "F16",
      "shape": [
        384,
        384
      ]
    },
    {
      "name": "blk.2.attn_k.bias",
      "type": "F32",
      "shape": [
        384
      ]
    },
    {
      "name": "blk.2.attn_v.weight",
      "type": "F16",
      "shape": [
        384,
        384
      ]
    },
    {
      "name": "blk.2.attn_v.bias",
      "type": "F32",
      "shape": [
        384
      ]
    },
    {
      "name": "blk.2.attn_output.weight",
      "type": "F16",
      "shape": [
        384,
        384
      ]
    },
    {
      "name": "blk.2.attn_output.bias",
      "type": "F32",
      "shape": [
        384
      ]
    },
    {
      "name": "blk.2.attn_output_norm.weight",
      "type": "F32",
      "shape": [
        384
      ]
    },
    {
      "name": "blk.2.attn_output_norm.bias",
      "type": "F32",
      "shape": [
        384
      ]
    },
    {
      "name": "blk.2.ffn_up.weight",
      "type": "F16",
      "shape": [
        384,
        1536
      ]
    },
    {
      "name": "blk.2.ffn_up.bias",
      "type": "F32",
      "shape": [
        1536
      ]
    },
    {
      "name": "blk.2.ffn_down.weight",
      "type": "F16",
      "shape": [
        1536,
        384
      ]
    },
    {
      "name": "blk.2.ffn_down.bias",
      "type": "F32",
      "shape": [
        384
      ]
    },
    {
      "name": "blk.2.layer_output_norm.weight",
      "type": "F32",
      "shape": [
        384
      ]
    },
    {
      "name": "blk.2.layer_output_norm.bias",
      "type": "F32",
      "shape": [
        384
      ]
    },
    {
      "name": "blk.3.attn_q.weight",
      "type": "F16",
      "shape": [
        384,
        384
      ]
    },
    {
      "name": "blk.3.attn_q.bias",
      "type": "F32",
      "shape": [
        384
      ]
    },
    {
      "name": "blk.3.attn_k.weight",
      "type": "F16",
      "shape": [
        384,
        384
      ]
    },
    {
      "name": "blk.3.attn_k.bias",
      "type": "F32",
      "shape": [
        384
      ]
    },
    {
      "name": "blk.3.attn_v.weight",
      "type": "F16",
      "shape": [
        384,
        384
      ]
    },
    {
      "name": "blk.3.attn_v.bias",
      "type": "F32",
      "shape": [
        384
      ]
    },
    {
      "name": "blk.3.attn_output.weight",
      "type": "F16",
      "shape": [
        384,
        384
      ]
    },
    {
      "name": "blk.3.attn_output.bias",
      "type": "F32",
      "shape": [
        384
      ]
    },
    {
      "name": "blk.3.attn_output_norm.weight",
      "type": "F32",
      "shape": [
        384
      ]
    },
    {
      "name": "blk.3.attn_output_norm.bias",
      "type": "F32",
      "shape": [
        384
      ]
    },
    {
      "name": "blk.3.ffn_up.weight",
      "type": "F16",
      "shape": [
        384,
        1536
      ]
    },
    {
      "name": "blk.3.ffn_up.bias",
      "type": "F32",
      "shape": [
        1536
      ]
    },
    {
      "name": "blk.3.ffn_down.weight",
      "type": "F16",
      "shape": [
        1536,
        384
      ]
    },
    {
      "name": "blk.3.ffn_down.bias",
      "type": "F32",
      "shape": [
        384
      ]
    },
    {
      "name": "blk.3.layer_output_norm.weight",
      "type": "F32",
      "shape": [
        384
      ]
    },
    {
      "name": "blk.3.layer_output_norm.bias",
      "type": "F32",
      "shape": [
        384
      ]
    },
    {
      "name": "blk.4.attn_q.weight",
      "type": "F16",
      "shape": [
        384,
        384
      ]
    },
    {
      "name": "blk.4.attn_q.bias",
      "type": "F32",
      "shape": [
        384
      ]
    },
    {
      "name": "blk.4.attn_k.weight",
      "type": "F16",
      "shape": [
        384,
        384
      ]
    },
    {
      "name": "blk.4.attn_k.bias",
      "type": "F32",
      "shape": [
        384
      ]
    },
    {
      "name": "blk.4.attn_v.weight",
      "type": "F16",
      "shape": [
        384,
        384
      ]
    },
    {
      "name": "blk.4.attn_v.bias",
      "type": "F32",
      "shape": [
        384
      ]
    },
    {
      "name": "blk.4.attn_output.weight",
      "type": "F16",
      "shape": [
        384,
        384
      ]
    },
    {
      "name": "blk.4.attn_output.bias",
      "type": "F32",
      "shape": [
        384
      ]
    },
    {
      "name": "blk.4.attn_output_norm.weight",
      "type": "F32",
      "shape": [
        384
      ]
    },
    {
      "name": "blk.4.attn_output_norm.bias",
      "type": "F32",
      "shape": [
        384
      ]
    },
    {
      "name": "blk.4.ffn_up.weight",
      "type": "F16",
      "shape": [
        384,
        1536
      ]
    },
    {
      "name": "blk.4.ffn_up.bias",
      "type": "F32",
      "shape": [
        1536
      ]
    },
    {
      "name": "blk.4.ffn_down.weight",
      "type": "F16",
      "shape": [
        1536,
        384
      ]
    },
    {
      "name": "blk.4.ffn_down.bias",
      "type": "F32",
      "shape": [
        384
      ]
    },
    {
      "name": "blk.4.layer_output_norm.weight",
      "type": "F32",
      "shape": [
        384
      ]
    },
    {
      "name": "blk.4.layer_output_norm.bias",
      "type": "F32",
      "shape": [
        384
      ]
    },
    {
      "name": "blk.5.attn_q.weight",
      "type": "F16",
      "shape": [
        384,
        384
      ]
    },
    {
      "name": "blk.5.attn_q.bias",
      "type": "F32",
      "shape": [
        384
      ]
    },
    {
      "name": "blk.5.attn_k.weight",
      "type": "F16",
      "shape": [
        384,
        384
      ]
    },
    {
      "name": "blk.5.attn_k.bias",
      "type": "F32",
      "shape": [
        384
      ]
    },
    {
      "name": "blk.5.attn_v.weight",
      "type": "F16",
      "shape": [
        384,
        384
      ]
    },
    {
      "name": "blk.5.attn_v.bias",
      "type": "F32",
      "shape": [
        384
      ]
    },
    {
      "name": "blk.5.attn_output.weight",
      "type": "F16",
      "shape": [
        384,
        384
      ]
    },
    {
      "name": "blk.5.attn_output.bias",
      "type": "F32",
      "shape": [
        384
      ]
    },
    {
      "name": "blk.5.attn_output_norm.weight",
      "type": "F32",
      "shape": [
        384
      ]
    },
    {
      "name": "blk.5.attn_output_norm.bias",
      "type": "F32",
      "shape": [
        384
      ]
    },
    {
      "name": "blk.5.ffn_up.weight",
      "type": "F16",
      "shape": [
        384,
        1536
      ]
    },
    {
      "name": "blk.5.ffn_up.bias",
      "type": "F32",
      "shape": [
        1536
      ]
    },
    {
      "name": "blk.5.ffn_down.weight",
      "type": "F16",
      "shape": [
        1536,
        384
      ]
    },
    {
      "name": "blk.5.ffn_down.bias",
      "type": "F32",
      "shape": [
        384
      ]
    },
    {
      "name": "blk.5.layer_output_norm.weight",
      "type": "F32",
      "shape": [
        384
      ]
    },
    {
      "name": "blk.5.layer_output_norm.bias",
      "type": "F32",
      "shape": [
        384
      ]
    }
  ],
  "capabilities": [
    "embedding"
  ],
  "modified_at": "2026-04-12T03:10:02.270756106Z"
}
{
  "license": "                                 Apache License\n                           Version 2.0, January 2004\n                        http://www.apache.org/licenses/\n\n   TERMS AND CONDITIONS FOR USE, REPRODUCTION, AND DISTRIBUTION\n\n   1. Definitions.\n\n      \"License\" shall mean the terms and conditions for use, reproduction,\n      and distribution as defined by Sections 1 through 9 of this document.\n\n      \"Licensor\" shall mean the copyright owner or entity authorized by\n      the copyright owner that is granting the License.\n\n      \"Legal Entity\" shall mean the union of the acting entity and all\n      other entities that control, are controlled by, or are under common\n      control with that entity. For the purposes of this definition,\n      \"control\" means (i) the power, direct or indirect, to cause the\n      direction or management of such entity, whether by contract or\n      otherwise, or (ii) ownership of fifty percent (50%) or more of the\n      outstanding shares, or (iii) beneficial ownership of such entity.\n\n      \"You\" (or \"Your\") shall mean an individual or Legal Entity\n      exercising permissions granted by this License.\n\n      \"Source\" form shall mean the preferred form for making modifications,\n      including but not limited to software source code, documentation\n      source, and configuration files.\n\n      \"Object\" form shall mean any form resulting from mechanical\n      transformation or translation of a Source form, including but\n      not limited to compiled object code, generated documentation,\n      and conversions to other media types.\n\n      \"Work\" shall mean the work of authorship, whether in Source or\n      Object form, made available under the License, as indicated by a\n      copyright notice that is included in or attached to the work\n      (an example is provided in the Appendix below).\n\n      \"Derivative Works\" shall mean any work, whether in Source or Object\n      form, that is based on (or derived from) the Work and for which the\n      editorial revisions, annotations, elaborations, or other modifications\n      represent, as a whole, an original work of authorship. For the purposes\n      of this License, Derivative Works shall not include works that remain\n      separable from, or merely link (or bind by name) to the interfaces of,\n      the Work and Derivative Works thereof.\n\n      \"Contribution\" shall mean any work of authorship, including\n      the original version of the Work and any modifications or additions\n      to that Work or Derivative Works thereof, that is intentionally\n      submitted to Licensor for inclusion in the Work by the copyright owner\n      or by an individual or Legal Entity authorized to submit on behalf of\n      the copyright owner. For the purposes of this definition, \"submitted\"\n      means any form of electronic, verbal, or written communication sent\n      to the Licensor or its representatives, including but not limited to\n      communication on electronic mailing lists, source code control systems,\n      and issue tracking systems that are managed by, or on behalf of, the\n      Licensor for the purpose of discussing and improving the Work, but\n      excluding communication that is conspicuously marked or otherwise\n      designated in writing by the copyright owner as \"Not a Contribution.\"\n\n      \"Contributor\" shall mean Licensor and any individual or Legal Entity\n      on behalf of whom a Contribution has been received by Licensor and\n      subsequently incorporated within the Work.\n\n   2. Grant of Copyright License. Subject to the terms and conditions of\n      this License, each Contributor hereby grants to You a perpetual,\n      worldwide, non-exclusive, no-charge, royalty-free, irrevocable\n      copyright license to reproduce, prepare Derivative Works of,\n      publicly display, publicly perform, sublicense, and distribute the\n      Work and such Derivative Works in Source or Object form.\n\n   3. Grant of Patent License. Subject to the terms and conditions of\n      this License, each Contributor hereby grants to You a perpetual,\n      worldwide, non-exclusive, no-charge, royalty-free, irrevocable\n      (except as stated in this section) patent license to make, have made,\n      use, offer to sell, sell, import, and otherwise transfer the Work,\n      where such license applies only to those patent claims licensable\n      by such Contributor that are necessarily infringed by their\n      Contribution(s) alone or by combination of their Contribution(s)\n      with the Work to which such Contribution(s) was submitted. If You\n      institute patent litigation against any entity (including a\n      cross-claim or counterclaim in a lawsuit) alleging that the Work\n      or a Contribution incorporated within the Work constitutes direct\n      or contributory patent infringement, then any patent licenses\n      granted to You under this License for that Work shall terminate\n      as of the date such litigation is filed.\n\n   4. Redistribution. You may reproduce and distribute copies of the\n      Work or Derivative Works thereof in any medium, with or without\n      modifications, and in Source or Object form, provided that You\n      meet the following conditions:\n\n      (a) You must give any other recipients of the Work or\n          Derivative Works a copy of this License; and\n\n      (b) You must cause any modified files to carry prominent notices\n          stating that You changed the files; and\n\n      (c) You must retain, in the Source form of any Derivative Works\n          that You distribute, all copyright, patent, trademark, and\n          attribution notices from the Source form of the Work,\n          excluding those notices that do not pertain to any part of\n          the Derivative Works; and\n\n      (d) If the Work includes a \"NOTICE\" text file as part of its\n          distribution, then any Derivative Works that You distribute must\n          include a readable copy of the attribution notices contained\n          within such NOTICE file, excluding those notices that do not\n          pertain to any part of the Derivative Works, in at least one\n          of the following places: within a NOTICE text file distributed\n          as part of the Derivative Works; within the Source form or\n          documentation, if provided along with the Derivative Works; or,\n          within a display generated by the Derivative Works, if and\n          wherever such third-party notices normally appear. The contents\n          of the NOTICE file are for informational purposes only and\n          do not modify the License. You may add Your own attribution\n          notices within Derivative Works that You distribute, alongside\n          or as an addendum to the NOTICE text from the Work, provided\n          that such additional attribution notices cannot be construed\n          as modifying the License.\n\n      You may add Your own copyright statement to Your modifications and\n      may provide additional or different license terms and conditions\n      for use, reproduction, or distribution of Your modifications, or\n      for any such Derivative Works as a whole, provided Your use,\n      reproduction, and distribution of the Work otherwise complies with\n      the conditions stated in this License.\n\n   5. Submission of Contributions. Unless You explicitly state otherwise,\n      any Contribution intentionally submitted for inclusion in the Work\n      by You to the Licensor shall be under the terms and conditions of\n      this License, without any additional terms or conditions.\n      Notwithstanding the above, nothing herein shall supersede or modify\n      the terms of any separate license agreement you may have executed\n      with Licensor regarding such Contributions.\n\n   6. Trademarks. This License does not grant permission to use the trade\n      names, trademarks, service marks, or product names of the Licensor,\n      except as required for reasonable and customary use in describing the\n      origin of the Work and reproducing the content of the NOTICE file.\n\n   7. Disclaimer of Warranty. Unless required by applicable law or\n      agreed to in writing, Licensor provides the Work (and each\n      Contributor provides its Contributions) on an \"AS IS\" BASIS,\n      WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or\n      implied, including, without limitation, any warranties or conditions\n      of TITLE, NON-INFRINGEMENT, MERCHANTABILITY, or FITNESS FOR A\n      PARTICULAR PURPOSE. You are solely responsible for determining the\n      appropriateness of using or redistributing the Work and assume any\n      risks associated with Your exercise of permissions under this License.\n\n   8. Limitation of Liability. In no event and under no legal theory,\n      whether in tort (including negligence), contract, or otherwise,\n      unless required by applicable law (such as deliberate and grossly\n      negligent acts) or agreed to in writing, shall any Contributor be\n      liable to You for damages, including any direct, indirect, special,\n      incidental, or consequential damages of any character arising as a\n      result of this License or out of the use or inability to use the\n      Work (including but not limited to damages for loss of goodwill,\n      work stoppage, computer failure or malfunction, or any and all\n      other commercial damages or losses), even if such Contributor\n      has been advised of the possibility of such damages.\n\n   9. Accepting Warranty or Additional Liability. While redistributing\n      the Work or Derivative Works thereof, You may choose to offer,\n      and charge a fee for, acceptance of support, warranty, indemnity,\n      or other liability obligations and/or rights consistent with this\n      License. However, in accepting such obligations, You may act only\n      on Your own behalf and on Your sole responsibility, not on behalf\n      of any other Contributor, and only if You agree to indemnify,\n      defend, and hold each Contributor harmless for any liability\n      incurred by, or claims asserted against, such Contributor by reason\n      of your accepting any such warranty or additional liability.\n\n   END OF TERMS AND CONDITIONS\n\n   APPENDIX: How to apply the Apache License to your work.\n\n      To apply the Apache License to your work, attach the following\n      boilerplate notice, with the fields enclosed by brackets \"[]\"\n      replaced with your own identifying information. (Don't include\n      the brackets!)  The text should be enclosed in the appropriate\n      comment syntax for the file format. We also recommend that a\n      file or class name and description of purpose be included on the\n      same \"printed page\" as the copyright notice for easier\n      identification within third-party archives.\n\n   Copyright [yyyy] [name of copyright owner]\n\n   Licensed under the Apache License, Version 2.0 (the \"License\");\n   you may not use this file except in compliance with the License.\n   You may obtain a copy of the License at\n\n       http://www.apache.org/licenses/LICENSE-2.0\n\n   Unless required by applicable law or agreed to in writing, software\n   distributed under the License is distributed on an \"AS IS\" BASIS,\n   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\n   See the License for the specific language governing permissions and\n   limitations under the License.\n",
  "modelfile": "# Modelfile generated by \"ollama show\"\n# To build a new Modelfile based on this, replace FROM with:\n# FROM nomic-embed-text:latest\n\nFROM /root/.ollama/models/blobs/sha256-970aa74c0a90ef7482477cf803618e776e173c007bf957f635f1015bfcfef0e6\nTEMPLATE {{ .Prompt }}\nPARAMETER num_ctx 8192\nLICENSE \"\"\"                                 Apache License\n                           Version 2.0, January 2004\n                        http://www.apache.org/licenses/\n\n   TERMS AND CONDITIONS FOR USE, REPRODUCTION, AND DISTRIBUTION\n\n   1. Definitions.\n\n      \"License\" shall mean the terms and conditions for use, reproduction,\n      and distribution as defined by Sections 1 through 9 of this document.\n\n      \"Licensor\" shall mean the copyright owner or entity authorized by\n      the copyright owner that is granting the License.\n\n      \"Legal Entity\" shall mean the union of the acting entity and all\n      other entities that control, are controlled by, or are under common\n      control with that entity. For the purposes of this definition,\n      \"control\" means (i) the power, direct or indirect, to cause the\n      direction or management of such entity, whether by contract or\n      otherwise, or (ii) ownership of fifty percent (50%) or more of the\n      outstanding shares, or (iii) beneficial ownership of such entity.\n\n      \"You\" (or \"Your\") shall mean an individual or Legal Entity\n      exercising permissions granted by this License.\n\n      \"Source\" form shall mean the preferred form for making modifications,\n      including but not limited to software source code, documentation\n      source, and configuration files.\n\n      \"Object\" form shall mean any form resulting from mechanical\n      transformation or translation of a Source form, including but\n      not limited to compiled object code, generated documentation,\n      and conversions to other media types.\n\n      \"Work\" shall mean the work of authorship, whether in Source or\n      Object form, made available under the License, as indicated by a\n      copyright notice that is included in or attached to the work\n      (an example is provided in the Appendix below).\n\n      \"Derivative Works\" shall mean any work, whether in Source or Object\n      form, that is based on (or derived from) the Work and for which the\n      editorial revisions, annotations, elaborations, or other modifications\n      represent, as a whole, an original work of authorship. For the purposes\n      of this License, Derivative Works shall not include works that remain\n      separable from, or merely link (or bind by name) to the interfaces of,\n      the Work and Derivative Works thereof.\n\n      \"Contribution\" shall mean any work of authorship, including\n      the original version of the Work and any modifications or additions\n      to that Work or Derivative Works thereof, that is intentionally\n      submitted to Licensor for inclusion in the Work by the copyright owner\n      or by an individual or Legal Entity authorized to submit on behalf of\n      the copyright owner. For the purposes of this definition, \"submitted\"\n      means any form of electronic, verbal, or written communication sent\n      to the Licensor or its representatives, including but not limited to\n      communication on electronic mailing lists, source code control systems,\n      and issue tracking systems that are managed by, or on behalf of, the\n      Licensor for the purpose of discussing and improving the Work, but\n      excluding communication that is conspicuously marked or otherwise\n      designated in writing by the copyright owner as \"Not a Contribution.\"\n\n      \"Contributor\" shall mean Licensor and any individual or Legal Entity\n      on behalf of whom a Contribution has been received by Licensor and\n      subsequently incorporated within the Work.\n\n   2. Grant of Copyright License. Subject to the terms and conditions of\n      this License, each Contributor hereby grants to You a perpetual,\n      worldwide, non-exclusive, no-charge, royalty-free, irrevocable\n      copyright license to reproduce, prepare Derivative Works of,\n      publicly display, publicly perform, sublicense, and distribute the\n      Work and such Derivative Works in Source or Object form.\n\n   3. Grant of Patent License. Subject to the terms and conditions of\n      this License, each Contributor hereby grants to You a perpetual,\n      worldwide, non-exclusive, no-charge, royalty-free, irrevocable\n      (except as stated in this section) patent license to make, have made,\n      use, offer to sell, sell, import, and otherwise transfer the Work,\n      where such license applies only to those patent claims licensable\n      by such Contributor that are necessarily infringed by their\n      Contribution(s) alone or by combination of their Contribution(s)\n      with the Work to which such Contribution(s) was submitted. If You\n      institute patent litigation against any entity (including a\n      cross-claim or counterclaim in a lawsuit) alleging that the Work\n      or a Contribution incorporated within the Work constitutes direct\n      or contributory patent infringement, then any patent licenses\n      granted to You under this License for that Work shall terminate\n      as of the date such litigation is filed.\n\n   4. Redistribution. You may reproduce and distribute copies of the\n      Work or Derivative Works thereof in any medium, with or without\n      modifications, and in Source or Object form, provided that You\n      meet the following conditions:\n\n      (a) You must give any other recipients of the Work or\n          Derivative Works a copy of this License; and\n\n      (b) You must cause any modified files to carry prominent notices\n          stating that You changed the files; and\n\n      (c) You must retain, in the Source form of any Derivative Works\n          that You distribute, all copyright, patent, trademark, and\n          attribution notices from the Source form of the Work,\n          excluding those notices that do not pertain to any part of\n          the Derivative Works; and\n\n      (d) If the Work includes a \"NOTICE\" text file as part of its\n          distribution, then any Derivative Works that You distribute must\n          include a readable copy of the attribution notices contained\n          within such NOTICE file, excluding those notices that do not\n          pertain to any part of the Derivative Works, in at least one\n          of the following places: within a NOTICE text file distributed\n          as part of the Derivative Works; within the Source form or\n          documentation, if provided along with the Derivative Works; or,\n          within a display generated by the Derivative Works, if and\n          wherever such third-party notices normally appear. The contents\n          of the NOTICE file are for informational purposes only and\n          do not modify the License. You may add Your own attribution\n          notices within Derivative Works that You distribute, alongside\n          or as an addendum to the NOTICE text from the Work, provided\n          that such additional attribution notices cannot be construed\n          as modifying the License.\n\n      You may add Your own copyright statement to Your modifications and\n      may provide additional or different license terms and conditions\n      for use, reproduction, or distribution of Your modifications, or\n      for any such Derivative Works as a whole, provided Your use,\n      reproduction, and distribution of the Work otherwise complies with\n      the conditions stated in this License.\n\n   5. Submission of Contributions. Unless You explicitly state otherwise,\n      any Contribution intentionally submitted for inclusion in the Work\n      by You to the Licensor shall be under the terms and conditions of\n      this License, without any additional terms or conditions.\n      Notwithstanding the above, nothing herein shall supersede or modify\n      the terms of any separate license agreement you may have executed\n      with Licensor regarding such Contributions.\n\n   6. Trademarks. This License does not grant permission to use the trade\n      names, trademarks, service marks, or product names of the Licensor,\n      except as required for reasonable and customary use in describing the\n      origin of the Work and reproducing the content of the NOTICE file.\n\n   7. Disclaimer of Warranty. Unless required by applicable law or\n      agreed to in writing, Licensor provides the Work (and each\n      Contributor provides its Contributions) on an \"AS IS\" BASIS,\n      WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or\n      implied, including, without limitation, any warranties or conditions\n      of TITLE, NON-INFRINGEMENT, MERCHANTABILITY, or FITNESS FOR A\n      PARTICULAR PURPOSE. You are solely responsible for determining the\n      appropriateness of using or redistributing the Work and assume any\n      risks associated with Your exercise of permissions under this License.\n\n   8. Limitation of Liability. In no event and under no legal theory,\n      whether in tort (including negligence), contract, or otherwise,\n      unless required by applicable law (such as deliberate and grossly\n      negligent acts) or agreed to in writing, shall any Contributor be\n      liable to You for damages, including any direct, indirect, special,\n      incidental, or consequential damages of any character arising as a\n      result of this License or out of the use or inability to use the\n      Work (including but not limited to damages for loss of goodwill,\n      work stoppage, computer failure or malfunction, or any and all\n      other commercial damages or losses), even if such Contributor\n      has been advised of the possibility of such damages.\n\n   9. Accepting Warranty or Additional Liability. While redistributing\n      the Work or Derivative Works thereof, You may choose to offer,\n      and charge a fee for, acceptance of support, warranty, indemnity,\n      or other liability obligations and/or rights consistent with this\n      License. However, in accepting such obligations, You may act only\n      on Your own behalf and on Your sole responsibility, not on behalf\n      of any other Contributor, and only if You agree to indemnify,\n      defend, and hold each Contributor harmless for any liability\n      incurred by, or claims asserted against, such Contributor by reason\n      of your accepting any such warranty or additional liability.\n\n   END OF TERMS AND CONDITIONS\n\n   APPENDIX: How to apply the Apache License to your work.\n\n      To apply the Apache License to your work, attach the following\n      boilerplate notice, with the fields enclosed by brackets \"[]\"\n      replaced with your own identifying information. (Don't include\n      the brackets!)  The text should be enclosed in the appropriate\n      comment syntax for the file format. We also recommend that a\n      file or class name and description of purpose be included on the\n      same \"printed page\" as the copyright notice for easier\n      identification within third-party archives.\n\n   Copyright [yyyy] [name of copyright owner]\n\n   Licensed under the Apache License, Version 2.0 (the \"License\");\n   you may not use this file except in compliance with the License.\n   You may obtain a copy of the License at\n\n       http://www.apache.org/licenses/LICENSE-2.0\n\n   Unless required by applicable law or agreed to in writing, software\n   distributed under the License is distributed on an \"AS IS\" BASIS,\n   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\n   See the License for the specific language governing permissions and\n   limitations under the License.\n\"\"\"\n",
  "parameters": "num_ctx                        8192",
  "template": "{{ .Prompt }}",
  "details": {
    "parent_model": "",
    "format": "gguf",
    "family": "nomic-bert",
    "families": [
      "nomic-bert"
    ],
    "parameter_size": "137M",
    "quantization_level": "F16"
  },
  "model_info": {
    "general.architecture": "nomic-bert",
    "general.file_type": 1,
    "general.parameter_count": 136727040,
    "nomic-bert.attention.causal": false,
    "nomic-bert.attention.head_count": 12,
    "nomic-bert.attention.layer_norm_epsilon": 1E-12,
    "nomic-bert.block_count": 12,
    "nomic-bert.context_length": 2048,
    "nomic-bert.embedding_length": 768,
    "nomic-bert.feed_forward_length": 3072,
    "nomic-bert.pooling_type": 1,
    "nomic-bert.rope.freq_base": 1000,
    "tokenizer.ggml.bos_token_id": 101,
    "tokenizer.ggml.cls_token_id": 101,
    "tokenizer.ggml.eos_token_id": 102,
    "tokenizer.ggml.mask_token_id": 103,
    "tokenizer.ggml.model": "bert",
    "tokenizer.ggml.padding_token_id": 0,
    "tokenizer.ggml.scores": null,
    "tokenizer.ggml.seperator_token_id": 102,
    "tokenizer.ggml.token_type": null,
    "tokenizer.ggml.token_type_count": 2,
    "tokenizer.ggml.tokens": null,
    "tokenizer.ggml.unknown_token_id": 100
  },
  "tensors": [
    {
      "name": "token_embd_norm.bias",
      "type": "F32",
      "shape": [
        768
      ]
    },
    {
      "name": "token_embd_norm.weight",
      "type": "F32",
      "shape": [
        768
      ]
    },
    {
      "name": "token_types.weight",
      "type": "F32",
      "shape": [
        768,
        2
      ]
    },
    {
      "name": "token_embd.weight",
      "type": "F16",
      "shape": [
        768,
        30522
      ]
    },
    {
      "name": "blk.0.attn_qkv.weight",
      "type": "F16",
      "shape": [
        768,
        2304
      ]
    },
    {
      "name": "blk.0.attn_output.weight",
      "type": "F16",
      "shape": [
        768,
        768
      ]
    },
    {
      "name": "blk.0.ffn_up.weight",
      "type": "F16",
      "shape": [
        768,
        3072
      ]
    },
    {
      "name": "blk.0.ffn_gate.weight",
      "type": "F16",
      "shape": [
        768,
        3072
      ]
    },
    {
      "name": "blk.0.ffn_down.weight",
      "type": "F16",
      "shape": [
        3072,
        768
      ]
    },
    {
      "name": "blk.0.attn_output_norm.bias",
      "type": "F32",
      "shape": [
        768
      ]
    },
    {
      "name": "blk.0.attn_output_norm.weight",
      "type": "F32",
      "shape": [
        768
      ]
    },
    {
      "name": "blk.0.layer_output_norm.bias",
      "type": "F32",
      "shape": [
        768
      ]
    },
    {
      "name": "blk.0.layer_output_norm.weight",
      "type": "F32",
      "shape": [
        768
      ]
    },
    {
      "name": "blk.1.attn_qkv.weight",
      "type": "F16",
      "shape": [
        768,
        2304
      ]
    },
    {
      "name": "blk.1.attn_output.weight",
      "type": "F16",
      "shape": [
        768,
        768
      ]
    },
    {
      "name": "blk.1.ffn_up.weight",
      "type": "F16",
      "shape": [
        768,
        3072
      ]
    },
    {
      "name": "blk.1.ffn_gate.weight",
      "type": "F16",
      "shape": [
        768,
        3072
      ]
    },
    {
      "name": "blk.1.ffn_down.weight",
      "type": "F16",
      "shape": [
        3072,
        768
      ]
    },
    {
      "name": "blk.1.attn_output_norm.bias",
      "type": "F32",
      "shape": [
        768
      ]
    },
    {
      "name": "blk.1.attn_output_norm.weight",
      "type": "F32",
      "shape": [
        768
      ]
    },
    {
      "name": "blk.1.layer_output_norm.bias",
      "type": "F32",
      "shape": [
        768
      ]
    },
    {
      "name": "blk.1.layer_output_norm.weight",
      "type": "F32",
      "shape": [
        768
      ]
    },
    {
      "name": "blk.10.attn_qkv.weight",
      "type": "F16",
      "shape": [
        768,
        2304
      ]
    },
    {
      "name": "blk.10.attn_output.weight",
      "type": "F16",
      "shape": [
        768,
        768
      ]
    },
    {
      "name": "blk.10.ffn_up.weight",
      "type": "F16",
      "shape": [
        768,
        3072
      ]
    },
    {
      "name": "blk.10.ffn_gate.weight",
      "type": "F16",
      "shape": [
        768,
        3072
      ]
    },
    {
      "name": "blk.10.ffn_down.weight",
      "type": "F16",
      "shape": [
        3072,
        768
      ]
    },
    {
      "name": "blk.10.attn_output_norm.bias",
      "type": "F32",
      "shape": [
        768
      ]
    },
    {
      "name": "blk.10.attn_output_norm.weight",
      "type": "F32",
      "shape": [
        768
      ]
    },
    {
      "name": "blk.10.layer_output_norm.bias",
      "type": "F32",
      "shape": [
        768
      ]
    },
    {
      "name": "blk.10.layer_output_norm.weight",
      "type": "F32",
      "shape": [
        768
      ]
    },
    {
      "name": "blk.11.attn_qkv.weight",
      "type": "F16",
      "shape": [
        768,
        2304
      ]
    },
    {
      "name": "blk.11.attn_output.weight",
      "type": "F16",
      "shape": [
        768,
        768
      ]
    },
    {
      "name": "blk.11.ffn_up.weight",
      "type": "F16",
      "shape": [
        768,
        3072
      ]
    },
    {
      "name": "blk.11.ffn_gate.weight",
      "type": "F16",
      "shape": [
        768,
        3072
      ]
    },
    {
      "name": "blk.11.ffn_down.weight",
      "type": "F16",
      "shape": [
        3072,
        768
      ]
    },
    {
      "name": "blk.11.attn_output_norm.bias",
      "type": "F32",
      "shape": [
        768
      ]
    },
    {
      "name": "blk.11.attn_output_norm.weight",
      "type": "F32",
      "shape": [
        768
      ]
    },
    {
      "name": "blk.11.layer_output_norm.bias",
      "type": "F32",
      "shape": [
        768
      ]
    },
    {
      "name": "blk.11.layer_output_norm.weight",
      "type": "F32",
      "shape": [
        768
      ]
    },
    {
      "name": "blk.2.attn_qkv.weight",
      "type": "F16",
      "shape": [
        768,
        2304
      ]
    },
    {
      "name": "blk.2.attn_output.weight",
      "type": "F16",
      "shape": [
        768,
        768
      ]
    },
    {
      "name": "blk.2.ffn_up.weight",
      "type": "F16",
      "shape": [
        768,
        3072
      ]
    },
    {
      "name": "blk.2.ffn_gate.weight",
      "type": "F16",
      "shape": [
        768,
        3072
      ]
    },
    {
      "name": "blk.2.ffn_down.weight",
      "type": "F16",
      "shape": [
        3072,
        768
      ]
    },
    {
      "name": "blk.2.attn_output_norm.bias",
      "type": "F32",
      "shape": [
        768
      ]
    },
    {
      "name": "blk.2.attn_output_norm.weight",
      "type": "F32",
      "shape": [
        768
      ]
    },
    {
      "name": "blk.2.layer_output_norm.bias",
      "type": "F32",
      "shape": [
        768
      ]
    },
    {
      "name": "blk.2.layer_output_norm.weight",
      "type": "F32",
      "shape": [
        768
      ]
    },
    {
      "name": "blk.3.attn_qkv.weight",
      "type": "F16",
      "shape": [
        768,
        2304
      ]
    },
    {
      "name": "blk.3.attn_output.weight",
      "type": "F16",
      "shape": [
        768,
        768
      ]
    },
    {
      "name": "blk.3.ffn_up.weight",
      "type": "F16",
      "shape": [
        768,
        3072
      ]
    },
    {
      "name": "blk.3.ffn_gate.weight",
      "type": "F16",
      "shape": [
        768,
        3072
      ]
    },
    {
      "name": "blk.3.ffn_down.weight",
      "type": "F16",
      "shape": [
        3072,
        768
      ]
    },
    {
      "name": "blk.3.attn_output_norm.bias",
      "type": "F32",
      "shape": [
        768
      ]
    },
    {
      "name": "blk.3.attn_output_norm.weight",
      "type": "F32",
      "shape": [
        768
      ]
    },
    {
      "name": "blk.3.layer_output_norm.bias",
      "type": "F32",
      "shape": [
        768
      ]
    },
    {
      "name": "blk.3.layer_output_norm.weight",
      "type": "F32",
      "shape": [
        768
      ]
    },
    {
      "name": "blk.4.attn_qkv.weight",
      "type": "F16",
      "shape": [
        768,
        2304
      ]
    },
    {
      "name": "blk.4.attn_output.weight",
      "type": "F16",
      "shape": [
        768,
        768
      ]
    },
    {
      "name": "blk.4.ffn_up.weight",
      "type": "F16",
      "shape": [
        768,
        3072
      ]
    },
    {
      "name": "blk.4.ffn_gate.weight",
      "type": "F16",
      "shape": [
        768,
        3072
      ]
    },
    {
      "name": "blk.4.ffn_down.weight",
      "type": "F16",
      "shape": [
        3072,
        768
      ]
    },
    {
      "name": "blk.4.attn_output_norm.bias",
      "type": "F32",
      "shape": [
        768
      ]
    },
    {
      "name": "blk.4.attn_output_norm.weight",
      "type": "F32",
      "shape": [
        768
      ]
    },
    {
      "name": "blk.4.layer_output_norm.bias",
      "type": "F32",
      "shape": [
        768
      ]
    },
    {
      "name": "blk.4.layer_output_norm.weight",
      "type": "F32",
      "shape": [
        768
      ]
    },
    {
      "name": "blk.5.attn_qkv.weight",
      "type": "F16",
      "shape": [
        768,
        2304
      ]
    },
    {
      "name": "blk.5.attn_output.weight",
      "type": "F16",
      "shape": [
        768,
        768
      ]
    },
    {
      "name": "blk.5.ffn_up.weight",
      "type": "F16",
      "shape": [
        768,
        3072
      ]
    },
    {
      "name": "blk.5.ffn_gate.weight",
      "type": "F16",
      "shape": [
        768,
        3072
      ]
    },
    {
      "name": "blk.5.ffn_down.weight",
      "type": "F16",
      "shape": [
        3072,
        768
      ]
    },
    {
      "name": "blk.5.attn_output_norm.bias",
      "type": "F32",
      "shape": [
        768
      ]
    },
    {
      "name": "blk.5.attn_output_norm.weight",
      "type": "F32",
      "shape": [
        768
      ]
    },
    {
      "name": "blk.5.layer_output_norm.bias",
      "type": "F32",
      "shape": [
        768
      ]
    },
    {
      "name": "blk.5.layer_output_norm.weight",
      "type": "F32",
      "shape": [
        768
      ]
    },
    {
      "name": "blk.6.attn_qkv.weight",
      "type": "F16",
      "shape": [
        768,
        2304
      ]
    },
    {
      "name": "blk.6.attn_output.weight",
      "type": "F16",
      "shape": [
        768,
        768
      ]
    },
    {
      "name": "blk.6.ffn_up.weight",
      "type": "F16",
      "shape": [
        768,
        3072
      ]
    },
    {
      "name": "blk.6.ffn_gate.weight",
      "type": "F16",
      "shape": [
        768,
        3072
      ]
    },
    {
      "name": "blk.6.ffn_down.weight",
      "type": "F16",
      "shape": [
        3072,
        768
      ]
    },
    {
      "name": "blk.6.attn_output_norm.bias",
      "type": "F32",
      "shape": [
        768
      ]
    },
    {
      "name": "blk.6.attn_output_norm.weight",
      "type": "F32",
      "shape": [
        768
      ]
    },
    {
      "name": "blk.6.layer_output_norm.bias",
      "type": "F32",
      "shape": [
        768
      ]
    },
    {
      "name": "blk.6.layer_output_norm.weight",
      "type": "F32",
      "shape": [
        768
      ]
    },
    {
      "name": "blk.7.attn_qkv.weight",
      "type": "F16",
      "shape": [
        768,
        2304
      ]
    },
    {
      "name": "blk.7.attn_output.weight",
      "type": "F16",
      "shape": [
        768,
        768
      ]
    },
    {
      "name": "blk.7.ffn_up.weight",
      "type": "F16",
      "shape": [
        768,
        3072
      ]
    },
    {
      "name": "blk.7.ffn_gate.weight",
      "type": "F16",
      "shape": [
        768,
        3072
      ]
    },
    {
      "name": "blk.7.ffn_down.weight",
      "type": "F16",
      "shape": [
        3072,
        768
      ]
    },
    {
      "name": "blk.7.attn_output_norm.bias",
      "type": "F32",
      "shape": [
        768
      ]
    },
    {
      "name": "blk.7.attn_output_norm.weight",
      "type": "F32",
      "shape": [
        768
      ]
    },
    {
      "name": "blk.7.layer_output_norm.bias",
      "type": "F32",
      "shape": [
        768
      ]
    },
    {
      "name": "blk.7.layer_output_norm.weight",
      "type": "F32",
      "shape": [
        768
      ]
    },
    {
      "name": "blk.8.attn_qkv.weight",
      "type": "F16",
      "shape": [
        768,
        2304
      ]
    },
    {
      "name": "blk.8.attn_output.weight",
      "type": "F16",
      "shape": [
        768,
        768
      ]
    },
    {
      "name": "blk.8.ffn_up.weight",
      "type": "F16",
      "shape": [
        768,
        3072
      ]
    },
    {
      "name": "blk.8.ffn_gate.weight",
      "type": "F16",
      "shape": [
        768,
        3072
      ]
    },
    {
      "name": "blk.8.ffn_down.weight",
      "type": "F16",
      "shape": [
        3072,
        768
      ]
    },
    {
      "name": "blk.8.attn_output_norm.bias",
      "type": "F32",
      "shape": [
        768
      ]
    },
    {
      "name": "blk.8.attn_output_norm.weight",
      "type": "F32",
      "shape": [
        768
      ]
    },
    {
      "name": "blk.8.layer_output_norm.bias",
      "type": "F32",
      "shape": [
        768
      ]
    },
    {
      "name": "blk.8.layer_output_norm.weight",
      "type": "F32",
      "shape": [
        768
      ]
    },
    {
      "name": "blk.9.attn_qkv.weight",
      "type": "F16",
      "shape": [
        768,
        2304
      ]
    },
    {
      "name": "blk.9.attn_output.weight",
      "type": "F16",
      "shape": [
        768,
        768
      ]
    },
    {
      "name": "blk.9.ffn_up.weight",
      "type": "F16",
      "shape": [
        768,
        3072
      ]
    },
    {
      "name": "blk.9.ffn_gate.weight",
      "type": "F16",
      "shape": [
        768,
        3072
      ]
    },
    {
      "name": "blk.9.ffn_down.weight",
      "type": "F16",
      "shape": [
        3072,
        768
      ]
    },
    {
      "name": "blk.9.attn_output_norm.bias",
      "type": "F32",
      "shape": [
        768
      ]
    },
    {
      "name": "blk.9.attn_output_norm.weight",
      "type": "F32",
      "shape": [
        768
      ]
    },
    {
      "name": "blk.9.layer_output_norm.bias",
      "type": "F32",
      "shape": [
        768
      ]
    },
    {
      "name": "blk.9.layer_output_norm.weight",
      "type": "F32",
      "shape": [
        768
      ]
    }
  ],
  "capabilities": [
    "embedding"
  ],
  "modified_at": "2026-04-11T04:15:03.46833539Z"
}
384
768
INFO:     Started server process [10]
INFO:     Waiting for application startup.
ERROR:main_brain.startup:[STARTUP] DB init failed: unable to open database file
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:8050 (Press CTRL+C to quit)

