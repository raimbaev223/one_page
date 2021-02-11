from django.shortcuts import render, redirect
import telebot

from .forms import ContactForm

bot = telebot.TeleBot('1566152078:AAFn5Gy6C4tDvQwp-vHrQmHAdsC73PuNgVg')


def index(request):
    return render(request, 'index.html', {})


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            mail = form.cleaned_data['mail']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            msg = f"Имя: {name} \n" \
                  f"Почта: {mail} \n" \
                  f"Тема: {subject} \n" \
                  f"Текст: {message}"
            bot.send_message(959339948, msg)

    return redirect('home')
