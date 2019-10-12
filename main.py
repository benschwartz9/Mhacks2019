# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# [START gae_python37_render_template]

from flask import Flask, render_template, redirect, url_for, request

import inputText
import urlReader

app = Flask(__name__)

@app.route('/')
def root():
    #result = web_scrape.quickResult()
    #result = inputText.simpleReturn()
    #result2 = urlReader.urlSearch()

    return render_template('index.html')#, result=result, result2=result2)

@app.route('/test/')
def test():
    #result = web_scrape.quickResult()
    return redirect(url_for('results', inptType="url", inpt="faeffa"))

@app.route('/results/<inptType>/<inpt>')
def results(inptType, inpt):
    if not inptType or not inpt:
        return redirect(url_for('/'))

    result = None
    if inptType == "url":
        result = urlReader.analyze(inpt)
    else:
        result = inputText.analyze(inpt)
    #result = inputText.simpleReturn()
    #result2 = urlReader.urlSearch()

    return render_template('results.html', result=result)


#Handle URL
@app.route('/handle_URL', methods=['POST'])
def handle_URL():
    url = request.form['articleURL']
    return redirect(url_for('results', inptType="url", inpt=url))


#Handle Text
@app.route('/handle_text', methods=['POST'])
def handle_text():
    text = request.form['articleText']
    return redirect(url_for('results', inptType="text", inpt=text))

if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    # Flask's development server will automatically serve static files in
    # the "static" directory. See:
    # http://flask.pocoo.org/docs/1.0/quickstart/#static-files. Once deployed,
    # App Engine itself will serve those files as configured in app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)

# [START gae_python37_render_template]
