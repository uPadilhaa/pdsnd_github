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
    while True:
        city = input("\nTo begin, enter the name of the city you want to explore. \nYour choice must be one of the cities in our system (New York City, Chicago or Washington). What's your choice?\n").lower()
        if city in CITY_DATA:
            break
        else:
            print("This option is not valid. Please write one of the options provided")

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input("\nWhat month do you want to search for ?. Your answer must be in one of the first 6 months of the year or every month, for example ('all', January, February, ..., June)\n").lower()
        if month in ['all', 'january', 'february', 'march', 'april', 'may', 'june']:
            break
        else:
            print("This option is not valid. Please write one of the options provided")

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input("\nWhat day do you want to search for ?. Your answer must be in one of the 7 days of the week or all days, for example ('all', Monday, Tuesday, Wednesday, ..., Sunday)\n").lower()
        if day in ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']:
            break
    else:
        print("This option is not valid. Please write one of the options provided")

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
    
    df['Start Time'] = pd.to_datetime(df['Start Time'])    
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1       
        df = df[df['month'] == month]
        
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]
        
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df['month'].mode()[0]
    print('The most common month is:', common_month)

    # TO DO: display the most common day of week
    common_day_of_week = df['day_of_week'].mode()[0]
    print('The most common day of week is:',common_day_of_week)

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    common_start_hour = df['hour'].mode()[0]
    print('The most common start hour is {}'.format(common_start_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print('The most commonly used start station is {}\n'.format(common_start_station))

    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print('The most commonly used end station is {}\n'.format(common_end_station))

    # TO DO: display most frequent combination of start station and end station trip
    df['combination'] = df['Start Station'] + ' till ' + df['End Station']
    most_combination = df['combination'].mode()[0]
    print('The most frequent combination of start station and end station trip is {}\n'.format(most_combination))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    t_travel_time = df['Trip Duration'].sum()
    print('The total travel time is {}'.format(t_travel_time))

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('The mean travel time is {}'.format(mean_travel_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print('Here is the counts of user types:\n', user_types)
    
    #The Chicago and New York City files also have the following two columns:
    if CITY_DATA == 'chicago' or CITY_DATA == 'new york city':
        # TO DO: Display counts of gender
        gender_types = df['Gender'].value_counts()
        print('Here is the counts of gender types:\n', gender_types)

    # TO DO: Display earliest, most recent, and most common year of birth
        earliest_yb = df['Birth Year'].min()
        print('Here is the earliest year of birth:\n', earliest_yb)
        most_recent_yb = df['Birth Year'].max()
        print('Here is the most recent year of birth:\n', most_recent_yb)
        most_common_yb = df['Birth Year'].mode()
        print('Here is the most common year of birth:\n', most_common_yb)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
    rd = 1
    while True:
        raw_data = input('\nWould you like to take a look at the first five lines of our raw data?. Please type yes or no!.\n')
        if raw_data.lower() not in ['yes', 'no']:
            raw_data = input('Just type yes or no please!')
        elif raw_data.lower() == 'yes':
            print(df[rd:rd+5])
            rd += 5
        else:
            break
       
            

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
