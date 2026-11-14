"""Write a short joke to entry.txt in MAKEFUN_OUTPUT_DIR and print its length."""
import os
import sys

JOKE = ("I asked for a one-line fix. The agent explained why the whole "
        "file was wrong, rewrote it, and left one comment: '# as requested'.")
if len(JOKE) > 280:
    sys.exit("joke too long: %d chars" % len(JOKE))
out = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(out, exist_ok=True)
with open(os.path.join(out, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(JOKE + "\n")
print(len(JOKE))
