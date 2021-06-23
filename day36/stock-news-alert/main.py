from alertmgr import AlertManager

alert = AlertManager("ORPH")

if abs(alert.percent_change) >= 5:
    alert.send_alert()

