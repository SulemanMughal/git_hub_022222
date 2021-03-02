"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from webaccount.admin import admin_site
from django.contrib.auth import views as auth_views
from django.urls import include
# from django.conf.urls import url

from webaccount.views import *

from django.contrib.auth.views import LoginView

urlpatterns = [
    path('admin/', admin_site.urls),
    path('select2/', include('django_select2.urls')),
    path('password_reset/',auth_views.PasswordResetView.as_view(),name='admin_password_reset'),
    path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(),name='password_reset_done'),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    path('reset/done/',auth_views.PasswordResetCompleteView.as_view(),name='password_reset_complete'),
    path('profile/',  profile_view , name="profile_url"),
    path('', index_view , name="index_url"),
    path('logout/', logout_view , name="logout_url"),
    # path('password_set/', password_set_user, name="password_set_user")
    path('change_password/', change_password, name = "change_password"),
    path('edit_profile/', edit_profile, name = "edit_profile"),
    # path('admin/password_change/', change_password, name='password_change'),

    # Admin : Add New Package
    path("admin/package/new", NEW_PACKAGE, name="NEW_PACKAGE_URL"),

    # Admin : Edit Existing Package
    path("admin/package/edit/<int:package_id>/", EDIT_PACKAGE, name="EDIT_PACKAGE_URL"),

    # Admin : Delete Existing Package
    path("admin/package/delete/<int:package_id>", DELETE_PACKAGE, name="DELETE_PACKAGE_URL"),
    
    # Admin : Detail Package
    path("admin/package/detail/<int:package_id>", DETAIL_PACKAGE, name="DETAIL_PACKAGE_URL"),

    # Admin : Pacakge Object List
    path("admin/package/list", PACKAGE_LIST, name="PACKAGE_LIST_URL"),

    # RM Dashboard
    path("Relational-Manager/dashboard", RM_Dashboard, name="RM_Dashboard_URL"),

    # saved generated charts for client reports
    path("Relational-Manager/Client/List/<int:client_id>/Reports/List/<int:report_id>/Charts/List/saved", save_report_chart, name="Save_Report_Chart"),

    # RM Cient Page
    path("Relational-Manager/Client/List/", Client_List, name="Client_List_URL"),

    # RM Client Invoice List Page
    path("Relational-Manager/Client/Invoice/List/", client_invoice_list, name="Client_Invoice_List_URL"),
    

    # Specific Client Reports
    path("Relational-Manager/Client/<int:client_id>/Reports", Client_Reports, name="Client_Reports_URL"),

    # Specific Client Invoice List
    path("Relational-Manager/Client/<int:obj_id>/Invoice", invoice_list, name="Specific_Client_Invoice_URL"),

    # Add Specific Client Invoice Entry
    path("Relational-Manager/Client/<int:client_id>/Invoice/New", add_specific_client_invoice_entry, name="ADD_SPECIFIC_CLIENT_INVOICE_ENTRY_URL"),

    # ! READ SPECIFIC CLIENT INVOICE ENTRY
    path("Relational-Manager/Client/<int:client_id>/Invoice/<int:invoice_id>/view", read_specfic_client_invoice_entry, name="READ_SPECFIC_CLIENT_INVOICE_ENTRY_URL"),

    # ! Read only-by concern client
    path("Relational-Manager/Client/<int:client_id>/Invoice/<int:invoice_id>/client/view", read_specfic_client_invoice_entry_client_view, name="READ_SPECFIC_CLIENT_INVOICE_ENTRY_CLIENT_VIEW_URL"),

    # ! Upload Again Invoice File by client only
    path("Relational-Manager/Client/<int:client_id>/Invoice/<int:invoice_id>/client/update", update_file_again_by_client, name="UPDATE_FILE_AGAIN_BY_CLIENT_URL"),


    path("Relational-Manager/Client/<int:client_id>/Invoice/<int:invoice_id>/update", update_specific_client_invoice_entry, name="UPDATE_SPECIFIC_CLIENT_INVOICE_ENTRY_URL"),
    

    # ! Coment onto invoice by Relational-Manager
    path("Relational-Manager/Client/<int:client_id>/Invoice/<int:invoice_id>/update/comments", update_specific_client_invoice_entry_comments, name="UPDATE_SPECIFIC_CLIENT_INVOICE_ENTRY_COMMENTS_URL"),

    # ! Coment onto invoice by Client
    path("Relational-Manager/Client/<int:client_id>/Invoice/<int:invoice_id>/update/client/comments", update_specific_client_invoice_entry_client_comments, name="UPDATE_SPECIFIC_CLIENT_INVOICE_ENTRY_CLIENT_COMMENTS_URL"),

    # Read Client Specific Report
    path("Relational-Manager/Client/<int:client_id>/Reports/<int:report_id>", Read_Client_Report, name="Read_Client_Report_URL"),

    # Send Notification of finalize report
    path("Relational-Manager/Client/<int:client_id>/<int:report_id>/notify/", Client_Notify, name="Client_Notify_URL"),

    # RM Reports Page
    path("Relational-Manager/Reports/List/", Reports_List, name="Reports_List_URL"),

    # Relational Manager Specific Client Report Chart Page
    path("Relational-Manager/Client/<int:client_id>/Report/<int:report_id>/Charts", Client_Report_Charts, name="Report_Charts"),

    # RM New  Reports Page
    path("Relational-Manager/Reports/List/<int:client_id>/add", Add_New_RMReport, name="Reports_List_Add_URL"),

    # RM Update Reports Page
    path("Relational-Manager/Reports/List/update/<int:report_id>", update_RMReport, name="Reports_List_Update_URL"),

    # RM Invoices Page
    path("Relational-Manager/Invoices/List/", Invoices_List, name="Invoices_List_URL"),

    # RM Client API Call
    path("Relational-Manager/api/client/", Client_API, name="CLIENT_API"),

    # RM Client Sales Invoice Details
    path("Relational-Manager/api/client/<str:invoice_id>", client_specific_api, name="CLIENT_API_details"),


    path('send_quote/<int:num>',send_quote_view, name="send_quote_specific"),
    path('send_quote_send_mail/<int:client_id>', send_quote_mail_view, name="send_mail_quote_view"),
    path('update_status_approved/<int:client_id>/<int:document_id>/', change_document_submitted_status_aaproved, name="document_approved"),
    path('update_status_rejected/<int:client_id>/<int:document_id>/', change_document_submitted_status_rejected, name="document_rejected"),
    path("send-consultant-requets-quote/<int:client_id>/<int:consultant_request_id>/", sendConsultantRequestQuote, name="sendConsultantRequestQuote_URL"),
    path('send_quote_send_mail_consultant/<int:client_id>/<int:consultant_request_id>/', save_send_quote_consultant_mail_view, name="send_mail_consultant_quote_URL"),
    path('reject_quote_consultant_send_mail/<int:client_id>/<int:consultant_request_id>/', reject_quote_consultant_mail_view, name="reject_mail_consultant_quote_URL"),
    path('confirm_quote_consultant_send_mail/<int:client_id>/<int:consultant_request_id>/', confirm_quote_consultant_mail_view, name="confirm_mail_consultant_quote_URL"),
    path('close_quo-te_consultant_send_mail/<int:client_id>/<int:consultant_request_id>/', close_quote_consultant_mail_view, name="close_mail_consultant_quote_URL"),
    path('complete_quo-te_consultant_send_mail/<int:client_id>/<int:consultant_request_id>/', complete_quote_consultant_mail_view, name="complete_mail_consultant_quote_URL"),
    path('sendFile/<int:client_id>/<int:consultant_request_id>/', sendFile, name="send-file"),
    path('declined/<int:client_id>/<int:consultant_request_id>/', declineVIew, name="declineVIew_URL"),
    path('ratings/<int:client_id>/<int:consultant_request_id>/', ratingsView, name="ratingsView_URL"),
    path("see-details-consultations-fields", SeeDetails, name="SeeDetails"),

    # --------------------------------------------------------------------------------------
    # Pick Up Order Request URLS
    path('pickup-client-order-request-list/<int:client_id>/<int:pickup_order_id>/', viewPickUpRequest, name="viewPickUpRequest_URL"),

    # Accetp Pick Up Order

    path('pickup-client-order-request-accept/<int:client_id>/<int:pickup_order_id>/', viewPickUpRequestAccept, name="viewPickUpRequestAccept_URL"),

    # Reject Pick up Order
    path('pickup-client-order-request-reject/<int:client_id>/<int:pickup_order_id>/', viewPickUpRequestReject, name="viewPickUpRequestReject_URL"),

    # On Delivery
    path('pickup-client-order-request-delivery/<int:client_id>/<int:pickup_order_id>/', viewPickUpRequestOnDelivery, name="viewPickUpRequestOnDelivery_URL"),


    path('pickup-client-order-request-received/<int:client_id>/<int:pickup_order_id>/', viewPickUpRequestRecieved, name="viewPickUpRequestReceived_URL"),


    path('pickup-client-order-request-failed/<int:client_id>/<int:pickup_order_id>/', viewPickUpRequestOnFailed, name="viewPickUpRequestFailed_URL"),
    # --------------------------------------------------------------------------------------

    # Chat
    path('support/', include('core.urls')),


    # Admin Dashboard Path
    path("admin/dashboard", ADMIN_DASHBOARD,name="ADMIN_DASHBOARD_URL"),
    
]



if settings.DEBUG:
    urlpatterns+= static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

