from django.contrib import admin
from .models import House

@admin.register(House)
class HouseAdmin(admin.ModelAdmin):
    # Fields to display in list view
    list_display = (
        'address', 
        'owner_name', 
        'well_depth', 
        'well_diameter',
        'water_ph',
        'is_potable',
        'daily_yield',
        'created_at'
    )
    
    # Filter options
    list_filter = (
        'is_potable',
        'well_depth',
    )

    
    # Searchable fields
    search_fields = (
        'address', 
        'owner_name',
        'contact_number'
    )
    
    # Fields grouping in edit view
    fieldsets = (
        ('House Information', {
            'fields': ('address', 'owner_name', 'contact_number')
        }),
        ('Well Characteristics', {
            'fields': ('well_depth', 'well_diameter', 'daily_yield')
        }),
        ('Water Quality', {
            'fields': ('water_ph', 'is_potable')
        }),
        ('Location', {
            'fields': ('latitude', 'longitude'),
            'classes': ('collapse',)  # Makes this section collapsible
        }),
        ('Additional Information', {
            'fields': ('notes',),
            'classes': ('collapse',)
        }),
    )
    
    # Read-only fields
    readonly_fields = ('created_at', 'updated_at')
    
    # Pagination
    list_per_page = 25
    
    # Ordering
    ordering = ('address',)