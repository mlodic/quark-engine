from collections import defaultdict

from prettytable import PrettyTable

from quark.utils.colors import red, green


def output_parent_function_table(call_graph_analysis_list):
    dd = defaultdict(list)

    for item in call_graph_analysis_list:
        # print(item["parent"].class_name, item["parent"].name, item["crime"])
        key = f"{item['parent'].class_name}{item['parent'].name}"
        dd[key].append(item["crime"])

    # Pretty Table Output

    for parent, crimes in dd.items():
        tb = PrettyTable()
        tb.field_names = ["Parent Function", f"{green(parent)}"]
        tb.align = "l"

        count = 1

        for crime in crimes:
            if count == 1:
                tb.add_row(["Crime Description", red(f"{count}. {crime}")])
            else:
                tb.add_row(["", red(f"{count}. {crime}")])
            count += 1

        print(tb)
