# RPTOR Post-GWAS Functional Annotation Repository

**Author:** Hugo Leonid Gallardo-Blanco

**Affiliation:** Servicio de Oncologia, CUCC, Hospital Universitario, UANL

## Citation

**Preprint:** Gallardo-Blanco HL. Post-GWAS functional annotation of the RPTOR locus identifies rs12950541 as a candidate regulatory variant for type 2 diabetes and metabolic traits. bioRxiv. 2026. DOI: [to be added upon posting]

## Overview

This repository contains the reproducible analysis pipeline for post-GWAS functional annotation of RPTOR (regulatory-associated protein of mTOR complex 1) and its interactions with ABCC8 (ATP-binding cassette subfamily C member 8, also known as sulfonylurea receptor 1/SUR1). The study integrates variant effect prediction, regulatory annotation, RNA-protein interaction data, and drug target information to identify novel functional mechanisms linking RPTOR variants to metabolic and oncogenic phenotypes.

## Quick Start

The repository contains seven analysis scripts that work together to reproduce the complete functional annotation:

- **01_open_targets_credible_sets.graphql** — Query GWAS credible sets and locus-specific genetic associations from Open Targets Platform
- **02_open_targets_colocalizations.graphql** — Retrieve colocalization analyses linking genetic and expression QTL signals
- **03_vep_analysis.sh** — Predict molecular consequences of variants using Ensembl VEP with CADD and SpliceAI scores
- **04_rnact_query.py** — Identify RNA-binding protein interactions on RPTOR transcripts via RNAct predictions
- **05_chembl_target_query.py** — Retrieve drug target and mechanism of action information for ABCC8 and RPTOR
- **06_pubmed_novelty_search.sh** — Verify novelty of RPTOR-ABCC8 associations in the published literature
- **07_t2dkp_query.sh** — Query T2D Knowledge Portal for PheWAS associations, regional variants, and transcription factor binding sites

## Study Description

Genome-wide association studies (GWAS) have identified numerous genetic variants associated with complex diseases, but the functional mechanisms underlying these associations remain largely unexplored. This project combines multi-database functional annotation to:

1. **Characterize RPTOR variants** identified in GWAS through credible sets and colocalization analyses
2. **Predict molecular consequences** using Variant Effect Predictor (VEP) and effect scores (CADD, SpliceAI, dbNSFP)
3. **Identify RNA-protein interactions** through RNAct predictions on RPTOR transcripts
4. **Assess therapeutic relevance** by connecting RPTOR to drug targets (ABCC8/SUR1)
5. **Determine tissue-specific expression** and functional networks through GTEx and ToppGene enrichment

## Data Sources

All analyses use publicly available databases and tools:

- **Open Targets Platform v24.12**: Genetic associations, credible sets, colocalization analyses
  - URL: https://platform.opentargets.org/
  - GraphQL API for programmatic access

- **Ensembl VEP release 105**: Variant effect prediction with regulatory annotations
  - URL: https://www.ensembl.org/Tools/VEP
  - Plugins: CADD, SpliceAI, dbNSFP

- **RNAct**: RNA-protein interaction predictions
  - URL: https://rnact.crg.eu/
  - Prediction scores based on catRAPID algorithm

- **ChEMBL**: Drug target information and mechanisms of action
  - URL: https://www.ebi.ac.uk/chembl/
  - REST API for target queries

- **GTEx v8**: Tissue-specific gene expression
  - URL: https://gtexportal.org/
  - Expression quantitative trait loci (eQTLs)

- **ToppGene Suite**: Functional enrichment analysis
  - URL: https://toppgene.cchmc.org/
  - Gene annotation and pathway analysis

- **T2D Knowledge Portal (T2DKP)**: PheWAS, regional analysis, transcription factor binding motifs
  - URL: https://t2d.hugeamp.org/
  - Bottom-line integrative analysis aggregating 703 phenotype-dataset combinations

## Repository Structure

