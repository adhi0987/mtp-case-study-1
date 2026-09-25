# mtp-case-study-1
this repo contains the case study which we are using for determining the probabilities of the prompt injection attaacks getting successful
## prompt injection 
exploiting sensitive information from the Large Language Models using prompts 

## case study
Here in this case study we try to create a baseline data for our future proof-of-concept on estimation of likelihood of success for AI vulnerabilities for three different attacker type [amateur, skilled, expert] 
### Personal Data
here we have created a person records like this 
each person  we have personal and some medical record information 
```
name, age, gender, phone-no, email, blood-group, mrn(medical record number), aadhar(aadhar number). 
```
these 6 records are attacched with a record-id them 
personal information dataset is list of jsons where is json is 
```
{
    "id" :1,
    "name":"john doe",
    "age" : 23,
    "gender" : "male",
    "email":"johndoe@example.com",
    "phoneno": "3123313132",
    "mrn":"mrn123456789",
    "aadhar":"956030040232" 
}
```
#### Specifications 
id : int <br>
name : string <br>
age: int<br>
gender : string["male" , "female"] <br>
email: string ending with @example.com<br>
phoneno: string with 10 digits<br>
mrn: string starting with mrn remaining 9 characters is [0-9] <br>
aadhar : string with 12 characters each character is [0-9]<br>
