import requests


class Surveymethods:

    def __init__(self,apikey, login):
        self.apikey = apikey
        self.login = login


    def getAllSurveyCodes(self):
        """
        returns all surveys and their codes without pagination.
        :return: json format
        """
        url = "https://api.surveymethods.com/v1/%s/%s/integrations/surveycodes/" %(self.login,self.apikey)

        return self.apiRequest(url)

    def getSurveyCodeForSurvey(self,survey):
        """
        returns the code for a given survey title (string
        :param survey: string of survey title
        :return: returns the code
        """

        allCodes = self.getAllSurveyCodes()

        surveyCode = ""
        for item in allCodes['surveys']:
            if item['title'].lower() == survey.lower():
                surveyCode = item['code']

        return surveyCode



    def getResponseCodes(self,surveyCode):
        """
        returns all response codes for a given survey
        :param surveyCode: code of the wanted survey
        :return: json format
        """
        url = "https://api.surveymethods.com/v1/%s/%s/responses/%s/codes" %(self.login,self.apikey,surveyCode)

        return self.apiRequest(url)

    def getSpecificResponse(self,surveyCode,responseCode):

        url = "https://api.surveymethods.com/v1/%s/%s/responses/%s/detail/%s/" %(self.login,self.apikey,surveyCode,responseCode)

        return self.apiRequest(url)


    def apiRequest(self, url):

        response = requests.get(url)

        return response.json()