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
    path("add/", views.AddProductView.as_view(), name="add-product"),
    path("deleted/", views.DeletedProductsView.as_view(), name="deleted-products"),
    path("action/", views.ProductActionView.as_view(), name="products-ation"),
    path("<int:id>/", views.ProductFormView.as_view(), name="product"),
    # path("filters/<int:id>/delete", views.DeleteProductFiltersView.as_view(), name="delete-filter"),
    
    path("filters/", views.ProductFiltersView.as_view(), name="product-filters"),
    path("filters/add", views.AddProductFilterView.as_view(), name="add-filter"),
    path("filters/action", views.ProductFiltersActionView.as_view(), name="filter-action"),
    path("filters/<int:id>", views.ProductFilterFormView.as_view(), name="filter"),
    # path("filters/<int:id>/delete", views.DeleteProductFiltersView.as_view(), name="delete-filter"),

    path("options/", views.ProductOptionsView.as_view(), name="product-options"),
    path("options/add", views.AddProductOptionView.as_view(), name="add-option"),
    path("options/<int:id>", views.ProductOptionFormView.as_view(), name="option"),
    path("options/action", views.ProductOptionsActionView.as_view(), name="option-action"),
    # path("filters/<int:id>/delete", views.DeleteProductFiltersView.as_view(), name="delete-filter"),

    path("categories/", views.CategoryView.as_view(), name="product-categories"),
    path("categories/<int:id>", views.CategoryFormView.as_view(), name="category"),
    path("categories/add", views.AddCategoryView.as_view(), name="add-category"),
    path("categories/action", views.CategoryActionView.as_view(), name="category-action"),

    path("store/<slug:slug>", views.StoreWebsite.as_view(), name="store-website"),
]

themePatterns = [
    path("", views.ThemesView.as_view(), name="themes"),
    path("<slug:slug>/", views.Theme1View.as_view(), name="theme"),
    # path("store/<slug:slug>", views.Theme1View.as_view(), name="store"),
    path("form/", views.ThemeFormView.as_view(), name="theme_form"),
    path("info/<int:id>", views.ThemInfoView.as_view(), name="theme-info"),
]

orderPatterns = [
    path("", views.OrdersView.as_view(), name="orders"),
    path("carts/abandoned", views.AbandonedCartsView.as_view(), name="abandoned-carts"),
    path("<int:id>", views.OrderView.as_view(), name="order"),
]

analyticsPatterns = [
    path("", views.AnalyticsView.as_view(), name="analytics"),
    path("reports/", views.ReportsView.as_view(), name="reports"),
    path("reports/sales", views.SalesReportView.as_view(), name="sales-report"),
    path("reports/products", views.ProductReportView.as_view(), name="products-report"),
    path("reports/customers", views.CustomerReportView.as_view(), name="customers-report"),
    path("reports/stock", views.StockReportView.as_view(), name="stock-report"),
    path("reports/orders", views.OrderReportView.as_view(), name="orders-report"),
    path("reports/coupons", views.CouponReportView.as_view(), name="coupons-report"),
    path("reports/payment", views.PaymentReportView.as_view(), name="payment-report"),
    path("reports/shipping", views.ShippingReportView.as_view(), name="shipping-report"),
]

advancedConfigPatterns = [
    path("tax/", views.TaxView.as_view(), name="tax"),
    path("team-alerts/", views.TeamAlertsView.as_view(), name="team_alerts"),
    path("members/", views.MembersView.as_view(), name="members"),
    path("questions/", views.QuestionsView.as_view(), name="questions"),
    # path("tax/", views.TaxView.as_view(), name="tax"),

]


termsPattern = [
    path("", views.TermsView.as_view(), name="terms"),
    path("license/", views.LicenseView.as_view(), name="license"),
    path("privacy/", views.PrivacyView.as_view(), name="privacy"),
    path("complaints/", views.ComplaintsView.as_view(), name="complaints"),
    path("return-policy", views.ReturnPolicyView.as_view(), name="return-policy"),
    path("conditions/", views.ConditionsView.as_view(), name="conditions"),
    
    path("payment/", views.PaymentView.as_view(), name="payment"),
    
    path("hours/", views.WorkingHoursView.as_view(), name="working-hours"),

    path("shipping/", views.ShippingView.as_view(), name="shipping"),
    path("shipping/concept", views.ShippingConceptView.as_view(), name="shipping-concept"),

    path("advanced/", include(advancedConfigPatterns)),
]

configPattern = [
    path("", views.ConfigurationView.as_view(), name="configuration"),
    path("plans", views.PlansView.as_view(), name="plans"),
    path("plans/config", views.PlanConfigView.as_view(), name="plan-config"),
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
    path("orders/", include(orderPatterns)),
    path("analytics/", include(analyticsPatterns)),
    path("config/", include(configPattern)),
    path("products/", include(storePatterns)),
]
