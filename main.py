import requests
import pandas as pd
import matplotlib.pyplot as plt

# Make the API call
response = requests.get("https://rickandmortyapi.com/api/character")

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Get the JSON data from the response
    data = response.json()

    # Display the result
    print(data)
    
    # Display the keys in the dictionary
    print(data.keys())

    characters = data["results"]

    # Display the keys of the first character
    print(characters[0].keys())

    # Reorganise data in tabular format
    df = pd.DataFrame(characters)
    print(df.head())

    # Verify data types
    print(df.dtypes)

    # Set 'created' as the index
    df.set_index('created', inplace=True)

    # Save the DataFrame in different formats
    df.to_excel('characters.xlsx')  # Save as .xlsx
    df.to_parquet('characters.parquet')  # Save as .parquet
    df.to_json('characters.json')  # Save as .json
    df.to_pickle('characters.pkl')  # Save as .pkl

    # How many unique characters are available?
    unique_characters = df['id'].nunique()
    print("Unique Characters:", unique_characters)


    # Separate 'name' and 'url' keys into separate columns
    df['location_name'] = df['location'].apply(lambda x: x['name'])
    df['location_url'] = df['location'].apply(lambda x: x['url'])

    # Display the updated DataFrame
    print(df)

    # How many unique locations?
    unique_locations = df['location_name'].nunique()
    print("Unique Locations:", unique_locations)

    # How many characters are from planet Earth?
    df['location_name_origin'] = df['origin'].apply(lambda x: x['name'])

    #Check how Earth is saved in the location_name column
    print(df['location_name'].unique()) # Saved as 'Earth (Replacement Dimension)'

    earth_characters = df[df['location_name_origin'] == 'Earth (Replacement Dimension)'].shape[0]
    print("Characters from Planet Earth:", earth_characters)

    # Bar chart comparing species
    species_counts = df['species'].value_counts()

    plt.figure(figsize=(10, 6))
    species_counts.plot(kind='bar')
    plt.title('Species Comparison')
    plt.xlabel('Species')
    plt.ylabel('Count')
    plt.xticks(rotation=45)

    # Save the chart as HTML and PNG
    plt.savefig('species_chart.png')
    #plt.savefig('species_chart.html', format='html')

    # Display the chart
    plt.show()

else:
    # If the request was not successful, print the status code
    print("Error:", response.status_code)
