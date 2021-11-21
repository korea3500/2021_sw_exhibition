function confirm_database() {
    const patient_no = document.getElementById('patient_no').value;
    const age = document.getElementById('age').value
    const score = document.getElementById('score').value;
    const sex = document.getElementsByName('sex_radio');
    const education = document.getElementsByName('education_radio');
    const category = document.getElementsByName('category_radio');
    const handedness = document.getElementsByName('hand_radio');
    

    // var temp = document.querySelector("input[name=='education_radio']:checked"); 
    // alert(temp.value);

    
    let sex_value;
    let handedness_value;
    let category_value;
    let education_value;
    let age_value;
    let result;
    let label_message;
    let label_age;
    let label_education;
    let exception;

    
    for(var i = 0; i < age.length; i++) {
        if(age[i].checked) {
            age_value = age[i].value
            
        }
    }
    // age 변환
    if(age > 0) {
        if(age < 60) {
            label_age = "57";
        }
        else if(age < 65) {
            label_age = "62";
        }
        else if(age < 70) {
            label_age = "67";
        }
        else if(age < 75) {
            label_age = "72";
        }
        else if(age < 80) {
            label_age = "77";
        }
        else if(age < 120) {
            label_age = "82";
        }
        else exception = "age must 0 < age < 120";
    }
    else if(age < 1) {
        exception = "age must 0 < age < 120";
    }
    else {
        exception = "age must have integer value"
    }
    
    //education_term 변환


    console.log(label_age);
    console.log(label_education)


    
    for(var i = 0; i < education.length; i++) {
        if(education[i].checked) {
            education_value = education[i].value
            
        }
    }
    if(education_value == "-1") {
        label_education = "-1";
        document.getElementById('education_hidden').value = label_education;
    }
    else if(education_value=="0") {
        label_education = "0";
        document.getElementById('education_hidden').value = label_education;
    }
    else if(education_value=="999") {
        
        education_value = document.getElementById('education_text').value;
        if(education_text === "" || education_text === undefined) {
            exception = "EDUCYRS column cannot be null";
        }
        document.getElementById("education_hidden").value = education_value;
        console.log(education_value);
        if(label_education < -1) {
            exception = ("education_value has incorrect value(button select)");
            console.log(label_education);
        }
        if(education_value > 0) {
            if(education_value < 7) {
                label_education = 1;
            }
            else if(education_value < 13) {
                label_education = 2;
            }
            else if(education_value < 99) {
                label_education = 3;
            }
        }
        else {
            exception = "education_value has incorrect value(button select)";
            console.log(label_education);
        }
    }
    else;
    
    for(var i = 0; i < sex.length; i++) {
        if(sex[i].checked) {
            sex_value = sex[i].value
            
        }
    }
    for(var i = 0; i < category.length; i++) {
        if(category[i].checked) {
            category_value = category[i].value
            
        }
    }
    for(var i = 0; i < handedness.length; i++) {
        if(handedness[i].checked) {
            handedness_value = handedness[i].value
            
        }
    }
        
    if(score > 30) {
        // alert("점수는 30점을 초과할 수 없습니다.");
        exception = "score_exception cannot over30";
    }
    else if(score < 0) {

        // alert("점수는 0점 미만일 수 없습니다.");
        exception = "score_exception cannot under0";
    }
    else;
    console.log(label_age);
    console.log(label_education)

    // if(patient_no == "") {
    //     exception = "patient_number column cannot be null";
    // }
    if(education_value == undefined) {
        exception = "education_term column cannot be null";
    }
    // if(sex_value == undefined) {
    //     exception = "sex column cannot be null"
    // }
    // if(handedness_value == undefined) {
    //     exception = "handedness column cannot be null"
    // }
    // if(category_value == undefined) {
    //     exception = "category column cannot be null";
    // }
    if(score == "") {
        exception = "score column cannot be null";
    }
    if(education_value == "999" && education_text == undefined) {
        exception = "please input education text"
    }
    if(education_value == "999" && education_text < 0) {
        exception = "education_term must be over than 0"
    }
    label_message = label(label_education, label_age, score)
    result = '환자번호 : ' + patient_no + '\nage : ' + age + '\n교육 받은 기간 : ' + education_value + '\n성별 : ' + sex_value + '\n주로 사용하는 손 : ' + handedness_value + '\n환자가 느끼는 인지능력 상태 : ' + category_value + '\n점수 : ' + score + "\n" + label_message;

    console.log(exception)

    if(exception === undefined) {
        return confirm(result)
    }
    else {
        alert(exception);
        return false;
    }
}

