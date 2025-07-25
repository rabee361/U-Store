from django.urls import path , include
from . import views

authPatterns = [
    path("login/", views.LoginView.as_view(), name="login"),
    path("logout/", views.LogoutView.as_view(), name="merchant-logout"),
    path("signup/", views.SignUpView.as_view(), name="signup"),
    path("otp/", views.OtpCodeView.as_view(), name="otp_code"),
    path("verify/", views.VerifyOtpView.as_view(), name="verify-otp"),
    path("register/", views.RegisterView.as_view(), name="register"),
    path("password/change", views.EmailChangePasswordView.as_view(), name="email_change_password"),
    path("change_password/", views.ChangePasswordView.as_view(), name="change_password"),
]

storePatterns = [
    path("", views.ProductsView.as_view(), name="products"),
    path("action/", views.ProductActionView.as_view(), name="products-action"),
    path("<int:id>/", views.ProductFormView.as_view(), name="product"),
    path("add/", views.AddProductView.as_view(), name="add-product"),
    path("deleted/", views.DeletedProductsView.as_view(), name="deleted-products"),
    path("categories/", views.CategoryView.as_view(), name="categories"),
    path("categories/<int:id>", views.CategoryFormView.as_view(), name="category"),
    path("categories/add", views.AddCategoryView.as_view(), name="add-category"),
    path("categories/action", views.CategoryActionView.as_view(), name="category-action"),
]

themePatterns = [
    path("", views.ThemesView.as_view(), name="themes"),
    path("theme1/", views.Theme1View.as_view(), name="theme1"),
    path("theme2/", views.Theme2View.as_view(), name="theme2"),
    path("form/", views.ThemeFormView.as_view(), name="theme_form"),
]

termsPattern = [
    path("", views.TermsView.as_view(), name="terms"),
]

configPattern = [
    path("", views.ConfigurationView.as_view(), name="configuration"),
    path("account/", views.AccountView.as_view(), name="account-setting"),
    path("currencies/", views.CurrencyView.as_view(), name="currencies"),
    path("warehouses/", views.WarehousesView.as_view(), name="warehouses"),
    path("warehouses/add", views.AddWarehouseView.as_view(), name="add-warehouse"),
    path("warehouses/<int:id>", views.WarehouseFormView.as_view(), name="warehouse"),
    path("terms/", include(termsPattern)),
]

urlpatterns = [
    path("dashboard/", views.DashboardView.as_view(), name="merchant-dasboard"),
    path("auth/", include(authPatterns)),
    path("theme/", include(themePatterns)),
    path("config/", include(configPattern)),
    path("products/", include(storePatterns)),
]