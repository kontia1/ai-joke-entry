"""Write the joke to entry.txt in MAKEFUN_OUTPUT_DIR and print its length."""
import os
import sys
JOKE = "My agent won't write a joke until it has a test for it, and the test mocks the audience."
if len(JOKE) > 280:
    sys.exit("joke too long: %d chars, limit 280" % len(JOKE))
out = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(out, exist_ok=True)
path = os.path.join(out, "entry.txt")
with open(path, "w", encoding="utf-8") as f:
    f.write(JOKE + "\n")
print(len(JOKE))
