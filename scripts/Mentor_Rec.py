#Import necessary libraries

import pandas as pd
import streamlit as st
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import os
import requests
from io import StringIO  # Import StringIO directly from the io module
from io import BytesIO
from datetime import datetime
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseUpload
import io
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from tempfile import NamedTemporaryFile
from pydrive2.auth import GoogleAuth
from oauth2client.service_account import ServiceAccountCredentials
from pydrive2.drive import GoogleDrive
import streamlit as st
import pandas as pd
import pyperclip  # Import the pyperclip module for clipboard operations
import os
import requests
#from supabase_py import create_client,Client
#from supabase_py import create_client,Client
# Read the category dataset and extract unique categories

from supabase import create_client, Client
from supabase.client import ClientOptions



# Function to get the current timestamp
def get_timestamp():
    return datetime.now()

# Display the PNG image in the top left corner of the Streamlit sidebar with custom dimensions
image_path = 'https://twetkfnfqdtsozephdse.supabase.co/storage/v1/object/sign/stemcheck/VS-logo.png?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1cmwiOiJzdGVtY2hlY2svVlMtbG9nby5wbmciLCJpYXQiOjE3MjE5NzA3ODUsImV4cCI6MTc1MzUwNjc4NX0.purLZOGk272W80A4OlvnavqVB9u-yExhzpmI3dZrjdM&t=2024-07-26T05%3A13%3A02.704Z'
st.markdown(
    f'<div style="text-align:center"><img src="{image_path}" width="150"></div>',
    unsafe_allow_html=True
)

#Display the title of the Google form
st.markdown(
    "<h1 style='color: black; font-weight: bold;'>Kalpana - She for STEM Role Model and Mentor Recruitment Form</h1>", 
    unsafe_allow_html=True
)

#Google form Questions

Name=st.text_input("Enter your full name*")
Email_id=st.text_input("Enter your email address*")
Number=st.text_input("Enter your WhatsApp number (with country code, DONOT ADD '+')*")
Profile=st.text_input("Enter your LinkedIn profile link here")
Institute=st.text_input("Enter your current Institute/University/Organization*")
Current_job=st.text_input("Current Job title/Designation")
Degree = st.selectbox('Highest degree obtained*',("B.Sc.","M.Sc.","B.E./B.Tech.","M.Tech.","B.Pharm.","M.Pharm.","MBA","Ph.D."))
primary_key = f"{Number}_{Name}"

country_names = ["Afghanistan","Albania","Algeria","Andorra","Angola","Antigua and Barbuda","Argentina","Armenia","Australia","Austria","Azerbaijan","The Bahamas","Bahrain","Bangladesh","Barbados","Belarus","Belgium","Belize","Benin",
"Bhutan","Bolivia","Bosnia and Herzegovina","Botswana","Brazil","Brunei","Bulgaria","Burkina Faso","Burundi","Cabo Verde","Cambodia","Cameroon",
"Canada","Central African Republic","Chad","Chile","China","Colombia","Comoros","Congo, Democratic Republic of the Congo", "Republic of the","Costa Rica",
"Côte d’Ivoire","Croatia","Cuba","Cyprus","Czech Republic","Denmark",
"Djibouti","Dominica","Dominican Republic","East Timor (Timor-Leste)","Ecuador","Egypt","El Salvador","Equatorial Guinea","Eritrea","Estonia","Eswatini",
"Ethiopia","Fiji","Finland","France","Gabon","The Gambia","Georgia","Germany","Ghana","Greece","Grenada","Guatemala","Guinea","Guinea-Bissau","Guyana"
"Haiti","Honduras","Hungary","Iceland","India","Indonesia","Iran","Iraq","Ireland","Israel","Italy","Jamaica","Japan","Jordan","Kazakhstan","Kenya",
"Kiribati","Korea", "North Korea", "South Kosovo","Kuwait","Kyrgyzstan","Laos","Latvia","Lebanon","Lesotho","Liberia","Libya","Liechtenstein","Lithuania",
"Luxembourg","Madagascar","Malawi","Malaysia","Maldives","Mali","Malta","Marshall Islands","Mauritania","Mauritius","Mexico","Micronesia, Federated States of","Moldova",
"Monaco","Mongolia","Montenegro","Morocco","Mozambique","Myanmar (Burma)","Namibia","Nauru","Nepal","Netherlands","New Zealand","Nicaragua","Niger",
"Nigeria","North Macedonia","Norway","Oman","Pakistan","Palau","Panama","Papua New Guinea","Paraguay","Peru","Philippines","Poland","Portugal",
"Qatar","Romania","Russia","Rwanda","Saint Kitts and Nevis","Saint Lucia","Saint Vincent and the Grenadines","Samoa","San Marino","Sao Tome and Principe","Saudi Arabia",
"Senegal","Serbia","Seychelles","Sierra Leone","Singapore","Slovakia","Slovenia","Solomon Islands","Somalia","South Africa","Spain","Sri Lanka",
"Sudan","Suriname","Swaziland","Sweden","Switzerland","Syria","Taiwan","Tajikistan","Tanzania","Thailand","Togo","Tonga","Trinidad and Tobago","Tunisia",
"Turkey","Turkmenistan","Tuvalu","Uganda","Ukraine","United Arab Emirates","United Kingdom","United States","Uruguay","Uzbekistan","Vanuatu",
"Vatican City","Venezuela","Vietnam","Yemen","Zambia","Zimbabwe"]

