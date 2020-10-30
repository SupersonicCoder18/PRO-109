import pandas as pd
import plotly.express as px
import plotly.figure_factory as ff
import statistics
import csv

df = pd.read_csv("Students.csv")
Read = df["reading score"].to_list()

ReadMean = statistics.mean(Read)

ReadMedian = statistics.median(Read)

ReadMode = statistics.mode(Read)

print("Mean, median, and mode of Reading Score is {}, {}, {} respectively".format(ReadMean, ReadMedian, ReadMode))

fig = ff.create_distplot([Read], ["Reading Score"], show_hist = False)
fig.show()

ReadStd = statistics.stdev(Read)

print("Standard deviation of Reading Score is {}".format(ReadStd))

ReadStd1Start, ReadStd1End = ReadMean - ReadStd, ReadMean + ReadStd
ReadStd2Start, ReadStd2End = ReadMean - ( 2* ReadStd), ReadMean + (2 * ReadStd)
ReadStd3Start, ReadStd3End = ReadMean - (3* ReadStd), ReadMean + (3* ReadStd)

ReadFirstStd = [result for result in Read if result > ReadStd1Start and result < ReadStd1End]
ReadSecondStd = [result for result in Read if result > ReadStd2Start and result < ReadStd2End]
ReadThirdStd = [result for result in Read if result > ReadStd3Start and result < ReadStd3End]

print("{} % of Reading Score lies with FirstStd".format(len(ReadFirstStd)*100/len(Read)))
print("{} % of Reading Score lies with SecondStd".format(len(ReadSecondStd)*100/len(Read)))
print("{} % of Reading Score lies with ThirdStd".format(len(ReadThirdStd)*100/len(Read)))