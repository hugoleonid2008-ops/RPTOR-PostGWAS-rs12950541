#!/usr/bin/env python3
"""
Query RNAct database for RPTOR transcript RNA-protein interactions.
RNAct URL: https://rnact.crg.eu/

NOTE: RNAct does not have a public API. Queries must be performed manually through the web interface.
This script documents the parameters and instructions for manual query execution.
"""

# Manual query instructions for RNAct database:
#
# Step 1: Open RNAct (https://rnact.crg.eu/)
# Step 2: Search for RPTOR-201 canonical transcript
#    - Transcript ID: ENST00000306801
#    - Select prediction score >= 1.0
#    - Download page 1 results
#    - Save as: rnact_ENST00000306801_page1.csv
#
# Step 3: Search for RPTOR-208 NMD isoform transcript
#    - Transcript ID: ENST00000574767
#    - Select prediction score >= 1.5 (more stringent threshold for shorter transcript)
#    - Download page 1 results
#    - Save as: rnact_ENST00000574767_page1.csv
#
# Step 4: Consolidate interaction lists
#    - Extract protein accessions from both files
#    - Create unified lists for functional annotation
#
# Step 5: Submit to ToppGene for enrichment
#    - Go to https://toppgene.cchmc.org/
#    - Upload protein lists
#    - Analyze functional enrichment and pathways

TRANSCRIPTS = {
    "RPTOR-201": {
        "id": "ENST00000306801",
        "biotype": "protein_coding",
        "length_bp": 6838,
        "protein_aa": 1335,
        "score_threshold": 1.0,
        "n_interactions": 100,
        "description": "Canonical RPTOR transcript"
    },
    "RPTOR-208": {
        "id": "ENST00000574767",
        "biotype": "nonsense_mediated_decay",
        "length_bp": 2461,
        "protein_aa": 95,
        "score_threshold": 1.5,
        "n_interactions": 100,
        "description": "RPTOR isoform subject to nonsense-mediated decay (NMD)"
    }
}

def print_query_instructions():
    """Print RNAct query parameters and instructions."""
    print("=" * 80)
    print("RNAct Query Instructions for RPTOR Transcripts")
    print("=" * 80)
    print()

    print("Database URL: https://rnact.crg.eu/")
    print()

    for name, info in TRANSCRIPTS.items():
        print(f"\nTranscript: {name}")
        print(f"  Ensembl ID: {info['id']}")
        print(f"  Biotype: {info['biotype']}")
        print(f"  Description: {info['description']}")
        print(f"  Length: {info['length_bp']} bp ({info['protein_aa']} amino acids)")
        print(f"  Prediction Score Threshold: >= {info['score_threshold']}")
        print(f"  Expected Interactions: ~{info['n_interactions']}")
        print(f"  Output File: rnact_{info['id']}_page1.csv")

    print("\n" + "=" * 80)
    print("Query Steps:")
    print("=" * 80)
    print("""
1. Open RNAct at https://rnact.crg.eu/
2. For each transcript:
   a. Paste the Ensembl ID in the search box
   b. Click "Search" or submit the query
   c. Filter results by prediction score (see thresholds above)
   d. Select and download page 1 results as CSV
   e. Save with filename: rnact_[ENST_ID]_page1.csv
3. Place downloaded CSV files in: ../data/ directory
4. For enrichment analysis, submit protein lists to ToppGene:
   - Visit https://toppgene.cchmc.org/
   - Upload consolidated protein lists
   - Analyze Gene Ontology, pathway, and disease enrichment
    """)

if __name__ == "__main__":
    print_query_instructions()

    print("\n" + "=" * 80)
    print("Next Steps After RNAct Queries:")
    print("=" * 80)
    print("""
After downloading RNAct results:

1. Extract protein accessions from CSV files:
   cut -d',' -f2 rnact_ENST00000306801_page1.csv | sort | uniq > proteins_RPTOR201.txt
   cut -d',' -f2 rnact_ENST00000574767_page1.csv | sort | uniq > proteins_RPTOR208.txt

2. Submit to ToppGene Suite for enrichment:
   - Visit https://toppgene.cchmc.org/
   - Upload protein lists (convert to gene names/accessions as needed)
   - Download enrichment results

3. Save ToppGene results as:
   - toppgene_ENST00000306801_enrichment.txt
   - toppgene_ENST00000574767_enrichment.txt
    """)
