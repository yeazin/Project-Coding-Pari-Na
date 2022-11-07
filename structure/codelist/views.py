from django.shortcuts import render,redirect
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator



from structure.codelist.models import ListInput


class ListInputView(View):
    @method_decorator(login_required(login_url='login'))
    def dispatch(self,request,*args,**kwargs):
        return super().dispatch(request,*args,**kwargs)

    def get(self,request):
        current_user = request.user
        list_obj = ListInput.objects.filter(
            profile = current_user.id,
            is_active = True
        )
        return render(request,'list/list_create.html',{
            'list_input':list_obj
        })

    # def post(self,request):
    #     current_user = request.user.profile
    #     get_list = request.POST.get('list')

    #     list_input_obj = ListInput(
    #         profile = current_user,
    #         input_values = get_list
    #     )
    #     list_input_obj.save()