```
RPTOR_GitHub_Final/
├── README.md                           # This file
├── LICENSE                             # Dual licensing (CC-BY 4.0 for data, MIT for code)
├── scripts/
│   ├── 01_open_targets_credible_sets.graphql    # Query credible sets from Open Targets
│   ├── 02_open_targets_colocalizations.graphql  # Query colocalizations from Open Targets
│   ├── 03_vep_analysis.sh                       # Variant Effect Predictor analysis pipeline
│   ├── 04_rnact_query.py                        # RNAct transcript interaction queries
│   ├── 05_chembl_target_query.py                # ChEMBL drug target queries
│   ├── 06_pubmed_novelty_search.sh              # PubMed novelty verification searches
│   └── 07_t2dkp_query.sh                        # T2D Knowledge Portal PheWAS and regional analysis
├── data/
│   └── README.md                       # Data directory documentation
├── supplementary/
│   ├── Table_S1_RPTOR_Transcripts.csv           # Supplementary Table S1: RPTOR transcript annotations
│   ├── Table_S2_GWAS_Credible_Sets.csv         # Supplementary Table S2: GWAS credible sets
│   ├── Table_S3_Colocalizations.csv            # Supplementary Table S3: Colocalization results
│   ├── Table_S4_RNAct_Interactions.csv         # Supplementary Table S4: RNA-protein interactions
│   └── Table_S5_T2DKP_PheWAS.csv               # Supplementary Table S5: PheWAS associations
└── figures/
    ├── Figure1_Pipeline.svg                     # Analysis pipeline schematic
    └── Figure1_Pipeline.html                    # Interactive pipeline figure
```

## Supplementary Tables

- **Table S1**: RPTOR transcript annotations including transcript IDs, lengths, protein products, and biotypes
- **Table S2**: GWAS credible sets for variants at the RPTOR locus from Open Targets Platform
- **Table S3**: Colocalization analyses linking GWAS signals to expression QTLs
- **Table S4**: RNAct predictions for RNA-binding protein interactions on RPTOR transcripts
- **Table S5**: PheWAS associations for the RPTOR lead variant from T2D Knowledge Portal

## How to Reproduce the Analyses

### Prerequisites

- Python 3.8+
- Bash shell
- curl command-line tool
- Variant Effect Predictor (VEP) release 105 with plugins
- Optional: R for statistical analysis

### Step 1: Query Open Targets Platform

Use GraphQL queries to retrieve credible set and colocalization information:

```bash
# Query credible sets
cd scripts
cat 01_open_targets_credible_sets.graphql

# Query colocalizations
cat 02_open_targets_colocalizations.graphql

# Alternatively, use curl to submit to Open Targets GraphQL endpoint:
curl -X POST https://api.platform.opentargets.org/graphql \
  -H "Content-Type: application/json" \
  -d @01_open_targets_credible_sets.graphql
```

### Step 2: Variant Effect Prediction

Run the VEP analysis pipeline on RPTOR LD block variants:

```bash
bash 03_vep_analysis.sh

# This will:
# 1. Query Ensembl REST API for LD partners of rs12950541
# 2. Extract variant IDs for annotation
# 3. Run VEP with CADD, SpliceAI, and dbNSFP predictions
# 4. Generate regulatory annotation
```

Output: `vep_output.txt` containing predicted consequences for all variants in the LD block

### Step 3: Query RNA-Protein Interactions

RNAct database does not offer a public API, so queries must be performed manually:

```bash
cd ../scripts
python3 04_rnact_query.py

# Instructions:
# 1. Visit https://rnact.crg.eu/
# 2. Search for ENST00000306801 (RPTOR-201 canonical), download page 1 with score >= 1.0
# 3. Search for ENST00000574767 (RPTOR-208 NMD isoform), download page 1 with score >= 1.5
# 4. Save to ../data/ directory as specified
# 5. Submit protein lists to ToppGene (https://toppgene.cchmc.org/) for enrichment
```

### Step 4: Query ChEMBL Drug Targets

Retrieve drug target information for ABCC8 and RPTOR:

```bash
python3 05_chembl_target_query.py

# This script will output:
# - Target information for ABCC8 (CHEMBL2071)
# - Target information for RPTOR (CHEMBL3120040)
# - Mechanisms of action for ABCC8
```

### Step 5: Novelty Verification

Verify novelty of RPTOR-ABCC8 link through PubMed searches:

```bash
bash 06_pubmed_novelty_search.sh

# Search results indicate:
# - No direct RPTOR-ABCC8 associations in literature (as of April 2026)
# - Known mTOR-KATP channel interactions in beta cells (key supporting evidence)
```

### Step 6: T2D Knowledge Portal Analysis

Retrieve PheWAS associations, regional variant data, and transcription factor binding motif information:

