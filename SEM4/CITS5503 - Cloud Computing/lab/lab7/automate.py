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

 
