# contexor

### A python classifier that provides accurates contextual classifying for any website in seconds. 

## 1. Background 

Researchers commonly can benefit from a capability to classify websites automatically based on prominent content on the site. For example, a researcher may want to scan a large number of sites to identify sites that have a strong affinity with a specific topic ('privacy') or behaviour ('strong language').

### 1.1. How to use? 

    predictions = kuubio(X=[0:300],                   # features
                             Y='ivt',                 # indepedent variable
                             data=sites,              # name of dataframe
                             dims=300,                # number of features
                             epoch=5,                 # no of training cycles
                             flatten=.8,              # conversion to binary
                             layers=5,                # number of layers in the model
                             neuron_first='auto',     # number of neurons on first layer
                             neuron_last=1,           # number of neurons on last layer
                             model='model',           # option to load model
                             loss='binary_crossentropy',  # which model to use
                             save_model=False)        # option to save model


### 1.2. Capabilities 

Basically the rule is that everything that can be done now in Keras, to the extent of what are the most commonly used features by researchers in our field, can be done in a one line command. The other rule is that the one line command has to run with as little input as x,y and still perform. So the simplest use case is: 

     kuubio('feature','indepedent_var',df)
     
    
## 2. Solution 

The solution consist of three primary capabilities: 

1) to capture a representative set of pages from the site
2) to distinguis between sections (e.g. comments) on the page and parse clean text 
3) make prediction for classification 

### 2.1. data capture 

1) domain/s input from user
2) extract urls of prominent pages from landing page
3) extract html from invididual pages

### 2.2. content capture 

- separate the page to sections (e.g. comments, body, ads) 
- separate clean text from other elements in each page section 

### 2.3. classification 

- tokenize text for analysis
- run models 
- output classification 

## 3. User Interactions

There are two kinds of interactions: 

1) configuration
2) regular use 

### 3.1. Configuration 

- create a list of seed sites for the category
- run through test results that prove the model works
- tweak the seed:
 - add or remove words
 - define co-occurance of words
 - define weights for words
 - define proximities 

### 3.2. Regular Use

- input a single site to API
- input a list of sites to API
- get a dictionary/json in return with the classification 

## 4. 3rd-party technology

- Pandas for data wrangling
- Numpy for arrays and maths
- nltk for semantics 
- nightmare.js or some other headless browswer for html extraction
- Beautiful soup for clear text extraction

## 5. System requirements 

The solution is able to perform classification for a single site in less than 5 seconds using an AWS micro instance with GB1 of RAM. 

## 6. Style guide

- PEP8 (at least close)
- no line of code longer than 50 chars
- no function longer than 50 rows 
