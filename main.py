import polars as pl

def load_data(url):
    df = pl.read_csv(url)
    # Unfortunately, skipping rows isn't directly supported in Polars, 
    # so we will have to use Pandas to skip rows and then convert to Polars
    # For now, we'll keep the data as is
    return df

def get_summary_statistics(df):
    return df.describe()

def get_mean(df, column_name):
    return df.column(column_name).mean().get(0)

def get_median(df, column_name):
    # Polars doesn't have a direct median method, 
    # but we can sort and then get the middle value
    sorted_col = df.sort(column_name).column(column_name)
    mid = len(sorted_col) // 2
    return (sorted_col[mid] + sorted_col[~mid]) / 2

def get_stdev(df, column_name):
    return df.column(column_name).std().get(0)

# Note: For plotting, we'll still rely on Matplotlib and Seaborn since Polars doesn't directly offer plotting
import matplotlib.pyplot as plt
import seaborn as sns

def plot_histogram_save(df, column_name, filename='histogram.png'):
    sns.set_style("whitegrid")
    plt.figure(figsize=(10, 6))
    
    # Convert the column to Python list for Seaborn plotting
    data = df.column(column_name).to_list()
    sns.histplot(data, kde=True, color="dodgerblue", bins=30)
    
    plt.title(f'Histogram of {column_name}', fontsize=18)
    plt.xlabel(column_name, fontsize=14)
    plt.ylabel('Density', fontsize=14)
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)
    plt.tight_layout()
    plt.savefig(filename)
    plt.close()
    return filename

url = 'https://gist.githubusercontent.com/tiangechen/b68782efa49a16edaf07dc2cdaa855ea/raw/0c794a9717f18b094eabab2cd6a6b9a226903577/movies.csv'
df = load_data(url)

# Print summary statistics
print(get_summary_statistics(df))

md = df.to_string()
with open('generated_markdown.md','w') as f:
    f.write(md)

print(f"Mean of 'Rotten Tomatoes %': {get_mean(df, 'Rotten Tomatoes %')}")
print(f"Median of 'Rotten Tomatoes %': {get_median(df, 'Rotten Tomatoes %')}")
print(f"Standard Deviation of 'Rotten Tomatoes %': {get_stdev(df, 'Rotten Tomatoes %')}")

# Plotting a histogram for 'Rotten Tomatoes %'
fname = plot_histogram_save(df, 'Rotten Tomatoes %')
