from django.shortcuts import render
import matplotlib.pyplot as plt
from io import BytesIO
import base64
import pandas as pd

# Create your views here.
def index(request):
    x = [1, 2, 3, 4]
    y = [2, 4, 6, 8]

    plt.plot(x, y)
    plt.title('test graph')
    plt.xlabel('x label')
    plt.ylabel('y label')

    # plt.show()

    buffer = BytesIO()
    plt.savefig(buffer, format='png')

    img_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8').replace('\n', '')
    buffer.close()

    csv_path = './austin_weather.csv'
    df = pd.read_csv(csv_path)

    context = {
        'chart_img': f'data:image/png;base64, {img_base64}',
        'df': df,
    }
    return render(request, 'myapps/index.html', context)