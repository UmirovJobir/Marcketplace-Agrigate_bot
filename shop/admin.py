from django.contrib import admin
from .models import User, Category, Product, KeyWords
from django.forms import forms
from django.urls import path
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.contrib import messages
from .models import Category
import pandas as pd
import json

@admin.register(KeyWords)
class KeyWordsAdmin(admin.ModelAdmin):
    raw_id_fields = ('category',)

class ExcelImportForm(forms.Form):
    excel_file = forms.FileField(label="Загрузить excel файл")

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'user_id', 'link')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    search_fields = 'name',
    # raw_id_fields = ('parent',)

    def get_urls(self):
        urls = super().get_urls()
        new_url = [
            path('upload-excel/',self.upload_excel),
            path('change-parent-id/',self.change_parent_id)
        ]
        return new_url + urls

    def upload_excel(self,request):
        if request.method == "POST":
            excel_file = request.FILES["excel_file"]
            if excel_file.name.endswith('.xlsx'):
                df = pd.read_excel(excel_file)
                count = 0
                for i in df.values:
                    Category.objects.create(id=i[0], name=json.loads(i[1]))
                    count += 1
                messages.info(request,f"{count} data added!")
            else:
                messages.error(request,"File is not in .xslx format!")
        form = ExcelImportForm()
        data = {'form':form}
        return render(request, 'admin/excel_upload.html', data)

    def change_parent_id(self,request):
        if request.method == "POST":
            excel_file = request.FILES["excel_file"]
            if excel_file.name.endswith('.xlsx'):
                df = pd.read_excel(excel_file)
                count = 0
                for i in df.values:
                    category = get_object_or_404(Category, id=i[1])
                    category.parent = get_object_or_404(Category, id=i[0])
                    category.save()
                    count += 1
                messages.info(request,f"{count} data changed!")
            else:
                messages.error(request,"File is not in .xslx format!")
        form = ExcelImportForm()
        data = {'form':form}
        return render(request, 'admin/change_id.html', data)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    raw_id_fields = ('category',)
    list_display = ('product_user', 'message_text', 'media_file')
    search_fields = ('category__name','message_text','product_user')




    
        