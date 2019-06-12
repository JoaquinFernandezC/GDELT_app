from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render
import random
def index(request):
    return render(request, 'tone/template.html', context={})

# Create your views here.
def count_resume(request):
    return render(request, 'tone/count_resume.html', context={})


def tone_count(request):
    tones = [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    tone_counts = [14491, 21643, 33160, 44407, 61895, 80683, 99974, 119951, 136927, 145210, 282204, 111183, 77508, 48980, 28618, 15628, 7944, 4092, 2107, 1056, 542]


    goldsteins = [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    goldsteins_counts=[90606, 26470, 2248, 11911, 10497, 95635, 42054, 0, 97843, 0, 131921, 253920, 124095, 144460, 113007, 38050, 34454, 114420, 22627, 1065, 5638]

    return JsonResponse(dict(tones=tones,
                             counts=tone_counts,
                             goldsteins=goldsteins,
                             goldsteins_counts=goldsteins_counts))


def events_counts(request):
    event_codes = ["DEMAND","DISAPPROVE","REJECT","THREATEN", "PROTEST","EXHIBIT FORCE POSTURE","REDUCE RELATIONS","COERCE","ASSAULT","FIGHT","USE UNCONVENTIONAL MASS VIOLENCE"]
    counts =[33.570763218111495, 0.61104023651864, 5.897272340684041, 10.617013952169776, 8.01743514974789, 2.8430836522689993, 1.5126663021687625, 3.341230787922969, 0.7340582791648947, 0.16149282141627685, 32.693943259826256]

    return JsonResponse(dict(events_codes=event_codes,
                             counts=counts,most_repeated = 10))

def event_counts_resume(request):
    return render(request, 'tone/events_resume.html', context={})


def tone_by_date(request):


    labels=['2015-1', '2015-2', '2015-3', '2015-4', '2015-5', '2015-6', '2015-7', '2015-8', '2015-9', '2015-10', '2015-11', '2015-12', '2016-1', '2016-2', '2016-3', '2016-4', '2016-5', '2016-6', '2016-7', '2016-8', '2016-9', '2016-10', '2016-11', '2016-12', '2017-1', '2017-2', '2017-3', '2017-4', '2017-5', '2017-6', '2017-7', '2017-8', '2017-9', '2017-10', '2017-11', '2017-12', '2018-1', '2018-2', '2018-3', '2018-4', '2018-5', '2018-6', '2018-7', '2018-8', '2018-9', '2018-10', '2018-11', '2018-12', '2019-1', '2019-2', '2019-3', '2019-4', '2019-5', '2019-6']
    tones=[
        0.5, -1.0227272727272727, -2.0265486725663715, -1.5238095238095237, -0.5, -1.7329545454545454,
        -1.1951219512195121, -1.0410958904109588, -1.423841059602649, -1.3739837398373984, -0.8181818181818182,
        -1.9621212121212122, -2.7899159663865545, -1.1893939393939394, -1.0384615384615385, -1.4076923076923078,
        -1.1625615763546797, -1.8402777777777777, -0.22448979591836735, -0.9507042253521126, -1.5726495726495726,
        -0.8762886597938144, -1.1443298969072164, -1.0588235294117647, -0.9523809523809523, -1.2183908045977012,
        -1.970873786407767, -1.6474820143884892, -2.015267175572519, -2.2, -0.2283464566929134, -1.2074074074074075,
        -1.2461538461538462, -1.116504854368932, -0.6944444444444444, -0.8857142857142857, -1.04, -1.2857142857142858,
        -1.5562913907284768, -0.949685534591195, -0.6050420168067226, -1.875, 3.0, -1.3333333333333333, 0.0, 0.375,
        -0.6666666666666666, -3.0, -5.0, 2.5, -1.7222222222222223, -2.95, -1.599700710811822, -1.8211498973305955,
        -1.8021595680863827, -1.7257579553996492, -1.819300164024057, -1.5861137218045114, -1.6871486969851814,
        -1.598967741935484, -1.556390977443609, -1.3657195233730521, -1.5579237349572277, -2.2557016642695706,
        -1.9746678857634594, -1.794236602628918, -1.9021393376161666, -1.6709791150019422, -1.8551501473261864,
        -1.7817697937458417, -1.951973265436028, -1.8192289386006664, -1.85428014921924, -1.8555677713208734,
        -1.878699073041761, -2.005472680730868, -1.9236742007481689, -1.9623702672928625, -1.9110038054427425,
        -1.6642316258351892, -1.84402267371505, -1.9672444225816719, -1.9038796861377507, -1.6976108556545226,
        -1.7570547441756414, -1.531147948869468, -1.6703537682608276, -1.748720896809428, -1.843045498018855,
        -1.7365654021722021, -1.7771936532211814, -1.7350343473994112, -1.7748359580052493, -1.7686966798389778,
        -1.9280622664046545, -1.752447607439154, -1.6814771005064133, -1.6597416271817924, -1.598799320668273,
        -1.8950202934748672, -1.7937028824833703, -1.6292847080920332, -1.6585870413739265, -1.5602669208770257,
        -1.544095840162335, -1.6344795586946435, -1.8815447456368362, -1.6495152870991796, -1.6413846752236483,
        -1.7176908752327746, -1.5758962623951183, -1.8530785562632697, -1.7893772893772895, -1.7301878149335777,
        -1.8848776574408344, -1.5669623996620194, -1.6637931034482758]

    return JsonResponse(dict(labels=labels, tones=tones))

