from django.core.management.base import BaseCommand
from django.utils import timezone

from faker import Faker

from tasks.models import (
    Task,
    SubTask,
    Note,
    Priority,
    Category,
)

import random


class Command(BaseCommand):

    help = "Create initial Hangarin data"

    def handle(self, *args, **kwargs):

        fake = Faker()

        priorities = list(
            Priority.objects.all()
        )

        categories = list(
            Category.objects.all()
        )

        if not priorities:
            self.stdout.write(
                self.style.ERROR(
                    "Add Priority records first."
                )
            )
            return

        if not categories:
            self.stdout.write(
                self.style.ERROR(
                    "Add Category records first."
                )
            )
            return

        for _ in range(20):

            task = Task.objects.create(

                title=fake.sentence(
                    nb_words=5
                ),

                description=fake.paragraph(
                    nb_sentences=3
                ),

                status=fake.random_element(
                    elements=[
                        "Pending",
                        "In Progress",
                        "Completed",
                    ]
                ),

                deadline=timezone.make_aware(
                    fake.date_time_this_month()
                ),

                priority=random.choice(
                    priorities
                ),

                category=random.choice(
                    categories
                ),
            )

            for _ in range(2):

                SubTask.objects.create(

                    title=fake.sentence(
                        nb_words=5
                    ),

                    status=fake.random_element(
                        elements=[
                            "Pending",
                            "In Progress",
                            "Completed",
                        ]
                    ),

                    task=task,
                )

            for _ in range(2):

                Note.objects.create(

                    task=task,

                    content=fake.paragraph(
                        nb_sentences=2
                    ),
                )

        self.stdout.write(
            self.style.SUCCESS(
                "Hangarin data created successfully."
            )
        )