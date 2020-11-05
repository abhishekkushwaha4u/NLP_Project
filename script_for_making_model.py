import os

model_base_template = """

class {}(models.Model):
"""
import sys
def add_model(name, model_dict):
    """
    Right now only CharField and IntegerField accepted with timestamp as a datetimefield
    Expecting a dict like this:
    {
        "name": {"type": "CharField", "max_length": 100, "primary_key":True},
        "age": {"type": "IntegerField", "default":0},
        "desc": {"type": "CharField", "max_length": 100, blank=True}
        "timestamp":True
    }

    """
    model_base = model_base_template.format(name)
    model_stuct = ""
    for i in model_dict:
        default = None
        primary_key = False
        additional_params = ""
        new_column_template = "\t{}=models.{}({})\n"
        if model_dict[i]["type"] == "CharField":
            if "max_length" not in model_dict[i]:
                print("Need a max_length for CharField to proceed!!!")
                sys.exit(0)
            else:
                additional_params+="max_length={}".format(model_dict[i]['max_length'])
            if "default" in model_dict[i]:
                default=model_dict[i]["default"]
                additional_params+=",default={}".format(default)
            if "primary_key" in model_dict[i]:
                primary_key=model_dict[i]["primary_key"]
                additional_params+=",primary_key=True"
            

            model_stuct += new_column_template.format(name, model_dict[i]["type"], additional_params)
        



def add_model_temp_fix(project_name, app_name, model_name, field_names):
    base_template = "\t{} = models.CharField(max_length=500)\n"
    final_model = model_base_template.format(model_name)
    for i in field_names:
        final_model += base_template.format(i)
    
    #print(final_model)
    with open(os.path.join(os.getcwd(), project_name, app_name, 'models.py'), 'r') as e:
        model = e.read()
    model = model + final_model
    with open(os.path.join(os.getcwd(), project_name, app_name, 'models.py'), 'w') as e:
        e.write(model)
        print("Successfully added models!!")
    


    serializer = """
    class {}Serializer(serializers.ModelSerializer):
        class Meta:
            model = {}
            fields = "__all__"
    """
    with open(os.path.join(os.getcwd(), project_name, app_name, 'serializers.py'), 'r') as e:
        serializers = e.read()
    serializers = serializers + serializer.format(model_name, model_name)
    with open(os.path.join(os.getcwd(), project_name, app_name, 'serializers.py'), 'w') as e:
        e.write(serializers)
        print("Successfully added serializer!!")




#add_model_temp_fix('new','api','User', ["name", "description"])