MAIN_DOCUMENT = main

make:
	pdflatex -output-directory=$(CURDIR) -output-format=pdf $(MAIN_DOCUMENT).tex
	bibtex $(MAIN_DOCUMENT)
	#pdflatex -output-directory=$(CURDIR) -output-format=pdf $(MAIN_DOCUMENT).tex
	make clean
	mv main.pdf output/paper.pdf

arxiv:
	zip -r upload.zip . -x \*.git\* -x MAKEFILE -x *.zip -x *.pdf

clean:
	rm -rf $(TARGET) *.class *.html *.aux *.out *.thm *.idx *.toc *.ilg *.glg *.glo *.gls *.ist *.xdy *.fdb_latexmk *.bak *.blg *.glsdefs *.acn *.acr *.alg *.nls *.nlo *.bak *.pyg *.lot *.lof *.xmpdata *.xmpi *.bbl
	rm -rf _minted-booka4
	rm -rf *.log  # Analyze this for errors
	rm -rf *.bbl *.ind  # Needed for arxiv
    