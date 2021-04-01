# python-nlp-toolbox

Collection of Python scripts related to natural language processing

## Maintainer

Michał Marcińczuk <marcinczuk@gmail.cm>


# Tools

## Corpora

Scripts related to processing corpus files.

### CCL

Scripts for converting CCL to other formats.

#### ccl2iob2.py

```
python corpora/ccl/ccl2iob2.py --input resources/corpora/00223160.xml 
```

Expected output:

```bash
14      14      NUM     -       -       O
:       :       PUNCT   -       -       O
25      25      NUM     -       -       O
Еврокомисията   еврокомисия     NOUN    Еврокомисия     ORG-European-Commission B-ORG
:       :       PUNCT   -       -       O
Пакистан        Пакистан        PROPN   Пакистан        GPE-Pakistan    B-LOC
да      да      AUX     -       -       O
вземе   взема   VERB    -       -       O
мерки   мярка   NOUN    -       -       O
за      за      ADP     -       -       O
сигурността     сигурност       NOUN    -       -       O
на      на      ADP     -       -       O
своите  свой    DET     -       -       O
граждани        гражданин       NOUN    -       -       O

Очакваме        очаквам VERB    -       -       O
правителството  правителство    NOUN    -       -       O
на      на      ADP     -       -       O
Пакистан        Пакистан        PROPN   Пакистан        GPE-Pakistan    B-LOC
да      да      AUX     -       -       O
вземе   взема   VERB    -       -       O
необходимите    необходим       ADJ     -       -       O
мерки   мярка   NOUN    -       -       O
за      за      ADP     -       -       O
сигурността     сигурност       NOUN    -       -       O
на      на      ADP     -       -       O
своите  свой    DET     -       -       O
граждани        гражданин       NOUN    -       -       O
,       ,       PUNCT   -       -       O
включително     включително     ADV     -       -       O
на      на      ADP     -       -       O
Асия    Асия    PROPN   Асия Биби       PER-Asia-Bibi   B-PER
Биби    Биби    PROPN   -       -       I-PER
.       .       PUNCT   -       -       O

Това    този    PRON    -       -       O
заяви   заявя   VERB    -       -       O
днес    днес    ADV     -       -       O
на      на      ADP     -       -       O
пресконференция пресконференция ADJ     -       -       O
говорител       говорител       NOUN    -       -       O
на      на      ADP     -       -       O
Европейската    европейски      ADJ     Европейска комисия      ORG-European-Commission B-ORG
комисия комисия NOUN    -       -       I-ORG
в       в       ADP     -       -       O
отговор отговор NOUN    -       -       O
на      на      ADP     -       -       O
въпрос  въпрос  NOUN    -       -       O
.       .       PUNCT   -       -       O

(...)
```