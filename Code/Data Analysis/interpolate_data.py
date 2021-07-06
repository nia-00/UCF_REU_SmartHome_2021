import pandas as pd


def clean_file(r_file, i_w_file):
    cleaned_data = pd.read_csv(r_file)
    # Fills in blank cells with interpolated values
    cleaned_data = cleaned_data.interpolate(method='linear').round(decimals=1)
    # Save interpolated data to new file
    cleaned_data.to_csv(path_or_buf=i_w_file, index=False)

    print("\nData successfully interpolated!")


if __name__ == "__main__":
    original_file = input("Enter file path: ")
    read_file = original_file.replace('\\', '/')
    read_file = read_file.replace('"', '')

    end_name_index = read_file.find('.csv')
    interpolated_write_file = read_file[:end_name_index] + '_interpolated' + read_file[end_name_index:]

    print("\nInput file name: ", original_file)
    print("Interpolated file name: ", interpolated_write_file.replace("/", "\\"))

    clean_file(read_file, interpolated_write_file)
