from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from rest_framework.response import Response
from rest_framework import status
from usuario.models import Usuario as User

def send_email_to_evaluated(evaluated, evaluator, score):
    

    html_render = render_to_string('avaliation.html', context={
        "avaliado": evaluated.first_name,
        "avaliador": evaluator.first_name,
        "avaliacao": score
    })

    email_multiarternative = EmailMultiAlternatives(
        "Sua Avaliação",
        from_email=evaluator.email,
        to=[evaluated.email]
    )

    email_multiarternative.attach_alternative(html_render, "text/html")
    email_multiarternative.send()

    print('email enviado')

    return Response(data={f"email enviado para o colaborador"}, status=status.HTTP_200_OK)

    