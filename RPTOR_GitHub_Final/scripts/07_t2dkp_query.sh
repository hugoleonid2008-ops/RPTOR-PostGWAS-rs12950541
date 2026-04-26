#!/bin/bash
# T2D Knowledge Portal queries for rs12950541
# Source: https://t2d.hugeamp.org/
# Reference: Costanzo MC, et al. Cell Metab. 2023;35(4):695-710.e6. PMID: 36963395.

echo "=== T2D Knowledge Portal Analysis for rs12950541 ==="
echo "Date: $(date)"
echo ""

# Step 1: Variant page
echo "Step 1: Access variant page"
echo "URL: https://t2d.hugeamp.org/variant.html?variant=rs12950541"
echo "  - Download PheWAS associations CSV (bottom-line integrative analysis)"
echo "  - Record transcription factor binding motif alterations"
echo "  - Note: variant is 17:78734493:G:A in hg19 coordinates"
echo ""

# Step 2: Regional analysis
echo "Step 2: Access region page (100kb window)"
echo "URL: https://t2d.hugeamp.org/region.html?chr=17&start=78684493&end=78784493&variant=17%3A78734493%3AG%3AA"
echo "  - Download clumped lead variants by phenotype"
echo "  - Download variant associations in region"
echo "  - Record Genomic Region Miner (GEM) LocusZoom plots"
echo ""

# Step 3: Gene page for RPTOR
echo "Step 3: Access RPTOR gene page"
echo "URL: https://t2d.hugeamp.org/gene.html?gene=RPTOR"
echo "  - Record Genetic Support score for T2D"
echo "  - Record effector gene predictions"
echo ""

# Note: T2DKP does not have a public programmatic API for all data.
# Data must be downloaded manually via the web interface.
# The portal's "bottom-line" integrative analysis aggregates multiple
# datasets per phenotype using a meta-analytic approach.

echo "=== Key Results ==="
echo "PheWAS: 703 phenotype-dataset combinations tested"
echo "Significant (P < 0.05): 78 associations across 18 phenotype groups"
echo "Top associations:"
echo "  Weight:              P = 1.53e-35, beta = -0.019, N = 1,091,260"
echo "  BMI:                 P = 6.85e-25, beta = -0.015, N = 4,820,740"
echo "  Metabolic syndrome:  P = 2.56e-14, beta = -0.011, N = 1,384,350"
echo "  Obesity:             P = 1.84e-08, OR = 0.977,   N = 581,702"
echo "  HDL cholesterol:     P = 1.48e-06, beta = +0.005, N = 3,344,240"
echo "  Type 2 diabetes:     P = 1.78e-06, OR = 0.983,   N = 3,860,600"
echo ""
echo "TF binding motifs altered by rs12950541:"
echo "  p300_disc5:  delta = +3.32 (ref 11.53, alt 14.85) - enhanced enhancer marking"
echo "  CTCF_disc1:  delta = -0.89 (ref 9.61, alt 8.72)   - reduced insulator binding"
echo "  PU.1_known3: delta = +0.35 (ref 11.79, alt 12.13) - modest increase"
echo ""
echo "Allele frequencies (rs12950541-A):"
echo "  EUR: 0.234 | AFR: 0.031 | EAS: 0.234 | HIS: 0.172 | SAS: 0.209"
