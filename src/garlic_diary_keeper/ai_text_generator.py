import random

from infrastructure.openai_client import OpenAIClient
from infrastructure.twitter_client import TwitterClient
from settings import settings


class AITextGenerator(object):
    def __init__(self):
        self.openai_client = OpenAIClient()
        self.twitter_client = TwitterClient()

    def generate(self) -> str:
        # トレンドを取得する
        trend_topic = self.twitter_client.get_trend_topic()
        # 文章を生成するための書き出しをランダムに取り出す
        prompt_template = random.choice(settings.openai_prompt_format_list)
        prompt = prompt_template.format(trend_topic)
        # 文章を生成する
        created_text = self.openai_client.create(prompt)
        return f'{prompt}{created_text}'
