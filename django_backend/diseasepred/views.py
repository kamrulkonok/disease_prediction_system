from django.http import request
from django.shortcuts import render
from rest_framework import viewsets , status, permissions
from rest_framework.response import Response
from rest_framework.decorators  import api_view, permission_classes, authentication_classes
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
# from knox.models import AuthToken
from rest_framework import generics
# from rest_framework import generics
import numpy as np
from .models import BreastCancer, Diabetes, HeartDisease, diseaseinfo, consultation, rating_review
from users.models import Patient, Doctor
from .serializers import HeartDiseaseSerializer, BreastCancerSerializer, consultationSerializer, diseaseinfoSerializer, DiabetesSerializer,  SkinCancerSerializer
from users.serializers import PatientSerializer, UserSerializer
from django.contrib.auth import get_user_model
import tensorflow as tf
from tensorflow import keras
import tensorflow_hub as hub
import efficientnet.tfkeras as efn
from django.core.files.storage import FileSystemStorage
import cv2
from dps.settings import MEDIA_ROOT, AI_Models_ROOT
User = get_user_model()
#loading model
import joblib as jb
model = jb.load(AI_Models_ROOT+'/model')
heartModel = jb.load(AI_Models_ROOT + '/heartDisease')

breastModel = jb.load(AI_Models_ROOT + '/breastCancer')

  

# @api_view(['GET'])
# @permission_classes((permissions.IsAuthenticated, ))
# def pviewprofile(request):

#    if request.method == 'GET':
#       print(request.user)
#       puser = User.objects.filter(user_name=request.user)
#       return Response({"puser":puser})

class pviewprofile(generics.RetrieveAPIView):
  permission_classes = [
    permissions.IsAuthenticated,
  ]
  serializer_class = UserSerializer

  def get_object(self):
    puser = User.objects.filter(user_name=self.request.user).first()
    print(self.request.user)
    pat = Patient.objects.filter(user = self.request.user).first()
    print(self.request.user.is_patient)
    return self.request.user



