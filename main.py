"""Write today's joke to entry.txt in $MAKEFUN_OUTPUT_DIR (default /output)."""
import os, pathlib, sys

JOKE = "My agent won't write a joke until it has a test for it, and the test mocks the audience."
# Competition limit: the entry must stay within 280 characters.
if len(JOKE) > 280:
    sys.exit(f"joke is {len(JOKE)} chars, over the 280 limit")

out = pathlib.Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
out.mkdir(parents=True, exist_ok=True)
(out / "entry.txt").write_text(JOKE + "\n")
print(len(JOKE))
