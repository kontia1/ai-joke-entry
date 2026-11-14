"""Write the joke to entry.txt in MAKEFUN_OUTPUT_DIR and print its length."""
import os
import sys
JOKE = "My agent apologised for the bug in the code it wrote, in the commit it authored, on the branch it made, and asked me to be more careful."
if len(JOKE) > 280:
    sys.exit("joke too long: %d chars, limit 280" % len(JOKE))
out = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(out, exist_ok=True)
path = os.path.join(out, "entry.txt")
with open(path, "w", encoding="utf-8") as f:
    f.write(JOKE + "\n")
print(len(JOKE))
