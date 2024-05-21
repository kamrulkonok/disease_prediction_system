from django.shortcuts import render ,redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from .models import Chat , Feedback
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from .serializers import feedbackSerializer, chatSerializer

# Create your views here.


@api_view(['POST'])
@permission_classes((permissions.IsAuthenticated,))
def post_feedback(request):
    
  if request.method == "POST":

      feedback = request.data.get('feedback')
      if feedback != '':  
        f = Feedback(sender=request.user, feedback=feedback)
        f.save()        
        print(feedback)   

        try:
           if (request.user.is_patient == True) :
              return HttpResponse("Feedback successfully sent.")
        except:
          pass
        if (request.user.is_doctor == True) :
           return HttpResponse("Feedback successfully sent.")

      else :
        return HttpResponse("Feedback field is empty   .")


@api_view(['GET'])
@permission_classes((permissions.IsAuthenticated,))
def get_feedback(request):
    
    if request.method == "GET":

      texts = Feedback.objects.all()
      serializer = feedbackSerializer(texts, many=True)

      
      return Response(serializer.data)  





#-----------------------------chatting system ---------------------------------------------------


# def post(request):
#     if request.method == "POST":
#         msg = request.POST.get('msgbox', None)

#         consultation_id = request.session['consultation_id'] 
#         consultation_obj = consultation.objects.get(id=consultation_id)

#         c = Chat(consultation_id=consultation_obj,sender=request.user, message=msg)

#         #msg = c.user.username+": "+msg

#         if msg != '':            
#             c.save()
#             print("msg saved"+ msg )
#             return JsonResponse({ 'msg': msg })
#     else:
#         return HttpResponse('Request must be POST.')



# def messages(request):
#    if request.method == "GET":

#          consultation_id = request.session['consultation_id'] 

#          c = Chat.objects.filter(consultation_id=consultation_id)
#          return render(request, 'consultation/chat_body.html', {'chat': c})
