# DataDen

![Screenshot (42)](https://user-images.githubusercontent.com/68649921/170031097-3c750c43-6f8a-4b60-8c29-677490cb074f.png)

## Deployed website link:

Link to the deployed website: https://share.streamlit.io/smriti04501/dataden/main/app.py

**(IMPORTANT NOTE: This is the new link for the deployed website and the previous link (link given in the form) is not working due to authentication issues.)**

**PLEASE CLICK ON THE LINK ABOVE TO CHECKOUT THE WEBSITE**


## About the app:

*DataDen* is a holistic one-stop solution for automotive businesses to analyze customer & company data through intuitive statistical & graphical reports. This user-friendly application is designed for better comprehension of data which can further be used to:
- Improvise the business models
- Enhance customer experience 
- Take other major decisions to promote company growth

This web application has been developed as a submission for the month long mentorship program, **Microsoft Engage'22**.

## Features of the app:

- **Easy importation and exploration** of massive data (upto 200 MB csv files).
- **Displays interactive plots/graphs**, both univariate and multivariate for different features.
- **Report feature**- Generates the complete univariate data analysis report of data at once.
- **NOTEMAKER** - Mark observations or notedown anything else during app usage and download it.
- **Let's C about CARBON**- Check out the amount of CO2 emitted by a car by entering it's engine size.
- **Pan, zoom in or out, hover over the plots** to analyze them closely.
- **Save/Download** interactive plots and/or the complete data analysis report for viewing offline.
- Responsive, user-friendly and easy on the eye interface.


## How to run this app locally?

1. Clone this repository to your local machine.
2. Install all the libraries mentioned in the requirements.txt file with the command **pip install -r requirements.txt**
3. Open your terminal/command prompt from your project directory and run the file app.py by executing the command **streamlit run app.py**

## Video Demo:
https://youtu.be/QN9Z8-A0l7k

## App architecture and flow:

 Architecture            |  App flow
:-------------------------:|:-------------------------:
![Add a little bit of body text](https://user-images.githubusercontent.com/68649921/170649353-b9388cc6-cb30-44c1-bd58-8793ceea1a16.png) | ![Minimalist A4 Resume (1)](https://user-images.githubusercontent.com/68649921/170854949-bb7e9dcf-df74-4fcc-b762-68768d82a3c0.png)

## Project Approach & Overview:

**Week 1 (4th-8th May):-** Explored the problem statement and decided on the tech stack to be used.

**Week 2 (9th-14th May):** Worked on analyzing the dataset and created the basic environment to display univariate and multivariate plots, statistical insights and the 'Report' feature (that displays the complete univariate data analysis at once) for the application.

**Week 3 (15th-21st May):** Worked on the UI/UX of the application, made the application more responsive and added some additional static and functional features such as the Notetaker.

**Week 4 (22nd-27th May):** Worked on the *X factor feature (CO2 emissions in cars)* and improving the overall website. Deployed the website and created the video demonstration.

<br> 
<br> 

Analyze (Univariate/Multivariate)             |  NoteTaker
:-------------------------:|:-------------------------:
![Screenshot (50)](https://user-images.githubusercontent.com/68649921/170663225-81195813-d509-4554-b2b4-7ac228513cee.png) |  ![Screenshot (51)](https://user-images.githubusercontent.com/68649921/170664284-5f8cdca2-bb0a-4307-91f6-6ceada72da09.png)

 Report            |  Check CO2 emissions
:-------------------------:|:-------------------------:
![Screenshot (45)](https://user-images.githubusercontent.com/68649921/170662104-456363be-8393-49f0-8776-e19fa5c20b58.png) |  ![Screenshot (46)](https://user-images.githubusercontent.com/68649921/170662164-08e09bc5-3b07-4d10-a095-c9f136b8531b.png)

## Note:

The CO2 emission predictor in this app has been developed on data extracted from different sources and *some data may be hypotherical*. **The purpose here is to demonstrate the working of the model.** The same model when trained on real life data (actual data) will yield results compatible with real life scenarios. To train the model on real data (the new dataset must contain these 2 columns- Engine_size, CO2_emission):
- Open the python file 'machine_learning.py' and copy the code on the local system.
- Read the new data by pasting the file path of the new dataset in pd.read_csv()
- Run the file (the model will get trained on the new dataset)

## What's next for the app?

- The application should accept multiple file types other than csv (for eg: excel)
- Share feature for sharing the live visualization dashboards after the analysis with colleagues.
- Introduction of more variety of plot types for data analysis.
- Create a ML model that accepts car specifications such as the engine type, fuel type, mileage, body type and seating capacity to yield the most suitable car models.
- User Interface and User Experience improvements.
