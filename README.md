# RPTOR-PostGWAS-rs12950541

[![DOI](https://img.shields.io/badge/bioRxiv-10.64898%2F2026.04.26.720864-blue)](https://doi.org/10.64898/2026.04.26.720864)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

Reproducibility repository for post-GWAS functional annotation of rs12950541 at the RPTOR locus.

## Preprint

**Gallardo-Blanco HL** (2026). Post-GWAS functional annotation of the RPTOR locus identifies rs12950541 as a candidate regulatory variant for type 2 diabetes and metabolic traits. *bioRxiv*. doi: [10.64898/2026.04.26.720864](https://doi.org/10.64898/2026.04.26.720864)

## Overview

This study applies a systematic 10-stage post-GWAS functional annotation pipeline (Pipeline PostGWAS Gallardo v1) to characterize rs12950541 (chr17:80760693 G>A) at the RPTOR locus, encoding Raptor, a scaffold protein critical for mTORC1 signaling and beta-cell function.

### Key Findings

- **RPTOR** ranked #1 L2G gene across all 31 GWAS credible sets (mean score 0.428)
- **1,047 GWAS-GWAS colocalizations** with adiposity traits (mean H4 = 0.975)
- **eQTL gap**: zero GWAS-QTL colocalizations in pancreatic islets, adipose, or liver
- **140 LD partners** — 100% non-coding (MODIFIER impact), including 24 regulatory region variants
- **Novel RPTOR-208/ABCC8 RNA-protein interaction** linking mTORC1 to sulfonylurea receptor biology
- **78 PheWAS associations** across 18 phenotype groups (insulin response, HDL, hepatic enzymes, sleep)
- rs12950541 enhances **p300 enhancer marking** while reducing **CTCF insulator binding**

### Seven Convergent Lines of Evidence

1. L2G prioritization (RPTOR #1 in 31/31 credible sets)
2. GWAS-GWAS colocalization with adiposity
3. eQTL gap in metabolic tissues
4. VEP: exclusively non-coding regulatory variants
5. Novel RNA-protein interaction (RPTOR-208 / ABCC8)
6. Druggable targets (ABCC8: CHEMBL2071, sulfonylureas)
7. PheWAS: 78 associations with TF binding motif changes (p300 gain / CTCF loss)

## Repository Structure

```
RPTOR-PostGWAS-rs12950541/
├── Manuscript/
│   └── RPTOR_PostGWAS_Manuscript_v7.docx
├── RPTOR_GitHub_Final/
│   ├── scripts/
│   │   ├── 01_open_targets_credible_sets.graphql
│   │   ├── 02_open_targets_colocalizations.graphql
│   │   ├── 03_vep_analysis.sh
│   │   ├── 04_rnact_query.py
│   │   ├── 05_chembl_target_query.py
│   │   ├── 06_pubmed_novelty_search.sh
│   │   └── 07_t2dkp_query.sh
│   ├── data/
│   │   └── README.md
│   ├── supplementary/
│   │   ├── Table_S1_RPTOR_Transcripts.csv
│   │   ├── Table_S2_GWAS_Credible_Sets.csv
│   │   ├── Table_S3_Colocalizations.csv
│   │   ├── Table_S4_RNAct_Interactions.csv
│   │   └── Table_S5_T2DKP_PheWAS.csv
│   └── figures/
│       ├── Figure1_Pipeline.svg
│       └── Figure1_Pipeline.html
├── LICENSE
└── README.md
```

## Pipeline PostGWAS Gallardo v1

The 10-stage pipeline used in this study:

| Stage | Analysis | Tool/Database |
|-------|----------|---------------|
| 1 | Credible set analysis | Open Targets Platform v24.12 |
| 2 | L2G scoring | Open Targets L2G model |
| 3 | GWAS-GWAS colocalization | Open Targets (coloc) |
| 4 | GWAS-QTL colocalization | Open Targets (QTL) |
| 5 | Tissue-specific QTL mapping | GTEx v8 / Open Targets |
| 6 | Variant Effect Prediction | Ensembl VEP |
| 7 | LD block characterization | Ensembl VEP (D' >= 0.7) |
| 8 | RNA-protein interactions | RNAct / catRAPID |
| 9 | Drug target analysis | ChEMBL |
| 10 | Phenome-wide associations | T2D Knowledge Portal |

## Data Availability

All data used in this study are publicly available from:

- [Open Targets Platform](https://platform.opentargets.org/) (v24.12)
- [Ensembl VEP](https://www.ensembl.org/Tools/VEP)
- [RNAct/catRAPID](https://rnact.crg.eu/)
- [ChEMBL](https://www.ebi.ac.uk/chembl/)
- [T2D Knowledge Portal](https://t2d.hugeamp.org/)
- [GWAS Catalog](https://www.ebi.ac.uk/gwas/)
- [PubMed](https://pubmed.ncbi.nlm.nih.gov/)

## Citation

If you use this pipeline or data, please cite:

```bibtex
@article{gallardo-blanco_2026_rptor,
  author  = {Gallardo-Blanco, Hugo Leonid},
  title   = {Post-GWAS functional annotation of the RPTOR locus identifies rs12950541 as a candidate regulatory variant for type 2 diabetes and metabolic traits},
  journal = {bioRxiv},
  year    = {2026},
  doi     = {10.64898/2026.04.26.720864},
  url     = {https://doi.org/10.64898/2026.04.26.720864}
}
```

## Related Work

This is part of a systematic series applying Pipeline PostGWAS Gallardo v1 to T2D GWAS loci:

- **RPTOR** (rs12950541) — this repository | [bioRxiv](https://doi.org/10.64898/2026.04.26.720864)
- **ANKRD55** (rs459193) — [GitHub](https://github.com/hugoleonid2008-ops) | bioRxiv (forthcoming)
- **TCF7L2** (rs7903146) — forthcoming
- **Cross-loci comparative** (10 loci) — forthcoming

## License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.

## Contact

**Hugo Leonid Gallardo-Blanco**
Servicio de Oncologia, Centro Universitario Contra el Cancer (CUCC)
Hospital Universitario "Dr. Jose Eleuterio Gonzalez"
Universidad Autonoma de Nuevo Leon, Monterrey, NL, Mexico
Email: hugoleonid2008@gmail.com
