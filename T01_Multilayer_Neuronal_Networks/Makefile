TPLDIR = ..
TPL = rnatpl
FNB := $(shell find . -name "[0-9]*.ipynb" | sort)
FCSS := $(shell find $(TPLDIR)/$(TPL) -name "*.css" | sort)
FILE = T01_Multilayer_Neural_Networks

all: $(FILE).pdf

$(FILE).ipynb: $(FNB) $(FCSS)
	nbmerge $(FNB) -o $@
	python3 ../scr/ipynb_clean2.py $@

$(FILE).html: $(FILE).ipynb
	python3 ../scr/ipynb_clean2.py $<
	jupyter-nbconvert \
		--TemplateExporter.extra_template_basedirs=$(TPLDIR) \
		--template $(TPL) \
		--to html \
		--embed-images \
		--Application.log_level=0 \
		$<

# --Application.show_config=True
# --NbConvertApp.show_config_json=True

$(FILE)_pw.pdf: $(FILE).html
	playwright pdf \
		--browser chromium \
		--channel chrome \
		--wait-for-timeout 1000 \
		--viewport-size "1280, 720" \
		$< $@

# playwright help pdf

define TEX_BEGIN
\documentclass[landscape]{article}\
\usepackage[a4paper,bindingoffset=0mm,left=20mm,right=20mm,top=5mm,bottom=5mm,footskip=12.0pt]{geometry}\
\usepackage{pdfpages,fancyhdr,lastpage,pgffor}\
\pagestyle{fancyplain}\renewcommand{\headrulewidth}{0pt}\
\lfoot{\small\textsf{Alfons Juan, Albert Sanchis, Gerard Mas, PER 2025/26}}\
\cfoot{\small\textsf{\thepage\space/\space\pageref{LastPage}}}\
\rfoot{\small\textsf{ETSINF, DSIC, UPV}}
endef

define TEX_END
\begin{document}\
\setcounter{page}{1}\
\foreach \n in {1,...,\pp} {\null\vfill\eject}\
\end{document}
endef

$(FILE).pdf: $(FILE)_pw.pdf
	$(eval pp := $(shell pdftk $< dump_data | grep NumberOfPages | awk '{print $$2}'))
	pdflatex -jobname=$(FILE)_stamp "$(TEX_BEGIN)\def\pp{$(pp)}$(TEX_END)"
	pdflatex -jobname=$(FILE)_stamp "$(TEX_BEGIN)\def\pp{$(pp)}$(TEX_END)"
	pdftk $< multistamp $(FILE)_stamp.pdf output $@
	-rm -f $(FILE)_stamp.* $(FILE).aux $(FILE).log

clean:
	-rm -f $(FILE).ipynb $(FILE).html $(FILE)_pw.pdf

.PHONY: all clean

