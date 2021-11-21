
from os import times
from flask import Flask, render_template, request, session
from flask import make_response
from flask_wtf import csrf
from pandas.core.indexes.base import Index
from sqlalchemy import types, create_engine
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql.elements import Null
from sqlalchemy.sql.expression import false
from werkzeug.exceptions import HTTPException
from datetime import timedelta
import pandas as pd
import time
import pymysql
import json
import rsa
import base64
import numpy as np
import statsmodels.api as sm

import sqlalchemy
import forms

import logging

from werkzeug.utils import redirect

# Flask App 생성
app = Flask(__name__)
app.app_context().push()
#dir_path = "/home/kyeongmin/Desktop/flask/"
private_key_bytes = ...
app.config['SECRET_KEY'] = private_key_bytes


## FOR LOG SYSTEM

now = time.localtime()
datetime = "%04d%02d%02d" % (now.tm_year, now.tm_mon, now.tm_mday)
# file = "home/kyeongmin/Desktop/flask/log/" + datetime + ".log"
file = "D:/labs/moca_mmse/" + datetime + ".log"
#file = datetime + ".log"
logging.basicConfig(filename = file, level = logging.DEBUG)

## LOG SYSTEM END

conn = None
engine_value = None
# dir_path = "/home/kyeongmin/Desktop/flask/"
dir_path = 'D:/labs/moca_mmse/'
def database_connect() :
    global conn
    engine = create_engine("mysql+pymysql://...", encoding='utf-8')
    conn = engine.connect()
    conn.execute("use moca")
    return conn

def database_connect_engine() :
    global conn
    global engine_value
    engine_value = create_engine("mysql+pymysql://...", encoding='utf-8')
    conn = engine_value.connect()
    return engine_value
    
def cut_off(y, threshold) :
    cut = y.copy()
    cut[cut>=threshold] = 1
    cut[cut<threshold] = 0
    return cut.astype(float)
def database_disconnect() :
    global conn
    if conn != None :
        conn.close()
        conn = None

def load_model(age, gender, educyrs, handed, diag_duration, mcaalttm, mcacube, mcaclckc, mcaclckn, mcaclckh, mcalion, mcarhino, mcacamel, mcafds, 
                                             mcabds, mcavigil, mcaser7, mcasntnc, mcavf, mcavfnum, mcaabstr, mcarec1, mcarec2, mcarec3, mcarec4, mcarec5, mcadate, mcamonth, mcayr, mcaday, 
                                             mcaplace, mcacity, cog_cmplt) :
    input_df = pd.DataFrame(data = np.array([[age, gender, educyrs, handed, diag_duration, mcaalttm, mcacube, mcaclckc, mcaclckn, mcaclckh, mcalion, mcarhino, mcacamel, mcafds, 
                                             mcabds, mcavigil, mcaser7, mcasntnc, mcavf, mcavfnum, mcaabstr, mcarec1, mcarec2, mcarec3, mcarec4, mcarec5, mcadate, mcamonth, mcayr, mcaday, 
                                             mcaplace, mcacity, cog_cmplt]]), 
                                             columns = ['AGE', 'GENDER', 'EDUCYRS', 'HANDED', 'DIAG_DURATION', 'MCAALTTM', 'MCACUBE', 'MCACLCKC', 
                                               'MCACLCKN', 'MCACLCKH', 'MCALION', 'MCARHINO', 'MCACAMEL', 'MCAFDS',
                                               'MCABDS', 'MCAVIGIL', 'MCASER7', 'MCASNTNC', 'MCAVF', 'MCAVFNUM',
                                               'MCAABSTR', 'MCAREC1', 'MCAREC2', 'MCAREC3', 'MCAREC4', 'MCAREC5',
                                               'MCADATE', 'MCAMONTH', 'MCAYR', 'MCADAY', 'MCAPLACE', 'MCACITY', 'COG_CMPLT'
                                               ]
                           )
    
    model = sm.load("Dataset_a2.pickle")
    logistic_predict = model.predict(sm.add_constant(input_df.astype(float), prepend = True, has_constant = 'add'))
    return logistic_predict[0]


