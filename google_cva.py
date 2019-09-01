import base64
import json
from requests import Request, Session
from io import BytesIO
from PIL import Image

#PILで開いた画像をbase64形式に変換します
def pil_image_to_base64(pil_image):
    buffered = BytesIO()
    pil_image.save(buffered, format="PNG")
    str_encode_file = base64.b64encode(buffered.getvalue()).decode("utf-8")
    return str_encode_file

#PILで開いた画像をCloud Vision APIに投げます
def recognize_image(pil_image):
        #str_encode_file = pil_image_to_base64(pil_image)
        str_encode_file = pil_image
        str_url = "https://vision.googleapis.com/v1/images:annotate?key="
        str_api_key = "YOURS"
        str_headers = {'Content-Type': 'application/json'}
        str_json_data = {
            'requests': [
                {
                    'image': {
                        'content': str_encode_file
                    },
                    'features': [
                        {
                            'type': "TEXT_DETECTION",
                            'maxResults': 10
                        }
                    ]
                }
            ]
        }

        obj_session = Session()
        obj_request = Request("POST",
                              str_url + str_api_key,
                              data=json.dumps(str_json_data),
                              headers=str_headers
                              )
        obj_prepped = obj_session.prepare_request(obj_request)
        obj_response = obj_session.send(obj_prepped,
                                        verify=True,
                                        timeout=60
                                        )

        if obj_response.status_code == 200:
            with open('data.json', 'w') as outfile:
                json.dump(obj_response.json(), outfile)
                text = get_fullTextAnnotation(obj_response.text)
            return text

        else:
            return "error"

#返ってきたjsonデータの"fullTextAnnotation"部分のテキストを抽出します。
def get_fullTextAnnotation(json_data):
    text_dict = json.loads(json_data)
    try:
        text = text_dict["responses"][0]["fullTextAnnotation"]["text"]
        return text
    except:
        print(None)
        return None

def main(img_url):
    # image_path = img_url
    #pil_image = Image.open(image_path)
    return recognize_image(img_url)