from django.shortcuts import render
from django.views.generic import TemplateView


class LoginView(TemplateView):
    template_name = "auth/login.html"

class OtpCodeView(TemplateView):
    template_name = "auth/otp_code.html"

class RegisterView(TemplateView):
    template_name = "auth/register.html"

class VerifyOtpView(TemplateView):
    template_name = "auth/verify_otp.html"

class EmailChangePasswordView(TemplateView):
    template_name = "auth/email_change_password.html"

class ChangePasswordView(TemplateView):
    template_name = "auth/change_password.html"

class RegisterCardsView(TemplateView):
    template_name = "auth/register_cards.html"