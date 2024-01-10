# -*- coding: utf-8 -*-
"""

"""

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.gridspec as gs

def read_world_bank_data(file_path, skip_rows):
    """
    Reads and imports data from a CSV file into a Pandas DataFrame.

    Parameters:
    file_path (str): The path of the CSV file.
    skip_rows (int): The number of rows to skip.

    Returns:
    data (pd.DataFrame): The Pandas DataFrame containing the data.
    transposed_data (pd.DataFrame): The transposed DataFrame.
    """
    data = pd.read_csv(file_path, skiprows=skip_rows)
    data = data.drop(['Country Code', 'Indicator Code'], axis=1)
    transposed_data = data.set_index(data['Country Name']).T.reset_index().rename(columns={'index': 'Year'})
    transposed_data = transposed_data.set_index('Year').dropna(axis=1).drop(['Country Name'])
    return data, transposed_data

def select_indicators(data_frame, indicators):
    """
    Selects specific indicators from the World Bank DataFrame.

    Parameters:
    data_frame (pd.DataFrame): The World Bank DataFrame.
    indicators (list): List of indicator names.

    Returns:
    selected_indicators (pd.DataFrame): DataFrame with selected indicators.
    """
    selected_indicators = data_frame[data_frame['Indicator Name'].isin(indicators)]
    return selected_indicators

def select_countries(data_frame, countries):
    """
    Selects specific countries from the World Bank DataFrame.

    Parameters:
    data_frame (pd.DataFrame): The World Bank DataFrame.
    countries (list): List of country names.

    Returns:
    selected_countries (pd.DataFrame): DataFrame with selected countries.
    """
    selected_countries = data_frame[data_frame['Country Name'].isin(countries)].dropna(axis=1).reset_index(drop=True)
    return selected_countries

def group_and_clean_by_indicator(data_frame, indicator, countries):
    """
    Groups countries based on a specific indicator and cleans the data.

    Parameters:
    data_frame (pd.DataFrame): The World Bank DataFrame.
    indicator (str): The indicator name.
    countries (list): List of country names.

    Returns:
    grouped_and_cleaned_data (pd.DataFrame): Grouped and cleaned DataFrame.
    """
    grouped_and_cleaned_data = data_frame[data_frame["Indicator Name"] == indicator]
    grouped_and_cleaned_data = grouped_and_cleaned_data.set_index('Country Name').transpose().drop('Indicator Name')
    grouped_and_cleaned_data[countries] = grouped_and_cleaned_data[countries].apply(pd.to_numeric, errors='coerce', axis=1)
    return grouped_and_cleaned_data

def create_line_plot(data_frame, title, x_label, y_label):
    """
    Creates a line plot from the given DataFrame.

    Parameters:
    data_frame (pd.DataFrame): The DataFrame for plotting.
    title (str): Title of the plot.
    x_label (str): Label for the x-axis.
    y_label (str): Label for the y-axis.
    """
    plt.figure(figsize=(12, 8))
    data_frame.plot()
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.savefig(f"{title.replace(' ', '_')}_plot.png", dpi=300)  # Save the plot as a PNG file

def create_bar_plot(data_frame, title, x_label, y_label, start_index, end_index):
    """
    Creates a bar plot from the given DataFrame.

    Parameters:
    data_frame (pd.DataFrame): The DataFrame for plotting.
    title (str): Title of the plot.
    x_label (str): Label for the x-axis.
    y_label (str): Label for the y-axis.
    start_index (int): Start index for slicing the DataFrame.
    end_index (int): End index for slicing the DataFrame.
    """
    plt.figure(figsize=(12, 8))
    data_frame.iloc[start_index:end_index].plot(kind='bar')
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.savefig(f"{title.replace(' ', '_')}_plot.png", dpi=300)  # Save the plot as a PNG file

def create_horizontal_bar_plot(data_frame, title, x_label, y_label, start_index, end_index):
    """
    Creates a horizontal bar plot from the given DataFrame.

    Parameters:
    data_frame (pd.DataFrame): The DataFrame for plotting.
    title (str): Title of the plot.
    x_label (str): Label for the x-axis.
    y_label (str): Label for the y-axis.
    start_index (int): Start index for slicing the DataFrame.
    end_index (int): End index for slicing the DataFrame.
    """
    plt.figure(figsize=(12, 8))
    data_frame.iloc[start_index:end_index].plot(kind='barh')
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.savefig(f"{title.replace(' ', '_')}_plot.png", dpi=300)  # Save the plot as a PNG file

def create_pie_chart(data_frame, title):
    """
    Creates a pie chart from the given DataFrame.

    Parameters:
    data_frame (pd.DataFrame): The DataFrame for plotting.
    title (str): Title of the plot.
    """
    labels = data_frame.columns  # Use column names as labels
    plt.figure(figsize=(12, 6))
    plt.pie(data_frame.iloc[-1], labels=labels, autopct='%1.1f%%', startangle=0)
    plt.title(title)
    plt.savefig(f"{title.replace(' ', '_')}_plot.png", dpi=300)

