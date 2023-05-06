from django.contrib import admin

# Register your models here.

from .models import Medecine
from .models import Infermier
from .models import Abcense
from .models import Patient
from .models import Planing
from .models import Dossier_medecale
from .models import Rapport
from .models import administrator
from .models import driver
from .models import User


admin.site.register(Medecine)
admin.site.register(Infermier)
admin.site.register(Patient)
admin.site.register(Planing)
admin.site.register(Dossier_medecale)
admin.site.register(Abcense)
admin.site.register(Rapport)
admin.site.register(administrator)
admin.site.register(driver)
admin.site.register(User)








# Register your models here.
