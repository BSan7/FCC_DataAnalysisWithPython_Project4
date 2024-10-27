import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv', parse_dates = True, index_col = 'date')

# Clean data
df = df[
        (df['value'] <= df['value'].quantile(0.975)) &
        (df['value'] >= df['value'].quantile(0.025))
        ]


def draw_line_plot():
    # Draw line plot
    fig = plt.figure(figsize = (32,10))
    ax = fig.add_subplot(111)
    
    ax.plot(df.index, df['value'], 'r-')
    ax.set_xlabel('Date', fontsize = 20)
    ax.set_ylabel('Page Views', fontsize = 20)
    ax.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019', fontsize = 22)




    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig


def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()
    
    df_bar['year'] = df_bar.index.year.values
    df_bar['month'] = df_bar.index.month_name()

    months_list = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    

    # Draw bar plot
    fig = plt.figure(figsize=(15.14, 13.30))
    ax = fig.add_subplot(111)
    
    ax = sns.barplot(x = df_bar['year'],  hue = df_bar['month'], y = df_bar['value'], hue_order = months_list, palette = sns.color_palette())
    ax.set_xlabel('Years', fontsize = 20)
    ax.set_ylabel('Average Page Views', fontsize = 20)
    ax.legend(title = 'Months')


    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig


def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]
    
    months_list = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

    # Draw box plots (using Seaborn)
    fig = plt.figure(figsize = (28.8, 10.8))
    
    ax1 = fig.add_subplot(121)
    ax1 = sns.boxplot(x = df_box['year'], y = df_box['value'])
    ax1.set_xlabel('Year')
    ax1.set_ylabel('Page Views')
    ax1.set_title('Year-wise Box Plot (Trend)')
    
    ax2 = fig.add_subplot(122)
    ax2 = sns.boxplot(x = df_box['month'], y = df_box['value'], order = months_list)
    ax2.set_xlabel('Month')
    ax2.set_ylabel('Page Views')
    ax2.set_title('Month-wise Box Plot (Seasonality)')
     






    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig

