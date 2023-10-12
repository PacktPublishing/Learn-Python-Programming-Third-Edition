# data.science.example.py
def fetch_data(data_source):
    return data_source


def parse_data(data):
    return data


def filter_data(parsed_data):
    return parsed_data


def polish_data(filtered_data):
    return filtered_data


def analyse(polished_data):
    return polished_data


def report(final_data):
    return final_data


def do_report(data_source):
    # fetch and prepare data
    data = fetch_data(data_source)
    parsed_data = parse_data(data)
    filtered_data = filter_data(parsed_data)
    polished_data = polish_data(filtered_data)

    # run algorithms on data
    final_data = analyse(polished_data)

    # create and return report
    report_v = report(final_data)
    return report_v


if __name__ == "__main__":
    print("Please don't call the `do_report` function. "
          "It's just and example.")