@api_view(['GET','POST'])
@permission_classes((permissions.IsAuthenticated,))
def checkdisease(request):

  diseaselist=['Fungal infection','Allergy','GERD','Chronic cholestasis','Drug Reaction','Peptic ulcer diseae','AIDS','Diabetes ',
  'Gastroenteritis','Bronchial Asthma','Hypertension ','Migraine','Cervical spondylosis','Paralysis (brain hemorrhage)',
  'Jaundice','Malaria','Chicken pox','Dengue','Typhoid','hepatitis A', 'Hepatitis B', 'Hepatitis C', 'Hepatitis D',
  'Hepatitis E', 'Alcoholic hepatitis','Tuberculosis', 'Common Cold', 'Pneumonia', 'Dimorphic hemmorhoids(piles)',
  'Heart attack', 'Varicose veins','Hypothyroidism', 'Hyperthyroidism', 'Hypoglycemia', 'Osteoarthristis',
  'Arthritis', '(vertigo) Paroymsal  Positional Vertigo','Acne', 'Urinary tract infection', 'Psoriasis', 'Impetigo']


  symptomslist=['itching','skin_rash','nodal_skin_eruptions','continuous_sneezing','shivering','chills','joint_pain',
  'stomach_pain','acidity','ulcers_on_tongue','muscle_wasting','vomiting','burning_micturition','spotting_ urination',
  'fatigue','weight_gain','anxiety','cold_hands_and_feets','mood_swings','weight_loss','restlessness','lethargy',
  'patches_in_throat','irregular_sugar_level','cough','high_fever','sunken_eyes','breathlessness','sweating',
  'dehydration','indigestion','headache','yellowish_skin','dark_urine','nausea','loss_of_appetite','pain_behind_the_eyes',
  'back_pain','constipation','abdominal_pain','diarrhoea','mild_fever','yellow_urine',
  'yellowing_of_eyes','acute_liver_failure','fluid_overload','swelling_of_stomach',
  'swelled_lymph_nodes','malaise','blurred_and_distorted_vision','phlegm','throat_irritation',
  'redness_of_eyes','sinus_pressure','runny_nose','congestion','chest_pain','weakness_in_limbs',
  'fast_heart_rate','pain_during_bowel_movements','pain_in_anal_region','bloody_stool',
  'irritation_in_anus','neck_pain','dizziness','cramps','bruising','obesity','swollen_legs',
  'swollen_blood_vessels','puffy_face_and_eyes','enlarged_thyroid','brittle_nails',
  'swollen_extremeties','excessive_hunger','extra_marital_contacts','drying_and_tingling_lips',
  'slurred_speech','knee_pain','hip_joint_pain','muscle_weakness','stiff_neck','swelling_joints',
  'movement_stiffness','spinning_movements','loss_of_balance','unsteadiness',
  'weakness_of_one_body_side','loss_of_smell','bladder_discomfort','foul_smell_of urine',
  'continuous_feel_of_urine','passage_of_gases','internal_itching','toxic_look_(typhos)',
  'depression','irritability','muscle_pain','altered_sensorium','red_spots_over_body','belly_pain',
  'abnormal_menstruation','dischromic _patches','watering_from_eyes','increased_appetite','polyuria','family_history','mucoid_sputum',
  'rusty_sputum','lack_of_concentration','visual_disturbances','receiving_blood_transfusion',
  'receiving_unsterile_injections','coma','stomach_bleeding','distention_of_abdomen',
  'history_of_alcohol_consumption','fluid_overload','blood_in_sputum','prominent_veins_on_calf',
  'palpitations','painful_walking','pus_filled_pimples','blackheads','scurring','skin_peeling',
  'silver_like_dusting','small_dents_in_nails','inflammatory_nails','blister','red_sore_around_nose',
  'yellow_crust_ooze']

  alphabaticsymptomslist = sorted(symptomslist)



  if request.method == 'GET':
    
     return Response({"list":alphabaticsymptomslist})




  elif request.method == 'POST':
       
      #psymptoms = []
      
      psymptoms=request.data.get('symptoms')
      
      inputno = len(psymptoms)
      print(inputno)
      if (inputno == 0 ) :
         return Response({'predicteddisease': "none",'confidencescore': 0 })
  
      else :

         # print(psymptoms[1])
         # a = ["a_s_d", "As_das", 1]
         # print(a[1])
      
         """      #main code start from here...
         """
      

         
         testingsymptoms = []
         #append zero in all coloumn fields...
         for x in range(0, len(symptomslist)):

            testingsymptoms.append(0)


         #update 1 where symptoms gets matched...
         for k in range(0, len(symptomslist)):

            for z in range(0, len(psymptoms)):
               if (psymptoms[z] == symptomslist[k]):
               
                  testingsymptoms[k] = 1


         inputtest = [testingsymptoms]

         print(inputtest)
      

         predicted = model.predict(inputtest)
         print("predicted disease is : ")
         print(predicted)

         y_pred_2 = model.predict_proba(inputtest)
         confidencescore = y_pred_2.max() * 100
         print(" confidence score of : = {0} ".format(confidencescore))

         confidencescore = format(confidencescore, '.0f')
         predicted_disease = predicted[0]

         

         #consult_doctor codes----------

         #   doctor_specialization = ["Rheumatologist","Cardiologist","ENT specialist","Orthopedist","Neurologist",
         #                             "Allergist/Immunologist","Urologist","Dermatologist","Gastroenterologist"]
         

         Rheumatologist = [  'Osteoarthristis','Arthritis']
      
         Cardiologist = [ 'Heart attack','Bronchial Asthma','Hypertension ']
      
         ENT_specialist = ['(vertigo) Paroymsal  Positional Vertigo','Hypothyroidism' ]

         Orthopedist = []

         Neurologist = ['Varicose veins','Paralysis (brain hemorrhage)','Migraine','Cervical spondylosis']

         Allergist_Immunologist = ['Allergy','Pneumonia',
         'AIDS','Common Cold','Tuberculosis','Malaria','Dengue','Typhoid']

         Urologist = [ 'Urinary tract infection',
          'Dimorphic hemmorhoids(piles)']

         Dermatologist = [  'Acne','Chicken pox','Fungal infection','Psoriasis','Impetigo']

         Gastroenterologist = ['Peptic ulcer diseae', 'GERD','Chronic cholestasis','Drug Reaction','Gastroenteritis','Hepatitis E',
         'Alcoholic hepatitis','Jaundice','hepatitis A',
          'Hepatitis B', 'Hepatitis C', 'Hepatitis D','Diabetes ','Hypoglycemia']
          
         if predicted_disease in Rheumatologist :
            consultdoctor = "Rheumatologist"
            
         if predicted_disease in Cardiologist :
            consultdoctor = "Cardiologist"
            

         elif predicted_disease in ENT_specialist :
            consultdoctor = "ENT specialist"
      
         elif predicted_disease in Orthopedist :
            consultdoctor = "Orthopedist"
      
         elif predicted_disease in Neurologist :
            consultdoctor = "Neurologist"
      
         elif predicted_disease in Allergist_Immunologist :
            consultdoctor = "Allergist/Immunologist"
      
         elif predicted_disease in Urologist :
            consultdoctor = "Urologist"
      
         elif predicted_disease in Dermatologist :
            consultdoctor = "Dermatologist"
      
         elif predicted_disease in Gastroenterologist :
            consultdoctor = "Gastroenterologist"
      
         else :
            consultdoctor = "other"


         request.session['doctortype'] = consultdoctor 

      #    patientusername = request.session['patientusername']
      #    puser = User.objects.get(username=patientusername)
      

         #saving to database.....................

      #    patient = puser.patient
         diseasename = predicted_disease
         no_of_symp = inputno
         symptomsname = psymptoms
         confidence = confidencescore
         pat = Patient.objects.filter(user = request.user).first()

         diseaseinfo_new = diseaseinfo(patient=pat,diseasename=diseasename,no_of_symp=no_of_symp,symptomsname=symptomsname,confidence=confidence,consultdoctor=consultdoctor)
         diseaseinfo_new.save()
         

     

      #    print("disease record saved sucessfully.............................")

         return Response({'predicteddisease': predicted_disease ,'confidencescore':confidencescore , "consultdoctor": consultdoctor})
   

