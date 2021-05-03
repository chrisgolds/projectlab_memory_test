import re
import datetime
import matplotlib.pyplot as plt

# Code for generating plot showing Microsoft Teams usage
ms_files = [
        "syrupy_20210429152226.ps.log",
        "syrupy_20210429152225.ps.log"
        ]
ms_labels = [
        "Microsoft Teams",
        "Microsoft Teams Helper (Renderer)"
        ]
fig, ax = plt.subplots()

for ms_file, ms_label in zip(ms_files, ms_labels):
    x = []
    y = []
    with open(ms_file) as f:
        for line in f:
            try:
                fields = line.split("\t")
                tab_fields = re.sub(r'\s+', '\t', fields[0]).split("\t")
                x.append(datetime.datetime.strptime(tab_fields[2] + " " + tab_fields[3],'%Y-%m-%d %H:%M:%S'))
                y.append(int(tab_fields[7]))
            except:
                pass
    plt.plot(x,y)
    fig.autofmt_xdate()
plt.title("Microsoft Teams - memory usage")
plt.ylabel("Memory (Kilobytes)")
plt.xlabel("Time")
plt.legend(ms_labels)
plt.show()

# Code for generating individual plots for Github and ProjectLab (local and production)
files = [
        "syrupy_20210429184128.ps.log",
        "syrupy_20210429194643.ps.log",
        "syrupy_20210429214616.ps.log"
        ]
labels = [
        "Github",
        "ProjectLab (local testing)",
        "ProjectLab (production testing)"
        ]

for file, label in zip(files, labels):
    x = []
    y = []
    fig, ax = plt.subplots()
    with open(file) as f:
        for line in f:
            try:
                fields = line.split("\t")
                tab_fields = re.sub(r'\s+', '\t', fields[0]).split("\t")
                x.append(datetime.datetime.strptime(tab_fields[2] + " " + tab_fields[3],'%Y-%m-%d %H:%M:%S'))
                y.append(int(tab_fields[7]))
            except:
                pass
    plt.plot(x,y)
    fig.autofmt_xdate()
    plt.title(label + " - memory usage")
    plt.ylabel("Memory (Kilobytes)")
    plt.xlabel("Time")
    plt.show()