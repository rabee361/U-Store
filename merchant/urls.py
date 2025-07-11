from django.urls import path , include
from . import views

authPatterns = [
    path("dashboard/", views.DashboardView.as_view(), name="dashboard"),
    path("login/", views.LoginView.as_view(), name="login"),
    path("otp_code/", views.OtpCodeView.as_view(), name="otp_code"),
    path("register/", views.RegisterView.as_view(), name="register"),
    path("verify_otp/", views.VerifyOtpView.as_view(), name="verify_otp"),
    path("email_change_password/", views.EmailChangePasswordView.as_view(), name="email_change_password"),
    path("change_password/", views.ChangePasswordView.as_view(), name="change_password"),
    path("register_cards/", views.RegisterCardsView.as_view(), name="register_cards"),
]

configPattern = [
    path("config/", views.ConfigurationView.as_view(), name="configuration"),
    path("currencies/", views.CurrencyView.as_view(), name="currencies"),
]

urlpatterns = [
    path("auth/", include(authPatterns)),
    path("config/", include(configPattern)),
]