@api_view(['POST'])
@permission_classes((permissions.IsAuthenticated,))
def heartDisease(request):
   if request.method == 'POST':

      age = float(request.data.get('age'))
      sex = float(request.data.get('sex'))
      cp = float(request.data.get('cp'))
      trestbps = float(request.data.get('trestbps'))
      chol = float(request.data.get('chol'))
      fbs = float(request.data.get('fbs'))
      restecg = float(request.data.get('restecg'))
      thalach = float(request.data.get('thalach'))
      exang = float(request.data.get('exang'))
      oldpeak = float(request.data.get('oldpeak'))
      slope = float(request.data.get('slope'))
      ca = float(request.data.get('ca'))
      thal = float(request.data.get('thal'))
      user_data = np.array(
          (age,
           sex,
           cp,
           trestbps,
           chol,
           fbs,
           restecg,
           thalach,
           exang,
           oldpeak,
           slope,
           ca,
           thal)
      ).reshape(1, -1)

      val = heartModel.predict_proba(user_data)[0][1]*100
      val = round(val, 2)
      comment = ''
      print(val)
      if val < 50:
         comment='You are not at risk, but stay healthy'
      elif val >= 50 and val <=80:
         comment='You have a high chance of having a heart disease, please consult a cardiologist'
      elif val > 80:
         comment = 'You have heart disease, please consult our doctor immediately'
      #serializer = HeartDiseaseSerializer(data=request.data)
      #if serializer.is_valid(raise_exception=ValueError):
      #  serializer.create(validated_data=request.data)
      pat = Patient.objects.filter(user = request.user).first()
      heartDisease_new = HeartDisease(
           patient=pat,
           age =age,
           sex = sex,
           cp = cp,
           trestbps = trestbps,
           chol = chol,
           fbs = fbs,
           restecg = restecg,
           thalach = thalach,
           exang = exang,
           oldpeak = oldpeak,
           slope = slope,
           ca  = ca,
           thal = thal,
           confidence = val,
           comment = comment)
      heartDisease_new.save()
      
      return Response({
         'score': val,
         'comment': comment
      }

      )   

