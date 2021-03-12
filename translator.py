"""
this is simple language translator program which uses watson language translator api
"""
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator


def translator(text, lang):
    """
    authentication with the ibm language translator instance/function returns a dictionary with
    the translated text
    """
    authenticator = IAMAuthenticator('aqN9P5bdcTcFD-fNty-Ag1R6Azc82p1HbxfTX6B_GXDP')
    language_translator = LanguageTranslatorV3(version='2018-05-01', authenticator=authenticator)
    language_translator.set_service_url(
        'https://api.us-south.language-translator.watson.cloud.ibm.com/instances/2598d376-0b24-4053-a279-aeabd167e5a8')
    translation = language_translator.translate(text=text, model_id=lang).get_result()
    return translation


def english_to_french(text_to_translate):
    """
    function returns a string of the translated text in french
    """
    dictionary = translator(text_to_translate, 'en-fr')
    translated_text = dictionary['translations'][0]['translation']
    return translated_text


def english_to_german(text_to_translate):
    """
    function returns a string of the translated text in german
    """
    dictionary = translator(text_to_translate, 'en-de')
    translated_text = dictionary['translations'][0]['translation']
    return translated_text


# getting the input string in english from the user
input_text = input('Enter an English text to translate : ')
print(english_to_french(input_text))
print(english_to_german(input_text))
