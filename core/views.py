from django.shortcuts import render, redirect  #  funciones para renderizar plantillas y redirigir URLs
from django.template.loader import render_to_string  #función para renderizar plantillas a cadenas
from django.core.mail import EmailMessage  #clase para crear y enviar correos electrónicos
from django.conf import settings  #la configuración del proyecto Django
from django.contrib import messages  #el sistema de mensajes de Django

def index(request):  # Define la vista para la página principal (index.html)
    return render(request, 'index.html')  # Renderiza la plantilla index.html

def contact(request):  # Define la vista para el formulario de contacto

    if request.method == 'POST':  # Verifica si la solicitud es POST (envío de formulario)
        name = request.POST['name']  # Obtiene el valor del campo 'name' del formulario
        email = request.POST['email']  # Obtiene el valor del campo 'email' del formulario
        subject = request.POST['subject']  # Obtiene el valor del campo 'subject' del formulario
        message = request.POST['message']  # Obtiene el valor del campo 'message' del formulario

        template = render_to_string('email-template.html', {  # Renderiza la plantilla 'email-template.html' con los datos del formulario
            'name': name,  # Pasa el nombre al contexto de la plantilla
            'email': email,  # Pasa el email al contexto de la plantilla
            'subject': subject,  # Pasa el asunto al contexto de la plantilla
            'message': message  # Pasa el mensaje al contexto de la plantilla
        })

        emailSender = EmailMessage(  # Crea un objeto EmailMessage para el correo electrónico
            subject,  # Asunto del correo
            template,  # Cuerpo del correo (HTML)
            settings.EMAIL_HOST_USER,  # Remitente del correo (obtenido de la configuración)
            ['correo1@correo.com','correo2@correo.com']  # Lista de destinatarios
        )
        emailSender.content_subtype = 'html'  # Establece el subtipo de contenido a HTML
        emailSender.fail_silently = False  # No ignora los errores al enviar el correo (para desarrollo)
        emailSender.send()  # Envía el correo electrónico

        messages.success(request, 'El correo electrónico se envió correctamente')  # Muestra un mensaje de éxito
        return redirect('index')  # Redirige a la página principal (index)
    else: # Si la solicitud no es POST, podrías manejarla de otra forma, por ejemplo, mostrando el formulario.
        return render(request, 'contact.html') # Esto asume que tienes un template 'contact.html' para el formulario.