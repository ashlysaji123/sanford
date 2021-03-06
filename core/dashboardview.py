import datetime
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from coordinators.models import SalesCoordinator, SalesManager
from core.functions import get_current_role
from core.models import Shop
from core.decorators import checking_dashboard_access
from executives.models import SalesExecutive
from leave.models import LeaveRequest
from merchandiser.models import Merchandiser
from notifications.models import Notification
from products.models import Product
from loans.models import Loan
from salaries.models import SalaryAdavance
from documents.models import EmployeeDocuments
from sales.models import Sales
from expenses.models import Expenses


@login_required
@checking_dashboard_access
def app(request):
    datetime.date.today()
    role_data = get_current_role(request)
    current_role = None
    if role_data:
        for key, value in role_data.items():
            if key == "role":
                current_role = value
            elif key == "user":
                pass

    is_superuser = False
    is_global_manager = False
    is_sales_manager = False
    is_sales_coordinator = False
    is_sales_supervisor = False

    notifications = Notification.objects.filter(is_deleted=False)
    notifications_count = notifications.count()
    product_count = Product.objects.filter(is_deleted=False).count()
    hot_products = Product.objects.filter(is_hot_product=True).order_by("-created")[:5]

    if current_role == "superuser":
        is_superuser = True
        manager_count = SalesManager.objects.filter(is_deleted=False).count()
        coordinator_count = SalesCoordinator.objects.filter(is_deleted=False).count()
        executive_count = SalesExecutive.objects.filter(is_deleted=False).count()
        merchandiser_count = Merchandiser.objects.filter(is_deleted=False).count()
        shope_count = Shop.objects.filter(is_deleted=False).count()
        pending_leave_request = LeaveRequest.objects.filter(
            is_deleted=False,
            is_approved=False,
            is_rejected=False,
            global_manager_approved=True
        ).count()
        pending_loan_request = Loan.objects.filter(
            is_deleted=False,
            is_approved=False,
            is_rejected=False,
            global_manager_approved=True
        ).count()
        salary_advance_request = SalaryAdavance.objects.filter(
            is_deleted=False,
            is_approved=False,
            is_rejected=False,
            global_manager_approved=True
        ).count()
        pending_documents_request = EmployeeDocuments.objects.filter(
            is_deleted=False,
            is_approved=False,
            is_rejected=False,
            global_manager_approved=True
        ).count()
        #sales
        monthly_sales = Sales.objects.filter(
            is_approved=True,
            is_deleted=False,
            created__month=datetime.datetime.now().month
        )
        monthly_sales_amount = 0
        for i in monthly_sales:
            monthly_sales_amount += i.total_amount
        #expeses
        monthly_expense = Expenses.objects.filter(
            is_approved=True,
            is_deleted=False,
            created__month=datetime.datetime.now().month
        )
        monthly_expense_amount = 0
        for i in monthly_expense:
            monthly_expense_amount += i.amount

    elif current_role == "globalmanager":
        is_global_manager = True
        manager_count = SalesManager.objects.filter(is_deleted=False).count()
        coordinator_count = SalesCoordinator.objects.filter(is_deleted=False).count()
        executive_count = SalesExecutive.objects.filter(is_deleted=False).count()
        merchandiser_count = Merchandiser.objects.filter(is_deleted=False).count()
        shope_count = Shop.objects.filter(is_deleted=False).count()
        pending_leave_request = LeaveRequest.objects.filter(
            is_deleted=False,
            is_approved=False,
            is_rejected=False,
            manager_approved=True
        ).count()
        pending_loan_request = Loan.objects.filter(
            is_deleted=False,
            is_approved=False,
            is_rejected=False,
            manager_approved=True
        ).count()
        salary_advance_request = SalaryAdavance.objects.filter(
            is_deleted=False,
            is_approved=False,
            is_rejected=False,
            manager_approved=True
        ).count()
        pending_documents_request = EmployeeDocuments.objects.filter(
            is_deleted=False,
            is_approved=False,
            is_rejected=False,
            manager_approved=True
        ).count()
        # Sales
        monthly_sales = Sales.objects.filter(
            is_approved=True,
            is_deleted=False,
            created__month=datetime.datetime.now().month
        )
        monthly_sales_amount = 0
        for i in monthly_sales:
            monthly_sales_amount += i.total_amount
        #expeses
        monthly_expense = Expenses.objects.filter(
            is_approved=True,
            is_deleted=False,
            created__month=datetime.datetime.now().month
        )
        monthly_expense_amount = 0
        for i in monthly_expense:
            monthly_expense_amount += i.amount

    elif current_role == "salesmanager":
        is_sales_manager = True
        coordinator_count = SalesCoordinator.objects.filter(
            is_deleted=False, region=request.user.region
        ).count()
        executive_count = SalesExecutive.objects.filter(
            is_deleted=False, region=request.user.region
        ).count()
        merchandiser_count = Merchandiser.objects.filter(
            is_deleted=False, area__sub_region__region=request.user.region
        ).count()
        shope_count = Shop.objects.filter(
            is_deleted=False, area__sub_region__region=request.user.region
        ).count()
        pending_leave_request = LeaveRequest.objects.filter(
            is_deleted=False,
            is_approved=False,
            is_rejected=False,
            coordinator_approved=True,
            user__region=request.user.region
        ).count()
        pending_loan_request = Loan.objects.filter(
            is_deleted=False,
            is_approved=False,
            is_rejected=False,
            coordinator_approved=True,
            creator__region=request.user.region
        ).count()
        salary_advance_request = SalaryAdavance.objects.filter(
            is_deleted=False,
            is_approved=False,
            is_rejected=False,
            coordinator_approved=True,
            user__region=request.user.region
        ).count()
        pending_documents_request = EmployeeDocuments.objects.filter(
            is_deleted=False,
            is_approved=False,
            is_rejected=False,
            coordinator_approved=True,
            user__region=request.user.region
        ).count()
        pending_sales_request = Sales.objects.filter(
            is_deleted=False,
            is_approved=False,
            is_rejected=False,
            coordinator_approved=True,
            user__region=request.user.region
        ).count()
        pending_expense_claim_request = Expenses.objects.filter(
            is_deleted=False,
            is_approved=False,
            is_rejected=False,
            coordinator_approved=True,
            user__region=request.user.region,
        ).count()

    elif current_role == "salescoordinator":
        is_sales_coordinator = True
        executive_count = SalesExecutive.objects.filter(
            is_deleted=False, region=request.user.region
        ).count()
        merchandiser_count = Merchandiser.objects.filter(
            is_deleted=False, area__sub_region__region=request.user.region
        ).count()
        shope_count = Shop.objects.filter(
            is_deleted=False, area__sub_region__region=request.user.region
        ).count()
        pending_leave_request = LeaveRequest.objects.filter(
            is_deleted=False,
            is_approved=False,
            is_rejected=False,
            supervisor_approved=True,
            user__region=request.user.region
        ).count()
        pending_loan_request = Loan.objects.filter(
            is_deleted=False,
            is_approved=False,
            is_rejected=False,
            supervisor_approved=True,
            creator__region=request.user.region
        ).count()
        salary_advance_request = SalaryAdavance.objects.filter(
            is_deleted=False,
            is_approved=False,
            is_rejected=False,
            supervisor_approved=True,
            user__region=request.user.region
        ).count()
        pending_documents_request = EmployeeDocuments.objects.filter(
            is_deleted=False,
            is_approved=False,
            is_rejected=False,
            supervisor_approved=True,
            user__region=request.user.region
        ).count()
        pending_sales_request = Sales.objects.filter(
            is_deleted=False,
            is_approved=False,
            is_rejected=False,
            supervisor_approved=True,
            user__region=request.user.region
        ).count()
        pending_expense_claim_request = Expenses.objects.filter(
            is_deleted=False,
            is_approved=False,
            is_rejected=False,
            supervisor_approved=True,
            user__region=request.user.region,
        ).count()

    elif current_role == "salessupervisor":
        is_sales_supervisor = True
        executive_count = SalesExecutive.objects.filter(
            is_deleted=False, region=request.user.region
        ).count()
        merchandiser_count = Merchandiser.objects.filter(
            is_deleted=False, area__sub_region__region=request.user.region
        ).count()
        shope_count = Shop.objects.filter(
            is_deleted=False, area__sub_region__region=request.user.region
        ).count()
        """ Sales request query joining """
        qs = Sales.objects.filter(
            is_deleted=False,
            is_approved=False,
            is_rejected=False,
            supervisor_approved=False,
            supervisor_rejected=False
        ).prefetch_related('user')
        exe_qs = qs.filter(user__salesexecutive__supervisor__user=request.user).count()
        mer_qs = qs.filter(user__merchandiser__executive__supervisor__user=request.user).count()
        pending_sales_request = exe_qs + mer_qs
        """ sales query ends here """
        """ documents request query joining """
        qs = EmployeeDocuments.objects.filter(
            is_deleted=False,
            is_approved=False,
            is_rejected=False,
            supervisor_approved=False,
            supervisor_rejected=False
        ).prefetch_related('user')
        exe_qs = qs.filter(user__salesexecutive__supervisor__user=request.user).count()
        mer_qs = qs.filter(user__merchandiser__executive__supervisor__user=request.user).count()
        pending_documents_request = exe_qs + mer_qs
        """ documents query ends here """
        """ slary advance request query joining """
        qs = SalaryAdavance.objects.filter(
            is_deleted=False,
            is_approved=False,
            is_rejected=False,
            supervisor_approved=False,
            supervisor_rejected=False
        ).prefetch_related('user')
        exe_qs = qs.filter(user__salesexecutive__supervisor__user=request.user).count()
        mer_qs = qs.filter(user__merchandiser__executive__supervisor__user=request.user).count()
        salary_advance_request = exe_qs + mer_qs
        """ slary advance query ends here """
        """ leave request query joining """
        qs = LeaveRequest.objects.filter(
            is_deleted=False,
            is_approved=False,
            is_rejected=False,
            supervisor_approved=False,
            supervisor_rejected=False
        ).prefetch_related('user')
        exe_qs = qs.filter(user__salesexecutive__supervisor__user=request.user).count()
        mer_qs = qs.filter(user__merchandiser__executive__supervisor__user=request.user).count()
        pending_leave_request = exe_qs + mer_qs
        """ leave query ends here """
        """ loan request query joining """
        qs = Loan.objects.filter(
            is_deleted=False,
            is_approved=False,
            is_rejected=False,
            supervisor_approved=False,
            supervisor_rejected=False
        ).prefetch_related('creator')
        exe_qs = qs.filter(creator__salesexecutive__supervisor__user=request.user).count()
        mer_qs = qs.filter(creator__merchandiser__executive__supervisor__user=request.user).count()
        pending_loan_request = exe_qs + mer_qs
        """ loan query ends here """
        pending_expense_claim_request = Expenses.objects.filter(
            is_deleted=False,
            is_approved=False,
            is_rejected=False,
            supervisor_approved=False,
            supervisor_rejected=False,
            user__salesexecutive__supervisor__user=request.user
        ).count()

    context = {
        "domain": request.build_absolute_uri("/")[:-1],
        "current_path": request.get_full_path(),
        "site_title": "sanfordcorp Portal",
        "current_role": current_role,
        "is_superuser": is_superuser,
        "is_global_manager": is_global_manager,
        "is_sales_manager": is_sales_manager,
        "is_sales_coordinator": is_sales_coordinator,
        "is_sales_supervisor": is_sales_supervisor,
        "notifications_count": notifications_count,
        "notifications": notifications,
        "product_count": product_count,
        "hot_products": hot_products,
    }
    if current_role == "superuser":
        context.update(
            {
                "merchandiser_count": merchandiser_count,
                "executive_count": executive_count,
                "coordinator_count": coordinator_count,
                "manager_count": manager_count,
                "shope_count": shope_count,
                "pending_loan_request":pending_loan_request,
                "pending_leave_request":pending_leave_request,
                "salary_advance_request":salary_advance_request,
                "pending_documents_request":pending_documents_request,
                "monthly_sales_amount":monthly_sales_amount,
                "monthly_expense_amount":monthly_expense_amount,
            }
        )
    if current_role == "globalmanager":
        context.update(
            {
                "merchandiser_count": merchandiser_count,
                "executive_count": executive_count,
                "coordinator_count": coordinator_count,
                "manager_count": manager_count,
                "shope_count": shope_count,
                "pending_loan_request":pending_loan_request,
                "pending_leave_request":pending_leave_request,
                "salary_advance_request":salary_advance_request,
                "pending_documents_request":pending_documents_request,
                "monthly_sales_amount":monthly_sales_amount,
                "monthly_expense_amount":monthly_expense_amount,
            }
        )
    elif current_role == "salesmanager":
        context.update(
            {
                "merchandiser_count": merchandiser_count,
                "executive_count": executive_count,
                "coordinator_count": coordinator_count,
                "pending_expense_claim_request":pending_expense_claim_request,
                "pending_loan_request":pending_loan_request,
                "pending_leave_request":pending_leave_request,
                "salary_advance_request":salary_advance_request,
                "pending_documents_request":pending_documents_request,
                "pending_sales_request":pending_sales_request,
                "shope_count":shope_count,
            }
        )
    elif current_role == "salescoordinator":
        context.update(
            {
                "merchandiser_count": merchandiser_count,
                "executive_count": executive_count,
                "pending_expense_claim_request":pending_expense_claim_request,
                "pending_loan_request":pending_loan_request,
                "pending_leave_request":pending_leave_request,
                "salary_advance_request":salary_advance_request,
                "pending_documents_request":pending_documents_request,
                "pending_sales_request":pending_sales_request,
                "shope_count":shope_count,
            }
        )
    elif current_role == "salessupervisor":
        context.update(
            {
                "merchandiser_count": merchandiser_count,
                "executive_count": executive_count,
                "pending_expense_claim_request":pending_expense_claim_request,
                "pending_loan_request":pending_loan_request,
                "pending_leave_request":pending_leave_request,
                "salary_advance_request":salary_advance_request,
                "pending_documents_request":pending_documents_request,
                "pending_sales_request":pending_sales_request,
                "shope_count":shope_count,
            }
        )

    return render(request, "index.html", context)
