import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    
    city = input("Would you like to see data for Chicago, New York City or Washinton?").lower()
    while city not in (CITY_DATA.keys()):
        city = input("invalid city! please enter Chicago, New York City or Washinton").lower()

    filter_option = input ("would you like to filter by month, day or not at all? enter \"none\" for no filter ").lower()
    while filter_option not in ["month","day","none"]:
        filter_option = input ( "please enter month, day or none?").lower()
    # TO DO: get user input for month (all, january, february, ... , june)
    months = ["january","february","march","april","may","june"]
    if filter_option == "month":
        month = input ("Which month? January, February , March, April, May, June?").lower()
        while month not in months:
            month = input ("Which month? January, February , March, April, May, June?").lower()
    else:
        month = "all"
            
    

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    days = ["mo","tu","w","th","f","sa","su"]
    if filter_option == "day":
        day = input ("Which day? M, Tu, W, Th, F, Sa, Su?").lower()
        while day not in days:
            day = input ("Invalid input ... Which day? M, Tu, W, Th, F, Sa, Su?").lower()
    else:
        day = "all"

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])
    df ["Start Time"] = pd.to_datetime(df["Start Time"])
    df ["month"] = df["Start Time"].dt.month
    df ["day_of_week"] = df["Start Time"].dt.day_name()
    
    if month != "all":
        months = ["january","february","march","april","may","june"]
        month = months.index(month) + 1
        df = df [df["month"] == month]
        
        
    if day != "all":
        df = df [df["day_of_week" == day.title()]]


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    month = df['month'].mode()[0]
    months = ["january","february","march","april","may","june"]
    print('the most common month is: {}'.format(months[month-1]))


    # TO DO: display the most common day of week
    day = df ['day_of_week'].mode()[0]
    print("the most common day of the week is: ", day )
                 

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    common_hour = df['hour'].mode()[0]
    print("the most common hour is: " , common_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_common_start_station = df['Start Station'].mode()[0]
    print("the most common start statin is: " , most_common_start_station)

    # TO DO: display most commonly used end station
    most_common_end_station = df['End Station'].mode()[0]
    print("the most common end statin is: " , most_common_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    trip = df['Start Station'] + ' , '+ df['End Station']
    frequent_trip = trip.mode()[0]
    print("the most frequent trip is: " , frequent_trip)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time            
    print ('Total travel time is: ', df['Trip Duration'].sum())

    # TO DO: display mean travel time
    print ('Average travel time is: ', df['Trip Duration'].mean())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print('number of user types is: ', user_types)

    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
       gender = df['Gender'].value_counts()   
       print(gender)


    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
       earliest_year = df['Birth Year'].min()
       most_recent_year = df['Birth Year'].max()
       most_common_year = df['Birth Year'].mode()[0]
       print('The earliest year is: ', earliest_year)
       print('The most recent year is: ', most_recent_year)
       print('the most common year is: ',most_common_year)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    


def display_raw_data(df):
    input = input('would you like to display the first 5 raws?')
    if input.lower() == 'yes':
        count = 0
        while True:
            print(df.iloc[count:count+5])
            count += 5 
            again = input('would you like to display the next 5 raws')
            if again.lower() != 'yes':
                break


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