@api_view(['POST'])
@permission_classes((permissions.IsAuthenticated,))
def diabetes(request):
   diabetesModel = jb.load(AI_Models_ROOT +'/diabetes')
   if request.method == 'POST':
      pregnancies = float(request.data.get('pregnancies'))
      glucose = float(request.data.get('glucose'))
      bloodpressure = float(request.data.get('bloodpressure'))
      skinthickness = float(request.data.get('skinthickness'))
      bmi = float(request.data.get('bmi'))
      insulin = float(request.data.get('insulin'))
      age = float(request.data.get('age'))

      user_data = np.array(
            (pregnancies,
             glucose,
             bloodpressure,
             skinthickness,
             bmi,
             insulin,
             age)
        ).reshape(1, 7)

      val =  diabetesModel.predict_proba(user_data)[0][1]*100
      val = round(val, 2)
      print(val)
      pred =  diabetesModel.predict_proba(user_data)
      comment = ''
      print(val)
      if val < 60:
         comment='You are not at risk, but stay healthy'
      elif val >= 60 and val <=80:
         comment='You have a high chance of having diabetes, please consult a doctor'
      elif val > 80:
         comment = 'You have diabetes, please consult our doctor immediately'
      print(comment)
      # serializer = DiabetesSerializer(data=request.data)
      # if serializer.is_valid(raise_exception=ValueError):
      #    serializer.create(validated_data=request.data)
      pat = Patient.objects.filter(user = request.user).first()
      diabetes_new = Diabetes(
         patient = pat,
         pregnancies = pregnancies,
         glucose = glucose,
         bloodpressure = bloodpressure,
         skinthickness = skinthickness,
         bmi = bmi,
         insulin = insulin,
         age = age,
         confidence = val,
         comment = comment,

      )
      diabetes_new.save()

      
      return Response({
         'score': val,
         'comment': comment
      }

      )

