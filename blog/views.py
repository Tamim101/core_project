import pathlib
import uuid

from ajax_datatable import AjaxDatatableView
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import transaction

from django.shortcuts import render, redirect

# Create your views here.
from blog.forms import BlogForm
from blog.models import blog
from utils.helper import row_details


def home(request):
    return render(request, 'backend/home.html')

def blog_add(request):
    obj = blog.objects.all()
    return render(request, "backend/user/blog-list.html",{'obj':obj})
@transaction.atomic
def show_now_add(request):
    if request.method == 'POST':
        try:
            id = request.POST.get('pk', 0)
            title = request.POST.get('title')
            description = request.POST.get('description')
            created_at = request.POST.get('create_at')

            updated_at = request.POST.get('updated_at')


            instance = blog.objects.filter(id=id).first()
            if instance is None:
                obj = blog()
                form = BlogForm(request.POST)
            else:
                form = BlogForm(request.POST,instance)
                obj = instance
            if form.is_valid():
                obj.title = title
                obj.created_at = created_at
                obj.updated_at = updated_at
                obj.description = description
                obj.save()

                # thm_file = request.FILES.get('thumbail',None)
                # print(thm_file)

                # if thm_file != None:
                #     thm_uniq_name = uuid.uuid4().hex
                #     thm_ext = pathlib.Path(thm_file.name).suffix
                #     thumbnail_name = str(obj.id)+'-'+'-'+thm_uniq_name + thm_ext
                #     thm_file._set_name(thumbnail_name)
                #     obj.thumbail = thm_file



                obj.save()
                messages.success(request, 'Saved successfully')
                return redirect("blog_list")
            else:
                transaction.set_rollback(True)
                messages.error(request, form._error)
        except Exception as e:

            transaction.set_rollback(True)
            messages.error(request, 'Failed')
    return redirect("blog_list")




class list_blog(AjaxDatatableView):
    model = blog
    title = 'Blog List'
    initial_order = [["id", "asc"], ]
    length_menu = [[10, 20, 50, 100, -1], [10, 20, 50, 100, 'all']]
    search_values_separator = '+'

    column_defs = [
         AjaxDatatableView.render_row_tools_column_def(),
        {'name': 'id','title':'SN', 'visible': True, },
        {'name': 'title', 'visible': True, },
        # {'name': 'thumbail', 'visible': True, },
        {'name': 'description', 'visible': True, },
        {'name': 'created_at', 'visible': True, },
        {'name': 'updated_at', 'visible': True, },
        {'name': 'btn','title':'Action', 'visible': True, },
    ]

    def render_row_details(self, pk, request=None):
        fields = ["id", 'title', 'description', 'created_at', 'updated_at']
        return row_details(self, pk, fields)

   # fields def customize_row(self, row, obj):
   #      row['btn'] = '<button class="btn btn-info btn-sm" onclick="editVideo(\'' + str(row['pk']) + '\')">' \
   #                                                                                                  '<i class="fa fa-pencil-alt mr-0"></i></button><button onclick="deleteVideo(' + \
   #                   str(row["pk"]) + ')" class="btn btn-danger btn-sm"><i class="fa fa-trash mr-0"></i></button>'
   #      row['thumbnail'] = '<img  class="hp-100 wp-100" src="' + (str(row['thumbnail'])) + '" alt="' + str(
   #          row['thumbnail']) + '" />'


