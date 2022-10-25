"""
Module for functional test cases of main script.
"""


import nlp_text_cleaner

print(nlp_text_cleaner.apply_stemming("I played Cricket"))

'''



def test_server_status():
    """Tests if server is running."""
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"msg": "API server is running"}


def test_model_output():
    """Tests if model output generation api is up and giving expected result."""
    response = client.post("/model_inference/", json={"data": "test input","model": "tfidf_pycaret"})
    assert response.status_code == 200
    assert response.json() == {
        "model_output": "model_output:NEUTRAL"
    }
'''
