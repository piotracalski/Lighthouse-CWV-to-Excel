import os
import json
import xlwt
import time

reports_directory = 'reports'

def read_report(path):
  with open(path) as f:
    data = json.load(f)
    return data

def get_tti_from_report(report):
  try:
    value = round(float(report['audits']['interactive']['numericValue']))
  except:
    value = 'No result'
  return value

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
  sh = book.add_sheet('tti_times')
  sh.write_merge(0, 1, 0, 0, 'URL')
  sh.write(0, 1, 'Fetch time')
  sh.write(0, 2, 'Time to interactive')

  sh.write(1, 1, f'[UTC{"%+d" % int(-float(time.timezone / 3600))}]')
  sh.write(1, 2, '[ms]')

  i=2

  for (url, fetch_time, tti) in samples:
      sh.write(i, 0, url)
      sh.write(i, 1, fetch_time)
      sh.write(i, 2, tti)
      i = i+1

  book.save('tti_times.xls')

def get_results(directory):
  samples = []

  for filename in os.listdir(directory):
    report = read_report(f'{directory}/{filename}')
    tti = get_tti_from_report(report)
    fetch_time = get_fetch_time_from_report(report)
    requested_url = get_url_from_report(report)
    samples.append((requested_url, fetch_time, tti))

  save_samples_to_excel(samples)

if __name__ == "__main__":
  get_results(reports_directory)