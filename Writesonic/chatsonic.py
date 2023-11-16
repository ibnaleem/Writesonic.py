import requests


class Chatsonic:
    def __init__(self, api_key: str, name: str = "Chatsonic 1") -> None:
        self.api_key = api_key
        self.history_data = []
        self.name = name

    @property
    def api_key(self) -> str:
        return self._api_key

    @api_key.setter
    def api_key(self, value: str) -> None:
        self._api_key = value

    def conversation(
        self,
        input_text: str,
        language: str = "en",
        enable_google_results: bool = True,
        enable_memory: bool = True,
    ) -> str:
        url = f"https://api.writesonic.com/v2/business/content/chatsonic?engine=premium&language={language}"

        payload = {
            "enable_google_results": str(enable_google_results).lower(),
            "enable_memory": enable_memory,
            "input_text": input_text,
        }

        headers = {
            "accept": "application/json",
            "content-type": "application/json",
            "X-API-KEY": self.api_key,
        }

        response = requests.post(url, json=payload, headers=headers)

        if enable_memory:
            # Parse the JSON response
            response_data = response.json()

            # Access the "message" field
            message = response_data.get("message")

            self.history_data.append(
                {"is_sent": True, "message": input_text},
                {"is_sent": False, "message": message},
            )

        else:
            pass

        return response.text