function label(education_value, age, score) {
    // const score = int(score_val);
    let label;
    let label_range;
    let SD;
    let m;
    let n;
    let result_message;
    if(education_value == "-1") {
        if(age <= 62) {
            SD = "4.20";
            n = "14";
            m = "13.43"
            label_range = "9/10";
            if(score > 9) {
                label = "0";
            }
            else label = "1";
            result_message = "\n평균 : " + m + "\n표준편차 : " + SD + "\n사례 수 : " + n + "\n절단 점수 : " + label_range + "\n정상(0) / 인지장애(1) : " + label;

        }
        else if(age == "67") {
            SD = "3.90";
            n = "41";
            m = "12.12"
            label_range = "8/9";
            if(score > 8) {
                label = "0";
            }
            else label = "1";
            result_message = "\n평균 : " + m + "\n표준편차 : " + SD + "\n사례 수 : " + n + "\n절단 점수 : " + label_range + "\n정상(0) / 인지장애(1) : " + label;        }
        else if(age == "72") {
            SD = "3.72";
            n = "59";
            m = "11.29"
            label_range = "7/8";
            if(score > 7) {
                label = "0";
            }
            else label = "1";
            result_message = "\n평균 : " + m + "\n표준편차 : " + SD + "\n사례 수 : " + n + "\n절단 점수 : " + label_range + "\n정상(0) / 인지장애(1) : " + label;        }
        else if(age == "77") {
            SD = "3.30";
            n = "33";
            m = "10.43"
            label_range = "7/8";
            if(score > 7) {
                label = "0";
            }
            else label = "1";
            result_message = "\n평균 : " + m + "\n표준편차 : " + SD + "\n사례 수 : " + n + "\n절단 점수 : " + label_range + "\n정상(0) / 인지장애(1) : " + label;        }
        else if(age == "82") {
            SD = "2.69";
            n = "33";
            m = "9.33"
            label_range = "6/7";
            if(score > 7) {
                label = "0";
            }
            else label = "1";
            result_message = "\n평균 : " + m + "\n표준편차 : " + SD + "\n사례 수 : " + n + "\n절단 점수 : " + label_range + "\n정상(0) / 인지장애(1) : " + label;        }
    }
    else if(education_value == "0") {
        if(age == "57") {
            SD = "5.32";
            n = "6";
            m = "19.67"
            label_range = "14/15";
            if(score > 14) {
                label = "0";
            }
            else label = "1";
            result_message = "\n평균 : " + m + "\n표준편차 : " + SD + "\n사례 수 : " + n + "\n절단 점수 : " + label_range + "\n정상(0) / 인지장애(1) : " + label;
        }
        else if(age == "62") {
            SD = "4.10";
            n = "19";
            m = "18.53"
            label_range = "14/15";
            if(score > 14) {
                label = "0";
            }
            else label = "1";
            result_message = "\n평균 : " + m + "\n표준편차 : " + SD + "\n사례 수 : " + n + "\n절단 점수 : " + label_range + "\n정상(0) / 인지장애(1) : " + label;
        }
        else if(age == "67") {
            SD = "3.61";
            n = "45";
            m = "17.02"
            label_range = "13/14";
            if(score > 13) {
                label = "0";
            }
            else label = "1";
            result_message = "\n평균 : " + m + "\n표준편차 : " + SD + "\n사례 수 : " + n + "\n절단 점수 : " + label_range + "\n정상(0) / 인지장애(1) : " + label;        }
        else if(age == "72") {
            SD = "3.58";
            n = "55";
            m = "16.69"
            label_range = "13/14";
            if(score > 13) {
                label = "0";
            }
            else label = "1";
            result_message = "\n평균 : " + m + "\n표준편차 : " + SD + "\n사례 수 : " + n + "\n절단 점수 : " + label_range + "\n정상(0) / 인지장애(1) : " + label;        }
        else if(age == "77") {
            SD = "3.48";
            n = "47";
            m = "16.30"
            label_range = "12/13";
            if(score > 12) {
                label = "0";
            }
            else label = "1";
            result_message = "\n평균 : " + m + "\n표준편차 : " + SD + "\n사례 수 : " + n + "\n절단 점수 : " + label_range + "\n정상(0) / 인지장애(1) : " + label;        }
        else if(age == "82") {
            SD = "3.58";
            n = "20";
            m = "16.50"
            label_range = "12/13";
            if(score > 7) {
                label = "0";
            }
            else label = "1";
            result_message = "\n평균 : " + m + "\n표준편차 : " + SD + "\n사례 수 : " + n + "\n절단 점수 : " + label_range + "\n정상(0) / 인지장애(1) : " + label;        }
        
    }
    else if(education_value == "1") {
        if(age == "57") {
            SD = "2.96";
            n = "41";
            m = "21.66"
            label_range = "18/19";
            if(score > 18) {
                label = "0";
            }
            else label = "1";
            result_message = "\n평균 : " + m + "\n표준편차 : " + SD + "\n사례 수 : " + n + "\n절단 점수 : " + label_range + "\n정상(0) / 인지장애(1) : " + label;
        }
        else if(age == "62") {
            SD = "4.03";
            n = "54";
            m = "20.30"
            label_range = "16/17";
            if(score > 16) {
                label = "0";
            }
            else label = "1";
            result_message = "\n평균 : " + m + "\n표준편차 : " + SD + "\n사례 수 : " + n + "\n절단 점수 : " + label_range + "\n정상(0) / 인지장애(1) : " + label;
        }
        else if(age == "67") {
            SD = "3.88";
            n = "79";
            m = "19.77"
            label_range = "15/16";
            if(score > 15) {
                label = "0";
            }
            else label = "1";
            result_message = "\n평균 : " + m + "\n표준편차 : " + SD + "\n사례 수 : " + n + "\n절단 점수 : " + label_range + "\n정상(0) / 인지장애(1) : " + label;        }
        else if(age == "72") {
            SD = "4.11";
            n = "72";
            m = "19.11"
            label_range = "15/16";
            if(score > 15) {
                label = "0";
            }
            else label = "1";
            result_message = "표준편차 : " + SD + "\n표본수 : " + n + "\n평균 : " + m + "\n절단점 : " + label_range + "\n정상 / 인지장애(1) : " + label;
        }
        else if(age == "77") {
            SD = "3.78";
            n = "58";
            m = "19.29"
            label_range = "15/16";
            if(score > 15) {
                label = "0";
            }
            else label = "1";
            result_message = "표준편차 : " + SD + "\n표본수 : " + n + "\n평균 : " + m + "\n절단점 : " + label_range + "\n정상 / 인지장애(1) : " + label;
        }
        else if(age == "82") {
            SD = "4.01";
            n = "24";
            m = "18.54"
            label_range = "14/15";
            if(score > 14) {
                label = "0";
            }
            else label = "1";
            result_message = "표준편차 : " + SD + "\n표본수 : " + n + "\n평균 : " + m + "\n절단점 : " + label_range + "\n정상 / 인지장애(1) : " + label;
        }
    }
    
    else if(education_value == "2") {
        if(age == "57") {
            SD = "2.48";
            n = "47";
            m = "24.11"
            label_range = "21/22";
            if(score > 21) {
                label = "0";
            }
            else label = "1";
            result_message = "표준편차 : " + SD + "\n표본수 : " + n + "\n평균 : " + m + "\n절단점 : " + label_range + "\n정상 / 인지장애(1) : " + label;

        }
        else if(age == "62") {
            SD = "2.72";
            n = "40";
            m = "22.75"
            label_range = "20/21";
            if(score > 20) {
                label = "0";
            }
            else label = "1";
            result_message = "표준편차 : " + SD + "\n표본수 : " + n + "\n평균 : " + m + "\n절단점 : " + label_range + "\n정상 / 인지장애(1) : " + label;

        }
        else if(age == "67") {
            SD = "2.94";
            n = "59";
            m = "22.64"
            label_range = "19/20";
            if(score > 19) {
                label = "0";
            }
            else label = "1";
            result_message = "표준편차 : " + SD + "\n표본수 : " + n + "\n평균 : " + m + "\n절단점 : " + label_range + "\n정상 / 인지장애(1) : " + label;
        }
        else if(age == "72") {
            SD = "3.31";
            n = "55";
            m = "22.25"
            label_range = "18/19";
            if(score > 18) {
                label = "0";
            }
            else label = "1";
            result_message = "표준편차 : " + SD + "\n표본수 : " + n + "\n평균 : " + m + "\n절단점 : " + label_range + "\n정상 / 인지장애(1) : " + label;
        }
        else if(age == "77") {
            SD = "3.51";
            n = "43";
            m = "22.12"
            label_range = "18/19";
            if(score > 18) {
                label = "0";
            }
            else label = "1";
            result_message = "표준편차 : " + SD + "\n표본수 : " + n + "\n평균 : " + m + "\n절단점 : " + label_range + "\n정상 / 인지장애(1) : " + label;
        }
        else if(age == "82") {
            SD = "3.96";
            n = "14";
            m = "20.57"
            label_range = "16/17";
            if(score > 16) {
                label = "0";
            }
            else label = "1";
            result_message = "표준편차 : " + SD + "\n표본수 : " + n + "\n평균 : " + m + "\n절단점 : " + label_range + "\n정상 / 인지장애(1) : " + label;
        }
    
    }
    else if(education_value == 3) {
        if(age == "57") {
            SD = "1.00";
            n = "3";
            m = "27.00"
            label_range = "26/27";
            if(score > 26) {
                label = "0";
            }
            else label = "1";
            result_message = "표준편차 : " + SD + "\n표본수 : " + n + "\n평균 : " + m + "\n절단점 : " + label_range + "\n정상 / 인지장애(1) : " + label;
        }
        else if(age == "62") {
            SD = "2.22";
            n = "4";
            m = "25.75"
            label_range = "23/24";
            if(score > 23) {
                label = "0";
            }
            else label = "1";
            result_message = "표준편차 : " + SD + "\n표본수 : " + n + "\n평균 : " + m + "\n절단점 : " + label_range + "\n정상 / 인지장애(1) : " + label;

        }
        else if(age == "67") {
            SD = "1.46";
            n = "19";
            m = "25.32"
            label_range = "23/24";
            if(score > 23) {
                label = "0";
            }
            else label = "1";
            result_message = "표준편차 : " + SD + "\n표본수 : " + n + "\n평균 : " + m + "\n절단점 : " + label_range + "\n정상 / 인지장애(1) : " + label;
        }
        else if(age == "72") {
            SD = "2.05";
            n = "23";
            m = "24.87"
            label_range = "22/23";
            if(score > 22) {
                label = "0";
            }
            else label = "1";
            result_message = "표준편차 : " + SD + "\n표본수 : " + n + "\n평균 : " + m + "\n절단점 : " + label_range + "\n정상 / 인지장애(1) : " + label;
        }
        else if(age == "77") {
            SD = "2.26";
            n = "24";
            m = "24.58"
            label_range = "22/23";
            if(score > 22) {
                label = "0";
            }
            else label = "1";
            // result_message = "표준편차 : " + SD + "\n표본수 : " + n + "\n평균 : " + m + "\n절단점 : " + label_range + "\n정상 / 인지장애(1) : " + label;
        }
        else if(age == "82") {
            SD = "3.17";
            n = "9";
            m = "23.56"
            label_range = "20/21";
            if(score > 20) {
                label = "0";
            }
            else label = "1";
            // result_message = "표준편차 : " + SD + "\n표본수 : " + n + "\n평균 : " + m + "\n절단점 : " + label_range + "\n정상 / 인지장애(1) : " + label;
        }
    

    }
    else;
    result_message = "\n평균 : " + m + "\n표준편차 : " + SD + "\n사례 수 : " + n + "\n절단 점수 : " + label_range + "\n정상(0) / 인지장애(1) : " + label;
    
    if(label == "0") {
        label = "정상";
    }
    else if(label == "1") {
        label = "비정상";
    }
    else;
    console.log(label);
    document.getElementById("label").value = label;
    
    return result_message;
}