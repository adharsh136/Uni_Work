<div style="display: flex; flex-direction: column; justify-content: center; align-items: center; height: 100vh;">

  <h2>Labs 6-9</h2>
  
  <p><b>Student ID:</b> 23796349</p>

  <p><b>Student Name:</b> Adharsh Sundaram Soudakar</p>

</div>
<div style="page-break-after: always;"></div>

# Lab 6

## Set up an EC2 instance

### [1] Create an EC2 micro instance with Ubuntu and SSH into it

* I used AWS CLI to create the EC2 instance required to complete this lab.
* The steps followed is the same steps that were done in `Lab 2`.
* The screenshots below show the commands and steps followed to create the EC2 instance and connect to it using `SSH`:

<img src="C:/Users/adhar/Desktop/sem4/CITS5503 - Cloud Computing/lab/lab6/lab6/lab6-1.png" alt="EC2" width="1920"/>

### [2] Install the Python 3 virtual environment package

* Before installing Python 3 virtual environment, the instance has to be updated and upgraded to the latest version.
* The following commands were used:

~~~bash
sudo apt-get update
sudo apt-get upgrade
~~~

* The screenshot below shows the output:

<img src="C:/Users/adhar/Desktop/sem4/CITS5503 - Cloud Computing/lab/lab6/lab6/lab6-2.png" alt="update&upgrade" width="1920"/>

* Then the following command can be used to install Python 3 virtual environment:

~~~bash
sudo apt-get install python3-venv
~~~

* The screenshot below shows the output:

<img src="C:/Users/adhar/Desktop/sem4/CITS5503 - Cloud Computing/lab/lab6/lab6/lab6-3.png" alt="venv" width="1920"/>

* Since we are going to run commands that require **su** access, it will be easier to persist the command line to be in **su** state for a while.
* This can be achieved with the following command:

~~~bash
sudo bash
~~~

### [3] Access a directory

* To create the required directories and traverse to that location, the following commands were used:

~~~bash
mkdir -p opt/wwc/mysites
cd opt/wwc/mysites
~~~

* The screenshot below shows the output:

<img src="C:/Users/adhar/Desktop/sem4/CITS5503 - Cloud Computing/lab/lab6/lab6/lab6-4.png" alt="mkdir" width="1920"/>

### [4] Set up a virtual environment

* To set up a virtual environment, the following command can be used:<br>
*NOTE*: Here we create a virtual environment called **myvenv**

~~~bash
python3 -m venv myvenv
~~~

* The screenshot below shows the output:

<img src="C:/Users/adhar/Desktop/sem4/CITS5503 - Cloud Computing/lab/lab6/lab6/lab6-5.png" alt="venv1" width="1249"/>

### [5] Activate the virtual environment

* The virtual environment (myvenv) can be activated using the following command:

~~~bash
source myvenv/bin/activate
~~~

* Now that we are inside the virtual environment, we can install **django** and create a project called **lab** using the following commands:

~~~bash
pip install django
django admin startproject lab
~~~

* Then we traverse into the project (lab) directory and create an app called **polls** using the following commands:

~~~bash
cd lab
python3 manage.py startapp polls
~~~

* The screenshot below shows the output of the above steps:

<img src="C:/Users/adhar/Desktop/sem4/CITS5503 - Cloud Computing/lab/lab6/lab6/lab6-6.png" alt="djangoset" width="1249"/>

* The screenshot below shows the files and content created after executing the `startproject` and `startapp` commands:

<img src="C:/Users/adhar/Desktop/sem4/CITS5503 - Cloud Computing/lab/lab6/lab6/lab6-7.png" alt="files&content" width="1249"/>

### [6] Install nginx

* To host our web app, we need a web server. Here, we plan to use **nginx**. It can be installed using the following command:

~~~bash
apt install nginx
~~~

* The screenshot below shows the installation output:

<img src="C:/Users/adhar/Desktop/sem4/CITS5503 - Cloud Computing/lab/lab6/lab6/lab6-8.png" alt="nginx" width="1920"/>

### [7] Configure nginx

* We need to configure nginx, specifying the port to listen to and how requests should be handled (forward requests to localhost on port 8000).

* The following code accomplishes the same:<br>
*NOTE*: This code was placed in the configuration file `default` located in the directory `/etc/nginx/sites-enabled/`

~~~nginx
server {
  listen 80 default_server;
  listen [::]:80 default_server;

  location / {
    proxy_set_header X-Forwarded-Host $host;
    proxy_set_header X-Real-IP $remote_addr;

    proxy_pass http://127.0.0.1:8000;
  }
}
~~~

* The screenshot below shows the changes made to the `default` file:

<img src="C:/Users/adhar/Desktop/sem4/CITS5503 - Cloud Computing/lab/lab6/lab6/lab6-9.png" alt="nginxconfig" width="1059"/>

### [8] Restart nginx

* We need to restart nginx to apply the changes made to the configuration file. This can be done using the following command:

~~~bash
service nginx restart
~~~

### [9] Access your EC2 instance

* To run our web application, use the following command:<br>
*NOTE*: This will start the Django development server on port **8000**.

~~~bash
python3 manage.py runserver 8000
~~~

* The screenshot below shows the output on the terminal when the above command was executed:

