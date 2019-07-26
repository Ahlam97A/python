
from flask import Flask, render_template, request,jsonify
import requests
from onesignal import OneSignal, FilterNotification,SegmentNotification

app = Flask(__name__)

Filterclient = OneSignal("c9747114-c2ba-46e9-955a-3950b932e786", "N2I1ZjdlYzMtMjlmMS00ZmMwLTkwZDYtNWRmNWYwYjk0NTk0")
SegmentNotificationclient = OneSignal("c9747114-c2ba-46e9-955a-3950b932e786", "N2I1ZjdlYzMtMjlmMS00ZmMwLTkwZDYtNWRmNWYwYjk0NTk0")
#requests.post(    "https://onesignal.com/api/v1/notifications",    headers={"Authorization": "Basic N2I1ZjdlYzMtMjlmMS00ZmMwLTkwZDYtNWRmNWYwYjk0NTk0"})
data = {    "app_id": "c9747114-c2ba-46e9-955a-3950b932e786",    "included_segments": ["All"],    "contents": {"en": "ahlam"} ,"icon": "https://omaharentalads.com/images/vector-pizza-flat-design-3.png"}
requests.post(    "https://onesignal.com/api/v1/notifications",    headers={"Authorization": "Basic N2I1ZjdlYzMtMjlmMS00ZmMwLTkwZDYtNWRmNWYwYjk0NTk0"},    json=data)

if __name__ == '__main__':
    app.run()
#filter_notification = FilterNotification(    {        "en": "Hello from OneSignal-Notifications"    },    filters=[        Filter.Tag("my_key", "<", "5"),        "AND",        Filter.AppVersion(">", "5"),        "OR",        Filter.LastSession(">", "1"),    ])