Country=st.selectbox('Country you currently reside in*',country_names)
Current_city=st.text_input("Your current city*")

options = ['English','Hindi','Marathi','Malayalam','Kannada','Telgu','Assamese','Bengali','Gujarati','Manipuri','Tamil','Odia','Punjabi','Urdu','Maithili','Konkani','Kashmiri']
selected_options = st.multiselect("What communication languages are you comfortable in? * ", options)

comments=['Inspirational female role model for young women in STEM| You will\n share your personal & professional journey in STEM|\n Virtual engagement| 1.5 hours 1-2 times a year','Mentor|Help fellows advance their STEM skills through innovative & frugal\nhands-on projects|Virtual engagement|\n 3 hours per week for 12-14 weeks once a year','Tech Capstone Project/Research Project Developers| Design challenging hands on projects for fellows to elicit critical thinking| Virtual engagement |atleast 2-3 hours per week/1 month']
comments_a=st.selectbox("How would you like to join VigyanShaala's #SheforSTEM movement?*",comments)

option2 = st.radio("How many years have you worked as a STEM professional?*", ("2-3 years","4-6 years","7-10 years","More than 10 years"))
#Time=["Thursday | 3:00 - 4:30 PM IST","Friday | 3:00 - 4:30 PM IST","Saturday | 10:00 - 11:30 AM IST","Saturday | 3:00 - 4:30 PM IST","Saturday | 4:00 - 5:30 PM IST","Saturday | 6:00 - 7:30 PM IST"]
#session_times=st.multiselect("Do you have any preferred days and times for these sessions? Please select all that apply*",Time)
option_B = st.radio(" Would you like to schedule a 10-15 minute call with us for understanding the structure/content of your talk?*",("Yes","No","Maybe"))

#uploaded_file = st.file_uploader("Upload a file", type=["csv", "txt"])
uploaded_file1 = st.file_uploader(" Upload your Curriculum Vitae/Resume*", accept_multiple_files=False, type=["pdf", "txt"])
   
#uploaded_file = st.file_uploader("Upload a file", type=["csv", "txt"])
uploaded_file2 = st.file_uploader(" Please upload your bio and a professional headshot", accept_multiple_files=False, type=["pdf", "txt"])

if not Name or not Email_id or not Number or not Institute or not Degree or not Country or not Current_city or not selected_options or not comments_a or not option2 or not option_B or not uploaded_file1:
    st.error("Please fill in all the compulsory fields marked with * before proceeding.")
    st.stop()


#Create Data Frame for the inputs in the GUI's element

def create_feedback_dataframe(primary_key, Name, Email_id, Number, Profile, Institute, Current_job, Degree, Country, Current_city, selected_options, comments_a,option2,option_B,uploaded_file1,uploaded_file2):
    data = {
        'ID': primary_key,
        'Enter your full name *': Name,
        'Enter your email address *':Email_id ,
        "Enter your WhatsApp number (with country code, DONOT ADD '+') *":Number,
        'Enter your LinkedIn profile link here': Profile,
        'Enter your current Institute/University/Organization *':Institute,
        'Current Job title/Designation': Current_job ,
        'Highest degree obtained *':Degree ,
        'Country you currently reside in *': Country,
        'Your current city *':Current_city ,
        'What communication languages are you comfortable in?  *': selected_options,
        "How would you like to join VigyanShaala's #SheforSTEM movement?": comments_a,
        'How many years have you worked as a STEM professional? *': option2,
        #'Do you have any preferred days and times for these sessions? Pl': session_times,
        'Would you like to schedule a 10-15 minute call with us for unde': option_B,
        'Upload your Curriculum Vitae/Resume *': uploaded_file1.name if uploaded_file1 else None,  # Add file name or None if no file
        'Please upload your bio and a professional headshot': uploaded_file2.name if uploaded_file2 else None  # Same for second file
    }

    feedback_df = pd.DataFrame([data])
    return feedback_df


