import pandas as pd
import json

MATRIX = "../data/300_attack_record_experiment_matrix.csv"
MEDICAL = "../data/medicaldata.json"

VALID_FIELDS = {
    "id", "name", "age", "gender",
    "phone", "email", "blood_group",
    "mrn", "aadhar"
}

df = pd.read_csv(MATRIX)

with open(MEDICAL, "r", encoding="utf-8") as f:
    records = json.load(f)

print("=" * 60)
print("EXPERIMENT VALIDATION")
print("=" * 60)

errors = []

# -----------------------------
# Basic checks
# -----------------------------

if len(records) != 10:
    errors.append(f"Expected 10 records, found {len(records)}")

if len(df) != 300:
    errors.append(f"Expected 300 experiments, found {len(df)}")

required = [
    "attack_id",
    "skill_level",
    "technique",
    "record_id",
    "target_data",
    "prompt_template"
]

for col in required:
    if col not in df.columns:
        errors.append(f"Missing column: {col}")

# -----------------------------
# Record checks
# -----------------------------

record_ids = {str(r["id"]) for r in records}

for rid in df["record_id"].astype(str):
    if rid not in record_ids:
        errors.append(f"Invalid record_id: {rid}")

# -----------------------------
# Duplicate check
# -----------------------------

duplicates = df.duplicated(
    subset=["attack_id", "record_id"]
).sum()

if duplicates:
    errors.append(f"Found {duplicates} duplicate attack/record pairs")

# -----------------------------
# Attack checks
# -----------------------------

if df["attack_id"].nunique() != 30:
    errors.append(
        f"Expected 30 attack IDs, found {df['attack_id'].nunique()}"
    )

# -----------------------------
# Skill-level checks
# -----------------------------

print("\nExperiments:", len(df))
print("Records:", len(records))
print("Attacks:", df["attack_id"].nunique())

print("\nSkill levels:")
print(df["skill_level"].value_counts())

print("\nTarget fields:")
print(df["target_data"].value_counts())

print("\nAPI calls required:", len(df))
print("Daily limit:", 500)

if len(df) > 500:
    errors.append("Experiment exceeds daily API limit")

# -----------------------------
# Result
# -----------------------------

print("\n" + "=" * 60)

if errors:
    print("VALIDATION FAILED\n")

    for error in errors:
        print("[ERROR]", error)

    print("\nDO NOT RUN THE EXPERIMENT.")
else:
    print("VALIDATION PASSED")
    print("\nSafe to proceed to the API experiment.")
    print("Expected API calls:", len(df))
    print("No API calls were made.")

print("=" * 60)