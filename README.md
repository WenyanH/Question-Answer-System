# nlp-wiki-system

02/20/2016 - wenyanh
1. I have uploaded four wiki raw files we once used for our questions asking & answering in txt format.

2. The wikiPretreament.py is used for pretreatment the wiki file into an operable txt file for your further steps.
It is in the command line format for your file input and output.
And I have produced 4 data files (data1-4) for you to use. Contact me directly if there is any problem.

3. I tried to fetch the main information from the website directly but haven't found a good way for the data cleaning. Now the code is in the txtFetch.py.
It would be better if you could give me some advice. Or, need we complete this function?


02/22/2016 - xc2
1. I have updated the file of creating easy question. The file deals with the verbs of be(is, are, am, was, were). One of the problem is to identify whether the first word is proper noun or not. My thought is to record the appearance of each word in the dictionary. Then we check whether the lower case of the first word is in the dictionary. If it is in the dictionary, it has lowercase format. So it is not a proper noun.  
