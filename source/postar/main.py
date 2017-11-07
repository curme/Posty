#   @author_group  [huizhan,]

from configparser import ConfigParser
from flask import Flask, Response

from manager import Manager as PostarManager


# create app
app = Flask(__name__)
# load app config info
config = ConfigParser()
config.read("system.cfg")

# create app manager
postar = PostarManager(config)


#   @brief  API
#           retrieve open survey questions
@app.route('', methods=['POST'])
def get_open_survey_api():
    pass



#   @brief  API
#           retrieve private survey questions
@app.route('', methods=['POST'])
def get_private_survey_api():
    pass



#   @brief  API
#           upload open survey questions
@app.route('', methods=['POST'])
def upload_open_survey_api():
    pass



#   @brief  API
#           upload commercial survey questions
@app.route('', methods=['POST'])
def upload_private_survey_api():
    pass



if __name__ == "__main__":
    
    # app start
    host = config.get('APP', 'host')
    port = config.get('APP', 'port')
    app.run(host=host, port=int(port), debug=True)