```bash
bash 07_t2dkp_query.sh

# This script documents manual steps for:
# 1. Variant page: https://t2d.hugeamp.org/variant.html?variant=rs12950541
# 2. Regional analysis: https://t2d.hugeamp.org/region.html (100kb window)
# 3. Gene page: https://t2d.hugeamp.org/gene.html?gene=RPTOR
#
# Key outputs:
# - PheWAS associations: 703 phenotype-dataset combinations tested
# - Significant hits: 78 associations (P < 0.05) across 18 phenotype groups
# - Top hit: Weight phenotype (P = 1.53e-35, beta = -0.019)
# - TF binding motif changes in p300, CTCF, and PU.1 binding sites
```

## Key Findings

### RPTOR Variant (rs12950541)

- **Chromosome:** 17
- **Position:** 80,760,693
- **Alleles:** G/A
- **LD Block:** Contains multiple variants with predicted regulatory consequences
- **Associated Traits:** Metabolic phenotypes, diabetes risk, cancer susceptibility

### RPTOR Transcripts

RPTOR is transcribed into 12 distinct isoforms with varying structures and biotypes (see Table S1):

| Transcript | ID | Biotype | Protein Product |
|-----------|----|---------|----|
| RPTOR-201 | ENST00000306801 | protein_coding | 1335 aa (canonical) |
| RPTOR-202 | ENST00000544334 | protein_coding | 1177 aa |
| RPTOR-203 | ENST00000570891 | protein_coding | 379 aa |
| RPTOR-210 | ENST00000576366 | protein_coding | 235 aa |
| RPTOR-208 | ENST00000574767 | nonsense_mediated_decay | 95 aa |
| RPTOR-209 | ENST00000575542 | processed_transcript | None |

### RNA-Protein Interactions

Two RPTOR transcripts were analyzed for RNA-binding protein interactions (Table S4):

| Transcript | ID | Biotype | Interactions Found | Score Threshold |
|-----------|----|---------|--------------------|-----------------|
| RPTOR-201 | ENST00000306801 | protein_coding | ~100 | ≥1.0 |
| RPTOR-208 | ENST00000574767 | nonsense_mediated_decay | ~100 | ≥1.5 |

### Drug Target: ABCC8 (SUR1)

- **ChEMBL ID:** CHEMBL2071
- **Type:** Ion channel (sulfonylurea receptor)
- **Key Mechanism:** Modulation of ATP-sensitive K+ channels
- **Clinical Relevance:** Diabetes treatment (sulfonylurea drugs)
- **Novel Connection:** RPTOR regulation may influence KATP channel function

### Enriched Pathways

ToppGene functional enrichment analysis reveals RPTOR interactors participate in:
- mTOR signaling
- Protein synthesis regulation
- Cell growth and proliferation
- Metabolic homeostasis
- Cancer-related pathways

## Reproducibility Notes

1. **Data Availability:** All source data comes from publicly accessible databases
2. **Version Control:** Specific database versions/release dates are documented
3. **Code:** All scripts are designed to be executable with minimal modifications
4. **Computational Requirements:** Modest (suitable for desktop/laptop execution)
5. **Estimated Runtime:**
   - Open Targets queries: <5 minutes
   - VEP analysis: 15-30 minutes depending on variant count
   - Manual RNAct queries: 20-30 minutes
   - ChEMBL queries: <5 minutes
   - T2D Knowledge Portal queries: 15-20 minutes (manual web interface)
   - Total time: ~1.5-2.5 hours

## License

This repository uses dual licensing to accommodate both data and code components:

- **Data License:** Creative Commons Attribution 4.0 International (CC-BY 4.0)
  - All data files, tables, and analysis results are released under CC-BY 4.0
  - Attribution required; permits modification and reuse

- **Code License:** MIT License
  - All scripts and code are released under MIT
  - Permits commercial use, modification, and distribution

See `LICENSE` file for full text of both licenses.

## Contact & Support

**Author:** Hugo Leonid Gallardo-Blanco
**Institution:** Servicio de Oncologia, CUCC, Hospital Universitario, UANL
**Email:** [Contact information]

For issues, questions, or suggestions about reproducing the analyses, please refer to the individual script documentation and external tool documentation:

- Open Targets Platform: https://platform.opentargets.org/
- Ensembl VEP: https://www.ensembl.org/Tools/VEP
- RNAct: https://rnact.crg.eu/
- ChEMBL: https://www.ebi.ac.uk/chembl/
- GTEx: https://gtexportal.org/
- ToppGene: https://toppgene.cchmc.org/

## Changelog

**Version 1.0 (April 2026)**
- Initial release with GraphQL queries, VEP pipeline, and functional enrichment analyses
- Comprehensive documentation for reproducibility
- All scripts tested with public database versions as of April 2026
- Complete supplementary tables (S1-S5) and pipeline figures included
