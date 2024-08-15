# third-party Packages
import time
import pandas as pd
import numpy as np

CITY_DATA = { 'Chicago': 'C:\\Yaser\Data Analysis\9 Project\chicago.csv',
              'New York City': 'new_york_city.csv',
              'Washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!', "\nyou can explors data about chicago, new york and washington cities")
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    #make list of available cities to explore
    cities = ["Chicago", "New York City", "Washington"]
    #Take user raw input for city
    city = input("What city do you want to analyze?\n").title()
    #Make a while loop to check if the user input is one of the available cities to explore (handle invalid inputs)
    while city not in cities:
        print("City name is invalid, please input city name correctly")
        # Ask the user again to input the correct city name
        city = input("What city do you want to analyze?\n").title()

    # TO DO: get user input for month (all, january, february, ... , june)
    #make list of available months to explore
    months = ["January", "February", "March", "April", "May", "June", "All"]
    print("List of available months to explore = [January, February, March, April, May, June, All]")
    month = input("What month do you want to analyze?\n").title()
    while month not in months:
        print("Month is invalid, please input Month correctly")
        # Ask the user again to input the correct month
        month = input("What month do you want to analyze?\n").title()

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    #make list of available days to explore
    days = ["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "All"]
    day = input("What day do you want to analyze?\n").title()
    while day not in days:
        print("day is invalid, please input day correctly")
        # Ask the user again to input the correct day
        day = input("What day do you want to analyze?\n").title()


    print('-'*40)
    print(city, month, day)
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
# load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city], encoding= 'Latin1', low_memory=False)

# convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

# extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month_name()
    df['day_of_week'] = df['Start Time'].dt.day_name()

    # filter by month if applicable
    if month != 'All':
        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'All':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day]
    return df

def time_stats(df, month, day):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # TO DO: display the most common month
    if month == "All":
        most_common_month = df['month'].mode()[0]
        print("Most_common_month is: ", most_common_month)

    # TO DO: display the most common day of week
    if day == "All":
        most_common_day = df['day_of_week'].mode()[0]
        print("Most_common_day is: ", most_common_day)

    # TO DO: display the most common start hour
    # extract hour from the Start Time column to create an hour column
    df['hour'] = df['Start Time'].dt.hour

    # find the most popular hour
    most_popular_hour = df['hour'].mode()[0]
    print("Most popular_hour is: ", most_popular_hour)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_common_start_station = df['Start Station'].mode()[0]
    print("Most_common_start_station is: ", most_common_start_station)

    # TO DO: display most commonly used end station
    most_common_end_station = df['End Station'].mode()[0]
    print("Most_common_end_station is: ", most_common_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    # Make "Total Trip" column
    df["Total Trip"] = "From " + df["Start Station"] + " to " + df["End Station"]

    #Most common Total trip
    most_common_total_trip = df["Total Trip"].mode()[0]
    print("Most_common_total_trip is: ", most_common_total_trip)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print("Total_travel_time is: ", total_travel_time)

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print("Mean_travel_time is: ", mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print("Count of user_types is: ", user_types)

    # TO DO: Display counts of gender
    if city != "Washington":
        user_gender = df['Gender'].value_counts()
        print("Count of user_gender is: ", user_gender)

        # TO DO: Display earliest, most recent, and most common year of birth
        # Earliest_year_of_birth
        earliest_year_of_birth = df['Birth Year'].min()
        print("Earliest_year_of_birth is: ", earliest_year_of_birth)

        # Most_recent_year_of_birth
        most_recent_year_of_birth = df['Birth Year'].max()
        print("Most_recent_year_of_birth is: ", most_recent_year_of_birth)

        # Common_year_of_birth
        common_year_of_birth = df['Birth Year'].mode()[0]
        print("Common_year_of_birth is: ", common_year_of_birth)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def raw_data(df):
    """prompt the user whether they would like want to see the raw data.
    every time user answers /'yes,/' the script should print 5 rows of the data untill user says: /"no/"
    """
    # Handle un expected answers
    answers = ["yes", "no"]
    answer = input("Do you want to print raw data?\nEnter yes or no.\n").lower()
    while answer not in answers:
        print("Enter yes or no only.\n")
        answer = input("Do you want to print raw data?\nEnter yes or no.\n").lower()

    while answer == "yes":
        print(df.sample(5))
        answer = input("Do you want to print raw data?\nEnter yes or no.\n").lower()


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df, month, day)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)
        raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
	main()
