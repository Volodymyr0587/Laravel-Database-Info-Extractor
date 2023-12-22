## Laravel Database Info Extractor

### Description:

The Laravel Database Info Extractor is a Python script that scans Laravel projects for .env files and extracts the DB_DATABASE values, saving the results in a CSV file. This tool is useful for quickly gathering information about database configurations in multiple Laravel projects.

### Features:

Recursively scans a directory for Laravel projects.
Extracts DB_DATABASE values from .env files.
Outputs results to a CSV file for easy analysis.

### Usage:

Clone the repository:


```git clone https://github.com/Volodymyr0587/Laravel-Database-Info-Extractor```

Navigate to the project directory:

```cd laravel-db-info-extractor```

Run the script:

```python main.py```

Follow the prompts to provide the absolute path to the folder containing your Laravel projects and the desired output file name.

### Requirements:

Python 3.x

### Example:

```bash
Enter absolute path to the folder with your Laravel projects.
Example: '/home/username/laravel'
>>> /path/to/your/laravel/projects

Enter the name of the output CSV file.
Example: 'LaravelDatabases.csv'
>>> LaravelDatabases.csv

DONE.
```

### Error Handling:

The script includes error handling for cases where the provided directory path does not exist or if there are any other unexpected issues.
