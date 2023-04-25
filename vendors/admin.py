# -*- coding: utf-8 -*-
# @Author: Your name
# @Date:   2023-04-24 22:39:29
# @Last Modified by:   Your name
# @Last Modified time: 2023-04-24 22:49:10
from django.contrib import admin

from .models import Vendor


@admin.register(Vendor)
class VendorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_at', 'created_by')
    list_filter = ('created_at', 'created_by')
    search_fields = ('name',)
    date_hierarchy = 'created_at'
