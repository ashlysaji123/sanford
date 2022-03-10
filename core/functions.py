import math

from coordinators.models import SalesCoordinator, SalesManager
from executives.models import SalesExecutive


def get_distance(origin, destination):

    lat1_str, lon1_str = origin.split(",")
    lat2_str, lon2_str = destination.split(",")

    lat1, lon1, lat2, lon2 = (
        float(lat1_str),
        float(lon1_str),
        float(lat2_str),
        float(lon2_str),
    )

    radius = 6371  # km

    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    a = math.sin(dlat / 2) * math.sin(dlat / 2) + math.cos(
        math.radians(lat1)
    ) * math.cos(math.radians(lat2)) * math.sin(dlon / 2) * math.sin(dlon / 2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    distance = radius * c

    return distance


def get_current_role(request):
    current_role = {}
    if request.user.is_authenticated:
        if request.user.is_superuser:
            current_role = {
                "role": "superuser",
            }
        elif SalesManager.objects.filter(
            user=request.user, user__is_sales_manager=True
        ).exists():
            current_role = {"role": "salesmanager", "user": request.user}
        elif SalesCoordinator.objects.filter(
            user=request.user, user__is_sales_coordinator=True
        ).exists():
            current_role = {"role": "salescoordinator", "user": request.user}
        elif SalesExecutive.objects.filter(
            user=request.user, user__is_sales_executive=True
        ).exists():
            current_role = {"role": "salesexecutive", "user": request.user}
        return current_role


def generate_form_errors(args, formset=False):
    message = ""
    if not formset:
        for field in args:
            if field.errors:
                message += field.errors[0] + "|"
        for err in args.non_field_errors():
            message += str(err) + "|"

    elif formset:
        for form in args:
            for field in form:
                if field.errors:
                    message += field.errors[0] + "|"
            for err in form.non_field_errors():
                message += str(err) + "|"
    return message[:-1]


def get_response_data(status_code, **kwargs):
    create_func_names = ["add", "create"]
    update_func_names = ["edit", "update"]
    MESSAGE = kwargs.get("message", None)

    if MESSAGE is None:
        try:
            invoking_func_name = (inspect.stack()[1].function).split("_")
            print(invoking_func_name, "<-- invoking_func_name")

            if invoking_func_name[0] in create_func_names:
                if len(invoking_func_name) > 2:
                    MESSAGE = "{} {} successfully created".format(
                        invoking_func_name[1].title(), invoking_func_name[2]
                    )
                else:
                    MESSAGE = "{} successfully created".format(
                        invoking_func_name[1].title()
                    )

            elif invoking_func_name[0] in update_func_names:
                if len(invoking_func_name) > 2:
                    MESSAGE = "{} {} updated successfully".format(
                        invoking_func_name[1].title(), invoking_func_name[2]
                    )
                else:
                    MESSAGE = "{} updated successfully".format(
                        invoking_func_name[1].title()
                    )
        except:
            raise ValueError(
                "missing attribute 'message' or use tfora standard function naming"
            )

    if status_code == 1:
        title_data = {"status": "true", "title": kwargs.get("title", "Success")}
        _response_data = {
            **title_data,
            "message": MESSAGE,
            "redirect": "true",
            "redirect_url": kwargs.get("redirect_url", None),
        }
    elif status_code == 0:
        title_data = {
            "status": "false",
            "title": kwargs.get("title", "Uh oh! Form Validation Error"),
        }
        _response_data = {**title_data, "message": MESSAGE, "stable": "true"}
    else:
        raise AssertionError("improper status_code.Valid codes are 1 or 0.")
    return _response_data
