import os
import json
import xlwt
import time

def read_JSON_file(path):
  with open(path) as f:
    data = json.load(f)
    return data

env_data = read_JSON_file('env_data.json')

def get_metrics_from_report(report):
  values = []
  for metric in env_data['metrics']:
    try:
      value = report['audits']['metrics']['details']['items'][0][metric['report_key']]
      value = round(value, 1) if metric['unit'] == '[s]' else value
    except:
      value = 'No result'
    finally:
      values.append(value)
  return values

def get_fetch_time_from_report(report):
  value = report['fetchTime'][11:-1]
  if time.timezone != 0:
    value = adjust_time(value)
  return value

def get_url_from_report(report):
  value = report['requestedUrl']
  return value

def adjust_time(time_value):
  hour = time_value[:2]
  if hour == '23':
    hour = '00'
  else:
    adjustment = time.timezone / 3600
    hour = f'{int(int(hour) - adjustment)}'
  return f'{hour}{time_value[2:]}'  

def save_samples_to_excel(samples):
  book = xlwt.Workbook()
  sh = book.add_sheet('core_web_vitals')
  sh.write_merge(0, 1, 0, 0, 'URL')
  sh.write(0, 1, 'Fetch time')
  j = 2
  for metric in env_data['metrics']:
    sh.write(0, j, metric['label'])
    sh.write(1, j, metric['unit'])
    j += 1

  sh.write(1, 1, f'[UTC{"%+d" % int(-float(time.timezone / 3600))}]')

  i = 2
  j = 2

  for (url, fetch_time, values) in samples:
      sh.write(i, 0, url)
      sh.write(i, 1, fetch_time)
      for value in values:
        sh.write(i, j, value)
        j += 1   
      i += 1
      j = 2

  book.save('core_web_vitals.xls')

def get_results(directory):
  samples = []

  for filename in os.listdir(directory):
    report = read_JSON_file(f'{directory}/{filename}')

    values = get_metrics_from_report(report)
    fetch_time = get_fetch_time_from_report(report)
    requested_url = get_url_from_report(report)
    samples.append((requested_url, fetch_time, values))

  save_samples_to_excel(samples)

if __name__ == "__main__":
  get_results(env_data["reports_directory"])