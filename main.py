import os
import csv

class DatabaseFinder:
    def __init__(self, folder_path, output_file_path):
        self.folder_path = folder_path
        self.output_file_path = output_file_path

    def find_and_write_db_lines(self):
        try:
            if not os.path.exists(self.folder_path):
                raise FileNotFoundError(f"Error: Directory not found - {self.folder_path}")
            with open(self.output_file_path, 'w', newline='') as csvfile:
                fieldnames = ['Folder Path', 'DB_DATABASE Value']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

                # Write the header
                writer.writeheader()

                for env_file_path, db_value in self._get_database_values():
                    writer.writerow({'Folder Path': env_file_path, 'DB_DATABASE Value': db_value})
        
        except Exception as e:
            print(f"Error: {e}")

    def _get_database_values(self):
        for root, dirs, files in os.walk(self.folder_path):
            # Include hidden files and directories
            for file in files:
                if file.endswith(".env"):
                    env_file_path = os.path.join(root, file)
                    with open(env_file_path, 'r') as env_file:
                        for line in env_file:
                            if line.startswith("DB_DATABASE="):
                                # Extract the value after the '=' sign
                                db_value = line.split('=')[1].strip()
                                yield env_file_path, db_value

def get_user_input(prompt):
    return input(prompt).strip()

if __name__ == "__main__":
    try:
        print("Enter absolute path to folder with your Laravel projects.")
        print("Example (without quotes): '/home/username/Desktop/websites/laravel'")
        folder_to_search = get_user_input(">>> ")

        print("Enter name of output csv file.")
        print("Example (without quotes): 'LaravelDatabases.csv'")
        output_file_path = get_user_input(">>> ")

        database_finder = DatabaseFinder(folder_to_search, output_file_path)
        database_finder.find_and_write_db_lines()

        print("DONE.")
        
    except Exception as e:
        print(f"Error: {e}")