def create_dashboard(line_data, bar_data, horizontal_bar_data, pie_data_a, student_name, student_id):
    """
    Creates a dashboard with multiple plots.

    Parameters:
    line_data, bar_data, horizontal_bar_data, pie_data_a (pd.DataFrame): DataFrames for each plot.
    student_name (str): Student's name.
    student_id (str): Student's ID.
    """ 
    plt.style.use('seaborn-darkgrid')  # Change the color theme here
    fig = plt.figure(figsize=(15, 18), dpi=300)
    gs_layout = gs.GridSpec(ncols=2, nrows=3, figure=fig, hspace=0.5, wspace=0.3)

    # Title
    plt.figtext(0.5, 0.95, 'Climate Change Data Study - World Bank Indicators', fontsize=16, ha='center', va='center')
    plt.figtext(0.5, 0.92, f'Student: {student_name}, ID: {student_id}', fontsize=12, ha='center', va='center')

    # Line Plot (Urban population)
    ax1 = fig.add_subplot(gs_layout[0, 0])
    line_data.plot(ax=ax1)
    ax1.set_title('Urban population', size=10, fontweight='bold')
    ax1.set_xlabel('Years')
    ax1.set_ylabel('Population In Millions')

    # Bar Plot (Electricity Output)
    ax2 = fig.add_subplot(gs_layout[0, 1])
    bar_data.iloc[6:10].plot(kind='bar', ax=ax2)
    ax2.set_title('Electricity Output', size=10, fontweight='bold')
    ax2.set_xlabel('Years')
    ax2.set_ylabel('% of total electricity output')

    # Horizontal Bar Plot (Urban Population)
    ax3 = fig.add_subplot(gs_layout[1, 0])
    horizontal_bar_data.iloc[6:10].plot(kind='barh', ax=ax3)
    ax3.set_title('Urban Population', size=10, fontweight='bold')
    ax3.set_xlabel('Population In Millions')
    ax3.set_ylabel('Years')

    # Bar Plot (Electricity Output)
    ax4 = fig.add_subplot(gs_layout[1, 1])
    bar_data.plot(ax=ax4)
    ax4.set_title('Electricity Output', size=10, fontweight='bold')
    ax4.set_xlabel('Years')
    ax4.set_ylabel('% of total electricity output')

    # Pie Chart A
    ax5 = fig.add_subplot(gs_layout[2, 0])
    ax5.pie(pie_data_a.iloc[-1], labels=pie_data_a.columns, autopct='%1.1f%%', startangle=0)
    ax5.set_title('Agricultural Land Distribution')

   
    # Add space and padding for the description
    plt.subplots_adjust(bottom=0.1, top=0.8)
    
    # Add the description
    description_text = """
In conclusion, analyzing data from six nations, my exploration of climate change drivers revealed significant insights into Agricultural land, Urban population, and Renewable power generation. The dynamic line and bar graphs vividly portrayed the ebb and flow of urban population trends, with China emerging as a leader in sheer numbers. The transition to a Bar Chart and Line Chart showcased the electrifying journey of global electricity production from 1996 to 1999, exposing unexpected energy consumption spikes despite a population growth slowdown. We unveiled the intricate relationships between population growth and energy consumption, highlighting China and India's minimal correlations and the United States' moderately positive association.
Fast-forwarding to 2010, a pie graph laid bare the percentage of agricultural land in square kilometers and its proportion to each country's total land area. Nigeria and South Africa were at the bottom, while China, the United States, and India claimed the spotlight.
In our concluding remarks, our scrutiny of climate change metrics from the World Bank showcased commendable progress in power access and ongoing urbanization. Yet, the stark reality of rising energy consumption intricately tied to population growth is a clarion call. The imperative now is clear: prioritize infrastructure expansion and champion sustainable energy policies to combat the relentless march of climate change."""
    
    plt.figtext(0.5, 0.05, description_text, fontsize=10, ha='center', va='bottom', wrap=True)
    # Save the dashboard as an image with the student ID in the filename
    plt.savefig(f"{student_id}.png", bbox_inches='tight', dpi=300)



# Data source: https://data.worldbank.org/topic/climate-change
file_path = 'WorldbankData.csv'
skip_rows = 4

data, transposed_data = read_world_bank_data(file_path, skip_rows)

# Indicators of interest
indicators = [
    'Arable land (% of land area)',
    'Renewable electricity output (% of total electricity output)',
    'Urban population',
    'Agricultural land (sq. km)'
]

# Selecting relevant indicators
selected_indicators = select_indicators(data, indicators)

# Countries of interest
countries_of_interest = ['United States', 'India', 'China', 'Nigeria', 'Germany', 'Japan']

# Selecting relevant countries
selected_countries = select_countries(selected_indicators, countries_of_interest)

# Grouping and cleaning data for specific indicators
urban_population_data = group_and_clean_by_indicator(selected_countries, 'Urban population', countries_of_interest)
electricity_output_data = group_and_clean_by_indicator(selected_countries, 'Renewable electricity output (% of total electricity output)', countries_of_interest)
agricultural_land_data = group_and_clean_by_indicator(selected_countries, 'Agricultural land (sq. km)', countries_of_interest)

# Creating plots
create_line_plot(urban_population_data, 'Urban population', 'Years', 'Population In Millions')
create_bar_plot(electricity_output_data, 'Electricity Output', 'Years', '% of total electricity output', 6, 10)
create_horizontal_bar_plot(urban_population_data, 'Urban Population', 'Population In Millions', 'Years', 6, 10)
create_bar_plot(electricity_output_data, 'Electricity Output', 'Years', '% of total electricity output', 0, None)

# Pie charts for agricultural and arable land
create_pie_chart(agricultural_land_data, 'Agricultural land (sq. km) 2010')

# Creating the dashboard
# Add your student name and ID
student_name = "Muhammad Asim"
student_id = "22100852"

create_dashboard(urban_population_data, electricity_output_data, urban_population_data,
                 agricultural_land_data, student_name, student_id)
