import requests

class Photosonic:
  def __init__(self, api_key:str, name: str = "Photosonic 1") -> None:
    self.api_key = api_key
    self.name = name

def generate_image(self, prompt:str, num_images:int=None, image_width:int=None, image_height:int=None) -> str:
  
  """Generate images with prompts
  - Prompt Arg: Required
  - API Key: Required"""

  url = "https://api.writesonic.com/v1/business/photosonic/generate-image"

  payload = {
      "num_images": num_images,
      "image_width": image_width,
      "image_height": image_height,
      "prompt": f"{prompt}"
  }
  headers = {
      "accept": "application/json",
      "content-type": "application/json",
      "X-API-KEY": self.api_key
  }

  response = requests.post(url, json=payload, headers=headers)

  return response.text