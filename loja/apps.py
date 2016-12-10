from __future__ import unicode_literals

from django.apps import AppConfig

class LojaConfig(AppConfig):
    name = 'loja'
    verbose_name = 'WebLaches Application'
 
    def ready(self):
        import loja.signals