@api_view(['POST'])
@permission_classes((permissions.IsAuthenticated,))
def breastCancer(request):
   if request.method == 'POST':
      radius_mean = float(request.data.get('radius_mean'))
      texture_mean = float(request.data.get('texture_mean'))
      perimeter_mean = float(request.data.get('perimeter_mean'))
      area_mean =  float(request.data.get('area_mean'))
      smoothness_mean = float(request.data.get('smoothness_mean'))
      compactness_mean = float(request.data.get('compactness_mean'))
      concavity_mean = float(request.data.get('concavity_mean'))
      concave_points_mean = float(request.data.get('concave_points_mean'))
      symmetry_mean = float(request.data.get('symmetry_mean'))
      fractal_dimension_mean = float(request.data.get('fractal_dimension_mean'))
      radius_se = float(request.data.get('radius_se'))
      texture_se = float(request.data.get('texture_se'))
      perimeter_se = float(request.data.get('perimeter_se'))
      area_se = float(request.data.get('area_se'))
      smoothness_se = float(request.data.get('smoothness_se'))
      compactness_se = float(request.data.get('compactness_se'))
      concavity_se = float(request.data.get('concavity_se'))
      concave_points_se = float(request.data.get('concave_points_se'))
      symmetry_se = float(request.data.get('symmetry_se'))
      fractal_dimension_se = float(request.data.get('fractal_dimension_se'))
      radius_worst = float(request.data.get('radius_worst'))
      texture_worst = float(request.data.get('texture_worst'))
      perimeter_worst = float(request.data.get('perimeter_worst'))
      area_worst = float(request.data.get('area_worst'))
      smoothness_worst = float(request.data.get('smoothness_worst'))
      compactness_worst = float(request.data.get('compactness_worst'))
      concavity_worst = float(request.data.get('concavity_worst'))
      concave_points_worst = float(request.data.get('concave_points_worst'))
      symmetry_worst = float(request.data.get('symmetry_worst'))
      fractal_dimension_worst = float(request.data.get('fractal_dimension_worst'))
      user_data = np.array(
         (
            radius_mean, 
            texture_mean,
            perimeter_mean, 
            area_mean,
            smoothness_mean, 
            compactness_mean, 
            concavity_mean, 
            concave_points_mean, 
            symmetry_mean,
            fractal_dimension_mean, 
            radius_se, 
            texture_se, 
            perimeter_se, 
            area_se,
            smoothness_se, 
            compactness_se, 
            concavity_se,
            concave_points_se, 
            symmetry_se, 
            fractal_dimension_se, 
            radius_worst, 
            texture_worst, 
            perimeter_worst, 
            area_worst, 
            smoothness_worst, 
            compactness_worst, 
            concavity_worst, 
            concave_points_worst,  
            symmetry_worst, 
            fractal_dimension_worst
         )
      ).reshape(1,30)

      probability =  breastModel.predict_proba(user_data)[0][1]*100
      probability = round(probability,2)
      pred =  breastModel.predict(user_data)
      print(probability)

      if pred == 'M':
         comment = 'The tumor is malignant and the patient has Breast Cancer'
         pred = 1
      else:
         comment =  "The patient is safe and the tumor is benign"
         pred = 0
      # serializer = BreastCancerSerializer(data=request.data)
      # if serializer.is_valid(raise_exception=ValueError):
      #    serializer.create(validated_data=request.data)
      pat = Patient.objects.filter(user = request.user).first()
      breastCancer_new = BreastCancer(
         patient = pat,
         radius_mean = radius_mean, 
         texture_mean = texture_mean,
         perimeter_mean = perimeter_mean, 
         area_mean = area_mean,
         smoothness_mean = smoothness_mean, 
         compactness_mean = compactness_mean, 
         concavity_mean = concavity_mean, 
         concave_points_mean = concave_points_mean, 
         symmetry_mean = symmetry_mean,
         fractal_dimension_mean = fractal_dimension_mean, 
         radius_se = radius_se, 
         texture_se = texture_se, 
         perimeter_se = perimeter_se, 
         area_se = area_se,
         smoothness_se = smoothness_se, 
         compactness_se = compactness_se, 
         concavity_se = concavity_se,
         concave_points_se = concave_points_se, 
         symmetry_se = symmetry_se, 
         fractal_dimension_se = fractal_dimension_se, 
         radius_worst = radius_worst, 
         texture_worst = texture_worst, 
         perimeter_worst = perimeter_worst, 
         area_worst = area_worst, 
         smoothness_worst = smoothness_worst, 
         compactness_worst = compactness_worst, 
         concavity_worst = concavity_worst, 
         concave_points_worst = concave_points_worst,  
         symmetry_worst = symmetry_worst, 
         fractal_dimension_worst = fractal_dimension_worst,
         confidence = probability,
         comment = comment,
         prediction = pred,
      )
      breastCancer_new.save()
      
      
      return Response({
         'score': probability,
         'comment': comment,
         'prediction' : pred
      }

      )


class skinCancer(generics.GenericAPIView):

    permission_classes = [
    permissions.IsAuthenticated,
  ]
    skinModel = tf.keras.models.load_model(AI_Models_ROOT + '/model.h5',custom_objects={'KerasLayer':hub.KerasLayer})
    serializer_class =  SkinCancerSerializer
    
    # Resize image to given dimensions
    resizing_layer = tf.keras.layers.experimental.preprocessing.Resizing(384, 384)  
    def post(self, request, format=None):
        serializer = SkinCancerSerializer(data=request.data)
        if serializer.is_valid():
            pat = Patient.objects.filter(user = request.user).first()

            image = request.FILES['image'].name
            print(image)
            image_path = MEDIA_ROOT + '/' + image
            
            
            img = cv2.imread(image_path)
            # resize image to match model's expected sizing
            img = cv2.resize(img,(384,384),3)
            img = img.reshape(1,384,384,3) 
            img = self.resizing_layer(img)
            
            prediction = self.skinModel.predict(img)
            sc = self.skinModel.predict_proba(img)
            print(prediction[0][0])
            print(sc)
            val = int(prediction[0][0])
            
            if val == 1:
               comment = 'The tumor is melignant'
            if val == 0:
               comment = 'The tumor is benign'
            print(val)
            print(comment)
            serializer.save(patient= pat, prediction = val)

            return Response({
               'score': val,
               'comment': comment
            })
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET'])
@permission_classes((permissions.IsAuthenticated,))
def pconsultation_history(request):

    if request.method == 'GET':

      # patientusername = request.session['patientusername']
      puser = Patient.objects.filter(user = request.user).first()
      #patient_obj = puser.patient
        
      consultationnew = consultation.objects.filter(patient = puser)
      
      #serializer = consultationSerializer(consultationnew, many=True)
      return Response({"consultation":consultationnew})

