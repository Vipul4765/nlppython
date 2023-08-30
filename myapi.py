# Import
import paralleldots


class API:
    def __init__(self):
        paralleldots.set_api_key('quA7Gu1OfXCeRxfgmsPjhOSUYjVxGFW4KCVWAwlgulI')

    def sentiment_result(self, text):
        response = paralleldots.sentiment(text)
        return response

    def ner(self,text):
        response = paralleldots.ner(text)
        return response

    def emotion(self,text):
        response = paralleldots.batch_emotion(text)
        return response



