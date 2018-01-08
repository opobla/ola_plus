import re
import inspect
from django.core.management.base import BaseCommand
from django.core.serializers import serialize
from core import models as core_models
import sys


class Command(BaseCommand):

    help = "Fixture Dumper. Export models to fixtures."
    format = 'json'

    def add_arguments(self, parser):
        pass

    def get_json_filename(self, name):
        s1 = re.sub('(.)([A-Z][a-z]+)', r'\1-\2', name)
        return "{0}.json".format(re.sub('([a-z0-9])([A-Z])', r'\1-\2', s1).lower())

    def get_models(self):
        return [model_name[0] for model_name in inspect.getmembers(core_models, inspect.isclass)
                if model_name[0] != 'BaseModel']

    def handle(self, *args, **options):
        sys.stdout.write('\n')
        for model_name in self.get_models():
            self.dump(model_name, 'core', self.get_json_filename(model_name))

    def dump(self, model_name, app, to_file):
        self.stdout.write("Dumping {0} in {1}".format(model_name, to_file), ending='')
        serialized_data = serialize(self.format, eval('core_models.' + model_name).objects.all(), indent=4)
        with open("{0}/fixtures/{1}".format(app, to_file), 'w+') as fixture_file:
            fixture_file.write(serialized_data)
        self.stdout.write(" [ OK ]".format(model_name, to_file))
