# -*- coding: utf-8 -*-
# @Author: Your name
# @Date:   2023-04-24 22:39:29
# @Last Modified by:   Your name
# @Last Modified time: 2023-04-24 22:41:21
from accounts.models import User
from django.db import models
from django.db.models.fields.related import OneToOneField

# Create your models here.


class Vendor(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.OneToOneField(
        User, related_name='vendor', on_delete=models.CASCADE)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_balance(self):
        items = self.items.filter(
            vendor_paid=False, order__vendors__in=[self.id])
        return sum((item.product.price * item.quantity) for item in items)

    def get_paid_amount(self):
        items = self.items.filter(
            vendor_paid=True, order__vendors__in=[self.id])
        return sum((item.product.price * item.quantity) for item in items)
