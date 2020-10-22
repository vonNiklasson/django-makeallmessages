from django.conf import settings

IGNORE_PATTERNS = getattr(settings, "MAM_IGNORE_PATTERNS", [])
