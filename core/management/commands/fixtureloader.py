from django.core.management.base import BaseCommand
from django.core.management import call_command
from django.db.utils import IntegrityError
from glob import glob


class Command(BaseCommand):
    help = 'Fixture loader. Imports models from fixtures.'

    def add_arguments(self, parser):
        pass

    def get_fixtures(self):
        fixtures = []
        for fixture_name in glob("core/fixtures/*.json"):
            fixtures.append({
                "name": fixture_name,
                "applied": False,
                "retries": 0,
            })
        return fixtures

    def handle(self, *args, **options):
        if options["settings"] == "ola_plus.settings.production":
            fix = input("Fixtures will be imported in the PRODUCTION environment. Are you sure? [Y/n] ")
            if fix != "Y":
                self.stderr.write("Operation cancelled.")
                return False
        fixtures = self.get_fixtures()
        while [fixture for fixture in fixtures if not fixture["applied"]]:
            for fixture in fixtures:
                if fixture["applied"]:
                    continue
                try:
                    self.stdout.write("Loading fixture " + fixture["name"])
                    call_command("loaddata", fixture["name"])
                    self.stdout.write("")
                    fixture["applied"] = True
                    fixture["retries"] = 0
                except IntegrityError as e:
                    self.stderr.write("[ FAILED ] Fixture " + fixture["name"] + ": " + e.args[0])
                    self.stdout.write("\tIt will be retried later...")
                    fixture["retries"] += 1
            if any(fixture["retries"] >= 5 for fixture in fixtures):
                self.stderr.write("Couldn't load all fixtures.")
                break
