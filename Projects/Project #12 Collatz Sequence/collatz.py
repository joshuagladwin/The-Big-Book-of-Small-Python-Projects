"""Collatz Sequence, by Al Sweigart al@inventwithpython.com
Generates numbers for the Collatz sequence, given a starting number.
More info at: https://en.wikipedia.org/wiki/Collatz_conjecture
View the original code at https://nostarch.com/big-book-small-python-projects
Tags: tiny, beginner, math"""

import sys, time
import plotly.graph_objects as go
import pandas as pd
import numpy as np

print('''Collatz Sequence, or, the 3n + 1 Problem
By Al Sweigart al@inventwithpython.com

The Collatz sequence is a sequence of numbers produced from a starting
number n, following three rules:

1) If n is even, the next number n is n / 2.
2) If n is odd, the next number n is n * 3 + 1.
3) If n is 1, stop. Otherwise, repeat.

It is generally thought, but so far not mathematically proven, that
every starting number eventually terminates at 1.
''')

print('Enter a starting number (greater that 0) or QUIT:')
response = input('> ')

if not response.isdecimal() or response == '0':
    print('You must enter an integer greater than 0.')
    sys.exit()

n = int(response)
print(n, end='', flush=True)
while n != 1:
    if n % 2 == 0:  # If n is even...
        n = n // 2
    else:  # Otherwise, n is odd...
        n = 3 * n + 1

    print(', ' + str(n), end='', flush=True)
    time.sleep(0.1)
print()

end = int(response)

list_n = []

for i in range(1, end+1):
    n = i
    while n != 1:
        list_n.append((i, n))
        if n % 2 == 0:  # If n is even...
            n = n // 2
        else:  # Otherwise, n is odd...
            n = 3 * n + 1
    list_n.append((i, n))

df = pd.DataFrame(list_n, columns=['i', 'n'])

df_n = df[df['i'] == end]

fig1 = go.Figure()

if len(df_n) <= 31:
    text= df_n['n']
else:
    text=''

fig1.add_trace(go.Scatter(x=np.linspace(0, len(df_n), len(df_n), endpoint=True), y=df_n['n'],
                         text=text, textposition='bottom center', mode="lines+markers+text",
                         marker=dict(size=8), line=dict(width=1, dash='dot')))
fig1.update_layout(
    title=f'Collatz Sequence for n={end}',
    showlegend=False,
    xaxis=dict(title='Step'),
    yaxis=dict(title='n'),
)

fig1.write_image(f"images/collatz_sequence_n{end}.png")

df_count = df.groupby(['i'], as_index=False).count()\
             .rename(columns={'n': 'steps'})

fig2 = go.Figure()
fig2.add_trace(go.Scatter(x=df_count['i'], y=df_count['steps'], mode="markers",
                         marker=dict(size=8, opacity=0.4)))
fig2.update_layout(
    title='Collatz Sequence - Number of Steps to Reach n=1',
    showlegend=False,
    xaxis=dict(title='Starting n'),
    yaxis=dict(title='Steps'),
)

fig2.write_image(f"images/collatz_sequences_num_steps_n{end}.png")