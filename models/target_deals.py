"""Build the 'target with deals' copy of the business plan: the base workbook with the negotiated partner costs.

Usage: python3 target_deals.py "Kelen business plan.xlsx" target.xlsx, then recalculate target.xlsx.
Column F is the base-scenario value of inputs that vary by scenario; column D holds single-value inputs.
"""
import sys
from openpyxl import load_workbook

TARGET = {"Cost of a transfer to a wallet: % of amount": [("F", 0.005)], "Cost of a transfer to a wallet: cap": [("F", 2500)],
          "Card processing per active card": [("F", 600)], "Partner bank fee per business account": [("F", 1500)],
          "Cost of a transfer to a bank account": [("F", 150)], "Cost of a salary paid to a bank account": [("F", 100)],
          "Visa / Mastercard cross-border fees and bank FX margin": [("F", 0.012)],
          "International payments: cost to Kelen (% of amount)": [("D", 0.027)],
          "Card programme collateral at the partner bank": [("D", 30000000)]}

wb = load_workbook(sys.argv[1])
A = wb["Assumptions"]
for lab, cells in TARGET.items():
    rows = [c.row for c in A["B"] if isinstance(c.value, str) and c.value.startswith(lab)]
    assert len(rows) == 1, (lab, rows)
    for col, val in cells:
        A[f"{col}{rows[0]}"] = val
wb.save(sys.argv[2])
