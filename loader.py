import requests
from datetime import date, timedelta

def get_earnings(username, password, vendor_id, report_type, date_type, report_subtype, report_date):
    params = ({
        "USERNAME" : username,
        "PASSWORD" : password,
        "VNDNUMBER" : vendor_id,
        "TYPEOFREPORT" : report_type,
        "DATETYPE" : date_type,
        "REPORTTYPE" : report_subtype,
        "REPORTDATE" : report_date
    })

    url_base = "https://reportingitc.apple.com/autoingestion.tft?"

    headers ={"Content-Type" : "application/x-www-form-urlencoded"}

    r = requests.post(url_base, headers = headers, params = params)

    if 'errormsg' in r.headers:
        print r.headers['errormsg']
    elif 'filename' in r.headers:
        filename = r.headers['filename']
        attachment = r.content
        output = open(filename, 'wb')
        output.write(attachment)
        output.close()
    else:
        print "An unexpected error occurred."

if __name__ == '__main__':

    yesterday = date.today() - timedelta(days=1)

    username = 'yourcoolusernamehere@yourdomain.com'
    password = 'yourawesomepassword'
    vendor_id = 'a_bunch_of_numbers'
    report_type = 'Sales'
    date_type = 'Daily'
    report_subtype = 'Summary'
    report_date = yesterday.strftime('%Y%m%d')

    get_earnings(username, password, vendor_id, report_type, date_type, report_subtype, report_date)

