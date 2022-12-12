from django.shortcuts import redirect, get_object_or_404, HttpResponseRedirect
from django.views.generic import FormView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView, UpdateView
from .forms import LoginForm, PortfolioForm
from .models import Portfolio


class LoginView(FormView):

    template_name = "login.html"

    form_class = LoginForm

    def get(self, request):
        if request.user.is_authenticated:
            return HttpResponseRedirect("/")
        else:
            return super(LoginView, self).get(request)
            
    success_url = "/"

    def form_valid(self, form):

        username = form.cleaned_data["username"]

        password = form.cleaned_data["password"]

        user = authenticate(username=username, password=password)

        if user is not None:

            login(self.request, user)

        return super().form_valid(form)
        

@login_required
def logout_view(request):
    logout(request)
    return redirect('login')


class HomeView(TemplateView):

    template_name = "home.html"


class PortfolioView(TemplateView):

    template_name = "portfolio.html"

    def get_context_data(self, **kwargs):
        
        context = super().get_context_data(**kwargs)

        context['portfolios'] = Portfolio.objects.order_by("created_at")

        return context


class CreatePortfolio(LoginRequiredMixin, CreateView):

    template_name = "addportfolio.html"

    model = Portfolio

    form_class = PortfolioForm

    def form_valid(self, form):

        form.save()

        return HttpResponseRedirect("/portfolio")

class UpdatePortfolio(LoginRequiredMixin, UpdateView):

    template_name = "updateportfolio.html"

    model = Portfolio

    form_class = PortfolioForm

    def form_valid(self, form):

        form.save()

        return HttpResponseRedirect("/portfolio")


@login_required
def destroyPortfolio(request, id):
    portfolio = get_object_or_404(Portfolio, id=id)
    portfolio.delete()
    return HttpResponseRedirect("/portfolio")


class ConectedView(LoginRequiredMixin, TemplateView):

    template_name = "conected.html"