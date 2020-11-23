import os
import re
import xlwt

def get_file_source(path):
  with open(path, 'r') as file:
    return file.read()

def get_tti_from_source(source):
  pattern = 'displayValue":"\d+.\d'
  all_findings = re.findall(pattern, source)
  tti = all_findings[9].replace('displayValue":"', '')
  return float(tti)

def get_report_time(report_name):
  time = (report_name
  .split('_')[2]
  .split('.')[0]
  .replace('-', ':'))
  return time

def save_ttis_to_excel(ttis):
  book = xlwt.Workbook()
  sh = book.add_sheet('tti_times')
  sh.write(0, 0, "Report")
  sh.write(0, 1, "Time of Execution")
  sh.write(0, 2, "Time to Interactive")

  i=2

  for (filename, time_of_execution, tti) in ttis:
      sh.write(i, 0, filename)
      sh.write(i, 1, time_of_execution)
      sh.write(i, 2, tti)
      i = i+1

  book.save("tti_times.xls")

def get_results(directory):
  ttis = []

  for filename in os.listdir(directory):
    source = get_file_source(f'{directory}/{filename}')
    tti = get_tti_from_source(source)
    time_of_execution = get_report_time(filename)
    ttis.append((filename, time_of_execution, tti))

  save_ttis_to_excel(ttis)

if __name__ == "__main__":
  get_results('reports')