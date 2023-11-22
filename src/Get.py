import requests

def Tokens(user, password):
    session = requests.session()
    
    login_url = 'https://edpuzzle.com/api/v3/users/login'
    login_data = {'username': user, 'password': password, 'role': "student"}
    
    login_response = session.post(url=login_url, data=login_data).headers
    
    csrf_token = str(login_response['set-cookie']).split(";")[0]
    csrf_token = csrf_token.split('=')[1]

    token = str(login_response['set-cookie']).split(";")[4]
    
    try:
        token = token.split('=')[2]
    except:
        return None, None

    return csrf_token, token

def Classes(csrf_token, token):
    url = 'https://edpuzzle.com/api/v3/classrooms/active'
    headers = {"cookie": f"G_ENABLED_IDPS=google; edpuzzleCSRF={csrf_token}; token={token}"}

    classes_response = requests.get(url=url, headers=headers).json()

    return list(classes_response)

def Assignments(classId, csrf_token, token):
    url = f'https://edpuzzle.com/api/v3/assignments/classrooms/{classId}/students?needle='
    headers = {"cookie": f"G_ENABLED_IDPS=google; edpuzzleCSRF={csrf_token}; token={token}"}

    assignments_response = requests.get(url=url, headers=headers).json()

    return assignments_response['medias']
