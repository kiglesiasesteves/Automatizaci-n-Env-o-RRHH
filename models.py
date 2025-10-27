from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    year_vacation_days = models.IntegerField(default=22)  # Asignación anual

    def __str__(self):
        return self.name

    def vacation_days_taken(self, year=None):
        if not year:
            from datetime import date
            year = date.today().year
        return sum(record.days_taken for record in self.vacationrecord_set.filter(date__year=year))

    def vacation_days_remaining(self, year=None):
        return self.year_vacation_days - self.vacation_days_taken(year)


class VacationRecord(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    date = models.DateField()
    days_taken = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.employee.name} - {self.days_taken} días - {self.date}"
