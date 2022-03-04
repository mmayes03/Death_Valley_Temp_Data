import csv
from datetime import date, datetime
from matplotlib import pyplot as plt

filename = 'csv_files/death_valley_2014.csv'

with open(filename) as f:
    reader = csv.reader(f)
    header_read = next(reader)
    # for index, column_title in enumerate(header_read):
    #     print(index, column_title)
    dates, high_temps, low_temps = [], [], []
    for row in reader:
        try:
            current_date = datetime.strptime(row[0], '%Y-%m-%d')
            ht = int(row[1])
            lw = int(row[3])
        except ValueError:
            print(current_date, 'missing data')
        else:
            high_temps.append(ht)
            low_temps.append(lw)
            dates.append(current_date)

fig = plt.figure(dpi=128, figsize=(10,5))
plt.plot(dates, high_temps, c = 'red', alpha = 0.5)
plt.plot(dates, low_temps,  c = 'blue', alpha = 0.5)
plt.fill_between(dates, high_temps, low_temps, facecolor = 'grey', alpha = 0.2)
plt.title('Daily high and low temperatures - 2014\nDeath Valley, CA', fontsize = 20)
# plt.ticklabel_format(axis = 'y', style= 'plain')
plt.xlabel('', fontsize = 14)
fig.autofmt_xdate()
plt.ylabel('Temperature(F)', fontsize = 14)
plt.tick_params(axis= 'both', which = 'major', rotation=45, labelsize = 16)
plt.show()
plt.savefig('Death_Valley_Temp_Data.png')