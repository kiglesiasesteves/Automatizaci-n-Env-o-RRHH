from django.core.management.base import BaseCommand
from django.core.mail import send_mail
from yourapp.models import Employee
from datetime import date


class Command(BaseCommand):
    help = 'Envía resumen de vacaciones a cada empleado'

    def handle(self, *args, **kwargs):
        current_year = date.today().year

        for employee in Employee.objects.all():
            taken = employee.vacation_days_taken(current_year)
            remaining = employee.vacation_days_remaining(current_year)

            subject = f"Resumen de Vacaciones {current_year}"
            message = (
                f"Hola {employee.name},\n\n"
                f"Hasta la fecha, has tomado {taken} días de vacaciones este año.\n"
                f"Te quedan {remaining} días disponibles.\n\n"
                "Por favor, planifica tus vacaciones con tiempo.\n\n"
                "Saludos,\nRecursos Humanos"
            )

            send_mail(
                subject=subject,
                message=message,
                from_email="rrhh@tuempresa.com",
                recipient_list=[employee.email],
                fail_silently=False
            )

            self.stdout.write(self.style.SUCCESS(f"Correo enviado a {employee.email}"))
