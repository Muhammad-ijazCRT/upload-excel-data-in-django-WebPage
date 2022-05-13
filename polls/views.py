from django.shortcuts import render
from django.http import HttpResponse
from polls.models import UploadCsv
from csv import excel
import pandas as pd
import numpy as np


def index(request):
    if request.method == 'POST':
        text_excel_file = request.FILES["text_file"]
        UploadCsv(textfile=text_excel_file).save()

        last_ob = UploadCsv.objects.all().last()
        textfile_name = last_ob.textfile
        df_text = pd.read_csv(textfile_name)

        bulk_data = []
        for i in range(len(df_text)):
            list_ = df_text.iloc[i].values
            joined_text = ' '.join(list_)
            joined_text = [joined_text]
            print('this is list text text///////////.............................', list_)
            fm = list_[0]
            doc = ["{} ".format(fm)]

            bulk_data.append(fm)

        # vector = encode.transform(doc)
        # print('this is vector', vector)
        # text_res = forester.predict(vector)
        # print('this is text_res', fm)
        print('the lenth as : aldjfklasjdfklajsd: ', len(bulk_data))
        for i in bulk_data:
            print('this is i', type)

    return render(request, 'polls/index.html')
