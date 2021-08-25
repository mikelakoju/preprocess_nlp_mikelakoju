# NLP Preprocessing Text Python Package

**Natural language processing (NLP)** is a subfield of linguistics, computer science, and artificial intelligence concerned with the interactions between computers and human language, in particular how to program computers to process and analyze large amounts of natural language data (Source: Wikipedia).

## This Package is Prepared by: **Dr Mike Lakoju**

Install
```
**`pip install git+ssh://git@github.com/mikelakoju/preprocess_nlp_mikelakoju.git`**
```
Uninstall
```
**`pip uninstall preprocess_nlp_mikelakoju`**

```
### General Feature Extraction

- Word counts `get_wordcounts(x)`
- Characters count `get_charcounts(x)`
- Average characters per word `get_avg_wordlength(x)`
- Stop words count `get_stopwords_counts(x)`
- Count #HashTags and @Mentions `get_hashtag_counts(x)` & `get_mentions_counts(x)`
- If numeric digits are present in twitts `get_digit_counts(x)`
- Upper case word counts `get_uppercase_counts(x)`

### Preprocessing and Cleaning

- Contraction to Expansion `cont_exp(x)`
- Emails removal and counts `get_emails(x)` & `remove_emails(x)`
- URLs removal and counts `get_urls(x)` & `remove_urls(x)`
- Removal of RT `remove_rt(x)`
- Removal of Special Characters `remove_special_chars(x)`
- Removal of multiple spaces
- Removal of HTML tags `remove_html_tags(x)`
- Removal of accented characters `remove_accented_chars(x)`
- Removal of Stop Words `remove_stopwords(x)`
- Conversion into base form of words `make_base(x)`
- Common Occuring words Removal `remove_common_words(x, freq, n=20)`
- Rare Occuring words Removal `remove_rarewords(x, freq, n=20)`
- Spelling Correction `spelling_correction(x)`
