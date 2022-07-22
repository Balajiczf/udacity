import time
import pandas as pd
import numpy as np
import statistics

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
    city = input("Type city name: ")
    city=city.lower()
    check=True
    while(check==True):
        if(CITY_DATA.get(city)!=None):
            check=False
        else:
            city = input("Type a valid city name: ")
    
    # TO DO: get user input for month (all, january, february, ... , june)
    month = input("Type month name/all: ")
    month=month.lower()

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input("Type the day/all: ")
    day=day.lower()


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
    #print(city)
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])
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
    # TO DO: display the most common month
    print('the most common month is')
    print(df['month'].mode()[0])


    # TO DO: display the most common day of week
    print('the most common day of week is')
    print(df['day_of_week'].mode()[0])

    # TO DO: display the most common start hour
    print('the most common start hour is')
    print(df['Start Time'].mode()[0])


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print('the most common start Station is')
    print(df['Start Station'].mode()[0])


    # TO DO: display most commonly used end station
    print('the most common end station is')
    print(df['End Station'].mode()[0])


    # TO DO: display most frequent combination of start station and end station trip
    print('the most common end station is')
    print((df['Start Station']+ df['End Station']).mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    print(df.dtypes)
    # TO DO: display total travel time
    delta = df['End Time'] - df['Start Time']
    df['diff'] = delta.dt.days.astype(float) + (delta.dt.seconds.astype(float) / 86400)
    print('total travel time: ')
    print(sum(df['diff']))
    


    # TO DO: display mean travel time
    print('mean travel time: ')
    print(statistics.mean(df['diff']))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print('count of user types: ')
    print(df.groupby('User Type')['User Type'].count())

    # TO DO: Display counts of gender
    try:
        print('count of Gender: ')
        print(df.groupby('Gender')['Gender'].count())
    except KeyError:
        print('Gender stats cannot be calculated because Gender does not appear in the dataframe')
    


    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        print('earliest year of birth')
        print(min(df['Birth Year']))
        print('most recent year of birth')
        print(max(df['Birth Year']))
        print(' most common year of birth')
        print(df['Birth Year'].mode()[0])
    except KeyError:
        print('Birth Year stats cannot be calculated because Birth Year does not appear in the dataframe')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    sc=True
    while sc:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            #break
            view_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n')
            start_loc = 0
            sc=True
            while (view_data.lower()=='yes'):
                print(df.iloc[start_loc:start_loc+5])
                start_loc += 5
                view_data = input("Do you wish to continue?: ").lower()
                if(view_data.lower()=='no'):
                    sc=False
          


if __name__ == "__main__":
	main()