def encrypted(msg) :
#    dir_path = './'



    return encrypted_msg

def decrypted(encrypted_msg) :
#    dir_path = './'

    return msg
    



    
@app.route('/index.html')       #메인 도메인 라우트
def index():
                        
    return render_template("/index.html")       #메인 도메인으로 접속한 경우 index.html템플릿 반환
                                                                #html파일에서 활용할 제목 변수 title에 요소 할당
    

@app.route('/output_database.html', methods = ['GET', 'POST'])                          
def output_database() :
    if session.get('email', None) == None :
        return redirect("/")
    else :
        username = session.get('email', None)
        message = "None"
        if request.method == 'GET' :
            current_user = session.get('email', None)
            conn = database_connect()
            query = "select GENDER, AGE, EDUCYRS, Category, HANDED, MCATOT, COGCAT_TEXT, LABEL,TIME from temp_moca where EMAIL = " + "\"" + current_user + "\""
            instance = conn.execute(query)
            information_df = pd.read_sql("select  GENDER, AGE, EDUCYRS, Category, HANDED, MCATOT, COGCAT_TEXT, LABEL, TIME from temp_moca where EMAIL = " + "\"" + current_user + "\"", conn)
            # col = information_df.columns
            col = ["GENDER", "AGE", "EDUCYRS", "Category", "HANDED", "MCATOT", "COGCAT_TEXT", "LABEL", "TIME"]
            database_disconnect()
            try :
                df_column = "GENDER"
                normal_df = information_df[information_df['COGCAT_TEXT'] == "Normal"]
                other_df = information_df[information_df['COGCAT_TEXT'] == "Dementia"]
                normal_value_counts = normal_df[df_column].value_counts().tolist()
                normal_value = normal_df[df_column].value_counts().index.tolist()
                other_value_counts = other_df[df_column].value_counts().tolist()
                other_value = other_df[df_column].value_counts().index.tolist()
                return render_template("output_database.html", title = "information",  username = username, waring_message = message, col = col, column = df_column,  data_list = instance , normal_column = normal_value, normal_instance = normal_value_counts, other_column = other_value, other_instance = other_value_counts)
            except KeyError or IndexError as e:
                print(e)
        else : #request.method == POST
            current_user = session.get('email', None)
            conn = database_connect()
            query = "select GENDER, AGE, EDUCYRS, Category, HANDED, MCATOT, COGCAT_TEXT, LABEL, TIME from temp_moca where EMAIL = " + "\"" + current_user + "\""
            instance = conn.execute(query)
            information_df = pd.read_sql("select GENDER, AGE, EDUCYRS, Category, HANDED, MCATOT, COGCAT_TEXT, LABEL, TIME from temp_moca where EMAIL = " + "\"" + current_user + "\"", conn)
            col = ["GENDER", "AGE", "EDUCYRS", "Category", "HANDED", "MCATOT", "COGCAT_TEXT", "LABEL", "TIME"]
            database_disconnect()
            normal_df = information_df[information_df['COGCAT_TEXT'] == 'Normal']
            other_df = information_df[information_df['COGCAT_TEXT'] == 'Dementia']

            df_column = request.values.get('df_column')
            if df_column == None :
                message = "그래프를 그릴 속성을 선택해 주세요."
                return render_template("output_database.html", title = "information", username = username, waring_message = message, col = col, data_list = instance)
            elif df_column == 'MCATOT' :

                normal_value = normal_df[df_column].value_counts().sort_index(ascending=False).index.tolist()
                normal_value.append("NA")
                normal_value_counts = normal_df[df_column].value_counts().sort_index(ascending=False).tolist()
                normal_value_counts.append(normal_df[df_column].isna().sum())
                other_value = other_df[df_column].value_counts().sort_index(ascending=False).index.tolist()
                other_value.append("NA")
                other_value_counts = other_df[df_column].value_counts().sort_index(ascending=False).tolist()
                other_value_counts.append(other_df[df_column].isna().sum())

            elif df_column == 'AGE' :
                normal_value = ["over than 90", "80 ~ 90", "70 ~ 80", "60 ~ 70", "50 ~ 60", "40 ~ 50", "under than 40", "NA"]
                normal_value_counts = [normal_df[(normal_df[df_column]>=90)][df_column].value_counts().sort_index(ascending=False).sum().tolist(),
                normal_df[(normal_df[df_column]>=80)&(normal_df[df_column] < 90)][df_column].value_counts().sort_index(ascending=False).sum().tolist(),
                normal_df[(normal_df[df_column]>=70)&(normal_df[df_column] < 80)][df_column].value_counts().sort_index(ascending=False).sum().tolist(),
                normal_df[(normal_df[df_column]>=60)&(normal_df[df_column] < 70)][df_column].value_counts().sort_index(ascending=False).sum().tolist(),
                normal_df[(normal_df[df_column]>=50)&(normal_df[df_column] < 60)][df_column].value_counts().sort_index(ascending=False).sum().tolist(),
                normal_df[(normal_df[df_column]>=40)&(normal_df[df_column] < 50)][df_column].value_counts().sort_index(ascending=False).sum().tolist(),
                normal_df[(normal_df[df_column]<40)][df_column].value_counts().sort_index(ascending=False).sum().tolist(),
                normal_df[df_column].isna().sum()]

                other_value = ["over than 90", "80 ~ 90", "70 ~ 80", "60 ~ 70", "50 ~ 60", "40 ~ 50", "under than 40", "NA"]
                other_value_counts = [other_df[(other_df[df_column]>=90)][df_column].value_counts().sort_index(ascending=False).sum().tolist(),
                other_df[(other_df[df_column]>=80)&(other_df[df_column] < 90)][df_column].value_counts().sort_index(ascending=False).sum().tolist(),
                other_df[(other_df[df_column]>=70)&(other_df[df_column] < 80)][df_column].value_counts().sort_index(ascending=False).sum().tolist(),
                other_df[(other_df[df_column]>=60)&(other_df[df_column] < 70)][df_column].value_counts().sort_index(ascending=False).sum().tolist(),
                other_df[(other_df[df_column]>=50)&(other_df[df_column] < 60)][df_column].value_counts().sort_index(ascending=False).sum().tolist(),
                other_df[(other_df[df_column]>=40)&(other_df[df_column] < 50)][df_column].value_counts().sort_index(ascending=False).sum().tolist(),
                other_df[(other_df[df_column]<40)][df_column].value_counts().sort_index(ascending=False).sum().tolist(),
                other_df[df_column].isna().sum()]
            elif df_column == 'EDUCYRS' :
                normal_value = ["over than 23", "19 ~ 22", "17 ~ 18", "13 ~ 16", "under than 12", "NA"]

                normal_value_counts = [normal_df[(normal_df[df_column]>=23)][df_column].value_counts().sort_index(ascending=False).sum().tolist(),
                normal_df[(normal_df[df_column]>=19)&(normal_df[df_column] < 23)][df_column].value_counts().sort_index(ascending=False).sum().tolist(),
                normal_df[(normal_df[df_column]>=17)&(normal_df[df_column] < 19)][df_column].value_counts().sort_index(ascending=False).sum().tolist(),
                normal_df[(normal_df[df_column]>=13)&(normal_df[df_column] < 17)][df_column].value_counts().sort_index(ascending=False).sum().tolist(),
                normal_df[(normal_df[df_column]<13)][df_column].value_counts().sort_index(ascending=False).sum().tolist(),
                normal_df['AGE'].isna().sum()]

                other_value = ["over than 23", "19 ~ 22", "17 ~ 18", "13 ~ 16", "under than 12", "NA"]

                other_value_counts = [other_df[(other_df[df_column]>=23)][df_column].value_counts().sort_index(ascending=False).sum().tolist(),
                other_df[(other_df[df_column]>=19)&(other_df[df_column] < 23)][df_column].value_counts().sort_index(ascending=False).sum().tolist(),
                other_df[(other_df[df_column]>=17)&(other_df[df_column] < 19)][df_column].value_counts().sort_index(ascending=False).sum().tolist(),
                other_df[(other_df[df_column]>=13)&(other_df[df_column] < 17)][df_column].value_counts().sort_index(ascending=False).sum().tolist(),
                other_df[(other_df[df_column]<13)][df_column].value_counts().sort_index(ascending=False).sum().tolist(),
                other_df['AGE'].isna().sum()]
            else : #case column == GENDER or HANDED or Category
                # normal_df = information_df[information_df['COGCAT_TEXT'] == "Normal"]
                # other_df = information_df[information_df['COGCAT_TEXT'] == "Dementia"]
                normal_value_counts = normal_df[df_column].value_counts().tolist()
                normal_value = normal_df[df_column].value_counts().index.tolist()
                normal_value.append("NA")
                normal_value_counts.append(normal_df[df_column].isna().sum())

                other_value_counts = other_df[df_column].value_counts().tolist()
                other_value = other_df[df_column].value_counts().index.tolist()
                other_value.append("NA")
                other_value_counts.append(other_df[df_column].isna().sum())

            return render_template("output_database.html", title = "information", username= username, col = col, waring_message = message,
             column = df_column, data_list = instance, normal_column = normal_value, normal_instance = normal_value_counts, other_column = other_value, other_instance = other_value_counts)