@api_view(['GET'])
@permission_classes((permissions.IsAuthenticated,))
def dconsultation_history(request):

    if request.method == 'GET':

      #doctorusername = request.session['doctorusername']
      duser = Doctor.objects.filter(user = request.user).first()
      #doctor_obj = duser.doctor
        
      consultationnew = consultation.objects.filter(doctor = duser)
      
      serializer = consultationSerializer(consultationnew, many=True)
      return Response({"consultation":consultationnew})



# def doctor_ui(request):

#     if request.method == 'GET':

#       doctorid = request.session['doctorusername']
#       duser = User.objects.get(username=doctorid)

    
#       return render(request,'doctor/doctor_ui/profile.html',{"duser":duser})



      


# def dviewprofile(request, doctorusername):

#     if request.method == 'GET':

         
#          duser = User.objects.get(username=doctorusername)
#          r = rating_review.objects.filter(doctor=duser.doctor)
       
#          return render(request,'doctor/view_profile/view_profile.html', {"duser":duser, "rate":r} )








       
# def  consult_a_doctor(request):


#     if request.method == 'GET':

        
#         doctortype = request.session['doctortype']
#         print(doctortype)
#         dobj = doctor.objects.all()
#         #dobj = doctor.objects.filter(specialization=doctortype)


#         return render(request,'patient/consult_a_doctor/consult_a_doctor.html',{"dobj":dobj})

   


# def  make_consultation(request, doctorusername):

#     if request.method == 'POST':
       

#         patientusername = request.session['patientusername']
#         puser = User.objects.get(username=patientusername)
#         patient_obj = puser.patient
        
        
#         #doctorusername = request.session['doctorusername']
#         duser = User.objects.get(username=doctorusername)
#         doctor_obj = duser.doctor
#         request.session['doctorusername'] = doctorusername


#         diseaseinfo_id = request.session['diseaseinfo_id']
#         diseaseinfo_obj = diseaseinfo.objects.get(id=diseaseinfo_id)

#         consultation_date = date.today()
#         status = "active"
        
#         consultation_new = consultation( patient=patient_obj, doctor=doctor_obj, diseaseinfo=diseaseinfo_obj, consultation_date=consultation_date,status=status)
#         consultation_new.save()

#         request.session['consultation_id'] = consultation_new.id

#         print("consultation record is saved sucessfully.............................")

         
#         return redirect('consultationview',consultation_new.id)



# def  consultationview(request,consultation_id):
   
#     if request.method == 'GET':

   
#       request.session['consultation_id'] = consultation_id
#       consultation_obj = consultation.objects.get(id=consultation_id)

#       return render(request,'consultation/consultation.html', {"consultation":consultation_obj })

#    #  if request.method == 'POST':
#    #    return render(request,'consultation/consultation.html' )





# def rate_review(request,consultation_id):
#    if request.method == "POST":
         
#          consultation_obj = consultation.objects.get(id=consultation_id)
#          patient = consultation_obj.patient
#          doctor1 = consultation_obj.doctor
#          rating = request.POST.get('rating')
#          review = request.POST.get('review')

#          rating_obj = rating_review(patient=patient,doctor=doctor1,rating=rating,review=review)
#          rating_obj.save()

#          rate = int(rating_obj.rating_is)
#          doctor.objects.filter(pk=doctor1).update(rating=rate)
         

#          return redirect('consultationview',consultation_id)





# def close_consultation(request,consultation_id):
#    if request.method == "POST":
         
#          consultation.objects.filter(pk=consultation_id).update(status="closed")
         
#          return redirect('home')






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



# def chat_messages(request):
#    if request.method == "GET":

#          consultation_id = request.session['consultation_id'] 

#          c = Chat.objects.filter(consultation_id=consultation_id)
#          return render(request, 'consultation/chat_body.html', {'chat': c})


#-----------------------------chatting system ---------------------------------------------------