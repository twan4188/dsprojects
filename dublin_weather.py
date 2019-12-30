from matplotlib import pyplot as plt

x = range(12)
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
perc = [78, 80, 82, 84, 86, 88]
percentages = ['78%', '80%', '82%', '84%', '86%', '88%']

y1 = [8, 8, 10, 12, 15, 18, 20, 19, 17, 14, 10, 8]
y2 = [2, 2, 3, 5, 7, 10, 12, 12, 10, 7, 5, 3]

precipation = [65, 50, 55, 55, 60, 65, 55, 75, 60, 80, 75, 75]
sunshine = [2, 3, 4, 5, 6, 6, 5, 5, 4, 3, 2, 2]
hum = [86, 84, 82, 80, 79, 79, 81, 82, 83, 85, 87, 87]

#function calculating the average temperatures from two lists

def avg(lst1, lst2):
    mean_temp = []
    for i in range(len(lst1)):
        avg_temp = (lst1[i]+lst2[i])/2
        mean_temp.append(avg_temp)
    return mean_temp

y3 = avg(y1,y2)

#first subplot for avg temperatures

plt.figure(figsize=(12,8))
ax1 = plt.subplot(2,2,1)
plt.plot(x, y1, color='red', marker='o')
plt.plot(x, y2, color='blue', marker='o')
plt.plot(x, y3, color='orange', marker='o')

plt.title('Average Temperature in Dublin')
plt.ylabel('Temperature in C')
plt.legend(['Max Temperature', 'Min Temperature', 'Avg Temperature'])

ax1.set_xticks(x)
ax1.set_xticklabels(months)

#second subplot for avg precipation

ax2 = plt.subplot(2,2,2)
plt.plot(x, precipation, color='blue', marker='o')
plt.axis([0,11,0,100])

plt.title('Average Precipation in Dublin')
plt.ylabel('Precipation in MM')
ax2.set_xticks(x)
ax2.set_xticklabels(months)

#third subplot for avg hours of sunshine

ax3 = plt.subplot(2,2,3)
plt.plot(x, sunshine, color='orange', marker='o')
plt.axis([0,11,0,7])

plt.title('Average Hours of Sunshine in Dublin')
plt.ylabel('Hours of Sun')
ax3.set_xticks(x)
ax3.set_xticklabels(months)

ax4 = plt.subplot(2,2,4)
plt.plot(x, hum, color='blue', marker='o')
#plt.axis([0,11,75,90])

#fourth subplot for avg humidity

plt.title('Average Humidity in Dublin')
ax4.set_xticks(x)
ax4.set_xticklabels(months)
ax4.set_yticks(perc)
ax4.set_yticklabels(percentages)

plt.subplots_adjust(hspace=.35)
plt.savefig('dublin_weather.png')
plt.show()