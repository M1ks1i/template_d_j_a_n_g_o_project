"""
ASGI config for template_d_j_a_n_g_o_project project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'template_d_j_a_n_g_o_project.settings')

application = get_asgi_application()
