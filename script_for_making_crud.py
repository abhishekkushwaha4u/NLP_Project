from script_for_starting_project import add_url_to_urlpatterns
import os
def making_create_route(cwd, project_name, app_name, model, endpoint):
    template = "\nclass {}CreateAPIView(CreateAPIView):\n\tqueryset = {}.objects.all()\n\tserializer_class = {}Serializer\n\n".format(model, model, model)
    with open(os.path.join(cwd, project_name, app_name, 'views.py'), 'r') as e:
        views = e.read()
    views = views + template
    with open(os.path.join(cwd, project_name, app_name, 'views.py'), 'w') as e:
        e.write(views)
        print("Successfully added create view!!")
    
    add_url_to_urlpatterns(os.path.join(cwd, project_name, app_name, 'urls.py'), '\tpath("{}/", {}CreateAPIView.as_view()),'.format(endpoint, model))
    print("Added url to path for the view!")





def making_update_route(cwd, project_name, app_name, model, endpoint):
    template = "\nclass {}UpdateAPIView(UpdateAPIView):\n\tqueryset = {}.objects.all()\n\tserializer_class = {}Serializer\n\n".format(model, model, model)
    with open(os.path.join(cwd, project_name, app_name, 'views.py'), 'r') as e:
        views = e.read()
    views = views + template
    with open(os.path.join(cwd, project_name, app_name, 'views.py'), 'w') as e:
        e.write(views)
        print("Successfully added update view!!")
    
    add_url_to_urlpatterns(os.path.join(cwd, project_name, app_name, 'urls.py'), '\tpath("{}/<id>/", {}UpdateAPIView.as_view()),'.format(endpoint, model))
    print("Added url to path for the view!")


def making_read_route(cwd, project_name, app_name, model, endpoint):
    template = "\nclass {}RetrieveAPIView(RetrieveAPIView):\n\tqueryset = {}.objects.all()\n\tserializer_class = {}Serializer\n\n".format(model, model, model)
    with open(os.path.join(cwd, project_name, app_name, 'views.py'), 'r') as e:
        views = e.read()
    views = views + template
    with open(os.path.join(cwd, project_name, app_name, 'views.py'), 'w') as e:
        e.write(views)
        print("Successfully added read view!!")
    
    add_url_to_urlpatterns(os.path.join(cwd, project_name, app_name, 'urls.py'), '\tpath("{}/<id>/", {}RetrieveAPIView.as_view()),'.format(endpoint, model))
    print("Added url to path for the view!")

def making_delete_route(cwd, project_name, app_name, model, endpoint):
    template = "\nclass {}DestroyAPIView(DestroyAPIView):\n\tqueryset = {}.objects.all()\n\tserializer_class = {}Serializer\n\n".format(model, model, model)
    with open(os.path.join(cwd, project_name, app_name, 'views.py'), 'r') as e:
        views = e.read()
    views = views + template
    with open(os.path.join(cwd, project_name, app_name, 'views.py'), 'w') as e:
        e.write(views)
        print("Successfully added delete view!!")
    
    add_url_to_urlpatterns(os.path.join(cwd, project_name, app_name, 'urls.py'), '\tpath("{}/<id>/", {}DestroyAPIView.as_view()),'.format(endpoint, model))
    print("Added url to path for the view!")


# making_create_route(os.getcwd(),'new', 'api', 'User', 'user/create')
# making_update_route(os.getcwd(),'new', 'api', 'User', 'user/update')
# making_read_route(os.getcwd(),'new', 'api', 'User', 'user/read')
# making_delete_route(os.getcwd(), 'new', 'api', 'User', 'user/delete')