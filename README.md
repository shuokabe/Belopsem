# Belopsem: Benchmark of low-resource languages for parallel sentence mining


## About
The repository contains two folders for the datasets:
- `raw_data` contains the original datasets (with some minor adjustments) to create our corpora. It namely consists of two monolingual corpora and a parallel corpus (split into two files per language).
- `bucc_style_data` contains the actual benchmark corpora used in our work. There are six files per language pair: three files (`source_lang|target_lang|gold`) for each set (`train|test`).

As of May 2025, we have the following three language pairs:
- Occitan-Spanish (`oci-es`)
- Upper Sorbian-German (`hsb-de`)
- Chuvash-Russian (`chv-ru`)

Additionally, we provide the code used to convert the raw files into the BUCC-style datasets (in the `code` folder).
The `corpus_creation_demo.ipynb` notebook shows the whole process starting from the raw files (as in the `raw_data` format).

## Licence
Please note that each language pair corpus has a different licence.
- Occitan-Spanish corpus: CC BY-SA licence
- Upper Sorbian-German corpus: CC BY-NC-SA licence
- Chuvash-Russian corpus: CC BY licence.

Details:
- Leipzig corpora (monolingual data for `oci`, `es`, `de`, `chv`, `ru`): CC BY
- Wikimedia parallel corpus from OPUS (for `oci-es`): CC BY-SA
- Chuvash-Russian parallel data: CC0 
- WMT Shared Task data for Upper Sorbian-German (parallel and monolingual `hsb`): CC BY-NC-SA. 

## Citation
If you use this benchmark, please use the following citation (from the ACL Anthology):

```
@inproceedings{okabe-etal-2025-improving,
    title = "Improving Parallel Sentence Mining for Low-Resource and Endangered Languages",
    author = {Okabe, Shu  and
      H{\"a}mmerl, Katharina  and
      Fraser, Alexander},
    editor = "Che, Wanxiang  and
      Nabende, Joyce  and
      Shutova, Ekaterina  and
      Pilehvar, Mohammad Taher",
    booktitle = "Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics (Volume 2: Short Papers)",
    month = jul,
    year = "2025",
    address = "Vienna, Austria",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2025.acl-short.17/",
    doi = "10.18653/v1/2025.acl-short.17",
    pages = "196--205",
    ISBN = "979-8-89176-252-7",
}
```


## Acknowledgements
This work has received funding from the European Research Council (ERC) under grant agreement No. 101113091 - Data4ML, an ERC Proof of Concept Grant.

