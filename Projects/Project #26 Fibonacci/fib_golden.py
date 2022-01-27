import math
import plotly.graph_objects as go

fib = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181]

golden = (1+math.sqrt(5))/2
fib_div = []

for i, f in enumerate(fib):
    try:
        fib_div.append(f/fib[i-1])
    except:
        pass

fib_golden_diff = [x - golden for x in fib_div]

fig = go.Figure(
    data=go.Scatter(y=fib_golden_diff,
                    mode='lines+markers'))

fig.update_layout(title='$\\text{Difference between} \\frac{F_n}{F_n-1} \\text{and the Golden Ratio}$',
                  xaxis_title='$F_n$',
                  yaxis_title='$\\text{diff}$')

fig.write_image("images/fib_golden.png")
