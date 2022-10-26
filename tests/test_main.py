"""
Module for functional test cases of main script.
"""


import nlp_text_cleaner

TEXT = "Tesla is a EV producer.It's based ~~ in Austin.#Tesla <p>Tesla is   fmous</p>"


def test_split_into_sentences():
    """Tests split_into_sentences"""
    clean_text = nlp_text_cleaner.split_into_sentences(TEXT)
    assert clean_text == [
        "Tesla is a EV producer.It's based ~~ in Austin.#Tesla <p>Tesla is   fmous</p>"
    ]


def test_split_into_words():
    """Tests split_into_words"""
    clean_text = nlp_text_cleaner.split_into_words(TEXT)
    assert clean_text == [
        "Tesla",
        "is",
        "a",
        "EV",
        "producer.It",
        "'s",
        "based",
        "~~",
        "in",
        "Austin.",
        "#",
        "Tesla",
        "<",
        "p",
        ">",
        "Tesla",
        "is",
        "fmous",
        "<",
        "/p",
        ">",
    ]


def test_lower_case_text():
    """Tests lower_case_text"""
    clean_text = nlp_text_cleaner.lower_case_text(TEXT)
    assert (
        clean_text
        == "tesla is a ev producer.it's based ~~ in austin.#tesla <p>tesla is   fmous</p>"
    )


def test_remove_punctuation():
    """Tests remove_punctuation"""
    clean_text = nlp_text_cleaner.remove_punctuation(TEXT)
    assert (
        clean_text
        == "Tesla is a EV producer.It 's based ~~ in Austin. Tesla p Tesla is fmous /p"
    )


def test_remove_unicode():
    """Tests remove_unicode"""
    clean_text = nlp_text_cleaner.remove_unicode(TEXT)
    assert (
        clean_text
        == "Tesla is a EV producer It s based in Austin Tesla p Tesla is fmous p"
    )


def test_remove_leading_trailing_whitespaces():
    """Tests remove_leading_trailing_whitespaces"""
    clean_text = nlp_text_cleaner.remove_leading_trailing_whitespaces(TEXT)
    assert (
        clean_text
        == "Tesla is a EV producer.It's based ~~ in Austin.#Tesla <p>Tesla is   fmous</p>"
    )


def test_remove_duplicate_whitespaces():
    """Tests remove_duplicate_whitespaces"""
    clean_text = nlp_text_cleaner.remove_duplicate_whitespaces(TEXT)
    assert (
        clean_text
        == "Tesla is a EV producer.It's based ~~ in Austin.#Tesla <p>Tesla is fmous</p>"
    )


def test_detect_language():
    """Tests detect_language"""
    clean_text = nlp_text_cleaner.detect_language(TEXT)
    assert clean_text == "en"


def test_correct_grammar():
    """Tests correct_grammar"""
    clean_text = nlp_text_cleaner.correct_grammar(TEXT)
    assert (
        clean_text
        == "Tesla is a EV producer.It's based ~~ in Austin.#Tesla <p>Tesla is  famous</p>"
    )


def test_remove_stopwords():
    """Tests remove_stopwords"""
    clean_text = nlp_text_cleaner.remove_stopwords(TEXT)
    assert (
        clean_text
        == "Tesla EV producer.It 's based ~~ Austin. # Tesla < p > Tesla fmous < /p >"
    )


def test_apply_stemming():
    """Tests apply_stemming"""
    clean_text = nlp_text_cleaner.apply_stemming(TEXT)
    assert (
        clean_text
        == "tesla is a ev producer.it 's base ~~ in austin. # tesla < p > tesla is fmou < /p >"
    )


def test_apply_lammatization():
    """Tests apply_lammatization"""
    clean_text = nlp_text_cleaner.apply_lammatization(TEXT)
    assert (
        clean_text
        == "Tesla is a EV producer.It 's based ~~ in Austin. # Tesla < p > Tesla is fmous < /p >"
    )


def test_remove_hashtags():
    """Tests remove_hashtags"""
    clean_text = nlp_text_cleaner.remove_hashtags(TEXT)
    assert (
        clean_text
        == "Tesla is a EV producer.It's based ~~ in Austin.Tesla <p>Tesla is   fmous</p>"
    )


def test_remove_hyperlinks():
    """Tests remove_hyperlinks"""
    clean_text = nlp_text_cleaner.remove_hyperlinks(TEXT)
    assert (
        clean_text
        == "Tesla is a EV producer.It's based ~~ in Austin.#Tesla <p>Tesla is   fmous</p>"
    )


def test_clean_html_code():
    """Tests clean_html_code"""
    clean_text = nlp_text_cleaner.clean_html_code(TEXT)
    assert (
        clean_text
        == "Tesla is a EV producer.It's based ~~ in Austin.#Tesla <p>Tesla is   fmous</p>"
    )


def test_replace_contraction():
    """Tests replace_contraction"""
    clean_text = nlp_text_cleaner.replace_contraction(TEXT)
    assert (
        clean_text
        == "Tesla is a EV producer.It is based ~~ in Austin.#Tesla <p>Tesla is   fmous</p>"
    )


def test_get_pos_tags():
    """Tests get_pos_tags"""
    clean_text = nlp_text_cleaner.get_pos_tags(TEXT)
    assert clean_text == [
        ("Tesla", "NNP"),
        ("is", "VBZ"),
        ("a", "DT"),
        ("EV", "NNP"),
        ("producer.It", "NN"),
        ("'s", "POS"),
        ("based", "VBN"),
        ("~~", "NN"),
        ("in", "IN"),
        ("Austin.", "NNP"),
        ("#", "#"),
        ("Tesla", "NNP"),
        ("<", "NNP"),
        ("p", "NN"),
        (">", "NNP"),
        ("Tesla", "NNP"),
        ("is", "VBZ"),
        ("fmous", "JJ"),
        ("<", "NNP"),
        ("/p", "NNP"),
        (">", "NN"),
    ]


def test_clean_single_sentence():
    """Tests clean_single_sentence"""
    clean_text = nlp_text_cleaner.clean_single_sentence(TEXT)
    assert (
        clean_text
        == "Tesla is a EV producer It is based in Austin Tesla p Tesla is fmous p"
    )


def test_clean_paragraph_to_sentences():
    """Tests clean_paragraph_to_sentences"""
    clean_text = nlp_text_cleaner.clean_paragraph_to_sentences(TEXT)
    assert clean_text == [
        "Tesla is a EV producer It is based in Austin Tesla p Tesla is fmous p"
    ]


def test_clean_paragraph():
    """Tests clean_paragraph"""
    clean_text = nlp_text_cleaner.clean_paragraph(TEXT)
    assert (
        clean_text
        == "Tesla is a EV producer It is based in Austin Tesla p Tesla is fmous p"
    )
