from django.core.management.base import BaseCommand
from django.core.management import call_command
from django.db.utils import IntegrityError
from glob import glob


class Command(BaseCommand):
    help = 'Fixture loader. Imports models from fixtures.'

    def add_arguments(self, parser):
        pass

    def get_fixtures(self):
        return glob("core/fixtures/*.json")

    def handle(self, *args, **options):
        if options["settings"] == "ola_plus.settings.production":
            fix = input("Fixtures will be imported in the PRODUCTION environment. Are you sure? [Y/n] ")
            if fix != "Y":
                self.stderr.write("Operation cancelled.")
                return False

        for fixture in self.get_fixtures():
            try:
                self.stdout.write("Fixture for: " + fixture)
                call_command('loaddata', fixture)
            except IntegrityError as e:
                self.stderr.write("Fixture: " + fixture + " [ FAILED ]", e.args)
