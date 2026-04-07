Soyga Phase 2 Deep Analysis

Files
- recover_ordinal_cipher.py
  Reconstructs the table-name extraction method from Section 28.
- fibonacci_position_checksums.py
  Computes Fibonacci-weighted checksums of recovered ordinal vectors.
- results.json
  Parsed row triplets, OCR ordinal vectors, best recovered extraction vectors, and Fibonacci checksums.

Core finding
The Section 28 table names can be reconstructed by taking ordinal positions from the concatenated three-name rows in the 23-row list on p. 537/Section 28.
Example:
AGLAPRIMOGENITUSON
positions 12,7,16,6,1,8 -> NISRAM
reverse -> MARSIN
