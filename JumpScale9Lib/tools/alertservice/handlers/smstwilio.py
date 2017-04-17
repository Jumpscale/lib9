from JumpScale import j
from JumpScale.tools.alertservice.AlertService import Handler
import requests


class TwilioSMSHandler(Handler):
    ORDER = 50

    def __init__(self, service):
        self.service = service
        self._baseurl = 'https://%(AccountSid)s:%(AuthToken)s@api.twilio.com/2010-04-01/Accounts/%(AccountSid)s/Messages'
        self.authurl = None
        if j.application.config.exists('twilio.accountsid'):
            accountinfo = {'AccountSid': j.application.config.get('twilio.accountsid'),
                           'AuthToken': j.application.config.get('twilio.authtoken')}
            self.authurl = self._baseurl % accountinfo
            self.fromnr = j.application.config.get('twilio.from')

    def escalate(self, alert, users):
        if not self.authurl:
            return
        numbers = set()
        for user in users:
            if users['mobile']:
                if isinstance(users['mobile'], list):
                    numbers.append(users['mobile'][0])
                else:
                    numbers.append(users['mobile'])
        message = self.makeMessage(alert)
        for nr in numbers:
            requests.post(self.auth, data={'From': self.fromnr, 'To': nr, 'Body': message}, verify=False)
        return users

    def makeMessage(self, alert):
        alert['url'] = self.service.getUrl(alert)
        message = """Level: %(level)s
Details: %(url)s
Message: %(errormessage)s
""" % alert
        return message
