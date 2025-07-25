from django.shortcuts import render, redirect, get_object_or_404, reverse, HttpResponseRedirect
from django.urls import reverse
from django.views.generic import TemplateView, ListView
from django.views import View
from django.contrib.auth import login, logout
from django.contrib import messages
from .forms import *
from .models import *
from django.db import transaction
from accounts.tasks import send_otp_task
from utils.email import send_otp_email
from utils.types import UserType
from django.contrib.auth import get_user_model
User = get_user_model()
import json



class DashboardView(TemplateView):
    template_name = "dashboard.html"

class LoginView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('merchant-dasboard')
        form = MerchantLoginForm()
        return render(request, "auth/login.html", {"form": form})

    def post(self, request):
        form = MerchantLoginForm(request.POST)
        if form.is_valid():
            user = form.cleaned_data.get('user', None)
            if user:
                login(request, user)
                return redirect('merchant-dasboard')
        return render(request, "auth/login.html", {"form": form})

class LogoutView(View):
    def get(self, request):
        logout(request.user)
        return redirect('login')

class SignUpView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('dashboard')
        form = MerchantSignUpForm()
        return render(request, "auth/signup.html", {"form": form})

    @transaction.atomic
    def post(self, request):
        form = MerchantSignUpForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = User.objects.create_user(username=email, email=email, password=password,user_type=UserType.MERCHANT)
            x = OTPCode.checkLimit(email)
            print(x)
            print(user)
            if user and not OTPCode.checkLimit(email):
                user.create_signup_otp()
                request.session['signup_email'] = email
                print(request.session['signup_email'])
                # send_otp_task.delay(user.create_signup_otp(), user.email) #TODO test it in prod with redis
                # send_otp_email(code, user.email)
                return redirect('verify-otp')
        return render(request, "auth/signup.html", {"form": form})

class OtpCodeView(View):
    def get(self,request):
        form = OTPForm()
        return render(request, "auth/otp_code.html", {"form":form})

    def post(self,request):
        form = OTPForm()
        if form.is_valid():
            return redirect('verify-otp')
        return render(request, "auth/otp_code.html", {"form":form})

class VerifyOtpView(TemplateView):
    def get(self, request):
        # Check if user email is in session
        email = request.session.get('signup_email')
        if not email:
            messages.error(request, 'يرجى إعادة المحاولة من البداية')
            return redirect('signup')
        form = VerifyOTPForm()
        return render(request, "auth/verify_otp.html", {"form": form, "email": email})

    def post(self, request):
        email = request.session.get('signup_email')
        if not email:
            messages.error(request, 'يرجى إعادة المحاولة من البداية')
            return redirect('signup')
        form = VerifyOTPForm(request.POST)
        if form.is_valid():
            try:
                user = form.save(email)
                if user:
                    messages.success(request, 'تم التحقق من البريد الإلكتروني بنجاح')
                    return redirect('register')
            except forms.ValidationError as e:
                form.add_error(None, str(e))

        return render(request, "auth/verify_otp.html", {"form": form, "email": email})

class EmailChangePasswordView(TemplateView):
    template_name = "auth/email_change_password.html"

class ChangePasswordView(TemplateView):
    template_name = "auth/change_password.html"

class RegisterView(View):
    def get(self, request):
        # Check if user email exists in session
        email = request.session.get('signup_email')
        if not email:
            return redirect('signup')

        form = RegisterMerchantForm()
        return render(request, "auth/register.html", {"form": form})

    def post(self, request):
        try:
            email = request.session.get('signup_email')
            if not email:
                return redirect('signup')

            user = User.objects.get(email=email)
            form = RegisterMerchantForm(request.POST)

            if form.is_valid():
                merchant = form.save(user)
                # Clear session after successful registration
                request.session.pop('signup_email', None)
                return redirect('merchant-dasboard')
            return render(request, "auth/register.html", {"form": form})
        except User.DoesNotExist:
            return redirect('signup')

class ConfigurationView(TemplateView):
    template_name = "config/main/configuration.html"

class CurrencyView(TemplateView):
    template_name = "config/main/currencies.html"

class WarehousesView(TemplateView):
    template_name = "config/warehouses/management/warehouse_management.html"

class AddWarehouseView(TemplateView):
    template_name = "config/warehouses/management/warehouse_form.html"

class WarehouseFormView(TemplateView):
    template_name = "config/warehouses/management/warehouse_form.html"

class AccountView(TemplateView):
    template_name = "config/main/account.html"

class ProductsView(ListView):
    model = Product
    context_object_name = 'products'
    template_name = "products/products.html"

class DeletedProductsView(View):
    def get(self, request):
        products = Product.objects.filter(isDeleted=True)
        return render(request, "products/products.html", {"products": products})

class AddProductView(TemplateView):
    template_name = "products/product.html"

class ProductFormView(TemplateView):
    template_name = "products/product.html"
    
class ProductActionView(View):
    def post(self, request):
        selected_ids = json.loads(request.POST.get('selected_ids', '[]'))
        action = request.POST.get('action')
        if action == 'delete':
            Product.objects.filter(id__in=selected_ids).delete()
        return HttpResponseRedirect(reverse('products'))

class CategoryView(ListView):
    model = ProductCategory
    context_object_name = 'categories'
    template_name = "products/categories/categories.html"

class AddCategoryView(View):
    def get(self, request):
        form = CategoryForm()
        context = {
            'form': form,
            'is_edit': False
        }
        return render(request, "products/categories/category_form.html", context)

    def post(self, request):
        form = CategoryForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            category = form.save(commit=False)
            category.merchant = request.user.merchant
            category.save()
            return redirect('categories')

        context = {
            'form': form,
            'is_edit': False
        }
        return render(request, "products/categories/category_form.html", context)

class CategoryFormView(View):
    def get(self, request, id=None):
        if id:
            try:
                category = ProductCategory.objects.get(id=id)
                form = CategoryForm(instance=category)
                context = {
                    'form': form,
                    'category': category,
                    'is_edit': True
                }
            except ProductCategory.DoesNotExist:
                return redirect('404')
        else:
            form = CategoryForm()
            context = {
                'form': form,
                'is_edit': False
            }

        return render(request, "products/categories/category_form.html", context)

    def post(self, request, id=None):
        if id:
            try:
                category = ProductCategory.objects.get(id=id)
                form = CategoryForm(instance=category, data=request.POST, files=request.FILES)
                is_edit = True
            except ProductCategory.DoesNotExist:
                return redirect('404')
        else:
            form = CategoryForm(data=request.POST, files=request.FILES)
            is_edit = False
            category = None

        if form.is_valid():
            saved_category = form.save(commit=False)
            if not is_edit:
                saved_category.merchant = request.user.merchant
            saved_category.save()
            return redirect('categories')

        context = {
            'form': form,
            'category': category,
            'is_edit': is_edit
        }
        return render(request, "products/categories/category_form.html", context)


class CategoryActionView(View):
    def post(self, request):
        selected_ids = json.loads(request.POST.get('selected_ids', '[]'))
        action = request.POST.get('action')
        if action == 'delete':
            ProductCategory.objects.filter(id__in=selected_ids).delete()
        return HttpResponseRedirect(reverse('categories'))

class Theme1View(TemplateView):
    template_name = "themes/theme1/main.html"

class Theme2View(TemplateView):
    template_name = "themes/theme2/main.html"

class ThemesView(TemplateView):
    template_name = "themes/main/themes.html"

class ThemeFormView(TemplateView):
    template_name = "themes/main/theme_form.html"

class TermsView(TemplateView):
    template_name = "config/terms/terms.html"

