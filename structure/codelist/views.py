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


## List input Create and List view
class ListInputView(View):
    ## only accessble for logged In user else return to the Login page
    @method_decorator(login_required(login_url='login'))
    def dispatch(self,request,*args,**kwargs):
        return super().dispatch(request,*args,**kwargs)

    def get(self,request):
        ## getting the current logged In user 
        current_user = request.user.profile
        ## filter the data by user 
        list_obj = ListInput.objects.filter(
            profile = current_user.id,
            is_active = True
        ).order_by('-created_at')

        return render(request,'list/list_create.html',{
            'list_input':list_obj
        })

    def post(self,request):
        ## getting the Logged in user 
        current_user = request.user.profile
        get_list = request.POST.get('list')

        ## saveing the data 
        # with the current user 
        # with the input value (descending order)
        list_input_obj = ListInput(
            profile = current_user,
            input_values = array_conversation_string(get_list)
        )
        list_input_obj.save()
        return redirect('single_list', list_input_obj.id)


### List OBJ single View    
class ListInputSingleView(View):
    ## only accessble for logged In user else return to the Login page
    @method_decorator(login_required(login_url='login'))
    def dispatch(self,request,*args,**kwargs):
        return super().dispatch(request,*args,**kwargs)

    def get(self,request,valueID):
        ## return the Single list input OBJ
        input_obj = get_object_or_404(ListInput, id=valueID)
        return render(request,'list/single_value.html',{
            'input_value':input_obj
        })


### List obj Delete View 
class ListInputDeleteView(View):
    ## only accessble for logged In user else return to the Login page
    @method_decorator(login_required(login_url='login'))
    def dispatch(self,request,*args,**kwargs):
        return super().dispatch(request,*args,**kwargs)

    def post(self,request,valueID):
        ## getting the current list obj and delete it
        list_obj = get_object_or_404(ListInput,id=valueID)
        list_obj.delete()
        return redirect('/')


### API endpoint view of List Input by Current User 
## to access the data user has to be autheticated 
class ListInputViewbyProfile(generics.GenericAPIView):
    queryset = Profile.objects.filter(is_active=True)
    serializer_class = ProfileSerializer

    def get(self,request):
        ## filtering the data of current Logged In user 
        list_obj = Profile.objects.filter(
            is_active=True,
            user=request.user
        )
        serializer = ProfileSerializer(list_obj,many=True)
        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )