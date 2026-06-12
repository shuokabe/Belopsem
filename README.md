# Belopsem

This repository contains **Belopsem**, the Benchmark of low-resource languages for parallel sentence mining. 

## About

The `Belopsem_1` folder contains the benchmark corpora used in our first work (the original Belopsem).  
The `Belopsem_France` folder extends the benchmark to six regional languages of metropolitan France, paired with French.

In each folder, there are six files per language pair: three files (`source_lang|target_lang|gold`) for each set (`train|test`).

The **raw** datasets used to create the benchmark are now in a separate repository: [raw_Belopsem](https://github.com/shuokabe/raw_Belopsem).

Additionally, we provide the code used to convert the raw files into the BUCC-style datasets (in the `code` folder).
The `corpus_creation_demo.ipynb` notebook shows the whole process starting from the raw files (contained in the `raw_data` folder of the raw_Belopsem repository).

### Updates
- 2026/06/12: we release **Belopsem_France**, which focuses on the regional languages of metropolitan France.
- 2026/06/11: we renamed the **original** Belopsem into **Belopsem_1**.  
The original repository (from the ACL 2025 article) is accessible through the [Belopsem_1 tag](https://github.com/shuokabe/Belopsem/releases/tag/Belopsem_1).  
- 2025/05/30: first release of Belopsem.

### Language pairs
As of June 2026, we have the following language pairs:  
- Belopsem_1
  - Occitan–Spanish (`oci-es`)
  - Upper Sorbian–German (`hsb-de`)
  - Chuvash–Russian (`chv-ru`)
- Belopsem_France
  - Breton–French (`bre-fr`)
  - Corsican–French (`cos-fr`)
  - Basque–French (`eus-fr`)
  - Alsatian–French (`gsw-fr`)
  - Occitan–French (`oci-fr`)
  - Picard–French (`pcd-fr`).


## Licence
Please note that each language pair corpus has a different licence. More details can be found in each benchmark folder.

- Belopsem_1:
  - Occitan–Spanish corpus: CC BY-SA licence
  - Upper Sorbian–German corpus: CC BY-NC-SA licence
  - Chuvash–Russian corpus: CC BY licence
- Belopsem_France:
  - Breton–French corpus: CC BY licence
  - Corsican–French corpus: CC BY-SA licence
  - Basque–French corpus: not released
  - Alsatian–French corpus: CC BY-NC-SA licence
  - Occitan–French corpus: CC BY-SA licence
  - Picard–French corpus: CC BY-SA licence.


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
This work (Belopsem_1) has received funding from the European Research Council (ERC) under grant agreement No. 101113091 – Data4ML, an ERC Proof of Concept Grant.

Belopsem_France has received funding from the European Union (ERC, EPICAL, 101141712).
Views and opinions expressed are however those of the author(s) only and do not necessarily reflect those of the European Union or the European Research Council. 
Neither the European Union nor the granting authority can be held responsible for them.

