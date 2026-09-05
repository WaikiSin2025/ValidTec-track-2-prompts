# Copy this package into the cloned GitHub repository

Repository:

`https://github.com/WaikiSin2025/ValidTec-track-2-prompts`

## macOS / Linux

```bash
git clone https://github.com/WaikiSin2025/ValidTec-track-2-prompts.git
cd ValidTec-track-2-prompts

# Unzip the downloaded package directly into this cloned folder.
unzip ~/Downloads/ValidTec-track-2-prompts-files.zip

python3 run_demo.py
python3 -m unittest discover -s tests -v

git status
git add .
git commit -m "Add ValidTec Track 2 prompt context and evaluation project"
git push origin main
```

If your browser saves the ZIP somewhere other than `~/Downloads`, replace that path with the actual location.

The package ZIP contains repository contents at its root, so it is intended to be extracted directly inside the cloned repository directory.