<img src="C:/Users/adhar/Desktop/sem4/CITS5503 - Cloud Computing/lab/lab6/lab6/lab6-11.png" alt="runserver" width="1252"/>

* To verify if this works correctly, we can enter the IP address of the created EC2 instance in a browser.
* The following screenshot shows the page that was displayed:

<img src="C:/Users/adhar/Desktop/sem4/CITS5503 - Cloud Computing/lab/lab6/lab6/lab6-10.png" alt="showserver" width="1323"/>

## Set up Django inside the created EC2 instance

### [1] Edit the following files (create them if non-existent)

* **Vim** text editor was used to edit all the three files.

* The file `views.py` in the directory `polls` was replaced with the following code:

~~~py
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world.")
~~~

* The file `urls.py` was created in the directory `polls` and the following code was added:

~~~py
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world.")
~~~

* The file `urls.py` in the directory `lab` was replaced with the following code:

~~~py
from django.urls import include, path
from django.contrib import admin

urlpatterns = [
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
]
~~~

### [2] Run the web server again

* The same command used in [Access your EC2 instance](#9-access-your-ec2-instance) was used again to start the Django web development server.
* The screenshot below shows the output:

<img src="C:/Users/adhar/Desktop/sem4/CITS5503 - Cloud Computing/lab/lab6/lab6/lab6-13.png" alt="showserver" width="1259"/>

### [3] Access the EC2 instance

* Use the URL:`http://<ip_add_of_your_EC2>/polls/` to see the HTTP Response in your browser screen.
* In my case the URL is `http://13.209.14.57/polls/`.
* The screenshot below shows the output that I got:

<img src="C:/Users/adhar/Desktop/sem4/CITS5503 - Cloud Computing/lab/lab6/lab6/lab6-12.png" alt="HttpResponse" width="1329"/>

## Set up an ALB

### [1] Create an application load balancer

To create the ALB, the code in **Lab 5** was reused:

*NOTE*: Refer to comments in the code to understand the implementation.

~~~py
import boto3

# Constants
#The created instance's ID
inst_ID = 'i-078581ec7b4427335'
#The security group created in previous lab (lab5), has both ssh and http permissions
sec_grp_id = 'sg-0ba69d87ee7933db6'
#The subnets 'a' and 'c' IDs (since my instance is a t2.micro machine)
SUBNETS = [ 'subnet-09f996d1ad81767a9', 'subnet-0b3601189181ee48e']
#The default VPC ID
VPC_ID = 'vpc-01f842220d0070f97'

#Initiating client for alb 
client = boto3.client('elbv2')

#Application Load Balancer
response = client.create_load_balancer(
   Name='23796349-ALB',
   Subnets=SUBNETS[:2],  
   SecurityGroups=[sec_grp_id],
   Scheme='internet-facing',
   Tags=[
       {
           'Key': 'Name',
           'Value': '23796349-ALB'
       },
   ]
)
lb_arn = response['LoadBalancers'][0]['LoadBalancerArn']
print(f"Load Balancer ARN: {lb_arn}")
 
#Target group
response = client.create_target_group(
   Name='23796349-TG',
   Protocol='HTTP',
   Port=80,
   HealthCheckPath='/polls/', #Specifying polls as the path for heath check
   VpcId=VPC_ID,
   Tags=[
       {
           'Key': 'Name',
           'Value': '23796349-TG'
       },
   ]
)
tg_arn = response['TargetGroups'][0]['TargetGroupArn']
print(f"Target Group ARN: {tg_arn}")
 
#Register the created instance as a target in the target group
client.register_targets(
   TargetGroupArn=tg_arn,
   Targets=[
       {'Id': inst_ID},
   ]
)

#Listener with HTTP and Port 80 forwarding
client.create_listener(
   LoadBalancerArn=lb_arn,
   Protocol='HTTP',
   Port=80,
   DefaultActions=[
       {
           'Type': 'forward',
           'TargetGroupArn': tg_arn
       },
   ]
)
 
print("Application Load Balancer and listener successfully created. The instance was registered as a target")
~~~

* The screenshots below show the ALB that was created:

<img src="C:/Users/adhar/Desktop/sem4/CITS5503 - Cloud Computing/lab/lab6/lab6/lab6-14.png" alt="ALB" width="1259"/>

<img src="C:/Users/adhar/Desktop/sem4/CITS5503 - Cloud Computing/lab/lab6/lab6-1w.png" alt="ALB1" width="1877"/>

### [2] Health check

* By default health checks are fetched every 30 seconds.
* The screenshot below shows the Target group that was created and its health check settings:

<img src="C:/Users/adhar/Desktop/sem4/CITS5503 - Cloud Computing/lab/lab6/lab6-2w.png" alt="TG" width="1878"/>

### [3] Access

* To see if the ALB is working as intended, access the URL: `http://<alb_dns_name>/polls/`. In my case, it is `http://23796349-alb-1538659132.ap-northeast-w.elb.amazonaws.com/polls/`.
* The screenshot below shows the output that I got:

<img src="C:/Users/adhar/Desktop/sem4/CITS5503 - Cloud Computing/lab/lab6/lab6-3w.png" alt="ALBcheck" width="1919"/>

<br>

**All resources that were created for the lab (*EC2 instance, ALB and TG*) were deleted using the AWS Console after the lab completion.**

---
<div style="page-break-after: always;"></div>

# Lab 7

### Create an EC2 instance

* The EC2 instance required for this lab was created using the same methods used in `Lab 6` ([Refer here](#1-create-an-ec2-micro-instance-with-ubuntu-and-ssh-into-it)).

### Install and configure Fabric

* The following command can be used to install `fabric`:

~~~bash
pip install fabric
~~~

* The screenshot below shows the output of the command:

<img src="C:/Users/adhar/Desktop/sem4/CITS5503 - Cloud Computing/lab/lab7/lab7-1.png" alt="fabricinst" width="1248"/>

* Once `fabric` is installed, we need to configure it. We can do this by creating a **config** file in the `~/.ssh` folder.
* The following content was added to the config file:

~~~fabric
Host <your EC2 instance name>
    Hostname <your EC2 instance public IPv4 DNS>
    User ubuntu
    UserKnownHostsFile /dev/null
    StrictHostKeyChecking no
    PasswordAuthentication no
    IdentityFile <path to your private key>
~~~

* The following screenshot shows the content that I added to my config file:<br>
*NOTE: I copied my private key to the `~/.ssh` folder. Hence I haven't specified path for the same. Also I replaced the placeholders with the appropriate content.*

<img src="C:/Users/adhar/Desktop/sem4/CITS5503 - Cloud Computing/lab/lab7/lab7-5.png" alt="fabriccon" width="1250"/>

* To see if fabric has been configured the right way, connect to your instance using the following code:

~~~py
python3
>>> from fabric import Connection
>>> c = Connection('<your EC2 instance name>')
>>> result = c.run('uname -s')
Linux
>>>
~~~

* The screenshot below shows my attempt to connect to my instance:

<img src="C:/Users/adhar/Desktop/sem4/CITS5503 - Cloud Computing/lab/lab7/lab7-2.png" alt="fabriccon" width="1248"/>

### Use Fabric for automation

* The entirety of `Lab 6` steps in [Set up an EC2 instance](#set-up-an-ec2-instance) and [Set up Django inside the created EC2 instance](#set-up-django-inside-the-created-ec2-instance) has been automated with the following code:<br><br>
Code referenced from [Fabric documention](https://docs.fabfile.org/en/2.0/).<br><br>
*NOTE:<br>Refer to comments in the code to understand the implementation.<br>Note the usage of `run` and `sudo` functions, wherever **su** permissions were required `sudo` was used.<br>Appropriate number of `\` were used to escape special characters.<br>Full path to a file was always used.*

~~~py
from fabric import Connection, task
 
def automate_setup_and_run():

    with Connection('23796349-vm') as c:

        print('----------------------------------------')
        print('+----Installing necessary things-------+')
        print('----------------------------------------')

        # Installing python3 virtual environment and nginx
        c.sudo("apt update")
        c.sudo("apt upgrade -y")
        c.sudo("apt install python3-pip -y")
        c.sudo("apt install python3-venv -y")
        c.sudo("apt install nginx -y")
        
        print('-------------------------------------------')
        print('+----Setting up Virtual Environment-------+')
        print('-------------------------------------------')

        # Setup virtual environment
        c.run("python3 -m venv myvenv")
        c.run("source myvenv/bin/activate")

        print('------------------------------')
        print('+----Installing django-------+')
        print('------------------------------')
      
        # Installing Django within the virtual environment
        c.sudo("pip install django")
      
        print('------------------------------')
        print('+----Setting up django-------+')
        print('------------------------------')

        # Setting up Django project
        c.run("django-admin startproject lab")
        
        print('-------------------------------')
        print('+----Creating polls app-------+')
        print('-------------------------------')

        # Changing directory and creating polls app
        c.run("cd lab && python3 manage.py startapp polls")
        
        print('------------------------------')
        print('+----Configuring nginx-------+')
        print('------------------------------')

        # Configure nginx
        c.run("echo 'server {\n    listen 80 default_server;\n    listen [::]:80 default_server;\n\n    location / {\n        proxy_set_header X-Forwarded-Host $host;\n        proxy_set_header X-Real-IP $remote_addr;\n        proxy_pass http://127.0.0.1:8000;\n    }\n}' | sudo tee /etc/nginx/sites-enabled/default")
        c.sudo("nginx -t")
        c.sudo("service nginx restart")
        
        print('-----------------------------------')
        print('+----Editing polls/views.py-------+')
        print('-----------------------------------')

        # Edit /polls/views.py
        c.run("echo 'from django.http import HttpResponse\n\ndef index(request):\n    return HttpResponse(\"Hello, world.\")' | sudo tee /home/ubuntu/lab/polls/views.py")
        
        print('----------------------------------')
        print('+----Editing polls/urls.py-------+')
        print('----------------------------------')

        # Edit /polls/urls.py
        c.run("echo 'from django.urls import path\nfrom . import views\n\nurlpatterns = [\n    path(\"\", views.index, name=\"index\"),\n]' | sudo tee /home/ubuntu/lab/polls/urls.py")
        
        print('--------------------------------')
        print('+----Editing lab/urls.py-------+')
        print('--------------------------------')

        # Edit /lab/urls.py
        c.run("echo 'from django.urls import include, path\nfrom django.contrib import admin\n\nurlpatterns = [\n    path(\"polls/\", include(\"polls.urls\")),\n    path(\"admin/\", admin.site.urls),\n]' | sudo tee /home/ubuntu/lab/lab/urls.py")
        
        print('---------------------------------------')
        print('+----Starting Development Server------+')
        print('---------------------------------------')

        # Starting development server
        c.run("cd lab && python3 manage.py runserver 0.0.0.0:8000 &")
 
if __name__ == "__main__":
    automate_setup_and_run()
~~~

* The screenshot below shows the end result (*web development server on port 8000*) of the code execution:

<img src="C:/Users/adhar/Desktop/sem4/CITS5503 - Cloud Computing/lab/lab7/lab7-3.png" alt="code_exe" width="1255"/>

* The screenshot below shows the output when the *IP address of my EC2 instance is accessed through a web browser*:

<img src="C:/Users/adhar/Desktop/sem4/CITS5503 - Cloud Computing/lab/lab7/lab7-4.png" alt="IP" width="1328"/>

<br>

**All resources that were created for the lab (*EC2 instance*) were deleted using the AWS Console after the lab completion.**

---
<div style="page-break-after: always;"></div>

# Lab 8

## Install and run jupyter notebooks

* To install **Jupyter Notebook**, use the following command:

~~~bash
pip install notebook
~~~

* The screenshot below shows the output of the command:

<img src="C:/Users/adhar/Desktop/sem4/CITS5503 - Cloud Computing/lab/lab8/lab8/lab8-1.png" alt="ntins" width="788"/>

* To run Jupyter Notebook, use the following command:

~~~bash
jupyter notebook
~~~

* The screenshot below shows the command execution and its output:

<img src="C:/Users/adhar/Desktop/sem4/CITS5503 - Cloud Computing/lab/lab8/lab8/lab8-2.png" alt="ntrun" width="1843"/>

## Install ipykernel

* To install **ipykernel**, use the following command:

~~~bash
pip install ipykernel
~~~

* The screenshot below shows the output of the command:

<img src="C:/Users/adhar/Desktop/sem4/CITS5503 - Cloud Computing/lab/lab8/lab8/lab8-3.png" alt="pyker" width="1405"/>

## Run hyperparameter tuning jobs

* I first downloaded the [LabAI.ipynb](https://github.com/zhangzhics/CITS5503_Sem2/blob/master/Labs/src/LabAI.ipynb).
* Then, I opened the file using Jupyter Notebook.
* I followed the instructions in the notebook.
* One of the instructions, asks us to create a S3 bucket and create appropriate objects(folders) in the same.
* I used the code below to create the bucket, which is a modified version of **Lab 3** code:

~~~py
import boto3

#Bucket configuration
name = '23796349-lab8' #The name that was recommended in the notebook
bucket_config = {'LocationConstraint': 'ap-northeast-2'} #My specified region

#S3 client
s3 = boto3.client("s3")

try:
    s3.create_bucket(Bucket=name,CreateBucketConfiguration=bucket_config) #create_bucket function is idempotent.
    response = s3.head_bucket(Bucket=name)
    print(f"Bucket '{name}' created and exists.")
    print(response)
except Exception as error:
    pass

~~~

* The screenshot below shows the created S3 bucket:

<img src="C:/Users/adhar/Desktop/sem4/CITS5503 - Cloud Computing/lab/lab8/lab8-1w.png" alt="bucket" width="1877"/>

* Then, I used AWS Console to create the required objects (**folders - sagemaker/23796349-hpo-xgboost-dm**) in my S3 Bucket.
* The screenshot below shows the objects (folders) created using AWS Console:

<img src="C:/Users/adhar/Desktop/sem4/CITS5503 - Cloud Computing/lab/lab8/lab8-3w.png" alt="objects" width="1876"/>

* I made the necessary changes to the variables as instructed by the comments in the notebook. The screenhot below shows the changes I made:

<img src="C:/Users/adhar/Desktop/sem4/CITS5503 - Cloud Computing/lab/lab8/lab8/lab8-5.png" alt="varchnge" width="1212"/>

* I ran all the code blocks and the output of the **final code block** is shown in the screenshot below:

<img src="C:/Users/adhar/Desktop/sem4/CITS5503 - Cloud Computing/lab/lab8/lab8/lab8-6.png" alt="finalcode" width="1212"/>

* The execution of all the code blocks and the final block resulted in the creation of objects(folders and files) in the bucket. This is the result of training the model and validating it.

* The screenshot below shows the content in the folder **23796349-hpo-xgboost-dm**:

<img src="C:/Users/adhar/Desktop/sem4/CITS5503 - Cloud Computing/lab/lab8/lab8-4w.png" alt="2folder" width="1877"/>

* The screenshot below shows the content in the folders **train** and **validation**:

<img src="C:/Users/adhar/Desktop/sem4/CITS5503 - Cloud Computing/lab/lab8/lab8-5w.png" alt="trainvalid" width="1878"/>

* The screenshot below shows the **Hyperparameter Tuning Jobs**:

<img src="C:/Users/adhar/Desktop/sem4/CITS5503 - Cloud Computing/lab/lab8/lab8-6w.png" alt="hyp1" width="1877"/>

*NOTE: <br>I encountered the Non-numeric type error, that is why you could see more than one hyperparameter tuning jobs.<br>To solve this problem, I converted the Non-numeric data to Numeric data (True/False to 1/0 respectively).<br><br>**The screenshot below shows the code block that contains the code to convert Non-numeric data to Numeric data before uploading to the S3 bucket:***

<img src="C:/Users/adhar/Desktop/sem4/CITS5503 - Cloud Computing/lab/lab8/lab8/lab8-7.png" alt="codeblock" width="1212"/>

~~~py
#Converting True/False to 1/0 respectively

#train data
train_df = pd.read_csv('train.csv', header=None)
train_df = train_df.astype(int)
train_df.to_csv('train.csv', index=False, header=False)

#validation data
valid_df = pd.read_csv('validation.csv', header=None)
valid_df = valid_df.astype(int)
valid_df.to_csv('validation.csv', index=False, header=False)
~~~

* The screenshot below shows the details (the associated training jobs) of **Successful Tunning job**:

<img src="C:/Users/adhar/Desktop/sem4/CITS5503 - Cloud Computing/lab/lab8/lab8-7w.png" alt="hyp2" width="1878"/>

* The screenshot below shows the contents of the **output** folder:

<img src="C:/Users/adhar/Desktop/sem4/CITS5503 - Cloud Computing/lab/lab8/lab8-8w.png" alt="o/p" width="1877"/>

* The screenshot below shows the **models** created:

<img src="C:/Users/adhar/Desktop/sem4/CITS5503 - Cloud Computing/lab/lab8/lab8-9w.png" alt="models" width="1917"/>

* I have linked my Jupyter Notebook [here](https://uniwa-my.sharepoint.com/:u:/g/personal/23796349_student_uwa_edu_au/EdopF5oudNNMmqWQVyyZCKcBroiHeJGa3dmVYp2AJwnBdQ?e=cdQfQt).

**All resources that were created for the lab (*S3 Bucket and the objects in it*) were deleted using the AWS Console after the lab completion.**

---
<div style="page-break-after: always;"></div>

# Lab 9

## AWS Comprehend

### Detect Languages from text

#### [1] Modify the code above

* The code given in the lab sheet was modified to display output in the specified format.

~~~py
import boto3
import langcodes

#Sample
sentence = "Hi my name is John. Nice to meet you!"

client = boto3.client('comprehend')
response = client.detect_dominant_language(Text=sentence)
lng_code = response['Languages'][0]['LanguageCode']
score = response['Languages'][0]['Score']
lng_detected = langcodes.get(lng_code).language_name()
print(f"For the sentence:\n\"{sentence}\"\n")
print("Detection")
print("---------")
print(f"{lng_detected} detected with {int(score*100)}% confidence!")
~~~

* To do this, I had to change the *Language Code* returned by the [*detect_dominant_language*](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/comprehend/client/detect_dominant_language.html) method to the respective full form (eg. "en" should be converted to "English").
* I searched and found that there is a python library called [langcodes](https://pypi.org/project/langcodes/) that returns the full language name given a language code.
* I used the following command to install the library:

~~~bash
pip install langcodes
~~~

* The screenshot below shows the output of the **modified code**:

<img src="C:/Users/adhar/Desktop/sem4/CITS5503 - Cloud Computing/lab/lab9/2.png" alt="modify" width="1598"/>

#### [2] Test your code with other languages

* The next task was to test the modified code with other lanuages.
* I created a list that contains the text provided in the Lab sheet as its elements.
* The code below shows my implementation:

~~~py
import boto3
import langcodes

#Sample
#sentence = "Hi my name is John. Nice to meet you!"

#Test text provided in Lab Sheet
test = ["The French Revolution was a period of social and political upheaval in France and its colonies beginning in 1789 and ending in 1799.",
        "El Quijote es la obra más conocida de Miguel de Cervantes Saavedra. Publicada su primera parte con el título de El ingenioso hidalgo don Quijote de la Mancha a comienzos de 1605, es una de las obras más destacadas de la literatura española y la literatura universal, y una de las más traducidas. En 1615 aparecería la segunda parte del Quijote de Cervantes con el título de El ingenioso caballero don Quijote de la Mancha.",
        "Moi je n'étais rien Et voilà qu'aujourd'hui Je suis le gardien Du sommeil de ses nuits Je l'aime à mourir Vous pouvez détruire Tout ce qu'il vous plaira Elle n'a qu'à ouvrir L'espace de ses bras Pour tout reconstruire Pour tout reconstruire Je l'aime à mourir",
        "L'amor che move il sole e l'altre stelle."]

for sentence in test:
    client = boto3.client('comprehend')
    response = client.detect_dominant_language(Text=sentence)
    lng_code = response['Languages'][0]['LanguageCode']
    score = response['Languages'][0]['Score']
    lng_detected = langcodes.get(lng_code).language_name()
    print(f"For the sentence:\n\"{sentence}\"\n")
    print("Detection")
    print("---------")
    print(f"{lng_detected} detected with {int(score*100)}% confidence!")
    print("\n")
~~~

* The screenshot below shows the **ouput**:

<img src="C:/Users/adhar/Desktop/sem4/CITS5503 - Cloud Computing/lab/lab9/3.png" alt="modify1" width="1598"/>

***NOTE**: I used the **detect_dominant_language** method to get and feed the appropriate language code in the following sections.*

### Analyze sentiment

* The following code shows the implementation of the [*detect_sentiment*](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/comprehend/client/detect_sentiment.html) method to return the sentiment of a given sentence.

~~~py
import boto3

#Test provided in Lab Sheet
test = ["The French Revolution was a period of social and political upheaval in France and its colonies beginning in 1789 and ending in 1799.",
        "El Quijote es la obra más conocida de Miguel de Cervantes Saavedra. Publicada su primera parte con el título de El ingenioso hidalgo don Quijote de la Mancha a comienzos de 1605, es una de las obras más destacadas de la literatura española y la literatura universal, y una de las más traducidas. En 1615 aparecería la segunda parte del Quijote de Cervantes con el título de El ingenioso caballero don Quijote de la Mancha.",
        "Moi je n'étais rien Et voilà qu'aujourd'hui Je suis le gardien Du sommeil de ses nuits Je l'aime à mourir Vous pouvez détruire Tout ce qu'il vous plaira Elle n'a qu'à ouvrir L'espace de ses bras Pour tout reconstruire Pour tout reconstruire Je l'aime à mourir",
        "L'amor che move il sole e l'altre stelle."]

for sentence in test:
    client = boto3.client('comprehend')
    response_lng = client.detect_dominant_language(Text=sentence)
    lng_code = response_lng['Languages'][0]['LanguageCode']
    response_sent = client.detect_sentiment(Text=sentence, LanguageCode=lng_code)
    sentiment = response_sent['Sentiment']
    score = response_sent['SentimentScore'][sentiment.capitalize()]
    print(f"For \"{sentence}\"\n\nThe sentiment detected is {sentiment.capitalize()} with {int(score*100)}% confidence!")
    print("\n")
~~~

* The screenshot below shows the **output**:

<img src="C:/Users/adhar/Desktop/sem4/CITS5503 - Cloud Computing/lab/lab9/4.png" alt="sent" width="1260"/>

### Detect entities

* The following code shows the implementation of [*detect_entities*](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/comprehend/client/detect_entities.html) method to return the entities found in a given sentence.

~~~py
import boto3

#Test provided in Lab Sheet
test = ["The French Revolution was a period of social and political upheaval in France and its colonies beginning in 1789 and ending in 1799.",
        "El Quijote es la obra más conocida de Miguel de Cervantes Saavedra. Publicada su primera parte con el título de El ingenioso hidalgo don Quijote de la Mancha a comienzos de 1605, es una de las obras más destacadas de la literatura española y la literatura universal, y una de las más traducidas. En 1615 aparecería la segunda parte del Quijote de Cervantes con el título de El ingenioso caballero don Quijote de la Mancha.",
        "Moi je n'étais rien Et voilà qu'aujourd'hui Je suis le gardien Du sommeil de ses nuits Je l'aime à mourir Vous pouvez détruire Tout ce qu'il vous plaira Elle n'a qu'à ouvrir L'espace de ses bras Pour tout reconstruire Pour tout reconstruire Je l'aime à mourir",
        "L'amor che move il sole e l'altre stelle."]

for sentence in test:
    client = boto3.client('comprehend')
    response_lng = client.detect_dominant_language(Text=sentence)
    lng_code = response_lng['Languages'][0]['LanguageCode']
    reponse_ent = client.detect_entities(Text=sentence, LanguageCode=lng_code)
    entities = reponse_ent['Entities']
    print(f"In the sentence:\n\"{sentence}\"\n")
    print("Detection")
    print("---------")
    if len(entities) != 0:
        for entity in entities:
            print(f"Entity: {entity['Text']} | Type: {entity['Type']} | Confidence: {int(entity['Score']*100)}%")
    else:
        print("None")
    print("\n")
~~~

* The screenshot below shows the **output**:

<img src="C:/Users/adhar/Desktop/sem4/CITS5503 - Cloud Computing/lab/lab9/5.png" alt="ent" width="1598"/>

* **Answer to lab sheet question**: Entities can be described as specific pieces of information that are found and categorized in a given text. (eg. Location, Dates, Events, People, etc.)

### Detect keyphrases

* The following code shows the implementation of [*detect_key_phrases*](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/comprehend/client/detect_key_phrases.html) method to return the keyphrases found in a given sentence.

~~~py
import boto3

#Test provided in Lab Sheet
test = ["The French Revolution was a period of social and political upheaval in France and its colonies beginning in 1789 and ending in 1799.",
        "El Quijote es la obra más conocida de Miguel de Cervantes Saavedra. Publicada su primera parte con el título de El ingenioso hidalgo don Quijote de la Mancha a comienzos de 1605, es una de las obras más destacadas de la literatura española y la literatura universal, y una de las más traducidas. En 1615 aparecería la segunda parte del Quijote de Cervantes con el título de El ingenioso caballero don Quijote de la Mancha.",
        "Moi je n'étais rien Et voilà qu'aujourd'hui Je suis le gardien Du sommeil de ses nuits Je l'aime à mourir Vous pouvez détruire Tout ce qu'il vous plaira Elle n'a qu'à ouvrir L'espace de ses bras Pour tout reconstruire Pour tout reconstruire Je l'aime à mourir",
        "L'amor che move il sole e l'altre stelle."]

for sentence in test:
    client = boto3.client('comprehend')
    response_lng = client.detect_dominant_language(Text=sentence)
    lng_code = response_lng['Languages'][0]['LanguageCode']
    response_kpd = client.detect_key_phrases(Text=sentence, LanguageCode=lng_code)
    keyPhrases = response_kpd['KeyPhrases']
    print(f"In the sentence:\n\"{sentence}\"\n")
    print("Detection")
    print("---------")
    for kp in keyPhrases:
        print(f"Keyphrase: {kp['Text']} | Confidence: {int(kp['Score']*100)}%")
    print("\n")
~~~

* The screenshots below show the **output**:

<img src="C:/Users/adhar/Desktop/sem4/CITS5503 - Cloud Computing/lab/lab9/6.png" alt="kp" width="1598"/><br>
<img src="C:/Users/adhar/Desktop/sem4/CITS5503 - Cloud Computing/lab/lab9/6a.png" alt="kp1" width="1598"/>

* **Answer to lab sheet question**: Keyphrases can be described as crucial expressions that give the main idea of a given text.

### Detect syntaxes

* The following code shows the implementation of [*detect_syntax*](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/comprehend/client/detect_syntax.html) method to return the syntaxes found in a given sentence.

~~~py
import boto3

#Test provided in Lab Sheet
test = ["The French Revolution was a period of social and political upheaval in France and its colonies beginning in 1789 and ending in 1799.",
        "El Quijote es la obra más conocida de Miguel de Cervantes Saavedra. Publicada su primera parte con el título de El ingenioso hidalgo don Quijote de la Mancha a comienzos de 1605, es una de las obras más destacadas de la literatura española y la literatura universal, y una de las más traducidas. En 1615 aparecería la segunda parte del Quijote de Cervantes con el título de El ingenioso caballero don Quijote de la Mancha.",
        "Moi je n'étais rien Et voilà qu'aujourd'hui Je suis le gardien Du sommeil de ses nuits Je l'aime à mourir Vous pouvez détruire Tout ce qu'il vous plaira Elle n'a qu'à ouvrir L'espace de ses bras Pour tout reconstruire Pour tout reconstruire Je l'aime à mourir",
        "L'amor che move il sole e l'altre stelle."]

for sentence in test:
    client = boto3.client('comprehend')
    response_lng = client.detect_dominant_language(Text=sentence)
    lng_code = response_lng['Languages'][0]['LanguageCode']
    response_syntx = client.detect_syntax(Text=sentence, LanguageCode=lng_code)
    syntxTokens = response_syntx['SyntaxTokens']
    print(f"In the sentence:\n\"{sentence}\"\n")
    print("Detection")
    print("---------")
    for tk in syntxTokens:
        print(f"Word: {tk['Text']} | Part of Speech: {tk['PartOfSpeech']['Tag']} | Confidence: {int(tk['PartOfSpeech']['Score']*100)}%")
    print("\n")
~~~

* The screenshots below show the **output**:

<img src="C:/Users/adhar/Desktop/sem4/CITS5503 - Cloud Computing/lab/lab9/7.png" alt="syn" width="1596"/><br>
<img src="C:/Users/adhar/Desktop/sem4/CITS5503 - Cloud Computing/lab/lab9/7a.png" alt="syn1" width="1596"/><br>
<img src="C:/Users/adhar/Desktop/sem4/CITS5503 - Cloud Computing/lab/lab9/7b.png" alt="syn2" width="1596"/><br>
<img src="C:/Users/adhar/Desktop/sem4/CITS5503 - Cloud Computing/lab/lab9/7c.png" alt="syn3" width="1596"/>

* **Answer to lab sheet question**: Syntaxes can be described as each individual word in a given text that can be used to identify the grammatical structure of the sentences in the text.

## AWS Rekognition

### Add images

* First, I downloaded the required images to complete the task in this section.
* These are the images that I chose.
* The image **urban.jpg**:

<img src="C:/Users/adhar/Desktop/sem4/CITS5503 - Cloud Computing/lab/lab9/urban.jpg" alt="urban" width="2592"/>

* The image **beach.jpg**:

<img src="C:/Users/adhar/Desktop/sem4/CITS5503 - Cloud Computing/lab/lab9/beach.jpg" alt="beach" width="1280"/>

* The image **faces.jpg**:

<img src="C:/Users/adhar/Desktop/sem4/CITS5503 - Cloud Computing/lab/lab9/faces.jpg" alt="faces" width="1300"/>

* The image **text.jpg**:

<img src="C:/Users/adhar/Desktop/sem4/CITS5503 - Cloud Computing/lab/lab9/text.jpg" alt="text" width="283"/>

* The following code creates a S3 bucket named **23796349-lab9** in the region that I am mapped to (ap-notheast-2) and uploads the four images, it is a modification of code from `Lab 5`:

~~~py
import boto3
import os

#Bucket configuration
name = '23796349-lab9'
bucket_config = {'LocationConstraint': 'ap-northeast-2'} 

#S3 client
s3 = boto3.client("s3")

#File paths
file_paths = [
    '/home/cits5503/lab9/beach.jpg',
    '/home/cits5503/lab9/faces.jpg',
    '/home/cits5503/lab9/urban.jpg',
    '/home/cits5503/lab9/text.jpg'
]

try:
    s3.create_bucket(Bucket=name,CreateBucketConfiguration=bucket_config) #create_bucket function is idempotent.
    response = s3.head_bucket(Bucket=name)
    print(f"Bucket '{name}' created and exists.")
    print(response)
except Exception as error:
    pass

for file_path in file_paths:
    file_name = os.path.basename(file_path)
    s3.upload_file(file_path, bucket_name, file_name)
    print(f'Uploaded {file_name} to {bucket_name}')
~~~

### Test AWS rekognition

* The code below shows the implementation of [detect_labels](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_DetectLabels.html), [detect_moderation_labels](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_DetectModerationLabels.html), [detect_faces](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_DetectFaces.html), and [detect_text](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_DetectText.html) methods to return appropriate labels and their confidence level.
* I used argument parser to have the choice to run only the required method.
* The user has to specify two options, the method they want to use and the photo they want to use that is present in their S3 bucket.

~~~py
import boto3,argparse

#Constants
bucket = '23796349-lab9'
client = boto3.client('rekognition')

# Argument Parsing
parser = argparse.ArgumentParser(description='AWS_Rekognition_options')
parser.add_argument('--labelrecog', '-l', action='store_true', help='Label Recognition')
parser.add_argument('--imgmoderation', '-i', action='store_true', help='Image Moderation')
parser.add_argument('--faceanalyse', '-f', action='store_true', help='Facial Analysis')
parser.add_argument('--exttxt', '-e', action='store_true', help='Extract Text')
parser.add_argument('--photo', '-p', required=True, help='Photo name with extension present in your S3 bucket')
args = parser.parse_args()

#Label Recognition
def detectLabels(photo_name):
    reponse = client.detect_labels(Image={'S3Object':{'Bucket':bucket,'Name':photo_name}})
    print("Detection")
    print("---------")
    for label in reponse['Labels']:
        print(f"Label: {label['Name']} | Confidence: {int(label['Confidence'])}%")

#Image Moderation
def imgMod(photo_name):
    reponse = client.detect_moderation_labels(Image={'S3Object':{'Bucket':bucket,'Name':photo_name}})
    print("Detection")
    print("---------")
    for label in reponse['ModerationLabels']:
        print(f"Label: {label['Name']} | Confidence: {int(label['Confidence'])}%")

#Facial Analysis
def analyFace(photo_name):
    response = client.detect_faces(Image={'S3Object':{'Bucket':bucket,'Name':photo_name}}, Attributes=['ALL'])
    faceCount = 0
    for face in response['FaceDetails']:
        faceCount+=1
        print("Face Number: "+ str(faceCount))
        print("Detection")
        print("---------")
        print("Gender: "+face['Gender']['Value']+" | Confidence: "+str(int(face['Gender']['Confidence']))+"%")
        print("Age Range (years): "+str(face['AgeRange']['Low'])+" to "+str(face['AgeRange']['High']))
        print("Glasses: "+str(face['Eyeglasses']['Value'])+" | Confidence: "+str(int(face['Eyeglasses']['Confidence']))+"%")
        print("------------------------------------------------------------------------------")

#Extract Text
def extText(photo_name):
    response = client.detect_text(Image={'S3Object':{'Bucket':bucket,'Name':photo_name}})
    print("Detection")
    print("---------")
    for text in response['TextDetections']:
        print(f"Text detected: {text['DetectedText']} | Confidence: {int(text['Confidence'])}%")

#Calling appropriate function based on the option specified
if args.labelrecog:
    detectLabels(args.photo)

if args.imgmoderation:
    imgMod(args.photo)

if args.faceanalyse:
    analyFace(args.photo)

if args.exttxt:
    extText(args.photo)
~~~

* The screenshot below shows the output of **Label Recognition**:

<img src="C:/Users/adhar/Desktop/sem4/CITS5503 - Cloud Computing/lab/lab9/8.png" alt="lbl" width="1596"/>

* The screenshot below shows the output of **Image Moderation**:

<img src="C:/Users/adhar/Desktop/sem4/CITS5503 - Cloud Computing/lab/lab9/9.png" alt="imgm" width="1596"/>

* The screenshot below shows the output of **Facial Analysis**:

<img src="C:/Users/adhar/Desktop/sem4/CITS5503 - Cloud Computing/lab/lab9/10.png" alt="fa" width="1596"/>

* The screenshot below shows the output of **Extract Text**:

<img src="C:/Users/adhar/Desktop/sem4/CITS5503 - Cloud Computing/lab/lab9/11.png" alt="et" width="1596"/>

**All resources that were created for the lab (*S3 Bucket and the objects in it*) were deleted using the AWS Console after the lab completion.**

---
<div style="page-break-after: always;"></div>
