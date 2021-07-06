# Malicious JS Detection
[Report](https://www.overleaf.com/2177694124dmmtpdwvndcj)

[Article](https://swag.cispa.saarland/papers/fass2019jstap.pdf)

[JStap GitHub](https://github.com/Aurore54F/JStap)

## DataSets
### Malicious
[Geek Dataset](https://github.com/geeksonsecurity/js-malicious-dataset)

### Benign
[React Dataset](https://github.com/facebook/react)

[Jasmine Dataset](https://github.com/jasmine/jasmine)

## Add js/html files to our DataSet
```shell
 > python3 js_extraction.py -h
usage: js_extraction.py [-h] -s FROM_DIR [-m]

Export js and HTML files

optional arguments:
  -h, --help       show this help message and exit
  -s FROM_DIR      The source directory from which the js and html files are copied
  -m, --malicious  Indicates if the files are malicious or benign
```