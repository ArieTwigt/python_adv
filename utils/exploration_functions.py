

def cars_df_exploration(cars_df) -> None:
    '''
    Exploration logs for the DataFrame:

    * Show the dimensions of the DataFrame
    * Show the first rows of the DataFrame
    * Brief technical information about the DataFrame
    * Statistical information
    * Unique values of several columns
    * Average value for the car price

    '''

    # Show the dimensions of the DataFrame
    print("\nShape:")
    print(cars_df.shape)

    # Show the first rows of the DataFrame
    print("\nFirst rows:")
    print(cars_df.head())

    # Show the first rows of the DataFrame
    print("\nLast rows:")
    print(cars_df.tail(20))

    # Brief technical information about the DataFrame
    print("\nInfo:")
    print(cars_df.info())

    # select a column in pandas, get the values
    #print("\nInfo:")
    #cars_df['datum_tenaamstelling'].values

    # information about the values
    print("\nDescription:")
    print(cars_df.describe())

    # Summarize text columns
    print("\nUnique values:")
    print(cars_df['handelsbenaming'].unique())

    # For a textual column, provide the unique values and their occurances
    print("\nUnique values and their occurances of 'handelsbenaming':")
    print(cars_df['handelsbenaming'].value_counts())
    