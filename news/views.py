import json
from datetime import datetime
from django.shortcuts import render, redirect
from django.views import View
from django.conf import settings


class ComingSoon(View):
    def get(self, request):
        return redirect('news/')


with open(settings.NEWS_JSON_PATH, 'r+') as json_file:
    articles = json.load(json_file)


    class MainView(View):
        def get(self, request):

            result = []
            query = request.GET.get('q')
            if query:
                for article in articles:
                    if query in article['title']:
                        result.append(article)
                context = {'articles': result}
                return render(request, 'news/main.html', context)
            else:
                context = {'articles': articles}
                return render(request, 'news/main.html', context)


    class SingleView(View):
        def get(self, request, article_link):
            context = {}
            for article in articles:
                if article['link'] == int(article_link):
                    context = {'article': article}
            return render(request, 'news/single.html', context)


    class NewArticle(View):
        dic = {}

        def get(self, request):
            return render(request, 'news/form.html')

        def post(self, request):
            self.dic['created'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            self.dic['text'] = request.POST.get('text')
            self.dic['title'] = request.POST.get('title')
            self.dic['link'] = len(articles) + 1

            articles.append(self.dic)

            return redirect('/news')

