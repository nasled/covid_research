MAIN_DOCUMENT = main

make:
	pdflatex -file-line-error -interaction=nonstopmode -synctex=1 -output-directory=$(CURDIR) -output-format=pdf $(MAIN_DOCUMENT).tex
	bibtex $(MAIN_DOCUMENT)
	pdflatex -file-line-error -interaction=nonstopmode -synctex=1 -output-format=pdf -output-directory=$(CURDIR) main.tex
	pdflatex -file-line-error -interaction=nonstopmode -synctex=1 -output-format=pdf -output-directory=$(CURDIR) main.tex
	make clean
	mv main.pdf output/paper.pdf

clean:
	rm -rf $(TARGET) *.class *.html *.aux *.out *.thm *.idx *.toc *.ilg *.glg *.glo *.gls *.ist *.xdy *.fdb_latexmk *.bak *.blg *.glsdefs *.acn *.acr *.alg *.nls *.nlo *.bak *.pyg *.lot *.lof *.xmpdata *.xmpi *.bbl
	rm -rf _minted-booka4
	rm -rf *.log
	rm -rf *.bbl *.ind
	rm -rf *.synctex.gz



