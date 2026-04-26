#!/bin/bash
# Variant Effect Predictor analysis for rs12950541 LD block
# Requires: Ensembl VEP release 105, CADD, SpliceAI, dbNSFP plugins

# Step 1: Get LD partners from Ensembl REST API
curl -s "https://rest.ensembl.org/ld/human/rs12950541/1000GENOMES:phase_3:EUR?d_prime=0.7" \
  -H "Content-type:application/json" > ld_partners.json

# Step 2: Extract variant IDs
python3 -c "
import json
with open('ld_partners.json') as f:
    data = json.load(f)
variants = set()
for entry in data:
    for v in entry.get('variations', [entry.get('variation2', '')]):
        variants.add(v)
print('\n'.join(sorted(variants)))
" > ld_variant_ids.txt

# Step 3: Run VEP
vep --input_file ld_variant_ids.txt \
    --output_file vep_output.txt \
    --cache --assembly GRCh38 \
    --plugin CADD \
    --plugin SpliceAI \
    --plugin dbNSFP,BayesDel_addAF_score,ClinPred_score,DEOGEN2_score \
    --regulatory \
    --force_overwrite
