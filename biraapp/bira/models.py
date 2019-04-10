import uuid
from django.db import models


class Projectlist(models.Model):
    project_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    project_name = models.CharField(max_length=255, blank=False, unique=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    # issues = models.ArrayField(models.CharField())

    def __str__(self):
        return "{}".format(self.project_name)


class User(models.Model):
    user_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_name = models.CharField(max_length=50)
    user_status = models.BooleanField(default=True)
    # issues = models.ArrayField(models.CharField())

    def __str__(self):
        return "{}".format(self.user_name)


class Issue(models.Model):
    issue_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    issue_title = models.CharField(max_length=50)
    # labels = models.ArrayField(models.CharField())
    assignee = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.CharField(max_length=50)
    sprint = models.CharField(max_length=50)
    status = models.CharField(max_length=50)
    issue_date_created = models.DateTimeField(auto_now_add=True)
    issue_date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{}".format(self.issue_title)


class Assign_Issue(models.Model):
    issue_id = models.ForeignKey(Issue, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return "{}".format(self.issue_id)

