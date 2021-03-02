from django.db import models


class NewConsulatationRequestManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status = "New")

class ConfirmedConsulatationRequestManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status = "Confirmed")

    
class PendingConsulatationRequestManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status = "Pending")


class CompletedConsulatationRequestManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status = "Completed")


class CloseConsulatationRequestManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status = "Close")

class RejectedConsulatationRequestManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status = "Rejected")

class DeclinedConsulatationRequestManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status = "Declined")


class ACCEPTPickUpRequestOrders(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status = "ACCEPT")

class REJECTPickUpRequestOrders(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status = "REJECT")


class ON_DELIVERYPickUpRequestOrders(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status = "ON DELIVERY")

class RECEIVEDPickUpRequestOrders(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status = "RECEIVED")

class FAILEDPickUpRequestOrders(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status = "FAILED")

class PENDINGPickUpRequestOrders(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status = "PENDING")


class NewclientInvoice(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(statusType = "New")


class ApprovedclientInvoice(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(statusType = "Approved")

class RejectedclientInvoice(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(statusType = "Rejected")


class ProcessedclientInvoice(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(statusType = "Processed")


class PostponedclientInvoice(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(statusType = "Postponed")

class New_Client_Personal_Info(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status = "New")

class Active_Client_Personal_Info(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status = "Active")

class Pending_Client_Personal_Info(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status = "Pending")

class Completed_Client_Personal_Info(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status = "Completed")

class Disabled_Client_Personal_Info(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status = "Disabled")