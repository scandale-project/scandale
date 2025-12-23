# A Libre Architecture for Verifiable Data Collection and Proof-of-Check Timestamping


## Build the paper

The latest buld is available [here](A_Libre_Architecture_for_Verifiable_Data_Collection_and_Proof_of_Check_Timestamping_2026.pdf).

### Install Eisvogel

Follow the instructions:

https://github.com/Wandmalfarbe/pandoc-latex-template


### Install Mermaid

Install the Mermaid cli and Let Puppeteer install a Chromium:

```bash
sudo npm install -g @mermaid-js/mermaid-cli
npx puppeteer install
```

### Generate the PDF

```
pandoc paper.md \
  --from=markdown-implicit_figures \
  --template=eisvogel \
  --toc \
  --number-sections \
  --bibliography=bibliography.bib \
  --citeproc \
  --filter pandoc-mermaid \
  -o A_Libre_Architecture_for_Verifiable_Data_Collection_and_Proof_of_Check_Timestamping_2026.pdf
```

## License

[This work](https://github.com/scandale-project/scandale/tree/main/paper) is licensed under
[Attribution-ShareAlike 4.0 International](https://creativecommons.org/licenses/by-sa/4.0/)

~~~
Copyright (c) 2025 Computer Incident Response Center Luxembourg (CIRCL)
Copyright (C) 2025 Cédric Bonhomme - https://github.com/cedricbonhomme
~~~

