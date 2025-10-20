echo -e "writing my PhD..."

# make environment
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# run analysis
cd experiment1
python ./../src/triangle.py --config config.yaml
cd ./../

# compile thesis
cd thesis
pdflatex main.tex
bibtex main
for run in {1..2}; do pdflatex main.tex; done
cd ./../
