from django.shortcuts import render,redirect,get_object_or_404
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from structure.codelist.utils import array_conversation_string



from structure.codelist.models import ListInput
from structure.accounts.models.profile import Profile
from structure.codelist.serializer import ProfileSerializer


class ListInputView(View):
    @method_decorator(login_required(login_url='login'))
    def dispatch(self,request,*args,**kwargs):
        return super().dispatch(request,*args,**kwargs)

    def get(self,request):
        current_user = request.user
        list_obj = ListInput.objects.filter(
            profile = current_user.id,
            is_active = True
        ).order_by('-created_at')
        return render(request,'list/list_create.html',{
            'list_input':list_obj
        })

    def post(self,request):
        current_user = request.user.profile
        get_list = request.POST.get('list')

        list_input_obj = ListInput(
            profile = current_user,
            input_values = array_conversation_string(get_list)
        )
        list_input_obj.save()
        return redirect('single_list', list_input_obj.id)

    
class ListInputSingleView(View):
    @method_decorator(login_required(login_url='login'))
    def dispatch(self,request,*args,**kwargs):
        return super().dispatch(request,*args,**kwargs)

    def get(self,request,valueID):
        input_obj = get_object_or_404(ListInput, id=valueID)
        return render(request,'list/single_value.html',{
            'input_value':input_obj
        })


class ListInputDeleteView(View):
    @method_decorator(login_required(login_url='login'))
    def dispatch(self,request,*args,**kwargs):
        return super().dispatch(request,*args,**kwargs)

    def post(self,request,valueID):
        list_obj = get_object_or_404(ListInput,id=valueID)
        list_obj.delete()
        return redirect('/')



class ListInputViewbyProfile(generics.GenericAPIView):
    queryset = Profile.objects.filter(is_active=True)
    serializer_class = ProfileSerializer

    def get(self,request):

        list_obj = Profile.objects.filter(
            is_active=True,
            user=request.user
        )
        serializer = ProfileSerializer(list_obj,many=True)
        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )