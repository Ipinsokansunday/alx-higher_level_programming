#!/usr/bin/python3

save_to_json_file = __import__('7-save_to_json_file').save_to_json_file


def main():
    try:
        filename = "my_list.json"
        my_list = [1, 2, 3]
        save_to_json_file(my_list, filename)
        print(f"List saved successfully to {filename}")

        filename = "my_dict.json"
        my_dict = {
            'id': 12,
            'name': "John",
            'places': ["San Francisco", "Tokyo"],
            'is_active': True,
            'info': {
                'age': 36,
                'average': 3.14
            }
        }
        save_to_json_file(my_dict, filename)
        print(f"Dictionary saved successfully to {filename}")

        filename = "my_set.json"
        my_set = {132, 3}
        save_to_json_file(my_set, filename)
        print(f"Set saved successfully to {filename}")

    except FileNotFoundError as file_not_found_error:
        print(f"Error: {file_not_found_error}. Please check the file path.")
    except json.JSONDecodeError as json_decode_error:
        print(f"Error: {json_decode_error}. Failed to decode JSON.")
    except Exception as e:
        print(f"Error: {e.__class__.__name__} - {e}")

if __name__ == "__main__":
    main()
