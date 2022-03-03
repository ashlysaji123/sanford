import datetime

from core.functions import get_current_role

def main_context(request):
    datetime.date.today()
    role_data = get_current_role(request)
    current_role = None

    if role_data:
        for key, value in role_data.items():
            if key == "role":
                current_role = value
            elif key == "user":
                user = value

    is_superuser = False
    is_sales_manager = False
    is_sales_coordinator = False
    is_sales_executive = False

    if current_role == "superuser":
        is_superuser = True
    elif current_role == "salesmanager":
        is_sales_manager = True
    elif current_role == "salescoordinator":
        is_sales_coordinator = True
    elif current_role == "salesexecutive":
        is_sales_executive = True


    return {
        # "domain": request.META["HTTP_HOST"],
        "title": "Home",
        "domain" : request.build_absolute_uri('/')[:-1],
        "current_path": request.get_full_path(),
        "site_title": "sanfordcorp Portal",

        "current_role": current_role,
        "is_superuser": is_superuser,
        "is_sales_manager": is_sales_manager,
        "is_sales_coordinator":is_sales_coordinator,
        "is_sales_executive":is_sales_executive,
    }
