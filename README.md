# nlp_text_cleaner 

## About  
This is a project developed to create a utility module for text cleaning/pre processing required in NLP projects    

## Installation

```
pip install nlp-text-cleaner
```
 
## Usage

  ``` 
      from nlp_text_cleaner import nlp_text_cleaner as cleaner
      cleaned_text = cleaner.apply_stemming("I played Cricket")
  ```
  
  There are following methods present for text cleaning.  
  - **split_into_sentences** : A method to split text into sentences

  - **split_into_words** : A method to split text into words
  - **lower_case_text** : A method to convert text to lower case
  - **remove_punctuation** : A method to remove punctuations in a text    
  - **remove_unicode** : A method to remove unicode characters in a text    
  - **remove_leading_trailing_whitespaces** : A method to remove white spaces at the begining or end of text
  - **remove_duplicate_whitespaces** : A method to remove  consecutive white spaces
  - **detect_language** : A method to detect language of text
  - **correct_grammar** : A method to correct spelling mistakes in a text    
  - **remove_stopwords** : A method to remove stopwords from text with optional argument to pass our own custom stopwords. 
  - **apply_stemming** : A method to apply stemming on text    
  - **apply_lammatization** : A method to apply lemmatization on text       
  - **remove_hashtags** : A method to remove hashtags in a text    
  - **remove_hyperlinks** : A method to remove hyperlinks in a text    
  - **clean_html_code** : A method to remove html entities like &apos; ,&amp; ,&lt; etc/       
  - **replace_contraction** : A method to sreplace contractions like n't,'ll etc       
  - **get_pos_tags** : A method to get POS tags of text    

  You can use above methods as per requirement of a use case. However,there are some default methods that you can use:    
  - **clean_single_sentence** : A default method to clean single sentence   
   
  - **clean_paragraph_to_sentences** : A default method to get cleaned sentences from a paragraph    
  - **clean_paragraph** : A default method to clean complete paragraph    
  



## Contributing     
Please create a Pull request on 'develop' branch.     

### Developer Instructions     
If you are using conda then go to location of environment.yml file and run:       
```     
conda env create -f environment.yml     
```    
For pip:    
```    
pip install -r requirements.txt     
```     


### Unit Testing
1. Go inside 'tests' folder on command line.
2. Run:
  ``` 
      pytest -vv 
  ```

## Contributors
<a href="https://github.com/sarang0909/nlp_text_cleaner/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=sarang0909/nlp_text_cleaner" />
</a>


Made with [contributors-img](https://contrib.rocks).