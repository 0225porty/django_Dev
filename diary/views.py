from django.shortcuts import render,redirect,get_object_or_404
from .forms import DayCreateForm
from .models import Day

# Create your views here.
def index(request):
    context = {
        'day_list':Day.objects.all(),
    }
    return render(request, 'diary/day_list.html', context)

def add(request):
    #送信内容をもとにフォームを作る。
    #POSTでなければ、空のフォーム
    form = DayCreateForm(request.POST or None)

    #method=POST、つまり送信ボタン押下時、入力内容が問題なければ
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('diary:index')
    
    #通常時のページアクセスや、入力内容に誤りがあればまたページを表示
    context = {
        'form': form
    }
    return render(request, 'diary/day_form.html', context)

def update(request,pk):
    #urlのpkをもとに、Dayを取得
    day=get_object_or_404(Day,pk=pk)

    #フォームに取得したDayを紐づける
    form=DayCreateForm(request.POST or None,instance=day)

    #method=POST、つまり送信ボタン押下時、入力内容に間違いがなければ
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('diary:index')
    
    #通常時のページアクセスや、入力内容に誤りがあればまたページを表示
    context={
        'form':form
    }
    return render(request,'diary/day_form.html',context)

def delete(request,pk):
    #urlのpkをもとに、Dayを取得
    day=get_object_or_404(Day,pk=pk)

    #method=POST、つまり送信ボタン押下時、入力内容に間違いがなければ
    if request.method == 'POST':
        day.delete()
        return redirect('diary:index')
    
    #通常時のページアクセスや、入力内容に誤りがあればまたページを表示
    context={
        'day':day
    }
    return render(request,'diary/day_confirm_delete.html',context)

def detail(request,pk):
    #urlのpkをもとに、Dayを取得
    day=get_object_or_404(Day,pk=pk)

    #通常時のページアクセスや、入力内容に誤りがあればまたページを表示
    context={
        'day':day
    }
    return render(request,'diary/day_detail.html',context)