@app.route('/input_database.html', methods = ['GET', 'POST'])                         
def input_database(): 
    if session.get('email', None) == None :
        return redirect("/")
    form = forms.input_database()
    if request.method == 'GET' :
        return render_template("input_database.html", form = form, username = session.get('email', None))                   
    
    else :
        moca_dtype = {
            'EMAIL' : types.VARCHAR(length = 50),
            'PATNO' : types.VARCHAR(length = 300),
            'EDUCYRS' : types.INTEGER(),
            'GENDER' : types.VARCHAR(length = 50),
            'HANDED' : types.VARCHAR(length = 50),
            'AGE' : types.INTEGER(),
            'BIRTHDT' : types.VARCHAR(length = 50),
            'COGCAT_TEXT' : types.VARCHAR(length = 50),
            'MCTOT' : types.INTEGER(),
            'Category' : types.VARCHAR(length = 50),
            'EVENT_ID_MoCA' : types.VARCHAR(length = 50),
            'INFODT_MoCA' : types.VARCHAR(length = 50),
            'MCAALTTM' : types.INTEGER(),
            'MCACUBE' : types.INTEGER(),
            'MCACLCKC' : types.INTEGER(),
            'MCACLCKN' : types.INTEGER(),
            'MCACLCKH' : types.INTEGER(),
            'MCALION' : types.INTEGER(),
            'MCARHINO' : types.INTEGER(),
            'MCACAMEL' : types.INTEGER(),
            'MCAFDS' : types.INTEGER(),
            'MCABDS' : types.INTEGER(),
            'MCAVIGIL' : types.INTEGER(),
            'MCASER7' : types.INTEGER(),
            'MCASNTNC' : types.INTEGER(),
            'MCAVFNUM' : types.INTEGER(),
            'MCAVF' : types.INTEGER(),
            'ACAABSTR' : types.INTEGER(),
            'MCAREC1' : types.INTEGER(),
            'MCAREC2' : types.INTEGER(),
            'MCAREC3' : types.INTEGER(),
            'MCAREC4' : types.INTEGER(),
            'MCAREC5' : types.INTEGER(),
            'MCADATE' : types.INTEGER(),
            'MCAMONTH' : types.INTEGER(),
            'MCAYR' : types.INTEGER(),
            'MCADAY' : types.INTEGER(),
            'MCAPLACE' : types.INTEGER(),
            'MCACITY' : types.INTEGER(),
            'EVENT_ID_Cognitive' : types.VARCHAR(length = 50),
            'INFODT_Cognitive' : types.VARCHAR(length = 50),
            'TIME' : types.VARCHAR(length= 50),
            'PK' : types.VARCHAR(length = 200),
            'INDEX' : types.INTEGER,
            'label' : types.VARCHAR(length = 50),
        }
        input_df = pd.DataFrame(columns = ['EMAIL', 'PATNO', 'EDUCYRS', 'AGE', 'BIRTHDT',  'GENDER', 'HANDED', 'Category', 'MCATOT', 'COGCAT_TEXT', 'label',
        'EVENT_ID_MoCA', 'INFODT_MoCA',  'MCAALTTM', 'MCACUBE', 
        'MCACLCKC', 'MCACLCKN', 'MCACLCKH', 'MCALION', 'MCARHINO', 'MCACAMEL',
        'MCAFDS', 'MCABDS', 'MCAVIGIL', 'MCASER7', 'MCASNTNC', 'MCAVFNUM',
        'MCAVF', 'MCAABSTR', 'MCAREC1', 'MCAREC2', 'MCAREC3', 'MCAREC4',
        'MCAREC5', 'MCADATE', 'MCAMONTH', 'MCAYR', 'MCADAY', 'MCAPLACE',
        'MCACITY', 'EVENT_ID_Cognitive', 'INFODT_Cognitive', 'INDEX', 'TIME', 'PK'])
        input_df = input_df.append(pd.Series(), ignore_index=True)

        patient_no = request.form.get('patient_no')
        age = request.form.get('age')
        education = request.values.get('education_hidden')
        sex = request.values.get('sex_radio')
        handedness = request.values.get('hand_radio')
        category = request.values.get('category_radio')
        score = request.form.get('score')
        label = request.form.get('label')
        id = session.get('email', None)
        now = time.localtime()
        datetime = "%04d/%02d/%02d/%02d:%02d:%02d" % (now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec)
#        name = request.form.get('name')
        patient_no = encrypted(patient_no)
        input_df['EMAIL'] = id
        input_df['PATNO'] = patient_no
        input_df['AGE'] = age
        input_df['Category'] = category
        input_df['HANDED'] = handedness
        input_df['label'] = label
        input_df['MCATOT'] = score
        input_df['GENDER'] = sex
        input_df['EDUCYRS'] = education
        input_df['TIME'] = datetime
        input_df['PK'] = id + datetime
        
        engine = database_connect_engine()
        input_df.to_sql("temp_moca", engine, if_exists='append', index=False, dtype=moca_dtype)

        
        database_disconnect()

        return redirect('/')

# @app.route('/database_visualizing.html', methods = ['GET', 'POST'])
# def database_visualizing() :
#     conn = database_connect()

#     information_df = pd.read_sql("select * from information", conn)
#     nc = information_df['label'].value_counts()[1]
#     dementia = information_df['label'].value_counts()[0]
#     data = '{"dementia" : dementia, "nc" : nc}'
#     database_disconnect()
#     return render_template("database_visualizing.html", data = data)

# @app.route("/setcookie", methods = ["GET", "POST"])
# def setcookie() : #for database visualizing
    
#     df_column = request.form.get('df_column')
#     conn = database_connect()
#     information_df = pd.read_sql("select * from temp_moca", conn)
#     normal_df = information_df[information_df['label'] == "정상"]
#     other_df = information_df[information_df['label'] == "비정상"]
    
