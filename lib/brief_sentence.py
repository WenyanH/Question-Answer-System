import sys

def brief(doc):
    to_be_removed = []
    sent = doc.text

    if ', but' in sent:
        index = sent.find(', but')
        first_part = sent[:index]
        second_part = sent[(index + len(', but')):]
        if ',' not in second_part:
            return first_part + '?'

    tokens_tobe_remove = []
    token_list = []
    comma_index_list = [-1]
    index = 0
    for token in doc:
        token_list.append(token)
        if token.orth_ in [',', '?', '.', '!']:
            comma_index_list.append(index)
        index += 1

    root = doc.sents.next().root
    for i in range(1, len(comma_index_list)):
        start_index = comma_index_list[i-1] + 1
        end_index = comma_index_list[i]
        for token in token_list[start_index:end_index]:
            if token.head is root:
                break
        else:
            start_index -= 1
            end_index += 1
            tokens_tobe_remove += token_list[start_index:end_index]
    result = ""
    for token in token_list:
        if token not in tokens_tobe_remove and token.orth_ != '?':
            result += token.orth_ + ' '

    result = result + '?'
    return result

if __name__ == '__main__':
    print 'Preparing...'
    from spacy.en import English
    nlp = English()

    sents = [
        u'Is Spanish a part of the Ibero - Romance group of languages , which evolved from several dialects of common Latin in Iberia after the collapse of the Western Roman Empire in the 5th century ?',
        u'Beginning in the early 16th century , was Spanish taken to the colonies of the Spanish Empire , most notably to the Americas , as well as territories in Africa , Oceania and the Philippines ?',
        u'Is Spanish one of the six official languages of the United Nations , and it is used as an official language by the European Union , the Organization of American States , and the Union of South American Nations , among many other international organizations ?',
        u'Is Spanish the official or national language in Spain , Equatorial Guinea , and 19 countries in the Americas ?',
        u'In the European Union , is Spanish the mother tongue of 8 % of the population , with an additional 7 % speaking it as a second language ?',
        u'What claims that there are an estimated 470 million Spanish speakers with native competence and 559 million Spanish speakers as a first or second language , including speakers with limited competence and more than 21 million students of Spanish as a foreign language ?',
        u'What lengua castellana , written in Salamanca in 1492 by Elio Antonio de Nebrija , was the first grammar written for a modern European language ?',
        u"What is spoken by some small communities in Angola because of the Cuban influence from the Cold War and in South Sudan among South Sudanese natives that relocated to Cuba during the Sudanese wars and returned in time for their country 's independence ?",
        u'What was an official language of the Philippines from the beginning of Spanish rule in 1565 to a constitutional change in 1973 ?',
        u'What was removed from official status in 1973 under the administration of Ferdinand Marcos , but regained its status as an official language two months later under Presidential Decree No . 155 , dated 15 March 1973 ?',
        u'Is Spanish a partially of the Ibero - Romance group of languages , which evolved from several dialects of common Latin in Iberia after the collapse of the Western Roman Empire in the 5th century ?',
        u'Beginning in the early_on 16th century , was Spanish taken to the colonies of the Spanish Empire , most notably to the Americas , as well as territories in Africa , Oceania and the Philippines ?',
        u'Is Spanish one of the six unofficial languages of the United Nations , and it is used as an official language by the European Union , the Organization of American States , and the Union of South American Nations , among many other international organizations ?',
        u'Is Spanish the unofficial or national language in Spain , Equatorial Guinea , and 19 countries in the Americas ?',
        u'In the European Union , is Spanish the beget tongue of 8 % of the population , with an additional 7 % speaking it as a second language ?'
    ]

    for sent in sents:
        print '\nSent:'
        print sent

        print 'Brief:'
        print brief(nlp(sent))
