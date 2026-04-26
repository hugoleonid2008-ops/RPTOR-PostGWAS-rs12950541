#!/usr/bin/env python3
"""
Query ChEMBL for ABCC8 and RPTOR drug target information.

ChEMBL API Documentation: https://www.ebi.ac.uk/chembl/api/docs/
"""

import urllib.request
import json
import sys

CHEMBL_API = "https://www.ebi.ac.uk/chembl/api/data"

def get_target(chembl_id):
    """Retrieve target information from ChEMBL by ID."""
    try:
        url = f"{CHEMBL_API}/target/{chembl_id}.json"
        with urllib.request.urlopen(url) as resp:
            return json.loads(resp.read())
    except urllib.error.URLError as e:
        print(f"Error fetching target {chembl_id}: {e}", file=sys.stderr)
        return None

def get_mechanism(chembl_id):
    """Retrieve mechanism of action data for a ChEMBL target."""
    try:
        url = f"{CHEMBL_API}/mechanism.json?target_chembl_id={chembl_id}"
        with urllib.request.urlopen(url) as resp:
            return json.loads(resp.read())
    except urllib.error.URLError as e:
        print(f"Error fetching mechanisms for {chembl_id}: {e}", file=sys.stderr)
        return None

def get_activities(chembl_id, limit=50):
    """Retrieve bioactivity data for a ChEMBL target."""
    try:
        url = f"{CHEMBL_API}/activity.json?target_chembl_id={chembl_id}&limit={limit}"
        with urllib.request.urlopen(url) as resp:
            return json.loads(resp.read())
    except urllib.error.URLError as e:
        print(f"Error fetching activities for {chembl_id}: {e}", file=sys.stderr)
        return None

def main():
    print("=" * 80)
    print("ChEMBL Target Query: ABCC8 and RPTOR")
    print("=" * 80)
    print()

    # Query ABCC8 (ATP-binding cassette subfamily C member 8)
    # Also known as: SUR1 (Sulfonylurea Receptor 1)
    print("Target 1: ABCC8 (Sulfonylurea Receptor 1 / SUR1)")
    print("-" * 80)

    abcc8_chembl_id = "CHEMBL2071"
    abcc8_target = get_target(abcc8_chembl_id)

    if abcc8_target:
        print(f"ChEMBL ID: {abcc8_chembl_id}")
        print(f"Preferred Name: {abcc8_target.get('pref_name', 'N/A')}")
        print(f"Target Type: {abcc8_target.get('target_type', 'N/A')}")
        print(f"Organism: {abcc8_target.get('organism', 'N/A')}")
        print(f"Description: {abcc8_target.get('description', 'N/A')[:200]}...")

        # Get mechanisms of action
        abcc8_mechanisms = get_mechanism(abcc8_chembl_id)
        if abcc8_mechanisms:
            mech_count = abcc8_mechanisms.get('page_meta', {}).get('total_count', 0)
            print(f"\nMechanisms of Action: {mech_count}")
            for i, mech in enumerate(abcc8_mechanisms.get('mechanisms', [])[:5], 1):
                moa = mech.get('mechanism_of_action', 'N/A')
                action_type = mech.get('action_type', 'N/A')
                molecule = mech.get('molecule_pref_name', 'N/A')
                print(f"  {i}. {moa} (Action: {action_type})")
                print(f"     Molecule: {molecule}")

        # Get bioactivity overview
        abcc8_activities = get_activities(abcc8_chembl_id, limit=5)
        if abcc8_activities:
            activity_count = abcc8_activities.get('page_meta', {}).get('total_count', 0)
            print(f"\nBioactivity Data: {activity_count} records")
            for activity in abcc8_activities.get('activities', [])[:3]:
                standard_type = activity.get('standard_type', 'N/A')
                standard_value = activity.get('standard_value', 'N/A')
                units = activity.get('standard_units', 'N/A')
                compound_name = activity.get('molecule_pref_name', 'N/A')
                print(f"  - {compound_name}: {standard_type} = {standard_value} {units}")

    print("\n")

    # Query RPTOR (Regulatory-Associated Protein of mTOR Complex 1)
    print("Target 2: RPTOR (Regulatory-Associated Protein of mTOR Complex 1)")
    print("-" * 80)

    rptor_chembl_id = "CHEMBL3120040"
    rptor_target = get_target(rptor_chembl_id)

    if rptor_target:
        print(f"ChEMBL ID: {rptor_chembl_id}")
        print(f"Preferred Name: {rptor_target.get('pref_name', 'N/A')}")
        print(f"Target Type: {rptor_target.get('target_type', 'N/A')}")
        print(f"Organism: {rptor_target.get('organism', 'N/A')}")
        print(f"Description: {rptor_target.get('description', 'N/A')[:200]}...")

        # Get mechanisms of action
        rptor_mechanisms = get_mechanism(rptor_chembl_id)
        if rptor_mechanisms:
            mech_count = rptor_mechanisms.get('page_meta', {}).get('total_count', 0)
            print(f"\nMechanisms of Action: {mech_count}")
            for i, mech in enumerate(rptor_mechanisms.get('mechanisms', [])[:5], 1):
                moa = mech.get('mechanism_of_action', 'N/A')
                action_type = mech.get('action_type', 'N/A')
                molecule = mech.get('molecule_pref_name', 'N/A')
                print(f"  {i}. {moa} (Action: {action_type})")
                print(f"     Molecule: {molecule}")
        else:
            print("\nNo known mechanisms of action in ChEMBL")

        # Get bioactivity overview
        rptor_activities = get_activities(rptor_chembl_id, limit=5)
        if rptor_activities:
            activity_count = rptor_activities.get('page_meta', {}).get('total_count', 0)
            print(f"\nBioactivity Data: {activity_count} records")
            if activity_count > 0:
                for activity in rptor_activities.get('activities', [])[:3]:
                    standard_type = activity.get('standard_type', 'N/A')
                    standard_value = activity.get('standard_value', 'N/A')
                    units = activity.get('standard_units', 'N/A')
                    compound_name = activity.get('molecule_pref_name', 'N/A')
                    print(f"  - {compound_name}: {standard_type} = {standard_value} {units}")

    print("\n")
    print("=" * 80)
    print("Query Complete")
    print("=" * 80)
    print()
    print("Key Observations:")
    print("  1. ABCC8 (SUR1) is a well-characterized drug target with known mechanisms")
    print("  2. RPTOR is less characterized in ChEMBL (expected, as it's primarily a")
    print("     scaffold protein rather than a direct drug target)")
    print("  3. Novel connection: RPTOR regulation may influence ABCC8 expression/function")
    print("     via mTOR signaling pathway")
    print()

if __name__ == "__main__":
    main()
