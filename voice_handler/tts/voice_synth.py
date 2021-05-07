from aip import AipSpeech
from .secrets import API_SECRETS

APP_ID = API_SECRETS["APP_ID"]
API_KEY = API_SECRETS["API_KEY"]
SECRET_KEY = API_SECRETS["SECRET_KEY"]


def tts(synth_text):
    """
    Baidu Text-to-Speech API handler
    :param synth_text: Text to be synthesized
    :return: Voice file object
    """
    client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

    result = client.synthesis(
        text=synth_text,
        lang="zh",
        ctp=1,
        options={
            "vol": 5,
        },
    )

    if not isinstance(result, dict):
        return result
