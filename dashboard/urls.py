from django.urls import path
from .views import LoginView, PortfolioView, CreatePortfolio, UpdatePortfolio, destroyPortfolio, ConectedView, HomeView, logout_view

urlpatterns = [
    path("", HomeView.as_view(), name="dashboard"),
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", logout_view, name="logout_view"),
    path("portfolio/", PortfolioView.as_view(), name="portfolio"),
    path("portfolio/create/", CreatePortfolio.as_view(), name="create_porfolio"),
    path("portfolio/delete/<int:id>", destroyPortfolio, name="delete_port"),
    path("portfolio/update/<int:id>", UpdatePortfolio.as_view(), name="update_port"),
    path("conected/", ConectedView.as_view(), name="conected")
]