#     try :
#         normal_value_counts = normal_df[df_column].value_counts().tolist()
#         normal_value = normal_df[df_column].value_counts().index.tolist()
#         other_value_counts = other_df[df_column].value_counts().tolist()
#         other_value = other_df[df_column].value_counts().tolist()
#     except KeyError as e:
#         return render_template("output_database.html")
#     database_disconnect()
#     result_cookie = make_response(output_database())
#     result_cookie.set_cookie("column_name", json.dumps(df_column))
#     result_cookie.set_cookie("normal_value_index", json.dumps(normal_value))
#     result_cookie.set_cookie("other_value_index",json.dumps(other_value))
#     result_cookie.set_cookie("normal_value_counts", json.dumps(normal_value_counts))
#     result_cookie.set_cookie("other_value_counts", json.dumps(other_value_counts))

#     return result_cookie

# @app.route("/getcookie")
# def getcookie() :
#     return request.cookies.get("normal_value_index"), request.cookies.get("other_value_index")




@app.route("/register.html", methods = ["GET", "POST"])
def register() :
    form = forms.RegisterForm()

    if session.get('email', None) != None :
        return render_template("input_database.html", form = form, username = session.get('email', None))   
    

    
    message = "None"
    if form.validate_on_submit() :
        database_connect()
        email = request.form.get("email")
        password = request.form.get("password")
        password_check = request.form.get("password_check") #just check 
        
        encrypted_password = encrypted(password)
        try :
            conn.execute("insert into login values(%s, %s)", email, encrypted_password)
        except sqlalchemy.exc.IntegrityError: 
            message = "가입된 ID가 존재하거나, 비밀번호가 동일하지 않습니다."
            database_disconnect()
            return render_template("/register.html", form = form, waring_message = message)
        database_disconnect()
        return redirect("/")



    return render_template("./register.html", form = form, waring_message = message)

