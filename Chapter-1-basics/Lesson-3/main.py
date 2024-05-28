

# data structure where we store final results gradually 
requiredDocuments = []
# get the age from console
age = input("العمر"[::-1])
# if this correct just append this one time and finish since we don't need any extra info
if(int(age)< 18):
    requiredDocuments.append('إخراج قيد'[::-1])
# if not, we continue asking questions:
elif(int(age)>= 18):
  if(int(age) < 42):
    # here is users with age scope 18 < and 42 < ,so if there is a male in this scope we require: موافقة شعبة التجنيد
    # if user is female we add nothing.
    while True:
            print('الجنس'[::-1])
            print('1 - ذكر'[::-1])
            print('2- أنثى'[::-1])
            gender = input('')
            # validating the answer : should be either 1 or 2 only
            if(gender not in ['1','2']):
                print('إدخال خاطئ'[::-1])
            else:
                # if user is male:
                if(int(gender) == 1):
                  requiredDocuments.append(' موافقة شعبة التجنيد'[::-1])
                break
  while True:
        # checking for الهوية الشخصية
        print('الهوية الشخصية موجودة؟'[::-1])
        print('1- نعم'[::-1])
        print('2- لا'[::-1])
        haveIdentityCard = input('')
        # validating the answer
        if(haveIdentityCard not in ['1','2']):
            print('إدخال خاطئ'[::-1])
        else:
            # if yes
            if(haveIdentityCard == '1'):
               requiredDocuments.append('الهوية الشخصية'[::-1])
            else:
            # if no
               requiredDocuments.append('إخراج قيد'[::-1])
               requiredDocuments.append('ضبط شرطة'[::-1])   
            break
  while True:
        print('هل أنت موظف؟'[::-1])
        print('1- نعم'[::-1])
        print('2- لا'[::-1])
        isEmployee = input('')
        if(isEmployee not in ['1','2']):
            print('إدخال خاطئ'[::-1])
        else:
            if(isEmployee == '1'):
               requiredDocuments.append(' صورة عن موافقة جهة التوظيف.'[::-1])
            break
# printing the results to the console
print(requiredDocuments)
