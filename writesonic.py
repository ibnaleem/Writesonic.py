import requests

class Writesonic:
  def __init__(self, api_key:str, name:str = "Writesonic 1") -> None:
    self.api_key = api_key
    self.name = name

  def article_ideas(self, topic:str, primary_keyword:str = None, engine:str = "economy", language:str = "en", num_copies: int = 1):
    url = f"https://api.writesonic.com/v2/business/content/blog-ideas?engine={engine}&language={language}&num_copies={num_copies}"

    if not primary_keyword:
      payload = {"topic": topic}

    else:
      payload = {"topic": topic, "primary_keyword": primary_keyword}

    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "X-API-KEY": self.api_key
    }

    response = requests.post(url, json=payload, headers=headers)

    return response.text