@app.route("/", methods = ['GET', 'POST'])
def login() :
    if session.get('email', None) != None :
        return redirect("/input_database.html")

    form = forms.LoginForm()
    if request.method == 'GET' :
        return render_template("/login.html", form = form)  
    if form.validate_on_submit() :
        database_connect()
        message = "None" 
        email = request.form.get("email")
        password = request.form.get("password")
        id_database = pd.read_sql("select * from login where email =" + "\""+ email + "\"", conn)

        if id_database.empty == True :
            message = "ID 또는 비밀번호가 틀립니다. 다시 입력해 주시기 바랍니다."
            return render_template("/login.html", form = form, waring_message = message) 
        
        else :
            if password == decrypted(id_database._get_value(0, "password")) :
                database_disconnect()
                session['email'] = email
                return redirect("/input_database.html")
            else :
                database_disconnect()
                message = "ID 또는 비밀번호가 틀립니다. 다시 입력해 주시기 바랍니다."
                return render_template("/login.html", form = form, waring_message = message)

@app.route("/logout.html", methods = ['GET'])
def logout() :
    session.clear()
    return redirect("/")

@app.before_request
def session_timeout() :
    session.permanent = False
    app.permanent_session_lifetime = timedelta(minutes = 10)




@app.route("/regression.html", methods = ["GET", "POST"])
def regression() :
    if session.get('email', None) == None :
        return redirect("/")
    
    username = session.get('email', None)

    form = forms.regression()
    if request.method == 'GET' :
        return render_template("/regression.html", form = form, username = username, result = "")  
    
    message = "None"
    result = None
    if form.validate_on_submit() :
        
        age = request.form.get("AGE")
        gender = request.form.get("GENDER")
        EDUCYRS = request.form.get("EDUCYRS")
        HANDED = request.form.get("HANDED")
        DIAG_DURATION = request.form.get("DIAG_DURATION")
        MOCA_vssp_exct = request.form.get("MOCA_vssp_exct")
        MOCA_CDT = request.form.get("MOCA_CDT")
        MOCA_ming = request.form.get("MOCA_ming")
        MOCA_attent = request.form.get("MOCA_attent")
        MOCA_lang = request.form.get("MOCA_lang")
        MOCA_abst = request.form.get("MOCA_abst")
        MOCA_memory = request.form.get("MOCA_memory")
        MOCA_orient = request.form.get("MOCA_orient")
        MCAVFNUM = request.form.get("MCAVFNUM")
        COGCMPLT = request.form.get("COGCMPLT")
        
        result = load_model(age = age, gender = gender, educyrs = EDUCYRS, handed = HANDED, diag_duration = DIAG_DURATION, moca_vssp_exct = MOCA_vssp_exct, moca_cdt = MOCA_CDT,
         moca_ming = MOCA_ming, moca_attent = MOCA_attent,
                 moca_lang = MOCA_lang, moca_abst = MOCA_abst, moca_memory = MOCA_memory, moca_orient = MOCA_orient, mcavfnum = MCAVFNUM, cog_cmplt = COGCMPLT)
        
        

    return render_template("/regression.html", form = form, username = username, result = result)

if __name__ == "__main__" :
    dir_path = './'
    private_key_bytes = ...

#    app.config['SECRET_KEY'] = private_key_bytes
#    app.config['SESSION_TYPE'] = 'filesystem'	

    #session.init_app(app)
    # csrf_object = csrf.CSRFProtect()
    # csrf_object.init_app(app)

    app.run(host = '0.0.0.0', port = 80, debug = True)

