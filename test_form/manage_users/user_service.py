from django.db import models
from .models import Users
from collections import OrderedDict
from django.db.models.functions import Upper

class UserService(object):
    def __init__(self):
        test = 1

    def get_all(self):
       return  Users.objects.all()


    def get_by_filters(self, filter_details):
        try:

            limit = self.filter_limit(filter_details)
            if limit:
                search = self.filter_search(filter_details)
                sort = self.filter_sort(filter_details)
                offset = int(filter_details["offset"])
                users = Users.objects.filter(email__contains=search).order_by(sort)[offset:offset+limit]
                count = len(Users.objects.filter(email__contains=search).order_by(sort))
            else:
                users = Users.objects.all()
                count = len(users)

            return self._normalize_response(users, count)

        except Exception as e:
            return {
                "total": 0,
                "rows": []
            }

    def filter_search(self, filter_details):
        search = ""
        if "search" in filter_details:
            search = filter_details["search"]
        return search

    def filter_sort(self, filter_details):
        order_by = Upper("email").asc()
        if "sort" in filter_details:
            if str(filter_details["order"]) == "asc":
                order_by = Upper("email").asc()
            else:
                order_by = Upper("email").desc()
        return order_by

    def filter_limit(self, filter_details):
        limit = int(filter_details["limit"])
        if "sort" not in filter_details and "search" not in filter_details and int(filter_details["offset"]) == 0:
            limit = False

        return limit

    def _normalize_rows(self, users):
        rows = []
        for user in users:
            row = OrderedDict()
            row["email"] = user.email
            row["state"] = user.state
            row["city"] = user.city
            row["notes"] = user.notes
            rows.append(row)
        return rows

    def _normalize_response(self, users, count):
        return {
            "total": count,
            "rows": self._normalize_rows(users)
        }
