from datetime import datetime, date
import statistics

from flask import Flask, render_template, request, flash, redirect, url_for

from bokeh.plotting import figure, output_file, show
from bokeh.layouts import gridplot
from bokeh.embed import components


def history(path, daystring, submit):
    time_arr = []
    lux = []
    try:
        with open(path, 'r') as f:
            for line in f:
                data = line.split()
                time = data[0].strip().strip('*\x00')
                time = datetime.strptime(time, '%H:%M:%S')
                today = date.today()
                time = time.replace(year=today.year, month=today.month, day=today.day)
                time_arr.append(time)
                lux.append(float(data[1]))
        lux_max = max(lux)
        lux_min = min(lux)
        lux_av = statistics.mean(lux)
        datadic = {
            "day" : today,
            "time" : time.strftime("%H:%M:%S"),
            "lux" : lux,
            "maxlux" : lux_max,
            "minlux" : lux_min,
            "avlux" : lux_av
            }

        lux_plot = figure(title="Lux", x_axis_label='Time', y_axis_label='Lux',
                   x_axis_type='datetime')
        lux_plot.sizing_mode = 'scale_width'
        lux_plot.circle(time_arr, lux, size=5)
        lux_plot.line(time_arr, lux_max, legend_label="Max lux today: %f" % lux_max,
                     line_color="red")
        lux_plot.line(time_arr, lux_av, legend_label="Average lux today: %f" % lux_av,
                     line_color="yellow")
        lux_plot.line(time_arr, lux_min, legend_label="Min lux today: %f" % lux_min,
                     line_color="blue")
        luxplots = {'plot' : lux_plot}
        luxplot = components(luxplots)

        days = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]
        months = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
        years = [2020, 2021]


        return render_template("history.html", data_date=data_date.strftime('%Y-%m-%d'),
                                luxplot=luxplot, submit=submit, days=days, months=months, years=years)
    except FileNotFoundError:
        flash('No data on that day')
        return redirect(url_for('history_'))

    except IndexError:
        flash('Bad data on that day')