#Supabase Credential to store data to database 

url: str = 'https://twetkfnfqdtsozephdse.supabase.co'
key: str = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InR3ZXRrZm5mcWR0c296ZXBoZHNlIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MjE5Njk0MzcsImV4cCI6MjAzNzU0NTQzN30.D76H5RoTel0M7Wj6PTRSAXxxYGic7K25BSaeQDZqIN0'
# Create a Supabase client
supabase: Client = create_client(url, key, options=ClientOptions(
    postgrest_client_timeout=10,
    storage_client_timeout=10,
    schema="public",
  ))


combined_button_text = "Submit"   

#Button to push data to supabase 

if st.button(combined_button_text):
    feedback_df = create_feedback_dataframe(primary_key, Name, Email_id, Number, Profile, Institute, Current_job, Degree, Country, Current_city, selected_options, comments_a,option2,option_B,uploaded_file1,uploaded_file2)

    # Prepare the JSON data
    json_data = feedback_df[[ 'Enter your full name *', 'Enter your email address *',"Enter your WhatsApp number (with country code, DONOT ADD '+') *", 'Enter your LinkedIn profile link here', 'Enter your current Institute/University/Organization *','Current Job title/Designation','Highest degree obtained *','Country you currently reside in *','Your current city *','What communication languages are you comfortable in?  *',"How would you like to join VigyanShaala's #SheforSTEM movement?",'How many years have you worked as a STEM professional? *','Would you like to schedule a 10-15 minute call with us for unde','Upload your Curriculum Vitae/Resume *','Please upload your bio and a professional headshot','ID']].to_dict(orient='records')[0]

    table_name = "Recruitment"

    # Insert the JSON data into Supabase
    response_json = supabase.table(table_name).insert([json_data]).execute()

    st.write("Thankyou for your response")


    #Demo code to add the google drive API . Please give it a AWS backend connection. This gets stored in the trial folder get a different folders for storing different uploaded files.
    #####################
    #Define google drive API Scope here
    #SCOPES = ['https://www.googleapis.com/auth/drive.file']
    #PARENT_FOLDER_ID = "14OXiGuiaksXmeTigOtHHRtky7bU8dOpG"

    ## Function to upload a Pdf/text file to Google Drive

    #def upload_csv(uploaded_file):
        #try:
            # Get the current directory of the script
            #current_dir = os.path.dirname(os.path.abspath(__file__))
        
            # Path to the service account JSON file
            #json_file_path = os.path.join(current_dir, 'strong-jetty-435412-q0-a8ef3686d38f.json')

            ##Please add this json file obtained from google cloud console to the aws cloud , for now it it present on the supabase.

            # Load the credentials from the service account JSON file
            #creds = service_account.Credentials.from_service_account_file(
                #json_file_path,
                #scopes=SCOPES
            #)

            # Build the Drive service
            #service = build('drive', 'v3', credentials=creds)
        
            # Create a temporary file to save the uploaded file
            #with tempfile.NamedTemporaryFile(delete=False) as temp_file:
                #temp_file.write(uploaded_file.read())  # Save the uploaded file to the temp file
                #temp_file_path = temp_file.name  # Get the temp file path

                # Metadata for the file
                #file_metadata = {
                    #'name': uploaded_file.name,  # Use the uploaded file name
                    #'parents': ['your_parent_folder_id']  # The ID of the folder where the file will be uploaded
                #}

                # Upload the file with the appropriate MIME type
                #media = MediaFileUpload(temp_file_path, mimetype='text/csv', resumable=True)
                #file = service.files().create(
                    #body=file_metadata,
                    #media_body=media,
                    #fields='id'
                #).execute()

                # File uploaded successfully
                #st.success(f"CSV file uploaded successfully with ID: {file.get('id')}")

                # Clean up the temporary file after uploading
                #os.remove(temp_file_path)

        #except Exception as e:
            #st.error(f"An error occurred: {e}")

# Assuming uploaded_file is a file uploaded using Streamlit file uploader
# Call the upload function
    #upload_csv(uploaded_file)
    


    
   


    
