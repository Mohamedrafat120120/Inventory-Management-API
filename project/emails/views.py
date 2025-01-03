from rest_framework import generics
from .models import Consult
from .serializers import ConsultSerializer
from django.core.mail import EmailMessage


class ConsultViewSet(generics.CreateAPIView):
    queryset = Consult.objects.all()
    serializer_class = ConsultSerializer


def send_email(request):
    email = EmailMessage(
        'Title',
        (ConsultSerializer.name, ConsultSerializer.email, ConsultSerializer.phone),
        'my-email',
        ['my-receive-email']
    )
    email.attach_file(ConsultSerializer.file)
    email.send()