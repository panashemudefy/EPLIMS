from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class House(models.Model):
    """Model representing a house with a water well"""
    
    # Basic house information
    address = models.CharField(max_length=255, unique=True)
    owner_name = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=20, blank=True, null=True)
    
    # Well characteristics
    well_depth = models.DecimalField(
        max_digits=6, 
        decimal_places=2,
        help_text="Depth of the well in meters",
        validators=[MinValueValidator(0)]
    )
    well_diameter = models.DecimalField(
        max_digits=5, 
        decimal_places=2,
        help_text="Diameter of the well in centimeters",
        validators=[MinValueValidator(0)]
    )
    
    # Water quality metrics
    water_ph = models.DecimalField(
        max_digits=3, 
        decimal_places=1,
        validators=[MinValueValidator(0), MaxValueValidator(14)],
        blank=True, 
        null=True
    )
    is_potable = models.BooleanField(
        default=False,
        help_text="Whether the water is safe for drinking"
    )
    
    # Water yield information
    daily_yield = models.DecimalField(
        max_digits=8, 
        decimal_places=2,
        help_text="Daily water yield in liters",
        validators=[MinValueValidator(0)],
        blank=True, 
        null=True
    )
    
    # Location coordinates (optional)
    latitude = models.DecimalField(
        max_digits=9, 
        decimal_places=6,
        blank=True, 
        null=True
    )
    longitude = models.DecimalField(
        max_digits=9, 
        decimal_places=6,
        blank=True, 
        null=True
    )
    
    # Additional notes
    notes = models.TextField(blank=True)
    
    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.address} - {self.owner_name}"
    
    class Meta:
        ordering = ['address']
        verbose_name_plural = "Houses with Wells"