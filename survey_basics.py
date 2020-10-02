from surveygizmo import SurveyGizmo
key = ""
secret = ""

client = SurveyGizmo(
    api_version='v4',

    # example token from SurveyGizmo docs
    api_token = key,
    api_token_secret = secret
)

for i in client.api.survey.list()["data"]:
    print(i["title"])
    
client.api.survey.filter('createdon', '>=', '2020-01-01').list()
