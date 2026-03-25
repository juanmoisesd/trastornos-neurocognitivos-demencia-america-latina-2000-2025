"""Trastornos Neurocognitivos y Demencia en América Latina e Iberoamérica (2000-202
DOI:10.5281/zenodo.19211345"""
__version__="1.0.0"
import pandas as pd,io,requests
def load_data(f=None):
  rid="10.5281/zenodo.19211345".split(".")[-1];m=requests.get("https://zenodo.org/api/records/"+rid,timeout=30).json();csvs=[x for x in m.get("files",[]) if x["key"].endswith(".csv")]
  if not csvs:raise ValueError("No CSV")
  tgt=next((x for x in csvs if f and x["key"]==f),csvs[0]);return pd.read_csv(io.StringIO(requests.get(tgt["links"]["self"],timeout=60).text))
def cite():return "de la Serna, Juan Moisés (2025). Trastornos Neurocognitivos y Demencia en América Latina e Ib"
def info():print("DOI: 10.5281/zenodo.19211345\nGitHub: https://github.com/juanmoisesd/trastornos-neurocognitivos-demencia-america-latina-2000-2025")
