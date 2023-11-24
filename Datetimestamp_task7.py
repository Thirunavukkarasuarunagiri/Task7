import datetime
def create_text_file_with_timestamp():
    current_timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    file_name = f"{current_timestamp}_output.txt"
    with open(file_name, 'w') as file:
        file.write(current_timestamp)

    print(f"Text file '{file_name}' created with content '{current_timestamp}'.")

create_text_file_with_timestamp()