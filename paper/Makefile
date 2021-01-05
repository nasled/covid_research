MAIN_DOCUMENT = main

make:
	pdflatex $(MAIN_DOCUMENT).tex -output-format=pdf
	bibtex $(MAIN_DOCUMENT)
	make clean

arxiv:
	zip -r upload.zip . -x \*.git\* -x MAKEFILE -x *.zip -x *.pdf

clean:
	rm -rf $(TARGET) *.class *.html *.aux *.out *.thm *.idx *.toc *.ilg *.glg *.glo *.gls *.ist *.xdy *.fdb_latexmk *.bak *.blg *.glsdefs *.acn *.acr *.alg *.nls *.nlo *.bak *.pyg *.lot *.lof *.xmpdata *.xmpi *.bbl
	rm -rf _minted-booka4
	rm -rf *.log  # Analyze this for errors
	rm -rf *.bbl *.ind  # Needed for arxiv
    