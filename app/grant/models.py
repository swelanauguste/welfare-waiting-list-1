from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Relationship(models.Model):
    name = models.CharField(max_length=255, unique=True)
    desc = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Education(models.Model):
    name = models.CharField(max_length=255, unique=True)
    desc = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Test(models.Model):
    t_name = models.CharField(max_length=255, unique=True)
    t_desc = models.TextField(blank=True)

    def __str__(self):
        return self.name


class School(models.Model):
    s_name = models.CharField(max_length=255, unique=True)
    s_address = models.CharField(max_length=255)
    s_phone = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Child(models.Model):
    c_name = models.CharField(
        max_length=255, help_text="First, Middle, Last", verbose_name="child's name"
    )
    a_name = models.CharField(
        max_length=255,
        help_text="If agency, provide agency and contact person",
        verbose_name="your name",
    )
    a_mail = models.CharField(
        max_length=255,
        help_text="Street, Town/City",
        verbose_name="your mailing address",
    )
    a_email = models.EmailField(blank=True)
    a_phone = models.CharField(max_length=255)
    a_nic = models.PositiveIntegerField(
        help_text="NIC number", verbose_name="your NIC number"
    )
    relation = models.ForeignKey(
        Relationship, on_delete=models.PROTECT, related_name="relationships"
    )
    liv_wth = models.BooleanField(
        default=False, verbose_name="does child live with you?"
    )
    liv_wth_name = models.CharField(max_length=255, verbose_name="name")
    liv_wth_rel = models.ForeignKey(
        Relationship,
        on_delete=models.PROTECT,
        related_name="live_with_relationships",
        verbose_name="relationship",
    )
    liv_wth_add = models.CharField(
        max_length=255, verbose_name="address", help_text="Street, Town/City"
    )
    liv_wth_phone = models.CharField(max_length=255, verbose_name="phone")
    c_age = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(21)],
    )
    c_dob = models.DateField()
    c_edu = models.ForeignKey(
        Education, on_delete=models.PROTECT, related_name="education_list"
    )
    edu_resn = models.TextField(blank=True, verbose_name="reason")
    school = models.ForeignKey(
        School, on_delete=models.PROTECT, related_name="school_list"
    )
    teacher = models.CharField(max_length=255, verbose_name="teacher's name")
    beh_learn = models.BooleanField(
        default=False,
        verbose_name="has the child been tested for behavioural or learning problems?",
    )
    spec_ed = models.BooleanField(
        default=False, verbose_name="is the child in special education?"
    )
    spec_ed_teacher = models.CharField(max_length=255, verbose_name="teacher's name")
    c_work = models.BooleanField(
        default=False, verbose_name="Has the child ever worked?"
    )
    c_work_date = models.DateField()


class ChildSchool(models.Model):
    child = models.ForeignKey(
        Child, on_delete=models.PROTECT, related_name="child_schools"
    )
    school = models.ForeignKey(
        School, on_delete=models.Protect, related_name="child_schools"
    )
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    teacher = models.CharField(
        max_length=255, null=True, blank=True, verbose_name="teacher's name"
    )

    def __str__(self):
        return self.name
