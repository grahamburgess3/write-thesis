echo -e "writing my PhD..."
cd thesis
pdflatex main.tex
bibtex main
for run in {1..2}; do pdflatex main.tex; done
cd ../
