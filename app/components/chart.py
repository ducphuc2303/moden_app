# app/components/chart.py

# import solara
# import matplotlib.pyplot as plt
# import pandas as pd

# @solara.component
# def InteractiveLineChart():
#     # Dữ liệu mẫu
#     data = {
#         'Year': [2018, 2019, 2020, 2021, 2022],
#         'Sales_A': [150, 200, 250, 300, 350],
#         'Sales_B': [100, 150, 200, 250, 300]
#     }

#     df = pd.DataFrame(data)

#     # Trạng thái biểu đồ
#     selected_data, set_selected_data = solara.use_state("Sales_A")

#     # Tạo biểu đồ sử dụng matplotlib
#     fig, ax = plt.subplots()
#     ax.plot(df['Year'], df[selected_data], marker='o')
#     ax.set_title('Sales Over Years')
#     ax.set_xlabel('Year')
#     ax.set_ylabel('Sales')

#     # Hiển thị biểu đồ và lựa chọn trong Solara
#     with solara.VBox():
#         solara.Select(label="Select Data", options=["Sales_A", "Sales_B"], value=selected_data, on_value=set_selected_data)
#         solara.FigureMatplotlib(fig)

import solara
import matplotlib.pyplot as plt
import pandas as pd

@solara.component
def InteractiveLineChart():
    # Dữ liệu mẫu
    data = {
        'Year': [2018, 2019, 2020, 2021, 2022],
        'Sales_A': [150, 200, 250, 300, 350],
        'Sales_B': [100, 150, 200, 250, 300]
    }

    df = pd.DataFrame(data)

    # Trạng thái biểu đồ
    selected_data, set_selected_data = solara.use_state("Sales_A")

    # Tạo biểu đồ sử dụng matplotlib
    fig, ax = plt.subplots()
    ax.plot(df['Year'], df[selected_data], marker='o')
    ax.set_title('Sales Over Years')
    ax.set_xlabel('Year')
    ax.set_ylabel('Sales')

    # Hiển thị biểu đồ và lựa chọn trong Solara
    with solara.VBox():
        solara.Select(label="Select Data", options=["Sales_A", "Sales_B"], value=selected_data, on_value=set_selected_data)
        solara.FigureMatplotlib(fig)