import statistics
import plotly.figure_factory as ff
import pandas
import random

df = pandas.read_csv("data.csv")

data = df["Math_score"].tolist()
mean = statistics.mean(data)

def randomdata():
    e = []
    for l in range(0, 30):
        r = random.randint(0, len(data) - 1)
        value = data[r]
        e.append(value)

    mean2 = statistics.mean(e)
    return mean2

def setup():
    e = []
    for i in range(0, 100):
        newdata = randomdata()
        e.append(float(newdata))
    
    fig = ff.create_distplot([e], ["name"], show_hist=False)
    fig.show()

setup()
    


