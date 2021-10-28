# apic/rails/views.py
from datetime import datetime
from operator import itemgetter
from urllib.parse import urljoin

import requests
from django.conf import settings
from django.urls import reverse_lazy
from django.views import generic
from requests.exceptions import RequestException

from .forms import AuthenticateForm


class IndexView(generic.TemplateView):
    template_name = "rails/index.html"


class StationsView(generic.TemplateView):
    template_name = "rails/stations.html"

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)

        api_url = urljoin(settings.BASE_API_URL, "stations")

        try:
            response = requests.get(api_url)
            response.raise_for_status()
        except RequestException as err:
            context["error"] = err
        else:
            context["stations"] = response.json()

        return self.render_to_response(context)


class DeparturesView(generic.TemplateView):
    template_name = "rails/departures.html"

    def get(self, request, station_id, *args, **kwargs):
        context = self.get_context_data(**kwargs)

        api_url = urljoin(
            settings.BASE_API_URL,
            f"stations/{station_id}/departures",
        )

        try:
            response = requests.get(api_url)
            response.raise_for_status()
        except RequestException as err:
            context["error"] = err
        else:
            trains = prepare_trains(response.json(), "departs_at")
            context["departures"] = trains

        return self.render_to_response(context)


class ArrivalsView(generic.TemplateView):
    template_name = "rails/arrivals.html"

    def get(self, request, station_id, *args, **kwargs):
        context = self.get_context_data(**kwargs)

        api_url = urljoin(
            settings.BASE_API_URL,
            f"stations/{station_id}/arrivals",
        )

        try:
            response = requests.get(api_url)
            response.raise_for_status()
        except RequestException as err:
            context["error"] = err
        else:
            trains = prepare_trains(response.json(), "arrives_at")
            context["arrivals"] = trains

        return self.render_to_response(context)


class UsersView(generic.TemplateView):
    template_name = "rails/users.html"

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)

        api_url = urljoin(
            settings.BASE_API_URL,
            "users",
        )

        try:
            response = requests.get(api_url)
            response.raise_for_status()
        except RequestException as err:
            context["error"] = err
        else:
            context["users"] = response.json()

        return self.render_to_response(context)


class AuthenticateView(generic.FormView):
    template_name = "rails/authenticate.html"
    success_url = reverse_lazy("auth_result")
    form_class = AuthenticateForm

    def form_valid(self, form):
        data = form.cleaned_data
        self.api_authenticate(data["email"], data["password"])
        # leave this as final instruction as it will just perform the redir.
        return super().form_valid(form)

    def api_authenticate(self, email, password):
        api_url = urljoin(
            settings.BASE_API_URL,
            f"users/authenticate",
        )

        payload = {
            "email": email,
            "password": password,
        }

        try:
            response = requests.post(api_url, json=payload)
            response.raise_for_status()
        except RequestException as err:
            self.set_session_data("auth_error", str(err))
        else:
            key = "token" if response.ok else "auth_error"
            self.set_session_data(key, response.json())

    def set_session_data(self, key, data):
        self.request.session[key] = data


class AuthenticateResultView(generic.TemplateView):
    template_name = "rails/authenticate.result.html"

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        context["token"] = request.session.pop("token", None)
        context["auth_error"] = request.session.pop(
            "auth_error", None
        )
        return self.render_to_response(context)


def prepare_trains(trains: list[dict], key: str):
    return list(
        map(
            parse_datetimes,
            sorted(trains, key=itemgetter(key)),
        )
    )


def parse_datetimes(train: dict):
    train["arrives_at"] = datetime.fromisoformat(
        train["arrives_at"]
    )
    train["departs_at"] = datetime.fromisoformat(
        train["departs_at"]
    )
    return train
