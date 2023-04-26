from flask import *
from datetime import datetime
import pytz
import openai
import simplejson as json

openai.api_key = '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'
app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False


def generate_response(prompt: str) -> str:
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": f"{prompt}"}
        ]
    )
    return completion.choices[0].message.content



@app.route('/', methods=['GET'])
def main_page():
    country_time_zone = pytz.timezone('Asia/Tehran')
    country_time = datetime.now(country_time_zone)
    msg = str(request.args.get('Message'))
    data = {'Page': 'GPT',
                       'Made_by': 'Javad_exe',
                       'Rubika_id': '@Javad_exe',
                       "Message":{'GPT_Message': f"{generate_response(msg)}",
                                  'Date_requested': country_time.strftime("%d-%m-%y"),
                                  'Time_requested': country_time.strftime("%H:%M:%S")
                                  }
                       }
    response_data = json.dumps(data, ensure_ascii=False)
    response = Response(
        response=response_data,
        status=200,
        mimetype='application/json'
    )
    response.headers['Content-Type'] = 'application/json; charset=utf-8'
    return response

if __name__ == '__main__':
    app.run()