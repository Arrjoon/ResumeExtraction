# nlp_app/nlp_utils.py

import spacy
import os
from django.conf import settings

class SpaCyNER:
    def __init__(self):
        model_path = os.path.join(settings.BASE_DIR, 'myapp/nlp_model')
        self.nlp = spacy.load(model_path,disable=["tagger", "parser", "attribute_ruler"])
        # nlp = spacy.load("en_core_web_trf", disable=["tagger", "parser", "attribute_ruler"])


    def predict(self, text):
        doc = self.nlp(text)
        entities = []
        for ent in doc.ents:
            entities.append({'text': ent.text, 'label': ent.label_})

        
        return entities
