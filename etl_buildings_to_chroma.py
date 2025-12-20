import psycopg2
import numpy as np
import chromadb

PG_HOST = "localhost"
PG_DB   = "msjarvis_gis"
PG_USER = "postgres"

CHROMA_COLLECTION = "building_footprint_wvgistc_v1"


def fetch_building_features():
    conn = psycopg2.connect(
        host=PG_HOST,
        dbname=PG_DB,
        user=PG_USER,
    )
    cur = conn.cursor()
    cur.execute("""
        SELECT worldview_id, log_area, confidence_norm, is_residential
        FROM public.building_features_v1;
    """)
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return rows


def main():
    print("Fetching building features from Postgres...")
    rows = fetch_building_features()
    print(f"Fetched {len(rows)} rows from building_features_v1")

    if not rows:
        print("No rows fetched; aborting ETL.")
        return

    worldview_ids = []
    vectors = []

    for wid, log_area, conf_norm, is_res in rows:
        worldview_ids.append(str(wid))
        vec = np.array([
            float(log_area or 0.0),
            float(conf_norm or 0.0),
            float(is_res or 0.0),
        ], dtype=float)
        vectors.append(vec.tolist())

    print("Initializing Chroma client...")
    client = chromadb.Client()
    print("Creating or getting collection...")
    collection = client.get_or_create_collection(
        name=CHROMA_COLLECTION,
        metadata={
            "entity_type": "building_footprint_wvgistc",
            "version": "v1",
        },
    )
    print("Collection ready.")

    batch_size = 1000
    total = len(worldview_ids)
    for i in range(0, total, batch_size):
        ids_batch = worldview_ids[i:i + batch_size]
        vec_batch = vectors[i:i + batch_size]

        collection.upsert(
            ids=ids_batch,
            embeddings=vec_batch,
            metadatas=[
                {"entity_type": "building_footprint_wvgistc"}
            ] * len(ids_batch),
        )
        if (i // batch_size) % 100 == 0:
            print(f"Upserted {i + len(ids_batch)} / {total} vectors")

    print("ETL complete.")


if __name__ == "__main__":
    main()
